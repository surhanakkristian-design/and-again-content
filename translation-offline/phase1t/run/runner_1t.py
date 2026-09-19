#!/usr/bin/env python3
"""Phase 1T runner — the frozen 1Q/1P stack, UNCHANGED, with exactly three differences:

  1. lever 1 is REMOVED (no rewritten side, no extra calls);
  2. rule AG v3 (phase1t/taskA/agent_drop_v3.py, all flags) sits with the deterministic guards
     BEFORE L3: an AG rejection is final and costs 0 calls — the item never reaches L3.  The
     0-call SHADOW verdicts of AG v2 and of each v3 flag alone are recorded per item;
  3. RUNNER_PATCH_1S is applied in full (safe_dump everywhere, serialise-before-truncate,
     guarded_run, a marker that always exists, every reply in calls.jsonl before aggregation).

Everything else is imported, not re-implemented: the prompt (P-FROZEN-1P), the transport, the
pacing, the quota wall, the layers F2B/F3/F4v2/F5, LOCKTIP, TIP-as-rejection, levers 2 and 3 and
the checker all come from runner_1p -> runner_1n -> runner_1l/runner_1k.

    PYTHONDONTWRITEBYTECODE=1 python3 phase1t/run/runner_1t.py --dry-run     # 0 calls, stub model
    PYTHONDONTWRITEBYTECODE=1 python3 phase1t/run/runner_1t.py --preflight   # 0 calls
    PYTHONDONTWRITEBYTECODE=1 python3 phase1t/run/runner_1t.py --final       # ONCE, owner only

Model gemini-3.1-flash-lite, temperature 0, thinkingBudget 0.  The call cap is read from
FROZEN_CONFIG_1T.json ("call_cap"); while it is null, --final REFUSES.
"""
import argparse
import collections
import datetime
import json
import os
import subprocess
import sys
import traceback

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))            # phase1t/run
P1T = os.path.dirname(HERE)                                  # phase1t
TOFF = os.path.dirname(P1T)                                  # translation-offline
P1P = os.path.join(TOFF, 'phase1p')
P1S = os.path.join(TOFF, 'phase1s')
TASKA = os.path.join(P1T, 'taskA')
for _p in (HERE, P1P, P1S, TASKA):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import runner_1p as R1P                                                        # noqa: E402
from safe_json import safe_dump, write_done_marker, guarded_run, flush_log     # noqa: E402
import agent_drop_v3 as AG3                                                    # noqa: E402
import loader_1t as LM                                                         # noqa: E402

RL, R1K, R, P, C, R1N = R1P.RL, R1P.R1K, R1P.R, R1P.P, R1P.C, R1P.R1N

CFG_PATH = os.path.join(HERE, 'FROZEN_CONFIG_1T.json')
FREEZE_FILES = os.path.join(HERE, 'FREEZE_FILES')
SET = os.path.join(P1T, 'set')
DATA = os.path.join(SET, 'data')
FLOORS_JSON = os.path.join(SET, 'FLOOR_CHECK_1T.json')
FLOOR_KEYS = ('F1_agentdrop_any_wrong', 'F2_agentdrop_embedded_wrong', 'F3_timeframe_wrong',
              'F4_bypassive_correct', 'F5_skp_correct')
SIDE_TAG = 'fresh1t'
PROMPT = R1P.PROMPT_1P                                  # 'P-FROZEN-1P' — the frozen 1P prompt
LEVERS = (2, 3)                                         # difference 1: lever 1 is gone
AG_FLAGS = AG3.ALL_FLAGS                                # ('clause', 'subj', 'by')
AG_SHADOWS = (('v2', ()), ('v3_clause', ('clause',)), ('v3_subj', ('subj',)), ('v3_by', ('by',)))
DET_LAYERS_AFTER_AG = ('L3', 'L3:TIPrej')               # rescore_1s_c.build(), K3 attribution
FINAL_ITEMS_EXPECTED = 900

CALLS = DONE = PAUSED = STOP_PRE = STOP_PLAN = STOP_CHK = RUNLOG = None


# ================================================================== run directory / paths
def set_run_dir(d):
    """Re-point EVERY write site of the imported frozen stack into `d`.  Nothing is ever written
    into phase1p / phase1n / phase1t/set."""
    global CALLS, DONE, PAUSED, STOP_PRE, STOP_PLAN, STOP_CHK, RUNLOG
    os.makedirs(d, exist_ok=True)
    CALLS = os.path.join(d, 'calls.jsonl')
    DONE = os.path.join(d, 'FINAL_RUN_DONE')
    PAUSED = os.path.join(d, 'RUN_PAUSED.txt')
    STOP_PRE = os.path.join(d, 'STOP_PREFLIGHT.txt')
    STOP_PLAN = os.path.join(d, 'STOP_PLAN.txt')
    STOP_CHK = os.path.join(d, 'STOP_CHK.txt')
    RUNLOG = os.path.join(d, 'run_1t.log')
    RL.CALLS = R1P.CALLS = R1N.CALLS = CALLS
    RL.ACCESS = LM.LOG = os.path.join(d, 'access_log.jsonl')
    RL.HYG = os.path.join(d, 'hygiene')                 # absent on purpose -> hygiene off
    RL.DONE = R1P.DONE = DONE
    RL.STOP_PRE = R1N.STOP_PRE = R1P.STOP_PRE = STOP_PRE
    RL.STOP_PLAN = R1N.STOP_PLAN = R1P.STOP_PLAN = STOP_PLAN
    R1N.PAUSED = R1P.PAUSED = PAUSED
    R1P.STOP_CHK = STOP_CHK
    R1P.HERE = d
    R1P.CFG_PATH = CFG_PATH
    R1P.FREEZE_FILES = FREEZE_FILES
    RL.FREEZE_HASH = R1P.FREEZE_HASH = os.path.join(HERE, 'FREEZE_HASH')
    R1N.RUNLOG = R1P.RUNLOG = RUNLOG
    return d


