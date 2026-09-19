#!/usr/bin/env python3
"""Phase 1N runner — the new set under P-FROZEN-1N, measured ONCE.

Built from phase1m/runner_1m.py; byte-identical copies of the executed 1M modules
(runner_1l.py / loader_1l.py / f8.py / f8v2.py / f9.py) sit next to this file.

Decisions frozen for 1N
  * prompt P-FROZEN-1N = P-FROZEN with ONE line inserted, the OPPOSITE voice rule
    ("... that is SAME, provided the meaning is preserved"). Nothing else in the prompt
    changes; see PROMPT_DIFF_1N.md. The request hash therefore differs from every stored
    1M verdict by construction: the 1N side is paid for in full.
  * F8 NEVER decides. f8 (v1) and f8v2 are computed per item as READOUTS and reported as the
    shadows "F8v1-on" / "F8v2-on" (headline under each + COST / CATCHES / UNIQUE with ids).
  * F9 does not decide, LOCKTIP on, TIP-as-rejection on, arm B, F2B / F3 / F4v2 / F5 untouched.
  * judge types T / W / M / S — V is retired as a TYPE; the passive dimension is carried by the
    writer key `passive` (null | by | agentless) and by the judge row's own `passive` key.
  * hygiene is deliberately OFF (phase1n/hygiene does not exist) and reported as a null.

Modes
  --dev             0 calls. Re-scores the CLOSED sides dev / replay1j / fresh1l / fresh1m from
                    stored verdicts. --f8 f8v2 must reproduce Phase 1M on fresh1m (547/614 and
                    69/646); --f8 none is the 1N headline configuration.
  --selftest-final  0 calls. Drives the ENTIRE post-transport --final path (label merge, metrics,
                    cells, shadows, markdown) over the fresh1m data and stored verdicts into
                    phase1n/selftest/.
  --probe           the NEW prompt on <=120 seeded-random L3-eligible 1M items of writer intent V;
                    counted in phase1n/calls.jsonl; writes probe_1n.json.
  --dry             no label read, no model call: build, chk distribution, preflight, plan.
  --final           once. Refuses on FINAL_RUN_DONE / missing FREEZE_HASH / code drift.

Model everywhere: gemini-3.1-flash-lite, temperature 0, thinkingBudget 0.
"""
import argparse, collections, json, os, random, subprocess, sys, threading
from concurrent.futures import ThreadPoolExecutor

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import loader_1l as L                                                          # noqa: E402
import runner_1l as RL                                                         # noqa: E402
import loader_1n as LM                                                         # noqa: E402

R1K, R, P, C = RL.R1K, RL.R, RL.P, RL.C
TYPES = ('T', 'W', 'M', 'S')                     # V is gone, E is gone
RL.TYPES = TYPES                                 # col_metrics reads the module global
TOFF = RL.TOFF
P1L = os.path.join(TOFF, 'phase1l')
P1M = os.path.join(TOFF, 'phase1m')
M_DATA = os.path.join(P1M, 'data')
M_JUDGE = os.path.join(P1M, 'judge')
TYPES_1M = ('T', 'W', 'M', 'S', 'V', 'E')        # only for re-scoring the CLOSED 1M labels
REPO = RL.REPO

# ---- stored verdicts of every earlier phase are reusable read-only; ours is phase1n/calls.jsonl
RL.LEDGERS_RO = list(RL.LEDGERS_RO) + [os.path.join(P1L, 'calls.jsonl'),
                                       os.path.join(P1M, 'calls.jsonl')]
CALLS = RL.CALLS                                    # phase1n/calls.jsonl (RL.HERE == phase1n)
FREEZE_HASH = RL.FREEZE_HASH                        # phase1n/FREEZE_HASH
FREEZE_FILES = os.path.join(HERE, 'FREEZE_FILES')
DONE = RL.DONE                                      # phase1n/FINAL_RUN_DONE
STOP_PRE = RL.STOP_PRE
STOP_PLAN = RL.STOP_PLAN
STOP_CHK = os.path.join(HERE, 'STOP_CHK.txt')
PAUSED = os.path.join(HERE, 'RUN_PAUSED.txt')
CFG_PATH = os.path.join(HERE, 'FROZEN_CONFIG_1N.json')
RUNLOG = os.path.join(HERE, 'run_1n.log')
SELFTEST = os.path.join(HERE, 'selftest')
PHASE_CAP_1N = 1200                                 # counted calls for the WHOLE phase
PRICE_IN, PRICE_OUT = RL.PRICE_IN, RL.PRICE_OUT
DEV_EXP = {'coverage': (182, 189), 'fa': (12, 301)}
REPLAY_EXP = {'coverage': (178, 196), 'fa': (15, 294), 'fa_T': (2, 59)}
FRESH1M_EXP = {'coverage': (547, 614), 'fa': (69, 646)}     # Phase 1M headline, --f8 f8v2
SIDE_TAG = 'fresh1n'
DEV_PROMPT = 'P-FROZEN'                             # every stored verdict was made under it
PROMPT_1N = 'P-FROZEN-1N'

# ---------------------------------------------------------------- the ONE prompt change
VOICE_SAME_LINE = (
    'Voice: if the Slovak names an agent in the nominative and the learner sentence moves that '
    'agent out of subject position or drops it (an active Slovak sentence turned into an English '
    'passive), that is SAME, provided the meaning is preserved. Where the Slovak is itself '
    'impersonal or passive, an English passive is SAME.')

_ORIG_BUILD_REQ = R1K.build_req


def build_req_1n(st, r, prompt_id):
    """P-FROZEN-1N = the P-FROZEN body with VOICE_SAME_LINE inserted after WORDING_LINE.

    The body comes from the original builder, so every other byte (system text, the P-B lines,
    the gender line, GROUND_LINE, WORDING_LINE, the tail, GEN_CFG) is identical.
    """
    if prompt_id != PROMPT_1N:
        return _ORIG_BUILD_REQ(st, r, prompt_id)
    sysx, user, gcfg, _h = _ORIG_BUILD_REQ(st, r, 'P-FROZEN')
    lines = user.split('\n')
    at = [k for k, ln in enumerate(lines) if ln == P.WORDING_LINE]
    if len(at) != 1:
        raise SystemExit('REFUSED: WORDING_LINE occurs %d times in the P-FROZEN body' % len(at))
    lines = lines[:at[0] + 1] + [VOICE_SAME_LINE] + lines[at[0] + 1:]
    user = '\n'.join(lines)
    return sysx, user, gcfg, R.req_hash(sysx, user, gcfg)


R1K.build_req = build_req_1n
if PROMPT_1N not in tuple(getattr(R1K, 'PROMPTS', ())):
    R1K.PROMPTS = tuple(getattr(R1K, 'PROMPTS', ())) + (PROMPT_1N,)


def say(line):
    print(line, flush=True)
    with open(RUNLOG, 'a', encoding='utf-8') as fh:
        fh.write(line + '\n')


def alog(side, what, n, purpose):
    LM._log(side, what, n, purpose, caller='runner_1n.py')


# ================================================================== config / guard modules
def load_cfg(overrides=None):
    if not os.path.exists(CFG_PATH):
        raise SystemExit('REFUSED: %s does not exist' % CFG_PATH)
    c = json.load(open(CFG_PATH, encoding='utf-8'))
    for k in ('f8_module', 'f8_decides', 'f9_decides', 'tip_reject', 'locktip', 'arm', 'prompt',
              'model', 'temperature', 'thinkingBudget'):
        if k not in c:
            raise SystemExit('REFUSED: FROZEN_CONFIG_1N.json has no %r' % k)
    if not c['locktip']:
        raise SystemExit('REFUSED: locktip is frozen true')
    if c['f8_decides'] or c['f8_module'] != 'none':
        raise SystemExit('REFUSED: F8 decides nothing in Phase 1N '
                         '(f8_decides false, f8_module "none")')
    if not c['tip_reject']:
        raise SystemExit('REFUSED: TIP-as-rejection is frozen true')
    if c['arm'] != 'B':
        raise SystemExit('REFUSED: arm B is frozen')
    if c['prompt'] != PROMPT_1N:
        raise SystemExit('REFUSED: the frozen prompt is %s' % PROMPT_1N)
    o = overrides or {}
    sel = {'prompt': c['prompt'], 'locktip': True, 'f9_strict': False,
           'f8_module': o.get('f8') or c['f8_module'],
           'f8': bool(o.get('f8')) and o.get('f8') != 'none',   # decides ONLY via a --dev override
           'f9': (o['f9'] == 'on') if o.get('f9') else bool(c['f9_decides']),
           'tip_reject': (o['tip'] != 'accept') if o.get('tip') else bool(c['tip_reject']),
           'arm': c['arm'], 'model': c['model'], 'temperature': c['temperature'],
           'thinkingBudget': c['thinkingBudget']}
    sel['name'] = 'LOCKTIP+%s%s (TIP-as-rejection %s)' % (
        sel['f8_module'].upper() if sel['f8'] else 'F8-READOUT-ONLY',
        '+F9' if sel['f9'] else '', 'on' if sel['tip_reject'] else 'off')
    return c, sel


