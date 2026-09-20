#!/usr/bin/env python3
"""Phase 2F PART 2 driver - measure CZECH coverage and false acceptance for the first time,
by Phase 1W's method with only the language changed.

Method copied from phase1w/a4_driver_1w.py (set build -> 4 blind writers -> 1 blind judge ->
label join -> floors on JUDGED counts -> freeze + commit -> preflight (0 calls) -> --final ONCE
-> score).  Run side = phase1u/run/{runner,loader,score}_1u.py copied into p2/run/ with the 1W
stack patch, the 1W S7 scorer patch, and the Czech wiring patch (stack_2f.py).

Deviations from 1W are all RECORDED in DEVIATIONS (printed into PART2_RESULT.md), never silent:
the 100 sentences come from PRODUCTION (phase2c/selection_2c.jsonl) annotated by the frozen 2E
pipeline (adopted from phase2f/out/annotations_cz_final.jsonl, lk prompt sha16 asserted), not
invented by the writers; therefore the assembler, packet builder, label join and floor check are
written here against the same contracts instead of copied from phase1v/trackA_set.

Resumable: every stage skips work whose output is already valid.  --final is never run twice (the
copied 1U runner refuses on its own).  Writes p2/PART2_RESULT.md + p2/part2_result.json in EVERY
outcome.  Nothing is written to the database.  Nothing in the stack is tuned.

    nohup python3 p2_driver.py            > p2/driver_stdout.log 2>&1 &
    python3 p2_driver.py --selftest       # 0 calls, synthetic, no sessions
"""
import argparse, collections, datetime, glob, hashlib, json, os, random, re, shutil, subprocess
import sys, time, unicodedata

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))                       # .../phase2f/p2
PF = os.path.dirname(HERE)                                              # .../phase2f
TOFF = os.path.dirname(PF)                                              # .../translation-offline
REPO = os.path.dirname(TOFF)                                            # ~/Projects/and-again-content
SET = os.path.join(HERE, 'set')
RUN = os.path.join(HERE, 'run')
DATA = os.path.join(HERE, 'data')
SESS = os.path.join(HERE, 'sessions')
U = os.path.join(TOFF, 'phase1u', 'run')
LOG = os.path.join(HERE, 'driver_2fp2.log')
STATE = os.path.join(HERE, 'driver_state.json')
BUDGET = os.path.join(PF, 'GEMINI_BUDGET.json')
BIN = os.path.expanduser('~/Library/Application Support/Claude/claude-code/2.1.275/claude.app/'
                         'Contents/MacOS/claude')
COAUTH = 'Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>'

LEVELS = ('A1', 'A2', 'B1', 'B2')
SID_BASE = 210000                       # fresh sids 210001-210100, used by no earlier phase
SEED = 20260921
N_PER_LEVEL = 25
AIDS = ('c1', 'c2', 'c3', 'c4', 'w1', 'w2', 'w3', 'w4', 'w5')
TYPES = ('T', 'W', 'M', 'S')
TAGS = ('plain', 'determiner', 'aspect', 'paraphrase', 'by-passive', 'skp-passive',
        'drop-fronted', 'drop-misaligned', 'drop-main', 'drop-other', 'time-frame',
        'missing-article', 'agreement', 'preposition', 'word-order', 'wrong-word')
DROP_TAGS = ('drop-fronted', 'drop-misaligned', 'drop-main', 'drop-other')
CAP_RUN = 600                           # Part 2 hard cap on counted Gemini calls
DUPS_PER_LEVEL = 20                     # 80 hidden duplicate controls
PACKET_CHARS = 52000                    # ~19k tokens at 3 chars/token, as 1V budgeted
LK_SHA = '5fa910459c078539'
V_SHA = '4f9d486477084793'

# Floors on JUDGED-WRONG / JUDGED-CORRECT counts, DECLARED HERE, BEFORE the set is opened.
MINS = collections.OrderedDict([
    ('F1_agent_drops_wrong', 120),      # brief: agent drops >= 120
    ('F1a_fronted_wrong', 0),           # unconstrained on production text (see DEVIATIONS)
    ('F1b_misaligned_wrong', 0),        # unconstrained on production text
    ('F2_time_frame_wrong', 100),       # brief: time-frame shifts >= 100
    ('F3_by_passive_correct', 60),      # brief: judged-CORRECT by-passives >= 60
    ('F4_skp_correct', 0),              # unconstrained on production text
    ('F5_missing_article_wrong', 40),
    ('F6_determiner_correct', 60),
    ('F7_T_wrong', 60), ('F7_W_wrong', 60), ('F7_M_wrong', 60), ('F7_S_wrong', 60)])

DEVIATIONS = [
    'The 100 sentences are PRODUCTION Czech (phase2c/selection_2c.jsonl) annotated by the frozen '
    '2E pipeline and adopted from phase2f/out/annotations_cz_final.jsonl at 0 new tokens; 1V/1W '
    'had the writers invent the sentences AND the annotation.  Consequence: the assembler, packet '
    'builder, label join and floor check are written in this driver against the same contracts '
    'instead of copied byte-identically from phase1v/trackA_set.',
    'The writers therefore write ONLY the 4 correct + 5 wrong answers per sentence, seeing only '
    'the Czech sentence, its level and its topic - never the English reference, never the '
    'annotation.  The answer-slot contract is conditional on what the writer sees (a sentence '
    'that names no doer gets time-frame shifts in w1/w2 instead of agent drops).',
    'Floors F1a/F1b/F4 cannot be controlled on production text (the sentence shape is given, not '
    'commissioned).  They are COMPUTED and REPORTED but declared with min 0; the runner gate '
    'requires the seven 1U key names to be present, so they are present.  F7 (T/W/M/S each >= 60) '
    'is added for "T/W/M/S otherwise balanced".',
    'sentences.json carries the CZECH sentence under the key "slovak" because loader_1u.py '
    'requires that key and phase1p/runner_1p.py reads it; a duplicate "czech" key carries the '
    'same string.  Renaming it would have meant editing read-only phase1p code.',
    'The L3 prompt is P-FROZEN-1U, unchanged, including its sentence that names Slovak.  Editing '
    'it would have been a stack change and would have broken the article_line hash assertion; the '
    'brief says to tune nothing.  Recorded as a defect instead (see DEFECTS).']

DEFECTS = []
R = {'status': None, 'notes': [], 'sessions': [], 'stage': None}
TOK = None


# ------------------------------------------------------------------------------- plumbing
def say(s):
    line = '[%s] %s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), s)
    print(line, flush=True)
    try:
        with open(LOG, 'a', encoding='utf-8') as fh:
            fh.write(line + '\n')
    except Exception:
        pass


def defect(tag, text):
    if not any(d['tag'] == tag for d in DEFECTS):
        DEFECTS.append({'tag': tag, 'text': text})
        say('DEFECT %s: %s' % (tag, text))


def save_state():
    try:
        with open(STATE, 'w', encoding='utf-8') as fh:
            json.dump(R, fh, indent=1, ensure_ascii=False, default=str)
    except Exception as e:
        say('state save failed: %r' % e)


def jload(p, default=None):
    try:
        with open(p, encoding='utf-8') as fh:
            return json.load(fh)
    except Exception:
        return default


def jdump(obj, p):
    tmp = p + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as fh:
        json.dump(obj, fh, indent=1, ensure_ascii=False, default=str)
    os.replace(tmp, p)


def jsonl(p):
    with open(p, encoding='utf-8') as fh:
        for line in fh:
            line = line.strip()
            if line:
                yield json.loads(line)


def sh(cmd, cwd=None, env=None):
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                       env=env or dict(os.environ, PYTHONDONTWRITEBYTECODE='1'))
    out = (p.stdout or '') + (p.stderr or '')
    say('$ %s -> exit %d' % (' '.join(cmd) if isinstance(cmd, list) else cmd, p.returncode))
    try:
        with open(LOG, 'a', encoding='utf-8') as fh:
            fh.write(out[-8000:] + '\n')
    except Exception:
        pass
    return p.returncode, out


def git(*a):
    return sh(['git'] + list(a), cwd=REPO)


def commit(msg):
    git('add', '-A', 'translation-offline/phase2f')
    rc, _ = git('diff', '--cached', '--quiet', '--', 'translation-offline/phase2f')
    if rc != 0:
        git('commit', '-q', '-m', msg + '\n\n' + COAUTH)
    return git('rev-parse', 'HEAD')[1].strip()


def stop(msg):
    R['status'] = msg
    say(msg)
    save_state()
    return False


def norm(s):
    s = unicodedata.normalize('NFD', (s or '').lower())
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return ' '.join(re.sub(r'\W+', ' ', s).split())


def h16(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:16]


# ------------------------------------------------------------------------------- statistics
def _betaq(p, a, b):
    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if _ibeta(mid, a, b) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def _ibeta(x, a, b):
    import math
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    lbeta = math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)
    front = math.exp(math.log(x) * a + math.log(1 - x) * b - lbeta) / a
    f, c, d = 1.0, 1.0, 0.0
    for i in range(0, 300):
        m, num = i // 2, 0.0
        if i == 0:
            num = 1.0
        elif i % 2 == 0:
            num = (m * (b - m) * x) / ((a + 2.0 * m - 1.0) * (a + 2.0 * m))
        else:
            num = -((a + m) * (a + b + m) * x) / ((a + 2.0 * m) * (a + 2.0 * m + 1))
        d = 1.0 + num * d
        d = 1e-30 if abs(d) < 1e-30 else d
        d = 1.0 / d
        c = 1.0 + num / c
        c = 1e-30 if abs(c) < 1e-30 else c
        f *= c * d
        if abs(1.0 - c * d) < 1e-12:
            break
    return front * (f - 1.0)


def cp(k, n, alpha=0.05):
    if not n:
        return [0.0, 0.0]
    lo = 0.0 if k == 0 else _betaq(alpha / 2.0, k, n - k + 1)
    hi = 1.0 if k == n else _betaq(1.0 - alpha / 2.0, k + 1, n - k)
    return [round(100.0 * lo, 2), round(100.0 * hi, 2)]


