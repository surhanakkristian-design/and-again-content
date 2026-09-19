#!/usr/bin/env python3
"""Phase 1M runner — the new 140-sentence set, measured ONCE.

Modes
  --dev    zero calls.  Replays sides dev / replay1j / fresh1l from stored records, stored
           verdicts (phase1j + phase1k ledgers + phase1l/calls.jsonl + phase1m/calls.jsonl) and
           stored judge labels.  With --f8 f8 --f9 on --tip reject it must reproduce Phase 1L
           (dev 182/189 and 12/301; replay1j 178/196, 15/294, 2/59).
  --dry    the new side only: load, compute chk, preflight, count the plan.  No labels, no calls.
           Writes DRY_RUN.md.
  --final  the one measurement.  Refuses without FREEZE_HASH / on a code drift / if FINAL_RUN_DONE
           exists.  Resumable: verdicts already in calls.jsonl are reused by request hash; a quota
           wall writes RUN_PAUSED.txt and exits 3 WITHOUT reading a single judge label.

Everything transport-, metric- and CP-related is imported from runner_1l (runner_1l.py in this
directory, byte-identical to phase1l's); only what the new formats changed is written here.
Model: gemini-3.1-flash-lite, temperature 0, thinkingBudget 0 (decided, not re-tested).
"""
import argparse, collections, json, os, random, subprocess, sys, threading
from concurrent.futures import ThreadPoolExecutor

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import loader_1l as L                                                          # noqa: E402
import runner_1l as RL                                                         # noqa: E402
import loader_1m as LM                                                         # noqa: E402

R1K, R, P, C = RL.R1K, RL.R, RL.P, RL.C
TYPES = RL.TYPES
TOFF = RL.TOFF
P1L = os.path.join(TOFF, 'phase1l')
REPO = RL.REPO

# ---- stored verdicts of every earlier phase are reusable read-only; ours is phase1m/calls.jsonl
RL.LEDGERS_RO = list(RL.LEDGERS_RO) + [os.path.join(P1L, 'calls.jsonl')]
CALLS = RL.CALLS                                    # phase1m/calls.jsonl (RL.HERE == phase1m)
FREEZE_HASH = RL.FREEZE_HASH                        # phase1m/FREEZE_HASH
FREEZE_FILES = os.path.join(HERE, 'FREEZE_FILES')
DONE = RL.DONE                                      # phase1m/FINAL_RUN_DONE
STOP_PRE = RL.STOP_PRE
STOP_PLAN = RL.STOP_PLAN
STOP_CHK = os.path.join(HERE, 'STOP_CHK.txt')
PAUSED = os.path.join(HERE, 'RUN_PAUSED.txt')
CFG_PATH = os.path.join(HERE, 'FROZEN_CONFIG_1M.json')
RUNLOG = os.path.join(HERE, 'run_1m.log')
PHASE_CAP_1M = 1600                                 # counted calls for the whole phase
PRICE_IN, PRICE_OUT = RL.PRICE_IN, RL.PRICE_OUT
DEV_EXP = {'coverage': (182, 189), 'fa': (12, 301)}
REPLAY_EXP = {'coverage': (178, 196), 'fa': (15, 294), 'fa_T': (2, 59)}
SIDE_TAG = 'fresh1m'


def say(line):
    print(line, flush=True)
    with open(RUNLOG, 'a', encoding='utf-8') as fh:
        fh.write(line + '\n')


def alog(side, what, n, purpose):
    LM._log(side, what, n, purpose, caller='runner_1m.py')


# ================================================================== config / guard modules
def load_cfg(overrides=None):
    if not os.path.exists(CFG_PATH):
        raise SystemExit('REFUSED: %s does not exist' % CFG_PATH)
    c = json.load(open(CFG_PATH, encoding='utf-8'))
    for k in ('f8_module', 'f9_decides', 'tip_reject', 'locktip', 'prompt', 'model',
              'temperature', 'thinkingBudget'):
        if k not in c:
            raise SystemExit('REFUSED: FROZEN_CONFIG_1M.json has no %r' % k)
    if not c['locktip']:
        raise SystemExit('REFUSED: locktip is frozen true')
    o = overrides or {}
    sel = {'prompt': c['prompt'], 'locktip': True, 'f8': True, 'f9_strict': False,
           'f8_module': o.get('f8') or c['f8_module'],
           'f9': (o['f9'] == 'on') if o.get('f9') else bool(c['f9_decides']),
           'tip_reject': (o['tip'] != 'accept') if o.get('tip') else bool(c['tip_reject']),
           'model': c['model'], 'temperature': c['temperature'], 'thinkingBudget': c['thinkingBudget']}
    sel['name'] = 'LOCKTIP+%s%s (TIP-as-rejection %s)' % (
        sel['f8_module'].upper(), '+F9' if sel['f9'] else '', 'on' if sel['tip_reject'] else 'off')
    return c, sel