def select_f8(name):
    """Bind an F8 implementation BY NAME onto R1K. 'none' leaves the readout module bound."""
    if name in (None, 'none'):
        return getattr(R1K, 'f8', None)
    if name == 'f8':
        mod = sys.modules.get('f8') or getattr(RL, 'f8', None)
        if mod is None:
            raise SystemExit('REFUSED: f8 module not importable')
    else:
        path = os.path.join(HERE, name + '.py')
        if not os.path.exists(path):
            raise SystemExit('REFUSED: F8 module %s does not exist' % path)
        import importlib.util
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[name] = mod
        spec.loader.exec_module(mod)
        if not hasattr(mod, 'check'):
            raise SystemExit('REFUSED: %s.py has no check()' % name)
    R1K.f8 = mod
    return mod


# ================================================================== 2.1 builder for the new side
def _band(sk):
    n = len((sk or '').split())
    return '1-6' if n <= 6 else '7-9' if n <= 9 else '10-12' if n <= 12 else '13-16' if n <= 16 else '17+'


def build_side_1n(purpose, hyg_on=False, data_dir=None, side_tag=None):
    """The 1M builder, parameterised by data directory / side tag.

    chk is COMPUTED for every record with runner_1l.compute_chk AFTER make_state — never read
    from the items, never asserted (that void-ed Phase 1k). The writer key `passive`
    (null | by | agentless) is carried through; a side without it tolerates None.
    """
    tag = side_tag or SIDE_TAG
    info = {'side': tag, 'data_dir': data_dir or os.path.join(HERE, 'data')}
    sents = {int(s['sid']): s for s in LM.load_sentences(purpose, caller='runner_1n.py',
                                                         data_dir=data_dir)}
    ann = LM.load_annotations(purpose, caller='runner_1n.py', data_dir=data_dir)
    items = LM.load_items(purpose, caller='runner_1n.py', data_dir=data_dir)
    recs = []
    for it in items:
        sid = int(it['sid'])
        if sid not in sents:
            raise SystemExit('REFUSED: item %s has no sentence %d' % (it['id'], sid))
        s = sents[sid]
        a = ann.get(str(sid)) or {}
        hy = a.get('hygienised', a)
        if not hy:
            raise SystemExit('REFUSED: sid %d has no annotation' % sid)
        lk = []
        for x in (hy.get('lk') or []):
            if isinstance(x, str):
                lk.append(x)
            elif isinstance(x, (list, tuple)):
                lk += [y for y in x if isinstance(y, str)]
        refs = [x for x in (hy.get('v') or []) if isinstance(x, str) and x.strip()]
        r = {'item_id': it['id'], 'kind': it['id'].split(':')[0], 'sid': sid, 'n': 1,
             'level': s.get('level'), 'topic': s.get('topic'), 'sk': s['slovak'],
             'band': _band(s['slovak']), 'reference': refs[0], 'refs': list(refs),
             'answer': it['answer'],
             'judged': 'wrong' if it['id'].startswith('W') else 'correct',
             'wrong_type': None, 'half': 'NEW', 'locks': lk,
             'intent': it.get('intent'), 'form': it.get('form'),
             'passive': it.get('passive'), 'tags': dict(s.get('tags') or {}),
             'chk': {'verdict': 'wrong', 'step': 'auto', 'feedback': ''}, 'chk_missing': False,
             'rows': [], 'lock_ok': True, 'lock_released_2_1': None}
        try:
            nrm = C.base.norm
            r['lock_ok'] = (not lk) or any(nrm(x).strip() in nrm(r['answer']) for x in lk)
            if not r['lock_ok']:
                ok, tr = C.lock_equivalent_ok(P.to_item(r))
                if ok:
                    r['lock_ok'], r['lock_released_2_1'] = True, tr
        except Exception:
            pass
        recs.append(r)
    if hyg_on:
        patches, files = RL.hygiene_patches(tag, purpose)
        if patches:
            info['hygiene'] = RL.apply_hygiene(recs, ann, patches)
            info['hygiene_files'] = [os.path.basename(f) for f in files]
    try:
        st = R.make_state(recs, ann, ('F4v3',), side_tag=tag)
    except Exception as e:                                   # unknown side tag -> the 1k tag
        say('[BUILD] make_state(side_tag=%r) failed (%s); falling back to "fresh1k"' % (tag, e))
        st = R.make_state(recs, ann, ('F4v3',), side_tag='fresh1k')
    how = collections.Counter()
    dist = collections.Counter()
    for r in recs:
        r['chk'], h = RL.compute_chk(r)                      # COMPUTED, never read from the item
        r['chk_missing'] = False
        how[h] += 1
        dist['%s/%s' % (r['chk']['verdict'], r['chk']['step'])] += 1
    info['chk_computed'] = dict(how)
    info['chk_distribution'] = dict(dist)
    info['n_items'] = len(recs)
    info['n_sentences'] = len({r['sid'] for r in recs})
    info['passive_tags'] = dict(collections.Counter(str(r['passive']) for r in recs))
    say('[BUILD %s] %d items / %d sentences   chk distribution %s   passive tags %s'
        % (tag, len(recs), info['n_sentences'],
           json.dumps(info['chk_distribution'], sort_keys=True),
           json.dumps(info['passive_tags'], sort_keys=True)))
    acc = [r for r in recs if r['chk']['verdict'] in ('correct', 'correct_with_tip')]
    if len(dist) == 1 and len(acc) == len(recs):
        open(STOP_CHK, 'w', encoding='utf-8').write(json.dumps(
            {'why': 'every record carries the same ACCEPTING chk — the Phase 1k hard-wired-checker '
                    'defect; nothing was measured and no model call was made',
             'chk_distribution': info['chk_distribution'], 'n_items': len(recs)}, indent=1) + '\n')
        raise SystemExit('STOP: degenerate chk, %s written, 0 model calls made' % STOP_CHK)
    return st, recs, ann, {r['item_id']: r for r in recs}, info


def preflight_1n(st, recs, tag):
    lock_rej, l3 = RL.lock_counts(st, recs)
    say('L2 lock firings under BASE: %d   L3-eligible under LOCKTIP: %d' % (len(lock_rej), len(l3)))
    say('[PREFLIGHT %s] (reference numbers: DEV 65/318, 1j replay 310/336, 1M fresh 249/1115)' % tag)
    if not lock_rej or not l3:
        open(STOP_PRE, 'w', encoding='utf-8').write(json.dumps(
            {'tag': tag, 'lock_rejections_BASE': len(lock_rej), 'l3_eligible_LOCKTIP': len(l3),
             'why': 'degenerate side (the Phase 1k defect); no model call was made'}, indent=1) + '\n')
        raise SystemExit('STOP: preflight failed, %s written, 0 model calls made' % STOP_PRE)
    return lock_rej, l3


# ================================================================== freeze
def check_freeze_1n():
    if not os.path.exists(FREEZE_HASH):
        raise SystemExit('REFUSED: %s does not exist — freeze the code first.' % FREEZE_HASH)
    if not os.path.exists(FREEZE_FILES):
        raise SystemExit('REFUSED: %s does not exist — list the frozen python files.' % FREEZE_FILES)
    h = open(FREEZE_HASH, encoding='utf-8').read().strip().split()[0]
    files = [x.strip() for x in open(FREEZE_FILES, encoding='utf-8').read().splitlines()
             if x.strip() and not x.strip().startswith('#')]
    here_py = sorted(f for f in os.listdir(HERE) if f.endswith('.py'))
    missing = [f for f in here_py if f not in files]
    if missing:
        raise SystemExit('REFUSED: these .py files are in phase1n but not in FREEZE_FILES: %s'
                         % ', '.join(missing))
    bad = []
    for f in files:
        p = os.path.join(HERE, f)
        if not os.path.exists(p):
            bad.append({'file': f, 'now': 'ABSENT', 'at_freeze': '?'})
            continue
        cur = subprocess.check_output(['git', 'hash-object', p], cwd=REPO).decode().strip()
        try:
            was = subprocess.check_output(
                ['git', 'rev-parse', '%s:translation-offline/phase1n/%s' % (h, f)],
                cwd=REPO, stderr=subprocess.DEVNULL).decode().strip()
        except subprocess.CalledProcessError:
            was = None
        if cur != was:
            bad.append({'file': f, 'now': cur[:12], 'at_freeze': (was or 'ABSENT')[:12]})
    if bad:
        raise SystemExit('REFUSED: phase1n code differs from FREEZE_HASH %s: %s'
                         % (h, json.dumps(bad)))
    say('[FREEZE] %d python files identical to commit %s' % (len(files), h))
    return h


