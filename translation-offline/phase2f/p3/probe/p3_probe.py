#!/usr/bin/env python3
"""Phase 2F PART 3.1 - the Slovak PRODUCTION-sentence PROBE.

One resumable driver.  Writes phase2f/p3/probe/PROBE_SLOVAK_PRODUCTION.md + probe_result.json in
EVERY outcome, including a 0-call stop.

Method (brief verbatim):
  * 60 Slovak sentences from phase2d/out/annotations_sk_final.jsonl (READ ONLY) - real uploaded
    production material, stratified across the levels present.
  * ONE blind writer role -> 3 correct + 3 wrong answers per sentence = 360 items.  The writer sees
    only the Slovak sentence, its level and its topic; never the English reference, never the
    annotation.
  * ONE blind judge over all items, shuffled, packets carrying jid / slovak / level / answer /
    topic, with hidden duplicate controls -> judge-noise rate.
  * The FROZEN stack, unchanged: phase1w/stack_1w.py (AG v4 full + v5 rs_nom + TIP determiner rule)
    with reader_nom, L3 = gemini-3.1-flash-lite, temperature 0, thinkingBudget 0, prompt
    P-FROZEN-1U.  phase1w/a4 tooling is copied, never edited in place; only the SET changes.
  * sids 220001..220060 (fresh: 1W used 200001-200100, Part 2 uses 210001-210100).

    python3 p3_probe.py --selftest   # 0 model calls, stub writer + stub judge + stub L3
    python3 p3_probe.py --run        # waits for PART2_RESULT.md, then the real thing, ONCE
"""
import argparse
import collections
import datetime
import json
import os
import random
import re
import shutil
import subprocess
import sys
import time

sys.dont_write_bytecode = True

TOFF = os.path.expanduser('~/Projects/and-again-content/translation-offline')
REPO = os.path.dirname(TOFF)
PROBE = os.path.join(TOFF, 'phase2f', 'p3', 'probe')
SET = os.path.join(PROBE, 'set')
DATA = os.path.join(PROBE, 'data')
RUN = os.path.join(PROBE, 'run')
SESS = os.path.join(PROBE, 'sessions')
U = os.path.join(TOFF, 'phase1u', 'run')
SRC_JSONL = os.path.join(TOFF, 'phase2d', 'out', 'annotations_sk_final.jsonl')
PART2_RESULT = os.path.join(TOFF, 'phase2f', 'p2', 'PART2_RESULT.md')
BUDGET = os.path.join(TOFF, 'phase2f', 'GEMINI_BUDGET.json')
LOG = os.path.join(PROBE, 'driver_p31.log')
STATE = os.path.join(PROBE, 'driver_state.json')
BIN = os.path.expanduser('~/Library/Application Support/Claude/claude-code/2.1.275/claude.app/'
                         'Contents/MacOS/claude')
COAUTH = 'Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>'

SEED = 20260921            # fresh seed, no earlier phase used it
SID_LO, SID_HI = 220001, 220060
USED_SIDS = [(190001, 190100), (200001, 200100), (210001, 210100)]
LEVELS = ('A1', 'A2', 'B1', 'B2')
PER_LEVEL = 15
N_CORRECT, N_WRONG = 3, 3
WRITER_CHUNK = 15          # 4 sessions of the one writer role
JUDGE_PACKETS = 4
DUP_FRACTION = 0.10
CAP_PHASE = 900
CAP_PART31 = 250          # the brief's approx budget
CAP_PART31_MAX = 320      # local ceiling; the HARD constraint is CAP_PHASE minus part2
WAIT_MAX_S = 10 * 3600
WAIT_POLL_S = 120
# 1W blind-test Slovak, the comparison the brief names
W1_COV = (392, 401, 97.76, 95.78, 98.97)
W1_FA = (16, 499, 3.21, 1.84, 5.15)

TAGS_OK = ('plain', 'determiner', 'aspect', 'number', 'by-passive', 'by-passive-embedded',
           'skp-passive', 'drop-main', 'drop-fronted', 'drop-misaligned', 'drop-other',
           'time-frame', 'missing-article')
TYPES = ('T', 'W', 'M', 'S')

R = {'status': None, 'notes': [], 'defects': [], 'sessions': [], 'stage': 'init',
     'gemini_counted': 0, 'started': datetime.datetime.now().isoformat(timespec='seconds')}
TOK = None


# ====================================================================== small helpers
def say(s):
    line = '[%s] %s' % (datetime.datetime.now().strftime('%H:%M:%S'), s)
    print(line, flush=True)
    try:
        with open(LOG, 'a') as fh:
            fh.write(line + '\n')
    except Exception:
        pass


def save_state():
    try:
        with open(STATE, 'w') as fh:
            json.dump(R, fh, indent=1, ensure_ascii=False, default=str)
    except Exception as e:
        say('save_state failed: %s' % e)


def sh(cmd, cwd=None, env=None):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                       env=env or dict(os.environ, PYTHONDONTWRITEBYTECODE='1'))
    out = (p.stdout or '') + (p.stderr or '')
    say('$ %s -> exit %d' % (' '.join(cmd), p.returncode))
    try:
        with open(LOG, 'a') as fh:
            fh.write(out[-6000:] + '\n')
    except Exception:
        pass
    return p.returncode, out


def jload(p, default=None):
    try:
        return json.load(open(p, encoding='utf-8'))
    except Exception:
        return default


def jdump(o, p):
    d = os.path.dirname(p)
    if d and not os.path.isdir(d):
        os.makedirs(d, exist_ok=True)
    tmp = p + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as fh:
        json.dump(o, fh, indent=1, ensure_ascii=False, default=str)
    os.replace(tmp, p)


def git(*a):
    return sh(['git'] + list(a), cwd=REPO)


def commit(msg):
    git('add', '-A', 'translation-offline/phase2f')
    rc, _ = git('diff', '--cached', '--quiet', '--', 'translation-offline/phase2f')
    if rc != 0:
        git('commit', '-q', '-m', msg + '\n\n' + COAUTH, '--', 'translation-offline/phase2f')
    return git('rev-parse', 'HEAD')[1].strip()


def defect(what, detail):
    R['defects'].append({'what': what, 'detail': detail})
    say('DEFECT recorded (not fixed): %s - %s' % (what, detail))
    save_state()


# ====================================================================== exact Clopper-Pearson
def _betacf(a, b, x):
    tiny, eps = 1e-300, 3e-16
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    if abs(d) < tiny:
        d = tiny
    d = 1.0 / d
    h = d
    for m in range(1, 300):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        c = 1.0 + aa / c
        if abs(d) < tiny:
            d = tiny
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        c = 1.0 + aa / c
        if abs(d) < tiny:
            d = tiny
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        de = d * c
        h *= de
        if abs(de - 1.0) < eps:
            break
    return h


def _lg(x):
    import math
    return math.lgamma(x)


def betai(a, b, x):
    import math
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    bt = math.exp(_lg(a + b) - _lg(a) - _lg(b) + a * math.log(x) + b * math.log(1 - x))
    if x < (a + 1) / (a + b + 2):
        return bt * _betacf(a, b, x) / a
    return 1.0 - bt * _betacf(b, a, 1 - x) / b


