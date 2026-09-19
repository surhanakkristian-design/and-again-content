#!/usr/bin/env python3
"""Phase 2B: run 1 vs run 2 of the same 5 sessions (run 2 was an unintended full re-run, see DEFECTS_score.md #1).
Reads run-1 session files from git history (first commit of each sessions/*.json) and run-2 files from disk. 0 calls."""
import json, subprocess, re, os, collections
REPO = os.path.expanduser("~/Projects/and-again-content"); P = "translation-offline/phase2b"
def git(*a): return subprocess.run(["git", *a], cwd=REPO, capture_output=True, text=True).stdout
def parse(txt):
    try: return {int(o["n"]): o for o in json.loads(txt[txt.find("["):txt.rfind("]") + 1])}
    except Exception: return {}
OUT = {"sessions": {}}
S = {}
for s in ("gold_sk", "gold_cz", "lk_judge", "rewrite_fallback", "v_sk"):
    hs = git("log", "--format=%h", "--reverse", "--", f"{P}/sessions/{s}.json").split()
    r1 = json.loads(git("show", f"{hs[0]}:{P}/sessions/{s}.json")); r2 = json.load(open(f"{REPO}/{P}/sessions/{s}.json"))
    tot = lambda m: sum(m.get(k) or 0 for k in ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens"))
    OUT["sessions"][s] = {"run1_commit": hs[0], "run2_commit": hs[-1], "run1_tok": tot(r1["meta"]), "run2_tok": tot(r2["meta"]),
                          "run1_out": r1["meta"]["output_tokens"], "run2_out": r2["meta"]["output_tokens"],
                          "run1_s": (r1["meta"]["duration_ms"] or 0) / 1000, "run2_s": (r2["meta"]["duration_ms"] or 0) / 1000,
                          "same_prompt": r1["prompt"] == r2["prompt"]}
    S[s] = (parse(r1["result"]), parse(r2["result"]))
norm = lambda x: " ".join(re.findall(r"\w+", str(x).lower())) if x is not None else None
g = {}
for s in ("gold_sk", "gold_cz"):
    a, b = S[s]; c = collections.Counter(); ex = 0
    for n in a:
        if n not in b: continue
        for f in ("tf", "person", "number", "gender", "voice", "subject", "tense_open", "perfective_present", "main_sentence_index"):
            c[f] += (norm(a[n].get(f)) == norm(b[n].get(f)))
        ex += all(norm(a[n].get(f)) == norm(b[n].get(f)) for f in ("tf", "person", "voice", "subject"))
    g[s] = {"n": len(a), **c, "exact_tf_person_voice_subject": ex}
OUT["gold_retest"] = g
a, b = S["lk_judge"]; OUT["lk_retest"] = {"n": len(a), "class_same": sum(a[n].get("class") == b.get(n, {}).get("class") for n in a),
                                          "run1": dict(collections.Counter(o.get("class") for o in a.values()))}
a, b = S["rewrite_fallback"]; OUT["rewrite_retest"] = {"n": len(a), "action_same": sum(a[n].get("action") == b.get(n, {}).get("action") for n in a),
    "text_same": sum(a[n].get("sk_new") == b.get(n, {}).get("sk_new") for n in a), "run1": dict(collections.Counter(o.get("action") for o in a.values()))}
a, b = S["v_sk"]; OUT["v_retest"] = {"n": len(a), "v_identical": sum(a[n].get("v") == b.get(n, {}).get("v") for n in a),
    "two_variants_run1": sum(len(o.get("v") or []) > 1 for o in a.values())}
OUT["headless_total_both_runs"] = sum(v["run1_tok"] + v["run2_tok"] for v in OUT["sessions"].values())
json.dump(OUT, open(f"{REPO}/{P}/retest_2b.json", "w"), indent=1)
print(json.dumps(OUT))