# ================================================================== requests / transport
def plan_1n(st, recs, ids, prompt_id, tag):
    req = RL.plan_requests(st, recs, ids, prompt_id, tag)
    return {h: (s, u, g, hh, 'L-1N:%s' % tag, i) for h, (s, u, g, hh, _t, i) in req.items()}


def counted_local():
    n = 0
    if os.path.exists(CALLS):
        for row in R.ledger_rows(CALLS):
            if row.get('counted'):
                n += 1
    return n


def make_calls(req, need):
    """Transport exactly as 1M/1L call_one; 5 consecutive fully-retried failures = quota wall.

    counted = HTTP 200 only; http 0 / 429 / 5xx is retried with backoff and logged counted:false;
    an empty 200 is a counted failure — never retried, never guessed.
    """
    keys = RL.load_keys()
    key = keys[0]                                  # free tier first, as 1M ran it
    st = {'ok': 0, 'bad': 0, 'empty': 0, 'streak': 0, 'wall': False, 'skipped': 0}
    lk = threading.Lock()

    def work(h):
        with lk:
            if st['wall']:
                st['skipped'] += 1
                return None
        row = RL.call_one(req[h], key)
        with lk:
            if row.get('http') == 200:
                st['ok'] += 1
                st['streak'] = 0
                if row.get('empty'):
                    st['empty'] += 1
            else:
                st['bad'] += 1
                st['streak'] += 1
                if st['streak'] >= 5:
                    st['wall'] = True
        return row

    todo = list(need)
    random.Random(1).shuffle(todo)                 # interleaved: an outage damages all cells equally
    with ThreadPoolExecutor(max_workers=6) as pool:
        for _ in pool.map(work, todo):
            pass
    say('[CALLS] http200 %d (empty replies %d)  transport-dead %d  skipped after the wall %d'
        % (st['ok'], st['empty'], st['bad'], st['skipped']))
    return st


def cap_or_stop(need, done, what):
    if done + len(need) > PHASE_CAP_1N:
        open(STOP_PLAN, 'w', encoding='utf-8').write(json.dumps(
            {'what': what, 'planned_new_calls': len(need), 'already_counted': done,
             'cap': PHASE_CAP_1N,
             'why': 'the plan exceeds the phase cap; nothing was trimmed and no call was made'},
            indent=1) + '\n')
        raise SystemExit('STOP: %d + %d > cap %d — %s written, 0 calls made'
                         % (done, len(need), PHASE_CAP_1N, STOP_PLAN))


# ================================================================== §13 builder limit
def _lev(a, b):
    if a == b:
        return 0
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def l1_nearmiss(r):
    """A plausible PRODUCTION L1 accept (spelling_variant / fuzzy) that compute_chk cannot make."""
    it = {'exercise_id': r['sid'], 'reference': r['reference'], 'answer': r['answer'],
          'item_id': r['item_id'], 'sk': r['sk']}
    n = C.base.norm(r['answer'])
    try:
        refs = C.refs_of(it)
    except Exception:
        refs = [r['reference']] + list(r.get('refs') or [])
    refs = [x for x in refs if isinstance(x, str)]
    if any(C.base.norm(x) == n for x in refs):
        return None
    best = None
    for x in refs:
        m = C.base.norm(x)
        ta, tb = n.split(), m.split()
        if len(ta) == len(tb):
            per = [_lev(p, q) for p, q in zip(ta, tb)]
            if per and max(per) <= 1 and sum(per) <= 2:
                cand = {'ref': x, 'dist': sum(per), 'len_mismatch': False}
                if best is None or cand['dist'] < best['dist']:
                    best = cand
        elif abs(len(ta) - len(tb)) <= 2:
            d = _lev(n, m)
            if d <= 2:
                cand = {'ref': x, 'dist': d, 'len_mismatch': True}
                if best is None or cand['dist'] < best['dist']:
                    best = cand
    return best


# ================================================================== scoring blocks
def cell_by_intent(by, res, lab, intent, split_by_form):
    ids = [i for i in by if by[i].get('intent') == intent and lab[i][0] == 'wrong']
    acc = [i for i in ids if res[i]['accepted']]
    out = {'judged_wrong': len(ids), 'accepted': len(acc), 'rate': P.rate(len(acc), len(ids)),
           'rejecting_layers': dict(collections.Counter(
               str(res[i]['layer']) for i in ids if not res[i]['accepted'])),
           'accepted_ids': sorted(acc)}
    if split_by_form:
        forms = {}
        for f in ('passive', 'cleft', 'reported', 'dropped', None):
            fid = [i for i in ids if by[i].get('form') == f]
            if not fid and f is None:
                continue
            fac = [i for i in fid if res[i]['accepted']]
            forms[str(f)] = {'judged_wrong': len(fid), 'accepted': len(fac),
                             'rate': P.rate(len(fac), len(fid)),
                             'rejecting_layers': dict(collections.Counter(
                                 str(res[i]['layer']) for i in fid if not res[i]['accepted']))}
        out['by_form'] = forms
    return out


def passive_cell(ids, res):
    """accepted / rejected per layer / TIP fired, for ONE passive tag."""
    acc = [i for i in ids if res[i]['accepted']]
    rej = [i for i in ids if not res[i]['accepted']]
    return {'n': len(ids), 'accepted': len(acc), 'accept_rate': P.rate(len(acc), len(ids)),
            'rejected': len(rej),
            'rejected_by_layer': dict(collections.Counter(str(res[i]['layer']) for i in rej)),
            'tip_fired_model_TIP': sum(1 for i in ids if res[i].get('model_tip')),
            'tip_fired_any': sum(1 for i in ids if res[i].get('tip') or res[i].get('model_tip')),
            'ids': sorted(ids)}


def passive_block(by, res, lab, tag_of, source):
    """The PASSIVE cells over the JUDGED-CORRECT items: `by` and `agentless` SEPARATELY."""
    corr = [i for i in by if lab[i][0] == 'correct']
    acc = {i for i in corr if res[i]['accepted']}
    tagged = [i for i in corr if tag_of(i) in ('by', 'agentless')]
    rest = [i for i in corr if tag_of(i) not in ('by', 'agentless')]
    out = {'source_of_the_tag': source, 'judged_correct_items': len(corr)}
    for tag in ('by', 'agentless'):
        out[tag] = passive_cell([i for i in corr if tag_of(i) == tag], res)
    out['untagged'] = passive_cell(rest, res)
    out['coverage_all_judged_correct'] = P.rate(len(acc), len(corr))
    out['coverage_without_passive_items'] = P.rate(len([i for i in rest if i in acc]), len(rest))
    out['coverage_passive_items_only'] = P.rate(len([i for i in tagged if i in acc]), len(tagged))
    return out


def guard_delta(by, lab, res_on, res_off, name):
    """caught / caught uniquely / cost of a guard, as the ROUTING difference on/off."""
    caught = [i for i in by if lab[i][0] == 'wrong' and res_off[i]['accepted']
              and not res_on[i]['accepted']]
    cost = [i for i in by if lab[i][0] == 'correct' and res_off[i]['accepted']
            and not res_on[i]['accepted']]
    return {'guard': name, 'caught_wrong_uniquely': len(caught), 'caught_ids': sorted(caught),
            'cost_correct_rejected': len(cost), 'cost_ids': sorted(cost),
            'basis': 'the same stack with the guard on vs off; "uniquely" = no other layer rejects it'}


def f8_shadow(by, lab, g, res_head, res_on, m_on, name):
    """COST / CATCHES / UNIQUE of an F8 module that decides NOTHING in the headline."""
    def rejects(i):
        return (g[i]['f8'] or {}).get('verdict') == 'reject'
    cost = sorted(i for i in by if lab[i][0] == 'correct' and rejects(i))
    catches = sorted(i for i in by if lab[i][0] == 'wrong' and rejects(i))
    unique = sorted(i for i in catches if res_head[i]['accepted'])
    return {'module': name, 'decides': False,
            'headline_under_this_guard': {'coverage': m_on['coverage'], 'fa': m_on['fa'],
                                          'fa_by_type': m_on['fa_by_type']},
            'reject_readouts': sum(1 for i in by if rejects(i)),
            'COST_judged_correct_it_would_reject': len(cost), 'cost_ids': cost,
            'CATCHES_judged_wrong_it_would_reject': len(catches), 'catch_ids': catches,
            'UNIQUE_caught_by_no_other_layer': len(unique), 'unique_ids': unique,
            'unique_definition': 'judged wrong, this readout rejects it, and the HEADLINE stack '
                                 '(every other layer incl. L3) accepts it',
            'routing_delta': guard_delta(by, lab, res_on, res_head, name)}


