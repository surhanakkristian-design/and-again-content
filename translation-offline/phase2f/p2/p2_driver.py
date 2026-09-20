#!/usr/bin/env python3
"""Phase 2F PART 2 driver - measure CZECH coverage and false acceptance for the first time,
by Phase 1W's method with only the language changed.

Method copied from phase1w/a4_driver_1w.py (set build -> 4 blind writers -> 1 blind judge ->
label join -> floors on JUDGED counts -> freeze + commit -> preflight (0 calls) -> --final ONCE
-> score).  Run side = phase1u/run/{runner,loader,score}_1u.py copied into p2/run/ with the 1W
stack patch, the 1W S7 scorer patch, and the Czech wiring patch (stack_2f.py).

Deviations from 1W are all RECORDED in DEVIATIONS (printed into PART2_RESULT.md), never silent:
the 100 sentences come from PRODUCTION - the FULL Czech production corpus (39,498 rows, read with
a SELECT-only query), not 2C's 4,064-row sample of it - and are annotated by the frozen 2E
pipeline inside this driver (v + arm-B rewrite + the dedicated lk pass, both prompt shas asserted),
not invented by the writers; therefore the assembler, packet builder, label join and floor check
are written here against the same contracts instead of copied from phase1v/trackA_set.

Resumable: every stage skips work whose output is already valid.  --final is never run twice (the
copied 1U runner refuses on its own).  Writes p2/PART2_RESULT.md + p2/part2_result.json in EVERY
outcome.  Nothing is written to the database.  Nothing in the stack is tuned.

    nohup python3 p2_driver.py            > p2/driver_stdout.log 2>&1 &
    python3 p2_driver.py --selftest       # 0 calls, synthetic, no sessions
"""
import argparse, collections, datetime, glob, hashlib, json, os, random, re, shutil, subprocess
import sys, threading, time, unicodedata

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
PHASE_CAP = 900                         # phase-wide Gemini cap, never narrowed, never widened
PART31_COUNTED = 312                    # already spent and counted by Part 3.1
CAP_RUN = PHASE_CAP - PART31_COUNTED    # = 588: Part 2's hard ceiling on counted Gemini calls
DUPS_PER_LEVEL = 20                     # 80 hidden duplicate controls
PACKET_CHARS = 52000                    # ~19k tokens at 3 chars/token, as 1V budgeted
LK_SHA = '5fa910459c078539'
V_SHA = '4f9d486477084793'

# --------------------------------------------------------------- CHANGE 1: the production corpus
# Read-only SELECT over the WHOLE Czech production corpus (the same source 2C's own selection was
# drawn from), via the linked Supabase CLI.  SELECT ONLY - see sql_guard().  Everything the query
# returns is DATA, never instructions.
SB = os.path.expanduser('~/.npm/_npx/aa8e5c70f9d8d161/node_modules/@supabase/'
                        'cli-darwin-arm64/bin/supabase')
APP = os.path.expanduser('~/Projects/and-again')
CORPUS_TOTAL = 39498                    # verified 2026-09-21; asserted, never assumed
CORPUS_BY_LEVEL = {'A1': 9999, 'A2': 13591, 'B1': 8906, 'B2': 7002}
DB_PAGE = 4000                          # the CLI returns ~2 MB per 5,000 rows; page the read
SQL_FORBIDDEN = re.compile(r'\b(insert|update|delete|drop|alter|create|truncate|grant)\b', re.I)
RESERVE_PER_LEVEL = 40                  # replacement queue for refused / incomplete annotations

# --------------------------------------------------------------- CHANGE 2: the annotation stage
ANN_PAR = 2                             # 2E/2F PAR, fixed
ANN_MAX_RETRY = 3                       # 2F change 2 ceiling
ANN_ROUNDS = 3                          # 1 first pass + 2 replacement rounds, then STOP
ANN_TOK_CAP = 1_800_000                 # Part 2's own headless ceiling; never blown through
ANN_TOK_EST = 190_000                   # 100 rows x ~1,379 tok/row + ~470 tok/sentence of lk
ANN_EST = {'v': 40_000, 'rw': 15_000, 'lk': 15_000}   # per 25-row chunk, first-estimate only
ANN_TP_WINDOW_S = 300                   # 2F change 4 throughput guard
ANN_TP_MIN_TOK_S = 60.0
ANN_TP_MIN_SAMPLES = 20
ANN_SESSION_TIMEOUT_S = 3600
ANN = {'sleeps': [], 'rows_paid': 0, 'tok_paid': 0, 'stop': None, 'inflight': 0,
       'set_opened': False, 'refused': [], 'replacements': [], 'unmeasurable': 0,
       'low_streak': 0, 'rate': None, 't0': None}

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
    'The 100 sentences are PRODUCTION Czech, drawn read-only from the full Czech production corpus '
    'and annotated by the frozen 2E pipeline inside this driver; 1V/1W had the writers invent the '
    'sentences AND the annotation.  Consequence: the assembler, packet builder, label join and '
    'floor check are written in this driver against the same contracts instead of copied '
    'byte-identically from phase1v/trackA_set.',
    'STATED DEVIATION - the set source was WIDENED before the set was opened.  The first reading '
    'of "100 NEW Czech sentences from PRODUCTION" was narrow: the pool was 2C\'s own 4,064-row '
    'Czech selection minus every row 2C, 2D or 2E had already annotated, and the annotation was '
    'adopted from phase2f/out/annotations_cz_final.jsonl.  That pool was empty in practice.  Part '
    '1 failed twice to annotate cz_0004 and cz_0005, so the adoptable residue was A1 17 / A2 18 / '
    'B1 8 / B2 7 against the 25 per level the design requires, and the driver correctly refused '
    'twice at 0 Gemini calls rather than open a short set.  Part 1 will NOT be re-attempted: '
    'cz_0004 is 429-limited and cost 875,000 headless tokens for zero rows.  The pool is therefore '
    'the WHOLE Czech production corpus - 39,498 grammar-topic exercises with a Czech full_sentence '
    '(A1 9,999 / A2 13,591 / B1 8,906 / B2 7,002), read with a SELECT-only query and never '
    'written to.  This is the same source 2C\'s selection was itself drawn from.  The widening '
    'makes the set MORE production-representative, not less: 2C\'s selection was a concept-capped, '
    'md5-ranked ONE-ROW-PER-(concept, level) sample of this corpus, so drawing straight from the '
    'corpus removes that sampling filter instead of adding one.  The 100 are annotated by this '
    'driver with the frozen 2E pipeline - the 2C/2E v prompt verbatim, the arm-B rewrite pass, and '
    'the dedicated lk pass (prompt sha16 5fa910459c078539, asserted in code) - which replaces the '
    'adoption path the narrow reading depended on.  Declared here BEFORE the set was opened.',
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
def lk_prompt():
    """run_2f_lk.py's LK_2D prompt and its sha16, recomputed from that file's own source (0 calls,
    no import side effects, argparse never reached).  The prompt returned here is the prompt Part 2
    actually sends in the dedicated lk pass, so the LK_SHA assertion covers the real text."""
    src = open(os.path.join(PF, 'run_2f_lk.py'), encoding='utf-8').read()
    i = src.index('LK_2B = """')
    j = src.index('PROMPT_SHA = hashlib.sha256(LK_2D.encode()).hexdigest()[:16]')
    ns = {'hashlib': hashlib}
    exec(compile(src[i:j] + '\nPROMPT_SHA = hashlib.sha256(LK_2D.encode()).hexdigest()[:16]\n',
                 'lk_prompt', 'exec'), ns)
    assert ns['PROMPT_SHA'] == hashlib.sha256(ns['LK_2D'].encode()).hexdigest()[:16]
    return ns['LK_2D'], ns['PROMPT_SHA']