def select_f8(name):
    """Bind the F8 implementation BY NAME onto R1K (runner_1l already bound phase1m/f8.py)."""
    if name == 'f8':
        mod = sys.modules.get('f8') or getattr(RL, 'f8', None)
        if mod is None:
            raise SystemExit('REFUSED: f8 module not importable')
    else:
        path = os.path.join(HERE, name + '.py')
        if not os.path.exists(path):
            raise SystemExit('REFUSED: F8 module %s does not exist yet (written in parallel)' % path)
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


def build_side_1m(purpose, hyg_on=False):
    """Replaces runner_1l.build_side's FRESH branch for the new file formats.

    The new sentences are NATIVELY arm B (explicit subjects): no prep_arm rewriting anywhere.
    reference / refs are derived from the annotation ('v', first entry = displayed reference),
    exactly as apply_hygiene promotes them.  chk is COMPUTED for every record with
    runner_1l.compute_chk after make_state — never asserted (that void-ed Phase 1k).
    """
    info = {'side': SIDE_TAG}
    sents = {int(s['sid']): s for s in LM.load_sentences(purpose, caller='runner_1m.py')}
    ann = LM.load_annotations(purpose, caller='runner_1m.py')
    items = LM.load_items(purpose, caller='runner_1m.py')
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
             'intent': it.get('intent'), 'form': it.get('form'), 'tags': dict(s.get('tags') or {}),
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
        patches, files = RL.hygiene_patches(SIDE_TAG, purpose)
        if patches:
            info['hygiene'] = RL.apply_hygiene(recs, ann, patches)
            info['hygiene_files'] = [os.path.basename(f) for f in files]
    try:
        st = R.make_state(recs, ann, ('F4v3',), side_tag=SIDE_TAG)
    except Exception as e:                                   # unknown side tag -> the 1k tag
        say('[BUILD] make_state(side_tag=%r) failed (%s); falling back to "fresh1k"' % (SIDE_TAG, e))
        st = R.make_state(recs, ann, ('F4v3',), side_tag='fresh1k')
    how = collections.Counter()
    dist = collections.Counter()
    for r in recs:
        r['chk'], h = RL.compute_chk(r)
        r['chk_missing'] = False
        how[h] += 1
        dist['%s/%s' % (r['chk']['verdict'], r['chk']['step'])] += 1
    info['chk_computed'] = dict(how)
    info['chk_distribution'] = dict(dist)
    info['n_items'] = len(recs)
    info['n_sentences'] = len({r['sid'] for r in recs})
    say('[BUILD] %d items / %d sentences   chk distribution %s'
        % (len(recs), info['n_sentences'], json.dumps(info['chk_distribution'], sort_keys=True)))
    acc = [r for r in recs if r['chk']['verdict'] in ('correct', 'correct_with_tip')]
    if len(dist) == 1 and len(acc) == len(recs):
        open(STOP_CHK, 'w', encoding='utf-8').write(json.dumps(
            {'why': 'every record carries the same ACCEPTING chk — the Phase 1k hard-wired-checker '
                    'defect; nothing was measured and no model call was made',
             'chk_distribution': info['chk_distribution'], 'n_items': len(recs)}, indent=1) + '\n')
        raise SystemExit('STOP: degenerate chk, %s written, 0 model calls made' % STOP_CHK)
    return st, recs, ann, {r['item_id']: r for r in recs}, info