def released_fixed(st, recs, by, res, lab, lock_rej, l3):
    """§11 counter fix: released = L2-lock-rejected under BASE *and* L3-eligible under LOCKTIP."""
    rel = sorted(set(lock_rej) & set(l3))
    wr = collections.Counter()
    corr = 0
    for i in rel:
        if lab[i][0] == 'correct':
            corr += 1
        else:
            wr[lab[i][1] or '?'] += 1
    return {'definition': 'rejected by the lock at L2 under BASE AND L3-eligible under LOCKTIP '
                          '(a change of ROUTING, not of the final verdict)',
            'rejected_at_L2_under_BASE': len(lock_rej), 'l3_eligible_under_LOCKTIP': len(l3),
            'released_total': len(rel),
            'released_accepted': sum(1 for i in rel if res[i]['accepted']),
            'released_judged_correct': corr,
            'released_judged_correct_accepted': sum(1 for i in rel if lab[i][0] == 'correct'
                                                    and res[i]['accepted']),
            'released_judged_wrong_by_type': dict(wr),
            'released_judged_wrong_accepted_by_type': dict(collections.Counter(
                lab[i][1] or '?' for i in rel if lab[i][0] == 'wrong' and res[i]['accepted'])),
            'released_ids': rel}


def judge_noise(labels, controls):
    dis, tdis, n, tn = [], [], 0, 0
    for iid, rows in (controls or {}).items():
        if iid not in labels:
            continue
        j, t = labels[iid]
        for cj, ct in rows:
            n += 1
            if cj != j:
                dis.append(iid)
                continue
            if j == 'wrong':
                tn += 1
                if ct != t:
                    tdis.append(iid)
    return {'controls_compared': n, 'judged_disagreements': P.rate(len(dis), n),
            'type_comparisons': tn, 'type_disagreements': P.rate(len(tdis), tn),
            'judged_disagreement_ids': sorted(set(dis)), 'type_disagreement_ids': sorted(set(tdis)),
            'caveat': 'same-session duplicates bound within-session inconsistency only'}


def spend():
    s = dict(RL.token_spend())
    s.pop('phase_budget_remaining_estimate', None)        # 1L's hard-wired -667 base, stale
    s['phase_cap_1n'] = PHASE_CAP_1N
    s['counted_calls_phase1n'] = counted_local()
    s['remaining_under_1n_cap'] = PHASE_CAP_1N - s['counted_calls_phase1n']
    s['price'] = {'in_per_1M': 0.25, 'out_per_1M': 1.50}
    return s