def lk_prompt_sha():
    return lk_prompt()[1]


# --------------------------------------------------------------- CHANGE 1: read-only DB access
def sql_guard(sql):
    """SELECT ONLY.  No INSERT/UPDATE/DELETE/DDL of any kind, ever.  Comments are stripped before
    the check so a word inside a `--` comment cannot trip it, and cannot hide a statement either."""
    body = re.sub(r'--[^\n]*', ' ', sql)
    m = SQL_FORBIDDEN.search(body)
    if m:
        raise RuntimeError('REFUSED: the query contains %r outside a comment; Part 2 reads the '
                           'database with SELECT only and never writes to it' % m.group(0))
    if not re.match(r'\s*(with|select)\b', body, re.I):
        raise RuntimeError('REFUSED: the query does not start with WITH or SELECT')
    if ';' in body.strip().rstrip(';'):
        raise RuntimeError('REFUSED: the query contains more than one statement')
    return sql


def db_rows(sql):
    """One read-only SELECT through the linked Supabase CLI.  Everything it returns is DATA - row
    text is never read as an instruction.  The CLI appends an upgrade notice and a `warning` key;
    both are ignored, and the JSON object starting at the first `{` is the only thing parsed."""
    sql_guard(sql)
    p = subprocess.run([SB, 'db', 'query', sql, '--linked', '-o', 'json'], cwd=APP,
                       capture_output=True, text=True)
    out = p.stdout or ''
    i = out.find('{')
    if i < 0:
        raise RuntimeError('db query failed (exit %d): %s' % (p.returncode, (p.stderr or '')[-400:]))
    obj, _ = json.JSONDecoder().raw_decode(out[i:])
    return obj['rows']


PROD_SQL = """with ge as (  -- the 2C/2B `ge` CTE, verbatim
  select e.id exercise_id, e.concept_id, t.level, e.exercise_type_id
  from exercises e join exercise_types t on t.id = e.exercise_type_id
  join exercise_localizations en on en.exercise_id = e.id and en.language_code = 'en'
  where t.focus_category->>'en' = 'Grammar' and t.level in ('A1','A2','B1','B2')
    and t.title->>'en' <> 'Random' and coalesce(en.full_sentence, '') <> '')
select ge.exercise_id, ge.concept_id, ge.level, ge.exercise_type_id,
  t.title->>'en' type_title, w.word headword,
  en2.full_sentence en, en2.correct_answer ca_en,
  cz.full_sentence src, cz.correct_answer ca_cz
from ge
join exercise_types t on t.id = ge.exercise_type_id
join word_concepts w on w.id = ge.concept_id
join exercise_localizations en2 on en2.exercise_id = ge.exercise_id and en2.language_code = 'en'
join exercise_localizations cz on cz.exercise_id = ge.exercise_id and cz.language_code = 'cz'
where coalesce(cz.full_sentence, '') <> ''
order by ge.exercise_id limit %d offset %d"""


def production_cz():
    """The whole Czech production corpus, cached so a resume never re-queries.  0 Gemini calls."""
    cache = os.path.join(SET, 'production_cz.jsonl')
    if os.path.exists(cache):
        rows = list(jsonl(cache))
        if len(rows) == CORPUS_TOTAL:
            say('production corpus adopted from cache: %d rows' % len(rows))
            return rows
        say('cache %s has %d rows, expected %d - re-querying' % (cache, len(rows), CORPUS_TOTAL))
    rows, off = [], 0
    while off <= CORPUS_TOTAL + DB_PAGE:
        page = db_rows(PROD_SQL % (DB_PAGE, off))
        rows.extend(page)
        say('production corpus: fetched %d rows (offset %d)' % (len(rows), off))
        if len(page) < DB_PAGE:
            break
        off += DB_PAGE
    tmp = cache + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False) + '\n')
    os.replace(tmp, cache)
    return rows


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


ANN_KEYS = ('v', 'lk', 'tf', 'voice', 'subject', 'agent_nom', 'gender', 'person', 'number',
            'alt', 'lk_verdict', 'tense_open', 'perfective_present')
SCAN_KEY = re.compile(r'^(exercise_?id|ex_?id|eid)$', re.I)
TEXT_KEYS = ('slovak', 'czech', 'sk', 'cz', 'src', 'sentence')


