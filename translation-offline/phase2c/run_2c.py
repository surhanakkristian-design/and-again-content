#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phase 2C RUN: production annotation of the 8,128-row selection (sk 4,064 + cz 4,064).

PIPELINE (per sentence)
  1. SCRIPT  derive_2c.derive(row, mode="after")  -> person / number / perfective_present  (the only three
     fields GATE 1 passed), the arm-B rewrite, the AG v4 / reader_nom / g4 voice paths (for GATE 3 only).
  2. SCRIPT  arm-B rewrite; where the reader ABSTAINs a model fallback session (2B REWRITE prompt, verbatim).
  3. MODEL   ONE session per 100 rows authors  v, the lk CORRECTION (lk_verdict exact|adjusted + reason),
     voice, agent_nom, subject, gender, tense_open, tf, embedded_agents, fragment and every residual null.
     2B SCORE #5: the v session copied lk[0] unchanged on 100/100 rows incl. the 41 the judge marked adjust,
     so the lk correction is stated explicitly and a per-row verdict is REQUIRED.  Adjust rate is a
     DIAGNOSTIC: < 5 % on a batch writes a DEFECT line and the run continues.
  4. SCRIPT  alt, mapped against the phase1b group table (alt_map_2b.py's classifier, reused).

LAYOUT   N = 100 rows/session, 4 sessions in parallel, batches of 1,000 rows, one language per batch:
         sk_0001..sk_0004 = 1,000 each, sk_0005 = 64;  same for cz.  82 v-sessions + <=82 rw-sessions.

IDEMPOTENT  keyed on (batch, session).  A batch with out/DONE_<batch> is skipped whole; a session whose
         out/sessions/<sid>.json is present, parsable, exit 0 and complete is never re-run.  Unknown argv
         is a hard error (2B breached its cap because a runner ignored argv and re-ran five finished
         sessions).  Safe:  nohup python3 run_2c.py --all &   and the same command again to resume.

CAPS     10,500,000 headless tokens (all tokens incl. cache reads), in-flight pre-check before every spawn;
         5 h wall, projected from batch 1.  Breach -> phase2c/STOP_<reason>.md + exit 2.
GATE 3   after every batch, 50 deterministic rows (seed = batch id): AG v4 voice path and the fixed
         reader_nom scored against that batch's own model annotation.  ERROR-of-decided > 12 % on either
         -> STOP.  g4 is recorded as a DIAGNOSTIC ONLY and never gates (2B: 20 of its 23-28 raw errors are
         the one reflexive si/sa/se pattern the arm-B rewrite amplifies by construction).
0 Gemini calls.  0 DB access.  Writes only inside phase2c/.  The OAuth token is never printed or logged.
"""
import os, re, sys, csv, json, time, random, hashlib, zipfile, subprocess, threading, collections
import concurrent.futures as cf
sys.dont_write_bytecode = True

H = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(H)
REPO = os.path.dirname(BASE)
B2 = os.path.join(BASE, "phase2b")
for p in (H, B2):
    if p not in sys.path:
        sys.path.insert(0, p)
BIN = os.path.expanduser("~/Library/Application Support/Claude/claude-code/2.1.275/claude.app/Contents/MacOS/claude")
MODEL = "opus"
PAR = 4
NSESS = 100                      # rows per session
NBATCH = 1000                    # rows per batch
CAP = 10_500_000                 # hard cap, all headless tokens incl. cache reads
EST = {"v": 95_000, "rw": 60_000}   # pre-check defaults until a running mean exists
WALL_CAP_S = 5 * 3600
GATE3_BAR = 12.0                 # ERROR-of-decided %, AG v4 and reader_nom
LK_ADJUST_FLOOR = 5.0            # diagnostic only

# ---------------------------------------------------------------- argv (nothing is ignored)
def parse_argv(argv):
    a = {"all": False, "batches": [], "only": [], "dry": False, "cap": CAP, "par": PAR, "max_sessions": None}
    i = 0
    while i < len(argv):
        x = argv[i]
        if x == "--all": a["all"] = True
        elif x == "--dry-run": a["dry"] = True
        elif x == "--batch": i += 1; a["batches"].append(argv[i])
        elif x == "--only": i += 1; a["only"].append(argv[i])
        elif x == "--cap": i += 1; a["cap"] = int(argv[i])
        elif x == "--par": i += 1; a["par"] = int(argv[i])
        elif x == "--max-sessions": i += 1; a["max_sessions"] = int(argv[i])
        else:
            sys.stderr.write("FATAL: unknown argument %r; refusing to run (no argv is ever ignored)\n" % x)
            sys.exit(2)
        i += 1
    if not a["all"] and not a["batches"]:
        sys.stderr.write("FATAL: nothing selected; pass --all or --batch <id>\n"); sys.exit(2)
    return a
A = parse_argv(sys.argv[1:])
OUT = os.path.join(H, "out_dry" if A["dry"] else "out")
SESSDIR = os.path.join(OUT, "sessions")
os.makedirs(SESSDIR, exist_ok=True)
LEDGER = os.path.join(H, "ledger_2c.json")
GATES = os.path.join(H, "gates_2c.json")
LOGP = os.path.join(H, "run_2c.log")
DEFECTS = os.path.join(H, "DEFECTS_run_2c.md")

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

# ---------------------------------------------------------------- git
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

def stop(reason, detail):
    fn = os.path.join(H, "STOP_%s.md" % reason)
    open(fn, "w", encoding="utf-8").write(
        "# Phase 2C STOP: %s\n\n%s\n\nWritten %s.\nSpent so far: %s headless tokens, %.1f s wall.\n"
        % (reason, detail, time.strftime("%Y-%m-%d %H:%M:%S"), STATE["tok"], time.time() - STATE["t0"]))
    log("STOP", reason, detail)
    save_ledger()
    commit([fn, LEDGER, GATES, LOGP], "Phase 2C: STOP %s" % reason)
    sys.exit(3)

# ---------------------------------------------------------------- prompts (2B text, reused verbatim)
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
    """The 2B v prompt, widened: it now also authors the lk CORRECTION and every field the script may not author."""
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
              for k, v in {"v_sk": VPROMPT("sk"), "v_cz": VPROMPT("cz"), "rw": REWRITE}.items()}

REQ_V = ["v", "lk", "lk_verdict", "voice", "subject", "agent_nom", "gender", "tf", "tense_open"]

# ---------------------------------------------------------------- data + script derivation
import derive_2c                                                    # noqa: E402  (GATE 1 entry point)

def load_selection():
    rows = [json.loads(l) for l in open(os.path.join(H, "selection_2c.jsonl"), encoding="utf-8") if l.strip()]
    assert len(rows) == 8128, "selection_2c.jsonl has %d rows, expected 8128" % len(rows)
    return rows
SEL = load_selection()
BYN = {r["n"]: r for r in SEL}

def batches_of(rows):
    out = []
    for lang in ("sk", "cz"):
        rs = [r for r in rows if r["lang"] == lang]
        for i in range(0, len(rs), NBATCH):
            out.append(("%s_%04d" % (lang, i // NBATCH + 1), lang, rs[i:i + NBATCH]))
    return out
BATCHES = batches_of(SEL)
BATCH_IDS = [b[0] for b in BATCHES]
if A["batches"]:
    bad = [b for b in A["batches"] if b not in BATCH_IDS]
    if bad:
        sys.stderr.write("FATAL: unknown batch id(s) %s; known: %s\n" % (bad, BATCH_IDS)); sys.exit(2)
SELECTED = [b for b in BATCHES if A["all"] or b[0] in A["batches"]]
MATCHED = set()
SID_RE = re.compile(r"^(sk|cz)_\d{4}_s\d{2}_(v|rw)$")
for _o in A["only"]:
    if not SID_RE.match(_o) or _o.rsplit("_s", 1)[0] not in [x[0] for x in SELECTED]:
        sys.stderr.write("FATAL: --only %r is not a session id of a selected batch; refusing to run\n" % _o); sys.exit(2)

def line(o): return json.dumps(o, ensure_ascii=False)

def chunks(batch_rows):
    return [batch_rows[i:i + NSESS] for i in range(0, len(batch_rows), NSESS)]

# ---------------------------------------------------------------- alt (alt_map_2b.py classifier, reused)
ALTC = os.path.join(H, "alt_index_2c.json")
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
STATE = {"tok": 0, "inflight": 0, "t0": time.time(), "rows_done": 0, "sessions": {}, "kind": collections.defaultdict(lambda: [0, 0])}
LOCK = threading.Lock()
def load_ledger():
    if os.path.exists(LEDGER):
        try:
            d = json.load(open(LEDGER, encoding="utf-8"))
            STATE["sessions"] = d.get("sessions", {})
            STATE["tok"] = sum(s.get("tokens", 0) for s in STATE["sessions"].values())
            for s in STATE["sessions"].values():
                k = s.get("kind", "v"); STATE["kind"][k][0] += 1; STATE["kind"][k][1] += s.get("tokens", 0)
        except Exception as ex:
            defect("ledger unreadable (%r); refusing to run rather than lose the budget count" % ex); sys.exit(2)
def save_ledger():
    if A["dry"]:
        return
    d = {"cap": A["cap"], "spent": STATE["tok"], "updated": time.strftime("%Y-%m-%dT%H:%M:%S"),
         "wall_s_this_process": round(time.time() - STATE["t0"], 1),
         "by_kind": {k: {"sessions": v[0], "tokens": v[1], "mean": round(v[1] / v[0], 1) if v[0] else None}
                     for k, v in STATE["kind"].items()},
         "sessions": STATE["sessions"]}
    tmp = LEDGER + ".tmp"
    json.dump(d, open(tmp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    os.replace(tmp, LEDGER)
def est_for(kind):
    n, tk = STATE["kind"][kind]
    return round(tk / n) if n >= 2 else EST[kind]
def usage_total(m): return sum(m.get(k) or 0 for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens"))

# ---------------------------------------------------------------- headless session
ENV = dict(os.environ)
def load_token():
    if not ENV.get("CLAUDE_CODE_OAUTH_TOKEN"):
        ENV["CLAUDE_CODE_OAUTH_TOKEN"] = subprocess.run(
            ["zsh", "-ic", 'printf %s "$CLAUDE_CODE_OAUTH_TOKEN"'], capture_output=True, text=True).stdout.strip()
    if not ENV.get("CLAUDE_CODE_OAUTH_TOKEN"):
        stop("no_oauth_token", "CLAUDE_CODE_OAUTH_TOKEN is empty; 0 sessions spent. Unblock: `claude auth login` "
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

def fake_rows(kind, rows):
    if kind == "rw":
        return [{"n": r["n"], "action": "U", "sk_new": r["src"], "pronoun": None, "where": None, "reason": "explicit_subject"}
                for r in rows]
    out = []
    for r in rows:
        o = {"n": r["n"], "v": [r["en"]], "lk": [r.get("correct_answer_en") or ""],
             "lk_verdict": "adjusted" if r["n"] % 4 == 0 else "exact", "lk_reason": "dry run",
             "voice": "passive" if r["n"] % 7 == 0 else ("active_prodrop" if r["n"] % 3 == 0 else "active_agent"),
             "subject": (r["src"].split() or [""])[0], "agent_nom": r["n"] % 3 != 0, "embedded_agents": [],
             "gender": "m", "tf": "present", "tense_open": False, "fragment": False, "main_sentence_index": 0,
             "person": "3sg", "number": "sg", "perfective_present": False}
        out.append(o)
    return out

def session(sid, kind, prompt, rows):
    want = [r["n"] for r in rows]
    have = sess_complete(sid, want)
    if have is not None:
        log("SKIP-DONE", sid, len(have["rows"]), "rows already on disk")
        return sid, have["rows"]
    if A["dry"]:
        rows_out = fake_rows(kind, rows)
        json.dump({"meta": {"session": sid, "kind": kind, "exit": 0, "dry_run": True, "wall_s": 0.0},
                   "prompt": prompt, "result": "", "rows": rows_out},
                  open(sess_path(sid), "w", encoding="utf-8"), ensure_ascii=False)
        log("DRY", sid, kind, len(rows_out), "rows", "prompt_chars", len(prompt))
        return sid, rows_out
    e = est_for(kind)
    with LOCK:
        proj = STATE["tok"] + STATE["inflight"] * max(EST.values()) + e
        if proj > A["cap"]:
            return sid, ("STOP", "token_cap", "session %s: %d spent + %d in flight + %d projected > cap %d"
                         % (sid, STATE["tok"], STATE["inflight"] * max(EST.values()), e, A["cap"]))
        STATE["inflight"] += 1
    try:
        t0 = time.time()
        p = subprocess.run([BIN, "-p", prompt, "--output-format", "json", "--max-turns", "12", "--model", MODEL],
                           capture_output=True, text=True, env=ENV, cwd=H)
        try:
            j = json.loads(p.stdout)
        except Exception:
            j = {"parse_error": p.stdout[-400:],
                 "stderr": re.sub(r"sk-ant-\S+", "sk-ant-REDACTED", p.stderr[-400:])}
        u = j.get("usage", {}) or {}
        meta = {"session": sid, "kind": kind, "exit": p.returncode, "wall_s": round(time.time() - t0, 1),
                "num_turns": j.get("num_turns"), "total_cost_usd": j.get("total_cost_usd"), "is_error": j.get("is_error"),
                **{k: u.get(k, 0) for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens")},
                "parse_error": j.get("parse_error"), "stderr": j.get("stderr"), "rows_asked": len(rows)}
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
                r = BYN.get(o["n"], {})
                need = list(REQ_V) if kind == "v" else ["action"]
                if kind == "v":
                    for f in ("person", "number", "perfective_present"):
                        if (DERIVED.get(o["n"], {}).get(f) is None) and f not in o:
                            miss[f] += 1
                for f in need:
                    if f not in o or o[f] is None and f in ("v", "lk", "lk_verdict", "voice", "tf"):
                        miss[f] += 1
            meta["missing_fields"] = dict(miss)
        json.dump({"meta": meta, "prompt": prompt, "result": txt, "rows": out},
                  open(sess_path(sid), "w", encoding="utf-8"), ensure_ascii=False)
        with LOCK:
            STATE["tok"] += tok
            STATE["kind"][kind][0] += 1; STATE["kind"][kind][1] += tok
            STATE["sessions"][sid] = {"kind": kind, "tokens": tok, "wall_s": meta["wall_s"], "exit": p.returncode,
                                      "rows": len(out or []), "asked": len(rows),
                                      "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}
            save_ledger()
        log("DONE", sid, kind, "exit", p.returncode, "tok", tok, "cum", STATE["tok"], "wall", meta["wall_s"],
            "rows", len(out or []), "/", len(rows), "missing", meta.get("missing_fields"))
        commit([sess_path(sid), LEDGER], "Phase 2C: session %s (%d tok)" % (sid, tok))
        if out is None:
            return sid, ("FAIL", sid, "unparsable/exit %d" % p.returncode)
        return sid, out
    finally:
        with LOCK:
            STATE["inflight"] -= 1

# ---------------------------------------------------------------- assembly
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
    # rewrite: script arm-B, model fallback where the reader abstained
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

# ---------------------------------------------------------------- GATE 3
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
         "lk_verdicts_returned": verd, "flagged_rows": sum(1 for a in anns if a.get("flags")),
         "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}
    all_g = json.load(open(GATES, encoding="utf-8")) if os.path.exists(GATES) else {"bar_pct": GATE3_BAR, "batches": {}}
    all_g["batches"][bid] = g
    json.dump(all_g, open(GATES, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    log("GATE3", bid, json.dumps({k: g[k] for k in ("agv4", "reader_nom", "g4_DIAGNOSTIC_ONLY", "lk_adjust_rate_pct")},
                                 ensure_ascii=False))
    if (g["lk_adjust_rate_pct"] is not None) and g["lk_adjust_rate_pct"] < LK_ADJUST_FLOOR:
        defect("batch %s lk adjust rate %.2f %% < %.1f %% (2B judge: 20.5 %%) - the v session may be copying "
               "lk_supplied again; run continues by instruction" % (bid, g["lk_adjust_rate_pct"], LK_ADJUST_FLOOR))
    return g

# ---------------------------------------------------------------- upload formats (first batch only)
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
    commit([xp, cp], "Phase 2C: upload format candidates from batch %s (xlsx structure-as-JSON, flat csv)" % bid)

# ---------------------------------------------------------------- batch driver
def run_batch(bid, lang, rows):
    done_marker = os.path.join(OUT, "DONE_%s" % bid)
    ann_path = os.path.join(OUT, "annotations_%s_%s.jsonl" % (lang, bid.split("_")[1]))
    if os.path.exists(done_marker) and os.path.exists(ann_path):
        log("SKIP-BATCH", bid, "already complete (DONE marker + annotations file)")
        return "skipped"
    t0 = time.time()
    drv = derive_batch(rows)
    ch = chunks(rows)
    tasks = []
    for k, c in enumerate(ch, 1):
        vsid = "%s_s%02d_v" % (bid, k)
        tasks.append((vsid, "v", VPROMPT(lang) + "\n".join(
            line({"n": r["n"], "src": r["src"], "en": r["en"], "lk_supplied": r.get("correct_answer_en"),
                  "topic": r.get("type_title"), "level": r.get("level"),
                  "person": DERIVED[r["n"]]["person"], "number": DERIVED[r["n"]]["number"],
                  "perfective_present": DERIVED[r["n"]]["perfective_present"]}) for r in c), c))
        fb = [r for r in c if (drv[r["n"]].get("rewrite") or {}).get("action") not in ("U", "R")]
        if fb:
            tasks.append(("%s_s%02d_rw" % (bid, k), "rw", REWRITE + "\n".join(
                line({"n": r["n"], "lang": r["lang"], "sk": r["src"], "en": r["en"]}) for r in fb), fb))
    ALLTASKS = list(tasks)
    if A["only"]:
        MATCHED.update(t[0] for t in ALLTASKS if t[0] in A["only"])
        tasks = [t for t in ALLTASKS if t[0] in A["only"]]
    if A["max_sessions"]:
        tasks = tasks[:A["max_sessions"]]
    log("BATCH", bid, lang, len(rows), "rows,", len(ch), "chunks,", len(ALLTASKS), "sessions total,", len(tasks), "to run now")
    with cf.ThreadPoolExecutor(A["par"]) as ex:
        fs = [ex.submit(session, *t) for t in tasks]
        for f in cf.as_completed(fs):
            sid, out = f.result()
            if isinstance(out, tuple) and out and out[0] == "STOP":
                stop(out[1], out[2])
            if isinstance(out, tuple) and out and out[0] == "FAIL":
                defect("session %s failed: %s" % (sid, out[2]))
    # assemble only when EVERY session of the batch is on disk and complete
    missing, MV, RW = [], {}, {}
    for sid, kind, prompt, crows in ALLTASKS:
        d = sess_complete(sid, [r["n"] for r in crows])
        if d is None:
            missing.append(sid); continue
        for o in (d["rows"] or []):
            (MV if kind == "v" else RW)[o["n"]] = o
    if missing:
        log("PARTIAL", bid, len(missing), "sessions still missing:", missing[:6], "... no annotations written")
        save_ledger(); commit([LOGP, LEDGER], "Phase 2C: partial batch %s" % bid)
        return "partial"
    anns = [assemble(r, drv[r["n"]], MV.get(r["n"]), RW.get(r["n"])) for r in rows]
    with open(ann_path, "w", encoding="utf-8") as f:
        for a in anns:
            f.write(json.dumps(a, ensure_ascii=False) + "\n")
    commit([ann_path], "Phase 2C: annotations %s (%d rows)" % (bid, len(anns)))
    g = gate3(bid, lang, anns)
    first = not any(os.path.exists(os.path.join(OUT, "upload_candidate_A_%s.xlsx" % b)) for b in BATCH_IDS)
    if first:
        write_uploads(bid, anns)
    open(done_marker, "w").write(time.strftime("%Y-%m-%dT%H:%M:%S") + "\n")
    STATE["rows_done"] += len(rows)
    save_ledger()
    commit([GATES, done_marker, LOGP, LEDGER, DEFECTS], "Phase 2C: batch %s complete + GATE 3" % bid)
    for k in ("agv4", "reader_nom"):
        p = g[k]["ERROR_of_decided_pct"]
        if p is not None and p > GATE3_BAR:
            stop("gate3_%s_%s" % (k, bid),
                 "GATE 3 failed on batch %s (%s): %s ERROR-of-decided %.2f %% > %.1f %% bar.\n\n"
                 "Counts: %s\nThe batch's annotations are written and committed; the run stopped before the next batch.\n"
                 "g4 (diagnostic only, never gates): %s" % (bid, lang, k, p, GATE3_BAR, g[k]["counts"],
                                                            g["g4_DIAGNOSTIC_ONLY"]))
    log("BATCH-DONE", bid, "rows", len(rows), "wall_s", round(time.time() - t0, 1), "cum_tok", STATE["tok"])
    return "done"

# ---------------------------------------------------------------- main
def main():
    load_ledger()
    if not A["dry"]:
        load_token()
    alt_build()
    total_rows = sum(len(b[2]) for b in SELECTED)
    log("START", "dry" if A["dry"] else "LIVE", "batches", [b[0] for b in SELECTED], "rows", total_rows,
        "cap", A["cap"], "already_spent", STATE["tok"], "par", A["par"], "prompt_sha", PROMPT_SHA,
        "only", A["only"] or None)
    done_batches = 0
    for bid, lang, rows in SELECTED:
        st = run_batch(bid, lang, rows)
        if st == "done":
            done_batches += 1
            if done_batches == 1 and STATE["rows_done"]:
                el = time.time() - STATE["t0"]
                proj = el / STATE["rows_done"] * total_rows
                log("WALL-PROJECTION", "elapsed", round(el, 1), "s for", STATE["rows_done"], "rows ->",
                    round(proj / 3600, 2), "h for", total_rows, "rows")
                if proj > WALL_CAP_S:
                    stop("wall_projection", "after batch %s: %.1f s for %d rows projects %.2f h for %d rows, over the "
                                            "5 h cap. Completed batches are committed; resume with the same command "
                                            "after raising --par or splitting the run." % (bid, el, STATE["rows_done"],
                                                                                           proj / 3600, total_rows))
    if A["only"] and set(A["only"]) - MATCHED:
        save_ledger()
        sys.stderr.write("FATAL: --only id(s) %s matched no session; nothing was ignored silently\n"
                         % sorted(set(A["only"]) - MATCHED)); sys.exit(2)
    save_ledger()
    commit([LOGP, LEDGER, GATES, DEFECTS], "Phase 2C: run segment finished (%d tokens cumulative)" % STATE["tok"])
    log("END", "tokens", STATE["tok"], "wall_s", round(time.time() - STATE["t0"], 1), "batches_done", done_batches)

if __name__ == "__main__":
    main()