# ================================================================== the post-transport path
def score_and_report(sel, st, recs, ann, by, info, lock_rej, l3, vm, labels, controls, lmeta,
                     req, need, made, no_verdict, unlabelled, fh, outdir, stem, title, side_tag):
    """Everything --final does AFTER transport. Shared with --selftest-final (0 calls)."""
    os.makedirs(outdir, exist_ok=True)
    jpass = (lmeta or {}).get('passive_by_item') or {}

    # ---- F8 readouts: BOTH modules; neither decides in the headline
    select_f8('f8')
    g_v1 = R1K.guard_readouts(recs, ann, sel['f9_strict'])
    select_f8('f8v2')
    g_v2 = R1K.guard_readouts(recs, ann, sel['f9_strict'])
    guards = {i: {'f8': None, 'f9': g_v1[i]['f9']} for i in g_v1}     # F8 CANNOT decide

    res = R1K.configure_row(st, recs, vm, True, guards, False, sel['f9'], sel['tip_reject'])
    RL.RES_VM[0] = vm
    lab = {i: labels.get(i, (by[i]['judged'], by[i]['wrong_type'])) for i in by}
    m = RL.col_metrics(recs, res, labels)
    say('[%s] coverage %s' % (stem.upper(), RL._r(m['coverage'])))
    say('[%s] FA       %s' % (stem.upper(), RL._r(m['fa'])))
    say('[%s] FA T     %s' % (stem.upper(), RL._r(m['fa_by_type']['T'])))

    # ---- named cells
    tf = cell_by_intent(by, res, lab, 'TF', False)
    tf['floor_line'] = 'the cell needs n >= 150 judged-wrong TF items'
    tf['floor_n_ge_150'] = tf['judged_wrong'] >= 150
    cells = {'TIME-FRAME (writer intent TF, judged wrong)': tf}
    if any(by[i].get('intent') == 'V' for i in by):
        cells['AGENT-DEMOTION (writer intent V, judged wrong)'] = cell_by_intent(
            by, res, lab, 'V', True)

    passive = {
        'by_writer_tag': passive_block(by, res, lab, lambda i: by[i].get('passive'),
                                       'the writer key `passive` on the item'),
        'by_judge_tag': passive_block(by, res, lab, lambda i: jpass.get(i),
                                      'the judge row key `passive`'),
        'writer_vs_judge_tag_agreement': dict(collections.Counter(
            '%s/%s' % (by[i].get('passive'), jpass.get(i)) for i in by if lab[i][0] == 'correct'))}

    # ---- §5 continuity block (needs RES_VM), then the carried counters
    try:
        sec5 = RL.section5(side_tag, st, recs, ann, by, res, guards, labels, sel, lock_rej,
                           info, info)
    except Exception as e:
        sec5 = {'error': '1L section5 did not apply to this side: %s' % e}

    base_res = R1K.configure_row(st, recs, {}, False, guards, False, False, sel['tip_reject'])
    lock_r = R1K.configure_row(st, recs, {}, True, guards, False, False, sel['tip_reject'])
    old_inert = [i for i in by if lock_r[i]['accepted'] and not base_res[i]['accepted']]
    rel = released_fixed(st, recs, by, res, lab, lock_rej, l3)
    rel['old_inert_counter_released_by_LOCKTIP_total'] = len(old_inert)
    say('[§5.1] released (fixed counter) %d of %d L2 lock rejections; old inert counter %d'
        % (rel['released_total'], len(lock_rej), len(old_inert)))
    mistake_l2 = [i for i in by if by[i]['chk']['step'] == 'mistake'
                  and i not in set(rel['released_ids'])]
    try:
        bug3 = sec5['unpatched_guard_bugs_5_4']['3 F2B not applied to lock-released items']
    except Exception:
        bug3 = None
    carried = {
        'released_by_LOCKTIP_total (inert accept-flip counter) — UNPATCHED': {
            'counted_not_patched': True, 'count': len(old_inert),
            'definition': 'items accepted under LOCKTIP but not under BASE (an accept-flip); inert '
                          'because a released item usually still fails elsewhere',
            'beside_it_the_fixed_routing_counter': rel['released_total']},
        'F2B not applied to lock-released items': {
            'counted_not_patched': True,
            'counter_A_routing_proxy_carried_bugs': rel['released_total'],
            'counter_B_section5_bug3_inert_accept_flip': bug3,
            'ids': rel['released_ids'],
            'measured_as': 'F2B is not separately callable offline (1L and 1M measured the same '
                           'proxy): every lock-released item is an item F2B never sees. The two 1M '
                           'counters disagree because bug3 reuses the inert accept-flip definition; '
                           'both are carried UNPATCHED under explicit names.'},
        'an L2 step=="mistake" rejection is not released': {
            'counted_not_patched': True, 'count': len(mistake_l2),
            'sids': sorted({by[i]['sid'] for i in mistake_l2}), 'ids': sorted(mistake_l2),
            'measured_as': 'records whose computed chk step is "mistake" (rejected at L2) and which '
                           'the lock release does not reach'},
        'reference hygiene — the NULL, unpatched': {
            'counted_not_patched': True, 'hygiene_applied': False,
            'hygiene_dir_present': os.path.isdir(RL.HYG), 'hygiene_dir': RL.HYG,
            'chk_distribution_before': info['chk_distribution'],
            'chk_distribution_after': info['chk_distribution'],
            'measured_as': 'phase1n/hygiene does not exist, so runner_1l.hygiene_patches returns '
                           'nothing and hygiene is silently OFF: chk before == chk after, 0 '
                           'references removed or replaced. Stated, not left implicit.'}}

    # ---- shadows (they decide nothing)
    res_v1 = R1K.configure_row(st, recs, vm, True, g_v1, True, sel['f9'], sel['tip_reject'])
    res_v2 = R1K.configure_row(st, recs, vm, True, g_v2, True, sel['f9'], sel['tip_reject'])
    m_v1 = RL.col_metrics(recs, res_v1, labels)
    m_v2 = RL.col_metrics(recs, res_v2, labels)
    res_f9on = R1K.configure_row(st, recs, vm, True, g_v1, False, True, sel['tip_reject'])
    res_f9off = R1K.configure_row(st, recs, vm, True, g_v1, False, False, sel['tip_reject'])
    res_tipalt = R1K.configure_row(st, recs, vm, True, guards, False, sel['f9'],
                                   not sel['tip_reject'])
    m_f9on = RL.col_metrics(recs, res_f9on, labels)
    m_tipalt = RL.col_metrics(recs, res_tipalt, labels)
    shadow = {
        'F8v1-on': f8_shadow(by, lab, g_v1, res, res_v1, m_v1, 'f8'),
        'F8v2-on': f8_shadow(by, lab, g_v2, res, res_v2, m_v2, 'f8v2'),
        'F9-on': dict(guard_delta(by, lab, res_f9on, res_f9off, 'F9'),
                      headline_under_F9_on={'coverage': m_f9on['coverage'], 'fa': m_f9on['fa'],
                                            'fa_T': m_f9on['fa_by_type']['T']},
                      f9_reject_readouts=sum(1 for i in by
                                             if (g_v1[i]['f9'] or {}).get('verdict') == 'reject'),
                      note='shadow only — F9 is %s in the frozen config'
                           % ('ON' if sel['f9'] else 'OFF')),
        'TIP-off': {'setting': 'TIP-as-rejection %s' % ('off' if sel['tip_reject'] else 'on'),
                    'coverage': m_tipalt['coverage'], 'fa': m_tipalt['fa'],
                    'fa_by_type': m_tipalt['fa_by_type']}}

    # ---- §13 builder limit, §14 judge noise
    nm = []
    for r in recs:
        b = l1_nearmiss(r)
        if b:
            nm.append((r['item_id'], b))
    nm_ids = [i for i, _b in nm]
    nm_corr = [i for i in nm_ids if lab[i][0] == 'correct']
    nm_corr_rej = [i for i in nm_corr if not res[i]['accepted']]
    builder_limit = {
        'definition': 'not an exact L1 match, but the normalised answer is within total edit '
                      'distance <= 2 (<= 1 per token) of an accepted reference/variant = a '
                      'plausible production L1 accept (spelling_variant / fuzzy) that the computed '
                      'chk cannot produce',
        'near_misses': len(nm_ids),
        'len_mismatch_subset': sum(1 for _i, b in nm if b['len_mismatch']),
        'judged_correct': len(nm_corr),
        'judged_correct_rejected_downstream': len(nm_corr_rej),
        'coverage_understatement': P.rate(len(nm_corr_rej), m['coverage']['n']),
        'judged_wrong': len([i for i in nm_ids if lab[i][0] == 'wrong']),
        'why_offline_understates': 'the production checker accepts spelling_variant and fuzzy '
                                   'matches; neither tolerance is reproducible offline, so '
                                   'compute_chk never makes those L1 accepts and offline coverage '
                                   'UNDERSTATES production coverage by up to the figure above',
        'ids': sorted(nm_ids)}
    say('[§2.1 limit] %d L1 near-misses, %d judged correct, %d of those rejected downstream'
        % (len(nm_ids), len(nm_corr), len(nm_corr_rej)))
    noise = judge_noise(labels, controls)

    out = {'phase': '1N', 'side': side_tag, 'title': title, 'freeze_commit': fh,
           'frozen_config': sel,
           'prompt': {'id': sel['prompt'], 'voice_line': VOICE_SAME_LINE,
                      'diff': 'PROMPT_DIFF_1N.md'},
           'model': {'model': sel['model'], 'temperature': sel['temperature'],
                     'thinkingBudget': sel['thinkingBudget']},
           'preflight': {'lock_rejections_BASE': len(lock_rej), 'l3_eligible_LOCKTIP': len(l3)},
           'builder_2_1': {'chk_computed': info['chk_computed'],
                           'chk_distribution': info['chk_distribution'],
                           'passive_tags': info.get('passive_tags')},
           'metrics': m, 'cells': cells, 'passive_cells': passive,
           'lock_released_5_1_fixed': rel,
           'carried_bugs_counted_not_patched': carried, 'shadow_readouts': shadow,
           'builder_limit_2_1': builder_limit, 'judge_noise': noise, 'label_meta': lmeta,
           'unlabelled_items': unlabelled, 'no_verdict_items': no_verdict,
           'section5_1L_block': sec5,
           'calls': dict(spend(), planned_new=len(need), made=made, unique_requests=len(req),
                         reused=len(req) - len(need))}
    json.dump(out, open(os.path.join(outdir, 'results_%s.json' % stem), 'w'), indent=1,
              ensure_ascii=False)

    # ---------------- markdown
    t = ['# %s' % title, '',
         'Freeze commit `%s`. Config **%s / %s** (F8 decides NOTHING), model `%s`, temperature %s, '
         'thinkingBudget %s. Every figure is numerator/denominator, point and exact 95 %% '
         'Clopper-Pearson interval; columns are never averaged.'
         % (fh, sel['name'], sel['prompt'], sel['model'], sel['temperature'], sel['thinkingBudget']),
         '', '## Headline', '', '| metric | value |', '|---|---|',
         '| items | %d over %d sentences |' % (info['n_items'], info['n_sentences']),
         '| coverage | %s |' % RL._r(m['coverage']),
         '| coverage (kind C) | %s |' % RL._r(m['coverage_kindC']),
         '| false accepts | %s |' % RL._r(m['fa']), '']
    t += ['## FA by type', '', '| type | FA |', '|---|---|']
    t += ['| %s | %s |' % (ty, RL._r(m['fa_by_type'][ty])) for ty in TYPES]
    t += ['', '## FA and false rejections by layer', '', '| layer | FA | false rejections |',
          '|---|---|---|']
    for layer in sorted(set(m['fa_by_layer']) | set(m['fr_by_layer'])):
        t.append('| %s | %s | %s |' % (
            layer, RL._r(m['fa_by_layer'][layer]) if layer in m['fa_by_layer'] else '—',
            RL._r(m['fr_by_layer'][layer]) if layer in m['fr_by_layer'] else '—'))
    t += ['', '## Targets', '', '| target | on the point | on the interval |', '|---|---|---|']
    for k, v in m['targets'].items():
        t.append('| %s | %s | %s |' % (k, 'MET' if v['point'] else 'missed',
                                       'MET' if v['interval'] else 'missed'))
    t += ['', '## The named cells', '']
    for nm_, cell in cells.items():
        t += ['**%s** — accepted %d of %d judged wrong = %s; rejecting layers `%s`'
              % (nm_, cell['accepted'], cell['judged_wrong'], RL._r(cell['rate']),
                 json.dumps(cell['rejecting_layers'], sort_keys=True))]
        if 'floor_line' in cell:
            t += ['', '* floor: %s — n = %d, %s' % (cell['floor_line'], cell['judged_wrong'],
                                                    'MET' if cell['floor_n_ge_150'] else 'MISSED')]
        if 'by_form' in cell:
            t += ['', '| form | accepted / judged wrong | rate | rejecting layers |',
                  '|---|---|---|---|']
            for f, d in cell['by_form'].items():
                t.append('| %s | %d/%d | %s | `%s` |' % (f, d['accepted'], d['judged_wrong'],
                                                         RL._r(d['rate']),
                                                         json.dumps(d['rejecting_layers'],
                                                                    sort_keys=True)))
        t.append('')
    t += ['## PASSIVE cells (judged-correct items only)', '']
    for src in ('by_writer_tag', 'by_judge_tag'):
        blk = passive[src]
        t += ['**%s** (%s), %d judged-correct items'
              % (src, blk['source_of_the_tag'], blk['judged_correct_items']), '',
              '| tag | n | accepted | rejected | rejected by layer | TIP fired (model / any) |',
              '|---|---|---|---|---|---|']
        for tag in ('by', 'agentless', 'untagged'):
            d = blk[tag]
            t.append('| %s | %d | %s | %d | `%s` | %d / %d |'
                     % (tag, d['n'], RL._r(d['accept_rate']), d['rejected'],
                        json.dumps(d['rejected_by_layer'], sort_keys=True),
                        d['tip_fired_model_TIP'], d['tip_fired_any']))
        t += ['', '* coverage, all judged correct: %s' % RL._r(blk['coverage_all_judged_correct']),
              '* coverage WITHOUT the passive items: %s'
              % RL._r(blk['coverage_without_passive_items']),
              '* coverage of the passive items only: %s'
              % RL._r(blk['coverage_passive_items_only']), '']
    t += ['## §5.1 the counter fix (routing, not verdicts)', '',
          '* rejected at L2 under BASE: **%d**; L3-eligible under LOCKTIP: **%d**'
          % (rel['rejected_at_L2_under_BASE'], rel['l3_eligible_under_LOCKTIP']),
          '* released (both): **%d**, of which accepted **%d**, judged correct %d, judged wrong '
          'by type `%s`'
          % (rel['released_total'], rel['released_accepted'], rel['released_judged_correct'],
             json.dumps(rel['released_judged_wrong_by_type'], sort_keys=True)),
          '* the OLD inert counter `released_by_LOCKTIP_total`, carried UNPATCHED: **%d**'
          % len(old_inert), '',
          '## Carried bugs (counted, NOT patched)', '',
          '* `released_by_LOCKTIP_total` (inert accept-flip): **%d**, beside the fixed routing '
          'counter **%d**.' % (len(old_inert), rel['released_total']),
          '* F2B never sees the lock-released items — counter A (routing proxy) **%d**, counter B '
          '(section5 bug3, inert accept-flip) **%s**; the two disagree and both are carried.'
          % (rel['released_total'], json.dumps(bug3) if bug3 is not None else 'not computed'),
          '* %d records whose chk step is "mistake" are rejected at L2 and not released.'
          % len(mistake_l2),
          '* reference hygiene: NOT applied (phase1n/hygiene present: %s) — chk before == chk '
          'after, `%s`.' % (os.path.isdir(RL.HYG),
                            json.dumps(info['chk_distribution'], sort_keys=True)), '',
          '## The builder limit (§2.1)', '',
          '* %d L1 near-misses (%d of them token-count mismatches), %d judged correct, %d of those '
          'rejected downstream = coverage understatement %s.'
          % (builder_limit['near_misses'], builder_limit['len_mismatch_subset'],
             builder_limit['judged_correct'], builder_limit['judged_correct_rejected_downstream'],
             RL._r(builder_limit['coverage_understatement'])),
          '* %s' % builder_limit['why_offline_understates'],
          '* %d near-misses are judged wrong (an L1 accept there would be a false accept).'
          % builder_limit['judged_wrong'], '',
          '## Judge noise (controls vs the part labels)', '',
          '* %d control comparisons; judged disagreements %s; type disagreements %s.'
          % (noise['controls_compared'], RL._r(noise['judged_disagreements']),
             RL._r(noise['type_disagreements'])), '',
          '## Shadow readouts (they decide nothing)', '']
    for k in ('F8v1-on', 'F8v2-on'):
        s8 = shadow[k]
        t.append('* **%s**: COST %d judged-correct items it would reject, CATCHES %d judged-wrong, '
                 'of which UNIQUE %d (rejected by no other layer incl. L3); headline under it '
                 'coverage %s, FA %s.'
                 % (k, s8['COST_judged_correct_it_would_reject'],
                    s8['CATCHES_judged_wrong_it_would_reject'],
                    s8['UNIQUE_caught_by_no_other_layer'],
                    RL._r(s8['headline_under_this_guard']['coverage']),
                    RL._r(s8['headline_under_this_guard']['fa'])))
    t += ['* **F9-on**: caught uniquely %d wrong, cost %d correct; coverage %s, FA %s.'
          % (shadow['F9-on']['caught_wrong_uniquely'], shadow['F9-on']['cost_correct_rejected'],
             RL._r(m_f9on['coverage']), RL._r(m_f9on['fa'])),
          '* **TIP-off** (%s): coverage %s, FA %s.'
          % (shadow['TIP-off']['setting'], RL._r(m_tipalt['coverage']), RL._r(m_tipalt['fa'])), '',
          '## Calls', '',
          '* unique requests %d, reused %d, new %d; counted calls in phase1n %d of cap %d; items '
          'without a verdict %d (a counted failure is never guessed).'
          % (len(req), len(req) - len(need), len(need), counted_local(), PHASE_CAP_1N,
             len(no_verdict)),
          '* spend at $0.25 in / $1.50 out per 1M tokens: `%s`'
          % json.dumps({k: v for k, v in spend().items()
                        if 'cost' in k or 'token' in k or 'spend' in k}, sort_keys=True), '']
    open(os.path.join(outdir, 'results_%s.md' % stem), 'w', encoding='utf-8').write('\n'.join(t))
    say('-- written %s/results_%s.json and results_%s.md' % (os.path.basename(outdir), stem, stem))
    return out, m


