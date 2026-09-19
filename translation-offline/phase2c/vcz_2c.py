#!/usr/bin/env python3
"""Phase 2C §2 / GATE 2: the v_cz session 2B never got to run (its in-flight budget check refused it twice).
ONE headless session, N = 100 (the 100 Czech rows of 2B's sample). Prompt construction copied verbatim from
phase2b/run_2b.py (VPROMPT("cz") + the same row JSON); the copy is verified byte-for-byte against the stored
v_sk prompt before anything is spent. Token loaded via `zsh -ic` exactly as 2A/2B did and never printed.
HARD CAP 200,000, EST 60,000. If the spawn fails: STOP at 0 cost. 0 Gemini calls, 0 DB access."""
import json, os, re, sys, time, hashlib, subprocess
sys.dont_write_bytecode = True
H = os.path.dirname(os.path.abspath(__file__)); BASE = os.path.dirname(H); REPO = os.path.dirname(BASE)
B2 = f"{BASE}/phase2b"
BIN = os.path.expanduser("~/Library/Application Support/Claude/claude-code/2.1.275/claude.app/Contents/MacOS/claude")
MODEL = "opus"; CAP = 200_000; EST = 60_000
os.makedirs(f"{H}/sessions", exist_ok=True)

LNAME = {"sk": "Slovak", "cz": "Czech"}
def VPROMPT(lang):  # verbatim from phase2b/run_2b.py
    L = LNAME[lang]
    return f"""You are the annotation agent of a {L}->English translation-checking pipeline. Every field except v is already
supplied. For each row you get the {L} sentence "src", the English reference "en", its key phrase "lk" and the known
tf / person / voice (null = not derived). Write ONLY the v field: 1-2 acceptable English translations of src; v[0] MUST be
the reference en verbatim; add a second only if a clearly different acceptable translation exists. lk = the key verb phrase
of each v (lk[0] = the supplied lk).
Reply with ONLY a JSON array, one object per row: {{"n": int, "v": [str], "lk": [str]}}. No prose, no fences.
Rows:
"""
S = json.load(open(f"{B2}/sample_2b.json", encoding="utf-8"))["rows"]
D = json.load(open(f"{B2}/derived_2b.json", encoding="utf-8"))
DR = {r["n"]: r for r in D["rows"]}
dv = lambda n, f: DR[n]["derived"][f]["value"]
line = lambda o: json.dumps(o, ensure_ascii=False)
ROWS = {lg: [line({"n": r["n"], "src": r["src"], "en": r["en"], "lk": r["correct_answer_en"], "tf": dv(r["n"], "tf"),
                   "person": dv(r["n"], "person"), "voice": dv(r["n"], "voice_sk")}) for r in S if r["lang"] == lg]
        for lg in ("sk", "cz")}
PROMPT = {lg: VPROMPT(lg) + "\n".join(ROWS[lg]) for lg in ("sk", "cz")}
VSK = json.load(open(f"{B2}/sessions/v_sk.json", encoding="utf-8"))
if PROMPT["sk"] != VSK["prompt"]:
    open(f"{H}/SPAWN_ERROR.txt", "w").write("STOP: rebuilt v_sk prompt != phase2b/sessions/v_sk.json prompt; 0 tokens spent\n")
    sys.exit("STOP: prompt construction does not reproduce v_sk byte-for-byte; 0 spent")
assert len(ROWS["cz"]) == 100

env = dict(os.environ)
if not env.get("CLAUDE_CODE_OAUTH_TOKEN"):
    env["CLAUDE_CODE_OAUTH_TOKEN"] = subprocess.run(["zsh", "-ic", 'printf %s "$CLAUDE_CODE_OAUTH_TOKEN"'], capture_output=True, text=True).stdout
if not env.get("CLAUDE_CODE_OAUTH_TOKEN"):
    open(f"{H}/SPAWN_ERROR.txt", "w").write("STOP: CLAUDE_CODE_OAUTH_TOKEN empty; 0 sessions spent\n"); sys.exit("STOP token empty")
if EST > CAP: sys.exit("STOP: pre-check projects more than the cap; 0 spent")

t0 = time.time()
p = subprocess.run([BIN, "-p", PROMPT["cz"], "--output-format", "json", "--max-turns", "12", "--model", MODEL],
                   capture_output=True, text=True, env=env, cwd=H)