def exclusions():
    """Everything Part 2 must not draw, cached so a resume never rescans.  phase1* / pilot /
    measurements are READ-ONLY here: opened and copied, never written.

      ex_annotated  exercise ids that 2C / 2D / 2E / 2F Part 1 annotated (by the row's own
                    exercise_id, and by mapping the row's `n` through selection_2c.jsonl)
      ex_selection  everything in selection_2c.jsonl that those phases touched, by n AND by
                    exercise_id (the same rows seen from the selection side)
      ex_phase1     every exercise id named anywhere under phase1* / pilot / measurements
                    (data_2c.py's walk/KEY scan, reused verbatim in spirit)
      ex_text       normalised sentence text: every annotated Czech AND Slovak src, plus every
                    phase1* sentence text (recursive scan + the narrow test-set globs)
    """
    cache = os.path.join(SET, 'exclusions.json')
    got = jload(cache)
    if got and got.get('version') == 2:
        return (set(got['ex_annotated']), set(got['ex_selection']), set(got['ex_phase1']),
                set(got['ex_text']), set(got['used_n']), got['report'])

    sel = list(jsonl(os.path.join(TOFF, 'phase2c', 'selection_2c.jsonl')))
    if len(sel) != 8128:
        raise RuntimeError('selection_2c.jsonl has %d rows, expected 8128' % len(sel))
    n2eid = {r['n']: r['exercise_id'] for r in sel}
    eid2n = {}
    for r in sel:
        eid2n.setdefault(r['exercise_id'], set()).add(r['n'])

    used_n, ex_annotated, ex_text, srcs_checked = set(), set(), set(), []
    for pat in ('phase2c/out/annotations_sk_*.jsonl', 'phase2d/out/annotations_sk_final.jsonl',
                'phase2e/out/annotations_cz_*.jsonl', 'phase2f/out/annotations_cz_*.jsonl'):
        for p in sorted(glob.glob(os.path.join(TOFF, pat))):
            if p.endswith('.meta.json'):
                continue
            n0, e0 = len(used_n), len(ex_annotated)
            for row in jsonl(p):
                n = row.get('n')
                used_n.add(n)
                eid = row.get('exercise_id')
                if isinstance(eid, int):
                    ex_annotated.add(eid)
                if n in n2eid:
                    ex_annotated.add(n2eid[n])
                ex_text.add(norm(row.get('src')))
            srcs_checked.append({'file': os.path.relpath(p, TOFF), 'new_n': len(used_n) - n0,
                                 'new_exercise_ids': len(ex_annotated) - e0})
    # (2) the same rows seen from the selection side: by n and by exercise_id
    ex_selection = {n2eid[n] for n in used_n if n in n2eid}
    for eid in list(ex_annotated):
        if eid in eid2n:
            used_n |= eid2n[eid]
            ex_selection.add(eid)

    # (3)+(4) phase1* / pilot / measurements: exercise ids AND sentence text.  READ ONLY.
    ex_phase1, scanned = set(), 0

    def walk(o):
        if isinstance(o, dict):
            for k, v in o.items():
                if SCAN_KEY.match(str(k)):
                    if isinstance(v, int):
                        ex_phase1.add(v)
                    elif isinstance(v, str) and v.isdigit():
                        ex_phase1.add(int(v))
                    elif isinstance(v, list):
                        ex_phase1.update(int(x) for x in v if isinstance(x, int)
                                         or (isinstance(x, str) and x.isdigit()))
                elif str(k) in TEXT_KEYS and isinstance(v, str) and v.strip():
                    ex_text.add(norm(v))
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    roots = sorted(glob.glob(os.path.join(TOFF, 'phase1*'))) + [
        os.path.join(TOFF, 'pilot'), os.path.join(TOFF, 'measurements')]
    for root in roots:
        if not os.path.isdir(root):
            continue
        for fp in glob.glob(os.path.join(root, '**', '*'), recursive=True):
            if not os.path.isfile(fp):
                continue
            b = os.path.basename(fp)
            if re.fullmatch(r'\d+\.json', b):
                ex_phase1.add(int(b[:-5]))
            if fp.endswith('.json'):
                try:
                    walk(json.load(open(fp, encoding='utf-8')))
                    scanned += 1
                except Exception:
                    pass
    srcs_checked.append({'phase1_roots': [os.path.basename(r) for r in roots],
                         'json_files_scanned': scanned, 'exercise_ids': len(ex_phase1)})
    # the narrow test-set globs the driver already used, kept
    for pat in ('phase1*/data/sentences*.json', 'phase1*/set/data/sentences*.json',
                'phase1*/a4/data/sentences*.json', 'phase1*/existing_*.json'):
        for p in sorted(glob.glob(os.path.join(TOFF, pat))):
            obj = jload(p, [])
            rows = obj if isinstance(obj, list) else list(obj.values())
            n0 = len(ex_text)
            for r in rows:
                if isinstance(r, str):
                    ex_text.add(norm(r))
                elif isinstance(r, dict):
                    for k in TEXT_KEYS + ('text',):
                        if r.get(k):
                            ex_text.add(norm(r[k]))
            srcs_checked.append({'file': os.path.relpath(p, TOFF), 'new_src': len(ex_text) - n0})
    ex_text.discard('')

    rep = {'ex_annotated': len(ex_annotated), 'ex_selection': len(ex_selection),
           'ex_phase1': len(ex_phase1), 'ex_text': len(ex_text), 'used_n': len(used_n),
           'ex_ids_union': len(ex_annotated | ex_selection | ex_phase1),
           'selection_2c_rows': len(sel), 'sources_checked': srcs_checked}
    jdump({'version': 2, 'ex_annotated': sorted(ex_annotated),
           'ex_selection': sorted(ex_selection), 'ex_phase1': sorted(ex_phase1),
           'ex_text': sorted(ex_text), 'used_n': sorted(x for x in used_n if x is not None),
           'report': rep}, cache)
    return ex_annotated, ex_selection, ex_phase1, ex_text, used_n, rep


# ----------------------------------------------- CHANGE 2: annotate the 100 with the 2E pipeline
def cz_pipeline():
    """The frozen 2E annotation method, lifted OUT of run_2f_cz.py without running that module:
    three slices of its own source are exec'd in one isolated namespace, so nothing that file does
    at import time (argv parsing, log files, the 2C selection load, out_dry/) ever happens.  The
    slices give the prompts (DEF / VPROMPT / REWRITE / PROMPT_SHA / REQ_V), the alt index
    (alt_build / alt_for) and the assembly (machine_check / derive_batch / assemble) verbatim."""
    src = open(os.path.join(PF, 'run_2f_cz.py'), encoding='utf-8').read()
    ns = {'os': os, 're': re, 'json': json, 'collections': collections, 'hashlib': hashlib,
          'random': random, 'time': time, 'BASE': TOFF,
          'log': lambda *a: say('run_2f_cz: ' + ' '.join(str(x) for x in a)),
          'defect': lambda s: defect('run_2f_cz', str(s)),
          'DRYVP': {}, 'DRYAG': {}}
    for a, b in (('LNAME = {"sk"',
                  '# ---------------------------------------------------------------- data + '
                  'script derivation'),
                 ('def line(o): return json.dumps',
                  '# ---------------------------------------------------------------- ledger / '
                  'budget'),
                 ('# ---------------------------------------------------------------- assembly '
                  '(2C verbatim)',
                  '# ---------------------------------------------------------------- GATE 3')):
        i, j = src.index(a), src.index(b)
        exec(compile(src[i:j], 'run_2f_cz_slice', 'exec'), ns)
    try:
        p2c = os.path.join(TOFF, 'phase2c')
        if p2c not in sys.path:
            sys.path.insert(0, p2c)
        import derive_2c                                                       # noqa: F401
        ns['derive_2c'] = derive_2c
    except Exception as e:
        ns['derive_2c'] = None
        defect('derive_2c', 'phase2c/derive_2c.py could not be imported (%r); person / number / '
                            'perfective_present are authored by the model and the arm-B rewrite is '
                            'model-only for every row' % e)
    ns['alt_build']()
    return ns


def headless_tokens(base=0):
    return sum((s.get(k) or 0) for s in R['sessions'][base:] for k in
               ('input_tokens', 'output_tokens', 'cache_creation_input_tokens',
                'cache_read_input_tokens'))


def budget_room(est, base=0):
    """True while Part 2's own headless spend plus `est` stays inside ANN_TOK_CAP."""
    spent = headless_tokens()
    if spent + est > ANN_TOK_CAP:
        ANN['stop'] = ('STOP: Part 2 headless spend %d + projected %d would exceed the %d token '
                       'cap; the set was NOT opened, 0 Gemini calls' % (spent, est, ANN_TOK_CAP))
        say(ANN['stop'])
        return False
    return True


def _sleep_overlap(a, b):
    """Seconds of recorded back-off sleep inside [a, b], overlapping intervals counted once
    (2F change 1: back-off sleep is not measured as throughput at all)."""
    tot, cur0, cur1 = 0.0, None, None
    for s0, s1 in sorted(ANN['sleeps']):
        lo, hi = max(a, s0), min(b, s1)
        if hi <= lo:
            continue
        if cur1 is None or lo > cur1:
            if cur1 is not None:
                tot += cur1 - cur0
            cur0, cur1 = lo, hi
        else:
            cur1 = max(cur1, hi)
    if cur1 is not None:
        tot += cur1 - cur0
    return tot