# ================================================================== the CLOSED 1M side
def fresh1m_side(purpose):
    """The closed Phase 1M side, re-built from phase1m/data (read-only), logged into phase1n."""
    return build_side_1n(purpose, False, M_DATA, 'fresh1m')


def fresh1m_labels(purpose):
    return LM.load_labels(purpose, caller='runner_1n.py', judge_dir=M_JUDGE, types=TYPES_1M)


# ================================================================== modes
def run_dev(args):
    cfg, sel = load_cfg({'f8': args.f8, 'f9': args.f9, 'tip': args.tip})
    select_f8(sel['f8_module'])
    say('== Phase 1N DEV re-score — %s (F8 %s, F9 %s, TIP-as-rejection %s), prompt %s, 0 new calls'
        % (sel['name'], sel['f8_module'], 'on' if sel['f9'] else 'off',
           'on' if sel['tip_reject'] else 'off', DEV_PROMPT))
    out = {'mode': 'dev', 'config': sel, 'dev_prompt': DEV_PROMPT, 'sides': {}}
    os.environ['PHASE1J_FINAL'] = os.environ.get('PHASE1J_FINAL', '1')
    os.environ['PHASE1K_OPEN_FRESH'] = '1'
    hyg0 = RL.HYG
    for side in ('dev', 'replay1j', 'fresh1l', 'fresh1m'):
        purpose = 'Phase 1N DEV re-score of the CLOSED side %s (zero new calls)' % side
        try:
            if side == 'fresh1m':
                RL.HYG = hyg0
                st, recs, ann, by, info = fresh1m_side(purpose)
                labels, _ctl, _lm = fresh1m_labels(purpose)
            elif side == 'fresh1l':
                RL.HYG = os.path.join(P1L, 'hygiene')
                st, recs, ann, by, info = RL.build_side('fresh', True, purpose)
                labels, _kr, _v = R1K.judge_labels('fresh', purpose)
            else:
                RL.HYG = hyg0
                st, recs, ann, by, info = RL.build_side(side, False, purpose)
                labels, _kr, _v = R1K.judge_labels({'dev': 'dev', 'replay1j': 'holdout1j'}[side],
                                                   purpose)
        except Exception as e:
            say('[%s] SKIPPED: %s' % (side.upper(), e))
            out['sides'][side] = {'error': str(e)}
            continue
        finally:
            RL.HYG = hyg0
        for r in recs:
            if r['item_id'] in labels:
                r['judged'], r['wrong_type'] = labels[r['item_id']]
        lock_rej, l3 = RL.lock_counts(st, recs)
        say('[%s] L2 lock firings under BASE: %d   L3-eligible under LOCKTIP: %d'
            % (side.upper(), len(lock_rej), len(l3)))
        req = plan_1n(st, recs, l3, DEV_PROMPT, side)
        hmap = RL.hashes_for(st, recs, l3, DEV_PROMPT)
        rep, ver, failed, _cl = RL.ledger_state()
        miss = [h for h in req if h not in ver and h not in failed]
        if miss:
            say('[%s] CACHE MISS %d prompts — reported, NOT called (dev makes no call)'
                % (side.upper(), len(miss)))
        vm = {i: ver[h] for i, h in hmap.items() if h in ver}
        guards = R1K.guard_readouts(recs, ann, sel['f9_strict'])
        res = R1K.configure_row(st, recs, vm, sel['locktip'], guards, sel['f8'], sel['f9'],
                                sel['tip_reject'])
        m = RL.col_metrics(recs, res, labels)
        say('[%s] coverage %s' % (side.upper(), RL._r(m['coverage'])))
        say('[%s] FA       %s' % (side.upper(), RL._r(m['fa'])))
        say('[%s] FA T     %s' % (side.upper(), RL._r(m['fa_by_type']['T'])))
        row = {'coverage': m['coverage'], 'fa': m['fa'], 'fa_by_type': m['fa_by_type'],
               'fa_by_layer': {k: v['k'] for k, v in m['fa_by_layer'].items()},
               'fr_by_layer': {k: v['k'] for k, v in m['fr_by_layer'].items()},
               'lock_rejections_BASE': len(lock_rej), 'l3_eligible': len(l3),
               'verdicts_found': len(vm), 'cache_misses_not_called': len(miss),
               'n_items': m['n_items']}
        # --- per-side F8 shadow readouts (they decide NOTHING; COST/CATCHES under the OLD labels)
        _f8_keep = getattr(R1K, 'f8', None)
        ids_sh = [i for i in by if i in labels and i in res]
        lab_sh = {i: labels[i] for i in ids_sh}
        shadows = {}
        for _mod, _key in (('f8', 'F8v1-on'), ('f8v2', 'F8v2-on')):
            select_f8(_mod)
            _g = R1K.guard_readouts(recs, ann, sel['f9_strict'])
            _res = R1K.configure_row(st, recs, vm, sel['locktip'], _g, True, sel['f9'],
                                     sel['tip_reject'])
            _m = RL.col_metrics(recs, _res, labels)
            shadows[_key] = f8_shadow(ids_sh, lab_sh, _g, res, _res, _m, _mod)
            say('[%s] %s  COST %d  CATCHES %d  UNIQUE %d  rejects %d  -> cov %s FA %s (readout only)'
                % (side.upper(), _key, shadows[_key]['COST_judged_correct_it_would_reject'],
                   shadows[_key]['CATCHES_judged_wrong_it_would_reject'],
                   shadows[_key]['UNIQUE_caught_by_no_other_layer'],
                   shadows[_key]['reject_readouts'],
                   RL._r(_m['coverage']), RL._r(_m['fa'])))
        if _f8_keep is not None:
            R1K.f8 = _f8_keep          # select_f8('none') does NOT rebind: restore explicitly
        else:
            select_f8(sel['f8_module'])
        row['f8_shadow_readouts'] = shadows
        row['labelled_items_in_shadow'] = len(ids_sh)
        exp = {'dev': DEV_EXP, 'replay1j': REPLAY_EXP, 'fresh1m': FRESH1M_EXP}.get(side)
        if exp:
            got = {'coverage': (m['coverage']['k'], m['coverage']['n']),
                   'fa': (m['fa']['k'], m['fa']['n']),
                   'fa_T': (m['fa_by_type']['T']['k'], m['fa_by_type']['T']['n'])}
            got = {k: got[k] for k in exp}
            row['expected'] = {k: '%d/%d' % v for k, v in exp.items()}
            row['observed'] = {k: '%d/%d' % v for k, v in got.items()}
            row['matches'] = all(got[k] == tuple(v) for k, v in exp.items())
            say('[%s] expected %s   observed %s   -> %s'
                % (side.upper(), json.dumps(row['expected']), json.dumps(row['observed']),
                   'MATCH' if row['matches'] else 'MISMATCH'))
        out['sides'][side] = row
    checked = [s for s in ('dev', 'replay1j') if 'matches' in out['sides'].get(s, {})]
    out['reproduces_phase1l'] = bool(checked) and all(out['sides'][s]['matches'] for s in checked)
    out['reproduces_phase1m'] = bool(out['sides'].get('fresh1m', {}).get('matches'))
    out['reproduction_scope'] = ('1L is valid only with --f8 f8 --f9 on --tip reject; 1M is valid '
                                 'only with --f8 f8v2 (the 1M frozen config)')
    say('== PHASE 1L REPRODUCED: %s   PHASE 1M REPRODUCED: %s (%s)'
        % (out['reproduces_phase1l'], out['reproduces_phase1m'], out['reproduction_scope']))
    json.dump(out, open(os.path.join(HERE, 'dev_regression_1n_%s.json' % (args.f8 or 'cfg')), 'w'),
              indent=1, ensure_ascii=False)
    say('-- written phase1n/dev_regression_1n_%s.json (0 new model calls)' % (args.f8 or 'cfg'))
    return out