def preflight_1m(st, recs, tag):
    lock_rej, l3 = RL.lock_counts(st, recs)
    say('L2 lock firings under BASE: %d   L3-eligible under LOCKTIP: %d' % (len(lock_rej), len(l3)))
    say('[PREFLIGHT %s] (reference numbers: DEV 65/318, 1j replay 310/336, 1L fresh side non-zero)'
        % tag)
    if not lock_rej or not l3:
        open(STOP_PRE, 'w', encoding='utf-8').write(json.dumps(
            {'tag': tag, 'lock_rejections_BASE': len(lock_rej), 'l3_eligible_LOCKTIP': len(l3),
             'why': 'degenerate side (the Phase 1k defect); no model call was made'}, indent=1) + '\n')
        raise SystemExit('STOP: preflight failed, %s written, 0 model calls made' % STOP_PRE)
    return lock_rej, l3


# ================================================================== freeze
def check_freeze_1m():
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
        raise SystemExit('REFUSED: these .py files are in phase1m but not in FREEZE_FILES: %s'
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
                ['git', 'rev-parse', '%s:translation-offline/phase1m/%s' % (h, f)],
                cwd=REPO, stderr=subprocess.DEVNULL).decode().strip()
        except subprocess.CalledProcessError:
            was = None
        if cur != was:
            bad.append({'file': f, 'now': cur[:12], 'at_freeze': (was or 'ABSENT')[:12]})
    if bad:
        raise SystemExit('REFUSED: phase1m code differs from FREEZE_HASH %s: %s'
                         % (h, json.dumps(bad)))
    say('[FREEZE] %d python files identical to commit %s' % (len(files), h))
    return h


# ================================================================== requests / transport
def plan_1m(st, recs, ids, prompt_id, tag):
    req = RL.plan_requests(st, recs, ids, prompt_id, tag)
    return {h: (s, u, g, hh, 'L-1M:%s' % tag, i) for h, (s, u, g, hh, _t, i) in req.items()}


def counted_local():
    n = 0
    if os.path.exists(CALLS):
        for row in R.ledger_rows(CALLS):
            if row.get('counted'):
                n += 1
    return n


def make_calls(req, need):
    """Transport exactly as 1L call_one; 5 consecutive fully-retried failures = quota wall."""
    keys = RL.load_keys()
    key = keys[0]
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
    random.Random(1).shuffle(todo)                 # one outage damages all cells equally
    with ThreadPoolExecutor(max_workers=6) as pool:
        for _ in pool.map(work, todo):
            pass
    say('[CALLS] http200 %d (empty replies %d)  transport-dead %d  skipped after the wall %d'
        % (st['ok'], st['empty'], st['bad'], st['skipped']))
    return st


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
    """A plausible PRODUCTION L1 accept (spelling_variant / fuzzy) that compute_chk cannot make.

    Not an exact L1 match, but the normalised answer is within total edit distance <= 2 of an
    accepted reference/variant with <= 1 edit per token.  When the token counts differ the
    per-token rule cannot be applied; those are kept separately (`len_mismatch`).
    """
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


def guard_delta(by, lab, res_on, res_off, name):
    """caught / caught uniquely / cost of a guard, as the ROUTING difference on/off."""
    caught = [i for i in by if lab[i][0] == 'wrong' and res_off[i]['accepted']
              and not res_on[i]['accepted']]
    cost = [i for i in by if lab[i][0] == 'correct' and res_off[i]['accepted']
            and not res_on[i]['accepted']]
    return {'guard': name, 'caught_wrong_uniquely': len(caught), 'caught_ids': sorted(caught),
            'cost_correct_rejected': len(cost), 'cost_ids': sorted(cost),
            'basis': 'the same stack with the guard on vs off; "uniquely" = no other layer rejects it'}


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
    s['phase_cap_1m'] = PHASE_CAP_1M
    s['counted_calls_phase1m'] = counted_local()
    s['remaining_under_1m_cap'] = PHASE_CAP_1M - s['counted_calls_phase1m']
    s['price'] = {'in_per_1M': 0.25, 'out_per_1M': 1.50}
    return s