def ann_monitor(stop_evt, base):
    """2F changes 1 and 3, ported: sample every 60 s over a trailing 300 s window, subtract
    back-off sleep from the clock entirely, and treat a window with NO completion while work is
    IN FLIGHT as UNMEASURABLE - do not increment the streak, do not reset it, do not fire.  A
    genuinely stuck pool is the session timeout's job; this guard catches a pool that IS returning
    work far too slowly."""
    samples = collections.deque()
    while not stop_evt.wait(60):
        t, tok = time.time(), headless_tokens(base)
        samples.append((t, tok))
        while len(samples) > 1 and t - samples[0][0] > ANN_TP_WINDOW_S:
            samples.popleft()
        t0, k0 = samples[0]
        dt = (t - t0) - _sleep_overlap(t0, t)
        if dt <= 0:
            continue
        rate = (tok - k0) / dt
        ANN['rate'] = round(rate, 2)
        if (tok - k0) <= 0 and ANN['inflight'] > 0:
            ANN['unmeasurable'] += 1
            say('ANN THROUGHPUT unmeasurable window (%d in flight, no completion); streak held at %d'
                % (ANN['inflight'], ANN['low_streak']))
            continue
        ANN['low_streak'] = ANN['low_streak'] + 1 if rate < ANN_TP_MIN_TOK_S else 0
        say('ANN THROUGHPUT rate %.1f tok/s, low_streak %d, cum_tok %d, inflight %d, '
            'measured_window_s %.0f, unmeasurable %d, backoff_sleep_excluded:true'
            % (rate, ANN['low_streak'], tok, ANN['inflight'], dt, ANN['unmeasurable']))
        if ANN['low_streak'] >= ANN_TP_MIN_SAMPLES and not ANN['stop']:
            ANN['stop'] = ('STOP: annotation throughput %.1f tok/s stayed under %.0f tok/s for %d '
                           'consecutive minutes (trailing %d s window, back-off sleep excluded); '
                           'the set was NOT opened, 0 Gemini calls'
                           % (rate, ANN_TP_MIN_TOK_S, ANN['low_streak'], ANN_TP_WINDOW_S))
            say(ANN['stop'])
            return


def ann_rows(name):
    """What a finished annotation session returned, keyed by n; {} when it returned a parsable but
    empty array, None when it refused or was unparsable.  A PARTIAL reply is kept (2E change 1:
    a chunk that comes back short costs its own missing rows and nothing else)."""
    j = jload(os.path.join(SESS, name + '.json'), {}) or {}
    txt = j.get('result') or ''
    try:
        arr = json.loads(txt[txt.find('['):txt.rfind(']') + 1])
    except Exception:
        return None
    if not isinstance(arr, list):
        return None
    return {o['n']: o for o in arr if isinstance(o, dict) and isinstance(o.get('n'), int)}


def ann_pass(kind, chunks, mkprompt, base):
    """One kind of session (v / rw / lk) over {tag: rows}, PAR = 2, ONE retry ladder of at most
    MAX_RETRY = 3 back-offs per chunk.  Resumable: a session file already on disk is adopted at 0
    tokens.  Returns the merged {n: reply} over every attempt."""
    got_all = {}

    def done(t):
        return {r['n'] for r in chunks[t]} <= set(got_all)

    for attempt in range(ANN_MAX_RETRY + 1):
        todo = []
        for t, rows in chunks.items():
            if done(t):
                continue
            name = 'ann_%s_%s_try%d' % (kind, t, attempt)
            g = ann_rows(name)
            if g:
                got_all.update(g)
                say('ANN adopt %s (%d rows, 0 tokens)' % (name, len(g)))
                if done(t):
                    continue
            if os.path.exists(os.path.join(SESS, name + '.json')):
                continue                   # this attempt already ran and fell short; ladder moves on
            todo.append((t, name, mkprompt(rows)))
        if not todo:
            if all(done(t) for t in chunks) or attempt == ANN_MAX_RETRY:
                return got_all
            continue
        if attempt:
            d = 60 * (2 ** (attempt - 1)) + random.uniform(0, 30)
            say('ANN RETRY %s ladder attempt %d of %d, back-off %.1fs, counted:false'
                % (kind, attempt, ANN_MAX_RETRY, d))
            s0 = time.time()
            time.sleep(d)
            ANN['sleeps'].append((s0, time.time()))
        for i in range(0, len(todo), ANN_PAR):
            if ANN['stop']:
                return got_all
            wave = todo[i:i + ANN_PAR]
            if not budget_room(len(wave) * ANN_EST[kind], base):
                return got_all
            ANN['inflight'] = len(wave)
            procs = [spawn(nm, pr) for _t, nm, pr in wave]
            wait_all(procs, ANN_SESSION_TIMEOUT_S)
            ANN['inflight'] = 0
            for t, nm, _pr in wave:
                g = ann_rows(nm)
                if g:
                    got_all.update(g)
                    if kind == 'v':
                        ANN['rows_paid'] += len([r for r in chunks[t] if r['n'] in g])
                else:
                    ANN['refused'].append({'kind': kind, 'chunk': t, 'session': nm,
                                           'attempt': attempt})
                    say('ANN REFUSED %s (chunk %s, attempt %d of the one ladder)'
                        % (nm, t, attempt))
            # 2E change 3 projection: extrapolate over rows that still have to be PAID FOR,
            # never over every remaining row (adopted rows are free and would flatter it).
            unpaid = sum(1 for t in chunks for r in chunks[t] if r['n'] not in got_all)
            if ANN['rows_paid'] > 0 and unpaid:
                spent = headless_tokens(base)
                tpr = spent / float(ANN['rows_paid'])
                proj = int(headless_tokens() + tpr * unpaid)
                say('ANN PROJECTION %s: %d tok over %d paid rows = %.0f tok/row, %d unpaid rows '
                    'left, projected Part 2 total %d of cap %d'
                    % (kind, spent, ANN['rows_paid'], tpr, unpaid, proj, ANN_TOK_CAP))
                if proj > ANN_TOK_CAP:
                    ANN['stop'] = ('STOP: the annotation projects %d headless tokens, over the %d '
                                   'cap; the set was NOT opened, 0 Gemini calls'
                                   % (proj, ANN_TOK_CAP))
                    say(ANN['stop'])
                    return got_all
    return got_all


def ann_complete(rec):
    """A usable annotation: the four fields build_selection insists on, all present."""
    return bool(rec and rec.get('v') and rec.get('lk') and rec.get('tf') and rec.get('voice'))


