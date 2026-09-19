#!/usr/bin/env python3
"""Phase 2B RUN (measurement only): 6 headless sessions over the 200-row sample (phase2b/sample_2b.json).
  gold_sk, gold_cz   blind gold (source only), 2A GOLD + DEF with the language named, extended schema
  lk_judge           en + correct_answer_en only -> exact / adjust / unusable
  v_sk, v_cz         the v field ALONE, every other field supplied (cost of v at N = 100)
  rewrite_fallback   2A REWRITE (language line widened to sk + cz) on derived_2b.model_fallback_ns (97 rows)
session(), commit(), usage accounting copied from phase2a/run_2a.py (bundled claude 2.1.275, --model opus,
--output-format json, --max-turns 12, token via zsh -ic, 4 parallel). HEADLESS HARD CAP 330,000, EST 60,000/session.
If the first spawn fails: STOP at 0 cost, error -> phase2b/SPAWN_ERROR.txt. 0 Gemini calls, 0 DB access."""
import json, os, re, sys, time, hashlib, subprocess, threading
import concurrent.futures as cf
sys.dont_write_bytecode = True
H = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(H)
REPO = os.path.dirname(BASE)
BIN = os.path.expanduser("~/Library/Application Support/Claude/claude-code/2.1.275/claude.app/Contents/MacOS/claude")
MODEL = "opus"; PAR = 4
CAP = 330_000; EST = 60_000
os.makedirs(f"{H}/sessions", exist_ok=True)

# ---------------------------------------------------------------- 2A text (verbatim copies from phase2a/run_2a.py)
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
LNAME = {"sk": "Slovak", "cz": "Czech"}
def DEF(lang):
    if lang == "sk": return DEF_2A
    return (DEF_2A.replace("(Slovak)", "(Czech)").replace("from the Slovak", "from the Czech")
            .replace('"je známe"', '"je známo"').replace("byť +", "být +"))
def GOLD(lang):
    L = LNAME[lang]
    return (f"""You are a blind gold annotator. You see ONLY {L} sentences. For each, write the gold label:
{{"n": int, "tf": str, "person": str, "number": "sg"|"pl"|null, "gender": "m"|"f"|"n"|null, "subject": str|null, "voice": str,
 "embedded_agents": [str], "perfective_present": bool, "tense_open": bool, "fragment": bool, "main_sentence_index": int}}
""" + DEF(lang) + """
number = number of the main-clause finite verb (sg / pl). gender = grammatical gender of the main-clause subject as the
sentence marks it (subject noun or pronoun, past participle, predicative adjective): m / f / n, or null if not marked.
tense_open = true iff more than one English tense is acceptable. perfective_present = true iff the main-clause finite verb
is perfective in present form. fragment = true iff the sentence has no finite main verb. main_sentence_index = if the item
contains more than one sentence, the 0-based index of the sentence whose main clause you labelled (0 otherwise).
Reply with ONLY a JSON array, no prose, no fences.
Sentences:
""")
LK = """You judge the "lk" field of a translation-checking pipeline. lk = the key verb phrase of an English translation:
the span of the English sentence that the exercise practises (the phrase the learner must produce), verbatim from the sentence.
For each row you see the English sentence "en" and the exercise's stored answer "correct_answer_en". Classify correct_answer_en as lk:
exact = usable as lk as is (a verbatim span of en that is the practised phrase);
adjust = overlaps the practised phrase but needs trimming or extension (give the corrected verbatim span of en);
unusable = not a span of en, or does not identify the practised phrase.
Reply with ONLY a JSON array, one object per row:
{"n": int, "class": "exact"|"adjust"|"unusable", "lk": str|null (the corrected span for adjust, else null), "reason": str (<= 8 words)}
No prose, no fences.
Rows:
"""
def VPROMPT(lang):
    L = LNAME[lang]
    return f"""You are the annotation agent of a {L}->English translation-checking pipeline. Every field except v is already
supplied. For each row you get the {L} sentence "src", the English reference "en", its key phrase "lk" and the known
tf / person / voice (null = not derived). Write ONLY the v field: 1-2 acceptable English translations of src; v[0] MUST be
the reference en verbatim; add a second only if a clearly different acceptable translation exists. lk = the key verb phrase
of each v (lk[0] = the supplied lk).
Reply with ONLY a JSON array, one object per row: {{"n": int, "v": [str], "lk": [str]}}. No prose, no fences.
Rows:
"""
REWRITE = (REWRITE_2A
           .replace("of a Slovak->English translation-checking pipeline.\nFor each Slovak sentence:",
                    "of a Slovak/Czech->English translation-checking pipeline.\nFor each sentence (\"lang\": sk = Slovak, cz = Czech; the text is in field \"sk\" for both):")
           .replace("personal pronoun (ja, ty, on, ona, ono, my, vy, oni, ony) agreeing",
                    "personal pronoun (Slovak: ja, ty, on, ona, ono, my, vy, oni, ony; Czech: já, ty, on, ona, ono, my, vy, oni, ony) agreeing"))
assert REWRITE != REWRITE_2A and REWRITE.count("Czech") == 3