set_run_dir(HERE)


def say(line):
    print(line, flush=True)
    with open(RUNLOG, 'a', encoding='utf-8') as fh:
        fh.write(str(line) + '\n')


R1N.say = say


# ================================================================== config / cap
def load_cfg():
    cfg = json.load(open(CFG_PATH, encoding='utf-8')) if os.path.exists(CFG_PATH) else {}
    if list(cfg.get('levers') or LEVERS) != list(LEVERS):
        raise SystemExit('REFUSED: 1T runs levers 2 and 3 only (lever 1 is removed), config says %s'
                         % cfg.get('levers'))
    if cfg.get('ag_rule') not in (None, 'v3'):
        raise SystemExit('REFUSED: 1T runs AG v3')
    _cfg, sel = R1P.load_cfg(LEVERS)                  # the frozen F8/F9/TIP guards, verbatim
    return cfg, sel


def call_cap():
    cfg = json.load(open(CFG_PATH, encoding='utf-8')) if os.path.exists(CFG_PATH) else {}
    return cfg.get('call_cap')


def counted_local():
    n = 0
    if os.path.exists(CALLS):
        for row in R.ledger_rows(CALLS):
            if row.get('counted'):
                n += 1
    return n


def verdicts():
    _rep, ver, failed, _c = RL.ledger_state()
    return ver, failed


# ================================================================== rule AG (difference 2)
def ag_map(recs, ann):
    """0 model calls.  Per item: the primary AG v3 decision (all flags) plus the shadow decisions
    of AG v2 and of each v3 flag alone.  SOURCE-SIDE inputs only; no item tag, no label."""
    out = {}
    for r in recs:
        a = ann.get(str(r['sid'])) or {}
        wt = dict((r.get('tags') or {}).get('writer_tags') or {})
        d = {}
        for name, flags in (('v3', AG_FLAGS),) + AG_SHADOWS:
            try:
                dec = AG3.decide(r['sk'], a, wt, r['answer'], r['reference'], 'primary', flags)
            except Exception as e:                                        # never kills a run
                dec = {'fired': False, 'reason': 'AG ERROR: %s' % e, 'error': True}
            cl = dec.get('clause') if isinstance(dec.get('clause'), dict) else None
            d[name] = {'fired': bool(dec.get('fired')), 'reason': dec.get('reason'),
                       'agent': dec.get('agent'), 'agent_kind': dec.get('agent_kind'),
                       'clause_idx': (cl or {}).get('idx'),
                       'answer_is_agentless_passive': bool(dec.get('answer_is_agentless_passive')),
                       'error': bool(dec.get('error'))}
        out[r['item_id']] = d
    return out


def ag_stats(ag):
    st = {'items': len(ag), 'errors': sum(1 for d in ag.values() if d['v3']['error'])}
    for name in ['v3'] + [n for n, _f in AG_SHADOWS]:
        st['fired_' + name] = sum(1 for d in ag.values() if d[name]['fired'])
    st['fired_v3_not_v2'] = sum(1 for d in ag.values() if d['v3']['fired'] and not d['v2']['fired'])
    st['fired_v2_not_v3'] = sum(1 for d in ag.values() if d['v2']['fired'] and not d['v3']['fired'])
    st['abstain_agentless_passive'] = sum(1 for d in ag.values()
                                          if d['v3']['answer_is_agentless_passive']
                                          and not d['v3']['fired'])
    return st


def ag_layer(accepted, layer, fired):
    """AG sits BEFORE L3: its rejection is final.  Attribution follows rescore_1s_c.build() (K3):
    an item a deterministic layer had already rejected keeps that layer."""
    if not fired:
        return bool(accepted), layer
    if (not accepted) and layer not in DET_LAYERS_AFTER_AG:
        return False, layer
    return False, 'AG'


# ================================================================== build / plan (0 calls)
def build(data_dir, tag, purpose, loader=LM):
    cfg, sel = load_cfg()
    st, recs, ann, by, info = R1P.build_side(purpose, data_dir, tag, sel['levers'], loader)
    ag = ag_map(recs, ann)
    info['ag'] = ag_stats(ag)
    say('[AG v3] %s' % json.dumps(info['ag'], sort_keys=True))
    return cfg, sel, st, recs, ann, by, info, ag


def plan_ids(st, recs, ag):
    """The exact 0-call pass: L2 firings, L3-eligible, the AG rejections taken out before L3,
    and what is left to ask the model."""
    lock_rej, l3 = R1P.l3_eligible(st, recs)
    ag_pre = [i for i in l3 if ag[i]['v3']['fired']]
    planned = [i for i in l3 if not ag[i]['v3']['fired']]
    return lock_rej, l3, planned, ag_pre


