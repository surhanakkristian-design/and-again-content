#!/usr/bin/env python3
"""Phase 2A: rewrite + annotate the first 1,000 production SK sentences with the measured 1W pipeline, unchanged
(prompts copied verbatim from phase1w/trackB/run_s5.py; bundled claude 2.1.275, --model opus, N = 30, 4 parallel).
Order: stage 1 rewrite x1000 + blind gold x100 -> stage 2 annotate the 100 gold rows -> §4.2 guard gate
(frozen stack reader_nom 'full'; any gated guard ERROR > 10 % => STOP) -> stage 3 annotate the other 900.
Writes phase2a/ only, commits every produced file at once. 0 Gemini calls, 0 DB access (selection.json is input).
  python3 run_2a.py --dry   : guard smoke test on 1W Track B rows + preflight, 0 sessions."""
import json, os, re, sys, math, time, hashlib, subprocess, threading, contextlib, importlib.util
import concurrent.futures as cf
sys.dont_write_bytecode = True
H = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(H)
REPO = os.path.dirname(BASE)
BIN = os.path.expanduser("~/Library/Application Support/Claude/claude-code/2.1.275/claude.app/Contents/MacOS/claude")
MODEL = "opus"; N = 30; PAR = 4
CAP = 2_850_000          # headless harness tokens; 150k of the 3.0M phase budget reserved for sub-agents
EST = 45_000             # per-session worst-case estimate used for the pre-launch budget check
GATE = 10.0
DRY = "--dry" in sys.argv
os.makedirs(f"{H}/sessions", exist_ok=True)

# ---------------------------------------------------------------- prompts: VERBATIM from phase1w/trackB/run_s5.py
DEF = """Definitions (Slovak): tf = time frame of the MAIN clause: past / present / future (a perfective verb in
present form = future). person = person+number of the main-clause finite verb: 1sg 2sg 3sg 1pl 2pl 3pl.
subject = the overt NOMINATIVE subject NP of the main-clause finite verb, copied verbatim from the Slovak
(it may stand anywhere in the clause, not only first), or null if the subject is dropped (pro-drop) or absent.
voice = active_agent (overt nominative subject) / active_prodrop (subject dropped, recoverable from the verb) /
impersonal (no subject possible, e.g. "je známe", "prší") / passive (byť + passive participle, or reflexive passive).
agent_nom = true iff voice == active_agent. embedded_agents = overt nominative subjects of subordinate clauses (verbatim list)."""
REWRITE = """You are the arm-B rewrite agent (1J rule) of a Slovak->English translation-checking pipeline.
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
ANNOT = """You are the annotation agent (1M/1N schema) of a Slovak->English translation-checking pipeline.
For each (possibly rewritten) Slovak sentence with its English reference, write the annotation:
{"n": int, "v": [1-2 acceptable English translations], "lk": [key verb phrase of each v],
 "alt": {english word: [acceptable alternatives]}, "tf_gold": "past"|"present"|"future",
 "person": str, "subject": str|null, "voice_sk": str, "agent_nom": bool, "embedded_agents": [str],
 "perfective_present": bool, "tense_open": bool}
