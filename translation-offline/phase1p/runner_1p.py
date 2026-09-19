#!/usr/bin/env python3
"""Phase 1P runner — the 1N stack (LOCKTIP + TIP-as-rejection ON + F8 readout-only + F9 off,
prompt P-FROZEN-1N, arm B) plus levers 1-3.

    PYTHONDONTWRITEBYTECODE=1 python3 phase1p/runner_1p.py --preflight
    PYTHONDONTWRITEBYTECODE=1 python3 phase1p/runner_1p.py --dry-run
    PYTHONDONTWRITEBYTECODE=1 python3 phase1p/runner_1p.py --final
    PYTHONDONTWRITEBYTECODE=1 python3 phase1p/runner_1p.py --ablation
    PYTHONDONTWRITEBYTECODE=1 python3 phase1p/runner_1p.py --dev --lever N [--go] [--fa-n K]

Model gemini-3.1-flash-lite, temperature 0, thinkingBudget 0.  counted = HTTP 200 only; http
0/429/5xx is retried with backoff and logged counted:false; an empty 200 is a counted failure,
never retried, never guessed.  Transport, pacing, shuffle and the quota wall are runner_1n's.
"""
import argparse, collections, json, os, random, subprocess, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
TOFF = os.path.dirname(HERE)
P1N = os.path.join(TOFF, 'phase1n')
for _p in (HERE, P1N):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import runner_1n as R1N                                                        # noqa: E402
RL, R1K, R, P, C = R1N.RL, R1N.R1K, R1N.R, R1N.P, R1N.C

# ---- every path that runner_1l resolves against ITS OWN directory (phase1n) is moved to phase1p
RL.LEDGERS_RO = sorted(set(list(RL.LEDGERS_RO) + [
    os.path.join(TOFF, 'phase1l', 'calls.jsonl'), os.path.join(TOFF, 'phase1m', 'calls.jsonl'),
    os.path.join(P1N, 'calls.jsonl'), os.path.join(TOFF, 'phase1o', 'calls.jsonl')]))
CALLS = RL.CALLS = os.path.join(HERE, 'calls.jsonl')
RL.ACCESS = os.path.join(HERE, 'access_log.jsonl')
RL.HYG = os.path.join(HERE, 'hygiene')                     # absent on purpose -> hygiene off
FREEZE_HASH = RL.FREEZE_HASH = os.path.join(HERE, 'FREEZE_HASH')
DONE = RL.DONE = os.path.join(HERE, 'FINAL_RUN_DONE')
STOP_PRE = RL.STOP_PRE = os.path.join(HERE, 'STOP_PREFLIGHT.txt')
STOP_PLAN = RL.STOP_PLAN = os.path.join(HERE, 'STOP_PLAN.txt')
PAUSED = os.path.join(HERE, 'RUN_PAUSED.txt')
STOP_CHK = os.path.join(HERE, 'STOP_CHK.txt')
R1N.CALLS, R1N.STOP_PLAN, R1N.STOP_PRE, R1N.PAUSED = CALLS, STOP_PLAN, STOP_PRE, PAUSED
R1N.RUNLOG = os.path.join(HERE, 'run_1p.log')

import loader_1p as LM                                                         # noqa: E402
import lever1, lever2, lever3                                                  # noqa: E402

FREEZE_FILES = os.path.join(HERE, 'FREEZE_FILES')
CFG_PATH = os.path.join(HERE, 'FROZEN_CONFIG_1P.json')
RUNLOG = R1N.RUNLOG
PHASE_CAP_1P = 1400
DEV_CAP = 300
PREFLIGHT_STOP_AT = 1390
PROMPT_1P = 'P-FROZEN-1P'
PROMPT_1N = R1N.PROMPT_1N                                   # 'P-FROZEN-1N' — the lever-free prompt
SIDE_TAG = 'fresh1p'
FINAL_ITEMS_EXPECTED = 1080
N_DATA, N_JUDGE = os.path.join(P1N, 'data'), os.path.join(P1N, 'judge')


def say(line):
    print(line, flush=True)
    with open(RUNLOG, 'a', encoding='utf-8') as fh:
        fh.write(str(line) + '\n')


# ================================================================== the prompt
def build_req_1p(st, r, prompt_id):
    """P-FROZEN-1P = the P-FROZEN body + VOICE_SAME_LINE (1N's one change) + this record's lever
    2 / lever 3 lines, inserted at the same place the gender chain is inserted."""
    if prompt_id != PROMPT_1P:
        return R1N.build_req_1n(st, r, prompt_id)
    sysx, user, gcfg, _h = R1N._ORIG_BUILD_REQ(st, r, 'P-FROZEN')
    lines = user.split('\n')
    at = [k for k, ln in enumerate(lines) if ln == P.WORDING_LINE]
    if len(at) != 1:
        raise SystemExit('REFUSED: WORDING_LINE occurs %d times in the P-FROZEN body' % len(at))
    ins = [R1N.VOICE_SAME_LINE] + list(r.get('_extra') or [])
    lines = lines[:at[0] + 1] + ins + lines[at[0] + 1:]
    user = '\n'.join(lines)
    return sysx, user, gcfg, R.req_hash(sysx, user, gcfg)


R1K.build_req = build_req_1p
if PROMPT_1P not in tuple(getattr(R1K, 'PROMPTS', ())):
    R1K.PROMPTS = tuple(getattr(R1K, 'PROMPTS', ())) + (PROMPT_1P,)