def preflight(data_dir=None, tag=SIDE_TAG, purpose='Phase 1T preflight (0 calls)', loader=LM):
    cfg, sel, st, recs, ann, by, info, ag = build(data_dir, tag, purpose, loader)
    lock_rej, l3, planned, ag_pre = plan_ids(st, recs, ag)
    say('[PREFLIGHT] L2 lock firings under BASE: %d   L3-eligible under LOCKTIP: %d   '
        'AG v3 rejects before L3: %d   reach L3: %d'
        % (len(lock_rej), len(l3), len(ag_pre), len(planned)))
    if not l3:
        safe_dump({'tag': tag, 'lock_rejections_BASE': len(lock_rej), 'l3_eligible_LOCKTIP': 0,
                   'why': 'L3-eligible 0 — degenerate side (the Phase 1k defect); no model call '
                          'was made'}, STOP_PRE)
        raise SystemExit('STOP: L3-eligible 0, %s written, 0 model calls made' % STOP_PRE)
    if not planned:
        safe_dump({'tag': tag, 'l3_eligible_LOCKTIP': len(l3), 'ag_rejected_before_l3': len(ag_pre),
                   'reach_l3': 0, 'why': 'nothing reaches L3 after the deterministic layers'},
                  STOP_PRE)
        raise SystemExit('STOP: nothing reaches L3, %s written, 0 model calls made' % STOP_PRE)
    assert len(lock_rej) > 0, 'PREFLIGHT: L2 fired 0 times — the measuring apparatus is wrong'
    req, hmap = R1P.plan(st, recs, planned, sel['prompt'])
    ver, failed = verdicts()
    need = [h for h in req if h not in ver and h not in failed]
    done, cap = counted_local(), call_cap()
    say('[PREFLIGHT] unique requests %d   reusable %d   PLANNED NEW CALLS %d   counted so far %d'
        % (len(req), len(req) - len(need), len(need), done))
    if cap is None:
        say('[PREFLIGHT] call_cap is null in FROZEN_CONFIG_1T.json — --final REFUSES until the '
            'owner fixes it.  Planned calls %d.' % (done + len(need)))
    else:
        say('[PREFLIGHT] counted + planned = %d + %d = %d   (cap %d, stop threshold %d)'
            % (done, len(need), done + len(need), cap, cap - 10))
        if done + len(need) > cap - 10:
            safe_dump({'counted': done, 'planned': len(need), 'cap': cap, 'stop_at': cap - 10,
                       'why': 'counted + planned exceeds cap - 10; nothing trimmed, no call made'},
                      STOP_PLAN)
            raise SystemExit('STOP: %d + %d > %d — %s written, 0 calls made'
                             % (done, len(need), cap - 10, STOP_PLAN))
    return dict(cfg=cfg, sel=sel, st=st, recs=recs, ann=ann, by=by, info=info, ag=ag,
                lock_rej=lock_rej, l3=l3, planned=planned, ag_pre=ag_pre, req=req, hmap=hmap,
                need=need)


# ================================================================== calls
def run_calls(req, need, what, call_fn=None, cap_required=True):
    cap = call_cap()
    if cap is None and cap_required:
        raise SystemExit('REFUSED: FROZEN_CONFIG_1T.json has no call_cap — the owner has not fixed '
                         'the cap yet; 0 calls made')
    done = counted_local()
    if cap is not None and done + len(need) > cap:
        safe_dump({'what': what, 'planned_new_calls': len(need), 'already_counted': done,
                   'cap': cap, 'why': 'the plan exceeds the cap; nothing was trimmed and no call '
                                      'was made'}, STOP_PLAN)
        raise SystemExit('STOP: %d + %d > cap %s — %s written, 0 calls made'
                         % (done, len(need), cap, STOP_PLAN))
    if not need:
        return {'ok': 0, 'bad': 0, 'empty': 0, 'skipped': 0, 'wall': False}
    return (call_fn or R1N.make_calls)(req, need)


# ================================================================== rows
def build_rows(recs, res, ag, planned, labels):
    planned = set(planned)
    rows, agg = {}, collections.Counter()
    for r in recs:
        i = r['item_id']
        m = res[i]
        lv = r.get('_lev') or {}
        accept, layer = ag_layer(m['accepted'], m['layer'], ag[i]['v3']['fired'])
        lab = (labels or {}).get(i) or {}
        dropped = lab.get('dropped')
        if dropped in (None, ''):
            dropped = lab.get('agent_drop')
        rows[i] = {
            'sid': r['sid'], 'item_id': i, 'kind': r['kind'], 'half': r['half'],
            'level': r['level'], 'tags': list(r.get('tags_list') or []),
            'writer_passive': r.get('passive'), 'intent': r.get('intent'), 'form': r.get('form'),
            'judged': lab.get('judged'), 'judged_type': lab.get('type'),
            'borderline': bool(lab.get('borderline')), 'dropped': dropped,
            'judge_passive': lab.get('passive'),
            'layers': {'main_layer': m['layer'], 'main_verdict': m['verdict'],
                       'model': m.get('model'), 'model_tip': m.get('model_tip'),
                       'reached_l3': m.get('reached_l3'), 'planned_call': i in planned},
            'ag': ag[i]['v3'],
            'ag_shadow': {n: ag[i][n] for n, _f in AG_SHADOWS},
            'lever2_fired': lv.get('lever2_fired'),
            'lever3': {'variants_shown': len((lv.get('lever3') or {}).get('shown') or []),
                       'variants_removed': len((lv.get('lever3') or {}).get('removed') or []),
                       'removed_detail': (lv.get('lever3') or {}).get('removed')},
            'final_accept': accept, 'final_layer': layer}
        agg['%s/%s' % ('accept' if accept else 'reject', lab.get('judged') or 'unlabelled')] += 1
    return rows, dict(agg)


