# LK invocation compare - 2D vs 2G vs 2H (static, 0 tokens)

Extracted with `ast` from the three files (the `subprocess.run([BIN, ...])` call of the lk session, module constants, the prompt assembly line, the token load line); `LK_2D` is rebuilt by executing only its defining assignments.

## BIN - identical

* 2D phase2d/run_2d_lk.py: `os.path.expanduser('~/Library/Application Support/Claude/claude-code/2.1.275/claude.app/Contents/MacOS/claude')`
* 2G phase2g/partB/run_2g_lk.py: `os.path.expanduser('~/Library/Application Support/Claude/claude-code/2.1.275/claude.app/Contents/MacOS/claude')`
* 2H phase2h/run_2h.py: `os.path.expanduser('~/Library/Application Support/Claude/claude-code/2.1.275/claude.app/Contents/MacOS/claude')`

## LK_2D chars - identical

* 2D phase2d/run_2d_lk.py: `1066`
* 2G phase2g/partB/run_2g_lk.py: `1066`
* 2H phase2h/run_2h.py: `1066`

## LK_2D sha16 - identical

* 2D phase2d/run_2d_lk.py: `5fa910459c078539`
* 2G phase2g/partB/run_2g_lk.py: `5fa910459c078539`
* 2H phase2h/run_2h.py: `5fa910459c078539`

## MODEL - identical

* 2D phase2d/run_2d_lk.py: `'opus'`
* 2G phase2g/partB/run_2g_lk.py: `'opus'`
* 2H phase2h/run_2h.py: `'opus'`

## argv - identical

* 2D phase2d/run_2d_lk.py: `[BIN, '-p', prompt, '--output-format', 'json', '--max-turns', '12', '--model', MODEL]`
* 2G phase2g/partB/run_2g_lk.py: `[BIN, '-p', prompt, '--output-format', 'json', '--max-turns', '12', '--model', MODEL]`
* 2H phase2h/run_2h.py: `[BIN, '-p', prompt, '--output-format', 'json', '--max-turns', '12', '--model', MODEL]`

## env - identical

* 2D phase2d/run_2d_lk.py: `ENV = dict(os.environ)`
* 2G phase2g/partB/run_2g_lk.py: `ENV = dict(os.environ)`
* 2H phase2h/run_2h.py: `ENV = dict(os.environ)`

## kw capture_output - identical

* 2D phase2d/run_2d_lk.py: `True`
* 2G phase2g/partB/run_2g_lk.py: `True`
* 2H phase2h/run_2h.py: `True`

## kw cwd - DIFFERENT

* 2D phase2d/run_2d_lk.py: `H`
* 2G phase2g/partB/run_2g_lk.py: `H`
* 2H phase2h/run_2h.py: `SCRIPT_DIR`

## kw env - identical

* 2D phase2d/run_2d_lk.py: `ENV`
* 2G phase2g/partB/run_2g_lk.py: `ENV`
* 2H phase2h/run_2h.py: `ENV`

## kw text - identical

* 2D phase2d/run_2d_lk.py: `True`
* 2G phase2g/partB/run_2g_lk.py: `True`
* 2H phase2h/run_2h.py: `True`

## kw timeout - DIFFERENT

* 2D phase2d/run_2d_lk.py: `(absent)`
* 2G phase2g/partB/run_2g_lk.py: `(absent)`
* 2H phase2h/run_2h.py: `timeout`

## prompt assembly - identical

* 2D phase2d/run_2d_lk.py: `LK_2D + "\n".join(line({"n": r["n"], "en": r["en"], "correct_answer_en": r["lk_supplied"]}) for r in rows)`
* 2G phase2g/partB/run_2g_lk.py: `LK_2D + "\n".join(line({"n": r["n"], "en": r["en"], "correct_answer_en": r["lk_supplied"]}) for r in rows)`
* 2H phase2h/run_2h.py: `LK_2D + "\n".join(line({"n": r["n"], "en": r["en"], "correct_answer_en": r["lk_supplied"]}) for r in rows)`

## stdin - identical

* 2D phase2d/run_2d_lk.py: `none (prompt passed as argv after -p; no input=)`
* 2G phase2g/partB/run_2g_lk.py: `none (prompt passed as argv after -p; no input=)`
* 2H phase2h/run_2h.py: `none (prompt passed as argv after -p; no input=)`

## token load - identical

* 2D phase2d/run_2d_lk.py: `["zsh", "-ic", 'printf %s "$CLAUDE_CODE_OAUTH_TOKEN"'], capture_output=True, text=True).stdout.strip()`
* 2G phase2g/partB/run_2g_lk.py: `["zsh", "-ic", 'printf %s "$CLAUDE_CODE_OAUTH_TOKEN"'], capture_output=True, text=True).stdout.strip()`
* 2H phase2h/run_2h.py: `["zsh", "-ic", 'printf %s "$CLAUDE_CODE_OAUTH_TOKEN"'], capture_output=True, text=True).stdout.strip()`

## Verdict

* lk prompt sha16: 5fa910459c078539, 5fa910459c078539, 5fa910459c078539 (asserted == 5fa910459c078539: True)
* differences: kw cwd, kw timeout
* notes: `cwd` is the text `H` in 2D/2G (their own script dir) and `SCRIPT_DIR` (phase2h) in 2H - three different directories inside the same git repo, so the same CLAUDE.md chain applies; `timeout` is absent in the 2D/2G lk call (2G's annotation call had one) and is WALL_CAP_S = 1800 s in 2H, where one call serves both stages. The argv list, binary, model, output format, max-turns, env (os.environ + the zsh-loaded OAuth token), no stdin and the prompt assembly are byte-identical; 2H takes `en`/`correct_answer_en` from selection_2c.jsonl, 2G from the annotation rows (2G asserted they equal selection_2c's), and test_2h.py T11 proves the assembled prompts byte-identical to 2G's stored ones.