# ================================================================== modes
def run_dev(args):
    cfg, sel = load_cfg({'f8': args.f8, 'f9': args.f9, 'tip': args.tip})
    select_f8(sel['f8_module'])
    say('== Phase 1M DEV regression — %s / %s (F8 %s, F9 %s, TIP-as-rejection %s), 0 new calls'
        % (sel['name'], sel['prompt'], sel['f8_module'], 'on' if sel['f9'] else 'off',
           'on' if sel['tip_reject'] else 'off'))
    out = {'mode': 'dev', 'config': sel, 'sides': {}}
    os.environ['PHASE1J_FINAL'] = os.environ.get('PHASE1J_FINAL', '1')
    os.environ['PHASE1K_OPEN_FRESH'] = '1'
    hyg0 = RL.HYG
    for side in ('dev', 'replay1j', 'fresh1l'):
        purpose = 'Phase 1M DEV-mode regression of the stored side %s (zero new calls)' % side
        try:
            if side == 'fresh1l':
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
        req = plan_1m(st, recs, l3, sel['prompt'], side)
        hmap = RL.hashes_for(st, recs, l3, sel['prompt'])
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
               'cache_misses_not_called': len(miss), 'n_items': m['n_items']}
        exp = {'dev': DEV_EXP, 'replay1j': REPLAY_EXP}.get(side)
        if exp:
            got = {'coverage': (m['coverage']['k'], m['coverage']['n']),
                   'fa': (m['fa']['k'], m['fa']['n']),
                   'fa_T': (m['fa_by_type']['T']['k'], m['fa_by_type']['T']['n'])}
            row['expected_1l'] = {k: '%d/%d' % v for k, v in exp.items()}
            row['observed'] = {k: '%d/%d' % v for k, v in got.items()}
            row['matches_1l'] = all(got[k] == tuple(v) for k, v in exp.items())
            say('[%s] Phase 1L expected %s   observed %s   -> %s'
                % (side.upper(), json.dumps(row['expected_1l']), json.dumps(row['observed']),
                   'MATCH' if row['matches_1l'] else 'MISMATCH'))
        out['sides'][side] = row
    checked = [s for s in ('dev', 'replay1j') if 'matches_1l' in out['sides'].get(s, {})]
    out['reproduces_phase1l'] = bool(checked) and all(out['sides'][s]['matches_1l'] for s in checked)
    out['reproduction_scope'] = ('valid only with --f8 f8 --f9 on --tip reject'
                                 if (args.f8, args.f9, args.tip) == ('f8', 'on', 'reject')
                                 else 'NOT the 1L configuration — the comparison is informational')
    say('== PHASE 1L REPRODUCED: %s (%s)' % (out['reproduces_phase1l'], out['reproduction_scope']))
    json.dump(out, open(os.path.join(HERE, 'dev_regression_1m.json'), 'w'), indent=1,
              ensure_ascii=False)
    say('-- written phase1m/dev_regression_1m.json (0 new model calls)')
    return out


def _plan_for(sel, purpose, hyg_on=False):
    st, recs, ann, by, info = build_side_1m(purpose, hyg_on)
    lock_rej, l3 = preflight_1m(st, recs, 'FRESH1M' + ('/after-hygiene' if hyg_on else ''))
    req = plan_1m(st, recs, l3, sel['prompt'], 'after' if hyg_on else 'main')
    hmap = RL.hashes_for(st, recs, l3, sel['prompt'])
    return st, recs, ann, by, info, lock_rej, l3, req, hmap


def run_dry(args):
    cfg, sel = load_cfg()
    select_f8(sel['f8_module'])
    purpose = 'Phase 1M DRY RUN of the new side: build, chk, preflight, plan (no labels, no calls)'
    say('== Phase 1M DRY RUN — %s / %s' % (sel['name'], sel['prompt']))
    st, recs, ann, by, info, lock_rej, l3, req, hmap = _plan_for(sel, purpose)
    rep, ver, failed, _cl = RL.ledger_state()
    need = [h for h in req if h not in ver and h not in failed]
    done = counted_local()
    say('[DRY] unique requests %d   reused %d   NEW %d   already counted in phase1m %d   cap %d'
        % (len(req), len(req) - len(need), len(need), done, PHASE_CAP_1M))
    body = ['# Phase 1M — DRY RUN (no judge label was read, no model call was made)', '',
            '* config: **%s / %s**, model `%s`, temperature %s, thinkingBudget %s'
            % (sel['name'], sel['prompt'], sel['model'], sel['temperature'], sel['thinkingBudget']),
            '* items %d over %d sentences' % (info['n_items'], info['n_sentences']),
            '* chk distribution (COMPUTED, never asserted): `%s`'
            % json.dumps(info['chk_distribution'], sort_keys=True),
            '* chk steps: `%s`' % json.dumps(info['chk_computed'], sort_keys=True),
            '* L2 lock firings under BASE: **%d**   L3-eligible under LOCKTIP: **%d**'
            % (len(lock_rej), len(l3)),
            '* unique requests **%d**, reusable from a ledger %d, NEW **%d**'
            % (len(req), len(req) - len(need), len(need)),
            '* counted calls already in phase1m/calls.jsonl: %d; cap %d; headroom %d'
            % (done, PHASE_CAP_1M, PHASE_CAP_1M - done - len(need)),
            '* level spread: `%s`' % json.dumps(dict(collections.Counter(
                r['level'] for r in recs)), sort_keys=True),
            '* writer intents: `%s`' % json.dumps(dict(collections.Counter(
                str(r['intent']) for r in recs)), sort_keys=True),
            '* writer forms: `%s`' % json.dumps(dict(collections.Counter(
                str(r['form']) for r in recs)), sort_keys=True), '']
    open(os.path.join(HERE, 'DRY_RUN.md'), 'w', encoding='utf-8').write('\n'.join(body))
    say('-- written phase1m/DRY_RUN.md')
    if done + len(need) > PHASE_CAP_1M:
        say('[DRY] WARNING: the plan would exceed the phase cap — --final would STOP.')
    return {'planned_new': len(need), 'unique': len(req)}