def headline(rows):
    cov = [sum(1 for x in rows.values() if x['judged'] == 'correct' and x['final_accept']),
           sum(1 for x in rows.values() if x['judged'] == 'correct')]
    fa = [sum(1 for x in rows.values() if x['judged'] == 'wrong' and x['final_accept']),
          sum(1 for x in rows.values() if x['judged'] == 'wrong')]
    return {'coverage_kn': cov, 'fa_kn': fa}


# ================================================================== freeze / floors
def repo_rel(path):
    return os.path.relpath(os.path.abspath(path), RL.REPO).replace(os.sep, '/')


def loaded_py():
    """Every .py of this repository that is loaded in this process — the run's real import set."""
    out = set()
    for m in list(sys.modules.values()):
        f = getattr(m, '__file__', None) or ''
        if f.endswith('.py') and os.path.abspath(f).startswith(os.path.abspath(TOFF) + os.sep):
            out.add(repo_rel(f))
    return sorted(out)


def freeze_list():
    if not os.path.exists(FREEZE_FILES):
        raise SystemExit('REFUSED: %s does not exist.' % FREEZE_FILES)
    return [x.strip() for x in open(FREEZE_FILES, encoding='utf-8').read().splitlines()
            if x.strip() and not x.strip().startswith('#')]


def check_freeze():
    """Every entry of FREEZE_FILES is a path relative to the repository root and must be identical
    to its blob in FREEZE_HASH; and every .py the run actually imported must be in the list."""
    fh_path = os.path.join(HERE, 'FREEZE_HASH')
    if not os.path.exists(fh_path):
        raise SystemExit('REFUSED: %s does not exist — freeze the code first.' % fh_path)
    h = open(fh_path, encoding='utf-8').read().strip().split()[0]
    files = freeze_list()
    missing = [f for f in loaded_py() if f not in files]
    if missing:
        raise SystemExit('REFUSED: imported .py files not in FREEZE_FILES: %s' % ', '.join(missing))
    bad = []
    for f in files:
        p = os.path.join(RL.REPO, f)
        if not os.path.exists(p):
            bad.append({'file': f, 'now': 'ABSENT'})
            continue
        cur = subprocess.check_output(['git', 'hash-object', p], cwd=RL.REPO).decode().strip()
        try:
            was = subprocess.check_output(['git', 'rev-parse', '%s:%s' % (h, f)], cwd=RL.REPO,
                                          stderr=subprocess.DEVNULL).decode().strip()
        except subprocess.CalledProcessError:
            was = None
        if cur != was:
            bad.append({'file': f, 'now': cur[:12], 'at_freeze': (was or 'ABSENT')[:12]})
    if bad:
        raise SystemExit('REFUSED: the code differs from FREEZE_HASH %s: %s' % (h, json.dumps(bad)))
    say('[FREEZE] %d python files identical to commit %s' % (len(files), h))
    return h


def check_floors():
    if not os.path.exists(FLOORS_JSON):
        raise SystemExit('REFUSED: %s does not exist — run floor_check_1t.py first.' % FLOORS_JSON)
    rep = json.load(open(FLOORS_JSON, encoding='utf-8'))
    got, req = rep.get('floors_got') or {}, rep.get('floors_required') or {}
    miss = [k for k in FLOOR_KEYS if k not in got or k not in req]
    if miss:
        raise SystemExit('REFUSED: FLOOR_CHECK_1T.json does not report the five floors: %s' % miss)
    if not rep.get('floors_pass') or rep.get('floors_failed'):
        raise SystemExit('REFUSED: the floors do not hold: %s' % json.dumps(rep.get('floors_failed')))
    say('[FLOORS] all five hold: %s' % json.dumps({k: got[k] for k in FLOOR_KEYS}, sort_keys=True))
    return {k: [got[k], req[k]] for k in FLOOR_KEYS}