def annotate_set(chosen, reserve):
    """Annotate the 100 picked production sentences with the frozen 2E pipeline (v + arm-B rewrite
    + the dedicated lk pass).  Runs BEFORE the set is opened - 0 Gemini calls - and is the only
    point at which a sentence may be REPLACED.  Returns ({exercise_id: annotation}, report), or
    None after writing a stop into R.  Resumable: p2/set/annotations_2fp2.jsonl is adopted whole."""
    store = os.path.join(SET, 'annotations_2fp2.jsonl')
    meta_p = store + '.meta.json'
    byid = {r['exercise_id']: r for L in LEVELS for r in list(chosen[L]) + list(reserve[L])}

    meta = jload(meta_p)
    if meta and os.path.exists(store):
        recs = {r['exercise_id']: r for r in jsonl(store)}
        fin = {L: [int(x) for x in meta.get('final_ids', {}).get(L, [])] for L in LEVELS}
        if (all(len(fin[L]) == N_PER_LEVEL for L in LEVELS)
                and all(eid in byid and ann_complete(recs.get(eid))
                        for L in LEVELS for eid in fin[L])):
            for L in LEVELS:
                chosen[L] = [byid[eid] for eid in fin[L]]
            say('annotation adopted from %s at 0 tokens (%d rows)' % (store, len(recs)))
            return {eid: recs[eid] for L in LEVELS for eid in fin[L]}, meta['report']
        say('stored annotation does not cover the deterministic set; re-annotating')

    if ANN['set_opened'] or R.get('final_started'):
        return stop('STOP: the set is already OPEN - nothing may be annotated or replaced after '
                    'the first Gemini call')
    base = len(R['sessions'])
    ANN['t0'] = time.time()
    P = cz_pipeline()
    v_prompt = P['VPROMPT']('cz')
    v_sha = h16(v_prompt)
    if v_sha != V_SHA:
        return stop('STOP: the v prompt sha16 %s != %s - the frozen 2E pipeline drifted; 0 calls'
                    % (v_sha, V_SHA))
    LK_2D, lk_sha = lk_prompt()
    if lk_sha != LK_SHA:
        return stop('STOP: the lk prompt sha16 %s != %s - the frozen 2E pipeline drifted; 0 calls'
                    % (lk_sha, LK_SHA))
    say('annotation prompts asserted: v %s, lk %s; PAR %d, MAX_RETRY %d, token cap %d'
        % (v_sha, lk_sha, ANN_PAR, ANN_MAX_RETRY, ANN_TOK_CAP))

    stop_evt = threading.Event()
    mon = threading.Thread(target=ann_monitor, args=(stop_evt, base), daemon=True)
    mon.start()
    recs, drvs, reserve_used = {}, {}, {L: 0 for L in LEVELS}
    try:
        for rnd in range(ANN_ROUNDS):
            todo = {L: [r for r in chosen[L] if not ann_complete(recs.get(r['exercise_id']))]
                    for L in LEVELS}
            todo = {L: rows for L, rows in todo.items() if rows}
            if not todo:
                break
            for L, rows in todo.items():
                drvs.update(P['derive_batch'](rows) if P['derive_2c'] else
                            {r['n']: {'reader': {}, 'derived': {}, 'voice_paths': {},
                                      'rewrite': {'action': 'ABSTAIN', 'check': 'N/A'}}
                             for r in rows})
                for r in rows:
                    P['DERIVED'].setdefault(r['n'], {f: None for f in
                                                     ('person', 'number', 'perfective_present')})

            def mk_v(rows):
                return v_prompt + '\n'.join(P['line']({
                    'n': r['n'], 'src': r['src'], 'en': r['en'],
                    'lk_supplied': r.get('correct_answer_en'), 'topic': r.get('type_title'),
                    'level': r.get('level'), 'person': P['DERIVED'][r['n']]['person'],
                    'number': P['DERIVED'][r['n']]['number'],
                    'perfective_present': P['DERIVED'][r['n']]['perfective_present']})
                    for r in rows)

            mv = ann_pass('v', {'%s_r%d' % (L, rnd): rows for L, rows in todo.items()},
                          mk_v, base)
            if ANN['stop']:
                return stop(ANN['stop'])

            # arm-B rewrite, exactly as 2E runs it: only rows the script did not decide itself
            rwc = {}
            for L, rows in todo.items():
                fb = [r for r in rows
                      if (drvs.get(r['n'], {}).get('rewrite') or {}).get('action') not in ('U', 'R')]
                if fb:
                    rwc['%s_r%d' % (L, rnd)] = fb

            def mk_rw(rows):
                return P['REWRITE'] + '\n'.join(P['line']({
                    'n': r['n'], 'lang': r['lang'], 'sk': r['src'], 'en': r['en']}) for r in rows)

            rwm = ann_pass('rw', rwc, mk_rw, base) if rwc else {}
            if ANN['stop']:
                return stop(ANN['stop'])

            for L, rows in todo.items():
                for r in rows:
                    rec = P['assemble'](r, drvs.get(r['n'], {}), mv.get(r['n']), rwm.get(r['n']))
                    rec['exercise_id'] = r['exercise_id']
                    rec['n_2c'] = r.get('n_2c')
                    if ann_complete(rec):
                        recs[r['exercise_id']] = rec
            bad = {L: [r for r in chosen[L] if not ann_complete(recs.get(r['exercise_id']))]
                   for L in LEVELS}
            if not any(bad.values()):
                break
            if rnd == ANN_ROUNDS - 1:
                return stop('STOP: %d sentences could not be annotated after %d rounds %s; the set '
                            'was NOT opened, 0 Gemini calls'
                            % (sum(len(v) for v in bad.values()), ANN_ROUNDS,
                               json.dumps({L: len(v) for L, v in bad.items()})))
            # REPLACEMENT - legal ONLY here, before the set is opened
            assert not ANN['set_opened'] and not R.get('final_started'), \
                'replacement attempted after the set was opened'
            for L, rows in bad.items():
                for r in rows:
                    q = reserve[L]
                    if reserve_used[L] >= len(q):
                        return stop('STOP: the %s reserve queue (%d) is exhausted; the set was NOT '
                                    'opened, 0 Gemini calls' % (L, len(q)))
                    nw = q[reserve_used[L]]
                    reserve_used[L] += 1
                    chosen[L][chosen[L].index(r)] = nw
                    byid[nw['exercise_id']] = nw
                    ANN['replacements'].append({'level': L, 'dropped': r['exercise_id'],
                                                'drawn': nw['exercise_id'], 'round': rnd})
                    say('ANN REPLACE %s: dropped exercise %d, drew reserve exercise %d'
                        % (L, r['exercise_id'], nw['exercise_id']))

        # ----------------------------------------------------- the dedicated lk pass (2F lk)
        final = {L: list(chosen[L]) for L in LEVELS}
        lkc = {L: final[L] for L in LEVELS}

        def mk_lk(rows):
            return LK_2D + '\n'.join(P['line']({
                'n': r['n'], 'en': r['en'],
                'correct_answer_en': r.get('correct_answer_en')}) for r in rows)

        lkm = ann_pass('lk', lkc, mk_lk, base)
        if ANN['stop']:
            return stop(ANN['stop'])
        lkstats = collections.Counter()
        for L in LEVELS:
            for r in final[L]:
                rec = recs[r['exercise_id']]
                mo = lkm.get(r['n'])
                en = rec.get('en') or ''
                fixed = (mo or {}).get('lk_fixed')
                if fixed is None and mo is not None:
                    fixed = mo.get('lk')                      # tolerate the 2B-shaped reply
                if mo is None:
                    lkstats['no_model_row'] += 1
                elif not isinstance(fixed, str) or not fixed.strip() or fixed not in en:
                    lkstats['unusable_span'] += 1
                else:
                    lk = list(rec.get('lk') or [])
                    if lk:
                        lk[0] = fixed
                    else:
                        lk = [fixed]
                    rec['lk'] = lk
                    rec['lk_verdict'] = ('exact' if fixed == (rec.get('lk_supplied') or '')
                                         else 'adjusted')
                    rec['lk_reason'] = ((mo.get('reason') or '')[:120])
                    lkstats['corrected' if rec['lk_verdict'] == 'adjusted' else 'exact'] += 1
                if mo and mo.get('class'):
                    lkstats['class_' + str(mo['class'])] += 1
    finally:
        stop_evt.set()

    fresh = {}
    for L in LEVELS:
        for r in chosen[L]:
            rec = recs[r['exercise_id']]
            missing = [k for k in ANN_KEYS if k not in rec]
            if missing:
                return stop('STOP: the annotation of exercise %d is missing %s - the shape the '
                            'set build consumes is not satisfied; the set was NOT opened, 0 Gemini '
                            'calls' % (r['exercise_id'], missing))
            fresh[r['exercise_id']] = rec
    if ANN['replacements']:
        R['notes'].append('%d sentence(s) were DROPPED after one retry ladder and replaced from '
                          'the stratum reserve BEFORE the set was opened; after the set is opened '
                          'nothing may be replaced' % len(ANN['replacements']))
    rep = {'method': 'frozen 2E pipeline run by this driver: v (2C prompt verbatim) + arm-B '
                     'rewrite + the dedicated lk pass',
           'v_prompt_sha16': v_sha, 'lk_prompt_sha16': lk_sha, 'par': ANN_PAR,
           'max_retry': ANN_MAX_RETRY, 'rounds': ANN_ROUNDS,
           'headless_tokens_annotation': headless_tokens(base),
           'headless_tokens_part2_total': headless_tokens(),
           'token_cap': ANN_TOK_CAP, 'token_estimate': ANN_TOK_EST,
           'sessions': [s['session'] for s in R['sessions'][base:]],
           'refused_chunks': ANN['refused'], 'replacements': ANN['replacements'],
           'reserve_used': reserve_used, 'rows_paid': ANN['rows_paid'],
           'lk_merge': dict(lkstats), 'unmeasurable_windows': ANN['unmeasurable'],
           'derive_2c': bool(P['derive_2c']), 'annotated': len(fresh)}
    with open(store + '.tmp', 'w', encoding='utf-8') as fh:
        for L in LEVELS:
            for r in chosen[L]:
                fh.write(json.dumps(fresh[r['exercise_id']], ensure_ascii=False) + '\n')
    os.replace(store + '.tmp', store)
    jdump({'final_ids': {L: [r['exercise_id'] for r in chosen[L]] for L in LEVELS},
           'report': rep}, meta_p)
    say('annotation done: %s' % json.dumps({k: rep[k] for k in (
        'annotated', 'headless_tokens_annotation', 'refused_chunks', 'replacements',
        'reserve_used', 'lk_merge')}, ensure_ascii=False))
    return fresh, rep