def run_final(args):
    if os.path.exists(DONE):
        raise SystemExit('REFUSED: %s exists — the new side is measured once.' % DONE)
    fh = check_freeze_1m()
    cfg, sel = load_cfg()
    select_f8(sel['f8_module'])
    purpose = 'Phase 1M FINAL run of the frozen configuration on the new 140-sentence set'
    say('== Phase 1M FINAL — %s / %s   freeze %s' % (sel['name'], sel['prompt'], fh))

    st, recs, ann, by, info, lock_rej, l3, req, hmap = _plan_for(sel, purpose)
    rep, ver, failed, _cl = RL.ledger_state()
    need = [h for h in req if h not in ver and h not in failed]
    done = counted_local()
    say('[FINAL] unique requests %d   reused %d   NEW %d   counted so far %d   cap %d'
        % (len(req), len(req) - len(need), len(need), done, PHASE_CAP_1M))
    if done + len(need) > PHASE_CAP_1M:
        open(STOP_PLAN, 'w', encoding='utf-8').write(json.dumps(
            {'planned_new_calls': len(need), 'already_counted': done, 'cap': PHASE_CAP_1M,
             'why': 'the plan exceeds the phase cap; nothing was trimmed and no call was made'},
            indent=1) + '\n')
        raise SystemExit('STOP: %d + %d > cap %d — %s written, 0 calls made'
                         % (done, len(need), PHASE_CAP_1M, STOP_PLAN))

    made = {'ok': 0, 'bad': 0, 'empty': 0, 'skipped': 0, 'wall': False}
    if need:
        made = make_calls(req, need)
        rep, ver, failed, _cl = RL.ledger_state()
    still = [h for h in req if h not in ver and h not in failed]
    if made.get('wall') or still:
        open(PAUSED, 'w', encoding='utf-8').write(json.dumps(
            {'why': 'the quota wall (5 consecutive fully-retried transport failures)' if made.get('wall')
                    else 'requests still without a verdict or a counted failure',
             'unique_requests': len(req), 'still_without_verdict': len(still),
             'http200_this_run': made.get('ok', 0), 'transport_dead_this_run': made.get('bad', 0),
             'counted_calls_phase1m': counted_local(),
             'next': 'rerun --final; every stored verdict is reused by request hash. '
                     'NO judge label was read.'}, indent=1) + '\n')
        say('[PAUSED] %d requests without a verdict — %s written, no label read' % (len(still), PAUSED))
        raise SystemExit(3)

    # ---------------- every planned request now has a verdict or a counted failure: read the labels
    labels, controls, lmeta = LM.load_labels(purpose, caller='runner_1m.py')
    for r in recs:
        if r['item_id'] in labels:
            r['judged'], r['wrong_type'] = labels[r['item_id']]
    unlabelled = sorted(i for i in by if i not in labels)
    vm = {i: ver[h] for i, h in hmap.items() if h in ver}
    no_verdict = sorted(i for i, h in hmap.items() if h not in ver)
    guards = R1K.guard_readouts(recs, ann, sel['f9_strict'])
    res = R1K.configure_row(st, recs, vm, True, guards, sel['f8'], sel['f9'], sel['tip_reject'])
    RL.RES_VM[0] = vm
    lab = {i: labels.get(i, (by[i]['judged'], by[i]['wrong_type'])) for i in by}
    m = RL.col_metrics(recs, res, labels)
    say('[FINAL] coverage %s' % RL._r(m['coverage']))
    say('[FINAL] FA       %s' % RL._r(m['fa']))
    say('[FINAL] FA T     %s' % RL._r(m['fa_by_type']['T']))

    # ---------------- the two named cells
    cells = {'AGENT-DEMOTION (writer intent V, judged wrong)':
             cell_by_intent(by, res, lab, 'V', True),
             'TIME-FRAME-SHIFT (writer intent TF, judged wrong)':
             cell_by_intent(by, res, lab, 'TF', False)}

    # ---------------- §11 counter fix + the old inert counter, §12 carried bugs
    base_res = R1K.configure_row(st, recs, {}, False, guards, False, False, sel['tip_reject'])
    lock_r = R1K.configure_row(st, recs, {}, True, guards, False, False, sel['tip_reject'])
    old_inert = [i for i in by if lock_r[i]['accepted'] and not base_res[i]['accepted']]
    rel = released_fixed(st, recs, by, res, lab, lock_rej, l3)
    rel['old_inert_counter_released_by_LOCKTIP_total'] = len(old_inert)
    say('[§5.1] released (fixed counter) %d of %d L2 lock rejections; old inert counter %d'
        % (rel['released_total'], len(lock_rej), len(old_inert)))
    mistake_l2 = [i for i in by if by[i]['chk']['step'] == 'mistake' and i not in set(rel['released_ids'])]
    carried = {
        'F2B not applied to lock-released items': {
            'counted_not_patched': True, 'released_items_F2B_never_sees': rel['released_total'],
            'ids': rel['released_ids'],
            'measured_as': 'F2B is not separately callable offline (1L measured the same proxy): '
                           'every lock-released item is an item F2B never sees'},
        'an L2 step=="mistake" rejection is not released': {
            'counted_not_patched': True, 'count': len(mistake_l2),
            'sids': sorted({by[i]['sid'] for i in mistake_l2}), 'ids': sorted(mistake_l2),
            'measured_as': 'records whose computed chk step is "mistake" (rejected at L2) and which '
                           'the lock release does not reach'}}

    # ---------------- §10 shadow readouts (they decide nothing)
    res_f9on = R1K.configure_row(st, recs, vm, True, guards, sel['f8'], True, sel['tip_reject'])
    res_f9off = R1K.configure_row(st, recs, vm, True, guards, sel['f8'], False, sel['tip_reject'])
    res_f8off = R1K.configure_row(st, recs, vm, True, guards, False, sel['f9'], sel['tip_reject'])
    res_tipalt = R1K.configure_row(st, recs, vm, True, guards, sel['f8'], sel['f9'],
                                   not sel['tip_reject'])
    m_f9on = RL.col_metrics(recs, res_f9on, labels)
    m_tipalt = RL.col_metrics(recs, res_tipalt, labels)
    shadow = {
        'a_F9_had_it_stayed_on': dict(
            guard_delta(by, lab, res_f9on, res_f9off, 'F9'),
            headline_under_F9_on={'coverage': m_f9on['coverage'], 'fa': m_f9on['fa'],
                                  'fa_T': m_f9on['fa_by_type']['T']},
            f9_reject_readouts=sum(1 for i in by if (guards[i]['f9'] or {}).get('verdict') == 'reject'),
            note='shadow only — F9 is %s in the frozen config' % ('ON' if sel['f9'] else 'OFF')),
        'b_the_other_TIP_setting': {
            'setting': 'TIP-as-rejection %s' % ('off' if sel['tip_reject'] else 'on'),
            'coverage': m_tipalt['coverage'], 'fa': m_tipalt['fa'],
            'fa_by_type': m_tipalt['fa_by_type']},
        'd_F8_active_module': dict(guard_delta(by, lab, res, res_f8off, sel['f8_module']),
                                   reject_readouts=sum(1 for i in by if (guards[i]['f8'] or {})
                                                       .get('verdict') == 'reject'))}
    if sel['f8_module'] != 'f8':
        try:
            select_f8('f8')
            g_v1 = R1K.guard_readouts(recs, ann, sel['f9_strict'])
            res_v1 = R1K.configure_row(st, recs, vm, True, g_v1, sel['f8'], sel['f9'],
                                       sel['tip_reject'])
            m_v1 = RL.col_metrics(recs, res_v1, labels)
            shadow['c_F8v1_in_place_of_%s' % sel['f8_module']] = {
                'fa': m_v1['fa'], 'fa_by_type': m_v1['fa_by_type'], 'coverage': m_v1['coverage'],
                'agent_demotion_cell': cell_by_intent(by, res_v1, lab, 'V', True),
                'items_whose_F8_readout_moved': sum(
                    1 for i in by if (g_v1[i]['f8'] or {}).get('verdict')
                    != (guards[i]['f8'] or {}).get('verdict'))}
        finally:
            select_f8(sel['f8_module'])
    else:
        shadow['c_F8v1_in_place_of_F8v2'] = 'not applicable — F8v1 IS the selected module'

    # ---------------- §13 builder limit, §14 judge noise
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
        'ids': sorted(nm_ids)}
    say('[§2.1 limit] %d L1 near-misses, %d judged correct, %d of those rejected downstream'
        % (len(nm_ids), len(nm_corr), len(nm_corr_rej)))
    noise = judge_noise(labels, controls)

    try:
        sec5 = RL.section5(SIDE_TAG, st, recs, ann, by, res, guards, labels, sel, lock_rej,
                           info, info)
    except Exception as e:
        sec5 = {'error': '1L section5 did not apply to this side: %s' % e}

    out = {'phase': '1M', 'side': SIDE_TAG, 'freeze_commit': fh, 'frozen_config': sel,
           'model': {'model': sel['model'], 'temperature': sel['temperature'],
                     'thinkingBudget': sel['thinkingBudget']},
           'preflight': {'lock_rejections_BASE': len(lock_rej), 'l3_eligible_LOCKTIP': len(l3)},
           'builder_2_1': {'chk_computed': info['chk_computed'],
                           'chk_distribution': info['chk_distribution']},
           'metrics': m, 'cells': cells, 'lock_released_5_1_fixed': rel,
           'carried_bugs_counted_not_patched': carried, 'shadow_readouts': shadow,
           'builder_limit_2_1': builder_limit, 'judge_noise': noise, 'label_meta': lmeta,
           'unlabelled_items': unlabelled, 'no_verdict_items': no_verdict,
           'section5_1L_block': sec5,
           'calls': dict(spend(), planned_new=len(need), made=made, unique_requests=len(req),
                         reused=len(req) - len(need))}
    json.dump(out, open(os.path.join(HERE, 'results_1m.json'), 'w'), indent=1, ensure_ascii=False)

    # ---------------- markdown
    t = ['# Phase 1M — the new 140-sentence set, measured once', '',
         'Freeze commit `%s`. Config **%s / %s**, model `%s`, temperature %s, thinkingBudget %s. '
         'Every figure is numerator/denominator, point and exact 95 %% Clopper-Pearson interval; '
         'columns are never averaged.'
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
    t += ['', '## The two named cells', '']
    for nm_, cell in cells.items():
        t += ['**%s** — accepted %d of %d judged wrong = %s; rejecting layers `%s`'
              % (nm_, cell['accepted'], cell['judged_wrong'], RL._r(cell['rate']),
                 json.dumps(cell['rejecting_layers'], sort_keys=True))]
        if 'by_form' in cell:
            t += ['', '| form | accepted / judged wrong | rate | rejecting layers |',
                  '|---|---|---|---|']
            for f, d in cell['by_form'].items():
                t.append('| %s | %d/%d | %s | `%s` |' % (f, d['accepted'], d['judged_wrong'],
                                                         RL._r(d['rate']),
                                                         json.dumps(d['rejecting_layers'],
                                                                    sort_keys=True)))
        t.append('')
    t += ['## §5.1 the counter fix (routing, not verdicts)', '',
          '* rejected at L2 under BASE: **%d**; L3-eligible under LOCKTIP: **%d**'
          % (rel['rejected_at_L2_under_BASE'], rel['l3_eligible_under_LOCKTIP']),
          '* released (both): **%d**, of which accepted **%d**, judged correct %d, '
          'judged wrong by type `%s`'
          % (rel['released_total'], rel['released_accepted'], rel['released_judged_correct'],
             json.dumps(rel['released_judged_wrong_by_type'], sort_keys=True)),
          '* the OLD inert counter, for continuity: **%d**' % len(old_inert), '',
          '## Carried bugs (counted, NOT patched)', '',
          '* F2B never sees the %d lock-released items.' % rel['released_total'],
          '* %d records whose chk step is "mistake" are rejected at L2 and not released.'
          % len(mistake_l2), '',
          '## The builder limit (§2.1)', '',
          '* %d L1 near-misses (%d of them token-count mismatches), %d judged correct, '
          '%d of those rejected downstream = coverage understatement %s.'
          % (builder_limit['near_misses'], builder_limit['len_mismatch_subset'],
             builder_limit['judged_correct'], builder_limit['judged_correct_rejected_downstream'],
             RL._r(builder_limit['coverage_understatement'])),
          '* %d near-misses are judged wrong (an L1 accept there would be a false accept).'
          % builder_limit['judged_wrong'], '',
          '## Judge noise (controls vs the part labels)', '',
          '* judged disagreements %s; type disagreements %s.'
          % (RL._r(noise['judged_disagreements']), RL._r(noise['type_disagreements'])), '',
          '## Shadow readouts (they decide nothing)', '',
          '* **F9 had it stayed on**: caught uniquely %d wrong, cost %d correct; coverage %s, '
          'FA %s.' % (shadow['a_F9_had_it_stayed_on']['caught_wrong_uniquely'],
                      shadow['a_F9_had_it_stayed_on']['cost_correct_rejected'],
                      RL._r(m_f9on['coverage']), RL._r(m_f9on['fa'])),
          '* **the other TIP setting** (%s): coverage %s, FA %s.'
          % (shadow['b_the_other_TIP_setting']['setting'], RL._r(m_tipalt['coverage']),
             RL._r(m_tipalt['fa'])),
          '* **%s**: caught uniquely %d wrong, cost %d correct.'
          % (sel['f8_module'], shadow['d_F8_active_module']['caught_wrong_uniquely'],
             shadow['d_F8_active_module']['cost_correct_rejected']), '',
          '## Calls', '',
          '* unique requests %d, reused %d, new %d; counted calls in phase1m %d of cap %d; '
          'items without a verdict %d (a counted failure is never guessed).'
          % (len(req), len(req) - len(need), len(need), counted_local(), PHASE_CAP_1M,
             len(no_verdict)),
          '* spend at $0.25 in / $1.50 out per 1M tokens: `%s`'
          % json.dumps({k: v for k, v in spend().items() if 'cost' in k or 'token' in k},
                       sort_keys=True), '']
    open(os.path.join(HERE, 'results_1m.md'), 'w', encoding='utf-8').write('\n'.join(t))
    say('-- written phase1m/results_1m.json and results_1m.md')
    open(DONE, 'w', encoding='utf-8').write(json.dumps(
        {'phase': '1M', 'freeze_commit': fh, 'coverage': RL._r(m['coverage']),
         'fa': RL._r(m['fa']), 'counted_calls': counted_local()}, indent=1) + '\n')
    say('-- FINAL_RUN_DONE written: the new side is measured, once.')
    return out


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--dev', action='store_true')
    g.add_argument('--dry', action='store_true')
    g.add_argument('--final', action='store_true')
    ap.add_argument('--f8', choices=('f8', 'f8v2', 'f8u'))
    ap.add_argument('--f9', choices=('on', 'off'))
    ap.add_argument('--tip', choices=('reject', 'accept', 'both'))
    a = ap.parse_args()
    if not a.dev and (a.f8 or a.f9 or a.tip):
        raise SystemExit('REFUSED: overrides are accepted in --dev only; --dry/--final use '
                         'FROZEN_CONFIG_1M.json')
    if a.dev:
        if a.tip == 'both':
            for t in ('reject', 'accept'):
                a.tip = t
                say('== TIP setting: %s' % t)
                run_dev(a)
        else:
            run_dev(a)
    elif a.dry:
        run_dry(a)
    else:
        run_final(a)


if __name__ == '__main__':
    main()