# ================================================================== the run (final + dry run)
def final_core(out_dir, data_dir=None, tag=SIDE_TAG, loader=LM, call_fn=None, checks=True,
               crash_at=None, exotic=False, results_name='results_1t.json', labels=True):
    """One code path for --final and the stubbed dry run.  Returns a dict with 'status'."""
    set_run_dir(out_dir)
    if os.path.exists(DONE):
        raise SystemExit('REFUSED: %s exists — the fresh set is measured once.' % DONE)
    fh, floors = None, None
    if checks:
        fh = check_freeze()
        floors = check_floors()
        if call_cap() is None:
            raise SystemExit('REFUSED: FROZEN_CONFIG_1T.json call_cap is null — the owner has not '
                             'fixed the cap; 0 calls made')
    pf = preflight(data_dir, tag, 'Phase 1T final (labels are read last)', loader)
    if pf['info']['n_items'] != FINAL_ITEMS_EXPECTED:
        say('[FINAL] NOTE: %d items, %d expected' % (pf['info']['n_items'], FINAL_ITEMS_EXPECTED))
    made = run_calls(pf['req'], pf['need'], 'final:main', call_fn, cap_required=checks)
    ver, failed = verdicts()
    still = [h for h in pf['req'] if h not in ver and h not in failed]
    if made.get('wall') or still:
        safe_dump({'why': 'the quota wall' if made.get('wall') else 'requests without a verdict',
                   'unique_requests': len(pf['req']), 'still_without_verdict': len(still),
                   'counted_calls_1t': counted_local(),
                   'next': 'rerun --final; every stored verdict is reused by request hash. NO '
                           'judge label was read.'}, PAUSED)
        say('[FINAL] PAUSED: %d requests without a verdict — no label was read.' % len(still))
        return {'status': 'PAUSED', 'still': len(still), 'wall': bool(made.get('wall'))}
    vm = {i: ver[h] for i, h in pf['hmap'].items() if h in ver}
    res, guards = R1P.decide(pf['st'], pf['recs'], pf['ann'], vm)
    if crash_at == 'aggregation':
        raise RuntimeError('SELFTEST: simulated crash inside aggregation, after every reply was '
                           'appended to calls.jsonl')
    lab, lmeta = ({}, {})
    if labels:
        lab, lmeta = LM.load_labels('Phase 1T final scoring', caller='runner_1t.py',
                                    data_dir=data_dir)
    rows, agg = build_rows(pf['recs'], res, pf['ag'], pf['planned'], lab)
    out = {'phase': '1T', 'side': tag, 'freeze_commit': fh, 'floors': floors,
           'frozen_config': pf['cfg'], 'prompt': PROMPT, 'levers': list(LEVERS),
           'ag_rule': {'module': 'phase1t/taskA/agent_drop_v3.py', 'flags': list(AG_FLAGS),
                       'placement': 'with the deterministic guards, BEFORE L3; a rejection is '
                                    'final and costs 0 calls'},
           'model': {'model': P.MODEL, 'temperature': 0, 'thinkingBudget': 0},
           'stub_model': bool(call_fn), 'ts': datetime.datetime.now().isoformat(timespec='seconds'),
           'preflight': {'l2': len(pf['lock_rej']), 'l3_eligible': len(pf['l3']),
                         'ag_rejected_before_l3': len(pf['ag_pre']), 'reach_l3': len(pf['planned'])},
           'build': pf['info'], 'label_meta': lmeta, 'accept_table': agg,
           'headline': headline(rows),
           'calls': {'counted_total_1t': counted_local(), 'unique_main': len(pf['req']),
                     'new_main': len(pf['need']), 'cap': call_cap()},
           'rows': [rows[k] for k in sorted(rows)]}
    if exotic:
        out['selftest_exotic'] = {'a set': {'b', 'a'}, 'a tuple': (1, 2),
                                  'nan': float('nan'), 'bytes': b'\xff\xfe',
                                  'tuple key dict': {(1, 2): 'x', None: 'y', 3.5: 'z'},
                                  'obj': object()}
    safe_dump(out, os.path.join(out_dir, results_name))
    write_md(out, out_dir, results_name)
    write_done_marker(DONE, meta={'phase': '1T', 'freeze_commit': fh,
                                  'coverage': out['headline']['coverage_kn'],
                                  'fa': out['headline']['fa_kn'],
                                  'counted_calls': counted_local(),
                                  'stub_model': bool(call_fn)})
    say('-- FINAL_RUN_DONE written: %s' % DONE)
    out['status'] = 'DONE'
    return out


def write_md(out, out_dir, results_name):
    h = out['headline']
    md = ['# Phase 1T — the fresh set, frozen stack minus lever 1, AG v3 before L3', '',
          '* items **%d**, planned model calls **%d**, AG rejections before L3 **%d**'
          % (out['build']['n_items'], out['preflight']['reach_l3'],
             out['preflight']['ag_rejected_before_l3']),
          '* coverage k/n **%s**, false accepts k/n **%s** (intervals: score_1t.py)'
          % (h['coverage_kn'], h['fa_kn']), '',
          '## AG v3 and its shadows', '', '```',
          json.dumps(out['build']['ag'], indent=1, sort_keys=True), '```', '',
          '## accept table', '', '```', json.dumps(out['accept_table'], indent=1, sort_keys=True),
          '```', '', 'Rows: `%s`.  Every figure with intervals: `python3 score_1t.py`.' % results_name,
          '']
    open(os.path.join(out_dir, results_name.replace('.json', '.md')), 'w',
         encoding='utf-8').write('\n'.join(md))


# ================================================================== modes
def run_preflight(a):
    set_run_dir(HERE)
    pf = preflight(a.data_dir or None)
    mods = loaded_py()
    safe_dump({'ts': datetime.datetime.now().isoformat(timespec='seconds'),
               'n_items': pf['info']['n_items'], 'l2_firings': len(pf['lock_rej']),
               'l3_eligible': len(pf['l3']), 'ag_rejected_before_l3': len(pf['ag_pre']),
               'reach_l3_planned_calls': len(pf['planned']),
               'unique_requests': len(pf['req']), 'new_calls': len(pf['need']),
               'counted_so_far': counted_local(), 'call_cap': call_cap(),
               'ag': pf['info']['ag'], 'levers': pf['info']['levers'],
               'imported_py': mods}, os.path.join(HERE, 'PREFLIGHT_1T.json'))
    open(os.path.join(HERE, 'MODULES_1T.txt'), 'w', encoding='utf-8').write(
        '\n'.join(mods) + '\n')
    say('[PREFLIGHT] PASS — 0 model calls; PREFLIGHT_1T.json + MODULES_1T.txt written')
    return pf