""" + DEF + """
tense_open = true iff more than one English tense is acceptable. Reply with ONLY a JSON array, no prose, no fences.
Sentences:
"""
GOLD = """You are a blind gold annotator. You see ONLY Slovak sentences. For each, write the gold label:
{"n": int, "tf": str, "person": str, "subject": str|null, "voice": str, "embedded_agents": [str], "fragment": bool}
""" + DEF + """
fragment = true iff the sentence has no finite main verb. Reply with ONLY a JSON array, no prose, no fences.
Sentences:
"""
PROMPT_SHA = {k: hashlib.sha256(v.encode()).hexdigest()[:16] for k, v in (("REWRITE", REWRITE), ("ANNOT", ANNOT), ("GOLD", GOLD))}

# ---------------------------------------------------------------- guards (1V trackb.py / 1W s2_validate.py method, unchanged)
def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(BASE, rel))
    m = importlib.util.module_from_spec(spec); sys.modules[name] = m; spec.loader.exec_module(m); return m
f9 = load("f9_1n", "phase1n/f9.py")
CK = load("checker_1i", "phase1i/checker_1i.py")
V2 = load("agent_drop_v2", "phase1s/taskC/agent_drop_v2.py")
V3 = load("agent_drop_v3", "phase1t/taskA/agent_drop_v3.py")
src = open(os.path.join(BASE, "phase1t/taskB/cz_validate.py"), encoding="utf-8").read()
NS = {"re": re, "json": json, "os": os, "f9": f9, "CK": CK, "V2": V2, "V3": V3}
exec(src[src.index("WORD = re.compile"):src.index("\nout = []")], NS)
sys.path.insert(0, os.path.join(BASE, "phase1w"))
import reader_nom as R                                                            # noqa: E402
OLD_SA = V2.slovak_agent
WORD = re.compile(r"[a-záäčďéěíĺľňóôöŕřšťúůüýž]+", re.I)
words = lambda s: set(WORD.findall((s or "").lower()))

def g3cls(agent, g, v3m=V3):                       # verbatim logic of phase1w/s2_validate.py
    toks_ = v3m.parse_agent_tokens(agent)[0] if agent else []
    gm = words(g.get("subject")); ga = set(gm)
    for e in (g.get("embedded_agents") or []):
        ga |= words(e)
    low = {x.lower().strip(".,!?;:„“\"'") for x in toks_ if x}
    if not agent:
        return "CONSERVATIVE" if gm else "AGREE"
    if not ga:
        return "ERROR"
    return "AGREE" if low & gm else "ERROR"

def cp(k, n, a=0.05):
    if n == 0: return [None, None]
    def cdf(x, p): return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(x + 1))
    def bis(f):
        lo, hi = 0.0, 1.0
        for _ in range(60):
            mid = (lo + hi) / 2
            if f(mid): lo = mid
            else: hi = mid
        return (lo + hi) / 2
    lo = 0.0 if k == 0 else bis(lambda p: 1 - cdf(k - 1, p) < a / 2)
    hi = 1.0 if k == n else bis(lambda p: cdf(k, p) > a / 2)
    return [round(100 * lo, 2), round(100 * hi, 2)]

def guard_classes(text, g):
    out = {}
    for tag, ctx in (("frozen", lambda: R.installed(V2, "sk", "full")), ("v1V", contextlib.nullcontext)):
        with ctx():
            try:
                o4 = NS["g4"](text, g)
                c = {"g1": NS["g1"](text, g)["class"], "g2": NS["g2"](text, g)["class"],
                     "g3_v2": NS["g3"](text, g, V2)["class"], "g3_v3": NS["g3"](text, g, V3)["class"],
                     "g4_v2": o4["class_v2"], "g4_v3": o4["class_v3"]}
            except Exception as ex:
                c = {k: "CRASH " + repr(ex)[:80] for k in ("g1", "g2", "g3_v2", "g3_v3", "g4_v2", "g4_v3")}
        for k, v in c.items(): out[f"{tag}:{k}"] = v
    out["reader_nom_full"] = g3cls(R.read(text, "sk", "full")[0], g)
    out["reader_1V_firstword"] = g3cls(OLD_SA(text, {}, {})[0], g)
    return out

GATED = lambda k: k.startswith("frozen:") or k == "reader_nom_full"

def guard_table(pairs):
    per, errs = {}, {}
    for n, text, g in pairs:
        for k, c in guard_classes(text, g).items():
            key = "ERROR" if str(c).startswith(("ERROR", "CRASH")) else str(c)
            per.setdefault(k, {}); per[k][key] = per[k].get(key, 0) + 1
            if key == "ERROR": errs.setdefault(k, []).append([n, text[:90], str(c)[:60], g.get("subject"), g.get("voice")])
    tab = {}
    for k, v in per.items():
        e = v.get("ERROR", 0); n = sum(v.values())
        tab[k] = {"counts": v, "n": n, "ERROR": e, "ERROR_pct": round(100 * e / n, 2), "cp95": cp(e, n), "gated": GATED(k)}
    return tab, errs

def gold_full(g):
    g = dict(g); g.setdefault("embedded_agents", []); g.setdefault("fragment", False)
    g["subject_explicit"] = g.get("subject") is not None; g["agent_nom"] = g.get("voice") == "active_agent"; g["tf_note"] = ""
    return g

def gold_after(g, w):
    ga = json.loads(json.dumps(g))
    if w.get("action") == "R" and w.get("machine_check"):
        if w.get("where") == "main" and g.get("voice") == "active_prodrop":
            ga.update(subject=w["pronoun"], subject_explicit=True, voice="active_agent", agent_nom=True)
        elif w.get("where") == "embedded":
            ga["embedded_agents"] = list(ga.get("embedded_agents") or []) + [w["pronoun"]]
    return ga

# ---------------------------------------------------------------- dry: guard smoke test on 1W Track B + preflight, 0 sessions
if DRY:
    s5 = json.load(open(os.path.join(BASE, "phase1w/trackB/s5_rows.json"), encoding="utf-8"))
    pairs = [(r["n"], r["sk"], gold_full(s5["gold"][str(r["n"])])) for r in s5["rows"] if str(r["n"]) in s5["gold"]]
    tab, _ = guard_table(pairs)
    print(json.dumps({k: [v["ERROR"], v["n"], v["counts"]] for k, v in tab.items()}, ensure_ascii=False))
    print("BIN exists:", os.path.exists(BIN), "| prompts sha:", PROMPT_SHA)
    sel = os.path.join(H, "selection.json")
    print("selection.json:", os.path.exists(sel))
    sys.exit(0)

# ---------------------------------------------------------------- run
env = dict(os.environ)
if not env.get("CLAUDE_CODE_OAUTH_TOKEN"):
    env["CLAUDE_CODE_OAUTH_TOKEN"] = subprocess.run(["zsh", "-ic", 'printf %s "$CLAUDE_CODE_OAUTH_TOKEN"'], capture_output=True, text=True).stdout
if not env.get("CLAUDE_CODE_OAUTH_TOKEN"):
    print("STOP: CLAUDE_CODE_OAUTH_TOKEN empty; 0 sessions spent"); sys.exit(2)
SEL = json.load(open(f"{H}/selection.json", encoding="utf-8"))
rows = sorted(SEL["rows"], key=lambda r: r["n"])
assert len(rows) == 1000 and len({r["exercise_id"] for r in rows}) == 1000
BY = {r["n"]: r for r in rows}
LOCK = threading.Lock(); GIT = threading.Lock()
STATE = {"tok": 0, "inflight": 0, "sessions": [], "refused": [], "t0": time.time()}
LOG = open(f"{H}/run_2a.log", "a", buffering=1)
def log(*a):
    s = time.strftime("%H:%M:%S ") + " ".join(str(x) for x in a)
    LOG.write(s + "\n"); print(s, flush=True)

def commit(paths, msg):
    with GIT:
        rel = [os.path.relpath(p, REPO) for p in paths]
        subprocess.run(["git", "add", "--"] + rel, cwd=REPO, capture_output=True)
        r = subprocess.run(["git", "commit", "-q", "-m", msg + "\n\nCo-Authored-By: Claude Opus 5 <noreply@anthropic.com>", "--"] + rel,
                           cwd=REPO, capture_output=True, text=True)
        if r.returncode: log("GIT-FAIL", rel, r.stderr[-200:])

def usage_total(m): return sum(m.get(k) or 0 for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens"))

def session(name, prompt):
    with LOCK:
        if STATE["tok"] + (STATE["inflight"] + 1) * EST > CAP:
            STATE["refused"].append(name); log("BUDGET-REFUSE", name, STATE["tok"]); return None, None
        STATE["inflight"] += 1
    recs = []
    try:
        for attempt in (1, 2):
            t0 = time.time()
            p = subprocess.run([BIN, "-p", prompt, "--output-format", "json", "--max-turns", "12", "--model", MODEL],
                               capture_output=True, text=True, env=env, cwd=H)
            try: j = json.loads(p.stdout)
            except Exception: j = {"parse_error": p.stdout[-500:], "stderr": re.sub(r"sk-ant-\S+", "sk-ant-REDACTED", p.stderr[-500:])}
            u = j.get("usage", {}) or {}
            rec = {"session": name, "attempt": attempt, "exit": p.returncode, "wall_s": round(time.time() - t0, 1),
                   "t_start": round(t0 - STATE["t0"], 1), "duration_ms": j.get("duration_ms"), "num_turns": j.get("num_turns"),
                   "total_cost_usd": j.get("total_cost_usd"), "is_error": j.get("is_error"),
                   **{k: u.get(k, 0) for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens")},
                   "modelUsage": j.get("modelUsage"), "parse_error": j.get("parse_error"), "stderr": j.get("stderr")}
            txt = j.get("result", "") or ""
            try: out = json.loads(txt[txt.find("["):txt.rfind("]") + 1])
            except Exception: out = None; rec["result_unparsable"] = txt[:300]
            fn = f"{H}/sessions/{name}{'' if attempt == 1 else '_retry'}.json"
            json.dump({"meta": rec, "prompt": prompt, "result": txt}, open(fn, "w"), ensure_ascii=False, indent=1)
            with LOCK:
                STATE["tok"] += usage_total(rec); STATE["sessions"].append(rec)
            recs.append(rec); log("DONE", name, "att", attempt, "exit", p.returncode, "tok", usage_total(rec), "cum", STATE["tok"], "ok", out is not None)
            commit([fn], f"Phase 2A: session {name}{'' if attempt == 1 else ' (retry)'}")
            if out is not None and p.returncode == 0: return rec, out
            with LOCK:
                if STATE["tok"] + (STATE["inflight"]) * EST > CAP: break
        return recs[-1], None
    finally:
        with LOCK: STATE["inflight"] -= 1

def fmt(bs, key, with_en=True):
    return "\n".join(json.dumps({"n": r["n"], "sk": r[key], **({"en": r["en"]} if with_en else {})}, ensure_ascii=False) for r in bs)
chunks = lambda xs: [xs[i:i + N] for i in range(0, len(xs), N)]
def run_many(jobs):
    with cf.ThreadPoolExecutor(PAR) as ex:
        fs = {ex.submit(session, name, pr): name for name, pr in jobs}
        return {fs[f]: f.result() for f in cf.as_completed(fs)}

log("START", "rows", len(rows), "cap", CAP, "prompts", PROMPT_SHA)
gold_rows = [r for r in rows if r.get("gold")]
assert len(gold_rows) == 100
# stage 1: rewrite x1000 + blind gold x100 (Slovak only)
jobs = [(f"rewrite_b{i+1:02d}", REWRITE + fmt(b, "sk")) for i, b in enumerate(chunks(rows))]
jobs += [(f"gold_b{i+1}", GOLD + fmt(b, "sk", False)) for i, b in enumerate(chunks(gold_rows))]
res1 = run_many(jobs)
rw, gold = {}, {}
for name, (rec, out) in res1.items():
    for o in (out or []):
        if isinstance(o, dict) and "n" in o: (rw if name.startswith("rewrite") else gold)[int(o["n"])] = o
def toks(s): return [w.lower() for w in re.findall(r"\w+", s)]
for r in rows:
    w = dict(rw.get(r["n"], {"action": "U", "missing": True})); new = r["sk"]
    if w.get("action") == "R":
        a, b = toks(r["sk"]), toks(w.get("sk_new") or r["sk"]); ok = True
        for t in a:
            if t in b: b.remove(t)
            else: ok = False
        w["machine_check"] = ok and b == [str(w.get("pronoun", "")).lower()]
        if w["machine_check"]: new = w["sk_new"]
    r["rewrite"] = w; r["sk_new"] = new
json.dump({"rewrite": {str(k): v for k, v in rw.items()}, "gold": {str(k): v for k, v in gold.items()},
           "rows": [{k: r[k] for k in ("n", "exercise_id", "level", "sk", "en", "gold", "rewrite", "sk_new")} for r in rows]},
          open(f"{H}/stage1_rewrite_gold.json", "w"), ensure_ascii=False, indent=1)
commit([f"{H}/stage1_rewrite_gold.json", f"{H}/run_2a.log"], "Phase 2A: stage 1 rewrite x1000 + blind gold x100 merged")

# stage 2: annotate the 100 gold rows first
ann = {}
res2 = run_many([(f"annot_g{i+1}", ANNOT + fmt(b, "sk_new")) for i, b in enumerate(chunks(gold_rows))])
for name, (rec, out) in res2.items():
    for o in (out or []):
        if isinstance(o, dict) and "n" in o: ann[int(o["n"])] = o

# §4.2 gate on the 100: before = raw SK vs blind gold; after = rewritten SK vs gold_after
gp_before, gp_after, gold_missing = [], [], []
for r in gold_rows:
    g = gold.get(r["n"])
    if not g: gold_missing.append(r["n"]); continue
    g0 = gold_full(g); g1 = gold_after(g0, r["rewrite"])
    r["gold_before"], r["gold_after"] = g0, g1
    gp_before.append((r["n"], r["sk"], g0)); gp_after.append((r["n"], r["sk_new"], g1))
tb, eb = guard_table(gp_before); ta, ea = guard_table(gp_after)
gate_fail = sorted({f"{st}:{k}" for st, t in (("before", tb), ("after", ta)) for k, v in t.items() if v["gated"] and v["ERROR_pct"] > GATE})
GATE_RES = {"n_before": len(gp_before), "n_after": len(gp_after), "gold_missing": gold_missing, "before": tb, "after": ta,
            "errors_before": eb, "errors_after": ea, "bar_pct": GATE, "fail": gate_fail, "verdict": "STOP" if gate_fail else "PASS"}
json.dump(GATE_RES, open(f"{H}/gate_4_2.json", "w"), ensure_ascii=False, indent=1)
commit([f"{H}/gate_4_2.json", f"{H}/run_2a.log"], f"Phase 2A §4.2 gate: {GATE_RES['verdict']}")
log("GATE", GATE_RES["verdict"], gate_fail)

# stage 3: annotate the other 900 only on PASS
if not gate_fail:
    rest = [r for r in rows if not r.get("gold")]
    res3 = run_many([(f"annot_b{i+1:02d}", ANNOT + fmt(b, "sk_new")) for i, b in enumerate(chunks(rest))])
    for name, (rec, out) in res3.items():
        for o in (out or []):
            if isinstance(o, dict) and "n" in o: ann[int(o["n"])] = o

# ---------------------------------------------------------------- outputs
out_rows, v0_moved, v0_absent = [], 0, []
for r in rows:
    a = ann.get(r["n"])
    if a:
        v, lk = list(a.get("v") or []), list(a.get("lk") or [])
        if v and v[0] != r["en"] and r["en"] in v:            # v[0] must be the reference: reorder deterministically
            i = v.index(r["en"]); v.insert(0, v.pop(i))
            if i < len(lk): lk.insert(0, lk.pop(i))
            v0_moved += 1
        elif v and v[0] != r["en"]: v_ref_absent = True; v0_absent.append(r["n"])
        a = dict(a, v=v, lk=lk)
    out_rows.append({"n": r["n"], "exercise_id": r["exercise_id"], "level": r["level"], "en": r["en"], "sk_raw": r["sk"],
                     "sk_new": r["sk_new"], "rewrite": r["rewrite"], "annotation": a, "gold": r.get("gold", False)})
json.dump({"rows": out_rows}, open(f"{H}/annotations_2a.json", "w"), ensure_ascii=False, indent=1)

# blind-gold agreement (1W logic)
def norm(s): return " ".join(toks(s or ""))
def subj_eq(a, b, lenient):
    a, b = norm(a), norm(b)
    if not a or not b: return a == b
    return a == b or (lenient and (a in b or b in a))
F = ["tf", "person", "voice", "agent_nom", "subject_exact", "subject_lenient"]
agree = {f: 0 for f in F}; exact = 0; dis = []; rw_dec = 0; n_cmp = 0; ex_unrw = [0, 0]
for r in gold_rows:
    g, a, w = r.get("gold_after"), ann.get(r["n"]), r["rewrite"]
    if not g or not a: dis.append(f"n{r['n']}: missing {'gold' if not g else 'annotation'}"); continue
    n_cmp += 1; gan = g.get("voice") == "active_agent"
    rw_dec += ((w.get("action") == "R" and w.get("where") == "main") == (r["gold_before"].get("voice") == "active_prodrop"))
    chk = {"tf": a.get("tf_gold") == g.get("tf"), "person": a.get("person") == g.get("person"),
           "voice": a.get("voice_sk") == g.get("voice"), "agent_nom": bool(a.get("agent_nom")) == gan,
           "subject_exact": subj_eq(a.get("subject"), g.get("subject"), False),
           "subject_lenient": subj_eq(a.get("subject"), g.get("subject"), True)}
    for f in F: agree[f] += chk[f]
    ok = all(chk[f] for f in ("tf", "person", "voice", "agent_nom", "subject_lenient")); exact += ok
    if w.get("action") != "R": ex_unrw[0] += ok; ex_unrw[1] += 1
    if not ok:
        dis.append(f"n{r['n']} ({r['exercise_id']}, {r['level']}) {r['sk_new']} | " + "; ".join(
            f"{f}: ann={a.get({'tf': 'tf_gold', 'voice': 'voice_sk'}.get(f, f.split('_')[0]))!r} gold={(gan if f == 'agent_nom' else g.get(f.split('_')[0]))!r}"
            for f in ("tf", "person", "voice", "agent_nom", "subject_lenient") if not chk[f]))

def stage(prefix, nsent):
    ms = [m for m in STATE["sessions"] if m["session"].startswith(prefix)]
    s = {k: sum((m.get(k) or 0) for m in ms) for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens", "total_cost_usd")}
    s["sessions"] = len(ms); s["sentences"] = nsent; s["duration_s"] = sum((m.get("duration_ms") or 0) for m in ms) / 1000
    s["all"] = s["input_tokens"] + s["cache_creation_input_tokens"] + s["cache_read_input_tokens"] + s["output_tokens"]
    s["no_cache_read"] = s["all"] - s["cache_read_input_tokens"]
    if nsent:
        s.update(per_sent_all=round(s["all"] / nsent, 1), per_sent_no_cache_read=round(s["no_cache_read"] / nsent, 1),
                 per_sent_output=round(s["output_tokens"] / nsent, 1), per_sent_usd=round(s["total_cost_usd"] / nsent, 5),
                 per_sent_s=round(s["duration_s"] / nsent, 2))
    return s
n_ann = len(ann)
ST = {"rewrite": stage("rewrite", len(rw)), "annot": stage("annot", n_ann), "gold": stage("gold", len(gold))}
REM = 4895; B = math.ceil(REM / N)
ext = {k: {"tokens_all": round(ST[k].get("per_sent_all", 0) * REM), "tokens_no_cache_read": round(ST[k].get("per_sent_no_cache_read", 0) * REM),
           "output": round(ST[k].get("per_sent_output", 0) * REM), "usd": round(ST[k].get("per_sent_usd", 0) * REM, 2),
           "sessions": B, "serial_h": round(ST[k].get("per_sent_s", 0) * REM / 3600, 2)} for k in ST}
lv = lambda r: r["level"]
LEVELS = sorted({r["level"] for r in rows})
RES = {"model": MODEL, "N": N, "parallel": PAR, "cap": CAP, "prompt_sha": PROMPT_SHA, "gemini_calls": 0,
       "wall_s": round(time.time() - STATE["t0"], 1), "tokens_headless_total": STATE["tok"],
       "sessions": STATE["sessions"], "refused_by_budget": STATE["refused"],
       "failures": [m["session"] for m in STATE["sessions"] if m["exit"] or m.get("result_unparsable") or m.get("parse_error")],
       "rewrites": {"returned": len(rw), "R": sum(1 for r in rows if r["rewrite"].get("action") == "R"),
                    "R_applied": sum(1 for r in rows if r["rewrite"].get("machine_check")),
                    "R_main": sum(1 for r in rows if r["rewrite"].get("machine_check") and r["rewrite"].get("where") == "main"),
                    "R_embedded": sum(1 for r in rows if r["rewrite"].get("machine_check") and r["rewrite"].get("where") == "embedded"),
                    "machine_check_fail": [r["n"] for r in rows if r["rewrite"].get("action") == "R" and not r["rewrite"].get("machine_check")],
                    "missing": [r["n"] for r in rows if r["rewrite"].get("missing")],
                    "by_level": {L: [sum(1 for r in rows if lv(r) == L and r["rewrite"].get("machine_check")), sum(1 for r in rows if lv(r) == L)] for L in LEVELS}},
       "annotated": n_ann, "annotation_missing": [r["n"] for r in rows if r["n"] not in ann] if not gate_fail else "stage 3 not run (gate STOP)",
       "v0_reordered_to_reference": v0_moved, "v0_reference_absent": v0_absent,
       "gate": {"verdict": GATE_RES["verdict"], "fail": gate_fail},
       "agreement": {"n_compared": n_cmp, **{f: [agree[f], n_cmp] for f in F}, "exact": [exact, n_cmp], "exact_cp95": cp(exact, n_cmp),
                     "exact_unrewritten": ex_unrw, "rewrite_decision_vs_gold_prodrop": [rw_dec, n_cmp], "disagreements": dis},
       "stages": ST, "extrapolation_remaining_4895": ext,
       "production_rewrite_plus_annotation_4895": {f: ext["rewrite"][f] + ext["annot"][f] for f in ("tokens_all", "tokens_no_cache_read", "output", "usd", "sessions", "serial_h")}}
json.dump(RES, open(f"{H}/results_2a.json", "w"), ensure_ascii=False, indent=1)
commit([f"{H}/annotations_2a.json", f"{H}/results_2a.json", f"{H}/run_2a.log"], f"Phase 2A: results (gate {GATE_RES['verdict']}, annotated {n_ann})")
log("END", "tok", STATE["tok"], "gate", GATE_RES["verdict"], "annotated", n_ann, "wall", RES["wall_s"])
open(f"{H}/RUN_DONE", "w").write(time.strftime("%Y-%m-%dT%H:%M:%S"))
