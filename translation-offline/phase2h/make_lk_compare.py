#!/usr/bin/env python3
"""Static (0 tokens): writes LK_INVOCATION_COMPARE.md - the lk headless invocation of 2D, 2G and 2H compared."""
import ast, os, hashlib, json
H = os.path.dirname(os.path.abspath(__file__)); TO = os.path.dirname(H)
F = [("2D phase2d/run_2d_lk.py", os.path.join(TO, "phase2d", "run_2d_lk.py")),
     ("2G phase2g/partB/run_2g_lk.py", os.path.join(TO, "phase2g", "partB", "run_2g_lk.py")),
     ("2H phase2h/run_2h.py", os.path.join(H, "run_2h.py"))]
def info(p):
    src = open(p, encoding="utf-8").read(); tree = ast.parse(src); d = {}
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and ast.unparse(n.func) == "subprocess.run" and n.args and isinstance(n.args[0], ast.List) \
                and n.args[0].elts and ast.unparse(n.args[0].elts[0]) == "BIN":
            d["argv"] = ast.unparse(n.args[0])
            for k in n.keywords: d["kw " + k.arg] = ast.unparse(k.value)
    env = {}
    for n in tree.body:
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
            nm = n.targets[0].id
            if nm in ("BIN", "MODEL"): d[nm] = ast.unparse(n.value)
            if nm in ("LK_2B", "SCHEMA_2B", "SCHEMA_2D", "EXTRA", "LK_2D"):
                exec(compile(ast.Module([n], []), p, "exec"), env)
    d["LK_2D sha16"] = hashlib.sha256(env["LK_2D"].encode()).hexdigest()[:16]
    d["LK_2D chars"] = str(len(env["LK_2D"]))
    for l in src.splitlines():
        s = l.strip()
        if 'LK_2D + "\\n".join(' in s: d["prompt assembly"] = s.replace("prompt = ", "").replace("return ", "")
        if '"zsh", "-ic"' in s: d["token load"] = s
        if s.startswith("ENV = "): d["env"] = s
    d["stdin"] = "none (prompt passed as argv after -p; no input=)" if "kw input" not in d else d["kw input"]
    return d
I = [(t, info(p)) for t, p in F]
keys = sorted(set().union(*[set(d) for _, d in I]))
md = ["# LK invocation compare - 2D vs 2G vs 2H (static, 0 tokens)", "",
      "Extracted with `ast` from the three files (the `subprocess.run([BIN, ...])` call of the lk session, module constants, "
      "the prompt assembly line, the token load line); `LK_2D` is rebuilt by executing only its defining assignments.", ""]
diffs = []
for k in keys:
    vals = [d.get(k, "(absent)") for _, d in I]
    same = len(set(vals)) == 1
    md += ["## %s - %s" % (k, "identical" if same else "DIFFERENT"), ""]
    for (t, _), v in zip(I, vals):
        md.append("* %s: `%s`" % (t, v))
    md.append("")
    if not same: diffs.append(k)
md += ["## Verdict", "",
       "* lk prompt sha16: %s (asserted == 5fa910459c078539: %s)" % (", ".join(d["LK_2D sha16"] for _, d in I), all(d["LK_2D sha16"] == "5fa910459c078539" for _, d in I)),
       "* differences: %s" % (", ".join(diffs) or "none - identical"),
       "* notes: `cwd` is the text `H` in 2D/2G (their own script dir) and `SCRIPT_DIR` (phase2h) in 2H - three different "
       "directories inside the same git repo, so the same CLAUDE.md chain applies; `timeout` is absent in the 2D/2G lk call "
       "(2G's annotation call had one) and is WALL_CAP_S = 1800 s in 2H, where one call serves both stages. The argv list, "
       "binary, model, output format, max-turns, env (os.environ + the zsh-loaded OAuth token), no stdin and the prompt "
       "assembly are byte-identical; 2H takes `en`/`correct_answer_en` from selection_2c.jsonl, 2G from the annotation rows "
       "(2G asserted they equal selection_2c's), and test_2h.py T11 proves the assembled prompts byte-identical to 2G's stored ones.", ""]
open(os.path.join(H, "LK_INVOCATION_COMPARE.md"), "w", encoding="utf-8").write("\n".join(md))
print(json.dumps({"differences": diffs, "sha16": [d["LK_2D sha16"] for _, d in I], "argv": [d.get("argv") for _, d in I]}))