def run_selftest_final(args):
    """Drive the ENTIRE post-transport --final path over the closed 1M side. 0 calls."""
    cfg, sel = load_cfg()
    select_f8('f8')
    purpose = 'Phase 1N SELFTEST of the --final post-transport path on the closed 1M side (0 calls)'
    say('== Phase 1N SELFTEST-FINAL — %s / %s (0 calls, fresh1m data + stored verdicts)'
        % (sel['name'], sel['prompt']))
    st, recs, ann, by, info = fresh1m_side(purpose)
    lock_rej, l3 = preflight_1n(st, recs, 'SELFTEST/fresh1m')
    req = plan_1n(st, recs, l3, DEV_PROMPT, 'selftest')       # the STORED prompt: 0 calls
    hmap = RL.hashes_for(st, recs, l3, DEV_PROMPT)
    rep, ver, failed, _cl = RL.ledger_state()
    vm = {i: ver[h] for i, h in hmap.items() if h in ver}
    no_verdict = sorted(i for i, h in hmap.items() if h not in ver)
    labels, controls, lmeta = fresh1m_labels(purpose)
    for r in recs:
        if r['item_id'] in labels:
            r['judged'], r['wrong_type'] = labels[r['item_id']]
    unlabelled = sorted(i for i in by if i not in labels)
    say('[SELFTEST] verdicts reused %d of %d L3-eligible; labels %d; judge passive tags %d'
        % (len(vm), len(l3), len(labels), lmeta.get('passive_tags_read', 0)))
    out, m = score_and_report(sel, st, recs, ann, by, info, lock_rej, l3, vm, labels, controls,
                              lmeta, req, [], {'selftest': True, 'ok': 0}, no_verdict, unlabelled,
                              '(selftest — no freeze)', SELFTEST, 'selftest',
                              'Phase 1N SELFTEST of the --final path (closed 1M side, 0 calls)',
                              'fresh1m')
    say('== SELFTEST done: coverage %s, FA %s. The 1M headline is NOT expected here — F8 decides '
        'nothing under the 1N config. Every post-transport block executed.'
        % (RL._r(m['coverage']), RL._r(m['fa'])))
    return out


def run_probe(args):
    """The NEW prompt on <=120 seeded-random L3-eligible 1M items of writer intent V."""
    cfg, sel = load_cfg()
    select_f8('f8')
    purpose = 'Phase 1N PROBE of P-FROZEN-1N on the closed 1M agent-demotion items'
    say('== Phase 1N PROBE — %s on <=120 1M intent-V items' % PROMPT_1N)
    st, recs, ann, by, info = fresh1m_side(purpose)
    lock_rej, l3 = preflight_1n(st, recs, 'PROBE/fresh1m')
    pool = sorted(i for i in l3 if by[i].get('intent') == 'V')
    rnd = random.Random(1730)
    rnd.shuffle(pool)
    ids = sorted(pool[:120])
    say('[PROBE] intent-V L3-eligible %d; sampled %d' % (len(pool), len(ids)))
    if not ids:
        raise SystemExit('STOP: no intent-V L3-eligible item on the 1M side, 0 calls made')
    req = plan_1n(st, recs, ids, PROMPT_1N, 'probe')
    h_new = RL.hashes_for(st, recs, ids, PROMPT_1N)
    h_old = RL.hashes_for(st, recs, ids, DEV_PROMPT)
    rep, ver, failed, _cl = RL.ledger_state()
    need = [h for h in req if h not in ver and h not in failed]
    done = counted_local()
    say('[PROBE] unique %d   reused %d   NEW %d   counted so far %d   cap %d'
        % (len(req), len(req) - len(need), len(need), done, PHASE_CAP_1N))
    cap_or_stop(need, done, 'probe')
    made = {'ok': 0, 'bad': 0, 'empty': 0, 'skipped': 0, 'wall': False}
    if need:
        made = make_calls(req, need)
        rep, ver, failed, _cl = RL.ledger_state()
    labels, _ctl, _lm = fresh1m_labels(purpose)
    rows, agree = [], 0
    for i in ids:
        old, new = ver.get(h_old[i]), ver.get(h_new[i])
        agree += int(old is not None and old == new)
        rows.append({'item_id': i, 'sid': by[i]['sid'], 'intent': by[i].get('intent'),
                     'form': by[i].get('form'), 'judged': (labels.get(i) or (None, None))[0],
                     'type': (labels.get(i) or (None, None))[1],
                     'old_prompt_verdict': old, 'new_prompt_verdict': new,
                     'sk': by[i]['sk'], 'answer': by[i]['answer']})
    flips = dict(collections.Counter('%s->%s' % (r['old_prompt_verdict'], r['new_prompt_verdict'])
                                     for r in rows))
    out = {'mode': 'probe', 'prompt_old': DEV_PROMPT, 'prompt_new': PROMPT_1N,
           'voice_line': VOICE_SAME_LINE, 'n_pool_intent_V_l3': len(pool), 'n_sampled': len(ids),
           'agreement': P.rate(agree, len(ids)), 'transitions': flips, 'made': made,
           'calls': spend(), 'rows': rows}
    json.dump(out, open(os.path.join(HERE, 'probe_1n.json'), 'w'), indent=1, ensure_ascii=False)
    say('[PROBE] transitions %s' % json.dumps(flips, sort_keys=True))
    say('-- written phase1n/probe_1n.json')
    return out