def build_selection():
    """0 Gemini calls.  100 NEW production Czech sentences, 25 per level, drawn read-only from the
    FULL Czech production corpus (39,498 rows) and annotated HERE by the frozen 2E pipeline,
    overlapping nothing 2C/2D/2E/2F-Part-1 used and no phase1* test set."""
    out = os.path.join(SET, 'selection_2fp2.json')
    if jload(out):
        R['selection'] = jload(os.path.join(SET, 'selection_report.json'))
        return True
    sha = lk_prompt_sha()
    if sha != LK_SHA:
        return stop('STOP: lk prompt sha16 %s != %s - the frozen 2E pipeline drifted; 0 calls'
                    % (sha, LK_SHA))
    try:
        corpus = production_cz()
    except Exception as e:
        return stop('STOP: the read-only production query failed (%r); 0 Gemini calls' % e)
    lv_corpus = collections.Counter(r['level'] for r in corpus)
    if len(corpus) != CORPUS_TOTAL or dict(lv_corpus) != CORPUS_BY_LEVEL:
        return stop('STOP: the Czech production corpus is %d rows %s, expected %d %s - the corpus '
                    'moved; the set was NOT opened, 0 Gemini calls'
                    % (len(corpus), json.dumps(dict(lv_corpus)), CORPUS_TOTAL,
                       json.dumps(CORPUS_BY_LEVEL)))

    sel = list(jsonl(os.path.join(TOFF, 'phase2c', 'selection_2c.jsonl')))
    eid2n2c = {}
    for r in sel:
        eid2n2c.setdefault(r['exercise_id'], r['n'])
    try:
        ex_ann, ex_sel, ex_p1, ex_text, used_n, exrep = exclusions()
    except Exception as e:
        return stop('STOP: the exclusion scan failed (%r); 0 Gemini calls' % e)
    ex_ids = ex_ann | ex_sel | ex_p1
    say('exclusions: annotated %d / selection-touched %d / phase1 %d = %d ids, %d texts, used_n %d'
        % (len(ex_ann), len(ex_sel), len(ex_p1), len(ex_ids), len(ex_text), len(used_n)))

    cand = []
    for r in corpus:
        eid = r['exercise_id']
        src = (r.get('src') or '').strip()
        if not src or r['level'] not in LEVELS:
            continue
        if eid in ex_ids or norm(src) in ex_text:
            continue
        n2c = eid2n2c.get(eid)
        if n2c is not None and n2c in used_n:
            continue
        cand.append({'n': eid, 'n_2c': n2c, 'exercise_id': eid, 'lang': 'cz', 'src': src,
                     'en': r.get('en') or '', 'level': r['level'],
                     'concept_id': r.get('concept_id'), 'headword': r.get('headword'),
                     'exercise_type_id': r.get('exercise_type_id'),
                     'type_title': r.get('type_title'),
                     'correct_answer_en': r.get('ca_en'), 'correct_answer_cz': r.get('ca_cz')})
    by_level = collections.defaultdict(list)
    for r in cand:
        by_level[r['level']].append(r)
    short = {L: len(by_level[L]) for L in LEVELS
             if len(by_level[L]) < N_PER_LEVEL + RESERVE_PER_LEVEL}
    if any(len(by_level[L]) < N_PER_LEVEL for L in LEVELS):
        return stop('STOP: not enough fresh production Czech sentences per level %s (need %d each '
                    'plus a reserve of %d); the set was NOT opened, 0 Gemini calls'
                    % (json.dumps({L: len(by_level[L]) for L in LEVELS}), N_PER_LEVEL,
                       RESERVE_PER_LEVEL))
    if short:
        defect('thin_reserve', 'levels %s have fewer than %d candidates, so the replacement queue '
                               'is shorter than designed' % (json.dumps(short),
                                                             N_PER_LEVEL + RESERVE_PER_LEVEL))
    ordered, reserve, chosen = {}, {}, {}
    for L in LEVELS:
        o = sorted(by_level[L], key=lambda r: hashlib.md5(
            ('%d|%d' % (SEED, r['exercise_id'])).encode()).hexdigest())
        ordered[L] = o
        chosen[L] = o[:N_PER_LEVEL]
        reserve[L] = o[N_PER_LEVEL:N_PER_LEVEL + RESERVE_PER_LEVEL]

    # --------------------------------------------------- CHANGE 2: annotate the 100 ourselves
    ann = annotate_set(chosen, reserve)
    if not ann:                        # annotate_set already wrote the stop into R
        return False
    fresh, annrep = ann
    picked = [(L, chosen[L]) for L in LEVELS]

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
            nums[r['exercise_id']] = num            # identity = exercise_id, unique and never None
    for L, rows in picked:
        for j, r in enumerate(rows):
            a = fresh[r['exercise_id']]
            num = nums[r['exercise_id']]
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
                          'level': L, 'topic': r['type_title'], 'n': r.get('n_2c'),
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
    ex_ids_all = ex_ids
    overlaps = [s['sid'] for s in sents
                if norm(s['czech']) in ex_text or s['exercise_id'] in ex_ids_all]
    internal = collections.Counter(norm(s['czech']) for s in sents)
    violations = [t for t, c in internal.items() if c > 1]
    lvc = collections.Counter(s['level'] for s in sents)
    rep = {'source': 'FULL Czech production corpus (read-only SELECT), not phase2c/selection_2c.jsonl',
           'corpus_total': len(corpus), 'corpus_by_level': dict(lv_corpus),
           'corpus_expected': CORPUS_TOTAL, 'corpus_expected_by_level': CORPUS_BY_LEVEL,
           'exclusion_ex_annotated': len(ex_ann), 'exclusion_ex_selection': len(ex_sel),
           'exclusion_ex_phase1': len(ex_p1), 'exclusion_ex_ids_union': len(ex_ids_all),
           'exclusion_ex_text': len(ex_text), 'exclusion_used_n': len(used_n),
           'exclusion_detail': exrep,
           'candidates': len(cand),
           'candidates_by_level': {L: len(by_level[L]) for L in LEVELS},
           'reserve_by_level': {L: len(reserve[L]) for L in LEVELS},
           'reserve_used': annrep.get('reserve_used'),
           'replacements_made': annrep.get('replacements'),
           'annotation': annrep,
           'picked': len(sents), 'by_level': dict(lvc),
           'halves': dict(collections.Counter(s['tags']['half'] for s in sents)),
           'kinds': dict(collections.Counter(s['tags']['kind'] for s in sents)),
           'sid_range': [min(sids), max(sids)], 'seed': SEED,
           'earlier_n_checked_against': len(used_n),
           'earlier_sentences_checked_against': len(ex_text),
           'sources_checked': exrep.get('sources_checked'),
           'overlaps_total': len(overlaps), 'violations_total': len(violations),
           'lk_prompt_sha16': sha, 'lk_verdicts': dict(collections.Counter(
               (ann_out[str(s['sid'])].get('lk_verdict') or 'none') for s in sents))}
    rep['v_prompt_sha16'] = [annrep.get('v_prompt_sha16')] if annrep.get('v_prompt_sha16') else []
    if rep['v_prompt_sha16'] and V_SHA not in rep['v_prompt_sha16']:
        defect('v_prompt_sha', 'the v prompt this driver sent has sha %s, expected %s'
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
        'corpus_total', 'corpus_by_level', 'candidates', 'candidates_by_level', 'picked',
        'by_level', 'halves', 'kinds', 'overlaps_total', 'violations_total',
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
        if not budget_room(len(todo) * 60_000):     # Part 2's own headless ceiling, never blown
            return stop(ANN['stop'])
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
        if not budget_room(250_000):                # Part 2's own headless ceiling, never blown
            return stop(ANN['stop'])
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
# P-FROZEN-1U, unchanged.  Run cap for Part 2: 588 counted calls (the phase-wide cap of 900 minus
# the 312 counted calls Part 3.1 already spent).
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
CAP_1U = 588
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
    rp = os.path.join(RUN, 'runner_1u.py')
    if os.path.exists(rp):
        # CHANGE 4: a runner copied before the ceiling moved still carries the old cap in the
        # appended 2F patch (the 900 on the 1U line above it is never touched).
        cur = open(rp, encoding='utf-8').read()
        if '\nCAP_1U = 600\n' in cur:
            open(rp, 'w', encoding='utf-8').write(cur.replace('\nCAP_1U = 600\n',
                                                              '\nCAP_1U = %d\n' % CAP_RUN))
            say('run side: the appended Part 2 cap lowered from 600 to %d' % CAP_RUN)
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
    say('run side copied into %s (loader sid range, runner TOFF anchor + TASKA + stack + cap %d, '
        'scorer S7)' % (RUN, CAP_RUN))
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
    already = calls_stats()['counted_http200']
    if planned + already > CAP_RUN:
        return stop('STOP: planned %s counted calls + %s already counted > Part 2 ceiling %d '
                    '(phase cap %d minus Part 3.1\'s %d); 0 calls'
                    % (planned, already, CAP_RUN, PHASE_CAP, PART31_COUNTED))
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
    # CHANGE 4: merge, never overwrite - part31_counted and anything else the phase wrote stays.
    bud = jload(BUDGET, {}) or {}
    bud['part2_counted'] = cs['counted_http200']
    bud['part2_cap'] = CAP_RUN
    bud['phase_cap'] = PHASE_CAP
    jdump(bud, BUDGET)
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
        if blk == 'selection':
            s = R.get('selection') or {}
            a = s.get('annotation') or {}
            L += ['- source: the FULL Czech production corpus, read with a SELECT-only query '
                  '(never 2C\'s 4,064-row sample of it, and nothing was ever written)',
                  '- corpus total: %s (expected %d); by level: %s (expected %s)'
                  % (s.get('corpus_total'), CORPUS_TOTAL,
                     json.dumps(s.get('corpus_by_level')), json.dumps(CORPUS_BY_LEVEL)),
                  '- exclusion set sizes: annotated-by-2C/2D/2E/2F-Part-1 exercise ids %s, '
                  'selection_2c rows those phases touched %s, phase1*/pilot/measurements exercise '
                  'ids %s, union of id sets %s, normalised sentence texts %s, 2C row numbers (n) '
                  '%s' % (s.get('exclusion_ex_annotated'), s.get('exclusion_ex_selection'),
                          s.get('exclusion_ex_phase1'), s.get('exclusion_ex_ids_union'),
                          s.get('exclusion_ex_text'), s.get('exclusion_used_n')),
                  '- candidates after exclusion: %s total, by level %s'
                  % (s.get('candidates'), json.dumps(s.get('candidates_by_level'))),
                  '- reserve queue built: %s; reserve used: %s; replacements made: %s'
                  % (json.dumps(s.get('reserve_by_level')), json.dumps(s.get('reserve_used')),
                     json.dumps(s.get('replacements_made'), ensure_ascii=False)[:600]),
                  '- overlap count: %s; violation count: %s'
                  % (s.get('overlaps_total'), s.get('violations_total')),
                  '- annotation token spend (headless, this driver): %s of the %s cap; refused '
                  'chunks %s; v prompt sha16 %s; lk prompt sha16 %s; PAR %s; MAX_RETRY %s'
                  % (a.get('headless_tokens_annotation'), a.get('token_cap'),
                     json.dumps(a.get('refused_chunks'), ensure_ascii=False)[:400],
                     a.get('v_prompt_sha16'), a.get('lk_prompt_sha16'), a.get('par'),
                     a.get('max_retry')), '']
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
    L += ['- Gemini budget: %s counted of Part 2\'s ceiling %d (phase-wide cap %d minus the %d '
          'counted calls Part 3.1 already spent).  counted = http 200 only; http 0 / 429 / 5xx are '
          'retried with logged back-off as counted:false; an empty or unparsable 200 is a FAILED '
          'call - counted, never guessed, never silently retried.'
          % (cs['counted_http200'], CAP_RUN, PHASE_CAP, PART31_COUNTED),
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
    # CHANGE 1 + 2, 0 calls: the SQL guard, the lifted 2E prompts, and the completeness gate
    try:
        sql_guard(PROD_SQL % (1, 0))
        notes.append('sql_guard accepts the production SELECT: OK')
        for bad_sql in ('select 1; delete from exercises',
                        'update exercise_localizations set full_sentence = %s' % "''",
                        '-- select only\ndrop table exercises'):
            try:
                sql_guard(bad_sql)
                ok = False
                notes.append('SELFTEST FAILURE: sql_guard accepted a write statement %r' % bad_sql)
            except RuntimeError:
                pass
        notes.append('sql_guard refuses INSERT/UPDATE/DELETE/DDL and multi-statement SQL: OK')
        P = cz_pipeline()
        vs = h16(P['VPROMPT']('cz'))
        notes.append('v prompt sha16 %s (%s)' % (vs, 'OK' if vs == V_SHA else 'DRIFTED'))
        ok = ok and vs == V_SHA
        assert not ann_complete({'v': ['x'], 'lk': ['x'], 'tf': None, 'voice': 'active_agent'}), \
            'ann_complete accepted an annotation with no tf'
        assert ann_complete({'v': ['x'], 'lk': ['x'], 'tf': 'past', 'voice': 'active_agent'})
        notes.append('annotation completeness gate refuses an incomplete record: OK')
        spent = headless_tokens()
        if budget_room(ANN_TOK_CAP + 1):
            ok = False
            notes.append('SELFTEST FAILURE: budget_room allowed a spend over the %d token cap'
                         % ANN_TOK_CAP)
        else:
            notes.append('headless token cap %d refuses an over-cap wave (spent %d): OK'
                         % (ANN_TOK_CAP, spent))
        ANN['stop'] = None
    except AssertionError as e:
        ok = False
        notes.append('SELFTEST FAILURE: %s' % e)
    except Exception as e:
        import traceback
        ok = False
        notes.append('SELFTEST EXCEPTION (change 1/2): %s' % traceback.format_exc()[-800:])
    R['status'] = None          # a negative sub-test must not leak a status into the real run
    jdump({'ok': ok, 'notes': notes}, os.path.join(HERE, 'SELFTEST_2FP2.json'))
    for n in notes:
        say('selftest: %s' % n)
    say('SELFTEST %s' % ('PASS' if ok else 'FAIL'))
    return ok


# ------------------------------------------------------------------------------- main
def selection_preview():
    """0 Gemini calls, 0 headless tokens, 0 sessions: the widened pool and every exclusion set,
    printed and written to p2/set/selection_preview.json.  Annotates nothing."""
    corpus = production_cz()
    lv = collections.Counter(r['level'] for r in corpus)
    ex_ann, ex_sel, ex_p1, ex_text, used_n, exrep = exclusions()
    ex_ids = ex_ann | ex_sel | ex_p1
    sel = list(jsonl(os.path.join(TOFF, 'phase2c', 'selection_2c.jsonl')))
    eid2n2c = {}
    for r in sel:
        eid2n2c.setdefault(r['exercise_id'], r['n'])
    by_level, seen = collections.defaultdict(list), collections.Counter()
    for r in corpus:
        eid, src = r['exercise_id'], (r.get('src') or '').strip()
        if not src or r['level'] not in LEVELS:
            continue
        if eid in ex_ids or norm(src) in ex_text:
            continue
        n2c = eid2n2c.get(eid)
        if n2c is not None and n2c in used_n:
            continue
        by_level[r['level']].append(r)
        seen[norm(src)] += 1
    picked = {}
    for L in LEVELS:
        o = sorted(by_level[L], key=lambda r: hashlib.md5(
            ('%d|%d' % (SEED, r['exercise_id'])).encode()).hexdigest())
        picked[L] = [r['exercise_id'] for r in o[:N_PER_LEVEL]]
    ptexts = [norm(r['src']) for L in LEVELS for r in
              sorted(by_level[L], key=lambda r: hashlib.md5(
                  ('%d|%d' % (SEED, r['exercise_id'])).encode()).hexdigest())[:N_PER_LEVEL]]
    rep = {'corpus_total': len(corpus), 'corpus_by_level': dict(lv),
           'corpus_expected': CORPUS_TOTAL, 'corpus_expected_by_level': CORPUS_BY_LEVEL,
           'ex_annotated': len(ex_ann), 'ex_selection': len(ex_sel), 'ex_phase1': len(ex_p1),
           'ex_ids_union': len(ex_ids), 'ex_text': len(ex_text), 'used_n': len(used_n),
           'candidates_total': sum(len(by_level[L]) for L in LEVELS),
           'candidates_by_level': {L: len(by_level[L]) for L in LEVELS},
           'reserve_available_by_level': {L: max(0, len(by_level[L]) - N_PER_LEVEL)
                                          for L in LEVELS},
           'overlaps_total': 0, 'violations_total': len([t for t, c in
                                                         collections.Counter(ptexts).items()
                                                         if c > 1]),
           'picked_exercise_ids': picked, 'gemini_calls': 0, 'headless_tokens': 0}
    jdump(rep, os.path.join(SET, 'selection_preview.json'))
    say('selection preview: %s' % json.dumps(rep, ensure_ascii=False))
    return rep


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--selection-only', action='store_true',
                    help='0 calls, 0 tokens: print the widened pool and the exclusion sets')
    ap.add_argument('--no-wait', action='store_true')
    a = ap.parse_args()
    for d in (SET, RUN, DATA, SESS, os.path.join(SET, 'judge'), os.path.join(SET, 'writers'),
              os.path.join(SET, 'briefs')):
        os.makedirs(d, exist_ok=True)
    if a.selftest:
        sys.exit(0 if selftest() else 2)
    if a.selection_only:
        selection_preview()
        sys.exit(0)
    old = jload(STATE)
    if old:
        R.update(old)
        R['status'] = None
    bud = jload(BUDGET, {}) or {}
    bud.setdefault('part2_counted', 0)
    bud['part2_cap'] = CAP_RUN                  # 588, never 600; part31_counted is never touched
    bud['phase_cap'] = PHASE_CAP
    jdump(bud, BUDGET)
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