try: j = json.loads(p.stdout)
except Exception: j = {"parse_error": p.stdout[-500:], "stderr": re.sub(r"sk-ant-\S+", "sk-ant-REDACTED", p.stderr[-500:])}
u = j.get("usage", {}) or {}
rec = {"session": "v_cz", "attempt": 1, "exit": p.returncode, "wall_s": round(time.time() - t0, 1),
       "duration_ms": j.get("duration_ms"), "num_turns": j.get("num_turns"), "total_cost_usd": j.get("total_cost_usd"),
       "is_error": j.get("is_error"),
       **{k: u.get(k, 0) for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens")},
       "modelUsage": j.get("modelUsage"), "parse_error": j.get("parse_error"), "stderr": j.get("stderr")}
txt = j.get("result", "") or ""
try: out = json.loads(txt[txt.find("["):txt.rfind("]") + 1])
except Exception: out = None; rec["result_unparsable"] = txt[:300]
json.dump({"meta": rec, "prompt": PROMPT["cz"], "result": txt}, open(f"{H}/sessions/v_cz_measure.json", "w"), ensure_ascii=False, indent=1)

tot = lambda r: sum(r.get(k) or 0 for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens"))
sk = VSK["meta"]
def figs(r, n=100):
    t = tot(r); ex = t - (r.get("cache_read_input_tokens") or 0)
    return {"input": r["input_tokens"], "output": r["output_tokens"], "cache_creation": r["cache_creation_input_tokens"],
            "cache_read": r["cache_read_input_tokens"], "total": t, "tok_per_sent_incl_cache_read": round(t / n, 1),
            "tok_per_sent_excl_cache_read": round(ex / n, 1), "output_per_sent": round(r["output_tokens"] / n, 1),
            "wall_s": r.get("wall_s")}
F = {"v_cz": figs(rec), "v_sk_2b_run2": figs(sk)}
ok = out is not None and p.returncode == 0
BY = {r["n"]: r for r in S}
q = {}
if ok:
    rows = {o["n"]: o for o in out if isinstance(o, dict) and "n" in o}
    q = {"rows_returned": len(rows),
         "lk0_copied_unchanged": sum(1 for n, o in rows.items() if (o.get("lk") or [None])[0] == BY[n]["correct_answer_en"]),
         "v0_is_reference": sum(1 for n, o in rows.items() if (o.get("v") or [None])[0] == BY[n]["en"]),
         "two_variants": sum(1 for o in rows.values() if len(o.get("v") or []) > 1)}
gate = "pass" if F["v_cz"]["tok_per_sent_incl_cache_read"] <= 700 else "FAIL"
# §4 re-extrapolation with the measured v_cz on the cz half (2B: v 476.7 + fallback 268.5 + lk 245.6 + nulls 42.6 E)
v_sk_ps = F["v_sk_2b_run2"]["tok_per_sent_incl_cache_read"]; v_cz_ps = F["v_cz"]["tok_per_sent_incl_cache_read"]
v_sk_ex = F["v_sk_2b_run2"]["tok_per_sent_excl_cache_read"]; v_cz_ex = F["v_cz"]["tok_per_sent_excl_cache_read"]
OTHER = 268.5 + 245.6 + 42.6; OTHER_EX = 584.2 - 252.1  # 2B's excl-cache total minus its v part
def extrap(nsent):
    half = nsent / 2
    a = half * (v_sk_ps + OTHER) + half * (v_cz_ps + OTHER)
    b = half * (v_sk_ex + OTHER_EX) + half * (v_cz_ex + OTHER_EX)
    return {"sentences": nsent, "tok_per_sent_mean": round(a / nsent, 1), "tokens_all": round(a),
            "tokens_excl_cache_read": round(b), "tokens_all_M": round(a / 1e6, 2)}
json.dump({"n": 100, "language": "cz", "model": MODEL, "cap": CAP, "est": EST, "session_ok": ok,
           "prompt_sha16": hashlib.sha256(VPROMPT("cz").encode()).hexdigest()[:16],
           "prompt_construction_verified_against": "phase2b/sessions/v_sk.json (byte-identical rebuild of the v_sk prompt)",
           "figures": F, "quality": q, "lk0_note": "2B SCORE #5: v copied lk[0] unchanged on 100/100 sk rows",
           "gate2": gate, "gate2_bar": "v_cz <= 700 tok/sent incl. cache reads",
           "reextrapolation_sk_plus_cz": {"basis": "2B §4 per-sentence components, v_sk and v_cz each measured; "
                                                   "rewrite fallback 268.5 + lk judge 245.6 + residual nulls 42.6 (E) unchanged",
                                          "phase2c_selection_8128": extrap(8128), "brief_figure_8218": extrap(8218),
                                          "target_14400": extrap(14400), "2b_reported_8218_all_M": 8.49},
           "headless_tokens_spent": tot(rec)},
          open(f"{H}/vcz_2c.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps({"ok": ok, "gate2": gate, "figs": F, "quality": q, "spent": tot(rec),
                  "extrap": extrap(8128)}, ensure_ascii=False))