# ================================================================== config
def load_cfg(levers=(1, 2, 3)):
    cfg = json.load(open(CFG_PATH, encoding='utf-8')) if os.path.exists(CFG_PATH) else {}
    if cfg.get('f8_decides') or (cfg.get('f8_module') or 'none') != 'none':
        raise SystemExit('REFUSED: F8 may not decide in 1P')
    if cfg.get('f9_decides'):
        raise SystemExit('REFUSED: F9 may not decide in 1P')
    if cfg.get('tip_reject') is False:
        raise SystemExit('REFUSED: TIP-as-rejection stays ON')
    sel = {'name': 'LOCKTIP+levers', 'prompt': PROMPT_1P, 'locktip': True, 'tip_reject': True,
           'f8': False, 'f9': False, 'f9_strict': False, 'arm': 'B',
           'model': P.MODEL, 'temperature': 0, 'thinkingBudget': 0,
           'levers': list(cfg.get('levers', levers))}
    return cfg, sel


# ================================================================== build
def attach_levers(recs, ann, levers):
    """Per-record prompt additions (lever 2 / lever 3).  0 model calls."""
    stats = collections.Counter()
    for r in recs:
        a = ann.get(str(r['sid'])) or {}
        extra, info = [], {}
        if 2 in levers:
            ls, fired = lever2.open_points(r['sk'], a, r['reference'], r['answer'])
            extra += ls
            info['lever2_fired'] = fired
            for f in fired:
                stats['l2:' + f] += 1
        if 3 in levers:
            ln, shown, removed = lever3.line(r['reference'], r.get('refs'))
            if ln:
                extra.append(ln)
            info['lever3'] = {'shown': shown, 'removed': removed}
            stats['l3:shown'] += len(shown)
            stats['l3:removed'] += len(removed)
            stats['l3:items_with_a_variant'] += 1 if shown else 0
        if 1 in levers:
            d = lever1.detect(r['sk'], a, r['answer'], r['reference'])
            info['lever1'] = d
            stats['l1:fired'] += 1 if d['fired'] else 0
            stats['l1:answer_is_agentless_passive'] += 1 if d['answer_is_agentless_passive'] else 0
        r['_extra'], r['_lev'] = extra, info
    return dict(stats)


