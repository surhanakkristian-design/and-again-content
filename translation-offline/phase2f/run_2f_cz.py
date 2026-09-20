#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phase 2E TASK B: finish the CZECH half of the 2C selection (4,064 rows, cz_0001..cz_0005).

This is phase2c/run_2c.py restricted to Czech, with SIX changes and no others (item numbers are the
brief's):

 1. PAR = 2 (2C used 4).  The concurrency is recorded in the ledger and in every batch sidecar.
 2. 429 / BACK-OFF.  A literal "429" anywhere in the CLI stdout/stderr, or a non-zero exit, is retried
    after 60 * 2**attempt seconds + uniform jitter in [0, 30) s, at most 3 retries.  Every retry writes a
    log line containing RETRY and counted:false (the attempt is NOT counted as a completed session; its
    tokens ARE added to the spend, because they were really spent).  After the 3rd retry the session is
    marked GIVEUP in the ledger and the run moves on - a session never hangs the run.
 3. PER-SESSION CIRCUIT BREAKER (2C defect 1: one session burned 436,644 tokens over 18,839 s).
      wall   : the subprocess is killed at max(900 s, 3 x running mean wall for its kind)  -> GIVEUP.
      tokens : max(200,000, 3 x running mean tokens for its kind).  Token usage is only observable when
               the CLI returns, so this ceiling is enforced on return: the session is marked
               GIVEUP-TOKENS, is never retried, and stops contributing to the running means.  Its rows
               are kept if they parsed (they are already paid for); the wall breaker is what actually
               makes the 2C burn impossible, since 18,839 s >> 900 s.
 4. MID-RUN THROUGHPUT GUARD (the single most important requirement; 2C ran five hours at 25 tok/s
    because nothing checked).  A monitor thread samples every 60 s and computes completed tokens / wall
    over a trailing 300 s window.  If that rate stays under 60 tok/s for 20 consecutive samples
    (= 20 continuous minutes) the stop reason is written, spawning stops, in-flight sessions are allowed
    to finish or time out, and the process exits cleanly (code 0) so the report can be written.
 5. PER-BATCH PROJECTION GATE.  After every completed batch: cumulative tokens and the projected total
    are printed; STOP if the projected wall exceeds 4 h, STOP if the projected total tokens exceed --cap.
    Both projections use only rows actually paid for in THIS process (adopted 2C sessions are free and
    would otherwise flatter the estimate).
 6. lk.  Task A established that the v-session lk_verdict is not trustworthy as a single sample.  The
    prompt is therefore UNCHANGED - VPROMPT("cz") is reused verbatim from 2C, lk is still authored by the
    v session - and every batch additionally carries "lk_needs_dedicated_pass": true in its sidecar, its
    gate record and the ledger, so Czech lk is corrected by the same dedicated pass Task A runs for
    Slovak rather than trusted from the v session.

REUSE.  phase2c/ is INPUT, READ ONLY.  The 13 finished Czech sessions phase2c/out/sessions/cz_0001_s*.json
are COPIED (never moved) into phase2e/out/sessions/ at startup, asserted complete per session id before
anything is spawned, and logged as "SKIP-DONE <sid> ... 0 tokens".

Everything else is 2C verbatim: prompts, selection, derivation, assembly, alt, N = 100 rows/session,
1,000 rows/batch, GATE 3 after every batch at bar 12 % on AG v4 and reader_nom, g4 recorded as a
DIAGNOSTIC ONLY and never gated, a batch written only when every one of its sessions is complete.

0 Gemini calls.  0 DB access.  No deploy, no migration, no push.  Writes only inside phase2e/.
The OAuth token is never printed or logged.  --dry-run uses out_dry/ and makes 0 model calls.
"""
import os, re, sys, csv, json, time, random, shutil, hashlib, zipfile, subprocess, threading, collections
import concurrent.futures as cf
sys.dont_write_bytecode = True

H = os.path.dirname(os.path.abspath(__file__))                 # .../translation-offline/phase2e
BASE = os.path.dirname(H)                                      # .../translation-offline
REPO = os.path.dirname(BASE)                                   # .../and-again-content
C2 = os.path.join(BASE, "phase2c")                             # INPUT, read only
D2 = os.path.join(BASE, "phase2d")                             # INPUT, read only
E2 = os.path.join(BASE, "phase2e")                             # INPUT, read only (2F adopts from here)
B2 = os.path.join(BASE, "phase2b")
for p in (C2, B2):
    if p not in sys.path:
        sys.path.insert(0, p)
BIN = os.path.expanduser("~/Library/Application Support/Claude/claude-code/2.1.275/claude.app/Contents/MacOS/claude")
MODEL = "opus"
PAR = 2                          # change 1
NSESS = 100                      # rows per session
NBATCH = 1000                    # rows per batch
CAP = 6_000_000                  # default; the real budget is passed as --cap
EST = {"v": 95_000, "rw": 60_000}
WALL_CAP_S = 4 * 3600            # change 5: 4 h, not 5 h
GATE3_BAR = 12.0
LK_ADJUST_FLOOR = 5.0
LK_NEEDS_DEDICATED_PASS = True   # change 6
MAX_RETRY = 3                    # 2F change 2: ceiling 5 -> 3 (2E defect 2).  With the SS1 batch rule a
                                 # give-up costs 100 rows, so attempts 4 and 5 bought nothing and cost
                                 # about 190,000 tokens across the two refused s04 chunks.
CB_WALL_FLOOR_S = 900            # change 3
CB_TOK_FLOOR = 200_000
CB_MULT = 3
TP_WINDOW_S = 300                # change 4
TP_MIN_TOK_S = 60.0
TP_MIN_SAMPLES = 20              # 2F change 1: the floor is back at 60 tok/s over 20 minutes because the
                                 # guard's clock now EXCLUDES back-off sleep ENTIRELY (SLEEPS /
                                 # sleep_overlap below).  2E raised this to 45 min to try to outlast one
                                 # ladder and was soft-stopped anyway by two ladders in one run: the
                                 # defect was measuring the sleep, not the length of the floor.
LANGS = ("cz",)

# ---------------------------------------------------------------- argv (nothing is ignored)
def parse_argv(argv):
    a = {"all": False, "batches": [], "only": [], "dry": False, "cap": CAP, "par": PAR, "max_sessions": None,
         "ignore_stop": False, "self_test": False}
    i = 0
    while i < len(argv):
        x = argv[i]
        if x == "--all": a["all"] = True
        elif x == "--dry-run": a["dry"] = True
        elif x == "--self-test": a["self_test"] = True
        elif x == "--ignore-stop-file": a["ignore_stop"] = True
        elif x == "--batch": i += 1; a["batches"].append(argv[i])
        elif x == "--only": i += 1; a["only"].append(argv[i])
        elif x == "--cap": i += 1; a["cap"] = int(argv[i])
        elif x == "--par": i += 1; a["par"] = int(argv[i])
        elif x == "--max-sessions": i += 1; a["max_sessions"] = int(argv[i])
        else:
            sys.stderr.write("FATAL: unknown argument %r; refusing to run (no argv is ever ignored)\n" % x)
            sys.exit(2)
        i += 1
    if a["dry"]:
        a["self_test"] = True
    if not a["all"] and not a["batches"]:
        sys.stderr.write("FATAL: nothing selected; pass --all or --batch <id>\n"); sys.exit(2)
    return a
A = parse_argv(sys.argv[1:])
OUT = os.path.join(H, "out_dry" if A["dry"] else "out")
SESSDIR = os.path.join(OUT, "sessions")
os.makedirs(SESSDIR, exist_ok=True)
DRY = "_dry" if A["dry"] else ""
STOPPFX = "STOPDRY" if A["dry"] else "STOP"
LEDGER = os.path.join(H, "ledger_2f_cz%s.json" % DRY)
GATES = os.path.join(H, "gates_2f_cz%s.json" % DRY)
LOGP = os.path.join(H, "run_2f_cz%s.log" % DRY)
DEFECTS = os.path.join(H, "DEFECTS_run_2f_cz%s.md" % DRY)

LOG = open(LOGP, "a", buffering=1, encoding="utf-8")
PRINTLOCK = threading.Lock()
def log(*a):
    s = time.strftime("%Y-%m-%d %H:%M:%S ") + " ".join(str(x) for x in a)
    with PRINTLOCK:
        LOG.write(s + "\n"); print(s, flush=True)
def defect(s):
    with PRINTLOCK:
        open(DEFECTS, "a", encoding="utf-8").write(time.strftime("%Y-%m-%d %H:%M ") + s + "\n")
    log("DEFECT", s)

# ---------------------------------------------------------------- git (add + commit only; never push)
GITLOCK = threading.Lock()
def commit(paths, msg):
    if A["dry"]:
        return
    paths = [p for p in paths if os.path.exists(p)]
    if not paths:
        return
    with GITLOCK:
        rel = [os.path.relpath(p, REPO) for p in paths]
        subprocess.run(["git", "add", "--"] + rel, cwd=REPO, capture_output=True)
        r = subprocess.run(["git", "commit", "-q", "-m",
                            msg + "\n\nCo-Authored-By: Claude Opus 5 <noreply@anthropic.com>", "--"] + rel,
                           cwd=REPO, capture_output=True, text=True)
        if r.returncode and b"nothing to commit" not in (r.stdout or "").encode():
            log("GIT-NOTE", rel[:3], (r.stdout or r.stderr)[-160:].replace("\n", " "))

def write_stop_file(reason, detail):
    fn = os.path.join(H, "%s_%s.md" % (STOPPFX, reason))
    open(fn, "w", encoding="utf-8").write(
        "# Phase 2E (Czech) STOP: %s\n\n%s\n\nWritten %s.\nSpent so far: %s headless tokens, %.1f s wall, par %d.\n"
        % (reason, detail, time.strftime("%Y-%m-%d %H:%M:%S"), STATE["tok"], time.time() - STATE["t0"], A["par"]))
    return fn

def stop(reason, detail):
    """Hard stop: a decision was breached. Everything finished is already committed."""
    fn = write_stop_file(reason, detail)
    log("STOP", reason, detail)
    save_ledger()
    commit([fn, LEDGER, GATES, LOGP], "Phase 2F: STOP %s" % reason)
    sys.exit(3)

def soft_stop(reason, detail):
    """Change 4: stop spawning, let in-flight sessions finish, exit cleanly so the report can be written."""
    with LOCK:
        if STATE["stop_spawn"]:
            return
        STATE["stop_spawn"] = "%s: %s" % (reason, detail)
    fn = write_stop_file(reason, detail)
    log("SOFT-STOP", reason, detail, "- no further sessions will be spawned; in-flight sessions may finish")
    commit([fn, LOGP], "Phase 2F: soft stop %s" % reason)

# ---------------------------------------------------------------- prompts (2C text, reused verbatim)
LNAME = {"sk": "Slovak", "cz": "Czech"}
DEF_2A = """Definitions (Slovak): tf = time frame of the MAIN clause: past / present / future (a perfective verb in
present form = future). person = person+number of the main-clause finite verb: 1sg 2sg 3sg 1pl 2pl 3pl.
subject = the overt NOMINATIVE subject NP of the main-clause finite verb, copied verbatim from the Slovak
(it may stand anywhere in the clause, not only first), or null if the subject is dropped (pro-drop) or absent.
voice = active_agent (overt nominative subject) / active_prodrop (subject dropped, recoverable from the verb) /
impersonal (no subject possible, e.g. "je známe", "prší") / passive (byť + passive participle, or reflexive passive).
agent_nom = true iff voice == active_agent. embedded_agents = overt nominative subjects of subordinate clauses (verbatim list)."""
REWRITE_2A = """You are the arm-B rewrite agent (1J rule) of a Slovak->English translation-checking pipeline.
For each Slovak sentence: if the MAIN clause has a dropped (pro-drop) subject, insert exactly ONE nominative
personal pronoun (ja, ty, on, ona, ono, my, vy, oni, ony) agreeing with the finite verb, at the natural
position; change NOTHING else (no other word added, removed or altered). If the main clause already has an
overt subject but a subordinate clause has a dropped subject, you may insert the pronoun there (where="embedded").
If the subject is overt or the clause is impersonal, leave the sentence untouched. Use the English reference
only to choose gender/person. Machine check afterwards: new tokens = old tokens + exactly the pronoun.
Reply with ONLY a JSON array, one object per sentence:
{"n": int, "action": "R"|"U", "sk_new": str, "pronoun": str|null, "where": "main"|"embedded"|null, "reason": str}
(reason for U: explicit_subject | impersonal | other). No prose, no code fences.
Sentences:
"""
REWRITE = (REWRITE_2A
           .replace("of a Slovak->English translation-checking pipeline.\nFor each Slovak sentence:",
                    "of a Slovak/Czech->English translation-checking pipeline.\nFor each sentence (\"lang\": sk = Slovak, cz = Czech; the text is in field \"sk\" for both):")
           .replace("personal pronoun (ja, ty, on, ona, ono, my, vy, oni, ony) agreeing",
                    "personal pronoun (Slovak: ja, ty, on, ona, ono, my, vy, oni, ony; Czech: já, ty, on, ona, ono, my, vy, oni, ony) agreeing"))
assert REWRITE != REWRITE_2A and REWRITE.count("Czech") == 3

def DEF(lang):
    if lang == "sk":
        return DEF_2A
    return (DEF_2A.replace("(Slovak)", "(Czech)").replace("from the Slovak", "from the Czech")
            .replace('"je známe"', '"je známo"').replace("byť +", "být +"))

def VPROMPT(lang):
    """The 2B v prompt, widened: it now also authors the lk CORRECTION and every field the script may not author.
    CHANGE 6: reused VERBATIM from 2C. lk stays exactly as 2C writes it; the dedicated lk pass corrects it."""
    L = LNAME[lang]
    return f"""You are the annotation agent of a {L}->English translation-checking pipeline. For each row you get the
{L} sentence "src", the English reference "en", the exercise's stored key phrase "lk_supplied", the exercise topic, and
the three script-derived fields "person" / "number" / "perfective_present" (null = the script abstained; you must author it).

Write, per row:
1. v = 1-2 acceptable English translations of src; v[0] MUST be the reference en verbatim; add a second only if a clearly
   different acceptable translation exists.
2. lk = the key verb phrase of each v (one entry per v entry), each a VERBATIM span of the matching v.
   lk_supplied is the exercise's stored answer and is OFTEN WRONG: about one row in five needs the span trimmed or extended.
   DO NOT COPY lk_supplied BY DEFAULT. Judge it, then set lk[0] to the correct span of v[0] and report:
   lk_verdict = "exact" if lk[0] is character-for-character lk_supplied, "adjusted" if you changed it in any way;
   lk_reason = one clause (<= 8 words) saying why.
3. voice, subject, agent_nom, embedded_agents - for the MAIN clause of src.
4. gender, tf, tense_open, fragment, main_sentence_index.
5. person, number, perfective_present - ONLY on rows where the supplied value is null.

{DEF(lang)}
number = number of the main-clause finite verb (sg / pl). gender = grammatical gender of the main-clause subject as the
sentence marks it (subject noun or pronoun, past participle, predicative adjective): m / f / n, or null if not marked.
tense_open = true iff more than one English tense is acceptable. perfective_present = true iff the main-clause finite verb
is perfective in present form. fragment = true iff the sentence has no finite main verb. main_sentence_index = if the item
contains more than one sentence, the 0-based index of the sentence whose main clause you labelled (0 otherwise).

Reply with ONLY a JSON array, one object per row, no prose, no fences:
{{"n": int, "v": [str], "lk": [str], "lk_verdict": "exact"|"adjusted", "lk_reason": str, "voice": str,
 "subject": str|null, "agent_nom": bool, "embedded_agents": [str], "gender": "m"|"f"|"n"|null, "tf": str,
 "tense_open": bool, "fragment": bool, "main_sentence_index": int,
 "person": str (only if supplied null), "number": str (only if supplied null), "perfective_present": bool (only if supplied null)}}
Rows:
"""
PROMPT_SHA = {k: hashlib.sha256(v.encode()).hexdigest()[:16]
              for k, v in {"v_cz": VPROMPT("cz"), "rw": REWRITE}.items()}

REQ_V = ["v", "lk", "lk_verdict", "voice", "subject", "agent_nom", "gender", "tf", "tense_open"]

# ---------------------------------------------------------------- data + script derivation (from phase2c)
import derive_2c                                                    # noqa: E402  (GATE 1 entry point)

def load_selection():
    rows = [json.loads(l) for l in open(os.path.join(C2, "selection_2c.jsonl"), encoding="utf-8") if l.strip()]
    assert len(rows) == 8128, "selection_2c.jsonl has %d rows, expected 8128" % len(rows)
    return rows
SEL = load_selection()
BYN = {r["n"]: r for r in SEL}

def batches_of(rows):
    out = []
    for lang in LANGS:                                              # Czech only
        rs = [r for r in rows if r["lang"] == lang]
        for i in range(0, len(rs), NBATCH):
            out.append(("%s_%04d" % (lang, i // NBATCH + 1), lang, rs[i:i + NBATCH]))
    return out
BATCHES = batches_of(SEL)
BATCH_IDS = [b[0] for b in BATCHES]
assert BATCH_IDS == ["cz_0001", "cz_0002", "cz_0003", "cz_0004", "cz_0005"], BATCH_IDS
if A["batches"]:
    bad = [b for b in A["batches"] if b not in BATCH_IDS]
    if bad:
        sys.stderr.write("FATAL: unknown batch id(s) %s; known: %s\n" % (bad, BATCH_IDS)); sys.exit(2)
SELECTED = [b for b in BATCHES if A["all"] or b[0] in A["batches"]]
MATCHED = set()
SID_RE = re.compile(r"^cz_\d{4}_s\d{2}_(v|rw)$")
for _o in A["only"]:
    if not SID_RE.match(_o) or _o.rsplit("_s", 1)[0] not in [x[0] for x in SELECTED]:
        sys.stderr.write("FATAL: --only %r is not a session id of a selected batch; refusing to run\n" % _o); sys.exit(2)

def line(o): return json.dumps(o, ensure_ascii=False)
def chunks(batch_rows): return [batch_rows[i:i + NSESS] for i in range(0, len(batch_rows), NSESS)]

# ---------------------------------------------------------------- alt (alt_map_2b.py classifier, reused)
_ALT = {"ready": False}
STOPW = set("""a an the and or but if so than then that this these those there here it its i me my mine you your yours he him his she
her hers we us our ours they them their theirs who whom whose which what when where why how not no nor of to in on at by for
with from into onto about as up down out off over under again very too also just only be am is are was were been being have
has had having do does did doing will would shall should can could may might must let s t d ll re ve m don doesn didn isn aren
wasn weren won wouldn can't cannot all any some each every both either neither one ones own same such more most much many
few other another""".split())
def lemmas(t):
    c = [t]
    for suf, rep in (("ies", "y"), ("ied", "y"), ("ier", "y"), ("iest", "y"), ("ing", ""), ("ing", "e"), ("ed", ""), ("ed", "e"),
                     ("es", ""), ("s", ""), ("er", ""), ("est", ""), ("ly", "")):
        if t.endswith(suf) and len(t) - len(suf) >= 3:
            b = t[: -len(suf)] + rep; c.append(b)
            if len(b) > 3 and b[-1] == b[-2] and not rep: c.append(b[:-1])
    return list(dict.fromkeys(c))
def alt_build():
    try:
        SY = os.path.join(BASE, "phase1b", "synonyms")
        table = json.load(open(os.path.join(SY, "table.json")))["groups"]
        forms = json.load(open(os.path.join(SY, "forms.json")))["groups"]
        ids = {g["id"] for g in table}
        member, surface, phrases = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)
        for g in table:
            for m in g["m"]:
                (phrases if " " in m else member)[m.lower()].add(g["id"])
        for gid, g in forms.items():
            if gid not in ids: continue
            for lst in (g.get("forms") or {}).values():
                for s in lst:
                    (phrases if " " in s else surface)[s.lower()].add(gid)
        cand = collections.defaultdict(set)
        for g in json.load(open(os.path.join(SY, "ng_phase1c.json")))["groups"]:
            ms = [m.lower() for m in g["m"]]
            for m in ms:
                cand[m].update(x for x in ms if x != m)
        known = set(w.strip().lower() for w in open(os.path.join(BASE, "wordlist", "en_words.txt"), encoding="utf-8"))
        pfirst = collections.defaultdict(list)
        for ph in phrases: pfirst[ph.split()[0]].append(ph)
        _ALT.update(member={k: sorted(v) for k, v in member.items()}, surface={k: sorted(v) for k, v in surface.items()},
                    phrases={k: sorted(v) for k, v in phrases.items()}, pfirst=dict(pfirst), cand={k: sorted(v) for k, v in cand.items()},
                    known=known, vocab=set(member) | set(surface), ready=True, groups=len(table))
        log("ALT index", len(member), "members", len(surface), "surface", len(phrases), "phrases", len(cand), "candidates")
    except Exception as ex:
        defect("alt index could not be built (%r); alt written empty" % ex)
        _ALT.update(ready=False)
def alt_for(en):
    if not _ALT.get("ready"):
        return []
    s = (en or "").lower().replace("’", "'")
    covered = {}
    present = set(re.findall(r"[a-z']+", s))
    for w0 in present & set(_ALT["pfirst"]):
        for p in _ALT["pfirst"][w0]:
            if re.search(r"\b" + re.escape(p) + r"\b", s):
                for w in p.split(): covered[w] = list(_ALT["phrases"][p])
    items = []
    for t in [x.split("'")[0] for x in re.findall(r"[a-z]+(?:'[a-z]+)?", s)]:
        if t in STOPW or len(t) < 2: continue
        L = lemmas(t); gs = set(covered.get(t, []))
        for l in L:
            gs |= set(_ALT["member"].get(l, [])) | set(_ALT["surface"].get(l, []))
        if gs:
            cls, info = "mapped", sorted(gs)
        else:
            c = set()
            for l in L: c |= {x for x in _ALT["cand"].get(l, []) if x in _ALT["vocab"]}
            cls, info = ("propose_new", sorted(c)[:5]) if (c and any(l in _ALT["known"] for l in L)) else ("unmapped", [])
        items.append({"tok": t, "class": cls, "groups_or_candidates": info})
    return items

# ---------------------------------------------------------------- ledger / budget
STATE = {"tok": 0, "inflight": 0, "t0": time.time(), "rows_done": 0, "rows_paid": 0, "sessions": {},
         "kind": collections.defaultdict(lambda: [0, 0, 0.0]), "stop_spawn": None, "giveups": [], "retries": 0}
LOCK = threading.Lock()
def load_ledger():
    if os.path.exists(LEDGER):
        try:
            d = json.load(open(LEDGER, encoding="utf-8"))
            STATE["sessions"] = d.get("sessions", {})
            STATE["tok"] = sum(s.get("tokens", 0) for s in STATE["sessions"].values())
            for s in STATE["sessions"].values():
                if s.get("adopted") or s.get("status", "").startswith("GIVEUP"):
                    continue
                k = s.get("kind", "v")
                STATE["kind"][k][0] += 1
                STATE["kind"][k][1] += s.get("tokens", 0)
                STATE["kind"][k][2] += s.get("wall_s", 0.0)
        except Exception as ex:
            defect("ledger unreadable (%r); refusing to run rather than lose the budget count" % ex); sys.exit(2)
def save_ledger():
    if A["dry"]:
        return
    d = {"cap": A["cap"], "spent": STATE["tok"], "par": A["par"], "concurrency": A["par"],
         "updated": time.strftime("%Y-%m-%dT%H:%M:%S"), "wall_s_this_process": round(time.time() - STATE["t0"], 1),
         "lk_needs_dedicated_pass": LK_NEEDS_DEDICATED_PASS,
         "circuit_breaker": {"wall_floor_s": CB_WALL_FLOOR_S, "token_floor": CB_TOK_FLOOR, "mult": CB_MULT},
         "throughput_guard": {"window_s": TP_WINDOW_S, "min_tok_per_s": TP_MIN_TOK_S, "min_minutes": TP_MIN_SAMPLES},
         "retries": STATE["retries"], "giveups": STATE["giveups"], "stop_spawn": STATE["stop_spawn"],
         "by_kind": {k: {"sessions": v[0], "tokens": v[1], "wall_s": round(v[2], 1),
                         "mean_tokens": round(v[1] / v[0], 1) if v[0] else None,
                         "mean_wall_s": round(v[2] / v[0], 1) if v[0] else None}
                     for k, v in STATE["kind"].items()},
         "sessions": STATE["sessions"]}
    tmp = LEDGER + ".tmp"
    json.dump(d, open(tmp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    os.replace(tmp, LEDGER)
def est_for(kind):
    n, tk, _w = STATE["kind"][kind]
    return round(tk / n) if n >= 2 else EST[kind]
def usage_total(m): return sum(m.get(k) or 0 for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens"))

# ---------------------------------------------------------------- change 2: back-off
def should_retry(exit_code, out, err):
    """A literal 429 anywhere in the CLI output, or a non-zero exit."""
    blob = (out or "") + "\n" + (err or "")
    return ("429" in blob) or (exit_code != 0)
def backoff_sleep_s(attempt, rnd=None):
    rnd = rnd or random
    return 60 * (2 ** attempt) + rnd.uniform(0, 30)

# ---------------------------------------------------------------- change 3: per-session circuit breaker
def circuit_limits(kind):
    n, tk, w = STATE["kind"][kind]
    wall = max(CB_WALL_FLOOR_S, CB_MULT * (w / n)) if n >= 2 else float(CB_WALL_FLOOR_S)
    tok = max(CB_TOK_FLOOR, CB_MULT * (tk / n)) if n >= 2 else float(CB_TOK_FLOOR)
    return wall, tok

# ---------------------------------------------------------------- 2F change 1: the back-off sleep ledger
# Every `counted:false` back-off sleep is recorded as an interval (t0, t1).  The throughput guard
# subtracts the part of those intervals that falls inside its trailing window from elapsed seconds
# BEFORE computing tok/s, so time spent asleep is not measured as throughput at all.  Intervals are
# MERGED before summing: at PAR = 2 two sessions can sleep at once, and double counting could drive the
# corrected clock negative.
SLEEPS = []
SLEEPLOCK = threading.Lock()
def record_sleep(t0, t1):
    if t1 > t0:
        with SLEEPLOCK:
            SLEEPS.append((t0, t1))
def sleep_overlap(a, b):
    """Seconds of recorded back-off sleep inside [a, b], overlapping intervals counted once."""
    with SLEEPLOCK:
        iv = sorted(SLEEPS)
    tot, cur0, cur1 = 0.0, None, None
    for s0, s1 in iv:
        lo, hi = max(a, s0), min(b, s1)
        if hi <= lo:
            continue
        if cur1 is None or lo > cur1:
            if cur1 is not None: tot += cur1 - cur0
            cur0, cur1 = lo, hi
        else:
            cur1 = max(cur1, hi)
    if cur1 is not None: tot += cur1 - cur0
    return tot

# ---------------------------------------------------------------- change 4: throughput guard
class ThroughputGuard(object):
    def __init__(self, window_s=TP_WINDOW_S, min_rate=TP_MIN_TOK_S, need=TP_MIN_SAMPLES):
        self.window_s, self.min_rate, self.need = window_s, min_rate, need
        self.samples = collections.deque(); self.low = 0; self.reason = None; self.rate = None; self.dt = None
        self.unmeasurable = 0                              # 2F change 3: windows with no completion in flight
    def sample(self, t, tok):
        self.samples.append((t, tok))
        while len(self.samples) > 1 and t - self.samples[0][0] > self.window_s:
            self.samples.popleft()
        t0, k0 = self.samples[0]
        dt = (t - t0) - sleep_overlap(t0, t)               # 2F change 1: sleep is not measured at all
        self.dt = dt
        if dt <= 0:                                        # window was entirely back-off sleep (or worse,
            return self.reason                             # rounding); the guard CANNOT fire on it
        self.rate = (tok - k0) / dt
        # 2F change 3: a window with NO session completion while work is IN FLIGHT is UNMEASURABLE.
        # STATE["tok"] only moves when a session RETURNS, so one long-running session reads as 0.0 tok/s
        # while the pool is in fact working - that is what soft-stopped 2F Part 1 at 00:13:25 with
        # cz_0003_s04_v still out.  A pool that is genuinely STUCK is the CIRCUIT BREAKER's job
        # (per-session wall and token floors, 3x the running mean).  This guard exists to catch a pool
        # that IS returning work far too slowly - 2C's five hours at 25 tok/s - and that case still
        # fires, because there tok rises.  Do not increment the streak, do not reset it, do not fire.
        if (tok - k0) <= 0 and STATE["inflight"] > 0:
            self.unmeasurable += 1
            return self.reason
        self.low = self.low + 1 if self.rate < self.min_rate else 0
        if self.low >= self.need and not self.reason:
            self.reason = ("measured throughput %.1f tok/s stayed under %.0f tok/s for %d consecutive minutes "
                           "(trailing %d s window)" % (self.rate, self.min_rate, self.low, self.window_s))
        return self.reason
GUARD = ThroughputGuard()
def monitor_loop():
    while not STATE.get("finished"):
        time.sleep(60)
        if STATE.get("finished"):
            return
        with LOCK:
            tok = STATE["tok"]
        r = GUARD.sample(time.time(), tok)
        log("THROUGHPUT", "rate %.1f tok/s" % (GUARD.rate or 0.0), "low_streak", GUARD.low, "cum_tok", tok,
            "inflight", STATE["inflight"], "measured_window_s %.0f" % (GUARD.dt if GUARD.dt is not None else -1),
            "unmeasurable_windows", GUARD.unmeasurable,
            "backoff_sleep_excluded:true")
        if r:
            soft_stop("throughput_guard", r + ".\n\n2C ran five hours at 25 tok/s because nothing checked; this run "
                                              "stops spawning instead. In-flight sessions finish or hit the circuit "
                                              "breaker, everything complete is committed, resume with the same command.")
            return

# ---------------------------------------------------------------- change 5: projection gate
def projection(rows_paid, rows_left, tok, elapsed):
    if rows_paid <= 0:
        return None
    tpr, spr = tok / float(rows_paid), elapsed / float(rows_paid)
    return {"rows_paid": rows_paid, "rows_left": rows_left, "tok_per_row": round(tpr, 1), "s_per_row": round(spr, 2),
            "cum_tokens": tok, "projected_total_tokens": int(tok + tpr * rows_left),
            "projected_total_s": round(elapsed + spr * rows_left, 1),
            "projected_total_h": round((elapsed + spr * rows_left) / 3600.0, 2)}

# ---------------------------------------------------------------- headless session
ENV = dict(os.environ)
def load_token():
    if not ENV.get("CLAUDE_CODE_OAUTH_TOKEN"):
        ENV["CLAUDE_CODE_OAUTH_TOKEN"] = subprocess.run(
            ["zsh", "-ic", 'printf %s "$CLAUDE_CODE_OAUTH_TOKEN"'], capture_output=True, text=True).stdout.strip()
    if not ENV.get("CLAUDE_CODE_OAUTH_TOKEN"):
        stop("no_oauth_token", "CLAUDE_CODE_OAUTH_TOKEN is empty; 0 sessions spent, 0 cost. Unblock: `claude auth login` "
                               "with the bundled binary, then re-run the same command.")

def sess_path(sid): return os.path.join(SESSDIR, sid + ".json")
def sess_complete(sid, want_ns):
    fn = sess_path(sid)
    if not os.path.exists(fn):
        return None
    try:
        d = json.load(open(fn, encoding="utf-8"))
    except Exception:
        return None
    rows = d.get("rows")
    if not isinstance(rows, list) or (d.get("meta") or {}).get("exit") != 0:
        return None
    got = {o.get("n") for o in rows if isinstance(o, dict)}
    if not set(want_ns) <= got:
        return None
    return d

# ---------------------------------------------------------------- reuse of the 13 finished 2C Czech sessions
def _v_want():
    """n-lists of every v session, computed from the selection alone (no derivation needed)."""
    w = {}
    for bid, lang, rows in BATCHES:
        for k, c in enumerate(chunks(rows), 1):
            w["%s_s%02d_v" % (bid, k)] = [r["n"] for r in c]
    return w
V_WANT = _v_want()

def adopt_prior_sessions():
    """phase2c/ and phase2e/ are READ-ONLY INPUT: COPY (never move) every FINISHED cz session file into
    phase2e/out/sessions/.  phase2e is searched first (it already holds 2C's own 13 copies).  A file that
    does not parse, did not exit 0, or does not cover its whole chunk is NOT adopted: it is treated as
    MISSING and re-run.  That is how cz_0001_s07_v (exit 0, unparsable, 81,602 tok in 2E) comes back."""
    srcs = [("phase2e", os.path.join(E2, "out", "sessions")), ("phase2d", os.path.join(D2, "out", "sessions")),
            ("phase2c", os.path.join(C2, "out", "sessions"))]
    got, rejected, per_src, seen = [], [], collections.Counter(), set()
    for tag, src in srcs:
        if not os.path.isdir(src):
            defect("%s/out/sessions missing; nothing to adopt from it" % tag); continue
        for fn in sorted(os.listdir(src)):
            if not re.match(r"^cz_\d{4}_s\d{2}_(v|rw)\.json$", fn) or fn in seen:
                continue
            sid, sp = fn[:-5], os.path.join(src, fn)
            meta, why = {}, None
            try:
                d = json.load(open(sp, encoding="utf-8"))
                meta = d.get("meta") or {}
                if not isinstance(d.get("rows"), list):    why = "rows is not a list (unparsable result)"
                elif meta.get("exit") != 0:                why = "exit %r" % meta.get("exit")
                elif not d["rows"]:                        why = "0 rows returned"
                elif sid in V_WANT and not set(V_WANT[sid]) <= {o.get("n") for o in d["rows"] if isinstance(o, dict)}:
                    why = "covers %d of %d chunk rows" % (len({o.get("n") for o in d["rows"] if isinstance(o, dict)}
                                                              & set(V_WANT[sid])), len(V_WANT[sid]))
            except Exception as e:
                why = "unparsable file (%s)" % type(e).__name__
            if why:
                rejected.append("%s/%s: %s" % (tag, sid, why))
                defect("prior session NOT adoptable -> treated as MISSING and re-run: %s/%s (%s)" % (tag, sid, why))
                continue
            seen.add(fn)
            dst = os.path.join(SESSDIR, fn)
            if not os.path.exists(dst):
                shutil.copy2(sp, dst)                      # COPY, never move
            per_src[tag] += 1
            got.append(sid)
            STATE["sessions"][sid] = {"kind": meta.get("kind"), "tokens": 0, "tokens_spent_earlier": meta.get("tokens"),
                                      "wall_s": meta.get("wall_s"), "exit": 0, "rows": len(d["rows"]),
                                      "asked": meta.get("rows_asked"), "adopted": True,
                                      "status": "ADOPTED-%s" % tag.upper(), "adopted_from": tag,
                                      "source": os.path.relpath(sp, REPO),
                                      "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}
    log("ADOPT", len(got), "finished Czech sessions COPIED (read only) from", dict(per_src),
        "| 0 tokens each ->", ",".join(sorted(got)))
    if rejected:
        log("ADOPT-REJECTED", len(rejected), "session file(s) NOT adoptable, will be re-run:", " | ".join(rejected))
    commit([LEDGER] + [sess_path(x) for x in got],
           "Phase 2F: adopt %d finished prior Czech sessions (copied; phase2c/phase2e untouched)" % len(got))
    return got

def nranges(ns):
    ns, out = sorted(ns), []
    for n in ns:
        if out and n == out[-1][1] + 1: out[-1][1] = n
        else: out.append([n, n])
    return ["%d-%d" % (a, b) if a != b else str(a) for a, b in out]

DRYVP, DRYAG = {}, {}                  # dry run only: the script's own AG v4 / reader readings
def _dry_voice(n):
    """DRY RUN ONLY. The fake model agrees with the script's AG v4 reading, so GATE 3 scores the plumbing
    (does the gate run, over the right rows, at the right bar) and not a fabricated disagreement."""
    vp = DRYVP.get(n) or {}
    if vp.get("agv4_main_passive") or vp.get("agv4_main_reflex"):
        return "passive"
    return "active_prodrop" if n % 3 == 0 else "active_agent"
def _dry_subject(r):
    """DRY RUN ONLY. Same reason, for the reader_nom leg of GATE 3."""
    return DRYAG.get(r["n"]) or (r["src"].split() or [""])[0]
def fake_rows(kind, rows):
    if kind == "rw":
        return [{"n": r["n"], "action": "U", "sk_new": r["src"], "pronoun": None, "where": None, "reason": "explicit_subject"}
                for r in rows]
    out = []
    for r in rows:
        out.append({"n": r["n"], "v": [r["en"]], "lk": [r.get("correct_answer_en") or ""],
                    "lk_verdict": "adjusted" if r["n"] % 4 == 0 else "exact", "lk_reason": "dry run",
                    "voice": _dry_voice(r["n"]), "subject": _dry_subject(r),
                    "agent_nom": r["n"] % 3 != 0, "embedded_agents": [],
                    "gender": "m", "tf": "present", "tense_open": False, "fragment": False, "main_sentence_index": 0,
                    "person": "3sg", "number": "sg", "perfective_present": False})
    return out

def record_giveup(sid, kind, why, tok, wall, rows_out=None):
    with LOCK:
        STATE["tok"] += tok
        STATE["giveups"].append({"session": sid, "why": why, "tokens": tok, "wall_s": round(wall, 1)})
        STATE["sessions"][sid] = {"kind": kind, "tokens": tok, "wall_s": round(wall, 1), "exit": None,
                                  "rows": len(rows_out or []), "status": "GIVEUP", "why": why,
                                  "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}
        save_ledger()
    log("GIVEUP", sid, kind, why, "tok", tok, "wall", round(wall, 1), "- moving on, the run never hangs")
    commit([LEDGER], "Phase 2F: GIVEUP %s (%s)" % (sid, why))

def session(sid, kind, prompt, rows):
    want = [r["n"] for r in rows]
    have = sess_complete(sid, want)
    if have is not None:                                           # assert per session id BEFORE spawning
        log("SKIP-DONE", sid, kind, len(have["rows"]), "rows already on disk, 0 tokens")
        return sid, have["rows"]
    if A["dry"]:
        rows_out = fake_rows(kind, rows)
        json.dump({"meta": {"session": sid, "kind": kind, "exit": 0, "dry_run": True, "wall_s": 0.0},
                   "prompt": prompt, "result": "", "rows": rows_out},
                  open(sess_path(sid), "w", encoding="utf-8"), ensure_ascii=False)
        log("DRY", sid, kind, len(rows_out), "rows", "prompt_chars", len(prompt))
        return sid, rows_out
    if STATE["stop_spawn"]:
        log("NO-SPAWN", sid, "stop already requested:", STATE["stop_spawn"][:90])
        return sid, ("SKIP", sid, "stop requested")
    e = est_for(kind)
    with LOCK:
        proj = STATE["tok"] + STATE["inflight"] * max(EST.values()) + e
        if proj > A["cap"]:
            return sid, ("STOP", "token_cap", "session %s: %d spent + %d in flight + %d projected > cap %d"
                         % (sid, STATE["tok"], STATE["inflight"] * max(EST.values()), e, A["cap"]))
        STATE["inflight"] += 1
    try:
        t_sess = time.time()
        retry_tok = 0
        p = None
        for attempt in range(MAX_RETRY + 1):
            wall_cap, tok_cap = circuit_limits(kind)
            t0 = time.time()
            try:
                p = subprocess.run([BIN, "-p", prompt, "--output-format", "json", "--max-turns", "12", "--model", MODEL],
                                   capture_output=True, text=True, env=ENV, cwd=H, timeout=wall_cap)
            except subprocess.TimeoutExpired:
                record_giveup(sid, kind, "circuit_breaker_wall: killed at %.0f s (floor %d s, %dx mean)"
                              % (wall_cap, CB_WALL_FLOOR_S, CB_MULT), retry_tok, time.time() - t_sess)
                return sid, ("GIVEUP", sid, "circuit_breaker_wall")
            if should_retry(p.returncode, p.stdout, p.stderr):
                try:
                    ju = (json.loads(p.stdout).get("usage") or {})
                    retry_tok += usage_total(ju)
                except Exception:
                    pass
                with LOCK:
                    STATE["retries"] += 1
                why = "429" if "429" in ((p.stdout or "") + (p.stderr or "")) else "exit %d" % p.returncode
                if attempt < MAX_RETRY:
                    d = backoff_sleep_s(attempt)
                    log("RETRY", sid, kind, "attempt", attempt + 1, "of", MAX_RETRY, "reason", why,
                        "sleep %.1fs" % d, "counted:false")
                    _sl0 = time.time()
                    time.sleep(d)
                    record_sleep(_sl0, time.time())        # 2F change 1: excluded from the guard's clock
                    continue
                record_giveup(sid, kind, "retries_exhausted after %d retries (%s)" % (MAX_RETRY, why),
                              retry_tok, time.time() - t_sess)
                return sid, ("GIVEUP", sid, "retries_exhausted")
            break
        try:
            j = json.loads(p.stdout)
        except Exception:
            j = {"parse_error": p.stdout[-400:],
                 "stderr": re.sub(r"sk-ant-\S+", "sk-ant-REDACTED", p.stderr[-400:])}
        u = j.get("usage", {}) or {}
        wall = round(time.time() - t0, 1)
        meta = {"session": sid, "kind": kind, "exit": p.returncode, "wall_s": wall,
                "num_turns": j.get("num_turns"), "total_cost_usd": j.get("total_cost_usd"), "is_error": j.get("is_error"),
                **{k: u.get(k, 0) for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens")},
                "parse_error": j.get("parse_error"), "stderr": j.get("stderr"), "rows_asked": len(rows),
                "retry_tokens_not_counted_as_session": retry_tok,
                "lk_needs_dedicated_pass": LK_NEEDS_DEDICATED_PASS}
        txt = j.get("result", "") or ""
        try:
            out = json.loads(txt[txt.find("["):txt.rfind("]") + 1])
            out = [o for o in out if isinstance(o, dict) and "n" in o]
        except Exception:
            out = None; meta["result_unparsable"] = txt[:300]
        tok = usage_total(meta)
        meta["tokens"] = tok
        meta["rows_returned"] = len(out or [])
        if out is not None:
            miss = collections.Counter()
            for o in out:
                need = list(REQ_V) if kind == "v" else ["action"]
                if kind == "v":
                    for f in ("person", "number", "perfective_present"):
                        if (DERIVED.get(o["n"], {}).get(f) is None) and f not in o:
                            miss[f] += 1
                for f in need:
                    if f not in o or o[f] is None and f in ("v", "lk", "lk_verdict", "voice", "tf"):
                        miss[f] += 1
            meta["missing_fields"] = dict(miss)
        _wc, tok_cap = circuit_limits(kind)
        over_tok = tok > tok_cap
        if over_tok:
            meta["circuit_breaker_tokens"] = {"tokens": tok, "ceiling": tok_cap}
        json.dump({"meta": meta, "prompt": prompt, "result": txt, "rows": out},
                  open(sess_path(sid), "w", encoding="utf-8"), ensure_ascii=False)
        with LOCK:
            STATE["tok"] += tok + retry_tok
            if not over_tok:
                STATE["kind"][kind][0] += 1; STATE["kind"][kind][1] += tok; STATE["kind"][kind][2] += wall
            STATE["sessions"][sid] = {"kind": kind, "tokens": tok + retry_tok, "wall_s": wall, "exit": p.returncode,
                                      "rows": len(out or []), "asked": len(rows),
                                      "status": "GIVEUP-TOKENS" if over_tok else "OK",
                                      "retry_tokens": retry_tok, "retries": 0,
                                      "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}
            STATE["rows_paid"] += len(rows) if kind == "v" else 0
            save_ledger()
        log("DONE", sid, kind, "exit", p.returncode, "tok", tok, "cum", STATE["tok"], "wall", wall,
            "rows", len(out or []), "/", len(rows), "missing", meta.get("missing_fields"))
        if over_tok:
            defect("%s burned %d tokens > ceiling %.0f (change 3): marked GIVEUP-TOKENS, never retried, excluded "
                   "from the running means; its rows are kept because they are already paid for" % (sid, tok, tok_cap))
        commit([sess_path(sid), LEDGER], "Phase 2F: session %s (%d tok)" % (sid, tok))
        if out is None:
            return sid, ("FAIL", sid, "unparsable/exit %d" % p.returncode)
        return sid, out
    finally:
        with LOCK:
            STATE["inflight"] -= 1

# ---------------------------------------------------------------- assembly (2C verbatim)
def toks(s): return [w.lower() for w in re.findall(r"\w+", s or "")]
def machine_check(old, new, pron):
    a, b = toks(old), toks(new or old); ok = True
    for t in a:
        if t in b: b.remove(t)
        else: ok = False
    return ok and b == [str(pron or "").lower()]
def words(s): return set(re.findall(r"[a-záäčďéěíĺľňóôöŕřšťúůüýž]+", (s or "").lower(), re.I))

DERIVED = {}
def derive_batch(rows):
    d = {}
    for r in rows:
        try:
            d[r["n"]] = derive_2c.derive({"n": r["n"], "lang": r["lang"], "src": r["src"], "en": r["en"], "level": r["level"]},
                                         mode="after")
        except Exception as ex:
            defect("derive crashed on n=%s (%r); row annotated model-only" % (r["n"], ex))
            d[r["n"]] = {"reader": {}, "derived": {}, "voice_paths": {}, "rewrite": {"action": "ABSTAIN", "check": "N/A"}}
        dd = d[r["n"]].get("derived", {})
        DRYVP[r["n"]] = d[r["n"]].get("voice_paths", {}) or {}
        DRYAG[r["n"]] = (d[r["n"]].get("reader") or {}).get("agent")
        DERIVED[r["n"]] = {f: (dd.get(f) or {}).get("value") for f in
                           ("person", "number", "perfective_present", "agent_nom", "gender", "tf", "tense_open", "voice_sk")}
    return d

def assemble(row, drv, mv, rwm):
    n, L = row["n"], row["lang"]
    dd = drv.get("derived", {}); sr = drv.get("rewrite", {}) or {}
    mv = mv or {}
    flags = []
    if not mv: flags.append("model_row_missing")
    if not (row.get("correct_answer_%s" % L) or "").strip(): flags.append("empty_correct_answer")
    get = lambda f: (dd.get(f) or {}).get("value")
    out = {}
    src_of = {}
    for f in ("person", "number", "perfective_present"):
        v = get(f)
        if v is None:
            out[f] = mv.get(f); src_of[f] = "model"
        else:
            out[f] = v; src_of[f] = "script:" + (dd.get(f) or {}).get("source", "?")
    for f in ("voice", "agent_nom", "gender", "tense_open", "tf", "subject", "embedded_agents", "fragment",
              "main_sentence_index"):
        out[f] = mv.get(f); src_of[f] = "model"
    act = sr.get("action", "ABSTAIN")
    if act in ("U", "R"):
        ok = sr.get("check") == "PASS"
        rw = {"action": act, "by": "script", "pronoun": sr.get("pronoun"), "where": sr.get("where"),
              "machine_check": ok if act == "R" else True,
              "text": sr.get("new") if (act == "R" and ok) else row["src"], "reason": sr.get("reason")}
        if act == "R" and not ok: flags.append("script_rewrite_machine_check_fail")
    else:
        o = rwm or {}
        mc = o.get("action") == "R" and machine_check(row["src"], o.get("sk_new"), o.get("pronoun"))
        rw = {"action": o.get("action", "U"), "by": "model", "pronoun": o.get("pronoun"), "where": o.get("where"),
              "machine_check": mc if o.get("action") == "R" else True,
              "text": o.get("sk_new") if mc else row["src"], "reason": o.get("reason")}
        if not o: flags.append("rewrite_fallback_missing")
        elif o.get("action") == "R" and not mc: flags.append("model_rewrite_machine_check_fail")
    v = mv.get("v") or []
    lk = mv.get("lk") or []
    if lk and v and lk[0] and lk[0] not in v[0]: flags.append("lk_not_span_of_v0")
    for f in REQ_V:
        if f not in mv: flags.append("missing:" + f)
    return {"exercise_id": row["exercise_id"], "language_code": L, "n": n, "concept_id": row.get("concept_id"),
            "headword": row.get("headword"), "level": row.get("level"), "exercise_type_id": row.get("exercise_type_id"),
            "type_title": row.get("type_title"), "src": row["src"], "en": row["en"],
            "correct_answer_src": row.get("correct_answer_%s" % L), "lk_supplied": row.get("correct_answer_en"),
            "v": v, "lk": lk, "lk_verdict": mv.get("lk_verdict"), "lk_reason": mv.get("lk_reason"),
            **out, "alt": alt_for(row["en"]), "rewrite": rw,
            "script_voice_paths": drv.get("voice_paths", {}), "script_reader_agent": (drv.get("reader") or {}).get("agent"),
            "field_sources": src_of, "flags": flags}

# ---------------------------------------------------------------- GATE 3 (2C verbatim, bar 12 %)
def gate3(bid, lang, anns):
    rnd = random.Random(int(hashlib.sha256(bid.encode()).hexdigest()[:12], 16))
    pick = rnd.sample(anns, min(50, len(anns)))
    c = {k: collections.Counter() for k in ("agv4", "reader_nom", "g4_diag")}
    for a in pick:
        vp = a.get("script_voice_paths") or {}
        mvoice = (a.get("voice") or "").strip().lower() or None
        reads_pass = bool(vp.get("agv4_main_passive") or vp.get("agv4_main_reflex"))
        if mvoice is None:
            c["agv4"]["UNDECIDED"] += 1
        elif mvoice in ("active_agent", "active_prodrop") and reads_pass:
            c["agv4"]["ERROR"] += 1
        elif mvoice == "passive" and not reads_pass:
            c["agv4"]["ERROR"] += 1
        else:
            c["agv4"]["AGREE"] += 1
        g4p = bool(vp.get("g4_v3_passive_or_reflex") or vp.get("g4_v2_sk_reflex") or vp.get("g4_cz_se_missed"))
        if mvoice is None:
            c["g4_diag"]["UNDECIDED"] += 1
        elif (mvoice in ("active_agent", "active_prodrop") and g4p) or (mvoice == "passive" and not g4p):
            c["g4_diag"]["ERROR"] += 1
        else:
            c["g4_diag"]["AGREE"] += 1
        ag = a.get("script_reader_agent")
        gm = words(a.get("subject"))
        ga = set(gm)
        for e in (a.get("embedded_agents") or []):
            ga |= words(e)
        if not ag:
            c["reader_nom"]["CONSERVATIVE" if gm else "AGREE"] += 1
        elif not ga:
            c["reader_nom"]["ERROR"] += 1
        else:
            c["reader_nom"]["AGREE" if (words(ag) & gm) else "ERROR"] += 1
    def pct(k):
        dec = c[k]["AGREE"] + c[k]["ERROR"]
        return round(100.0 * c[k]["ERROR"] / dec, 2) if dec else None
    adj = sum(1 for a in anns if a.get("lk_verdict") == "adjusted")
    verd = sum(1 for a in anns if a.get("lk_verdict") in ("exact", "adjusted"))
    g = {"batch": bid, "lang": lang, "n_scored": len(pick), "seed": bid, "rows_in_batch": len(anns),
         "agv4": {"counts": dict(c["agv4"]), "ERROR_of_decided_pct": pct("agv4"), "bar": GATE3_BAR},
         "reader_nom": {"counts": dict(c["reader_nom"]), "ERROR_of_decided_pct": pct("reader_nom"), "bar": GATE3_BAR},
         "g4_DIAGNOSTIC_ONLY": {"counts": dict(c["g4_diag"]), "ERROR_of_decided_pct": pct("g4_diag"),
                                "note": "never gates: built over AG v2/v3; 2B settled it as the reflexive si/sa/se pattern"},
         "lk_adjust_rate_pct": round(100.0 * adj / verd, 2) if verd else None,
         "lk_verdicts_returned": verd, "lk_needs_dedicated_pass": LK_NEEDS_DEDICATED_PASS,
         "flagged_rows": sum(1 for a in anns if a.get("flags")),
         "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}
    all_g = json.load(open(GATES, encoding="utf-8")) if os.path.exists(GATES) else {"bar_pct": GATE3_BAR, "batches": {}}
    all_g["batches"][bid] = g
    json.dump(all_g, open(GATES, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    log("GATE3", bid, json.dumps({k: g[k] for k in ("agv4", "reader_nom", "g4_DIAGNOSTIC_ONLY", "lk_adjust_rate_pct")},
                                 ensure_ascii=False))
    if (g["lk_adjust_rate_pct"] is not None) and g["lk_adjust_rate_pct"] < LK_ADJUST_FLOOR:
        defect("batch %s lk adjust rate %.2f %% < %.1f %% - diagnostic only; Czech lk is corrected by the dedicated "
               "pass (lk_needs_dedicated_pass), never trusted from the v session" % (bid, g["lk_adjust_rate_pct"], LK_ADJUST_FLOOR))
    return g

# ---------------------------------------------------------------- upload formats (first batch only, 2C verbatim)
CSV_COLS = ["exercise_id", "language_code", "concept_id", "headword", "level", "type_title", "src", "en",
            "v1", "v2", "lk1", "lk2", "lk_verdict", "lk_reason", "voice", "agent_nom", "subject", "embedded_agents",
            "person", "number", "gender", "tf", "tense_open", "perfective_present", "fragment",
            "rewrite_action", "rewrite_by", "rewrite_text", "alt_mapped_groups", "flags"]
def csv_row(a):
    v = a.get("v") or []; lk = a.get("lk") or []
    return [a.get("exercise_id"), a.get("language_code"), a.get("concept_id"), a.get("headword"), a.get("level"),
            a.get("type_title"), a.get("src"), a.get("en"),
            v[0] if v else "", v[1] if len(v) > 1 else "", lk[0] if lk else "", lk[1] if len(lk) > 1 else "",
            a.get("lk_verdict"), a.get("lk_reason"), a.get("voice"), a.get("agent_nom"), a.get("subject"),
            "|".join(a.get("embedded_agents") or []), a.get("person"), a.get("number"), a.get("gender"), a.get("tf"),
            a.get("tense_open"), a.get("perfective_present"), a.get("fragment"),
            (a.get("rewrite") or {}).get("action"), (a.get("rewrite") or {}).get("by"), (a.get("rewrite") or {}).get("text"),
            "|".join(str(g) for i in (a.get("alt") or []) if i["class"] == "mapped" for g in i["groups_or_candidates"]),
            "|".join(a.get("flags") or [])]
def colname(i):
    s = ""
    i += 1
    while i:
        i, r = divmod(i - 1, 26); s = chr(65 + r) + s
    return s
XSAFE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")
def xesc(v):
    s = "" if v is None else str(v)
    return XSAFE.sub("", s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
def write_xlsx(path, header, rows):
    def row_xml(vals, ri):
        cs = "".join('<c r="%s%d" t="inlineStr"><is><t xml:space="preserve">%s</t></is></c>' % (colname(ci), ri, xesc(v))
                     for ci, v in enumerate(vals))
        return '<row r="%d">%s</row>' % (ri, cs)
    body = row_xml(header, 1) + "".join(row_xml(r, i + 2) for i, r in enumerate(rows))
    sheet = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
             '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData>%s</sheetData></worksheet>' % body)
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml",
                   '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                   '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                   '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
                   '<Default Extension="xml" ContentType="application/xml"/>'
                   '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
                   '<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/></Types>')
        z.writestr("_rels/.rels",
                   '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                   '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/></Relationships>')
        z.writestr("xl/workbook.xml",
                   '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                   '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
                   'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
                   '<sheets><sheet name="annotations" sheetId="1" r:id="rId1"/></sheets></workbook>')
        z.writestr("xl/_rels/workbook.xml.rels",
                   '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                   '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                   '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/></Relationships>')
        z.writestr("xl/worksheets/sheet1.xml", sheet)
def write_uploads(bid, anns):
    xp = os.path.join(OUT, "upload_candidate_A_%s.xlsx" % bid)
    cp = os.path.join(OUT, "upload_candidate_B_%s.csv" % bid)
    write_xlsx(xp, ["exercise_id", "language_code", "level", "src", "en", "structure_json"],
               [[a["exercise_id"], a["language_code"], a["level"], a["src"], a["en"], json.dumps(a, ensure_ascii=False)]
                for a in anns])
    with open(cp, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f); w.writerow(CSV_COLS)
        for a in anns: w.writerow(csv_row(a))
    log("UPLOAD-FORMATS", os.path.basename(xp), os.path.getsize(xp), os.path.basename(cp), os.path.getsize(cp))
    commit([xp, cp], "Phase 2F: upload format candidates from batch %s" % bid)

# ---------------------------------------------------------------- batch driver
def batch_tasks(bid, lang, rows, drv):
    tasks = []
    for k, c in enumerate(chunks(rows), 1):
        tasks.append(("%s_s%02d_v" % (bid, k), "v", VPROMPT(lang) + "\n".join(
            line({"n": r["n"], "src": r["src"], "en": r["en"], "lk_supplied": r.get("correct_answer_en"),
                  "topic": r.get("type_title"), "level": r.get("level"),
                  "person": DERIVED[r["n"]]["person"], "number": DERIVED[r["n"]]["number"],
                  "perfective_present": DERIVED[r["n"]]["perfective_present"]}) for r in c), c))
        fb = [r for r in c if (drv[r["n"]].get("rewrite") or {}).get("action") not in ("U", "R")]
        if fb:
            tasks.append(("%s_s%02d_rw" % (bid, k), "rw", REWRITE + "\n".join(
                line({"n": r["n"], "lang": r["lang"], "sk": r["src"], "en": r["en"]}) for r in fb), fb))
    return tasks

def run_batch(bid, lang, rows):
    done_marker = os.path.join(OUT, "DONE_%s" % bid)
    ann_path = os.path.join(OUT, "annotations_%s_%s.jsonl" % (lang, bid.split("_")[1]))
    if os.path.exists(done_marker) and os.path.exists(ann_path):
        log("SKIP-BATCH", bid, "already complete (DONE marker + annotations file)")
        return "skipped"
    t0 = time.time()
    drv = derive_batch(rows)
    ALLTASKS = batch_tasks(bid, lang, rows, drv)
    done_now = [t[0] for t in ALLTASKS if sess_complete(t[0], [r["n"] for r in t[3]]) is not None]
    tasks = [t for t in ALLTASKS if t[0] not in set(done_now)]
    if A["only"]:
        MATCHED.update(t[0] for t in ALLTASKS if t[0] in A["only"])
        tasks = [t for t in ALLTASKS if t[0] in A["only"]]
    if A["max_sessions"]:
        tasks = tasks[:A["max_sessions"]]
    log("BATCH", bid, lang, len(rows), "rows,", len(ALLTASKS), "sessions total,", len(done_now),
        "already complete (0 tokens):", ",".join(done_now) or "-", "|", len(tasks), "to run now, par", A["par"])
    for sid in done_now:
        log("SKIP-DONE", sid, "already complete on disk, 0 tokens")
    with cf.ThreadPoolExecutor(A["par"]) as ex:
        fs = [ex.submit(session, *t) for t in tasks]
        for f in cf.as_completed(fs):
            sid, out = f.result()
            if isinstance(out, tuple) and out and out[0] == "STOP":
                stop(out[1], out[2])
            if isinstance(out, tuple) and out and out[0] == "FAIL":
                defect("session %s failed: %s" % (sid, out[2]))
    # ---------- 2E change 1: ASSEMBLE WHATEVER IS COMPLETE ----------------------------------------
    # 2E wrote a batch only when all 20 of its sessions were complete, so four give-ups voided 3,200
    # finished rows.  Here a missing session costs ITS OWN rows and nothing else: a missing v session
    # costs its 100-row chunk, a missing rw session costs only that chunk's rewrite-fallback rows.
    missing, MV, RW, blocked, owner = [], {}, {}, {}, {}
    for sid, kind, prompt, crows in ALLTASKS:
        ns = [r["n"] for r in crows]
        for n in ns:
            owner.setdefault(n, []).append(sid)
        d = sess_complete(sid, ns)
        if d is None:
            # 2F change 4: a HALF-CHUNK session (sid + "_h1"/"_h2") whose rows are a contiguous
            # sub-range of this chunk is accepted for ITS OWN rows.  The chunk still counts as
            # missing, so the meta records the partial coverage honestly.
            half = {}
            for suf, sub in (("_h1", ns[:len(ns) // 2]), ("_h2", ns[len(ns) // 2:])):
                if not sub:
                    continue
                dh = sess_complete(sid + suf, sub)
                if dh is not None:
                    for o in (dh["rows"] or []):
                        if o.get("n") in set(sub):
                            half[o["n"]] = o
            if half:
                for n, o in half.items():
                    (MV if kind == "v" else RW)[n] = o
                gone = [n for n in ns if n not in half]
                log("HALF-CHUNK", sid, "recovered", len(half), "row(s)", nranges(sorted(half))[:4],
                    "| still missing", len(gone))
                missing.append(sid)
                for n in gone:
                    blocked[n] = sid
                continue
            missing.append(sid)
            for n in ns:
                blocked[n] = sid
            continue
        for o in (d["rows"] or []):
            (MV if kind == "v" else RW)[o["n"]] = o
    write_rows = [r for r in rows if r["n"] not in blocked]
    lost = [r["n"] for r in rows if r["n"] in blocked]
    if missing:
        log("INCOMPLETE", bid, len(missing), "session(s) missing:", ",".join(missing),
            "| rows lost", len(lost), nranges(lost)[:8], "| rows written anyway", len(write_rows))
        defect("batch %s incomplete: sessions %s missing; %d rows (%s) not written, %d rows written"
               % (bid, ",".join(missing), len(lost), ",".join(nranges(lost)[:8]), len(write_rows)))
    if not write_rows:
        log("EMPTY", bid, "no session of this batch is complete; nothing written")
        save_ledger(); commit([LOGP, LEDGER, DEFECTS], "Phase 2F: batch %s has no complete session" % bid)
        return "partial"
    anns = [assemble(r, drv[r["n"]], MV.get(r["n"]), RW.get(r["n"])) for r in write_rows]
    with open(ann_path, "w", encoding="utf-8") as f:
        for a in anns:
            f.write(json.dumps(a, ensure_ascii=False) + "\n")
    side = os.path.join(OUT, "annotations_%s_%s.meta.json" % (lang, bid.split("_")[1]))
    json.dump({"batch": bid, "lang": lang, "phase": "2E", "task": "A",
               "complete": not missing,
               "rows_in_batch": len(rows), "rows_written": len(anns), "rows_missing": len(lost),
               "row_ranges_present": nranges([r["n"] for r in write_rows]),
               "row_ranges_missing": nranges(lost),
               "sessions_total": len(ALLTASKS), "sessions_present": [t[0] for t in ALLTASKS if t[0] not in set(missing)],
               "sessions_missing": missing,
               "lk_needs_dedicated_pass": LK_NEEDS_DEDICATED_PASS,
               "lk_note": "the v-session lk is NOT final; Task B re-judges every Czech row in a dedicated pass.",
               "par": A["par"], "prompt_sha": PROMPT_SHA,
               "adopted_from_prior": sorted(sid for sid in (t[0] for t in ALLTASKS)
                                            if (STATE["sessions"].get(sid) or {}).get("adopted")),
               "written": time.strftime("%Y-%m-%dT%H:%M:%S")},
              open(side, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    commit([ann_path, side, DEFECTS], "Phase 2F: annotations %s (%d of %d rows%s)"
            % (bid, len(anns), len(rows), "" if not missing else ", PARTIAL"))
    g = gate3(bid, lang, anns)
    first = not any(os.path.exists(os.path.join(OUT, "upload_candidate_A_%s.xlsx" % b)) for b in BATCH_IDS)
    if first:
        write_uploads(bid, anns)
    if not missing:
        open(done_marker, "w").write(time.strftime("%Y-%m-%dT%H:%M:%S") + "\n")
    else:
        json.dump({"batch": bid, "rows_written": len(anns), "rows_missing": len(lost),
                   "row_ranges_missing": nranges(lost), "sessions_missing": missing,
                   "ts": time.strftime("%Y-%m-%dT%H:%M:%S")},
                  open(os.path.join(OUT, "PARTIAL_%s.json" % bid), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    STATE["rows_done"] += len(anns)
    save_ledger()
    commit([GATES, done_marker if not missing else os.path.join(OUT, "PARTIAL_%s.json" % bid), LOGP, LEDGER, DEFECTS],
           "Phase 2F: batch %s %s + GATE 3" % (bid, "complete" if not missing else "partial"))
    for k in ("agv4", "reader_nom"):
        p = g[k]["ERROR_of_decided_pct"]
        if p is not None and p > GATE3_BAR:
            stop("gate3_%s_%s" % (k, bid),
                 "GATE 3 failed on batch %s (%s): %s ERROR-of-decided %.2f %% > %.1f %% bar.\n\n"
                 "Counts: %s\nThe batch's annotations are written and committed; the run stopped before the next batch.\n"
                 "g4 (diagnostic only, never gates): %s" % (bid, lang, k, p, GATE3_BAR, g[k]["counts"],
                                                            g["g4_DIAGNOSTIC_ONLY"]))
    log("BATCH-DONE", bid, "rows_written", len(anns), "of", len(rows), "wall_s",
        round(time.time() - t0, 1), "cum_tok", STATE["tok"], "complete", not missing)
    return "done" if not missing else "partial"

# ---------------------------------------------------------------- self-test (0 model calls)
def selftest():
    fails = []
    def ck(name, cond, extra=""):
        log("SELFTEST", "PASS" if cond else "FAIL", name, extra)
        if not cond: fails.append(name)
    # change 2: back-off
    ck("should_retry:429_in_stdout", should_retry(0, '{"x":1} 429 Too Many Requests', ""))
    ck("should_retry:429_in_stderr", should_retry(0, "", "HTTP 429"))
    ck("should_retry:nonzero_exit", should_retry(1, "", ""))
    ck("should_retry:clean_run_not_retried", not should_retry(0, '{"result":"[]"}', ""))
    r = random.Random(7)
    ds = [backoff_sleep_s(i, r) for i in range(MAX_RETRY)]
    ck("backoff:60/120/240_plus_jitter", all(60 * 2 ** i <= ds[i] < 60 * 2 ** i + 30 for i in range(MAX_RETRY)),
       "[%s]" % ", ".join("%.1f" % d for d in ds))
    ck("backoff:at_most_3_retries_2F", MAX_RETRY == 3, "MAX_RETRY=%d" % MAX_RETRY)
    # change 3: circuit breaker
    STATE["kind"]["v"] = [0, 0, 0.0]
    ck("cb:floors_before_any_mean", circuit_limits("v") == (900.0, 200000.0), str(circuit_limits("v")))
    STATE["kind"]["v"] = [10, 950_000, 3000.0]                 # mean 95,000 tok / 300 s
    w, t = circuit_limits("v")
    ck("cb:3x_mean_wall_900s", abs(w - 900.0) < 1e-6, "wall_cap=%.0f" % w)
    ck("cb:3x_mean_tokens_285k", abs(t - 285000.0) < 1e-6, "tok_cap=%.0f" % t)
    STATE["kind"]["v"] = [10, 1_600_000, 9000.0]               # mean 160,000 tok / 900 s
    w, t = circuit_limits("v")
    ck("cb:scales_above_floor", (w, t) == (2700.0, 480000.0), "wall=%.0f tok=%.0f" % (w, t))
    STATE["kind"]["v"] = [10, 950_000, 3000.0]                 # 2C's healthy mean: 95,000 tok / 300 s
    w, t = circuit_limits("v")
    ck("cb:2C_runaway_impossible", 18839 > w and 436644 > t,
       "2C's 18,839 s / 436,644 tok session is killed at %.0f s and is over the %.0f tok ceiling" % (w, t))
    STATE["kind"] = collections.defaultdict(lambda: [0, 0, 0.0])
    # change 4: throughput guard
    g = ThroughputGuard()
    t0, res, trip_at = 1000.0, None, None
    for i in range(1, 40):                                     # minutes at 0 tok/s
        res = g.sample(t0 + 60 * i, 0)
        if res:
            trip_at = i; break
    ck("guard:trips_at_20_low_minutes",
       res is not None and g.low == TP_MIN_SAMPLES and trip_at == TP_MIN_SAMPLES + 1,
       "low=%d, tripped at minute %s (sample 1 has no trailing window yet)" % (g.low, trip_at))
    g2 = ThroughputGuard()
    tok = 0
    for i in range(1, 60):                                     # 100 tok/s forever
        tok += 6000
        ck2 = g2.sample(t0 + 60 * i, tok)
    ck("guard:healthy_run_never_trips", ck2 is None and g2.low == 0, "rate=%.1f tok/s" % (g2.rate or 0))
    g3 = ThroughputGuard()
    tok = 0
    for i in range(1, 15):
        g3.sample(t0 + 60 * i, tok)
    streak_before = g3.low
    for i in range(15, 25):
        tok += 6000
        g3.sample(t0 + 60 * i, tok)
    ck("guard:recovery_resets_streak", streak_before >= 13 and g3.low == 0, "%d -> %d" % (streak_before, g3.low))
    # 2F change 1: the guard's clock excludes back-off sleep entirely
    ck("guard:floor_restored_to_20_min_60_toks", TP_MIN_SAMPLES == 20 and TP_MIN_TOK_S == 60.0 and TP_WINDOW_S == 300)
    del SLEEPS[:]
    ck("sleep:no_intervals_no_subtraction", sleep_overlap(0.0, 100.0) == 0.0)
    SLEEPS.extend([(10.0, 40.0), (20.0, 50.0)])                # two PAR=2 sessions asleep at once
    ck("sleep:overlapping_intervals_merged_not_double_counted", sleep_overlap(0.0, 100.0) == 40.0,
       "%.1f s" % sleep_overlap(0.0, 100.0))
    ck("sleep:clipped_to_the_window", sleep_overlap(30.0, 45.0) == 15.0, "%.1f s" % sleep_overlap(30.0, 45.0))
    del SLEEPS[:]
    tz = 1000.0
    g4 = ThroughputGuard(); SLEEPS.append((tz, tz + 60 * 40))   # a whole 40-minute ladder, 0 tokens
    res4 = None
    for i in range(1, 41):
        res4 = g4.sample(tz + 60 * i, 0)
    ck("guard:a_40_min_backoff_ladder_never_trips_it", res4 is None and g4.low == 0 and g4.dt == 0.0,
       "low=%d corrected_window=%.0f s" % (g4.low, g4.dt if g4.dt is not None else -1))
    del SLEEPS[:]
    g5 = ThroughputGuard(); SLEEPS.append((tz, tz + 60 * 31))   # 2E's ladder, then REAL dead time
    trip5 = None
    for i in range(1, 32):
        g5.sample(tz + 60 * i, 0)
    ck("guard:streak_stays_0_while_asleep", g5.low == 0, "low=%d" % g5.low)
    for i in range(32, 80):
        if g5.sample(tz + 60 * i, 0):
            trip5 = i; break
    ck("guard:trips_20_measured_minutes_after_the_ladder", trip5 == 31 + TP_MIN_SAMPLES,
       "tripped at minute %s (ladder ended at 31)" % trip5)
    g6 = ThroughputGuard(); del SLEEPS[:]
    SLEEPS.append((tz, tz + 60 * 31))
    tok6 = 0
    for i in range(1, 60):                                     # healthy 100 tok/s after the ladder
        tok6 += 6000 if i > 31 else 0
        r6 = g6.sample(tz + 60 * i, tok6)
    ck("guard:healthy_after_a_ladder_never_trips", r6 is None and g6.low == 0, "low=%d" % g6.low)
    del SLEEPS[:]
    # 2F change 3: an UNMEASURABLE window (no completion while work is in flight) neither counts nor fires
    del SLEEPS[:]
    g7 = ThroughputGuard(); STATE["inflight"] = 1
    res7 = None
    for i in range(1, 41):                                     # 40 minutes, one session still out, tok frozen
        res7 = g7.sample(tz + 60 * i, 285312)
    ck("guard:inflight_zero_delta_is_unmeasurable_never_fires",
       res7 is None and g7.low == 0 and g7.unmeasurable >= 39,
       "low=%d unmeasurable=%d (the 2F Part 1 stop at 00:13:25)" % (g7.low, g7.unmeasurable))
    g7b = ThroughputGuard()                                    # ... and it does not RESET a real streak either
    for i in range(1, 11):
        STATE["inflight"] = 0; g7b.sample(tz + 60 * i, 0)      # 10 genuinely idle minutes, nothing in flight
    pre = g7b.low
    STATE["inflight"] = 1
    for i in range(11, 21):
        g7b.sample(tz + 60 * i, 0)
    ck("guard:unmeasurable_does_not_reset_a_real_streak", pre == 9 and g7b.low == 9,
       "%d -> %d" % (pre, g7b.low))
    g8 = ThroughputGuard(); STATE["inflight"] = 2              # 2C: 25 tok/s WITH sessions returning
    tok8, trip8 = 0, None
    for i in range(1, 60):
        tok8 += 1500                                           # 25 tok/s * 60 s
        if g8.sample(tz + 60 * i, tok8):
            trip8 = i; break
    ck("guard:2C_25_toks_with_returns_still_fires_at_20_min",
       trip8 == TP_MIN_SAMPLES + 1 and g8.low == TP_MIN_SAMPLES,
       "tripped at minute %s, rate %.1f tok/s" % (trip8, g8.rate or 0))
    g9 = ThroughputGuard(); SLEEPS.append((tz, tz + 60 * 31))  # change 1 still behaves, now with inflight > 0
    for i in range(1, 32):
        g9.sample(tz + 60 * i, 0)
    ck("guard:change1_sleep_exclusion_intact_under_change3", g9.low == 0 and g9.dt == 0.0,
       "low=%d corrected_window=%.0f s" % (g9.low, g9.dt if g9.dt is not None else -1))
    del SLEEPS[:]; STATE["inflight"] = 0
    # change 5: projection gate
    p = projection(rows_paid=700, rows_left=3364, tok=966_000, elapsed=7000.0)
    ck("projection:tokens", p["projected_total_tokens"] == int(966_000 + 1380.0 * 3364), json.dumps(p))
    ck("projection:stops_over_4h", p["projected_total_s"] > WALL_CAP_S, "%.2f h" % p["projected_total_h"])
    ck("projection:stops_over_cap", p["projected_total_tokens"] > 3_000_000)
    p2 = projection(rows_paid=700, rows_left=3364, tok=700_000, elapsed=2000.0)
    ck("projection:passes_when_fast", p2["projected_total_s"] < WALL_CAP_S and p2["projected_total_tokens"] < 6_000_000,
       json.dumps(p2))
    ck("projection:no_paid_rows_no_gate", projection(0, 100, 0, 1.0) is None)
    # change 1 + 6
    ck("par_is_2", PAR == 2 and (A["par"] == 2 or "--par" in sys.argv))
    ck("lk_prompt_unchanged_vs_2C", hashlib.sha256(VPROMPT("cz").encode()).hexdigest()[:16] == PROMPT_SHA["v_cz"])
    ck("lk_needs_dedicated_pass_true", LK_NEEDS_DEDICATED_PASS is True)
    ck("gate3_bar_12", GATE3_BAR == 12.0)
    ck("N_is_100", NSESS == 100)
    ck("czech_only", BATCH_IDS == ["cz_0001", "cz_0002", "cz_0003", "cz_0004", "cz_0005"])
    # GATE 3 still fires: 50 synthetic rows where the model contradicts AG v4 on 20 of them
    syn = [{"voice": "passive" if i < 20 else "active_agent", "script_voice_paths": {"agv4_main_passive": False},
            "subject": "on", "script_reader_agent": "on", "embedded_agents": [],
            "lk_verdict": "adjusted" if i % 5 == 0 else "exact", "flags": []} for i in range(50)]
    gg = gate3("SELFTEST", "cz", syn)
    ck("gate3:fires_above_12pct_bar", gg["agv4"]["ERROR_of_decided_pct"] == 40.0 > GATE3_BAR, str(gg["agv4"]["counts"]))
    ck("gate3:reader_nom_leg_scored", gg["reader_nom"]["ERROR_of_decided_pct"] == 0.0, str(gg["reader_nom"]["counts"]))
    ck("gate3:g4_diagnostic_only", "g4_DIAGNOSTIC_ONLY" in gg and gg["g4_DIAGNOSTIC_ONLY"]["ERROR_of_decided_pct"] == 40.0)
    ck("gate3:lk_needs_dedicated_pass_recorded", gg["lk_needs_dedicated_pass"] is True)
    if fails:
        log("SELFTEST", "FAILED:", fails); sys.exit(5)
    log("SELFTEST", "all checks passed, 0 model tokens")

# ---------------------------------------------------------------- plan (what is left, what it should cost)
CZ_HEALTHY_TOK_PER_SENT = 1379.0
def plan(selected, adopted):
    tot_rows = sum(len(b[2]) for b in selected)
    # 2C's own measured per-slot speed, from its ledger (sk sessions = the healthy stretch)
    try:
        L2 = json.load(open(os.path.join(C2, "ledger_2c.json"), encoding="utf-8"))["sessions"]
        sk = [s for k, s in L2.items() if k.startswith("sk_") and s.get("wall_s")]
        rate = sum(s["tokens"] for s in sk) / sum(s["wall_s"] for s in sk)
        n_sk = len(sk)
    except Exception:
        rate, n_sk = None, 0
    rows_left = 0
    sess_left = 0
    per = []
    for bid, lang, rows in selected:
        ns = len(chunks(rows))
        done_v = [s for s in adopted if s.startswith(bid) and s.endswith("_v")]
        done_rw = [s for s in adopted if s.startswith(bid) and s.endswith("_rw")]
        left_v = ns - len(done_v)
        rows_left += left_v * NSESS if bid != "cz_0005" else max(0, len(rows) - len(done_v) * NSESS)
        sess_left += left_v
        per.append({"batch": bid, "rows": len(rows), "v_sessions": ns, "v_done": len(done_v), "rw_done": len(done_rw),
                    "v_left": left_v})
    proj_tok = int(rows_left * CZ_HEALTHY_TOK_PER_SENT)
    log("PLAN", json.dumps({"batches": per, "rows_left_v": rows_left, "v_sessions_left": sess_left,
                            "adopted_sessions": len(adopted),
                            "cz_healthy_tok_per_sentence": CZ_HEALTHY_TOK_PER_SENT,
                            "projected_tokens_v_rows": proj_tok,
                            "measured_2c_per_slot_tok_per_s": round(rate, 1) if rate else None,
                            "n_2c_sessions_measured": n_sk,
                            "projected_wall_h_at_par_%d" % A["par"]:
                                round(proj_tok / (rate * A["par"]) / 3600.0, 2) if rate else None},
                           ensure_ascii=False))
    return {"rows_left": rows_left, "sessions_left": sess_left, "proj_tok": proj_tok, "rate": rate}

# ---------------------------------------------------------------- main
def main():
    import glob as _g
    sf = [f for f in _g.glob(os.path.join(H, "%s_*.md" % STOPPFX))]
    if sf and not A["ignore_stop"]:
        sys.stderr.write("FATAL: an unresolved stop file exists (%s). A stop is a decision, not a hiccup: read it, "
                         "then re-run with --ignore-stop-file to continue.\n" % ", ".join(os.path.basename(x) for x in sf))
        sys.exit(2)
    load_ledger()
    if A["self_test"]:
        selftest()
    if not A["dry"]:
        if not os.path.exists(BIN):
            stop("no_cli_binary", "the bundled claude binary is not at %s; 0 sessions spent." % BIN)
        load_token()
    adopted = adopt_prior_sessions()
    alt_build()
    total_rows = sum(len(b[2]) for b in SELECTED)
    log("START", "dry" if A["dry"] else "LIVE", "batches", [b[0] for b in SELECTED], "rows", total_rows,
        "cap", A["cap"], "already_spent", STATE["tok"], "par", A["par"], "prompt_sha", PROMPT_SHA,
        "lk_needs_dedicated_pass", LK_NEEDS_DEDICATED_PASS, "adopted", len(adopted), "only", A["only"] or None)
    plan(SELECTED, adopted)
    if not A["dry"]:
        threading.Thread(target=monitor_loop, daemon=True).start()
    def unpaid_left(after_bid):
        """2E change 3: extrapolate over rows that still have to be PAID FOR, not over every remaining row.
        On a resume where most sessions are adopted at 0 tokens, this process's tok/row applied to all
        remaining rows overstates the total by the adopted:run ratio and stops a run well inside its cap."""
        seen, v_rows, rw_n = False, 0, 0
        for _bid, _lang, _rows in SELECTED:
            if not seen:
                if _bid == after_bid: seen = True
                continue
            for _k, _c in enumerate(chunks(_rows), 1):
                if sess_complete("%s_s%02d_v" % (_bid, _k), [r["n"] for r in _c]) is None:
                    v_rows += len(_c)
                if not os.path.exists(sess_path("%s_s%02d_rw" % (_bid, _k))):
                    rw_n += 1
        return v_rows, rw_n

    done_batches, rows_left = 0, total_rows
    for bid, lang, rows in SELECTED:
        if STATE["stop_spawn"]:
            log("SKIP-REMAINING", bid, "stop requested:", STATE["stop_spawn"][:120])
            break
        st = run_batch(bid, lang, rows)
        rows_left -= len(rows)
        if st in ("done", "partial"):
            done_batches += 1 if st == "done" else 0
            _vr, _rwn = unpaid_left(bid)
            p = projection(STATE["rows_paid"], _vr, STATE["tok"], time.time() - STATE["t0"])
            if p is not None:
                p["unpaid_rows_left"], p["rw_sessions_left"], p["all_rows_left"] = _vr, _rwn, rows_left
                p["projected_total_tokens"] += _rwn * EST["rw"]
            if p is None:
                log("PROJECTION", bid, "no rows paid for in this process (all sessions adopted); gate not applicable")
            else:
                log("PROJECTION", bid, json.dumps(p))
                if p["projected_total_s"] > WALL_CAP_S:
                    stop("projection_wall", "after batch %s: %s projects %.2f h for the remaining %d rows, over the "
                                            "4 h cap. Everything complete is committed; resume with the same command."
                         % (bid, json.dumps(p), p["projected_total_h"], rows_left))
                if p["projected_total_tokens"] > A["cap"]:
                    stop("projection_budget", "after batch %s: %s projects %d tokens, over the --cap %d remaining "
                                              "budget. Everything complete is committed."
                         % (bid, json.dumps(p), p["projected_total_tokens"], A["cap"]))
        if STATE["stop_spawn"]:
            break
    STATE["finished"] = True
    if A["only"] and set(A["only"]) - MATCHED:
        save_ledger()
        sys.stderr.write("FATAL: --only id(s) %s matched no session; nothing was ignored silently\n"
                         % sorted(set(A["only"]) - MATCHED)); sys.exit(2)
    save_ledger()
    commit([LOGP, LEDGER, GATES, DEFECTS], "Phase 2F: run segment finished (%d tokens cumulative)" % STATE["tok"])
    log("END", "tokens", STATE["tok"], "wall_s", round(time.time() - STATE["t0"], 1), "batches_done", done_batches,
        "retries", STATE["retries"], "giveups", len(STATE["giveups"]),
        "stopped_early", bool(STATE["stop_spawn"]))

if __name__ == "__main__":
    main()