def run_final(a):
    """guarded_run wraps the paid-for path so DONE or CRASHED(+traceback) always exists; the quota
    pause is NOT a crash, so it leaves the guard normally and exits 3 outside it."""
    out = guarded_run(lambda: final_core(HERE, a.data_dir or None), DONE + '.attempt',
                      meta_fn=lambda x: {'status': (x or {}).get('status'),
                                         'rows': len((x or {}).get('rows') or []),
                                         'counted_calls': counted_local()})
    if isinstance(out, dict) and out.get('status') == 'PAUSED':
        say('-- RUN_PAUSED.txt written, exit 3; no label was read.  Rerun --final to resume.')
        raise SystemExit(3)
    return out


# ------------------------------------------------------------------ dry run (0 calls, stub model)
def stub(policy, wall_after=None):
    """A stubbed model: it writes a normal ledger row per reply into calls.jsonl BEFORE anything is
    aggregated, so a crash can be replayed offline with 0 calls."""
    state = {'n': 0}

    def fn(req, need):
        st = {'ok': 0, 'bad': 0, 'empty': 0, 'skipped': 0, 'wall': False}
        for h in sorted(need):
            if st['wall']:
                st['skipped'] += 1
                continue
            _s, _u, _g, hh, variant, iid = req[h]
            if wall_after is not None and state['n'] >= wall_after:
                st['wall'] = True
                st['skipped'] += 1
                continue
            v = policy(iid)
            row = {'ts': datetime.datetime.now().isoformat(timespec='seconds'), 'req_hash': hh,
                   'item_id': iid, 'variant': variant, 'http': 200, 'counted': True,
                   'verdict': v, 'reply': json.dumps({'verdict': v}), 'model': 'STUB',
                   'empty': False, 'latency_ms': 0}
            with open(CALLS, 'a', encoding='utf-8') as fhh:
                fhh.write(json.dumps(row, ensure_ascii=False) + '\n')
                flush_log(fhh)
            state['n'] += 1
            st['ok'] += 1
        return st
    return fn


def policy(iid):
    """Deterministic stub verdicts, by the fixture's item id suffix."""
    if iid.endswith(':tip'):
        return 'TIP'
    if iid.endswith(':diff'):
        return 'DIFF'
    return 'SAME'


def make_fixture(d):
    """A tiny synthetic 1T side (never a measurement): AG-drop rows, an L3 row, a TIP row, a lock
    firing, and labels in the assemble_1t.py schema."""
    os.makedirs(d, exist_ok=True)
    sents = [
        {'sid': 189001, 'slovak': 'Mama upiekla veľkú tortu.', 'level': 'A1', 'topic': 'synthetic',
         'tags': {'half': 'P1', 'kind': 'ACT', 'emb': False, 'tf_gold': 'past',
                  'writer_tags': {'nom_agent': True, 'agent': 'Mama', 'emb_agent': None,
                                  'emb_type': None, 'passivizable': True,
                                  'impersonal_or_passive': False, 'kind': 'ACT', 'emb': False}}},
        {'sid': 189002, 'slovak': 'Peter kontroluje schránku každé ráno.', 'level': 'A2',
         'topic': 'synthetic',
         'tags': {'half': 'P2', 'kind': 'ACT', 'emb': False, 'tf_gold': 'present',
                  'writer_tags': {'nom_agent': True, 'agent': 'Peter', 'emb_agent': None,
                                  'emb_type': None, 'passivizable': True,
                                  'impersonal_or_passive': False, 'kind': 'ACT', 'emb': False}}},
        {'sid': 189003, 'slovak': 'Okno bolo zatvorené pred búrkou.', 'level': 'B1',
         'topic': 'synthetic',
         'tags': {'half': 'P1', 'kind': 'PAS', 'emb': False, 'tf_gold': 'past',
                  'writer_tags': {'nom_agent': False, 'agent': None, 'emb_agent': None,
                                  'emb_type': None, 'passivizable': False,
                                  'impersonal_or_passive': True, 'kind': 'PAS', 'emb': False}}}]
    ann = {
        '189001': {'voice_sk': 'active_agent', 'agent_nom': True, 'tf_gold': 'past',
                   'tense_open': False, 'perfective_present': False,
                   'hygienised': {'id': 189001, 'lv': 'A1', 'lk': ['baked'],
                                  'v': ['Mum baked a big cake.', 'Mother has baked a large cake.']}},
        '189002': {'voice_sk': 'active_agent', 'agent_nom': True, 'tf_gold': 'present',
                   'tense_open': True, 'perfective_present': False,
                   'hygienised': {'id': 189002, 'lv': 'A2', 'lk': ['checks'],
                                  'v': ['Peter checks the letterbox every morning.',
                                        'Every morning Peter checks the letterbox.']}},
        '189003': {'voice_sk': 'passive', 'agent_nom': False, 'tf_gold': 'past',
                   'tense_open': False, 'perfective_present': False,
                   'hygienised': {'id': 189003, 'lv': 'B1', 'lk': ['closed'],
                                  'v': ['The window was closed before the storm.']}}}
    items = [
        {'id': 'W:189001:agdrop', 'sid': 189001, 'kind': 'W', 'intent': 'M', 'form': None,
         'tags': ['agentdrop-main'], 'passive': 'agentless',
         'answer': 'A big cake was baked.'},
        {'id': 'C:189001:same', 'sid': 189001, 'kind': 'C', 'intent': 'C', 'form': None,
         'tags': ['determiner'], 'passive': None, 'answer': 'Mum baked the big cake.'},
        {'id': 'W:189001:tip', 'sid': 189001, 'kind': 'W', 'intent': 'T', 'form': None,
         'tags': ['timeframe'], 'passive': None, 'answer': 'Mum will bake a big cake.'},
        {'id': 'C:189002:same', 'sid': 189002, 'kind': 'C', 'intent': 'C', 'form': None,
         'tags': ['plain'], 'passive': None, 'answer': 'Peter checks a letterbox every morning.'},
        {'id': 'W:189002:agdrop', 'sid': 189002, 'kind': 'W', 'intent': 'M', 'form': None,
         'tags': ['agentdrop-main'], 'passive': 'agentless',
         'answer': 'The letterbox is checked every morning.'},
        {'id': 'W:189002:diff', 'sid': 189002, 'kind': 'W', 'intent': 'M', 'form': None,
         'tags': ['plain'], 'passive': None, 'answer': 'Peter checks the postbox every evening.'},
        {'id': 'C:189003:same', 'sid': 189003, 'kind': 'C', 'intent': 'C', 'form': None,
         'tags': ['skp-passive'], 'passive': 'agentless',
         'answer': 'The window had been closed before the storm.'},
        {'id': 'W:189003:tip', 'sid': 189003, 'kind': 'W', 'intent': 'W', 'form': None,
         'tags': ['skp-passive'], 'passive': 'agentless',
         'answer': 'The window was shut before the storm.'}]
    labels = {}
    for it in items:
        wrong = it['kind'] == 'W'
        labels[it['id']] = {'judged': 'wrong' if wrong else 'correct',
                            'type': it['intent'] if wrong else None,
                            'passive': it['passive'], 'agent_drop': 'Mama' if 'agdrop' in it['id']
                            else None, 'tip': False,
                            'borderline': it['id'] == 'W:189002:agdrop'}
    safe_dump(sents, os.path.join(d, 'sentences.json'))
    safe_dump(ann, os.path.join(d, 'annotations.json'))
    safe_dump(items, os.path.join(d, 'items.json'))
    safe_dump(labels, os.path.join(d, 'labels.json'))
    return d


