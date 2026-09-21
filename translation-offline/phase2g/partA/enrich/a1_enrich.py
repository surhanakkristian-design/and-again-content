#!/usr/bin/env python3
"""Phase 2G Part A1 - enrich references. ONE headless Claude session; it sees ONLY {sid, sk, refs}."""
import json, os, re, subprocess, sys, time
TOFF = os.path.expanduser('~/Projects/and-again-content/translation-offline')
A = os.path.join(TOFF, 'phase2g', 'partA'); E = os.path.join(A, 'enrich')
BIN = os.path.expanduser('~/Library/Application Support/Claude/claude-code/2.1.275/claude.app/Contents/MacOS/claude')
ann = json.load(open(os.path.join(TOFF, 'phase2f/p3/probe/data/annotations.json')))
sen = json.load(open(os.path.join(TOFF, 'phase2f/p3/probe/data/sentences.json')))
inp = []
for s in sen:
    a = ann[str(s['sid'])]; hy = a.get('hygienised', a)
    refs = []
    for v in hy.get('v') or []:
        if isinstance(v, str) and v.strip() and v.strip() not in refs: refs.append(v.strip())
    inp.append({'sid': s['sid'], 'sk': s['slovak'], 'refs': refs})
json.dump(inp, open(os.path.join(E, 'enrich_input.json'), 'w'), ensure_ascii=False, indent=1)
PROMPT = """You write extra English reference translations for Slovak sentences.
Read the file enrich_input.json in the current directory. It is a JSON list of objects {sid, sk, refs}:
sk = a Slovak sentence, refs = the English rendering(s) already accepted for it (the first is the main one).
For EVERY object, write exactly (3 - number of refs) NEW English renderings (none if it already has 3 or more), so that each sentence ends with 3.
Each new rendering must be a complete, natural, faithful English translation of the Slovak: same meaning, same persons and subjects, same number, same definiteness where Slovak makes it clear,
same time frame and tense as the main reference (present stays present, past stays past, future stays future), same voice where it matters; vary only wording, word order, synonyms, contractions or legitimately alternative constructions.
Never add or drop content. Never repeat an existing ref. Keep interjections/second sentences if the Slovak has them.
Write the result with the Write tool to enrich_output.json in the current directory as ONE JSON object mapping the sid (as a string) to a list of the new English strings, e.g. {"220001": ["...", "..."], ...}. Include every sid, even with an empty list.
No other files, no commentary; the file must parse as JSON."""
def tok():
    return subprocess.run(['zsh', '-ic', 'printf %s "$CLAUDE_CODE_OAUTH_TOKEN"'], capture_output=True, text=True).stdout.strip()
T = tok()
state = {'t0': time.time()}
if not T or not os.path.exists(BIN):
    state['status'] = 'SPAWN_FAIL: ' + ('no token' if not T else 'no binary'); json.dump(state, open(os.path.join(E, 'a1_state.json'), 'w')); sys.exit(2)
env = {k: v for k, v in os.environ.items() if not (k.startswith('CLAUDECODE') or k.startswith('CLAUDE_CODE_SDK') or k in ('CLAUDE_CODE_ENTRYPOINT', 'ANTHROPIC_API_KEY'))}
env['CLAUDE_CODE_OAUTH_TOKEN'] = T; env['CLAUDE_CODE_MAX_OUTPUT_TOKENS'] = '64000'
open(os.path.join(E, 'enrich.prompt.md'), 'w').write(PROMPT)
cmd = [BIN, '-p', PROMPT, '--output-format', 'json', '--max-turns', '12', '--model', 'opus', '--permission-mode', 'acceptEdits',
       '--allowedTools', 'Read,Write', '--disallowedTools', 'Bash,Glob,Grep,WebFetch,WebSearch,Task,NotebookEdit']
out, err = os.path.join(E, 'enrich_session.json'), os.path.join(E, 'enrich_session.err')
p = subprocess.Popen(cmd, cwd=E, env=env, stdout=open(out, 'w'), stderr=open(err, 'w'), stdin=subprocess.DEVNULL)
try: p.wait(timeout=1500)
except subprocess.TimeoutExpired: p.kill(); p.wait(); state['killed'] = True
for f in (out, err):
    s = open(f, errors='replace').read(); t = s.replace(T, '[REDACTED]'); t = re.sub(r'sk-ant-[A-Za-z0-9_\-]+', 'sk-ant-[REDACTED]', t)
    if t != s: open(f, 'w').write(t)
try: j = json.load(open(out))
except Exception: j = {}
state.update({'exit': p.returncode, 'wall_s': round(time.time() - state['t0'], 1), 'is_error': j.get('is_error'), 'subtype': j.get('subtype'),
              'num_turns': j.get('num_turns'), 'usage': j.get('usage'), 'total_cost_usd': j.get('total_cost_usd'),
              'result_head': str(j.get('result'))[:300], 'stderr_head': open(err, errors='replace').read()[:300]})
txt = (state['result_head'] + ' ' + state['stderr_head']).lower()
if (j.get('is_error') or p.returncode) and re.search(r'usage limit|rate limit|quota|limit reached|hit your limit|out of extra usage', txt):
    state['status'] = 'USAGE_LIMIT'
elif os.path.exists(os.path.join(E, 'enrich_output.json')):
    state['status'] = 'OK'
else:
    state['status'] = 'FAIL'
json.dump(state, open(os.path.join(E, 'a1_state.json'), 'w'), indent=1)