def _plan_for(sel, purpose, hyg_on=False):
    st, recs, ann, by, info = build_side_1n(purpose, hyg_on)
    lock_rej, l3 = preflight_1n(st, recs, 'FRESH1N' + ('/after-hygiene' if hyg_on else ''))
    req = plan_1n(st, recs, l3, sel['prompt'], 'after' if hyg_on else 'main')
    hmap = RL.hashes_for(st, recs, l3, sel['prompt'])
    return st, recs, ann, by, info, lock_rej, l3, req, hmap


def run_dry(args):
    cfg, sel = load_cfg()
    select_f8('f8')
    purpose = 'Phase 1N DRY RUN of the new side: build, chk, preflight, plan (no labels, no calls)'
    say('== Phase 1N DRY RUN — %s / %s' % (sel['name'], sel['prompt']))
    st, recs, ann, by, info, lock_rej, l3, req, hmap = _plan_for(sel, purpose)
    rep, ver, failed, _cl = RL.ledger_state()
    need = [h for h in req if h not in ver and h not in failed]
    done = counted_local()
    say('[DRY] unique requests %d   reused %d   NEW %d   already counted in phase1n %d   cap %d'
        % (len(req), len(req) - len(need), len(need), done, PHASE_CAP_1N))
    body = ['# Phase 1N — DRY RUN (no judge label was read, no model call was made)', '',
            '* config: **%s / %s**, model `%s`, temperature %s, thinkingBudget %s; F8 decides '
            'NOTHING, F9 %s, TIP-as-rejection %s, arm %s'
            % (sel['name'], sel['prompt'], sel['model'], sel['temperature'], sel['thinkingBudget'],
               'on' if sel['f9'] else 'off', 'on' if sel['tip_reject'] else 'off', sel['arm']),
            '* items %d over %d sentences' % (info['n_items'], info['n_sentences']),
            '* chk distribution (COMPUTED, never asserted): `%s`'
            % json.dumps(info['chk_distribution'], sort_keys=True),
            '* chk steps: `%s`' % json.dumps(info['chk_computed'], sort_keys=True),
            '* L2 lock firings under BASE: **%d**   L3-eligible under LOCKTIP: **%d**'
            % (len(lock_rej), len(l3)),
            '* unique requests **%d**, reusable from a ledger %d, NEW **%d**'
            % (len(req), len(req) - len(need), len(need)),
            '* counted calls already in phase1n/calls.jsonl: %d; cap %d; headroom %d'
            % (done, PHASE_CAP_1N, PHASE_CAP_1N - done - len(need)),
            '* level spread: `%s`' % json.dumps(dict(collections.Counter(
                r['level'] for r in recs)), sort_keys=True),
            '* writer intents: `%s`' % json.dumps(dict(collections.Counter(
                str(r['intent']) for r in recs)), sort_keys=True),
            '* writer forms: `%s`' % json.dumps(dict(collections.Counter(
                str(r['form']) for r in recs)), sort_keys=True),
            '* writer passive tags: `%s`' % json.dumps(info.get('passive_tags'), sort_keys=True),
            '* hygiene: OFF (phase1n/hygiene present: %s)' % os.path.isdir(RL.HYG), '']
    open(os.path.join(HERE, 'DRY_RUN_1N.md'), 'w', encoding='utf-8').write('\n'.join(body))
    say('-- written phase1n/DRY_RUN_1N.md')
    if done + len(need) > PHASE_CAP_1N:
        say('[DRY] WARNING: the plan would exceed the phase cap — --final would STOP.')
    return {'planned_new': len(need), 'unique': len(req)}


def run_final(args):
    if os.path.exists(DONE):
        raise SystemExit('REFUSED: %s exists — the new side is measured once.' % DONE)
    fh = check_freeze_1n()
    cfg, sel = load_cfg()
    select_f8('f8')
    purpose = 'Phase 1N FINAL run of the frozen configuration on the new set'
    say('== Phase 1N FINAL — %s / %s   freeze %s' % (sel['name'], sel['prompt'], fh))

    st, recs, ann, by, info, lock_rej, l3, req, hmap = _plan_for(sel, purpose)
    rep, ver, failed, _cl = RL.ledger_state()
    need = [h for h in req if h not in ver and h not in failed]
    done = counted_local()
    say('[FINAL] unique requests %d   reused %d   NEW %d   counted so far %d   cap %d'
        % (len(req), len(req) - len(need), len(need), done, PHASE_CAP_1N))
    cap_or_stop(need, done, 'final')

    made = {'ok': 0, 'bad': 0, 'empty': 0, 'skipped': 0, 'wall': False}
    if need:
        made = make_calls(req, need)
        rep, ver, failed, _cl = RL.ledger_state()
    still = [h for h in req if h not in ver and h not in failed]
    if made.get('wall') or still:
        open(PAUSED, 'w', encoding='utf-8').write(json.dumps(
            {'why': 'the quota wall (5 consecutive fully-retried transport failures)'
                    if made.get('wall')
                    else 'requests still without a verdict or a counted failure',
             'unique_requests': len(req), 'still_without_verdict': len(still),
             'http200_this_run': made.get('ok', 0), 'transport_dead_this_run': made.get('bad', 0),
             'counted_calls_phase1n': counted_local(),
             'next': 'rerun --final; every stored verdict is reused by request hash. '
                     'NO judge label was read.'}, indent=1) + '\n')
        say('[PAUSED] %d requests without a verdict — %s written, no label read'
            % (len(still), PAUSED))
        raise SystemExit(3)

    # ---------------- every planned request now has a verdict or a counted failure: read the labels
    labels, controls, lmeta = LM.load_labels(purpose, caller='runner_1n.py')
    for r in recs:
        if r['item_id'] in labels:
            r['judged'], r['wrong_type'] = labels[r['item_id']]
    unlabelled = sorted(i for i in by if i not in labels)
    vm = {i: ver[h] for i, h in hmap.items() if h in ver}
    no_verdict = sorted(i for i, h in hmap.items() if h not in ver)
    out, m = score_and_report(sel, st, recs, ann, by, info, lock_rej, l3, vm, labels, controls,
                              lmeta, req, need, made, no_verdict, unlabelled, fh, HERE, '1n',
                              'Phase 1N — the new set under P-FROZEN-1N, measured once', SIDE_TAG)
    open(DONE, 'w', encoding='utf-8').write(json.dumps(
        {'phase': '1N', 'freeze_commit': fh, 'coverage': RL._r(m['coverage']),
         'fa': RL._r(m['fa']), 'counted_calls': counted_local()}, indent=1) + '\n')
    say('-- FINAL_RUN_DONE written: the new side is measured, once.')
    return out


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--dev', action='store_true')
    g.add_argument('--selftest-final', dest='selftest_final', action='store_true')
    g.add_argument('--probe', action='store_true')
    g.add_argument('--dry', action='store_true')
    g.add_argument('--final', action='store_true')
    ap.add_argument('--f8', choices=('f8', 'f8v2', 'none'))
    ap.add_argument('--f9', choices=('on', 'off'))
    ap.add_argument('--tip', choices=('reject', 'accept', 'both'))
    a = ap.parse_args()
    if not a.dev and (a.f8 or a.f9 or a.tip):
        raise SystemExit('REFUSED: overrides are accepted in --dev only; every other mode uses '
                         'FROZEN_CONFIG_1N.json')
    if a.dev:
        if a.tip == 'both':
            for t in ('reject', 'accept'):
                a.tip = t
                say('== TIP setting: %s' % t)
                run_dev(a)
        else:
            run_dev(a)
    elif a.selftest_final:
        run_selftest_final(a)
    elif a.probe:
        run_probe(a)
    elif a.dry:
        run_dry(a)
    else:
        run_final(a)


if __name__ == '__main__':
    main()