def build_side(purpose, data_dir=None, side_tag=SIDE_TAG, levers=(1, 2, 3), loader=LM):
    """chk is COMPUTED with runner_1l.compute_chk, never read from the item and never asserted."""
    info = {'side': side_tag, 'data_dir': data_dir or os.path.join(HERE, 'data')}
    sents = {int(s['sid']): s for s in loader.load_sentences(purpose, caller='runner_1p.py',
                                                             data_dir=data_dir)}
    ann = loader.load_annotations(purpose, caller='runner_1p.py', data_dir=data_dir)
    items = loader.load_items(purpose, caller='runner_1p.py', data_dir=data_dir)
    recs = []
    for it in items:
        sid = int(it['sid'])
        if sid not in sents:
            raise SystemExit('REFUSED: item %s has no sentence %d' % (it['id'], sid))
        s, a = sents[sid], (ann.get(str(sid)) or {})
        hy = a.get('hygienised', a)
        if not hy:
            raise SystemExit('REFUSED: sid %d has no annotation' % sid)
        lk = []
        for x in (hy.get('lk') or []):
            lk += [x] if isinstance(x, str) else [y for y in x if isinstance(y, str)]
        refs = [x for x in (hy.get('v') or []) if isinstance(x, str) and x.strip()]
        r = {'item_id': it['id'], 'kind': it['id'].split(':')[0], 'sid': sid, 'n': 1,
             'level': s.get('level'), 'topic': s.get('topic'), 'sk': s['slovak'],
             'band': R1N._band(s['slovak']), 'reference': refs[0], 'refs': list(refs),
             'answer': it['answer'],
             'judged': 'wrong' if it['id'].startswith('W') else 'correct',
             'wrong_type': None, 'half': half_of(sid), 'locks': lk,
             'intent': it.get('intent'), 'form': it.get('form'),
             'passive': it.get('passive'), 'tags_list': list(it.get('tags') or []),
             'tags': dict(s.get('tags') or {}),
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
    st = make_state(recs, ann, side_tag)
    dist, how = collections.Counter(), collections.Counter()
    for r in recs:
        r['chk'], h = RL.compute_chk(r)                    # COMPUTED, never asserted
        how[h] += 1
        dist['%s/%s' % (r['chk']['verdict'], r['chk']['step'])] += 1
    info.update({'chk_computed': dict(how), 'chk_distribution': dict(dist), 'n_items': len(recs),
                 'n_sentences': len({r['sid'] for r in recs}),
                 'passive_tags': dict(collections.Counter(str(r['passive']) for r in recs)),
                 'writer_tags': dict(collections.Counter(
                     t for r in recs for t in (r['tags_list'] or ['<none>'])))})
    info['levers'] = attach_levers(recs, ann, levers)
    acc = [r for r in recs if r['chk']['verdict'] in ('correct', 'correct_with_tip')]
    if len(dist) == 1 and len(acc) == len(recs):
        open(STOP_CHK, 'w', encoding='utf-8').write(json.dumps(
            {'why': 'every record carries the same ACCEPTING chk — the Phase 1k hard-wired-checker '
                    'defect; nothing was measured and no model call was made',
             'chk_distribution': info['chk_distribution']}, indent=1) + '\n')
        raise SystemExit('STOP: degenerate chk, %s written, 0 model calls made' % STOP_CHK)
    say('[BUILD %s] %d items / %d sentences   chk %s   passive %s   levers %s'
        % (side_tag, len(recs), info['n_sentences'], json.dumps(info['chk_distribution'], sort_keys=True),
           json.dumps(info['passive_tags'], sort_keys=True), json.dumps(info['levers'], sort_keys=True)))
    return st, recs, ann, {r['item_id']: r for r in recs}, info


def make_state(recs, ann, side_tag):
    try:
        return R.make_state(recs, ann, ('F4v3',), side_tag=side_tag)
    except Exception as e:
        say('[BUILD] make_state(side_tag=%r) failed (%s); falling back to "fresh1k"' % (side_tag, e))
        return R.make_state(recs, ann, ('F4v3',), side_tag='fresh1k')


def half_of(sid):
    """SPLIT_1P.md: within each level, odd SID number -> P1, even -> P2."""
    return 'P1' if int(sid) % 2 == 1 else 'P2'


# ================================================================== decisions
def _no_f4v2(base, ids):
    def dec(it, flags, vm):
        if it['item_id'] in ids:
            flags = dict(flags, F4v2=False, F4=False)
        return base(it, flags, vm)
    return dec


def decide(st, recs, ann, vm, suppress_f4v2=()):
    g = R1K.guard_readouts(recs, ann, False)
    guards = {i: {'f8': None, 'f9': g[i]['f9']} for i in g}     # F8 CANNOT decide, F9 does not
    stx = dict(st)
    if suppress_f4v2:
        stx['decide'] = _no_f4v2(st['decide'], set(suppress_f4v2))
    RL.RES_VM[0] = vm
    return R1K.configure_row(stx, recs, vm, True, guards, False, False, True), guards


def l3_eligible(st, recs):
    lock_rej, l3 = RL.lock_counts(st, recs)
    return lock_rej, l3


def plan(st, recs, ids, prompt_id):
    by = {r['item_id']: r for r in recs}
    req, hmap = {}, {}
    for i in ids:
        s, u, g, h = R1K.build_req(st, by[i], prompt_id)
        R1K.SYS_TEXT_CACHE['sys'] = s
        req[h] = (s, u, g, h, 'L-1P', i)
        hmap[i] = h
    return req, hmap


def counted_local():
    n = 0
    if os.path.exists(CALLS):
        for row in R.ledger_rows(CALLS):
            if row.get('counted'):
                n += 1
    return n


def run_calls(req, need, what):
    done = counted_local()
    if done + len(need) > PHASE_CAP_1P:
        open(STOP_PLAN, 'w', encoding='utf-8').write(json.dumps(
            {'what': what, 'planned_new_calls': len(need), 'already_counted': done,
             'cap': PHASE_CAP_1P, 'why': 'the plan exceeds the phase cap; nothing was trimmed and '
                                         'no call was made'}, indent=1) + '\n')
        raise SystemExit('STOP: %d + %d > cap %d — %s written, 0 calls made'
                         % (done, len(need), PHASE_CAP_1P, STOP_PLAN))
    made = {'ok': 0, 'bad': 0, 'empty': 0, 'skipped': 0, 'wall': False}
    if need:
        made = R1N.make_calls(req, need)
    return made


def verdicts():
    rep, ver, failed, _c = RL.ledger_state()
    return ver, failed


# ================================================================== lever 1 side
def lever1_side(st, recs, ann, side_tag):
    """The rewritten records for every item lever 1 fires on.  Returns (st2, recs2, ids)."""
    fired = [r for r in recs if (r.get('_lev') or {}).get('lever1', {}).get('fired')]
    if not fired:
        return None, [], []
    recs2 = []
    for r in fired:
        r2 = dict(r)
        r2['answer'] = r['_lev']['lever1']['rewritten']
        r2['lock_ok'], r2['lock_released_2_1'] = True, None
        try:
            nrm = C.base.norm
            r2['lock_ok'] = (not r2['locks']) or any(nrm(x).strip() in nrm(r2['answer'])
                                                     for x in r2['locks'])
        except Exception:
            pass
        recs2.append(r2)
    st2 = make_state(recs2, ann, side_tag + ':l1rw')
    for r2 in recs2:
        r2['chk'], _h = RL.compute_chk(r2)
    return st2, recs2, [r['item_id'] for r in fired]


# ================================================================== scoring
def score(recs, by, res_main, res_l1, lab, info, guards_main):
    rows, agg = {}, collections.Counter()
    for r in recs:
        i = r['item_id']
        m = res_main[i]
        lv = r.get('_lev') or {}
        l1 = lv.get('lever1') or {}
        rw = res_l1.get(i) if res_l1 else None
        fired = bool(l1.get('fired'))
        l1_accept = bool(fired and rw and rw.get('accepted'))
        accept = bool(m['accepted'] or l1_accept)
        tip = None
        if l1_accept and not m['accepted']:
            tip = l1.get('tip')
        judged, typ = lab.get(i, (r['judged'], r['wrong_type']))
        rows[i] = {
            'sid': r['sid'], 'item_id': i, 'half': r['half'], 'level': r['level'],
            'judged': judged, 'judged_type': typ, 'tags': r.get('tags_list'),
            'writer_passive': r.get('passive'), 'intent': r.get('intent'),
            'layers': {'main_layer': m['layer'], 'main_verdict': m['verdict'],
                       'model': m.get('model'), 'model_tip': m.get('model_tip'),
                       'reached_l3': m.get('reached_l3')},
            'lever1': {'fired': fired, 'agent': l1.get('agent'), 'reason': l1.get('reason'),
                       'rewritten': l1.get('rewritten'),
                       'rewritten_layer': (rw or {}).get('layer'),
                       'rewritten_accept': bool(rw and rw.get('accepted')),
                       'shadow_unrewritten_accept': bool(m['accepted']),
                       'shadow_unrewritten_layer': m['layer']},
            'lever2_fired': lv.get('lever2_fired'),
            'lever3': {'variants_shown': len((lv.get('lever3') or {}).get('shown') or []),
                       'variants_removed': len((lv.get('lever3') or {}).get('removed') or []),
                       'removed_detail': (lv.get('lever3') or {}).get('removed')},
            'final_accept': accept, 'tip': tip,
            'f9_readout': (guards_main.get(i) or {}).get('f9')}
        agg[('accept' if accept else 'reject') + '/' + judged] += 1
    cov_k = sum(1 for i in rows if rows[i]['judged'] == 'correct' and rows[i]['final_accept'])
    cov_n = sum(1 for i in rows if rows[i]['judged'] == 'correct')
    fa_k = sum(1 for i in rows if rows[i]['judged'] == 'wrong' and rows[i]['final_accept'])
    fa_n = sum(1 for i in rows if rows[i]['judged'] == 'wrong')
    def _m(k, n):
        return {'k': k, 'n': n, 'pct': round(100.0 * k / n, 2) if n else None,
                'ci': P.cp(k, n) if n else [0.0, 0.0]}
    met = {'coverage': _m(cov_k, cov_n), 'fa': _m(fa_k, fa_n),
           'coverage_kn': [cov_k, cov_n], 'fa_kn': [fa_k, fa_n],
           'coverage_pct': round(100.0 * cov_k / cov_n, 2) if cov_n else None,
           'coverage_ci': P.cp(cov_k, cov_n) if cov_n else None,
           'fa_pct': round(100.0 * fa_k / fa_n, 2) if fa_n else None,
           'fa_ci': P.cp(fa_k, fa_n) if fa_n else None,
           'accept_table': dict(agg)}
    return rows, met


def cells(rows):
    out = {}
    for tag in ('agentless', 'by-passive', 'determiner', 'aspect', 'timeframe', 'number', 'plain'):
        ids = [i for i, x in enumerate(rows.values())]
        cor = [x for x in rows.values() if tag in (x['tags'] or []) and x['judged'] == 'correct']
        wro = [x for x in rows.values() if tag in (x['tags'] or []) and x['judged'] == 'wrong']
        out[tag] = {'judged_correct': len(cor),
                    'accepted': sum(1 for x in cor if x['final_accept']),
                    'judged_wrong': len(wro),
                    'false_accepts': sum(1 for x in wro if x['final_accept'])}
    for h in ('P1', 'P2'):
        cor = [x for x in rows.values() if x['half'] == h and x['judged'] == 'correct']
        wro = [x for x in rows.values() if x['half'] == h and x['judged'] == 'wrong']
        out['half:' + h] = {'coverage_kn': [sum(1 for x in cor if x['final_accept']), len(cor)],
                            'fa_kn': [sum(1 for x in wro if x['final_accept']), len(wro)]}
    l1 = [x for x in rows.values() if x['lever1']['fired']]
    out['lever1'] = {'fired': len(l1),
                     'gain': sum(1 for x in l1 if x['judged'] == 'correct'
                                 and x['final_accept'] and not x['lever1']['shadow_unrewritten_accept']),
                     'fa_cost': sum(1 for x in l1 if x['judged'] == 'wrong'
                                    and x['final_accept'] and not x['lever1']['shadow_unrewritten_accept']),
                     'shadow_accept': sum(1 for x in l1 if x['lever1']['shadow_unrewritten_accept'])}
    out['lever3'] = {'variants_shown': sum(x['lever3']['variants_shown'] for x in rows.values()),
                     'variants_removed_by_the_tense_filter':
                         sum(x['lever3']['variants_removed'] for x in rows.values())}
    return out


# ================================================================== modes
def preflight(levers=(1, 2, 3), data_dir=None, loader=LM, tag=SIDE_TAG, quiet=False):
    cfg, sel = load_cfg(levers)
    st, recs, ann, by, info = build_side('Phase 1P preflight (0 calls)', data_dir,
                                         tag, sel['levers'], loader)
    lock_rej, l3 = l3_eligible(st, recs)
    say('L2 lock firings under BASE: %d   L3-eligible under LOCKTIP: %d' % (len(lock_rej), len(l3)))
    if not l3:
        open(STOP_PRE, 'w', encoding='utf-8').write(json.dumps(
            {'tag': tag, 'lock_rejections_BASE': len(lock_rej), 'l3_eligible_LOCKTIP': 0,
             'why': 'L3-eligible 0 — degenerate side (the Phase 1k defect); no model call was made'},
            indent=1) + '\n')
        raise SystemExit('STOP: L3-eligible 0, %s written, 0 model calls made' % STOP_PRE)
    assert len(lock_rej) > 0, 'PREFLIGHT: L2 fired 0 times — the measuring apparatus is wrong'
    assert len(l3) > 0
    req, hmap = plan(st, recs, l3, sel['prompt'])
    ver, failed = verdicts()
    need = [h for h in req if h not in ver and h not in failed]
    done = counted_local()
    say('[PREFLIGHT] unique requests %d   reusable %d   PLANNED NEW CALLS %d   counted so far %d'
        % (len(req), len(req) - len(need), len(need), done))
    say('[PREFLIGHT] dev_used + planned = %d + %d = %d   (stop threshold %d, phase cap %d)'
        % (done, len(need), done + len(need), PREFLIGHT_STOP_AT, PHASE_CAP_1P))
    if done + len(need) > PREFLIGHT_STOP_AT:
        open(STOP_PLAN, 'w', encoding='utf-8').write(json.dumps(
            {'dev_used': done, 'planned': len(need), 'stop_at': PREFLIGHT_STOP_AT,
             'why': 'dev_used + planned exceeds 1,390; nothing trimmed, no call made'}, indent=1) + '\n')
        raise SystemExit('STOP: %d + %d > %d — %s written, 0 calls made'
                         % (done, len(need), PREFLIGHT_STOP_AT, STOP_PLAN))
    return st, recs, ann, by, info, lock_rej, l3, req, hmap, need, sel


def run_preflight(a):
    preflight()
    say('[PREFLIGHT] PASS')


def run_dry(a):
    """Synthetic rows, 0 calls: the whole build -> lever -> decide -> score path."""
    d = os.path.join(HERE, 'selftest', 'data')
    os.makedirs(d, exist_ok=True)
    make_fixture(d)
    st, recs, ann, by, info = build_side('Phase 1P dry run on synthetic rows (0 calls)',
                                         d, 'synthetic', (1, 2, 3), LM)
    lock_rej, l3 = l3_eligible(st, recs)
    say('[DRY-RUN] L2 %d   L3-eligible %d' % (len(lock_rej), len(l3)))
    req, hmap = plan(st, recs, l3, PROMPT_1P)
    vm = {i: 'SAME' for i in l3}                              # synthetic verdicts, 0 calls
    res_main, guards = decide(st, recs, ann, vm)
    st2, recs2, ids2 = lever1_side(st, recs, ann, 'synthetic')
    res_l1 = {}
    if recs2:
        vm2 = {r['item_id']: 'SAME' for r in recs2}
        res_l1, _g2 = decide(st2, recs2, ann, vm2, suppress_f4v2=ids2)
    rows, met = score(recs, by, res_main, res_l1, {}, info, guards)
    out = {'mode': 'dry-run (synthetic, 0 model calls)', 'n_items': len(recs),
           'unique_requests': len(req), 'l2': len(lock_rej), 'l3_eligible': len(l3),
           'metrics': met, 'cells': cells(rows), 'levers': info['levers'],
           'rows': list(rows.values())}
    json.dump(out, open(os.path.join(HERE, 'selftest', 'dry_run_1p.json'), 'w', encoding='utf-8'),
              indent=1, ensure_ascii=False)
    say('[DRY-RUN] %s' % json.dumps({k: out[k] for k in ('n_items', 'unique_requests', 'l2',
                                                         'l3_eligible')}))
    say('[DRY-RUN] levers %s' % json.dumps(info['levers'], sort_keys=True))
    say('[DRY-RUN] lever1 %s' % json.dumps(out['cells']['lever1']))
    say('[DRY-RUN] written selftest/dry_run_1p.json — 0 model calls')
    return out


def make_fixture(d):
    """A tiny synthetic side that exercises all three levers (never a measurement)."""
    sents = [{'sid': 170001, 'slovak': 'Peter kontroluje schránku každé ráno.', 'level': 'A1',
              'topic': 'home', 'tags': {}},
             {'sid': 170002, 'slovak': 'Mária upiekla chlieb pre hostí.', 'level': 'A2',
              'topic': 'food', 'tags': {}}]
    ann = {'170001': {'agent_nom': True, 'voice_sk': 'active_agent', 'tf_gold': 'present',
                      'tense_open': True, 'perfective_present': False,
                      'hygienised': {'id': 170001, 'lk': [], 'lv': 'A1',
                                     'v': ['Peter checks the letterbox every morning.',
                                           'Every morning Peter checks the letterbox.',
                                           'Peter will check the letterbox every morning.']}},
           '170002': {'agent_nom': True, 'voice_sk': 'active_agent', 'tf_gold': 'past',
                      'tense_open': False, 'perfective_present': False,
                      'hygienised': {'id': 170002, 'lk': [], 'lv': 'A2',
                                     'v': ['Mary baked bread for the guests.',
                                           'Mary has baked bread for the guests.']}}}
    items = [{'id': 'C:170001:1', 'sid': 170001, 'kind': 'C', 'intent': 'C', 'form': None,
              'tags': ['agentless'], 'answer': 'The letterbox is checked every morning.'},
             {'id': 'C:170001:2', 'sid': 170001, 'kind': 'C', 'intent': 'C', 'form': None,
              'tags': ['determiner'], 'answer': 'Peter checks a letterbox every morning.'},
             {'id': 'W:170001:3', 'sid': 170001, 'kind': 'W', 'intent': 'TF', 'form': None,
              'tags': ['timeframe'], 'answer': 'Peter checked the letterbox every morning.'},
             {'id': 'C:170002:1', 'sid': 170002, 'kind': 'C', 'intent': 'C', 'form': None,
              'tags': ['agentless'], 'answer': 'Bread was baked for the guests.'},
             {'id': 'C:170002:2', 'sid': 170002, 'kind': 'C', 'intent': 'C', 'form': None,
              'tags': ['aspect'], 'answer': 'Mary has baked bread for the guests.'},
             {'id': 'W:170002:3', 'sid': 170002, 'kind': 'W', 'intent': 'TF', 'form': None,
              'tags': ['timeframe'], 'answer': 'Mary will bake bread for the guests.'}]
    json.dump(sents, open(os.path.join(d, 'sentences.json'), 'w', encoding='utf-8'), indent=1,
              ensure_ascii=False)
    json.dump(ann, open(os.path.join(d, 'annotations.json'), 'w', encoding='utf-8'), indent=1,
              ensure_ascii=False)
    json.dump(items, open(os.path.join(d, 'items.json'), 'w', encoding='utf-8'), indent=1,
              ensure_ascii=False)


def check_freeze():
    if not os.path.exists(FREEZE_HASH):
        raise SystemExit('REFUSED: %s does not exist — freeze the code first.' % FREEZE_HASH)
    if not os.path.exists(FREEZE_FILES):
        raise SystemExit('REFUSED: %s does not exist.' % FREEZE_FILES)
    h = open(FREEZE_HASH, encoding='utf-8').read().strip().split()[0]
    files = [x.strip() for x in open(FREEZE_FILES, encoding='utf-8').read().splitlines()
             if x.strip() and not x.strip().startswith('#')]
    missing = [f for f in sorted(os.listdir(HERE)) if f.endswith('.py') and f not in files]
    if missing:
        raise SystemExit('REFUSED: .py files in phase1p not in FREEZE_FILES: %s' % ', '.join(missing))
    bad = []
    for f in files:
        p = os.path.join(HERE, f)
        if not os.path.exists(p):
            bad.append({'file': f, 'now': 'ABSENT'})
            continue
        cur = subprocess.check_output(['git', 'hash-object', p], cwd=RL.REPO).decode().strip()
        try:
            was = subprocess.check_output(
                ['git', 'rev-parse', '%s:translation-offline/phase1p/%s' % (h, f)],
                cwd=RL.REPO, stderr=subprocess.DEVNULL).decode().strip()
        except subprocess.CalledProcessError:
            was = None
        if cur != was:
            bad.append({'file': f, 'now': cur[:12], 'at_freeze': (was or 'ABSENT')[:12]})
    if bad:
        raise SystemExit('REFUSED: phase1p code differs from FREEZE_HASH %s: %s' % (h, json.dumps(bad)))
    say('[FREEZE] %d python files identical to commit %s' % (len(files), h))
    return h


def run_final(a):
    if os.path.exists(DONE):
        raise SystemExit('REFUSED: %s exists — the new side is measured once.' % DONE)
    fh = check_freeze()
    st, recs, ann, by, info, lock_rej, l3, req, hmap, need, sel = preflight()
    if info['n_items'] != FINAL_ITEMS_EXPECTED:
        say('[FINAL] NOTE: %d items, %d expected' % (info['n_items'], FINAL_ITEMS_EXPECTED))
    made = run_calls(req, need, 'final:main')
    ver, failed = verdicts()
    still = [h for h in req if h not in ver and h not in failed]
    if made.get('wall') or still:
        open(PAUSED, 'w', encoding='utf-8').write(json.dumps(
            {'why': 'the quota wall' if made.get('wall') else 'requests without a verdict',
             'unique_requests': len(req), 'still_without_verdict': len(still),
             'counted_calls_phase1p': counted_local(),
             'next': 'rerun --final; every stored verdict is reused by request hash. NO judge '
                     'label was read.'}, indent=1) + '\n')
        raise SystemExit(3)
    # ---- lever 1 side (a second, smaller request set: the REWRITTEN answers)
    st2, recs2, ids2 = lever1_side(st, recs, ann, SIDE_TAG)
    res_l1, vm2 = {}, {}
    if recs2:
        _lr2, l3b = l3_eligible(st2, recs2)
        req2, hmap2 = plan(st2, recs2, l3b, sel['prompt'])
        ver, failed = verdicts()
        need2 = [h for h in req2 if h not in ver and h not in failed]
        say('[FINAL] lever 1: %d rewritten records, %d L3-eligible, %d NEW calls'
            % (len(recs2), len(l3b), len(need2)))
        run_calls(req2, need2, 'final:lever1')
        ver, failed = verdicts()
        vm2 = {i: ver[h] for i, h in hmap2.items() if h in ver}
        res_l1, _g2 = decide(st2, recs2, ann, vm2, suppress_f4v2=ids2)
    # ---- labels, once, after every verdict exists
    labels, controls, lmeta = LM.load_labels('Phase 1P final', caller='runner_1p.py')
    for r in recs:
        if r['item_id'] in labels:
            r['judged'], r['wrong_type'] = labels[r['item_id']]
    vm = {i: ver[h] for i, h in hmap.items() if h in ver}
    res_main, guards = decide(st, recs, ann, vm)
    rows, met = score(recs, by, res_main, res_l1, labels, info, guards)
    out = {'phase': '1P', 'side': SIDE_TAG, 'freeze_commit': fh, 'frozen_config': load_cfg()[0],
           'prompt': PROMPT_1P, 'model': {'model': P.MODEL, 'temperature': 0, 'thinkingBudget': 0},
           'preflight': {'l2': len(lock_rej), 'l3_eligible': len(l3)}, 'build': info,
           'metrics': met, 'cells': cells(rows), 'judge_noise': R1N.judge_noise(labels, controls),
           'label_meta': {k: v for k, v in lmeta.items() if k != 'passive_by_item'},
           'calls': {'counted_total_phase1p': counted_local(), 'unique_main': len(req),
                     'new_main': len(need)},
           'rows': list(rows.values())}
    json.dump(out, open(os.path.join(HERE, 'results_1p.json'), 'w', encoding='utf-8'), indent=1,
              ensure_ascii=False)
    md = ['# Phase 1P — the new set under P-FROZEN-1P (levers 1-3), measured once', '',
          '* coverage **%s %%** %s (k/n %s)' % (met['coverage_pct'], met['coverage_ci'], met['coverage_kn']),
          '* false accepts **%s %%** %s (k/n %s)' % (met['fa_pct'], met['fa_ci'], met['fa_kn']), '',
          '## halves', '', '```', json.dumps({k: v for k, v in out['cells'].items()
                                              if k.startswith('half:')}, indent=1), '```', '',
          '## tags', '', '```', json.dumps({k: v for k, v in out['cells'].items()
                                            if not k.startswith('half:')}, indent=1), '```', '']
    open(os.path.join(HERE, 'results_1p.md'), 'w', encoding='utf-8').write('\n'.join(md))
    open(DONE, 'w', encoding='utf-8').write(json.dumps(
        {'phase': '1P', 'freeze_commit': fh, 'coverage': met['coverage_kn'], 'fa': met['fa_kn'],
         'counted_calls': counted_local()}, indent=1) + '\n')
    say('-- FINAL_RUN_DONE written: the new side is measured, once.')
    return out


def run_ablation(a):
    """PRE-DECLARED, leftover calls only: the baseline P-FROZEN-1N stack WITHOUT levers, on
    judged-correct determiner-tag L3-eligible items first, then judged-correct agentless items,
    in SID order, until the cap minus 10."""
    if not os.path.exists(DONE):
        raise SystemExit('REFUSED: --ablation runs after --final only.')
    st, recs, ann, by, info = build_side('Phase 1P ablation (baseline, no levers)', None,
                                         SIDE_TAG, (), LM)
    labels, _c, _m = LM.load_labels('Phase 1P ablation', caller='runner_1p.py')
    _lr, l3 = l3_eligible(st, recs)
    l3s = set(l3)
    def pick(tag):
        return sorted([r['item_id'] for r in recs
                       if tag in (r['tags_list'] or []) and r['item_id'] in l3s
                       and labels.get(r['item_id'], ('correct', None))[0] == 'correct'],
                      key=lambda i: (by[i]['sid'], i))
    order = pick('determiner') + [i for i in pick('agentless') if i not in set(pick('determiner'))]
    budget = max(0, PHASE_CAP_1P - 10 - counted_local())
    req, hmap = plan(st, recs, order, PROMPT_1N)
    ver, failed = verdicts()
    need, seen = [], set()
    for i in order:
        h = hmap[i]
        if h in ver or h in failed or h in seen:
            continue
        if len(need) >= budget:
            break
        need.append(h)
        seen.add(h)
    say('[ABLATION] candidates %d   budget %d   NEW calls %d' % (len(order), budget, len(need)))
    run_calls({h: req[h] for h in need} or {}, need, 'ablation')
    ver, failed = verdicts()
    sub = [i for i in order if hmap[i] in ver]
    vm = {i: ver[hmap[i]] for i in sub}
    res, _g = decide(st, recs, ann, vm)
    out = {'mode': 'ablation: baseline P-FROZEN-1N, levers OFF', 'items_scored': len(sub),
           'accepted': sum(1 for i in sub if res[i]['accepted']),
           'by_tag': {t: {'n': sum(1 for i in sub if t in (by[i]['tags_list'] or [])),
                          'accepted': sum(1 for i in sub if t in (by[i]['tags_list'] or [])
                                          and res[i]['accepted'])}
                      for t in ('determiner', 'agentless')},
           'counted_calls_phase1p': counted_local(), 'ids': sub}
    json.dump(out, open(os.path.join(HERE, 'ablation_1p.json'), 'w', encoding='utf-8'), indent=1,
              ensure_ascii=False)
    say('[ABLATION] %s' % json.dumps({k: out[k] for k in ('items_scored', 'accepted', 'by_tag')}))
    return out


# ================================================================== development (closed sides)
def run_dev(a):
    """Per-lever DEV measurement on the CLOSED 1N side.  Prints the plan and STOPS unless --go."""
    lv = a.lever
    levers = () if lv == 0 else (lv,)
    st, recs, ann, by, info = build_side('Phase 1P dev on the CLOSED 1N side (design only)',
                                         N_DATA, 'fresh1n', levers, LM)
    labels, controls, lmeta = LM.load_labels('Phase 1P dev labels (CLOSED 1N)',
                                             caller='runner_1p.py', judge_dir=N_JUDGE)
    for r in recs:
        if r['item_id'] in labels:
            r['judged'], r['wrong_type'] = labels[r['item_id']]
    _lr, l3 = l3_eligible(st, recs)
    l3s = set(l3)
    # ---- baseline: prompt P-FROZEN-1N, NO lever lines -> every verdict is stored (0 calls)
    saved = [(r['item_id'], r.get('_extra')) for r in recs]
    for r in recs:
        r['_extra'] = []
    req0, hmap0 = plan(st, recs, l3, PROMPT_1N)
    ver, failed = verdicts()
    miss = [h for h in req0.values() if h[3] not in ver and h[3] not in failed]
    vm0 = {i: ver[h] for i, h in hmap0.items() if h in ver}
    res0, guards0 = decide(st, recs, ann, vm0)
    for i, e in saved:
        by[i]['_extra'] = e
    cov0 = [sum(1 for r in recs if r['judged'] == 'correct' and res0[r['item_id']]['accepted']),
            sum(1 for r in recs if r['judged'] == 'correct')]
    fa0 = [sum(1 for r in recs if r['judged'] == 'wrong' and res0[r['item_id']]['accepted']),
           sum(1 for r in recs if r['judged'] == 'wrong')]
    say('[DEV] BASELINE on the closed 1N side: coverage %s  FA %s  (1N headline: 350/426, 14/474); '
        'stored verdicts missing for %d of %d L3 requests' % (cov0, fa0, len(miss), len(req0)))
    assert cov0 == [350, 426] and fa0 == [14, 474], 'APPARATUS: the 1N baseline is not reproduced'

    base_rej_correct = [r['item_id'] for r in recs if r['judged'] == 'correct'
                        and not res0[r['item_id']]['accepted']]
    out = {'lever': lv, 'baseline': {'coverage': cov0, 'fa': fa0,
                                     'false_rejections': len(base_rej_correct)},
           'lever_stats': info['levers']}

    if lv == 1:
        fired = [r for r in recs if r['_lev']['lever1']['fired']]
        tgt = [r for r in fired if r['judged'] == 'correct']
        exp = [r for r in fired if r['judged'] == 'wrong']
        agentless = [r for r in recs if r['passive'] == 'agentless']
        det_ok = sum(1 for r in agentless if r['_lev']['lever1']['answer_is_agentless_passive'])
        say('[DEV L1] detector fires on %d items: %d judged-correct, %d judged-wrong (EXPOSURE). '
            'writer agentless tag %d, of which the detector sees %d as an agentless passive'
            % (len(fired), len(tgt), len(exp), len(agentless), det_ok))
        cap = a.fa_n or 40
        exp_s = sorted(exp, key=lambda r: r['item_id'])
        random.Random(1).shuffle(exp_s)
        exp_s = sorted(exp_s[:cap], key=lambda r: r['item_id'])
        use = tgt + exp_s
        st2, recs2, ids2 = lever1_side(st, recs, ann, 'fresh1n')
        keep = {r['item_id'] for r in use}
        recs2 = [r for r in recs2 if r['item_id'] in keep]
        st2 = make_state(recs2, ann, 'fresh1n:l1rw')
        for r2 in recs2:
            r2['chk'], _h = RL.compute_chk(r2)
        _lr2, l3b = l3_eligible(st2, recs2)
        req2, hmap2 = plan(st2, recs2, l3b, PROMPT_1N)
        ver, failed = verdicts()
        need2 = [h for h in req2 if h not in ver and h not in failed]
        say('[DEV L1] PLAN: %d rewritten records, %d L3-eligible, NEW COUNTED CALLS %d '
            '(dev used so far %d, dev cap %d)' % (len(recs2), len(l3b), len(need2),
                                                  counted_local(), DEV_CAP))
        if not a.go:
            say('[DEV L1] plan only — rerun with --go to spend the calls')
            return out
        run_calls(req2, need2, 'dev:lever1')
        ver, failed = verdicts()
        vm2 = {i: ver[h] for i, h in hmap2.items() if h in ver}
        res2, _g = decide(st2, recs2, ann, vm2, suppress_f4v2=[r['item_id'] for r in recs2])
        gain = [r['item_id'] for r in use if r['judged'] == 'correct'
                and not res0[r['item_id']]['accepted'] and res2.get(r['item_id'], {}).get('accepted')]
        cost = [r['item_id'] for r in use if r['judged'] == 'wrong'
                and not res0[r['item_id']]['accepted'] and res2.get(r['item_id'], {}).get('accepted')]
        f4 = [r['item_id'] for r in use if res0[r['item_id']]['layer'] == 'F4v2']
        out['lever1'] = {
            'detector_fired': len(fired), 'target_judged_correct': len(tgt),
            'exposure_judged_wrong_total': len(exp), 'exposure_sampled': len(exp_s),
            'writer_agentless_items': len(agentless), 'detector_sees_them': det_ok,
            'gain_ids': gain, 'gain': len(gain), 'fa_cost_ids': cost, 'fa_cost': len(cost),
            'f4v2_stops_in_the_set': f4,
            'shadow_unrewritten_accept': sum(1 for r in use if res0[r['item_id']]['accepted']),
            'calls': len(need2)}
        say('[DEV L1] GAIN %d / %d judged-correct fired   FA COST %d / %d judged-wrong sampled'
            % (len(gain), len(tgt), len(cost), len(exp_s)))

    elif lv in (2, 3):
        l1flag = {r['item_id'] for r in recs
                  if lever1.detect(r['sk'], ann.get(str(r['sid'])), r['answer'],
                                   r['reference'])['fired']}
        gain_set = [i for i in base_rej_correct
                    if res0[i]['layer'] in ('L3', 'L3:TIPrej') and i not in l1flag]
        wrong = [r['item_id'] for r in recs if r['judged'] == 'wrong' and r['item_id'] in l3s]
        tf = [i for i in wrong if by[i]['intent'] == 'TF']
        oth = [i for i in wrong if by[i]['intent'] != 'TF']
        rng = random.Random(7)
        n_fa = a.fa_n or 55
        n_tf = int(round(n_fa * 0.7))
        fa_set = sorted(rng.sample(tf, min(n_tf, len(tf))) +
                        rng.sample(oth, min(n_fa - n_tf, len(oth))))
        use = [i for i in gain_set + fa_set if i in l3s]
        sub = [by[i] for i in use]
        req2, hmap2 = plan(st, sub, use, PROMPT_1P)
        ver, failed = verdicts()
        need2 = [h for h in req2 if h not in ver and h not in failed]
        say('[DEV L%d] PLAN: gain set %d (L3 false rejections, non-agentless), FA set %d '
            '(%d time-frame + %d other), NEW COUNTED CALLS %d (dev used %d, cap %d)'
            % (lv, len(gain_set), len(fa_set), min(n_tf, len(tf)), len(fa_set) - min(n_tf, len(tf)),
               len(need2), counted_local(), DEV_CAP))
        nolines = [i for i in use if not by[i].get('_extra')]
        say('[DEV L%d] items the lever adds no line to: %d (their request is the 1N one, 0 calls)'
            % (lv, len(nolines)))
        if not a.go:
            say('[DEV L%d] plan only — rerun with --go to spend the calls' % lv)
            return out
        run_calls(req2, need2, 'dev:lever%d' % lv)
        ver, failed = verdicts()
        vm = dict(vm0)
        vm.update({i: ver[h] for i, h in hmap2.items() if h in ver})
        res, _g = decide(st, recs, ann, vm)
        gain = [i for i in gain_set if res[i]['accepted']]
        cost = [i for i in fa_set if res[i]['accepted'] and not res0[i]['accepted']]
        tfcost = [i for i in cost if by[i]['intent'] == 'TF']
        out['lever%d' % lv] = {
            'gain_set': len(gain_set), 'gain': len(gain), 'gain_ids': gain,
            'fa_set': len(fa_set), 'fa_cost': len(cost), 'fa_cost_ids': cost,
            'fa_cost_time_frame': len(tfcost),
            'fa_set_baseline_accepts': sum(1 for i in fa_set if res0[i]['accepted']),
            'items_without_a_lever_line': len(nolines), 'calls': len(need2)}
        if lv == 3:
            rem = [x for r in recs for x in ((r['_lev'].get('lever3') or {}).get('removed') or [])]
            out['lever3']['variants_removed_by_the_filter_whole_side'] = len(rem)
            out['lever3']['variants_shown_whole_side'] = sum(
                len((r['_lev'].get('lever3') or {}).get('shown') or []) for r in recs)
            out['lever3']['removed_examples'] = rem[:8]
        say('[DEV L%d] GAIN %d / %d   FA COST %d / %d (time-frame %d)'
            % (lv, len(gain), len(gain_set), len(cost), len(fa_set), len(tfcost)))

    out['counted_calls_phase1p'] = counted_local()
    p = os.path.join(HERE, 'dev', 'dev_lever%d.json' % lv)
    json.dump(out, open(p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    say('-- written %s' % p)
    return out


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--preflight', action='store_true')
    g.add_argument('--dry-run', dest='dry_run', action='store_true')
    g.add_argument('--final', action='store_true')
    g.add_argument('--ablation', action='store_true')
    g.add_argument('--dev', action='store_true')
    ap.add_argument('--lever', type=int, default=0, choices=(0, 1, 2, 3))
    ap.add_argument('--fa-n', dest='fa_n', type=int, default=0)
    ap.add_argument('--go', action='store_true')
    a = ap.parse_args()
    if not a.dev and (a.go or a.fa_n or a.lever):
        raise SystemExit('REFUSED: --lever / --fa-n / --go are accepted in --dev only')
    (run_preflight if a.preflight else run_dry if a.dry_run else run_final if a.final
     else run_ablation if a.ablation else run_dev)(a)


if __name__ == '__main__':
    main()