# ---------------------------------------------------------------- data
S = json.load(open(f"{H}/sample_2b.json", encoding="utf-8"))["rows"]
D = json.load(open(f"{H}/derived_2b.json", encoding="utf-8"))
DR = {r["n"]: r for r in D["rows"]}
FB = D["model_fallback_ns"]
assert len(S) == 200 and len(FB) == 97
BY = {r["n"]: r for r in S}
dv = lambda n, f: DR[n]["derived"][f]["value"]
line = lambda o: json.dumps(o, ensure_ascii=False)
ROWS = {
  "gold_sk": [line({"n": r["n"], "sk": r["src"]}) for r in S if r["lang"] == "sk"],
  "gold_cz": [line({"n": r["n"], "cz": r["src"]}) for r in S if r["lang"] == "cz"],
  "lk_judge": [line({"n": r["n"], "en": r["en"], "correct_answer_en": r["correct_answer_en"]}) for r in S],
  "rewrite_fallback": [line({"n": n, "lang": BY[n]["lang"], "sk": BY[n]["src"], "en": BY[n]["en"]}) for n in FB],
  "v_sk": [line({"n": r["n"], "src": r["src"], "en": r["en"], "lk": r["correct_answer_en"], "tf": dv(r["n"], "tf"),
                 "person": dv(r["n"], "person"), "voice": dv(r["n"], "voice_sk")}) for r in S if r["lang"] == "sk"],
  "v_cz": [line({"n": r["n"], "src": r["src"], "en": r["en"], "lk": r["correct_answer_en"], "tf": dv(r["n"], "tf"),
                 "person": dv(r["n"], "person"), "voice": dv(r["n"], "voice_sk")}) for r in S if r["lang"] == "cz"],
}
HEAD = {"gold_sk": GOLD("sk"), "gold_cz": GOLD("cz"), "lk_judge": LK, "rewrite_fallback": REWRITE,
        "v_sk": VPROMPT("sk"), "v_cz": VPROMPT("cz")}
ORDER = ["gold_sk", "gold_cz", "lk_judge", "rewrite_fallback", "v_sk", "v_cz"]
PROMPT_SHA = {k: hashlib.sha256(HEAD[k].encode()).hexdigest()[:16] for k in ORDER}

# ---------------------------------------------------------------- run (session/commit/usage copied from 2A)
env = dict(os.environ)
if not env.get("CLAUDE_CODE_OAUTH_TOKEN"):
    env["CLAUDE_CODE_OAUTH_TOKEN"] = subprocess.run(["zsh", "-ic", 'printf %s "$CLAUDE_CODE_OAUTH_TOKEN"'], capture_output=True, text=True).stdout
if not env.get("CLAUDE_CODE_OAUTH_TOKEN"):
    open(f"{H}/SPAWN_ERROR.txt", "w").write("STOP: CLAUDE_CODE_OAUTH_TOKEN empty; 0 sessions spent\n"); print("STOP token empty"); sys.exit(2)
LOCK = threading.Lock(); GIT = threading.Lock()
STATE = {"tok": 0, "inflight": 0, "sessions": [], "refused": [], "t0": time.time(), "ok": 0, "stop": None}
LOG = open(f"{H}/run_2b.log", "a", buffering=1)
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
        if STATE["stop"]:
            STATE["refused"].append(name); log("STOP-SKIP", name); return None, None
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
                if out is not None and p.returncode == 0: STATE["ok"] += 1
                elif STATE["ok"] == 0 and usage_total(rec) == 0 and not STATE["stop"]:
                    STATE["stop"] = f"first spawn failed: session {name} exit {p.returncode}; parse_error={rec['parse_error']!r}; stderr={rec['stderr']!r}; result={txt[:300]!r}"
                    open(f"{H}/SPAWN_ERROR.txt", "w").write(STATE["stop"] + "\n")
            recs.append(rec); log("DONE", name, "att", attempt, "exit", p.returncode, "tok", usage_total(rec), "cum", STATE["tok"], "ok", out is not None)
            commit([fn], f"Phase 2B: session {name}{'' if attempt == 1 else ' (retry)'}")
            if out is not None and p.returncode == 0: return rec, out
            with LOCK:
                if STATE["stop"] or STATE["tok"] + (STATE["inflight"]) * EST > CAP: break
        return recs[-1], None
    finally:
        with LOCK: STATE["inflight"] -= 1

log("START", "cap", CAP, "est", EST, "prompts", PROMPT_SHA, {k: len(v) for k, v in ROWS.items()})
with cf.ThreadPoolExecutor(PAR) as ex:
    fs = {ex.submit(session, k, HEAD[k] + "\n".join(ROWS[k])): k for k in ORDER}
    RESULTS = {fs[f]: f.result() for f in cf.as_completed(fs)}
merged = {}
for k in ORDER:
    rec, out = RESULTS.get(k, (None, None))
    merged[k] = {str(o["n"]): o for o in (out or []) if isinstance(o, dict) and "n" in o}
RUN = {"model": MODEL, "parallel": PAR, "cap": CAP, "est": EST, "prompt_sha": PROMPT_SHA, "gemini_calls": 0,
       "wall_s": round(time.time() - STATE["t0"], 1), "tokens_headless_total": STATE["tok"], "sessions": STATE["sessions"],
       "refused": STATE["refused"], "stop": STATE["stop"],
       "rows_per_session": {k: len(v) for k, v in ROWS.items()},
       "chars": {k: {"head": len(HEAD[k]), "rows": len("\n".join(ROWS[k]))} for k in ORDER},
       "returned": {k: len(v) for k, v in merged.items()}, "outputs": merged}
json.dump(RUN, open(f"{H}/run_2b_results.json", "w"), ensure_ascii=False, indent=1)
open(f"{H}/RUN_DONE", "w").write(time.strftime("%Y-%m-%dT%H:%M:%S"))
commit([f"{H}/run_2b_results.json", f"{H}/run_2b.log", f"{H}/RUN_DONE"] + ([f"{H}/SPAWN_ERROR.txt"] if STATE["stop"] else []),
       f"Phase 2B: run results ({STATE['tok']} headless tokens{', STOP' if STATE['stop'] else ''})")
log("END", "tok", STATE["tok"], "stop", STATE["stop"], "returned", RUN["returned"])