def _rows_only(path):
    o = json.load(open(path, encoding='utf-8'))
    return o['rows']


def run_dry(a):
    """0 model calls: the whole --final path over a stubbed model, six checks."""
    root = os.path.join(HERE, 'selftest')
    checks, fixture = [], make_fixture(os.path.join(root, 'data'))

    def fresh(name):
        d = os.path.join(root, name)
        if os.path.isdir(d):
            for f in os.listdir(d):
                os.remove(os.path.join(d, f))
        os.makedirs(d, exist_ok=True)
        return d

    def ck(name, ok, detail=''):
        checks.append({'check': name, 'ok': bool(ok), 'detail': str(detail)[:300]})
        say('[DRY-RUN] %-38s %s  %s' % (name, 'PASS' if ok else 'FAIL', str(detail)[:200]))

    # ---- 1. the clean reference run -------------------------------------------------
    d1 = fresh('run_clean')
    out = final_core(d1, fixture, 'synthetic', LM, stub(policy), checks=False, exotic=True)
    rows = {r['item_id']: r for r in out['rows']}
    ag_rej = [r for r in out['rows'] if r['ag']['fired']]
    ck('AG reject path (0 calls, final)',
       ag_rej and all(not r['final_accept'] and not r['layers']['planned_call'] for r in ag_rej)
       and any(r['final_layer'] == 'AG' for r in ag_rej),
       '%d AG rejections, layers %s' % (len(ag_rej),
                                        sorted({r['final_layer'] for r in ag_rej})))
    l3 = [r for r in out['rows'] if r['layers']['planned_call']]
    ck('L3 path reached and accepted',
       any(r['final_accept'] and r['final_layer'] == 'L3' for r in l3),
       '%d planned calls, %d accepted at L3'
       % (len(l3), sum(1 for r in l3 if r['final_accept'] and r['final_layer'] == 'L3')))
    tip = [r for r in out['rows'] if r['final_layer'] == 'L3:TIPrej']
    ck('TIP rejection', tip and all(not r['final_accept'] for r in tip),
       '%d TIP rejections' % len(tip))
    ck('AG shadows recorded (v2 + each flag)',
       all(set(r['ag_shadow']) == {n for n, _f in AG_SHADOWS} for r in out['rows']),
       json.dumps(out['build']['ag'], sort_keys=True))
    ck('exotic JSON keys/values survive the write site',
       'selftest_exotic' in json.load(open(os.path.join(d1, 'results_1t.json'), encoding='utf-8')),
       'safe_dump wrote sets/tuples/NaN/bytes/tuple keys/objects')
    ck('labels are read after the verdicts only',
       _label_line_is_last(os.path.join(d1, 'access_log.jsonl')), 'access_log.jsonl order')

    # ---- 2. quota wall -> pause, then resume ----------------------------------------
    d2 = fresh('run_wall')
    o2 = final_core(d2, fixture, 'synthetic', LM, stub(policy, wall_after=1), checks=False)
    paused = os.path.exists(os.path.join(d2, 'RUN_PAUSED.txt'))
    no_label = not any('labels.json' in ln for ln in
                       open(os.path.join(d2, 'access_log.jsonl'), encoding='utf-8'))
    ck('quota wall pauses before any label read',
       o2.get('status') == 'PAUSED' and paused and no_label
       and not os.path.exists(os.path.join(d2, 'FINAL_RUN_DONE')),
       'status=%s paused_file=%s label_read=%s' % (o2.get('status'), paused, not no_label))
    o2b = final_core(d2, fixture, 'synthetic', LM, stub(policy), checks=False)
    ck('resume finishes without repeating a call',
       o2b.get('status') == 'DONE' and o2b['calls']['counted_total_1t'] == out['calls'][
           'counted_total_1t'],
       'counted after resume %s vs clean %s'
       % (o2b['calls']['counted_total_1t'], out['calls']['counted_total_1t']))

    # ---- 3. crash inside aggregation -> marker, then offline replay -----------------
    d3 = fresh('run_crash')
    crashed = None
    try:
        guarded_run(lambda: final_core(d3, fixture, 'synthetic', LM, stub(policy), checks=False,
                                       crash_at='aggregation'),
                    os.path.join(d3, 'FINAL_RUN_DONE.attempt'),
                    meta_fn=lambda r: {'status': (r or {}).get('status')})
    except Exception as e:
        crashed = e
    mk = os.path.join(d3, 'FINAL_RUN_DONE.attempt')
    mtxt = open(mk, encoding='utf-8').read() if os.path.exists(mk) else ''
    ck('crash in aggregation leaves a CRASHED marker',
       os.path.exists(mk) and 'CRASHED' in mtxt and 'Traceback' in mtxt
       and not os.path.exists(os.path.join(d3, 'FINAL_RUN_DONE')),
       'marker=%s crashed=%s' % (os.path.basename(mk), type(crashed).__name__))
    before = counted_of(os.path.join(d3, 'calls.jsonl'))
    o3 = final_core(d3, fixture, 'synthetic', LM, stub(policy), checks=False)
    after = counted_of(os.path.join(d3, 'calls.jsonl'))
    same = (json.dumps(o3['rows'], sort_keys=True, default=str)
            == json.dumps(out['rows'], sort_keys=True, default=str))
    ck('offline replay: 0 new calls, identical rows',
       o3.get('status') == 'DONE' and before == after and same,
       'calls before/after %d/%d, rows identical %s' % (before, after, same))

    # ---- 4. refusals ----------------------------------------------------------------
    r1 = _refuses(lambda: final_core(d1, fixture, 'synthetic', LM, stub(policy), checks=False))
    ck('a second --final on a finished dir refuses', r1, r1)
    r2 = _refuses(lambda: final_core(fresh('run_cap'), fixture, 'synthetic', LM, None, checks=True))
    ck('--final refuses unless FREEZE_HASH/floors/cap hold', r2, r2)
    set_run_dir(fresh('run_cap'))
    r3 = _refuses(lambda: run_calls({'h': None}, ['h'], 'selftest:cap', None, cap_required=True))
    ck('a null call_cap refuses before any call', 'REFUSED' in r3 and 'call_cap' in r3, r3)

    set_run_dir(HERE)
    rep = {'mode': 'dry run — stubbed model, 0 model calls, 0 network',
           'fixture': os.path.relpath(fixture, TOFF), 'checks': checks,
           'passed': sum(1 for c in checks if c['ok']), 'of': len(checks),
           'clean_run': {'preflight': out['preflight'], 'ag': out['build']['ag'],
                         'accept_table': out['accept_table'], 'headline': out['headline']},
           'imported_py': loaded_py()}
    safe_dump(rep, os.path.join(HERE, 'DRY_RUN_1T.json'))
    say('[DRY-RUN] %d/%d checks passed — DRY_RUN_1T.json written, 0 model calls'
        % (rep['passed'], rep['of']))
    if rep['passed'] != rep['of']:
        raise SystemExit(1)
    return rep


