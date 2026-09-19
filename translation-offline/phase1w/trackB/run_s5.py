#!/usr/bin/env python3
"""Phase 1W §5 Track B: honest harness-token measurement of the rewrite + annotation agents, blind gold.
Headless Claude Code sessions (bundled binary, --output-format json, --max-turns 12, --model opus). 0 Gemini calls."""
import json, os, re, subprocess, time, math, concurrent.futures as cf
H = os.path.dirname(os.path.abspath(__file__))
BIN = os.path.expanduser("~/Library/Application Support/Claude/claude-code/2.1.275/claude.app/Contents/MacOS/claude")
MODEL = "opus"; N = 30
rows = json.load(open(f"{H}/sample_raw.json"))["rows"]
for i, r in enumerate(rows, 1): r["n"] = i
batches = [rows[i:i + N] for i in range(0, len(rows), N)]
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
env = dict(os.environ)
if not env.get("CLAUDE_CODE_OAUTH_TOKEN"):
    env["CLAUDE_CODE_OAUTH_TOKEN"] = subprocess.run(["zsh", "-ic", 'printf %s "$CLAUDE_CODE_OAUTH_TOKEN"'], capture_output=True, text=True).stdout

def session(name, prompt):
    t0 = time.time()
    p = subprocess.run([BIN, "-p", prompt, "--output-format", "json", "--max-turns", "12", "--model", MODEL],
                       capture_output=True, text=True, env=env, cwd=H)
    wall = time.time() - t0
    try: j = json.loads(p.stdout)
    except Exception: j = {"parse_error": p.stdout[-500:], "stderr": re.sub(r"sk-ant-\S+", "sk-ant-REDACTED", p.stderr[-500:])}
    u = j.get("usage", {}) or {}
    rec = {"session": name, "exit": p.returncode, "wall_s": round(wall, 1), "duration_ms": j.get("duration_ms"),
           "num_turns": j.get("num_turns"), "total_cost_usd": j.get("total_cost_usd"), "is_error": j.get("is_error"),
           **{k: u.get(k, 0) for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens")},
           "modelUsage": j.get("modelUsage")}
    txt = j.get("result", "") or ""
    try: out = json.loads(txt[txt.find("["):txt.rfind("]") + 1])
    except Exception: out = None; rec["result_unparsable"] = txt[:300]
    json.dump({"meta": rec, "prompt": prompt, "result": txt}, open(f"{H}/session_{name}.json", "w"), ensure_ascii=False, indent=1)
    return rec, out

def fmt(bs, key): return "\n".join(json.dumps({"n": r["n"], "sk": r[key], **({"en": r["en"]} if key != "sk_only" else {})}, ensure_ascii=False) for r in bs)
T0 = time.time()
with cf.ThreadPoolExecutor(4) as ex:
    fr = {ex.submit(session, f"rewrite_b{i+1}", REWRITE + fmt(b, "sk")): ("rw", i) for i, b in enumerate(batches)}
    fg = {ex.submit(session, f"gold_b{i+1}", GOLD + "\n".join(json.dumps({"n": r["n"], "sk": r["sk"]}, ensure_ascii=False) for r in b)): ("gold", i) for i, b in enumerate(batches)}
    res = {v: f.result() for f, v in {**fr, **fg}.items()}
rw = {o["n"]: o for i in range(len(batches)) for o in (res[("rw", i)][1] or [])}
gold = {o["n"]: o for i in range(len(batches)) for o in (res[("gold", i)][1] or [])}
def toks(s): return [w.lower() for w in re.findall(r"\w+", s)]
for r in rows:
    w = rw.get(r["n"], {"action": "U"}); r["rewrite"] = w
    new = w.get("sk_new") or r["sk"]
    if w.get("action") == "R":
        a, b = toks(r["sk"]), toks(new); ok = True
        for t in a:
            if t in b: b.remove(t)
            else: ok = False
        w["machine_check"] = ok and b == [str(w.get("pronoun", "")).lower()]
        if not w["machine_check"]: new = r["sk"]
    r["sk_new"] = new
with cf.ThreadPoolExecutor(2) as ex:
    fa = {ex.submit(session, f"annot_b{i+1}", ANNOT + fmt(b, "sk_new")): i for i, b in enumerate(batches)}
    ares = {i: f.result() for f, i in fa.items()}
ann = {o["n"]: o for i in ares for o in (ares[i][1] or [])}
WALL = time.time() - T0
metas = [res[k][0] for k in sorted(res)] + [ares[i][0] for i in sorted(ares)]

# ---------------- agreement (annotation vs blind gold). After-gold = gold with the inserted main-clause pronoun as subject (1V rule).
def norm(s): return " ".join(toks(s or ""))
def subj_eq(a, b, lenient):
    a, b = norm(a), norm(b)
    if not a or not b: return a == b
    return a == b or (lenient and (a in b or b in a))
F = ["tf", "person", "voice", "agent_nom", "subject_exact", "subject_lenient"]
agree = {f: 0 for f in F}; exact = 0; dis = []; rw_dec = 0; n_cmp = 0
for r in rows:
    g, a, w = gold.get(r["n"]), ann.get(r["n"]), r["rewrite"]
    if not g or not a: dis.append(f"n{r['n']}: missing {'gold' if not g else 'annotation'}"); continue
    n_cmp += 1
    ga = dict(g)
    if w.get("action") == "R" and w.get("machine_check") and w.get("where") == "main" and g.get("voice") == "active_prodrop":
        ga.update(subject=w["pronoun"], voice="active_agent")
    gan = ga.get("voice") == "active_agent"
    rw_dec += ((w.get("action") == "R" and w.get("where") == "main") == (g.get("voice") == "active_prodrop"))
    chk = {"tf": a.get("tf_gold") == ga.get("tf"), "person": a.get("person") == ga.get("person"),
           "voice": a.get("voice_sk") == ga.get("voice"), "agent_nom": bool(a.get("agent_nom")) == gan,
           "subject_exact": subj_eq(a.get("subject"), ga.get("subject"), False),
           "subject_lenient": subj_eq(a.get("subject"), ga.get("subject"), True)}
    for f in F: agree[f] += chk[f]
    allok = all(chk[f] for f in ("tf", "person", "voice", "agent_nom", "subject_lenient")); exact += allok
    if not allok:
        bad = [f"{f}: ann={a.get({'tf':'tf_gold','voice':'voice_sk'}.get(f,f.split('_')[0] if f.startswith('subject') else f))!r} gold={ga.get(f.split('_')[0] if f.startswith('subject') else f, gan if f=='agent_nom' else None)!r}" for f in ("tf", "person", "voice", "agent_nom", "subject_lenient") if not chk[f]]
        dis.append(f"n{r['n']} ({r['exercise_id']}, {r['level']}) {r['sk_new']} | " + "; ".join(bad))

# ---------------- tokens + extrapolation
def stage(prefix):
    ms = [m for m in metas if m["session"].startswith(prefix)]
    s = {k: sum((m.get(k) or 0) for m in ms) for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens", "total_cost_usd", "num_turns")}
    s["duration_s"] = sum((m.get("duration_ms") or 0) for m in ms) / 1000; s["sessions"] = len(ms)
    s["all"] = s["input_tokens"] + s["cache_creation_input_tokens"] + s["cache_read_input_tokens"] + s["output_tokens"]
    s["no_cache_read"] = s["all"] - s["cache_read_input_tokens"]
    s["per_sent_all"] = s["all"] / len(rows); s["per_sent_no_cache_read"] = s["no_cache_read"] / len(rows)
    s["per_sent_output"] = s["output_tokens"] / len(rows); s["per_sent_usd"] = s["total_cost_usd"] / len(rows)
    s["per_sent_s"] = s["duration_s"] / len(rows); return s
ST = {k: stage(k) for k in ("rewrite", "annot", "gold")}
TOT = 5895; B = math.ceil(TOT / N)
ext = {}
for k in ("rewrite", "annot", "gold"):
    s = ST[k]; ext[k] = {"tokens_all": round(s["per_sent_all"] * TOT), "tokens_no_cache_read": round(s["per_sent_no_cache_read"] * TOT),
                         "output": round(s["per_sent_output"] * TOT), "usd": round(s["per_sent_usd"] * TOT, 2),
                         "sessions": B, "serial_hours": round(s["per_sent_s"] * TOT / 3600, 2)}
prod = {f: ext["rewrite"][f] + ext["annot"][f] for f in ("tokens_all", "tokens_no_cache_read", "output", "usd", "sessions", "serial_hours")}
OLD = 662008
out = {"model": MODEL, "batch_N": N, "n": len(rows), "sessions": metas, "stages": ST, "extrapolation_5895": ext, "production_rewrite_plus_annotation": prod,
       "ratio_vs_1V_662008": {"all_tokens": round(prod["tokens_all"] / OLD, 2), "no_cache_read": round(prod["tokens_no_cache_read"] / OLD, 2), "output_only": round(prod["output"] / OLD, 2)},
       "agreement": {"n_compared": n_cmp, **{f: [agree[f], round(100 * agree[f] / max(n_cmp, 1), 2)] for f in F},
                     "exact_match_per_sentence": [exact, round(100 * exact / max(n_cmp, 1), 2)],
                     "rewrite_decision_vs_gold_prodrop": [rw_dec, round(100 * rw_dec / max(n_cmp, 1), 2)]},
       "rewrites": sum(r["rewrite"].get("action") == "R" for r in rows),
       "rewrite_machine_check_fail": [r["n"] for r in rows if r["rewrite"].get("action") == "R" and not r["rewrite"].get("machine_check")],
       "disagreements": dis, "driver_wall_s": round(WALL, 1), "gemini_calls": 0}
json.dump(out, open(f"{H}/s5_results.json", "w"), ensure_ascii=False, indent=1)
json.dump({"rows": rows, "gold": gold, "annotation": ann}, open(f"{H}/s5_rows.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in out.items() if k not in ("disagreements",)}, ensure_ascii=False, default=str)[:6000])
print("\n".join(dis[:40]))