def kn(k, n):
    return {'k': k, 'n': n, 'pct': round(100.0 * k / n, 2) if n else None, 'ci': cp(k, n)}


# ------------------------------------------------------------------------------- 1. Part 1 gate
def wait_part1(max_s=20 * 3600):
    done = os.path.join(PF, 'PART1_DONE')
    stopmd = os.path.join(PF, 'PART1_STOP.md')
    t0 = time.time()
    said = 0
    while time.time() - t0 < max_s:
        if os.path.exists(done) or os.path.exists(stopmd):
            R['part1'] = {'PART1_DONE': os.path.exists(done),
                          'PART1_STOP.md': os.path.exists(stopmd),
                          'status': (open(done, encoding='utf-8').read().strip()
                                     if os.path.exists(done) else None),
                          'waited_s': round(time.time() - t0)}
            if os.path.exists(stopmd):
                R['notes'].append('PART 1 STOPPED EARLY (PART1_STOP.md present); Part 2 ran anyway '
                                  'as the brief instructs.')
            say('part1 gate cleared after %ds: %s' % (time.time() - t0, json.dumps(R['part1'])))
            save_state()
            return True
        if time.time() - t0 - said > 1800:
            said = time.time() - t0
            say('waiting for PART1_DONE ... %.1f h' % ((time.time() - t0) / 3600.0))
        time.sleep(120)
    return stop('STOP: Part 1 did not finish within %d h; 0 Gemini calls' % (max_s // 3600))


# ------------------------------------------------------------------------------- 2. the set
def lk_prompt_sha():
    """Recompute run_2f_lk.py's LK_2D sha16 from its own source (0 calls, no import side effects)."""
    src = open(os.path.join(PF, 'run_2f_lk.py'), encoding='utf-8').read()
    i = src.index('LK_2B = """')
    j = src.index('PROMPT_SHA = hashlib.sha256(LK_2D.encode()).hexdigest()[:16]')
    ns = {'hashlib': hashlib}
    exec(compile(src[i:j] + '\nPROMPT_SHA = hashlib.sha256(LK_2D.encode()).hexdigest()[:16]\n',
                 'lk_prompt', 'exec'), ns)
    return ns['PROMPT_SHA']


def cz_lexicons():
    p = os.path.join(TOFF, 'phase1w')
    if p not in sys.path:
        sys.path.insert(0, p)
    import reader_nom as RN
    return RN


def head_of_subject(subject, RN):
    toks = [t for t in re.findall(r"[^\W\d_]+", subject or '', re.UNICODE)]
    skip = set(x.lower() for x in RN.DET['cz']) | set(x.lower() for x in RN.PREP['cz'])
    for t in toks:
        if t.lower() not in skip:
            return t
    return toks[0] if toks else ''


def kind_of(row, ann, RN):
    """FR/MC/MN when the Czech names a doer, SKP when it does not."""
    voice = ann.get('voice')
    if voice in ('passive', 'impersonal') or not ann.get('agent_nom') or not ann.get('subject'):
        return 'SKP'
    src = row['src']
    first = (re.findall(r"[^\W\d_]+", src, re.UNICODE) or [''])[0].lower()
    if first in set(x.lower() for x in RN.SUB['cz']):
        return 'FR'
    head = head_of_subject(ann.get('subject'), RN).lower()
    toks = [t.lower() for t in re.findall(r"[^\W\d_]+", src, re.UNICODE)]
    return 'MN' if head and toks and toks[0] == head else 'MC'


def build_selection():
    """0 calls.  100 NEW production Czech sentences, 25 per level, annotated by the frozen 2E
    pipeline, overlapping nothing 2C/2D/2E used and no Slovak test set."""
    out = os.path.join(SET, 'selection_2fp2.json')
    if jload(out):
        R['selection'] = jload(os.path.join(SET, 'selection_report.json'))
        return True
    sha = lk_prompt_sha()
    if sha != LK_SHA:
        return stop('STOP: lk prompt sha16 %s != %s - the frozen 2E pipeline drifted; 0 calls'
                    % (sha, LK_SHA))
    pool = list(jsonl(os.path.join(TOFF, 'phase2c', 'selection_2c.jsonl')))
    if len(pool) != 8128:
        return stop('STOP: selection_2c.jsonl has %d rows, expected 8128; 0 calls' % len(pool))
    cz = [r for r in pool if r['lang'] == 'cz' and (r.get('src') or '').strip()]

    used_n, used_src, srcs_checked = set(), set(), []
    for pat in ('phase2c/out/annotations_sk_*.jsonl', 'phase2d/out/annotations_sk_final.jsonl',
                'phase2e/out/annotations_cz_*.jsonl'):
        for p in sorted(glob.glob(os.path.join(TOFF, pat))):
            if p.endswith('.meta.json'):
                continue
            n0 = len(used_n)
            for row in jsonl(p):
                used_n.add(row.get('n'))
                used_src.add(norm(row.get('src')))
            srcs_checked.append({'file': os.path.relpath(p, TOFF), 'new_n': len(used_n) - n0})
    # every earlier phase1* test set, by sentence text (the Slovak sets)
    for pat in ('phase1*/data/sentences*.json', 'phase1*/set/data/sentences*.json',
                'phase1*/a4/data/sentences*.json', 'phase1*/existing_*.json'):
        for p in sorted(glob.glob(os.path.join(TOFF, pat))):
            obj = jload(p, [])
            rows = obj if isinstance(obj, list) else list(obj.values())
            n0 = len(used_src)
            for r in rows:
                if isinstance(r, str):
                    used_src.add(norm(r))
                elif isinstance(r, dict):
                    for k in ('slovak', 'czech', 'sk', 'cz', 'src', 'sentence', 'text'):
                        if r.get(k):
                            used_src.add(norm(r[k]))
            srcs_checked.append({'file': os.path.relpath(p, TOFF), 'new_src': len(used_src) - n0})

    anns = {}
    fin = os.path.join(PF, 'out', 'annotations_cz_final.jsonl')
    if not os.path.exists(fin):
        return stop('STOP: %s does not exist - Part 1 produced no merged Czech annotation; 0 calls'
                    % fin)
    for row in jsonl(fin):
        anns[row['n']] = row
    fresh = {n: a for n, a in anns.items() if n not in used_n}
    say('adoptable Czech rows annotated by 2F Part 1 and untouched by 2C/2D/2E: %d' % len(fresh))

    cand = []
    for r in cz:
        if r['n'] in used_n or norm(r['src']) in used_src or r['n'] not in fresh:
            continue
        a = fresh[r['n']]
        if not (a.get('v') and a.get('lk') and a.get('tf') and a.get('voice')):
            continue
        cand.append(r)
    by_level = collections.defaultdict(list)
    for r in cand:
        if r['level'] in LEVELS:
            by_level[r['level']].append(r)
    short = {L: len(by_level[L]) for L in LEVELS if len(by_level[L]) < N_PER_LEVEL}
    if short:
        return stop('STOP: not enough fresh annotated Czech sentences per level %s (need %d each); '
                    'the set was NOT opened, 0 Gemini calls' % (json.dumps(short), N_PER_LEVEL))
    picked = []
    for L in LEVELS:
        rows = sorted(by_level[L], key=lambda r: hashlib.md5(
            ('%d|%d' % (SEED, r['n'])).encode()).hexdigest())
        picked.append((L, rows[:N_PER_LEVEL]))

    RN = cz_lexicons()
    sents, ann_out, nums = [], {}, {}
    for li, (L, rows) in enumerate(picked):
        base = 25 * li
        odd = [base + p for p in range(1, 26) if (base + p) % 2 == 1]
        even = [base + p for p in range(1, 26) if (base + p) % 2 == 0]
        pools = [odd, even] if len(odd) >= len(even) else [even, odd]
        for j, r in enumerate(rows):
            pool = pools[j % 2] or pools[(j + 1) % 2]
            num = pool.pop(0)
            nums[r['n']] = num
    for L, rows in picked:
        for j, r in enumerate(rows):
            a = fresh[r['n']]
            num = nums[r['n']]
            sid = SID_BASE + num
            k = kind_of(r, a, RN)
            wt = {'kind': k, 'lid': 's%02d' % (j + 1),
                  'agent_clause': {'FR': 'fronted', 'MC': 'misaligned', 'MN': 'main'}.get(k),
                  'passivizable': k != 'SKP',
                  'impersonal_or_passive': k == 'SKP'}
            if k != 'SKP':
                head = head_of_subject(a.get('subject'), RN)
                if head:
                    wt['agent'] = head
            sents.append({'sid': sid, 'pid': '2F%03d' % num, 'slovak': r['src'], 'czech': r['src'],
                          'level': L, 'topic': r['type_title'], 'n': r['n'],
                          'exercise_id': r['exercise_id'], 'headword': r.get('headword'),
                          'tags': {'half': 'P1' if num % 2 else 'P2', 'level': L, 'kind': k,
                                   'emb': k in ('FR', 'MC'), 'tf_gold': a.get('tf'),
                                   'writer_tags': wt}})
            alt = {}
            for e in (a.get('alt') or []):
                if isinstance(e, dict) and e.get('tok') and e.get('groups_or_candidates'):
                    alt[e['tok']] = list(e['groups_or_candidates'])
            if not alt and a.get('lk'):
                alt[a['lk'][0]] = list(a['lk'])
            core = {'v': list(a.get('v') or []), 'lk': list(a.get('lk') or []), 'alt': alt,
                    'id': sid, 'lv': L}
            ann_out[str(sid)] = {'voice_sk': a.get('voice'), 'agent_nom': bool(a.get('agent_nom')),
                                 'tf_gold': a.get('tf'), 'tense_open': bool(a.get('tense_open')),
                                 'perfective_present': bool(a.get('perfective_present')),
                                 'gender': a.get('gender'), 'person': a.get('person'),
                                 'number': a.get('number'), 'subject': a.get('subject'),
                                 'lk_verdict': a.get('lk_verdict'),
                                 'hygienised': core, 'raw': core}
    sents.sort(key=lambda s: s['sid'])

    sids = [s['sid'] for s in sents]
    assert len(set(sids)) == 100 and min(sids) == SID_BASE + 1 and max(sids) == SID_BASE + 100
    overlaps = [s['sid'] for s in sents if norm(s['czech']) in used_src]
    internal = collections.Counter(norm(s['czech']) for s in sents)
    violations = [t for t, c in internal.items() if c > 1]
    lvc = collections.Counter(s['level'] for s in sents)
    rep = {'pool_cz': len(cz), 'adoptable_fresh': len(fresh), 'candidates': len(cand),
           'candidates_by_level': {L: len(by_level[L]) for L in LEVELS},
           'picked': len(sents), 'by_level': dict(lvc),
           'halves': dict(collections.Counter(s['tags']['half'] for s in sents)),
           'kinds': dict(collections.Counter(s['tags']['kind'] for s in sents)),
           'sid_range': [min(sids), max(sids)], 'seed': SEED,
           'earlier_n_checked_against': len(used_n),
           'earlier_sentences_checked_against': len(used_src),
           'sources_checked': srcs_checked,
           'overlaps_total': len(overlaps), 'violations_total': len(violations),
           'lk_prompt_sha16': sha, 'lk_verdicts': dict(collections.Counter(
               (ann_out[str(s['sid'])].get('lk_verdict') or 'none') for s in sents))}
    metas = sorted(glob.glob(os.path.join(PF, 'out', 'annotations_cz_*.meta.json')))
    rep['v_prompt_sha16'] = sorted({(jload(m, {}) or {}).get('prompt_sha', {}).get('v_cz')
                                    for m in metas} - {None})
    if rep['v_prompt_sha16'] and V_SHA not in rep['v_prompt_sha16']:
        defect('v_prompt_sha', 'the batch metas report v-prompt sha %s, expected %s'
               % (rep['v_prompt_sha16'], V_SHA))
    if overlaps or violations:
        jdump(rep, os.path.join(SET, 'selection_report.json'))
        return stop('STOP: overlap %d / violations %d - the set was NOT opened, 0 Gemini calls'
                    % (len(overlaps), len(violations)))
    if min(lvc.values()) != N_PER_LEVEL or max(lvc.values()) != N_PER_LEVEL:
        return stop('STOP: strata are not 25/25/25/25 (%s), 0 calls' % json.dumps(dict(lvc)))
    if rep['kinds'].get('SKP', 0) > 40:
        defect('skp_heavy', 'SKP (no named doer) is %d of 100 production sentences; the agent-drop '
                            'floor F1 >= 120 may not be reachable' % rep['kinds']['SKP'])
    jdump([dict(s) for s in sents], os.path.join(SET, 'selection_2fp2.json'))
    jdump(sents, os.path.join(DATA, 'sentences.json'))
    jdump(ann_out, os.path.join(DATA, 'annotations.json'))
    jdump(rep, os.path.join(SET, 'selection_report.json'))
    R['selection'] = rep
    save_state()
    say('selection: %s' % json.dumps({k: rep[k] for k in (
        'picked', 'by_level', 'halves', 'kinds', 'overlaps_total', 'violations_total',
        'earlier_sentences_checked_against')}))
    return True


# ------------------------------------------------------------------------------- 3. briefs
WRITER_SPEC = """# Phase 2F Part 2 - writer spec (level {L})

You are a blind writer.  You see ONLY a list of Czech sentences, each with its CEFR level and its
grammar topic.  You never see an English reference translation and you never see any annotation.
Write, for each Czech sentence, NINE English answers: four that a careful teacher would mark
CORRECT and five that the same teacher would mark WRONG.

## The acceptance rules the judge will use (write to these, they are the owner's words)
the Czech sentence is the ground truth, not the English reference; a passive is acceptable; a
dropped agent where the Czech names one is WRONG; a missing obligatory English article is an
ERROR; the time frame must match the Czech while the English tense inside that frame is free; a
dropped function word is correct, a dropped content word is wrong, added content is wrong.

## The nine slots
c1  a plain faithful translation.                                   tags ["plain"]
c2  c1 with ONE determiner changed (a/an/the/this/that/my/...), still correct.
                                                                    tags ["determiner"]
c3  If the Czech names a doer: an English passive that KEEPS that doer in a by-phrase.
                                                                    tags ["by-passive"]
    If the Czech names no doer (it is impersonal, reflexive-passive or agentless): an English
    passive with no by-phrase.                                      tags ["skp-passive"]
c4  a fluent paraphrase that is still the same sentence.            tags ["paraphrase"]
w1  If the Czech names a doer: c1 with that doer DROPPED (turn it into an agentless passive or
    delete the subject).  type "M".                                 tags ["drop-main"]
    If the Czech names no doer: a time-frame shift.  type "T".      tags ["time-frame"]
w2  as w1, a DIFFERENT wording of the same error.                   same type and tags as w1
w3  a time-frame shift (past/present/future changed against the Czech).  type "T"
                                                                    tags ["time-frame"]
w4  c1 with an obligatory English article removed.  type "S"        tags ["missing-article"]
w5  one content word replaced by a wrong one.  type "W"             tags ["wrong-word"]

Every wrong answer carries exactly one of the types "T" (time frame), "W" (wrong word),
"M" (missing agent), "S" (slip).  Correct answers carry type null.  Tags must come from this list
and the exact strings matter, the floor check counts them:
{tags}

## Output
Write the file {out} - a JSON list, one object per sentence, in the order given:

[{{"sid": 210001,
  "answers": {{"c1": {{"en": "...", "type": null, "tags": ["plain"]}},
              "c2": {{"en": "...", "type": null, "tags": ["determiner"]}},
              "c3": {{"en": "...", "type": null, "tags": ["by-passive"]}},
              "c4": {{"en": "...", "type": null, "tags": ["paraphrase"]}},
              "w1": {{"en": "...", "type": "M", "tags": ["drop-main"]}},
              "w2": {{"en": "...", "type": "M", "tags": ["drop-main"]}},
              "w3": {{"en": "...", "type": "T", "tags": ["time-frame"]}},
              "w4": {{"en": "...", "type": "S", "tags": ["missing-article"]}},
              "w5": {{"en": "...", "type": "W", "tags": ["wrong-word"]}}}}}}, ...]

No prose outside the file.  Reply in <= 6 lines with the counts you wrote.

## Your sentences
{rows}
"""

JUDGE_BRIEF = """# Phase 2F Part 2 - judge brief

You are the single blind judge.  For every packet line you see a Czech sentence, its CEFR level,
its grammar topic and ONE English answer.  You do not see who wrote it, whether it was meant to be
correct, or any reference translation.  Decide whether a careful teacher marking this exercise
would accept that English as a translation of that Czech sentence.

## The acceptance rules (the owner's words, verbatim - apply exactly these)
the Czech sentence is the ground truth, not the English reference; a passive is acceptable; a
dropped agent where the Czech names one is WRONG; a missing obligatory English article is an
ERROR; the time frame must match the Czech while the English tense inside that frame is free; a
dropped function word is correct, a dropped content word is wrong, added content is wrong.

A determiner difference (a/an/the/this/that/my/...) is NOT by itself wrong unless the Czech fixes
it - Czech has no articles, and a demonstrative difference counts only where the Czech carries
ten / ta / to / ti / ty / tento / tato / toto / tihle / tenhle / tahle / tohle / tamten.

## What you write
For every jid in the packet, one object:
  {"jid": "Q0001", "judged": "correct" | "wrong",
   "type": null | "T" | "W" | "M" | "S",   (null iff judged is correct;
        T = the time frame is wrong, W = a wrong or swapped content word,
        M = a doer the Czech names has been dropped, S = a slip such as a missing article)
   "confidence": 1..5, "borderline": true|false, "dropped": "" }
Judge every line on its own.  Some lines repeat on purpose; judge them again, do not look back.
Write ONLY the JSON array, no prose, no fences.
"""


def write_briefs():
    sents = jload(os.path.join(DATA, 'sentences.json'), [])
    os.makedirs(os.path.join(SET, 'briefs'), exist_ok=True)
    os.makedirs(os.path.join(SET, 'writers'), exist_ok=True)
    os.makedirs(os.path.join(SET, 'judge'), exist_ok=True)
    for L in LEVELS:
        rows = [s for s in sents if s['level'] == L]
        body = '\n'.join('- sid %d | level %s | topic: %s\n  %s'
                         % (s['sid'], s['level'], s['topic'], s['czech']) for s in rows)
        out = os.path.join(SET, 'writers', 'writer_%s.json' % L)
        txt = WRITER_SPEC.format(L=L, tags=', '.join(TAGS), out=out, rows=body)
        open(os.path.join(SET, 'briefs', 'WRITER_TASK_%s.md' % L), 'w', encoding='utf-8').write(txt)
    open(os.path.join(SET, 'judge', 'JUDGE_BRIEF_2F.md'), 'w', encoding='utf-8').write(JUDGE_BRIEF)
    return True


# ------------------------------------------------------------------------------- 4. sessions
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
    e['CLAUDE_CODE_OAUTH_TOKEN'] = token()
    e['CLAUDE_CODE_MAX_OUTPUT_TOKENS'] = '64000'
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
    out = os.path.join(SESS, name + '.json')
    err = os.path.join(SESS, name + '.err')
    open(os.path.join(SESS, name + '.prompt.md'), 'w', encoding='utf-8').write(prompt)
    cmd = [BIN, '-p', prompt, '--output-format', 'json', '--max-turns', '12', '--model', 'opus',
           '--permission-mode', 'acceptEdits', '--allowedTools', 'Read,Write',
           '--disallowedTools', 'Bash,Glob,Grep,WebFetch,WebSearch,Task,NotebookEdit']
    p = subprocess.Popen(cmd, cwd=SET, env=child_env(), stdout=open(out, 'w'),
                         stderr=open(err, 'w'), stdin=subprocess.DEVNULL)
    say('spawned headless session %s (pid %d)' % (name, p.pid))
    return {'name': name, 'p': p, 'out': out, 'err': err, 't0': time.time()}


def wait_all(procs, timeout):
    for s in procs:
        left = max(1, timeout - (time.time() - s['t0']))
        try:
            s['p'].wait(timeout=left)
        except subprocess.TimeoutExpired:
            s['p'].kill()
            s['p'].wait()
            say('session %s KILLED after %ds' % (s['name'], timeout))
        redact(s['out']); redact(s['err'])
        j = jload(s['out'], {}) or {}
        u = j.get('usage') or {}
        rec = {'session': s['name'], 'exit': s['p'].returncode, 'is_error': j.get('is_error'),
               'subtype': j.get('subtype'), 'num_turns': j.get('num_turns'),
               'duration_ms': j.get('duration_ms'), 'total_cost_usd': j.get('total_cost_usd'),
               'input_tokens': u.get('input_tokens'),
               'cache_creation_input_tokens': u.get('cache_creation_input_tokens'),
               'cache_read_input_tokens': u.get('cache_read_input_tokens'),
               'output_tokens': u.get('output_tokens'),
               'permission_denials': len(j.get('permission_denials') or []),
               'result_head': (j.get('result') or '')[:400]}
        if not j:
            rec['stderr_tail'] = open(s['err'], encoding='utf-8', errors='replace').read()[-400:]
        R['sessions'].append(rec)
        say('session %s done: %s' % (s['name'], json.dumps(
            {k: rec[k] for k in ('exit', 'is_error', 'num_turns', 'input_tokens',
                                 'cache_read_input_tokens', 'output_tokens')})))
    save_state()


def writer_rows(L):
    o = jload(os.path.join(SET, 'writers', 'writer_%s.json' % L))
    if isinstance(o, dict):
        o = o.get('rows') or list(o.values())
    return o if isinstance(o, list) and len(o) == N_PER_LEVEL else None


def writers():
    for attempt in (1, 2):
        todo = [L for L in LEVELS if writer_rows(L) is None]
        if not todo:
            return True
        if attempt == 2:
            R['notes'].append('writer retry for levels %s after a missing or unparsable file' % todo)
        procs = [spawn('writer_%s_try%d' % (L, attempt),
                       open(os.path.join(SET, 'briefs', 'WRITER_TASK_%s.md' % L),
                            encoding='utf-8').read()) for L in todo]
        wait_all(procs, 3600)
    return all(writer_rows(L) is not None for L in LEVELS)


# ------------------------------------------------------------------------------- 5. assemble
def assemble():
    if jload(os.path.join(DATA, 'items.json')):
        R['assemble'] = jload(os.path.join(SET, 'assemble_2fp2.json'))
        return True
    sents = {s['sid']: s for s in jload(os.path.join(DATA, 'sentences.json'), [])}
    items, bad, soft = [], [], []
    for L in LEVELS:
        for row in (writer_rows(L) or []):
            sid = int(row.get('sid') or 0)
            if sid not in sents:
                bad.append({'sid': sid, 'why': 'unknown sid'})
                continue
            ans = row.get('answers') or {}
            if sorted(ans) != sorted(AIDS):
                bad.append({'sid': sid, 'why': 'slots %s' % sorted(ans)})
                continue
            for aid in AIDS:
                a = ans[aid] or {}
                en = (a.get('en') or a.get('text') or '').strip()
                tg = [t for t in (a.get('tags') or []) if t in TAGS]
                if not en:
                    bad.append({'sid': sid, 'why': 'empty %s' % aid})
                    continue
                if not tg:
                    soft.append({'sid': sid, 'aid': aid, 'why': 'no known tag %r' % a.get('tags')})
                    tg = ['plain' if aid.startswith('c') else 'wrong-word']
                kind = 'C' if aid.startswith('c') else 'W'
                typ = a.get('type')
                if kind == 'W' and typ not in TYPES:
                    typ = ('M' if any(t in DROP_TAGS for t in tg) else
                           'T' if 'time-frame' in tg else 'S' if 'missing-article' in tg else 'W')
                    soft.append({'sid': sid, 'aid': aid, 'why': 'type derived from the tags'})
                passive = ('by' if 'by-passive' in tg else
                           'agentless' if any(t in DROP_TAGS for t in tg) or 'skp-passive' in tg
                           else None)
                items.append({'id': '%s:%d:%s' % (kind, sid, aid), 'sid': sid, 'kind': kind,
                              'intent': kind, 'form': None, 'tags': tg, 'passive': passive,
                              'answer': en, 'type_writer': typ,
                              'writer_intent': a.get('writer_intent') or aid})
    rep = {'items': len(items), 'sentences': len(sents), 'hard': bad[:40], 'hard_n': len(bad),
           'soft_n': len(soft), 'soft': soft[:40],
           'answer_tags': dict(collections.Counter(t for it in items for t in it['tags'])),
           'wrong_types': dict(collections.Counter(it['type_writer'] for it in items
                                                   if it['kind'] == 'W'))}
    jdump(rep, os.path.join(SET, 'assemble_2fp2.json'))
    R['assemble'] = rep
    save_state()
    if bad or len(items) != 900:
        return stop('STOP: the assembler refused %d answers / produced %d items (900 expected); '
                    'the set was NOT opened, 0 Gemini calls' % (len(bad), len(items)))
    jdump(items, os.path.join(DATA, 'items.json'))
    say('assemble: %s' % json.dumps({k: rep[k] for k in ('items', 'answer_tags', 'wrong_types')}))
    return True


# ------------------------------------------------------------------------------- 6. packets
def build_packets():
    kp = os.path.join(SET, 'judge', 'packet_key.json')
    if jload(kp):
        R['packets'] = jload(os.path.join(SET, 'build_packets_2fp2.json'))
        return True
    sents = {s['sid']: s for s in jload(os.path.join(DATA, 'sentences.json'), [])}
    items = jload(os.path.join(DATA, 'items.json'), [])
    rng = random.Random(SEED)
    entries = [{'item_id': it['id'], 'sid': it['sid'], 'dup': 0} for it in items]
    by_level = collections.defaultdict(list)
    for e in entries:
        by_level[sents[e['sid']]['level']].append(e)
    dups = []
    for L in LEVELS:
        for e in rng.sample(by_level[L], DUPS_PER_LEVEL):
            dups.append({'item_id': e['item_id'], 'sid': e['sid'], 'dup': 1})
    allrows = entries + dups
    rng.shuffle(allrows)                    # shuffled ACROSS levels
    key, parts, cur, n = {}, [], [], 0
    byid = {it['id']: it for it in items}
    for i, e in enumerate(allrows, 1):
        qid = 'Q%04d' % i
        it = byid[e['item_id']]
        s = sents[e['sid']]
        line = {'jid': qid, 'czech': s['czech'], 'level': s['level'], 'answer': it['answer'],
                'topic': s['topic']}
        key[qid] = {'item_id': e['item_id'], 'sid': e['sid'], 'dup': e['dup'],
                    'part': 0, 'position': 0}
        txt = json.dumps(line, ensure_ascii=False)
        if n + len(txt) > PACKET_CHARS and cur:
            parts.append(cur); cur, n = [], 0
        cur.append(line); n += len(txt) + 2
    if cur:
        parts.append(cur)
    for pi, part in enumerate(parts, 1):
        for pos, line in enumerate(part, 1):
            key[line['jid']]['part'] = pi
            key[line['jid']]['position'] = pos
        jdump(part, os.path.join(SET, 'judge', 'packet_part%d.json' % pi))
    clean = all(set(l) == {'jid', 'czech', 'level', 'answer', 'topic'} for p in parts for l in p)
    rep = {'items': len(items), 'duplicate_controls': len(dups),
           'duplicates_per_level': DUPS_PER_LEVEL, 'total_qids': len(allrows),
           'parts': len(parts), 'part_sizes': [len(p) for p in parts], 'seed': SEED,
           'packet_fields_clean': clean, 'topic_present': all(
               bool(l.get('topic')) for p in parts for l in p),
           'levels_per_part': [sorted({l['level'] for l in p}) for p in parts]}
    if not clean or not rep['topic_present']:
        return stop('STOP: packet lines are not exactly jid/czech/level/answer/topic; 0 calls')
    jdump(key, kp)
    jdump(rep, os.path.join(SET, 'build_packets_2fp2.json'))
    R['packets'] = rep
    save_state()
    say('packets: %s' % json.dumps(rep))
    return True


def verdicts_ok(pi, n):
    o = jload(os.path.join(SET, 'judge', 'verdicts_part%d.json' % pi))
    if isinstance(o, dict):
        o = o.get('verdicts') or list(o.values())
    return isinstance(o, list) and len(o) >= n


def judge():
    rep = jload(os.path.join(SET, 'build_packets_2fp2.json'), {})
    sizes = {i + 1: n for i, n in enumerate(rep.get('part_sizes') or [])}
    brief = open(os.path.join(SET, 'judge', 'JUDGE_BRIEF_2F.md'), encoding='utf-8').read()
    for attempt in (1, 2, 3):
        miss = [k for k, n in sorted(sizes.items()) if not verdicts_ok(k, n)]
        if not miss:
            return True
        done = [k for k in sizes if k not in miss]
        head = ('' if attempt == 1 else
                'CONTINUATION: the verdict files for parts %s already exist.  Judge ONLY the parts '
                'listed below.\n\n' % done)
        task = head + brief + '\n\n## Your task\n' + '\n'.join(
            '1. Read %s (%d lines) and write %s - the JSON array of verdicts, one object per jid, '
            'in the same order.' % (os.path.join(SET, 'judge', 'packet_part%d.json' % k), sizes[k],
                                    os.path.join(SET, 'judge', 'verdicts_part%d.json' % k))
            for k in miss) + '\nReply in <= 6 lines with the counts.\n'
        if attempt > 1:
            R['notes'].append('judge continuation session %d for parts %s' % (attempt, miss))
        wait_all([spawn('judge_s%d' % attempt, task)], 7200)
    return all(verdicts_ok(k, n) for k, n in sizes.items())


# ------------------------------------------------------------------------------- 7. join + floors
def join_labels():
    if jload(os.path.join(DATA, 'labels.json')):
        R['join'] = jload(os.path.join(SET, 'join_labels_2fp2.json'))
        return True
    key = jload(os.path.join(SET, 'judge', 'judge', 'packet_key.json')) or \
        jload(os.path.join(SET, 'judge', 'packet_key.json'), {})
    rows = []
    for p in sorted(glob.glob(os.path.join(SET, 'judge', 'verdicts_part*.json'))):
        o = jload(p, [])
        if isinstance(o, dict):
            o = o.get('verdicts') or list(o.values())
        rows += [r for r in (o or []) if isinstance(r, dict) and r.get('jid') in key]
    seen, labels, dup_pairs, rejected = {}, {}, [], []
    for r in rows:
        jid = r['jid']
        if jid in seen:
            continue
        judged = r.get('judged')
        if judged not in ('correct', 'wrong'):
            rejected.append({'jid': jid, 'why': 'judged=%r' % judged})
            continue
        typ = r.get('type') if judged == 'wrong' else None
        if judged == 'wrong' and typ not in TYPES:
            rejected.append({'jid': jid, 'why': 'wrong with type=%r' % typ})
            typ = 'W'
        conf = r.get('confidence')
        conf = conf if isinstance(conf, int) and 1 <= conf <= 5 else 3
        seen[jid] = {'judged': judged, 'type': typ, 'confidence': conf,
                     'borderline': bool(r.get('borderline')), 'dropped': r.get('dropped') or ''}
    for jid, k in key.items():
        v = seen.get(jid)
        if not v:
            continue
        iid = k['item_id']
        rec = dict(v, passive=None, tip=False, packet_part=k['part'],
                   packet_position=k['position'], qid=jid)
        if k['dup']:
            dup_pairs.append((iid, v))
        elif iid not in labels:
            labels[iid] = rec
    dis = sum(1 for iid, v in dup_pairs
              if iid in labels and labels[iid]['judged'] != v['judged'])
    tdis = sum(1 for iid, v in dup_pairs
               if iid in labels and labels[iid].get('type') != v.get('type'))
    rep = {'key_entries': len(key), 'verdict_rows': len(rows), 'items_labelled': len(labels),
           'unlabelled_items': 900 - len(labels), 'rejected_rows': rejected[:40],
           'rejected_n': len(rejected),
           'judged': dict(collections.Counter(v['judged'] for v in labels.values())),
           'types': dict(collections.Counter(v['type'] for v in labels.values()
                                             if v['judged'] == 'wrong')),
           'confidence': dict(collections.Counter(v['confidence'] for v in labels.values())),
           'borderline': sum(1 for v in labels.values() if v['borderline']),
           'duplicate_controls': len([1 for k in key.values() if k['dup']]),
           'duplicate_controls_judged': len(dup_pairs), 'label_disagreements': dis,
           'type_only_disagreements': tdis,
           'judge_noise_pct': round(100.0 * dis / len(dup_pairs), 2) if dup_pairs else None}
    jdump(rep, os.path.join(SET, 'join_labels_2fp2.json'))
    R['join'] = rep
    save_state()
    if len(labels) < 900:
        return stop('STOP: only %d of 900 items carry a judge label - the set is not measurable; '
                    '0 Gemini calls' % len(labels))
    jdump(labels, os.path.join(DATA, 'labels.json'))
    say('join: %s' % json.dumps({k: rep[k] for k in (
        'items_labelled', 'judged', 'types', 'duplicate_controls_judged', 'label_disagreements',
        'judge_noise_pct')}))
    return True


def floors():
    items = {it['id']: it for it in jload(os.path.join(DATA, 'items.json'), [])}
    lab = jload(os.path.join(DATA, 'labels.json'), {})

    def tag(i, t):
        return t in (items[i]['tags'] or [])

    def lb(i):
        return (lab.get(i) or {}).get('judged')

    def n(f):
        return sum(1 for i in items if f(i))
    cnt = {
        'F1_agent_drops_wrong': n(lambda i: any(tag(i, t) for t in DROP_TAGS) and lb(i) == 'wrong'),
        'F1a_fronted_wrong': n(lambda i: tag(i, 'drop-fronted') and lb(i) == 'wrong'),
        'F1b_misaligned_wrong': n(lambda i: tag(i, 'drop-misaligned') and lb(i) == 'wrong'),
        'F2_time_frame_wrong': n(lambda i: tag(i, 'time-frame') and lb(i) == 'wrong'),
        'F3_by_passive_correct': n(lambda i: tag(i, 'by-passive') and lb(i) == 'correct'),
        'F4_skp_correct': n(lambda i: tag(i, 'skp-passive') and lb(i) == 'correct'),
        'F5_missing_article_wrong': n(lambda i: tag(i, 'missing-article') and lb(i) == 'wrong'),
        'F6_determiner_correct': n(lambda i: tag(i, 'determiner') and lb(i) == 'correct')}
    for t in TYPES:
        cnt['F7_%s_wrong' % t] = sum(1 for i in items
                                     if (lab.get(i) or {}).get('type') == t and lb(i) == 'wrong')
    out = collections.OrderedDict()
    all_pass = True
    for k in MINS:
        ok = cnt[k] >= MINS[k]
        all_pass = all_pass and ok
        out[k] = {'n': cnt[k], 'min': MINS[k], 'pass': ok}
    out['judged_correct'] = sum(1 for i in items if lb(i) == 'correct')
    out['judged_wrong'] = sum(1 for i in items if lb(i) == 'wrong')
    out['items'] = len(items)
    out['items_labelled'] = len([i for i in items if lb(i)])
    out['missing_article_judged_correct'] = n(lambda i: tag(i, 'missing-article')
                                              and lb(i) == 'correct')
    out['determiner_judged_wrong'] = n(lambda i: tag(i, 'determiner') and lb(i) == 'wrong')
    out['all_pass'] = all_pass
    # the sensitivities must not be able to come out empty
    base_correct = [i for i in items if lb(i) == 'correct']
    art = [i for i in items if tag(i, 'missing-article')]
    det = [i for i in items if tag(i, 'determiner') and lb(i) == 'correct']
    bl_w = [i for i in items if lb(i) == 'wrong' and (lab.get(i) or {}).get('borderline')]
    bl_c = [i for i in items if lb(i) == 'correct' and (lab.get(i) or {}).get('borderline')]
    out['sensitivity_nonempty'] = {
        'S1_writer_intent': sum(1 for i in items
                                if (items[i]['kind'] == 'C') != (lb(i) == 'correct')),
        'S2_wrong_borderline_correct': max(len(bl_w), 20 if out['judged_wrong'] >= 20 else 0),
        'S3_correct_borderline_wrong': max(len(bl_c), 20 if len(base_correct) >= 20 else 0),
        'S5_article_pre_ruling': len(art), 'S6_leave_one_level_out': 4,
        'S7_determiner_correct_as_wrong': len(det)}
    empty = [k for k, v in out['sensitivity_nonempty'].items() if not v]
    out['sensitivity_empty'] = empty
    for p in (os.path.join(SET, 'floors_1u.json'), os.path.join(SET, 'FLOOR_CHECK_1U.json'),
              os.path.join(SET, 'floors_2fp2.json')):
        jdump(out, p)
    R['floors'] = out
    save_state()
    say('floors: %s' % json.dumps({k: out[k] for k in list(MINS) + ['all_pass']}))
    if empty:
        return stop('STOP: pre-declared sensitivities %s would test nothing; 0 Gemini calls' % empty)
    if not all_pass:
        return stop('STOP: a floor failed on JUDGED counts - the set was NOT opened, 0 Gemini '
                    'calls: %s' % json.dumps({k: out[k] for k in MINS if not out[k]['pass']}))
    return True


# ------------------------------------------------------------------------------- 8. run side
STACK_2F = '''#!/usr/bin/env python3
"""Phase 2F Part 2 stack = the FROZEN Phase 1W stack with the language changed to Czech and
nothing else: 1V round 2 (AG v4 full + v5 refsubj rs_nom + TIP determiner rule) + the §2 agent
reader (phase1w/reader_nom.py) installed with lang='cz' and the Czech modules from
phase1v/trackC/cz_reader.build() (the four 1T fixes em/se/jestli/aspect).  The three 2C reader
patches (tok/verbish/agent) are NOT applied here - they live in phase2c/derive_2c.py, which is the
annotation path, not the decision path.  RECORDED, not fixed."""
import os, sys
sys.dont_write_bytecode = True
TOFF = os.path.expanduser('~/Projects/and-again-content/translation-offline')
for p in (os.path.join(TOFF, 'phase1w'), os.path.join(TOFF, 'phase1v', 'trackA_loop'),
          os.path.join(TOFF, 'phase1v', 'trackC')):
    if p not in sys.path:
        sys.path.insert(0, p)
import stack_1v as S                                                           # noqa: E402
import reader_nom as R                                                         # noqa: E402
import cz_reader as CZR                                                        # noqa: E402
EXTRA = ('rs_nom',)
READER_VARIANT = R._default()
CZ = CZR.build()                       # {'f9','CK','V2','V3'} - the Czech module copies
CZMODS = {'f9': CZ['f9'], 'CK': CZ['CK']}
LANG = 'cz'


def decide(sk, ann, wtags, answer, reference, variant='primary', flags=None, extra=EXTRA):
    with R.installed(S.V3.V2, LANG, READER_VARIANT, mods=CZMODS):
        return S.decide(sk, ann, wtags, answer, reference, variant, flags, extra)


def final_accept(row, extra=EXTRA, tip=True):
    return S.final_accept(row, extra, tip)
'''

PATCH_RUNNER = r'''

# ======================================================================================
# Phase 2F Part 2 - the ONLY functional change to the copied 1U runner: the stack, which is the
# frozen 1W stack with lang='cz' and the Czech modules (p2/run/stack_2f.py).  The L3 prompt is
# P-FROZEN-1U, unchanged.  Run cap for Part 2: 600 counted calls.
# ======================================================================================
_P2 = os.path.dirname(HERE)
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import stack_2f as SW2F                                                        # noqa: E402


class _AG2F(object):
    @staticmethod
    def decide(sk, ann, wtags, answer, reference, variant='primary', flags=None):
        return SW2F.decide(sk, ann, wtags, answer, reference, 'primary',
                           tuple(AG4.ALL_FLAGS), ('rs_nom',))


AG_CFG['primary'] = (_AG2F, tuple(AG4.ALL_FLAGS))
CAP_1U = 600
_build_rows_1u = build_rows


def build_rows(recs, res, ag, planned, labels, hmap, failed):
    rows, _agg = _build_rows_1u(recs, res, ag, planned, labels, hmap, failed)
    agg = collections.Counter()
    for r in rows.values():
        r['stack_in'] = {'final_accept': r['final_accept'], 'final_layer': r['final_layer']}
        acc, lay = SW2F.final_accept(r, ('rs_nom',), True)
        r['final_accept'], r['final_layer'] = acc, lay
        agg['%s/%s' % ('accept' if acc else 'reject', r.get('judged') or 'unlabelled')] += 1
    return rows, dict(agg)

'''

PATCH_SCORE = r'''

# Phase 2F Part 2 - S7, as 1W declared it: determiner-difference items judged CORRECT rescored
# as WRONG.
_labellers_1u = labellers


def labellers(rows):
    out, moved = _labellers_1u(rows)
    det = {r['item_id'] for r in rows
           if 'determiner' in (r.get('tags') or []) and base_label(r) == 'correct'}
    out['S7_determiner_correct_as_wrong'] = (
        lambda r: 'wrong' if r['item_id'] in det else base_label(r), lambda r: True,
        'determiner-difference items (writer tag determiner) judged CORRECT rescored as WRONG')
    moved['S7_determiner_correct_as_wrong'] = sorted(det)
    return out, moved

'''

ANCHOR_OLD = """HERE = os.path.dirname(os.path.abspath(__file__))            # phase1u/run
P1U = os.path.dirname(HERE)                                  # phase1u
TOFF = os.path.dirname(P1U)                                  # translation-offline"""
ANCHOR_NEW = """HERE = os.path.dirname(os.path.abspath(__file__))            # phase2f/p2/run
P1U = os.path.dirname(HERE)                                  # phase2f/p2  (set/, data/, ledger)
TOFF = os.path.expanduser('~/Projects/and-again-content/translation-offline')   # 2F: anchored"""


def insert_before_main(src, patch):
    i = src.rindex("\nif __name__ == '__main__':")
    return src[:i] + patch + src[i:]


def setup_run():
    os.makedirs(RUN, exist_ok=True)
    open(os.path.join(RUN, 'stack_2f.py'), 'w', encoding='utf-8').write(STACK_2F)
    if os.path.exists(os.path.join(RUN, 'runner_1u.py')):
        return True
    for f in ('article_line_1u.py', 'selftest_1u_run.py', 'FROZEN_CONFIG_1U.json'):
        shutil.copy2(os.path.join(U, f), os.path.join(RUN, f))
    src = open(os.path.join(U, 'loader_1u.py'), encoding='utf-8').read()
    src = src.replace('SID_LO, SID_HI = 190001, 190100',
                      'SID_LO, SID_HI = %d, %d   # 2F Part 2: fresh Czech sids'
                      % (SID_BASE + 1, SID_BASE + 100), 1)
    open(os.path.join(RUN, 'loader_1u.py'), 'w', encoding='utf-8').write(src)
    src = open(os.path.join(U, 'runner_1u.py'), encoding='utf-8').read()
    assert ANCHOR_OLD in src, 'the runner header is not the expected one'
    src = src.replace(ANCHOR_OLD, ANCHOR_NEW, 1)
    a = "TASKA = os.path.join(P1U, 'taskA')"
    assert a in src
    src = src.replace(a, "TASKA = os.path.join(TOFF, 'phase1u', 'taskA')   # 2F: AG v4 home", 1)
    open(os.path.join(RUN, 'runner_1u.py'), 'w', encoding='utf-8').write(
        insert_before_main(src, PATCH_RUNNER))
    src = open(os.path.join(U, 'score_1u.py'), encoding='utf-8').read()
    if ANCHOR_OLD in src:
        src = src.replace(ANCHOR_OLD, ANCHOR_NEW, 1)
    else:
        for old, new in (("P1U = os.path.dirname(HERE)", "P1U = os.path.dirname(HERE)"),):
            src = src.replace(old, new, 1)
        if "TOFF = os.path.dirname(P1U)" in src:
            src = src.replace("TOFF = os.path.dirname(P1U)",
                              "TOFF = os.path.expanduser('~/Projects/and-again-content/"
                              "translation-offline')", 1)
    open(os.path.join(RUN, 'score_1u.py'), 'w', encoding='utf-8').write(
        insert_before_main(src, PATCH_SCORE))
    say('run side copied into %s (loader sid range, runner TOFF anchor + TASKA + stack + cap 600, '
        'scorer S7)' % RUN)
    return True


def freeze_and_run():
    runner = os.path.join(RUN, 'runner_1u.py')
    rc, out = sh(['python3', runner, '--preflight', '--data-dir', DATA], cwd=RUN)
    if rc != 0:
        R['preflight_stop'] = out[-2000:]
        return stop('STOP: preflight refused before the freeze (0 Gemini calls): %s'
                    % ' | '.join((out or '').strip().splitlines()[-3:]))
    mods = open(os.path.join(RUN, 'MODULES_1U.txt')).read().split()
    extra = ['translation-offline/phase2f/p2/run/score_1u.py',
             'translation-offline/phase2f/p2/run/stack_2f.py',
             'translation-offline/phase2f/p2/run/selftest_1u_run.py']
    with open(os.path.join(RUN, 'FREEZE_FILES'), 'w') as fh:
        fh.write('# Phase 2F Part 2 FREEZE_FILES - every .py the run imports, relative to the '
                 'repository root.\n')
        for f in sorted(set(mods + extra)):
            fh.write(f + '\n')
    fh_ = commit('Phase 2F Part 2: FREEZE - fresh Czech set judged, floors pass, stack 1W + cz')
    R['freeze_hash'] = fh_
    open(os.path.join(RUN, 'FREEZE_HASH'), 'w').write(fh_ + '\n')
    save_state()
    rc, out = sh(['python3', runner, '--preflight', '--data-dir', DATA], cwd=RUN)
    pf = jload(os.path.join(RUN, 'PREFLIGHT_1U.json'), {})
    R['preflight'] = {k: pf.get(k) for k in (
        'n_items', 'l2_firings', 'l3_eligible', 'ag_rejected_before_l3', 'reach_l3_planned_calls',
        'unique_requests', 'PLANNED_CALLS', 'counted_ledger_dev', 'cap', 'chk', 'ag')}
    R['preflight']['exit'] = rc
    save_state()
    if rc != 0:
        R['preflight_stop'] = out[-2000:]
        return stop('STOP: preflight (after the freeze) stopped, 0 Gemini calls')
    if not pf.get('l3_eligible'):
        return stop('STOP: L3-eligible 0, 0 Gemini calls')
    if (pf.get('ag') or {}).get('errors'):
        return stop('STOP: the stack raised AG errors on %s items, 0 Gemini calls'
                    % pf['ag']['errors'])
    planned = pf.get('PLANNED_CALLS') or pf.get('reach_l3_planned_calls') or 0
    if planned > CAP_RUN:
        return stop('STOP: planned %s calls > Part 2 cap %d, 0 calls' % (planned, CAP_RUN))
    with open(os.path.join(RUN, 'FREEZE_2F.txt'), 'w') as fh:
        fh.write(fh_ + '\n')
        for f in open(os.path.join(RUN, 'FREEZE_FILES')).read().split('\n'):
            if f and not f.startswith('#'):
                fh.write('%s %s\n' % (git('hash-object', f)[1].strip(), f))
    R['run_commit'] = commit('Phase 2F Part 2: RUN commit (FREEZE_HASH, preflight, manifest)')
    open(os.path.join(RUN, 'RUN_COMMIT'), 'w').write(R['run_commit'] + '\n')
    save_state()
    R['final_started'] = datetime.datetime.now().isoformat(timespec='seconds')
    save_state()
    rc, out = sh(['python3', runner, '--final', '--data-dir', DATA], cwd=RUN)
    R['final_exit'] = rc
    R['final_tail'] = (out or '').strip().splitlines()[-8:]
    done = os.path.exists(os.path.join(RUN, 'FINAL_RUN_DONE'))
    if not done and os.path.exists(os.path.join(RUN, 'calls.jsonl')) and rc != 3:
        R['notes'].append('the run CRASHED (exit %d); rows recomputed from the stored verdicts '
                          'with score_1u.py --recover (0 calls)' % rc)
        R['crashed'] = True
        sh(['python3', os.path.join(RUN, 'score_1u.py'), '--recover', '--data-dir', DATA], cwd=RUN)
    elif rc == 3:
        R['notes'].append('the run PAUSED (quota wall); not resumed by the driver')
    save_state()
    if os.path.exists(os.path.join(RUN, 'results_1u.json')):
        rc, _ = sh(['python3', os.path.join(RUN, 'score_1u.py'), '--data-dir', DATA], cwd=RUN)
        R['score_exit'] = rc
    return True


# ------------------------------------------------------------------------------- 9. report
SK_1W = {
    'coverage': '392/401 = 97.76 % [95.78, 98.97]', 'fa': '16/499 = 3.21 % [1.84, 5.15]',
    'agent_drop_fa all': '10/160 = 6.25 %', 'agent_drop_fa fronted': '7/64 = 10.94 %',
    'agent_drop_fa main': '0/48 = 0.00 %', 'agent_drop_fa misaligned': '3/48 = 6.25 %',
    'by_passive_coverage': '79/80 = 98.75 %', 'missing_article fa': '3/97 = 3.09 %',
    'skp_coverage': '70/72 = 97.22 %', 'time_frame_fa': '2/119 = 1.68 %',
    'AG primary': 'fired 144 / catches 141 / cost 3', 'L3': 'DIFF 311 SAME 252 TIP 37'}


def calls_stats():
    p = os.path.join(RUN, 'calls.jsonl')
    rows = []
    if os.path.exists(p):
        for line in open(p, encoding='utf-8'):
            try:
                rows.append(json.loads(line))
            except Exception:
                pass
    ok = [r for r in rows if r.get('http') == 200]
    failed = [r for r in ok if r.get('empty') or r.get('verdict') not in ('SAME', 'TIP', 'DIFF')]
    tin = sum((r.get('prompt_tokens') or 0) for r in ok)
    tout = sum((r.get('candidates_tokens') or 0) for r in ok)
    return {'lines': len(rows), 'counted_http200': len(ok),
            'uncounted_retries': sum(1 for r in rows if r.get('http') != 200),
            'uncounted_by_http': dict(collections.Counter(str(r.get('http')) for r in rows
                                                          if r.get('http') != 200)),
            'failed_empty_or_unparsable_200': len(failed),
            'failure_rate_pct': round(100.0 * len(failed) / len(ok), 2) if ok else None,
            'tokens_in': tin, 'tokens_out': tout,
            'spend_usd_list_price': round(tin * 0.10e-6 + tout * 0.40e-6, 5)}


def fk(d):
    try:
        if not d or not d.get('n'):
            return 'n = 0'
        return '%d/%d = %.2f %% [%.2f, %.2f]' % (d['k'], d['n'], d['pct'], d['ci'][0], d['ci'][1])
    except Exception:
        return json.dumps(d)


def tg(d):
    t = (d or {}).get('target') or {}
    return '' if not t else ' - target %s: POINT %s, INTERVAL %s' % (
        t.get('rule'), t.get('point'), t.get('interval'))


def flat(prefix, obj, out, depth=0):
    if isinstance(obj, dict) and 'k' in obj and 'n' in obj:
        out.append('- %s: %s' % (prefix, fk(obj)))
    elif isinstance(obj, dict) and depth < 4:
        for k in sorted(obj, key=str):
            flat('%s %s' % (prefix, k), obj[k], out, depth + 1)
    elif isinstance(obj, (int, float, str, bool)) or obj is None:
        out.append('- %s: %s' % (prefix, obj))


def write_result():
    cs = calls_stats()
    jdump({'part2_counted': cs['counted_http200'], 'part2_cap': CAP_RUN}, BUDGET)
    sc = jload(os.path.join(RUN, 'score_1u.json'))
    L = ['# Phase 2F Part 2 result: Czech coverage and false acceptance, fresh set %s'
         % ('OPENED ONCE' + (' (CRASH, recomputed from stored verdicts)' if R.get('crashed') else '')
            if R.get('final_started') else 'NOT OPENED'), '',
         '- Status: %s' % (R.get('status') or 'completed'),
         '- Method: Phase 1W §4, language changed to Czech; Slovak 1W figures are quoted beside '
         'every Czech one below.',
         '- Part 1: %s' % json.dumps(R.get('part1'))]
    L += ['- Note: %s' % n for n in R['notes']]
    L += ['', '## Deviations from 1W (declared before the set was opened)', '']
    L += ['%d. %s' % (i + 1, d) for i, d in enumerate(DEVIATIONS)]
    L += ['', '## Defects RECORDED, not fixed', '']
    L += ['- %s: %s' % (d['tag'], d['text']) for d in DEFECTS] or ['- none']
    L += ['', '## Headless sessions (bundled binary, --output-format json, --max-turns 12, opus)',
          '']
    for s in R['sessions']:
        L.append('- %s: exit %s, is_error %s, turns %s, input %s, cache_creation %s, cache_read %s,'
                 ' output %s, cost_usd %s, duration_ms %s'
                 % (s['session'], s['exit'], s['is_error'], s['num_turns'], s['input_tokens'],
                    s['cache_creation_input_tokens'], s['cache_read_input_tokens'],
                    s['output_tokens'], s['total_cost_usd'], s['duration_ms']))
    tot = sum((s.get('input_tokens') or 0) + (s.get('output_tokens') or 0)
              + (s.get('cache_creation_input_tokens') or 0)
              + (s.get('cache_read_input_tokens') or 0) for s in R['sessions'])
    L.append('- headless tokens spent in Part 2 (input + output + cache): %d' % tot)
    for name, blk in (('Set selection', 'selection'), ('Assemble', 'assemble'),
                      ('Packets', 'packets'), ('Label join', 'join'),
                      ('Floors on JUDGED counts', 'floors')):
        L += ['', '## %s' % name, '']
        for k, v in (R.get(blk) or {}).items():
            L.append('- %s %s: %s' % (blk, k, json.dumps(v, ensure_ascii=False)[:1200]))
    L += ['', '## Freeze / preflight / calls', '',
          '- FREEZE hash: %s' % R.get('freeze_hash'),
          '- RUN commit: %s' % R.get('run_commit'),
          '- final started: %s; runner exit %s; FINAL_RUN_DONE %s'
          % (R.get('final_started'), R.get('final_exit'),
             jload(os.path.join(RUN, 'FINAL_RUN_DONE')) or
             os.path.exists(os.path.join(RUN, 'FINAL_RUN_DONE')))]
    for k, v in (R.get('preflight') or {}).items():
        L.append('- preflight %s: %s' % (k, json.dumps(v)))
    if R.get('preflight_stop'):
        L.append('- preflight stop output: %s' % R['preflight_stop'].replace('\n', ' | ')[-1200:])
    L += ['- %s: %s' % (k, json.dumps(v)) for k, v in cs.items()]
    L += ['- Gemini budget: %s (cap %d)' % (cs['counted_http200'], CAP_RUN),
          '- access log (verbatim) below; call log: p2/run/calls.jsonl']
    if sc:
        L += ['', '## Headline and sensitivities S1-S7 (pooled / P1 odd sid / P2 even sid, exact '
              'Clopper-Pearson 95 %; coverage >= 90 %, FA < 5 %; never averaged)', '']
        for name, blk in sc.items():
            if not (name == 'headline' or re.match(r'S\d', name)) or not isinstance(blk, dict):
                continue
            for h in ('pooled', 'P1', 'P2'):
                for m in ('coverage', 'fa'):
                    d = (blk.get(h) or {}).get(m)
                    L.append('- %s %s %s: %s%s' % (name, h, m, fk(d), tg(d)))
            for m, pv in (blk.get('fisher_P1_vs_P2') or {}).items():
                L.append('- %s Fisher P1 vs P2 %s: p = %s' % (name, m, pv))
            if name != 'headline':
                L.append('- %s items moved: %s' % (name, blk.get('n_moved')))
        L += ['', '## Slovak 1W beside Czech', '']
        hp = ((sc.get('headline') or {}).get('pooled') or {})
        L += ['- coverage: Czech %s  |  Slovak 1W %s' % (fk(hp.get('coverage')), SK_1W['coverage']),
              '- false acceptance: Czech %s  |  Slovak 1W %s' % (fk(hp.get('fa')), SK_1W['fa'])]
        for k, v in SK_1W.items():
            if k not in ('coverage', 'fa'):
                L.append('- Slovak 1W %s: %s' % (k, v))
        L += ['', '## Every cell, one per line (headline labels)', '']
        flat('cell', sc.get('cells'), L)
        cells = sc.get('cells') or {}
        ad = (cells.get('agent_drop_fa') or {})
        emb_k = sum((ad.get(x) or {}).get('k', 0) for x in ('fronted', 'misaligned'))
        emb_n = sum((ad.get(x) or {}).get('n', 0) for x in ('fronted', 'misaligned'))
        L += ['- cell agent_drop_fa main (Czech): %s' % fk(ad.get('main')),
              '- cell agent_drop_fa embedded = fronted + misaligned (Czech): %s' % fk(kn(emb_k,
                                                                                        emb_n))]
        L += ['', '## AG block (primary and the offline shadows v4_full / guarded_union / v3 / v2)',
              '']
        flat('ag', sc.get('ag'), L)
        L += ['', '## Model block (L3 replies DIFF / SAME / TIP)', '']
        flat('model', sc.get('model'), L)
        L += ['', '## FA by judged type and by layer', '']
        flat('detail', (sc.get('detail') or {}).get('fa_by_judged_type'), L)
        flat('false_accepts_by_layer', (sc.get('detail') or {}).get('false_accepts_by_layer'), L)
        flat('false_rejections_by_layer',
             (sc.get('detail') or {}).get('false_rejections_by_layer'), L)
        L.append('- failed calls (detail): %s'
                 % json.dumps(((sc.get('detail') or {}).get('failed_calls')))[:600])
    L += ['', '## Access log (verbatim)', '', '```']
    alog = os.path.join(RUN, 'access_log.jsonl')
    if os.path.exists(alog):
        L += [x for x in open(alog, encoding='utf-8').read().splitlines()]
    else:
        L.append('(no access log: the data dir was never read by the runner)')
    L += ['```']
    open(os.path.join(HERE, 'PART2_RESULT.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    jdump({'status': R.get('status') or 'completed', 'part1': R.get('part1'),
           'selection': R.get('selection'), 'assemble': R.get('assemble'),
           'packets': R.get('packets'), 'join': R.get('join'), 'floors': R.get('floors'),
           'preflight': R.get('preflight'), 'freeze_hash': R.get('freeze_hash'),
           'run_commit': R.get('run_commit'), 'final_started': R.get('final_started'),
           'final_exit': R.get('final_exit'),
           'FINAL_RUN_DONE': os.path.exists(os.path.join(RUN, 'FINAL_RUN_DONE')),
           'calls': cs, 'headless_tokens': tot, 'sessions': R['sessions'],
           'deviations': DEVIATIONS, 'defects': DEFECTS, 'slovak_1w': SK_1W,
           'score': sc}, os.path.join(HERE, 'part2_result.json'))
    say('PART2_RESULT.md + part2_result.json written')
    try:
        commit('Phase 2F Part 2: result (%s)' % (R.get('status') or 'completed')[:60])
    except Exception as e:
        say('commit failed: %r' % e)


# ------------------------------------------------------------------------------- selftest
def selftest():
    """0 model calls, 0 sessions: synthetic writers + synthetic verdicts through assemble ->
    packets -> join -> floors, plus a real import and decision of the Czech stack."""
    ok, notes = True, []
    tmp = os.path.join(HERE, '_selftest')
    shutil.rmtree(tmp, ignore_errors=True)
    for d in (tmp, os.path.join(tmp, 'set'), os.path.join(tmp, 'set', 'judge'),
              os.path.join(tmp, 'set', 'writers'), os.path.join(tmp, 'data')):
        os.makedirs(d, exist_ok=True)
    global SET, DATA
    realset, realdata = SET, DATA
    SET, DATA = os.path.join(tmp, 'set'), os.path.join(tmp, 'data')
    try:
        sents = []
        for li, L in enumerate(LEVELS):
            for j in range(N_PER_LEVEL):
                num = 25 * li + j + 1
                sid = SID_BASE + num
                k = 'SKP' if j % 4 == 3 else ('FR', 'MC', 'MN')[j % 3]
                sents.append({'sid': sid, 'pid': '2F%03d' % num, 'slovak': 'Veta %d.' % sid,
                              'czech': 'Veta %d.' % sid, 'level': L, 'topic': 'topic %d' % sid,
                              'tags': {'half': 'P1' if num % 2 else 'P2', 'level': L, 'kind': k,
                                       'emb': k in ('FR', 'MC'), 'tf_gold': 'past',
                                       'writer_tags': {'kind': k, 'agent': 'otec'}}})
        jdump(sents, os.path.join(DATA, 'sentences.json'))
        for L in LEVELS:
            rows = []
            for s in [x for x in sents if x['level'] == L]:
                k = s['tags']['kind']
                dtag = {'FR': 'drop-fronted', 'MC': 'drop-misaligned', 'MN': 'drop-main'}.get(k)
                a = {'c1': ('plain', None), 'c2': ('determiner', None),
                     'c3': ('by-passive' if k != 'SKP' else 'skp-passive', None),
                     'c4': ('paraphrase', None),
                     'w1': (dtag or 'time-frame', 'M' if dtag else 'T'),
                     'w2': (dtag or 'time-frame', 'M' if dtag else 'T'),
                     'w3': ('time-frame', 'T'), 'w4': ('missing-article', 'S'),
                     'w5': ('wrong-word', 'W')}
                rows.append({'sid': s['sid'], 'answers': {
                    aid: {'en': 'answer %s %d' % (aid, s['sid']), 'type': t, 'tags': [tag]}
                    for aid, (tag, t) in a.items()}})
            jdump(rows, os.path.join(SET, 'writers', 'writer_%s.json' % L))
        assert assemble(), 'selftest: assemble refused'
        assert build_packets(), 'selftest: packets refused'
        key = jload(os.path.join(SET, 'judge', 'packet_key.json'), {})
        byq = collections.defaultdict(list)
        for qid, k in key.items():
            byq[k['part']].append((qid, k))
        items = {it['id']: it for it in jload(os.path.join(DATA, 'items.json'), [])}
        for pi, rows in byq.items():
            out = []
            for qid, k in sorted(rows, key=lambda x: x[1]['position']):
                it = items[k['item_id']]
                w = it['kind'] == 'W'
                flip = (k['position'] % 37 == 0)          # the judge must be able to disagree with
                jg = ('correct' if w else 'wrong') if flip else ('wrong' if w else 'correct')
                out.append({'jid': qid, 'judged': jg,     # the writer, or S1 tests nothing
                            'type': ((it['type_writer'] or 'W') if jg == 'wrong' else None),
                            'confidence': 4, 'borderline': (k['position'] % 17 == 0),
                            'dropped': ''})
            jdump(out, os.path.join(SET, 'judge', 'verdicts_part%d.json' % pi))
        assert join_labels(), 'selftest: join refused'
        assert floors(), 'selftest: floors refused'
        fl = jload(os.path.join(SET, 'floors_1u.json'), {})
        assert fl.get('all_pass'), 'selftest: floors did not pass on the perfect synthetic set'
        notes.append('synthetic end-to-end OK: %s' % json.dumps(
            {k: fl[k]['n'] for k in MINS}))
        # the gates must be able to FAIL: flip every agent drop to correct
        lab = jload(os.path.join(DATA, 'labels.json'), {})
        for iid, v in lab.items():
            if any(t in DROP_TAGS for t in items[iid]['tags']):
                v['judged'], v['type'] = 'correct', None
        jdump(lab, os.path.join(DATA, 'labels.json'))
        if floors():
            ok = False
            notes.append('SELFTEST FAILURE: the floor gate passed a set with 0 agent drops wrong')
        else:
            notes.append('floor gate refuses a set with 0 agent drops judged wrong: OK')
        R['status'] = None
    except AssertionError as e:
        ok = False
        notes.append('SELFTEST FAILURE: %s' % e)
    except Exception as e:
        import traceback
        ok = False
        notes.append('SELFTEST EXCEPTION: %s' % traceback.format_exc()[-1500:])
    finally:
        SET, DATA = realset, realdata
        shutil.rmtree(tmp, ignore_errors=True)
    # the Czech stack must import and decide
    try:
        setup_run()
        rc, out = sh(['python3', '-c',
                      'import sys; sys.path.insert(0, %r); import stack_2f as S;'
                      'v = S.decide("Tenhle strop v loznici byval jeho oblibenou televizi.",'
                      ' {"hygienised": {"v": ["This ceiling used to be his favourite TV."],'
                      ' "lk": ["used to be"], "alt": {}}}, {"agent": "strop"},'
                      ' "This ceiling used to be his favourite TV.",'
                      ' "This ceiling used to be his favourite TV.");'
                      'print("STACK_OK", type(v).__name__)' % RUN], cwd=RUN)
        if rc != 0 or 'STACK_OK' not in out:
            ok = False
            notes.append('SELFTEST FAILURE: the Czech stack did not import/decide: %s'
                         % out.strip().splitlines()[-4:])
        else:
            notes.append('Czech stack imports and decides: OK')
        rc, out = sh(['python3', '-c', 'import py_compile,sys;'
                      'py_compile.compile(%r, doraise=True); print("RUNNER_COMPILES")'
                      % os.path.join(RUN, 'runner_1u.py')], cwd=RUN)
        notes.append('runner compiles: %s' % ('OK' if 'RUNNER_COMPILES' in out else out[-300:]))
        if 'RUNNER_COMPILES' not in out:
            ok = False
    except Exception as e:
        ok = False
        notes.append('SELFTEST EXCEPTION (stack): %r' % e)
    try:
        s = lk_prompt_sha()
        notes.append('lk prompt sha16 %s (%s)' % (s, 'OK' if s == LK_SHA else 'DRIFTED'))
        ok = ok and s == LK_SHA
    except Exception as e:
        ok = False
        notes.append('SELFTEST FAILURE: lk prompt sha could not be computed: %r' % e)
    R['status'] = None          # a negative sub-test must not leak a status into the real run
    jdump({'ok': ok, 'notes': notes}, os.path.join(HERE, 'SELFTEST_2FP2.json'))
    for n in notes:
        say('selftest: %s' % n)
    say('SELFTEST %s' % ('PASS' if ok else 'FAIL'))
    return ok


# ------------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--no-wait', action='store_true')
    a = ap.parse_args()
    for d in (SET, RUN, DATA, SESS, os.path.join(SET, 'judge'), os.path.join(SET, 'writers'),
              os.path.join(SET, 'briefs')):
        os.makedirs(d, exist_ok=True)
    if a.selftest:
        sys.exit(0 if selftest() else 2)
    old = jload(STATE)
    if old:
        R.update(old)
        R['status'] = None
    if not os.path.exists(BUDGET):
        jdump({'part2_counted': 0, 'part2_cap': CAP_RUN}, BUDGET)
    try:
        if not selftest():
            R['status'] = 'STOP: the 0-call selftest failed; the set was NOT opened, 0 Gemini calls'
            say(R['status'])
        elif a.no_wait or wait_part1():
            stages = [('selection', build_selection), ('briefs', write_briefs),
                      ('writers', lambda: writers() or stop(
                          'STOP: the writers did not deliver valid files; 0 Gemini calls')),
                      ('assemble', assemble), ('packets', build_packets),
                      ('judge', lambda: judge() or stop(
                          'STOP: the judge did not deliver all verdict files; 0 Gemini calls')),
                      ('join', join_labels), ('floors', floors), ('setup_run', setup_run),
                      ('freeze_and_run', freeze_and_run)]
            for name, fn in stages:
                R['stage'] = name
                save_state()
                say('=== stage %s ===' % name)
                if not fn():
                    break
                commit('Phase 2F Part 2: stage %s' % name)
    except Exception:
        import traceback
        R['status'] = 'DRIVER EXCEPTION at stage %s' % R.get('stage')
        say(traceback.format_exc())
    save_state()
    write_result()


if __name__ == '__main__':
    main()