def counted_of(path):
    if not os.path.exists(path):
        return 0
    return sum(1 for row in R.ledger_rows(path) if row.get('counted'))


def _refuses(fn):
    try:
        fn()
    except SystemExit as e:
        return 'SystemExit: %s' % e
    except Exception as e:                                             # pragma: no cover
        return 'UNEXPECTED %s: %s' % (type(e).__name__, e)
    return ''


def _label_line_is_last(path):
    lines = [json.loads(x) for x in open(path, encoding='utf-8') if x.strip()]
    lab = [k for k, r in enumerate(lines) if r['what'] == 'data/labels.json']
    return bool(lab) and lab[0] == len(lines) - 1 or (
        bool(lab) and all(r['what'].startswith('set/') for r in lines[lab[0] + 1:]))


# ================================================================== main
def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--preflight', action='store_true')
    g.add_argument('--dry-run', dest='dry_run', action='store_true')
    g.add_argument('--final', action='store_true')
    ap.add_argument('--data-dir', dest='data_dir', default=None)
    a = ap.parse_args()
    if a.final:
        r = guarded_run(lambda: run_final(a), DONE + '.attempt',
                        meta_fn=lambda x: {'status': (x or {}).get('status'),
                                           'rows': len((x or {}).get('rows') or [])})
        return r
    return (run_preflight if a.preflight else run_dry)(a)


if __name__ == '__main__':
    main()