def _inv(f, target, lo=0.0, hi=1.0):
    for _ in range(200):
        mid = (lo + hi) / 2
        if f(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def cp(k, n, conf=0.95):
    """Exact Clopper-Pearson two-sided interval, in percent."""
    if not n:
        return {'k': k, 'n': n, 'pct': None, 'ci': [None, None]}
    # DEFECT FIXED (reporting layer only, 0 model calls): betai is INCREASING in p, so the
    # earlier 1 - betai form inverted a decreasing function with a bisection that assumes an
    # increasing one and returned degenerate [0,0] / [100,100] bounds.  Clopper-Pearson is
    # lower = BetaInv(a; k, n-k+1), upper = BetaInv(1-a; k+1, n-k).
    a = (1 - conf) / 2
    lo = 0.0 if k == 0 else _inv(lambda p: betai(k, n - k + 1, p), a)
    hi = 1.0 if k == n else _inv(lambda p: betai(k + 1, n - k, p), 1 - a)
    return {'k': k, 'n': n, 'pct': round(100.0 * k / n, 2),
            'ci': [round(100 * lo, 2), round(100 * hi, 2)]}


def fk(d):
    if not d or not d.get('n'):
        return 'n = %s' % ((d or {}).get('n', 0))
    return '%d/%d = %.2f %% [%.2f, %.2f]' % (d['k'], d['n'], d['pct'], d['ci'][0], d['ci'][1])


# ====================================================================== stage A1: the set (0 calls)
def pick_sentences():
    """READ-ONLY selection from the production annotations, stratified across the levels present."""
    out = os.path.join(SET, 'selection.json')
    old = jload(out)
    if old:
        return old
    rows, seen_ex = [], set()
    with open(SRC_JSONL, encoding='utf-8') as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                d = json.loads(line)
            except Exception:
                continue
            v = [x for x in (d.get('v') or []) if isinstance(x, str) and x.strip()]
            if not (d.get('src') or '').strip() or not v:
                continue
            if d.get('level') not in LEVELS:
                continue
            if d['exercise_id'] in seen_ex:
                continue
            seen_ex.add(d['exercise_id'])
            rows.append(d)
    by_lv = collections.defaultdict(list)
    for d in rows:
        by_lv[d['level']].append(d)
    rng = random.Random(SEED)
    chosen = []
    for L in LEVELS:
        pool = sorted(by_lv[L], key=lambda x: x['exercise_id'])
        take = rng.sample(pool, min(PER_LEVEL, len(pool)))
        chosen += sorted(take, key=lambda x: x['exercise_id'])
    rng.shuffle(chosen)
    sel = {'seed': SEED, 'source': 'phase2d/out/annotations_sk_final.jsonl',
           'source_rows_total': len(rows), 'per_level_requested': PER_LEVEL,
           'pool_by_level': {L: len(by_lv[L]) for L in LEVELS},
           'sid_range': [SID_LO, SID_HI], 'rows': []}
    for n, d in enumerate(chosen):
        sid = SID_LO + n
        for lo, hi in USED_SIDS:
            assert not (lo <= sid <= hi), 'sid %d collides with an earlier phase' % sid
        sel['rows'].append({'sid': sid, 'exercise_id': d['exercise_id'], 'level': d['level'],
                            'topic': d.get('type_title') or 'general',
                            'slovak': d['src'], 'ann': d})
    sel['stratification'] = dict(collections.Counter(r['level'] for r in sel['rows']))
    jdump(sel, out)
    say('selection: %d sentences, stratification %s (pool %s)'
        % (len(sel['rows']), sel['stratification'], sel['pool_by_level']))
    return sel


def alt_dict(ann):
    out = {}
    for a in (ann.get('alt') or []):
        tok = a.get('tok')
        cand = [c for c in (a.get('groups_or_candidates') or [])
                if isinstance(c, str) and c.strip() and c.strip().lower() != str(tok).lower()]
        if tok and cand:
            out[tok] = cand
    return out


def build_data(sel, data_dir):
    """sentences.json / annotations.json in the 1U shapes, from production rows."""
    sents, anns = [], {}
    for r in sel['rows']:
        d, sid = r['ann'], r['sid']
        sents.append({
            'sid': sid, 'pid': 'P31%03d' % (sid - SID_LO + 1), 'slovak': r['slovak'],
            'level': r['level'], 'topic': r['topic'],
            'tags': {'half': 'P1' if sid % 2 else 'P2', 'level': r['level'], 'kind': 'PROD',
                     'emb': bool(d.get('embedded_agents')), 'tf_gold': d.get('tf'),
                     'writer_tags': {'agent_clause': 'main', 'agent': d.get('subject'),
                                     'other_subject': None, 'subordinator': None,
                                     'passivizable': None,
                                     'impersonal_or_passive': d.get('voice') != 'active_agent',
                                     'kind': 'PROD', 'lid': 'p%03d' % (sid - SID_LO + 1)}}})
        hy = {'v': [x for x in (d.get('v') or []) if isinstance(x, str) and x.strip()],
              'lk': [x for x in (d.get('lk') or []) if isinstance(x, str) and x.strip()],
              'alt': alt_dict(d), 'id': sid, 'lv': r['level']}
        anns[str(sid)] = {'voice_sk': d.get('voice'), 'agent_nom': d.get('agent_nom'),
                          'tf_gold': d.get('tf'), 'tense_open': d.get('tense_open'),
                          'perfective_present': d.get('perfective_present'),
                          'hygienised': hy, 'raw': dict(hy)}
    os.makedirs(data_dir, exist_ok=True)
    jdump(sents, os.path.join(data_dir, 'sentences.json'))
    jdump(anns, os.path.join(data_dir, 'annotations.json'))
    return sents, anns


# ====================================================================== the two briefs
ACCEPT_RULES = """ACCEPTANCE RULES (these are the owner's rules, verbatim, and they are the only
rules that decide):
- the Slovak sentence is the ground truth, not the English reference;
- a passive is acceptable;
- a dropped agent where the Slovak names one is WRONG;
- a missing obligatory English article is an ERROR;
- the time frame must match the Slovak while the English tense inside that frame is free;
- a dropped function word is correct, a dropped content word is wrong, added content is wrong."""

WRITER_BRIEF = """You are the blind writer for a measurement of a translation checker.

You see ONLY the Slovak sentence, its CEFR level and its topic. You do NOT see any English
reference translation and you do NOT see any annotation. Do not ask for them; they do not exist
for you. Write from the Slovak alone.

For EACH sentence below, write exactly %d CORRECT English translations and exactly %d WRONG
English translations.

%s

CORRECT answers must be acceptable under those rules, and the three should differ from each other
(different wording, a passive, a different but time-frame-preserving tense, a dropped function
word, and so on) - not three copies of one sentence.

WRONG answers must be wrong under those rules, and each must be wrong for ONE identifiable reason.
Give each wrong answer a type:
  T = the time frame does not match the Slovak (tense inside a matching frame is NOT an error)
  S = the subject/agent is wrong, or an agent the Slovak names is dropped
  M = something the Slovak says is missing in the English - a dropped CONTENT word, or a missing
      obligatory English article
  W = wrong word choice, changed meaning, or added content the Slovak does not have
Make the wrong answers plausible near-misses, not gibberish: a whole-sentence mistranslation
teaches nothing. Keep everything else about the sentence right.

Give every answer a tag from exactly this list:
%s
Use "plain" when nothing more specific fits; "missing-article" for a missing obligatory article;
"time-frame" for a wrong time frame; "drop-main" / "drop-fronted" / "drop-misaligned" /
"drop-other" for a dropped agent; "by-passive" / "by-passive-embedded" for an English by-passive;
"determiner" / "aspect" / "number" for those differences.

Write ONE file, %s, and nothing else. Exact JSON shape:
[
 {"sid": 220001,
  "correct": [{"answer": "...", "tag": "plain"}, {"answer": "...", "tag": "by-passive"},
              {"answer": "...", "tag": "plain"}],
  "wrong":   [{"answer": "...", "tag": "time-frame", "type": "T"},
              {"answer": "...", "tag": "drop-main", "type": "S"},
              {"answer": "...", "tag": "missing-article", "type": "M"}]},
 ...
]
One object per sentence, all %d sentences, in the order given. No commentary, no markdown fence
inside the file - the file must parse as JSON.

THE SENTENCES:
%s
"""

JUDGE_BRIEF = """You are the blind judge for a measurement of a translation checker.

Each packet item gives you a Slovak sentence, its CEFR level, its topic, and ONE English answer.
Judge that answer. You do NOT see who wrote it, whether it was meant to be right or wrong, or any
English reference translation.

%s

Apply those rules and nothing else. In particular: do not mark an answer wrong for being a
passive, for wording you would not have chosen, or for a tense that keeps the Slovak time frame.

For every item output:
  "judged": "correct" or "wrong"
  "type":   null when correct; when wrong, exactly one of
            "T" (time frame does not match the Slovak),
            "S" (subject/agent wrong, or an agent the Slovak names is dropped),
            "M" (a content word the Slovak says is missing, or a missing obligatory article),
            "W" (wrong word choice, changed meaning, or added content)
  "borderline": true if you could argue it either way, otherwise false
  "confidence": an integer 1-5 (1 = a guess, 5 = certain)

Judge every item independently and on its own. Some Slovak sentences appear more than once with
different answers; that is normal and tells you nothing.

Write ONE file, %s, and nothing else. Exact JSON shape:
[{"jid": "q0001", "judged": "wrong", "type": "M", "borderline": false, "confidence": 4}, ...]
All %d items, in the order given. No commentary; the file must parse as JSON.

THE PACKET:
%s
"""


# ====================================================================== headless sessions
def token():
    global TOK
    if TOK is None:
        TOK = subprocess.run(['zsh', '-ic', 'printf %s "$CLAUDE_CODE_OAUTH_TOKEN"'],
                             capture_output=True, text=True).stdout.strip()
    return TOK


def child_env():
    e = {k: v for k, v in os.environ.items()
         if not (k.startswith('CLAUDECODE') or k.startswith('CLAUDE_CODE_SDK')
                 or k in ('CLAUDE_CODE_ENTRYPOINT', 'ANTHROPIC_API_KEY'))}
    t = token()
    if not t:
        return None
    e['CLAUDE_CODE_OAUTH_TOKEN'] = t
    e['CLAUDE_CODE_MAX_OUTPUT_TOKENS'] = '64000'
    e['PYTHONDONTWRITEBYTECODE'] = '1'
    return e


def redact(path):
    if not os.path.exists(path):
        return
    s = open(path, encoding='utf-8', errors='replace').read()
    t = s.replace(TOK, '[REDACTED]') if TOK else s
    t = re.sub(r'sk-ant-[A-Za-z0-9_\-]+', 'sk-ant-[REDACTED]', t)
    if t != s:
        open(path, 'w', encoding='utf-8').write(t)


def spawn(name, prompt):
    env = child_env()
    if env is None:
        return None
    os.makedirs(SESS, exist_ok=True)
    out = os.path.join(SESS, name + '.json')
    err = os.path.join(SESS, name + '.err')
    open(os.path.join(SESS, name + '.prompt.md'), 'w', encoding='utf-8').write(prompt)
    cmd = [BIN, '-p', prompt, '--output-format', 'json', '--max-turns', '12', '--model', 'opus',
           '--permission-mode', 'acceptEdits', '--allowedTools', 'Read,Write',
           '--disallowedTools', 'Bash,Glob,Grep,WebFetch,WebSearch,Task,NotebookEdit']
    p = subprocess.Popen(cmd, cwd=SET, env=env, stdout=open(out, 'w'), stderr=open(err, 'w'),
                         stdin=subprocess.DEVNULL)
    say('spawned headless session %s (pid %d)' % (name, p.pid))
    return {'name': name, 'p': p, 'out': out, 'err': err, 't0': time.time()}


def wait_all(procs, timeout):
    for s in [x for x in procs if x]:
        left = max(1, timeout - (time.time() - s['t0']))
        try:
            s['p'].wait(timeout=left)
        except subprocess.TimeoutExpired:
            s['p'].kill()
            s['p'].wait()
            say('session %s KILLED after %ds' % (s['name'], timeout))
        redact(s['out'])
        redact(s['err'])
        j = jload(s['out'], {}) or {}
        u = j.get('usage') or {}
        rec = {'session': s['name'], 'exit': s['p'].returncode, 'is_error': j.get('is_error'),
               'subtype': j.get('subtype'), 'num_turns': j.get('num_turns'),
               'duration_ms': j.get('duration_ms'), 'total_cost_usd': j.get('total_cost_usd'),
               'input_tokens': u.get('input_tokens'),
               'cache_creation_input_tokens': u.get('cache_creation_input_tokens'),
               'cache_read_input_tokens': u.get('cache_read_input_tokens'),
               'output_tokens': u.get('output_tokens'),
               'models': sorted((j.get('modelUsage') or {}).keys()),
               'permission_denials': len(j.get('permission_denials') or [])}
        if not j:
            rec['stderr_tail'] = open(s['err'], encoding='utf-8', errors='replace').read()[-500:]
        R['sessions'].append(rec)
        say('session %s done: exit %s is_error %s out_tok %s'
            % (s['name'], rec['exit'], rec['is_error'], rec['output_tokens']))
    save_state()


def parse_json_file(path):
    """Tolerant read: a plain JSON file, or one wrapped in a markdown fence."""
    if not os.path.exists(path):
        return None
    s = open(path, encoding='utf-8', errors='replace').read().strip()
    try:
        return json.loads(s)
    except Exception:
        pass
    m = re.search(r'```(?:json)?\s*(.*?)```', s, re.S)
    if m:
        try:
            return json.loads(m.group(1))
        except Exception:
            pass
    for a, b in (('[', ']'), ('{', '}')):
        i, k = s.find(a), s.rfind(b)
        if i >= 0 and k > i:
            try:
                return json.loads(s[i:k + 1])
            except Exception:
                pass
    return None


# ====================================================================== writer
def writer_chunks(sel):
    rows = sel['rows']
    return [rows[i:i + WRITER_CHUNK] for i in range(0, len(rows), WRITER_CHUNK)]


def writer_path(k):
    return os.path.join(SET, 'writers', 'writer_part%d.json' % k)


def writer_valid(k, chunk):
    o = parse_json_file(writer_path(k))
    if not isinstance(o, list):
        return None
    by = {}
    for r in o:
        if not isinstance(r, dict):
            continue
        try:
            sid = int(r.get('sid'))
        except Exception:
            continue
        c = [x for x in (r.get('correct') or []) if isinstance(x, dict) and (x.get('answer') or '').strip()]
        w = [x for x in (r.get('wrong') or []) if isinstance(x, dict) and (x.get('answer') or '').strip()]
        if len(c) >= N_CORRECT and len(w) >= N_WRONG:
            by[sid] = {'correct': c[:N_CORRECT], 'wrong': w[:N_WRONG]}
    want = {r['sid'] for r in chunk}
    return by if want <= set(by) else None


def run_writers(sel, stub=False):
    os.makedirs(os.path.join(SET, 'writers'), exist_ok=True)
    chunks = writer_chunks(sel)
    if stub:
        for k, ch in enumerate(chunks, 1):
            if writer_valid(k, ch):
                continue
            out = []
            for r in ch:
                ref = (r['ann'].get('v') or [''])[0]
                out.append({'sid': r['sid'],
                            'correct': [{'answer': ref, 'tag': 'plain'},
                                        {'answer': ref.replace('  ', ' '), 'tag': 'plain'},
                                        {'answer': ref + '', 'tag': 'plain'}],
                            'wrong': [{'answer': ref.replace(' the ', ' ') or ref + ' x',
                                       'tag': 'missing-article', 'type': 'M'},
                                      {'answer': 'Yesterday ' + ref, 'tag': 'time-frame',
                                       'type': 'T'},
                                      {'answer': 'It ' + ref, 'tag': 'drop-main', 'type': 'S'}]})
            jdump(out, writer_path(k))
        return all(writer_valid(k, ch) for k, ch in enumerate(chunks, 1))
    for attempt in (1, 2):
        todo = [(k, ch) for k, ch in enumerate(chunks, 1) if not writer_valid(k, ch)]
        if not todo:
            return True
        if attempt == 2:
            R['notes'].append('writer retry for parts %s after a missing or unparsable file'
                              % [k for k, _ in todo])
        procs = []
        for k, ch in todo:
            body = '\n'.join(
                '- sid %d | level %s | topic: %s\n  Slovak: %s' % (r['sid'], r['level'],
                                                                  r['topic'], r['slovak'])
                for r in ch)
            prompt = WRITER_BRIEF % (N_CORRECT, N_WRONG, ACCEPT_RULES,
                                     ', '.join(TAGS_OK), 'writers/writer_part%d.json' % k,
                                     len(ch), body)
            procs.append(spawn('writer_part%d_try%d' % (k, attempt), prompt))
        if not any(procs):
            return False
        wait_all(procs, 5400)
    return all(writer_valid(k, ch) for k, ch in enumerate(chunks, 1))


def build_items(sel, data_dir):
    """items.json from the writer output.  Item ids C:<sid>:cN / W:<sid>:wN."""
    chunks = writer_chunks(sel)
    by = {}
    for k, ch in enumerate(chunks, 1):
        v = writer_valid(k, ch)
        if not v:
            return None
        by.update(v)
    items = []
    for r in sel['rows']:
        got = by.get(r['sid'])
        if not got:
            return None
        for n, x in enumerate(got['correct'], 1):
            tag = x.get('tag') if x.get('tag') in TAGS_OK else 'plain'
            items.append({'id': 'C:%d:c%d' % (r['sid'], n), 'sid': r['sid'], 'kind': 'C',
                          'intent': 'C', 'form': None, 'tags': [tag], 'passive': None,
                          'answer': str(x['answer']).strip(),
                          'writer_intent': 'correct (%s)' % tag})
        for n, x in enumerate(got['wrong'], 1):
            tag = x.get('tag') if x.get('tag') in TAGS_OK else 'plain'
            ty = x.get('type') if x.get('type') in TYPES else 'W'
            items.append({'id': 'W:%d:w%d' % (r['sid'], n), 'sid': r['sid'], 'kind': 'W',
                          'intent': 'W', 'form': ty, 'tags': [tag], 'passive': None,
                          'answer': str(x['answer']).strip(),
                          'writer_intent': 'wrong, writer type %s (%s)' % (ty, tag)})
    jdump(items, os.path.join(data_dir, 'items.json'))
    say('items: %d (%d correct, %d wrong)' % (len(items),
                                              sum(1 for i in items if i['kind'] == 'C'),
                                              sum(1 for i in items if i['kind'] == 'W')))
    return items


# ====================================================================== judge
def build_packets(sel, items):
    """Shuffled packets with hidden duplicate controls; the key file the judge never sees."""
    p = os.path.join(SET, 'judge', 'packets.json')
    old = jload(p)
    if old:
        return old
    topic = {r['sid']: r['topic'] for r in sel['rows']}
    sk = {r['sid']: r['slovak'] for r in sel['rows']}
    lv = {r['sid']: r['level'] for r in sel['rows']}
    rng = random.Random(SEED + 1)
    n_dup = int(round(len(items) * DUP_FRACTION))
    dups = rng.sample([i['id'] for i in items], n_dup)
    seq = [i['id'] for i in items] + list(dups)
    rng.shuffle(seq)
    key, packets = {}, [[] for _ in range(JUDGE_PACKETS)]
    per = (len(seq) + JUDGE_PACKETS - 1) // JUDGE_PACKETS
    ans = {i['id']: i['answer'] for i in items}
    sid_of = {i['id']: i['sid'] for i in items}
    for n, iid in enumerate(seq):
        jid = 'q%04d' % (n + 1)
        part = min(n // per, JUDGE_PACKETS - 1)
        key[jid] = {'item_id': iid, 'packet_part': part + 1, 'packet_position': len(packets[part]) + 1,
                    'is_duplicate_copy': False}
        s = sid_of[iid]
        packets[part].append({'jid': jid, 'slovak': sk[s], 'level': lv[s], 'topic': topic[s],
                              'answer': ans[iid]})
    seen = set()
    for jid in sorted(key):
        iid = key[jid]['item_id']
        if iid in seen:
            key[jid]['is_duplicate_copy'] = True
        seen.add(iid)
    rep = {'items': len(items), 'duplicate_controls': n_dup, 'total_qids': len(seq),
           'parts': JUDGE_PACKETS, 'seed': SEED + 1,
           'packet_fields': ['jid', 'slovak', 'level', 'answer', 'topic'],
           'sizes': {str(k + 1): len(packets[k]) for k in range(JUDGE_PACKETS)},
           'packets': {str(k + 1): packets[k] for k in range(JUDGE_PACKETS)}, 'key': key}
    jdump(rep, p)
    say('packets: %d qids in %d parts, %d duplicate controls' % (len(seq), JUDGE_PACKETS, n_dup))
    return rep


def verdict_path(k):
    return os.path.join(SET, 'judge', 'verdicts_part%d.json' % k)


def verdict_valid(k, pk):
    o = parse_json_file(verdict_path(k))
    if isinstance(o, dict):
        o = o.get('verdicts') or list(o.values())
    if not isinstance(o, list):
        return None
    want = {x['jid'] for x in pk['packets'][str(k)]}
    got = {}
    for r in o:
        if isinstance(r, dict) and r.get('jid') in want and r.get('judged') in ('correct', 'wrong'):
            got[r['jid']] = r
    return got if want <= set(got) else None


def run_judge(pk, stub=False):
    os.makedirs(os.path.join(SET, 'judge'), exist_ok=True)
    if stub:
        for k in range(1, JUDGE_PACKETS + 1):
            if verdict_valid(k, pk):
                continue
            out = []
            for it in pk['packets'][str(k)]:
                iid = pk['key'][it['jid']]['item_id']
                wrong = iid.startswith('W:')
                out.append({'jid': it['jid'], 'judged': 'wrong' if wrong else 'correct',
                            'type': 'M' if wrong else None, 'borderline': False, 'confidence': 4})
            jdump(out, verdict_path(k))
        return all(verdict_valid(k, pk) for k in range(1, JUDGE_PACKETS + 1))
    for attempt in (1, 2, 3):
        todo = [k for k in range(1, JUDGE_PACKETS + 1) if not verdict_valid(k, pk)]
        if not todo:
            return True
        if attempt > 1:
            R['notes'].append('judge continuation session %d for parts %s' % (attempt, todo))
        procs = []
        for k in todo:
            pkt = pk['packets'][str(k)]
            body = '\n'.join(json.dumps(x, ensure_ascii=False) for x in pkt)
            prompt = JUDGE_BRIEF % (ACCEPT_RULES, 'judge/verdicts_part%d.json' % k, len(pkt), body)
            procs.append(spawn('judge_part%d_try%d' % (k, attempt), prompt))
        if not any(procs):
            return False
        wait_all(procs, 7200)
    return all(verdict_valid(k, pk) for k in range(1, JUDGE_PACKETS + 1))


def join_labels(pk, data_dir):
    """labels.json keyed by item id, plus the judge-noise rate from the duplicate controls."""
    rows = {}
    for k in range(1, JUDGE_PACKETS + 1):
        got = verdict_valid(k, pk)
        if not got:
            return None, None
        for jid, r in got.items():
            rows[jid] = r
    per_item = collections.defaultdict(list)
    for jid, r in sorted(rows.items()):
        meta = pk['key'][jid]
        conf = r.get('confidence')
        conf = conf if isinstance(conf, int) and 1 <= conf <= 5 else 3
        ty = r.get('type') if r.get('type') in TYPES else None
        if r['judged'] == 'wrong' and ty is None:
            ty = 'W'
        per_item[meta['item_id']].append(
            {'jid': jid, 'judged': r['judged'], 'type': ty,
             'borderline': bool(r.get('borderline')), 'confidence': conf,
             'packet_part': meta['packet_part'], 'packet_position': meta['packet_position']})
    labels, dis, dis_type, n_pairs = {}, 0, 0, 0
    for iid, lst in per_item.items():
        first = lst[0]
        labels[iid] = {'judged': first['judged'], 'type': first['type'],
                       'borderline': first['borderline'], 'confidence': first['confidence'],
                       'packet_part': first['packet_part'],
                       'packet_position': first['packet_position'], 'passive': None,
                       'tip': None, 'dropped': False, 'qid': first['jid']}
        if len(lst) > 1:
            n_pairs += 1
            if len({x['judged'] for x in lst}) > 1:
                dis += 1
            elif len({x['type'] for x in lst}) > 1:
                dis_type += 1
    jdump(labels, os.path.join(data_dir, 'labels.json'))
    noise = {'duplicate_controls_judged': n_pairs, 'label_disagreements': dis,
             'type_only_disagreements': dis_type,
             'judge_noise_pct': round(100.0 * dis / n_pairs, 2) if n_pairs else None,
             'judge_noise_cp': cp(dis, n_pairs) if n_pairs else None,
             'items_labelled': len(labels),
             'judged': dict(collections.Counter(v['judged'] for v in labels.values())),
             'types': dict(collections.Counter(v['type'] for v in labels.values()
                                               if v['judged'] == 'wrong')),
             'borderline': sum(1 for v in labels.values() if v['borderline'])}
    jdump(noise, os.path.join(SET, 'judge', 'join_labels.json'))
    say('labels: %s ; judge noise %s' % (noise['judged'], noise['judge_noise_pct']))
    return labels, noise


# ====================================================================== the copied stack
PATCH_RUNNER = r'''

# ======================================================================================
# Phase 2F PART 3.1 PROBE - the ONLY functional changes to the copied 1U runner:
#   1. the stack = phase1w/stack_1w.py (1V round 2 + reader_nom): AG v4 full + v5 rs_nom + TIP
#      determiner rule.  AG primary = stack_1w.decide (rs_nom rejects land before L3, 0 calls);
#      after the rows are built, stack_1w.final_accept(row) is applied to every row, 0 calls.
#      This is EXACTLY the 1W §4 patch.
#   2. the ledger, the mirror state and the floors file are repointed into the probe directory,
#      because phase1u is read-only INPUT and nothing outside phase2f/p3/probe may be written.
#   3. CAP_1U = the probe's own 250-call cap.  FINAL_ITEMS_EXPECTED = 360.
# The METHOD, the prompt (P-FROZEN-1U), the model, the levers and the layers are unchanged.
# ======================================================================================
_P1W = os.path.join(TOFF, 'phase1w')
if _P1W not in sys.path:
    sys.path.insert(0, _P1W)
import stack_1w as SW1W                                                        # noqa: E402

PROBE_DIR = os.path.dirname(HERE)
LEDGER_DEV = os.path.join(PROBE_DIR, 'ledger_p31.jsonl')
MIRROR_STATE = os.path.join(HERE, 'ledger_mirror_state.json')
FLOORS_JSON = os.path.join(PROBE_DIR, 'set', 'floors_p31.json')
FLOORS_ALT = FLOORS_JSON
CAP_1U = int(os.environ.get('P31_CAP') or 250)
FINAL_ITEMS_EXPECTED = 360

_counted_dev_1u = counted_dev
_mirror_to_dev_1u = mirror_to_dev


def counted_dev(path=None):
    return _counted_dev_1u(path or LEDGER_DEV)


def mirror_to_dev(agent, calls_path=None, dev=None, state=None):
    return _mirror_to_dev_1u(agent, calls_path, dev or LEDGER_DEV, state or MIRROR_STATE)


class _AGP31(object):
    @staticmethod
    def decide(sk, ann, wtags, answer, reference, variant='primary', flags=None):
        return SW1W.decide(sk, ann, wtags, answer, reference, 'primary',
                           tuple(AG4.ALL_FLAGS), ('rs_nom',))


AG_CFG['primary'] = (_AGP31, tuple(AG4.ALL_FLAGS))
_build_rows_1u = build_rows


def build_rows(recs, res, ag, planned, labels, hmap, failed):
    rows, _agg = _build_rows_1u(recs, res, ag, planned, labels, hmap, failed)
    agg = collections.Counter()
    for r in rows.values():
        r['stack_in'] = {'final_accept': r['final_accept'], 'final_layer': r['final_layer']}
        acc, lay = SW1W.final_accept(r, ('rs_nom',), True)
        r['final_accept'], r['final_layer'] = acc, lay
        agg['%s/%s' % ('accept' if acc else 'reject', r.get('judged') or 'unlabelled')] += 1
    return rows, dict(agg)

'''


STUB_FINAL = r'''#!/usr/bin/env python3
"""Phase 2F PART 3.1 - 0-call stub of the final run, for the preflight selftest ONLY.
Same code path as --final (final_core), with a stub L3 in place of the transport and checks off:
it proves the set, the loader, the layers, the stack patch, the rows and the scorer all work
before a single model call is made.  Never used by --run."""
import json, os, random, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import runner_1u as RU                                                         # noqa: E402

DATA = sys.argv[sys.argv.index('--data-dir') + 1]


def stub(req, need):
    rng = random.Random(4242)
    with open(RU.CALLS, 'a', encoding='utf-8') as fh:
        for h in need:
            v = rng.choice(['SAME', 'SAME', 'SAME', 'DIFF', 'TIP'])
            fh.write(json.dumps({'ts': 'stub', 'http': 200, 'req_hash': h, 'verdict': v,
                                 'item_id': None, 'reply': v, 'prompt_tokens': 11,
                                 'candidates_tokens': 2, 'latency_ms': 1}) + chr(10))
    return {'ok': len(need), 'bad': 0, 'empty': 0, 'skipped': 0, 'wall': False}


fl = RU.check_floors_1u()
print('[STUB] floors gate exercised:', json.dumps(fl, sort_keys=True))
out = RU.final_core(HERE, DATA, call_fn=stub, checks=False)
print('[STUB] status', out.get('status'), 'headline', json.dumps(out.get('headline')))
'''


def insert_before_main(src, patch):
    i = src.rindex("\nif __name__ == '__main__':")
    return src[:i] + patch + src[i:]


def setup_run(run_dir):
    if os.path.exists(os.path.join(run_dir, 'runner_1u.py')):
        return
    os.makedirs(run_dir, exist_ok=True)
    for f in ('loader_1u.py', 'article_line_1u.py', 'selftest_1u_run.py', 'score_1u.py',
              'runner_1u.py', 'FROZEN_CONFIG_1U.json'):
        dst = os.path.join(run_dir, f)
        shutil.copy2(os.path.join(U, f), dst)
        os.chmod(dst, 0o644)      # phase1u is read-only INPUT; the copies must be writable
    # The copy lives one level deeper than phase1u/run, so the modules' own
    # TOFF = dirname(dirname(HERE)) would point at the wrong tree.  Pin TOFF to the real
    # translation-offline root; HERE (the run dir, where every output lands) is untouched.
    pin = ("TOFF = %r   # probe: pinned to the real translation-offline root\n"
           "P1U = os.path.join(TOFF, 'phase1u')" % TOFF)
    for f in ('runner_1u.py', 'score_1u.py'):
        t = open(os.path.join(run_dir, f), encoding='utf-8').read()
        for a, b in (("P1U = os.path.dirname(HERE)                                  # phase1u\n"
                      "TOFF = os.path.dirname(P1U)                                  # "
                      "translation-offline", pin),
                     ("P1U = os.path.dirname(HERE)\nTOFF = os.path.dirname(P1U)", pin)):
            if a in t:
                t = t.replace(a, b, 1)
                break
        else:
            raise SystemExit('REFUSED: could not pin TOFF in %s' % f)
        open(os.path.join(run_dir, f), 'w', encoding='utf-8').write(t)
    # article_line_1u re-reads the frozen L3 prompt text and REFUSES unless it is byte-identical;
    # keep that check alive by pointing it at the real phase1u/stack.
    t = open(os.path.join(run_dir, 'article_line_1u.py'), encoding='utf-8').read()
    a2 = 'P1U = os.path.dirname(HERE)'
    assert a2 in t
    open(os.path.join(run_dir, 'article_line_1u.py'), 'w', encoding='utf-8').write(
        t.replace(a2, "P1U = os.path.join(%r, 'phase1u')   # probe: the frozen stack's home"
                  % TOFF, 1))
    # the loader guards the sid range; point it at the probe's own fresh sids
    t = open(os.path.join(run_dir, 'loader_1u.py'), encoding='utf-8').read()
    a = 'SID_LO, SID_HI = 190001, 190100'
    assert a in t
    open(os.path.join(run_dir, 'loader_1u.py'), 'w', encoding='utf-8').write(
        t.replace(a, 'SID_LO, SID_HI = %d, %d   # probe: fresh sids' % (SID_LO, SID_HI), 1))
    src = open(os.path.join(run_dir, 'runner_1u.py'), encoding='utf-8').read()
    a = "TASKA = os.path.join(P1U, 'taskA')"
    assert a in src
    src = src.replace(a, "TASKA = os.path.join(TOFF, 'phase1u', 'taskA')   # probe: AG v4 home", 1)
    open(os.path.join(run_dir, 'runner_1u.py'), 'w', encoding='utf-8').write(
        insert_before_main(src, PATCH_RUNNER))
    open(os.path.join(run_dir, 'stub_final.py'), 'w', encoding='utf-8').write(STUB_FINAL)
    say('setup: 1U runner/loader/scorer copied to %s (runner patched: stack_1w, ledger + floors '
        'repointed, cap 250)' % run_dir)


def write_floors(items, labels, path):
    """The probe set is PRODUCTION material, not constructed: the 1U floors cannot be engineered
    into it.  The gate is kept (the runner still refuses on a missing/malformed key) but every
    minimum is 0 and the REAL counts are reported.  Recorded as a deviation, never tuned away."""
    tag_of = {i['id']: (i['tags'] or ['plain'])[0] for i in items}
    kind_of = {i['id']: i['kind'] for i in items}
    lab = labels or {}

    def n_of(pred):
        return sum(1 for iid in tag_of if pred(iid))

    drops = ('drop-main', 'drop-fronted', 'drop-misaligned', 'drop-other')
    rep = {
        'F1_agent_drops_wrong': n_of(lambda i: tag_of[i] in drops
                                     and (lab.get(i) or {}).get('judged') == 'wrong'),
        'F1a_fronted_wrong': n_of(lambda i: tag_of[i] == 'drop-fronted'
                                  and (lab.get(i) or {}).get('judged') == 'wrong'),
        'F1b_misaligned_wrong': n_of(lambda i: tag_of[i] == 'drop-misaligned'
                                     and (lab.get(i) or {}).get('judged') == 'wrong'),
        'F2_time_frame_wrong': n_of(lambda i: tag_of[i] == 'time-frame'
                                    and (lab.get(i) or {}).get('judged') == 'wrong'),
        'F3_by_passive_correct': n_of(lambda i: tag_of[i].startswith('by-passive')
                                      and (lab.get(i) or {}).get('judged') == 'correct'),
        'F4_skp_correct': n_of(lambda i: tag_of[i] == 'skp-passive'
                               and (lab.get(i) or {}).get('judged') == 'correct'),
        'F5_missing_article_wrong': n_of(lambda i: tag_of[i] == 'missing-article'
                                         and (lab.get(i) or {}).get('judged') == 'wrong'),
    }
    out = {k: {'n': v, 'min': 0, 'pass': True} for k, v in rep.items()}
    out['all_pass'] = True
    out['NOTE'] = ('PROBE: the set is production material, so the 1U construction floors cannot '
                   'hold by construction. Every minimum is 0; the n values are the real counts '
                   'and are reported as cells. This is a recorded DEVIATION, not a tuned gate.')
    out['items_total'] = len(tag_of)
    out['by_kind'] = dict(collections.Counter(kind_of.values()))
    out['by_tag'] = dict(collections.Counter(tag_of.values()))
    jdump(out, path)
    return out


# ====================================================================== gate
def wait_for_part2():
    t0 = time.time()
    n = 0
    while not os.path.exists(PART2_RESULT):
        if time.time() - t0 > WAIT_MAX_S:
            return False
        if n % 15 == 0:
            say('waiting for PART2_RESULT.md ... %d min' % int((time.time() - t0) / 60))
        n += 1
        time.sleep(WAIT_POLL_S)
    say('PART2_RESULT.md present after %d min' % int((time.time() - t0) / 60))
    return True


def budget_ok():
    b = jload(BUDGET, {}) or {}
    p2 = b.get('part2_counted')
    if not isinstance(p2, (int, float)):
        p2 = 0
        R['notes'].append('GEMINI_BUDGET.json carried no numeric part2_counted; read as 0')
    R['budget_before'] = dict(b)
    R['part2_counted'] = p2
    if p2 + CAP_PART31 > CAP_PHASE:
        return False, ('part2_counted %s + %d planned = %s would exceed the phase-wide cap %d'
                       % (p2, CAP_PART31, p2 + CAP_PART31, CAP_PHASE))
    allowed = int(min(CAP_PART31_MAX, CAP_PHASE - p2))
    R['allowed_calls'] = allowed
    os.environ['P31_CAP'] = str(allowed)
    return True, ('part2_counted %s + %d = %s, within the %d phase cap; this probe may spend at '
                  'most %d counted calls (declared budget %d, local ceiling %d)'
                  % (p2, CAP_PART31, p2 + CAP_PART31, CAP_PHASE, allowed, CAP_PART31,
                     CAP_PART31_MAX))


def budget_write(counted):
    b = jload(BUDGET, {}) or {}
    b['part31_counted'] = counted
    b['part31_cap'] = CAP_PART31
    b['phase_cap'] = CAP_PHASE
    b['part31_updated'] = datetime.datetime.now().isoformat(timespec='seconds')
    jdump(b, BUDGET)
    R['budget_after'] = dict(b)


# ====================================================================== calls accounting
def calls_stats(run_dir):
    p = os.path.join(run_dir, 'calls.jsonl')
    rows = []
    if os.path.exists(p):
        for line in open(p, encoding='utf-8'):
            try:
                rows.append(json.loads(line))
            except Exception:
                pass
    ok = [r for r in rows if r.get('http') == 200]
    failed = [r for r in ok if r.get('empty')
              or str(r.get('verdict') or '').upper() not in ('SAME', 'TIP', 'DIFF')]
    tin = sum((r.get('prompt_tokens') or r.get('tokens_in') or 0) for r in ok)
    tout = sum((r.get('candidates_tokens') or r.get('tokens_out') or 0) for r in ok)
    return {'lines': len(rows), 'counted_http200': len(ok),
            'uncounted_retries': sum(1 for r in rows if r.get('http') != 200),
            'uncounted_by_http': dict(collections.Counter(str(r.get('http')) for r in rows
                                                          if r.get('http') != 200)),
            'failed_empty_or_unparsable_200': len(failed),
            'tokens_in': tin, 'tokens_out': tout,
            'spend_usd_list_price': round(tin * 0.10e-6 + tout * 0.40e-6, 5),
            'failure_rate_pct': round(100.0 * len(failed) / len(ok), 2) if ok else None}


def headless_tokens():
    tin = sum((s.get('input_tokens') or 0) for s in R['sessions'])
    tcc = sum((s.get('cache_creation_input_tokens') or 0) for s in R['sessions'])
    tcr = sum((s.get('cache_read_input_tokens') or 0) for s in R['sessions'])
    tout = sum((s.get('output_tokens') or 0) for s in R['sessions'])
    cost = sum((s.get('total_cost_usd') or 0) for s in R['sessions'])
    return {'sessions': len(R['sessions']), 'input_tokens': tin,
            'cache_creation_input_tokens': tcc, 'cache_read_input_tokens': tcr,
            'output_tokens': tout, 'total_incl_cache': tin + tcc + tcr + tout,
            'reported_cost_usd': round(cost, 4)}


# ====================================================================== cells
def cells_from_rows(results, items, labels):
    rows = (results or {}).get('rows') or []
    tag_of = {i['id']: (i['tags'] or ['plain'])[0] for i in items}
    drops = ('drop-main', 'drop-fronted', 'drop-misaligned', 'drop-other')
    out = collections.OrderedDict()

    def cell(name, pred, want):
        sel = [r for r in rows if r.get('judged') == want and pred(r)]
        k = sum(1 for r in sel if r.get('final_accept'))
        out[name] = cp(k, len(sel))

    cell('agent drops (writer drop-*) - FA among judged wrong',
         lambda r: tag_of.get(r['item_id']) in drops, 'wrong')
    cell('by-passive (writer by-passive*) - coverage among judged correct',
         lambda r: str(tag_of.get(r['item_id'])).startswith('by-passive'), 'correct')
    cell('by-passive (writer by-passive*) - FA among judged wrong',
         lambda r: str(tag_of.get(r['item_id'])).startswith('by-passive'), 'wrong')
    cell('time-frame (writer time-frame) - FA among judged wrong',
         lambda r: tag_of.get(r['item_id']) == 'time-frame', 'wrong')
    cell('missing-article (writer missing-article) - FA among judged wrong',
         lambda r: tag_of.get(r['item_id']) == 'missing-article', 'wrong')
    for ty in TYPES:
        cell('judge type %s - FA among judged wrong' % ty,
             lambda r, t=ty: r.get('judged_type') == t, 'wrong')
    for L in LEVELS:
        cell('level %s - coverage' % L, lambda r, x=L: r.get('level') == x, 'correct')
        cell('level %s - FA' % L, lambda r, x=L: r.get('level') == x, 'wrong')
    # FA by layer, and the L3 verdict split
    fa_rows = [r for r in rows if r.get('judged') == 'wrong' and r.get('final_accept')]
    out['_fa_by_layer'] = dict(collections.Counter(str(r.get('final_layer')) for r in fa_rows))
    out['_accept_layer_all'] = dict(collections.Counter(
        '%s/%s' % (r.get('final_layer'), 'accept' if r.get('final_accept') else 'reject')
        for r in rows))
    l3 = [r for r in rows if (r.get('layers') or {}).get('reached_l3')]
    out['_l3_verdicts'] = dict(collections.Counter(
        str((r.get('layers') or {}).get('model')) for r in l3))
    out['_l3_verdicts_by_label'] = dict(collections.Counter(
        '%s/%s' % (str((r.get('layers') or {}).get('model')), r.get('judged')) for r in l3))
    out['_ag_rejected_before_l3'] = sum(1 for r in rows if (r.get('ag') or {}).get('fired'))
    out['_ag_fired_by_label'] = dict(collections.Counter(
        r.get('judged') for r in rows if (r.get('ag') or {}).get('fired')))
    return out


# ====================================================================== report
def write_report(results, score, cells, noise, sel, calls, run_dir, stopped=None):
    cov = fa = None
    if results:
        h = results.get('headline') or {}
        cov = cp(*(h.get('coverage_kn') or [0, 0]))
        fa = cp(*(h.get('fa_kn') or [0, 0]))
    R['coverage'] = cov
    R['fa'] = fa
    L = []
    L.append('# PROBE - Slovak PRODUCTION sentences, Phase 2F PART 3.1')
    L.append('')
    L.append('**THIS IS A PROBE, NOT A MEASUREMENT THAT SETTLES ANYTHING.** At n is about 180 '
             'judged-correct items the exact 95 % interval is roughly +/- 5 points. That is '
             'enough to show whether production sentences sit in the SAME REGION as the test '
             'sets, and not enough to settle it. No target is settled here on either side.')
    L.append('')
    L.append('- Status: %s' % (stopped or R.get('status') or 'completed'))
    L.append('- Run started: %s; report written: %s'
             % (R.get('started'), datetime.datetime.now().isoformat(timespec='seconds')))
    L.append('- Set: 60 Slovak sentences read READ-ONLY from '
             '`phase2d/out/annotations_sk_final.jsonl` (the real uploaded production material, '
             '%d usable rows), seed %d, sids %d-%d (fresh: 1W used 200001-200100, Part 2 uses '
             '210001-210100).' % ((sel or {}).get('source_rows_total', 0), SEED, SID_LO, SID_HI))
    L.append('- Stratification: %s (pool by level: %s)'
             % (json.dumps((sel or {}).get('stratification', {})),
                json.dumps((sel or {}).get('pool_by_level', {}))))
    L.append('- `topic` in the judge packet = the production row\'s `type_title` (the exercise '
             'type). The production rows carry NO `topic` field; this is stated so the 1N defect '
             '(topic dropped from the packet) cannot recur silently.')
    L.append('- Stack, unchanged: `phase1w/stack_1w.py` (AG v4 full + v5 `rs_nom` + TIP determiner '
             'rule) with `reader_nom`; L3 = gemini-3.1-flash-lite, temperature 0, thinkingBudget '
             '0, prompt P-FROZEN-1U. The 1U runner/loader/scorer were COPIED into '
             '`phase2f/p3/probe/run/`; only the SET changed. Nothing was tuned.')
    for n in R['notes']:
        L.append('- Note: %s' % n)
    L.append('')
    L.append('## Headline')
    L.append('')
    if cov and cov.get('n'):
        L.append('| | this probe (production) | 1W blind test (Slovak) |')
        L.append('|---|---|---|')
        L.append('| coverage | %s | %d/%d = %.2f %% [%.2f, %.2f] |' % ((fk(cov),) + W1_COV))
        L.append('| false accepts | %s | %d/%d = %.2f %% [%.2f, %.2f] |' % ((fk(fa),) + W1_FA))
        L.append('')
        ov_c = not (cov['ci'][1] < W1_COV[3] or cov['ci'][0] > W1_COV[4])
        ov_f = not (fa['ci'][1] < W1_FA[3] or fa['ci'][0] > W1_FA[4])
        L.append('- Coverage intervals %s. Points differ by %.2f points (probe %.2f %% vs 1W '
                 '%.2f %%).' % ('OVERLAP' if ov_c else 'DO NOT overlap',
                                cov['pct'] - W1_COV[2], cov['pct'], W1_COV[2]))
        L.append('- FA intervals %s. Points differ by %.2f points (probe %.2f %% vs 1W %.2f %%).'
                 % ('OVERLAP' if ov_f else 'DO NOT overlap', fa['pct'] - W1_FA[2], fa['pct'],
                    W1_FA[2]))
        L.append('- Target coverage >= 90 %%: on the POINT %s; on the INTERVAL (lower bound >= 90) '
                 '%s.' % ('MET' if cov['pct'] >= 90 else 'MISSED',
                          'MET' if cov['ci'][0] >= 90 else 'MISSED'))
        L.append('- Target FA < 5 %%: on the POINT %s; on the INTERVAL (upper bound < 5) %s.'
                 % ('MET' if fa['pct'] < 5 else 'MISSED', 'MET' if fa['ci'][1] < 5 else 'MISSED'))
        L.append('- **Neither target is settled by a probe of this size.** The statement above is '
                 'the arithmetic, not a verdict.')
    else:
        L.append('- NO RESULT: the set was not opened. See Status above.')
    L.append('')
    L.append('## Phase 2B beside it')
    L.append('')
    L.append('- Phase 2B (`phase2b/TRANSLATION_PRODUCTION_PHASE2B_REPORT.md`) measured the AGENT '
             'READER erring on **50 %** of raw production text against **1.67 %** on blind-test '
             'Slovak (1W).')
    L.append('- 2B measured a DIFFERENT quantity from this probe: 2B scored the reader\'s derived '
             'field (agent_nom and the voice path) against a gold annotation. This probe scores '
             'the WHOLE stack\'s accept/reject decision against a blind judge. A reader that errs '
             'often can still be overruled by the later layers, and a reader that is right can '
             'still be followed by a bad L3 call. The two numbers are not the same measurement '
             'and cannot be subtracted.')
    if cov and cov.get('n'):
        L.append('- Consistency: %s' % (
            'this probe is NOT consistent with a collapse of the same size as 2B\'s - the '
            'accept/reject decision on production sits in the same region as the blind test, so '
            'whatever the reader gets wrong is largely absorbed before the final verdict.'
            if (cov['ci'][1] >= W1_COV[3] and cov['ci'][0] > 80)
            else 'this probe IS consistent with production behaving materially worse than the '
                 'test sets - the coverage point falls well below 1W\'s and the intervals are '
                 'far apart.'))
        L.append('- The AG/reader cells below say how often the deterministic agent path fired on '
                 'production at all; that is the cell to read next to 2B, and at this n it is '
                 'thin.')
    L.append('')
    L.append('## Judge')
    L.append('')
    if noise:
        L.append('- Judge noise (hidden duplicate controls, same item judged twice under '
                 'different jids in different packets): **%s of %s pairs disagreed on '
                 'correct/wrong = %s %%**%s.'
                 % (noise.get('label_disagreements'), noise.get('duplicate_controls_judged'),
                    noise.get('judge_noise_pct'),
                    (' [%.2f, %.2f]' % tuple(noise['judge_noise_cp']['ci']))
                    if noise.get('judge_noise_cp') and noise['judge_noise_cp']['ci'][0] is not None
                    else ''))
        L.append('- Type-only disagreements (same correct/wrong, different type): %s'
                 % noise.get('type_only_disagreements'))
        L.append('- Labels: %s ; wrong-types %s ; borderline %s ; items labelled %s'
                 % (json.dumps(noise.get('judged')), json.dumps(noise.get('types')),
                    noise.get('borderline'), noise.get('items_labelled')))
        L.append('- The judge received the acceptance rules VERBATIM and every packet item carried '
                 '`jid / slovak / level / answer / topic`.')
    else:
        L.append('- no judge labels')
    L.append('')
    L.append('## Every cell (exact Clopper-Pearson 95 %); thin cells are left as n = ...')
    L.append('')
    for k, v in (cells or {}).items():
        if k.startswith('_'):
            L.append('- %s: %s' % (k.lstrip('_'), json.dumps(v)))
        elif not v.get('n'):
            L.append('- %s: n = 0 (no item of this kind in the production sample)' % k)
        elif v['n'] < 10:
            L.append('- %s: %d/%d - **n = %d, too thin to read as a rate**'
                     % (k, v['k'], v['n'], v['n']))
        else:
            L.append('- %s: %s' % (k, fk(v)))
    L.append('')
    L.append('## Provenance')
    L.append('')
    L.append('- FREEZE hash: %s' % R.get('freeze_hash'))
    L.append('- RUN commit: %s' % R.get('run_commit'))
    L.append('- FINAL_RUN_DONE: %s' % json.dumps(R.get('final_run_done')))
    L.append('- Runner exit: %s; preflight: %s'
             % (R.get('final_exit'), json.dumps(R.get('preflight'))))
    L.append('- Gemini budget gate: %s' % R.get('budget_msg'))
    for k, v in (calls or {}).items():
        L.append('- calls %s: %s' % (k, json.dumps(v)))
    L.append('- Headless (Claude Opus, bundled binary, --output-format json): %s'
             % json.dumps(headless_tokens()))
    for s in R['sessions']:
        L.append('  - %s: exit %s, is_error %s, turns %s, in %s, cache_creation %s, cache_read %s, '
                 'out %s, cost_usd %s, denials %s'
                 % (s['session'], s['exit'], s['is_error'], s.get('num_turns'),
                    s.get('input_tokens'), s.get('cache_creation_input_tokens'),
                    s.get('cache_read_input_tokens'), s.get('output_tokens'),
                    s.get('total_cost_usd'), s.get('permission_denials')))
    L.append('')
    L.append('## Defects recorded, NOT fixed')
    L.append('')
    if R['defects']:
        for d in R['defects']:
            L.append('- **%s** - %s' % (d['what'], d['detail']))
    else:
        L.append('- none recorded')
    L.append('')
    L.append('## Access log (verbatim)')
    L.append('')
    L.append('```')
    p = os.path.join(run_dir, 'access_log.jsonl')
    if os.path.exists(p):
        L.append(open(p, encoding='utf-8', errors='replace').read().rstrip())
    else:
        L.append('(no access log: the loader was never opened)')
    L.append('```')
    open(os.path.join(PROBE, 'PROBE_SLOVAK_PRODUCTION.md'), 'w', encoding='utf-8').write(
        '\n'.join(L) + '\n')
    jdump({'probe': 'phase2f p3.1 Slovak production', 'status': stopped or R.get('status')
           or 'completed', 'coverage': cov, 'fa': fa,
           'w1_blind_test': {'coverage': {'k': W1_COV[0], 'n': W1_COV[1], 'pct': W1_COV[2],
                                          'ci': [W1_COV[3], W1_COV[4]]},
                             'fa': {'k': W1_FA[0], 'n': W1_FA[1], 'pct': W1_FA[2],
                                    'ci': [W1_FA[3], W1_FA[4]]}},
           'judge_noise': noise, 'cells': cells, 'calls': calls,
           'headless': headless_tokens(), 'freeze_hash': R.get('freeze_hash'),
           'run_commit': R.get('run_commit'), 'final_run_done': R.get('final_run_done'),
           'stratification': (sel or {}).get('stratification'),
           'seed': SEED, 'sids': [SID_LO, SID_HI], 'defects': R['defects'],
           'notes': R['notes'], 'sessions': R['sessions'],
           'budget': {'before': R.get('budget_before'), 'after': R.get('budget_after'),
                      'msg': R.get('budget_msg')}},
          os.path.join(PROBE, 'probe_result.json'))
    say('PROBE_SLOVAK_PRODUCTION.md + probe_result.json written')


# ====================================================================== the pipeline
def pipeline(stub=False):
    set_dir = SET
    data_dir = DATA
    run_dir = RUN
    for d in (PROBE, set_dir, data_dir, SESS):
        os.makedirs(d, exist_ok=True)
    sel = pick_sentences()
    R['stage'] = 'data'
    build_data(sel, data_dir)
    setup_run(run_dir)
    save_state()

    R['stage'] = 'writer'
    if not run_writers(sel, stub=stub):
        R['status'] = 'STOP: the blind writer did not deliver valid files - set NOT opened, 0 ' \
                      'Gemini calls'
        write_report(None, None, None, None, sel, None, run_dir, R['status'])
        return False
    items = build_items(sel, data_dir)
    if not items:
        R['status'] = 'STOP: writer output incomplete after retries - 0 Gemini calls'
        write_report(None, None, None, None, sel, None, run_dir, R['status'])
        return False

    R['stage'] = 'judge'
    pk = build_packets(sel, items)
    if not run_judge(pk, stub=stub):
        R['status'] = 'STOP: the blind judge did not deliver all verdict files - 0 Gemini calls'
        write_report(None, None, None, None, sel, None, run_dir, R['status'])
        return False
    labels, noise = join_labels(pk, data_dir)
    if not labels:
        R['status'] = 'STOP: label join failed - 0 Gemini calls'
        write_report(None, None, None, None, sel, None, run_dir, R['status'])
        return False
    R['judge_noise'] = noise
    write_floors(items, labels, os.path.join(set_dir, 'set_floors_tmp.json'))
    write_floors(items, labels, os.path.join(set_dir, 'floors_p31.json'))
    try:
        os.remove(os.path.join(set_dir, 'set_floors_tmp.json'))
    except Exception:
        pass
    save_state()

    # ---------------------------------------------------------------- freeze + preflight
    R['stage'] = 'freeze'
    runner = os.path.join(run_dir, 'runner_1u.py')
    rc, out = sh(['python3', runner, '--preflight', '--data-dir', data_dir], cwd=run_dir)
    if rc != 0:
        R['status'] = 'STOP: preflight refused (0 Gemini calls): %s' % out.strip()[-600:]
        write_report(None, None, None, noise, sel, None, run_dir, R['status'])
        return False
    mods = open(os.path.join(run_dir, 'MODULES_1U.txt')).read().split()
    rel = os.path.relpath(run_dir, REPO).replace(os.sep, '/')
    with open(os.path.join(run_dir, 'FREEZE_FILES'), 'w') as fh:
        fh.write('# Phase 2F PART 3.1 PROBE FREEZE_FILES - every .py the run imports, relative to '
                 'the repository root.\n')
        for f in sorted(set(mods + ['%s/score_1u.py' % rel, '%s/selftest_1u_run.py' % rel])):
            fh.write(f + '\n')
    if stub:
        R['freeze_hash'] = 'SELFTEST (no commit)'
    else:
        R['freeze_hash'] = commit('Phase 2F PART 3.1: FREEZE - production probe set judged, stack '
                                  'copied unchanged, before the set is opened')
        open(os.path.join(run_dir, 'FREEZE_HASH'), 'w').write(R['freeze_hash'] + '\n')
    save_state()

    rc, out = sh(['python3', runner, '--preflight', '--data-dir', data_dir], cwd=run_dir)
    pf = jload(os.path.join(run_dir, 'PREFLIGHT_1U.json'), {}) or {}
    R['preflight'] = {k: pf.get(k) for k in ('n_items', 'l2_firings', 'l3_eligible',
                                             'ag_rejected_before_l3', 'reach_l3_planned_calls',
                                             'unique_requests', 'PLANNED_CALLS',
                                             'counted_ledger_dev', 'cap')}
    save_state()
    if rc != 0 or not pf:
        R['status'] = 'STOP: preflight (after freeze) refused - 0 Gemini calls'
        write_report(None, None, None, noise, sel, None, run_dir, R['status'])
        return False
    planned = pf.get('PLANNED_CALLS') or 0
    allowed = R.get('allowed_calls') or CAP_PART31
    if planned > CAP_PART31 and planned <= allowed:
        defect('planned calls above the declared ~250 budget',
               '%d planned; spent anyway because the HARD constraint is the phase-wide cap of %d '
               'shared with Part 2 (%s counted there), and the brief forbids narrowing the scope '
               'to fit. Local ceiling %d.'
               % (planned, CAP_PHASE, R.get('part2_counted'), allowed))
    if planned > allowed:
        R['status'] = ('STOP: %d planned calls exceed the probe cap %d; NOTHING was trimmed and '
                       'the scope was not narrowed - 0 Gemini calls' % (planned, allowed))
        defect('planned calls over the probe cap', '%d planned, allowed %d' % (planned, allowed))
        write_report(None, None, None, noise, sel, None, run_dir, R['status'])
        return False
    if not stub:
        R['run_commit'] = commit('Phase 2F PART 3.1: RUN commit (FREEZE_FILES, preflight, '
                                 'floors) - the production set is opened ONCE after this')
        open(os.path.join(run_dir, 'RUN_COMMIT'), 'w').write(R['run_commit'] + '\n')
    save_state()

    # ---------------------------------------------------------------- the run, ONCE
    R['stage'] = 'final'
    R['final_started'] = datetime.datetime.now().isoformat(timespec='seconds')
    save_state()
    args = (['python3', os.path.join(run_dir, 'stub_final.py'), '--data-dir', data_dir] if stub
            else ['python3', runner, '--final', '--data-dir', data_dir])
    rc, out = sh(args, cwd=run_dir)
    R['final_exit'] = rc
    R['final_tail'] = out.strip().splitlines()[-8:]
    res = jload(os.path.join(run_dir, 'results_1u.json'))
    if not res and os.path.exists(os.path.join(run_dir, 'calls.jsonl')) and rc != 3:
        R['notes'].append('the run did not finish (exit %d); rows recomputed from the stored '
                          'verdicts with score_1u.py --recover, 0 calls' % rc)
        sh(['python3', os.path.join(run_dir, 'score_1u.py'), '--recover', '--data-dir', data_dir],
           cwd=run_dir)
        res = jload(os.path.join(run_dir, 'results_1u.json'))
    if rc == 3:
        R['notes'].append('the run PAUSED on the quota wall; not resumed by the driver')
        defect('quota wall', 'the runner paused; the probe is reported on what was counted')
    R['final_run_done'] = jload(os.path.join(run_dir, 'FINAL_RUN_DONE'))
    calls = calls_stats(run_dir)
    R['gemini_counted'] = calls['counted_http200']
    if not stub:
        budget_write(calls['counted_http200'])
    if calls['failed_empty_or_unparsable_200']:
        defect('failed calls (empty or unparsable HTTP 200)',
               '%d of %d counted calls; counted, never guessed, never silently retried'
               % (calls['failed_empty_or_unparsable_200'], calls['counted_http200']))
    save_state()
    if not res:
        R['status'] = 'STOP: the run produced no results file (exit %s)' % rc
        write_report(None, None, None, noise, sel, calls, run_dir, R['status'])
        return False
    sh(['python3', os.path.join(run_dir, 'score_1u.py'), '--data-dir', data_dir], cwd=run_dir)
    score = jload(os.path.join(run_dir, 'score_1u.json'))
    cells = cells_from_rows(res, items, labels)
    R['status'] = 'completed'
    write_report(res, score, cells, noise, sel, calls, run_dir)
    return True



def _post_defects():
    pass


def rescore():
    """Rebuild the report from the stored artefacts.  0 model calls, nothing re-run, nothing
    tuned: only the reporting layer (the Clopper-Pearson helper) changed."""
    sel = jload(os.path.join(SET, 'selection.json'))
    items = jload(os.path.join(DATA, 'items.json'))
    labels = jload(os.path.join(DATA, 'labels.json'))
    noise = jload(os.path.join(SET, 'judge', 'join_labels.json'))
    if noise is not None:
        n_p = noise.get('duplicate_controls_judged') or 0
        noise['judge_noise_cp'] = cp(noise.get('label_disagreements') or 0, n_p) if n_p else None
        pk = jload(os.path.join(SET, 'judge', 'packets.json')) or {}
        by = collections.defaultdict(list)
        for jid, m in (pk.get('key') or {}).items():
            by[m['item_id']].append(m['packet_part'])
        pr = [v for v in by.values() if len(v) > 1]
        noise['duplicate_controls_cross_packet'] = sum(1 for v in pr if len(set(v)) > 1)
        noise['duplicate_controls_same_packet'] = sum(1 for v in pr if len(set(v)) == 1)
        jdump(noise, os.path.join(SET, 'judge', 'join_labels.json'))
    res = jload(os.path.join(RUN, 'results_1u.json'))
    calls = calls_stats(RUN)
    st = jload(STATE) or {}
    for k in ('freeze_hash', 'run_commit', 'final_run_done', 'final_exit', 'preflight',
              'budget_msg', 'budget_before', 'budget_after', 'sessions', 'notes', 'defects',
              'part2_counted', 'allowed_calls', 'started'):
        if k in st:
            R[k] = st[k]
    R['status'] = 'completed'
    cells = cells_from_rows(res, items, labels)
    write_report(res, jload(os.path.join(RUN, 'score_1u.json')), cells, noise, sel, calls, RUN)
    return True

def main():
    global SET, DATA, RUN, SESS, STATE, LOG
    ap = argparse.ArgumentParser()
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--run', action='store_true')
    ap.add_argument('--rescore', action='store_true')
    a = ap.parse_args()
    old = jload(STATE)
    if old and a.run:
        R.update(old)
        R['status'] = None
    if a.rescore:
        rescore()
        return 0
    if a.selftest:
        # a throwaway copy of the whole probe layout; touches nothing the real run uses
        base = os.path.join(PROBE, '_selftest')
        shutil.rmtree(base, ignore_errors=True)
        os.makedirs(base, exist_ok=True)
        SET, DATA, RUN, SESS = (os.path.join(base, x) for x in ('set', 'data', 'run', 'sessions'))
        STATE = os.path.join(base, 'state.json')
        LOG = os.path.join(base, 'selftest.log')
        ok = False
        try:
            ok = pipeline(stub=True)
        except Exception:
            import traceback
            say(traceback.format_exc())
        res = jload(os.path.join(RUN, 'results_1u.json')) or {}
        h = res.get('headline') or {}
        print('SELFTEST %s  headline=%s  status=%s'
              % ('PASS' if ok and h.get('coverage_kn') else 'FAIL', json.dumps(h), R.get('status')))
        jdump({'pass': bool(ok and h.get('coverage_kn')), 'headline': h, 'status': R.get('status'),
               'preflight': R.get('preflight'), 'notes': R['notes']},
              os.path.join(PROBE, 'SELFTEST_P31.json'))
        return 0 if (ok and h.get('coverage_kn')) else 1
    if not a.run:
        print('nothing to do; pass --selftest or --run')
        return 2
    # ---- the gate: wait for Part 2, then the phase-wide budget
    R['stage'] = 'gate'
    save_state()
    if not wait_for_part2():
        R['status'] = ('STOP: PART2_RESULT.md did not appear within %d h; the probe never opened '
                       'the set. 0 Gemini calls.' % (WAIT_MAX_S // 3600))
        R['budget_msg'] = 'not reached'
        write_report(None, None, None, None, jload(os.path.join(SET, 'selection.json')), None,
                     RUN, R['status'])
        save_state()
        return 1
    ok, msg = budget_ok()
    R['budget_msg'] = msg
    say('budget gate: %s -> %s' % (msg, 'PROCEED' if ok else 'REFUSE'))
    save_state()
    if not ok:
        R['status'] = 'STOP (budget): %s. The set was NOT opened. 0 Gemini calls.' % msg
        write_report(None, None, None, None, jload(os.path.join(SET, 'selection.json')), None,
                     RUN, R['status'])
        save_state()
        return 1
    try:
        pipeline(stub=False)
    except Exception as e:
        import traceback
        say(traceback.format_exc())
        R['status'] = 'DRIVER EXCEPTION: %s' % e
        try:
            write_report(jload(os.path.join(RUN, 'results_1u.json')), None, None,
                         R.get('judge_noise'), jload(os.path.join(SET, 'selection.json')),
                         calls_stats(RUN), RUN, R['status'])
        except Exception:
            say(traceback.format_exc())
    save_state()
    try:
        commit('Phase 2F PART 3.1: PROBE result (Slovak production sentences)')
    except Exception as e:
        say('final commit failed: %s' % e)
    return 0


if __name__ == '__main__':
    sys.exit(main())
