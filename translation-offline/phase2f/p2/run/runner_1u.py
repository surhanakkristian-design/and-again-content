#!/usr/bin/env python3
"""Phase 1U runner - the Phase 1T run (frozen 1Q/1P stack, lever 1 removed, RUNNER_PATCH_1S),
with EXACTLY three changes:

  1. AG v3 -> AG v4  (phase1u/taskA/agent_drop_v4.py, AG.decide(sk, ann, wtags, answer, reference,
     'primary', AG.ALL_FLAGS)), still with the deterministic guards BEFORE L3: a rejection is final
     and costs 0 calls.  v2 / v3 (= v4 flags=()) / guarded union / full v4 are 0-call shadows.
  2. ONE added L3 prompt line, ARTICLE_LINE_1U (the owner's ruling on articles), appended to `ins`
     in build_req_1p AFTER the lever lines and BEFORE the tail.  Wired by monkey-patch from
     phase1u/run; phase1p/runner_1p.py is never edited.  Prompt id P-FROZEN-1U.
  3. the data dir is phase1u/data (sid 190001-190100, 900 items).

Everything else - transport, pacing, quota wall, layers, LOCKTIP, TIP-as-rejection, levers 2/3,
the checker - is imported from runner_1t -> runner_1p -> runner_1n -> runner_1l/runner_1k.

    PYTHONDONTWRITEBYTECODE=1 python3 phase1u/run/runner_1u.py --preflight    # 0 calls
    PYTHONDONTWRITEBYTECODE=1 python3 phase1u/run/runner_1u.py --probe1t 80   # design-only calls
    PYTHONDONTWRITEBYTECODE=1 python3 phase1u/run/runner_1u.py --final        # ONCE, owner only
    PYTHONDONTWRITEBYTECODE=1 python3 phase1u/run/runner_1u.py --dry-run      # 0 calls, stub model
"""
import argparse
import collections
import datetime
import json
import os
import random
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))            # phase2f/p2/run
P1U = os.path.dirname(HERE)                                  # phase2f/p2  (set/, data/, ledger)
TOFF = os.path.expanduser('~/Projects/and-again-content/translation-offline')   # 2F: anchored
P1T_RUN = os.path.join(TOFF, 'phase1t', 'run')
P1P = os.path.join(TOFF, 'phase1p')
P1S = os.path.join(TOFF, 'phase1s')
TASKA = os.path.join(TOFF, 'phase1u', 'taskA')   # 2F: AG v4 home
for _p in (HERE, P1T_RUN, P1P, P1S, TASKA):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import runner_1t as R1T                                                        # noqa: E402
import runner_1p as R1P                                                        # noqa: E402
from safe_json import safe_dump, write_done_marker, guarded_run, flush_log      # noqa: E402
import agent_drop_v4 as AG4                                                    # noqa: E402
import agent_drop_v3 as AG3                                                    # noqa: E402
import loader_1u as LM                                                         # noqa: E402
import article_line_1u as AL                                                   # noqa: E402

RL, R1K, R, P, C, R1N = R1P.RL, R1P.R1K, R1P.R, R1P.P, R1P.C, R1P.R1N

CFG_PATH = os.path.join(HERE, 'FROZEN_CONFIG_1U.json')
FREEZE_FILES = os.path.join(HERE, 'FREEZE_FILES')
FREEZE_HASH = os.path.join(HERE, 'FREEZE_HASH')
SET = os.path.join(P1U, 'set')
FLOORS_JSON = os.path.join(SET, 'floors_1u.json')
FLOORS_ALT = os.path.join(SET, 'FLOOR_CHECK_1U.json')
LEDGER_DEV = os.path.join(P1U, 'ledger_dev.jsonl')
MIRROR_STATE = os.path.join(HERE, 'ledger_mirror_state.json')
SIDE_TAG = 'fresh1u'
PROMPT_1U = 'P-FROZEN-1U'
LEVERS = (2, 3)
CAP_1U = 900                                     # HARD CAP for the whole phase, never narrowed
FINAL_ITEMS_EXPECTED = 900
VERDICTS = ('SAME', 'TIP', 'DIFF')
FLOOR_KEYS_1U = ('F1_agent_drops_wrong', 'F1a_fronted_wrong', 'F1b_misaligned_wrong',
                 'F2_time_frame_wrong', 'F3_by_passive_correct', 'F4_skp_correct',
                 'F5_missing_article_wrong')
# name -> (module, flags).  'primary' is the run's rule; the rest are recorded, never decide.
AG_CFG = collections.OrderedDict([('primary', (AG4, tuple(AG4.ALL_FLAGS))),
                                  ('v2', (AG3, ())),
                                  ('v3', (AG4, ())),
                                  ('guarded_union', (AG4, ('union',))),
                                  ('v4_full', (AG4, tuple(AG4.ALL_FLAGS)))])
AG_SHADOWS_1U = ('v2', 'v3', 'guarded_union', 'v4_full')

CALLS = DONE = PAUSED = STOP_PRE = STOP_PLAN = STOP_CHK = RUNLOG = None


# ================================================================== the prompt (change 2)
def build_req_1u(st, r, prompt_id):
    """build_req_1p verbatim, plus ARTICLE_LINE_1U at the END of `ins`."""
    if prompt_id != PROMPT_1U:
        return R1P.build_req_1p(st, r, prompt_id)
    sysx, user, gcfg, _h = R1N._ORIG_BUILD_REQ(st, r, 'P-FROZEN')
    lines = user.split('\n')
    at = [k for k, ln in enumerate(lines) if ln == P.WORDING_LINE]
    if len(at) != 1:
        raise SystemExit('REFUSED: WORDING_LINE occurs %d times in the P-FROZEN body' % len(at))
    ins = [R1N.VOICE_SAME_LINE] + list(r.get('_extra') or []) + [AL.ARTICLE_LINE_1U]
    lines = lines[:at[0] + 1] + ins + lines[at[0] + 1:]
    user = '\n'.join(lines)
    return sysx, user, gcfg, R.req_hash(sysx, user, gcfg)


R1K.build_req = build_req_1u
if PROMPT_1U not in tuple(getattr(R1K, 'PROMPTS', ())):
    R1K.PROMPTS = tuple(getattr(R1K, 'PROMPTS', ())) + (PROMPT_1U,)


def assert_prompt(st, r):
    """The 1U prompt is the 1T prompt plus EXACTLY the one line, after every lever line and
    immediately before the tail; system text and generation config unchanged."""
    s1, u1, g1, h1 = R1P.build_req_1p(st, r, R1P.PROMPT_1P)
    s2, u2, g2, h2 = build_req_1u(st, r, PROMPT_1U)
    a, b = u1.split('\n'), u2.split('\n')
    fail = []
    if s1 != s2:
        fail.append('the system text differs from the 1T system text')
    if json.dumps(g1, sort_keys=True, default=str) != json.dumps(g2, sort_keys=True, default=str):
        fail.append('the generation config differs')
    if len(b) != len(a) + 1:
        fail.append('the 1U user prompt is %d lines, the 1T prompt %d (+1 expected)'
                    % (len(b), len(a)))
    if b.count(AL.ARTICLE_LINE_1U) != 1:
        fail.append('ARTICLE_LINE_1U occurs %d times' % b.count(AL.ARTICLE_LINE_1U))
    i = b.index(AL.ARTICLE_LINE_1U) if AL.ARTICLE_LINE_1U in b else -1
    if i < 0:
        fail.append('ARTICLE_LINE_1U is not in the built prompt')
    else:
        if b[:i] != a[:i] or b[i + 1:] != a[i:]:
            fail.append('the two prompts differ somewhere else than at the added line')
        extra = list(r.get('_extra') or [])
        want_before = extra[-1] if extra else R1N.VOICE_SAME_LINE
        if b[i - 1] != want_before:
            fail.append('the added line does not stand after the last lever line (before it: %r)'
                        % b[i - 1][:60])
        tail = [x for x in b[i + 1:] if x.strip()]
        if not tail or not tail[0].startswith('SAME'):
            fail.append('the line after the added line is not the frozen tail (%r)'
                        % (tail[0][:40] if tail else None))
        if 'SAME, TIP or DIFF?' not in b:
            fail.append('the frozen tail "SAME, TIP or DIFF?" is gone')
    if h1 == h2:
        fail.append('the request hash did not change - a 1T reply could be replayed')
    if fail:
        raise SystemExit('REFUSED: the prompt assertion failed: %s' % '; '.join(fail))
    rep = {'ok': True, 'item_id': r['item_id'], 'prompt_1t': R1P.PROMPT_1P, 'prompt_1u': PROMPT_1U,
           'lines_1t': len(a), 'lines_1u': len(b), 'added_at_line': i,
           'added_line': AL.ARTICLE_LINE_1U, 'line_before': b[i - 1][:80],
           'line_after': b[i + 1][:80] if i + 1 < len(b) else None,
           'sys_identical': True, 'req_hash_1t': h1[:12], 'req_hash_1u': h2[:12],
           'article_line_check': AL.CHECK,
           'user_sha_1u': AL._sha(u2), 'user_sha_1t': AL._sha(u1)}
    return rep


# ================================================================== run directory / paths
def set_run_dir(d):
    global CALLS, DONE, PAUSED, STOP_PRE, STOP_PLAN, STOP_CHK, RUNLOG
    os.makedirs(d, exist_ok=True)
    R1T.CFG_PATH = CFG_PATH
    R1T.FREEZE_FILES = FREEZE_FILES
    R1T.set_run_dir(d)                                   # re-points every imported write site
    CALLS, DONE = R1T.CALLS, R1T.DONE
    PAUSED, STOP_PRE, STOP_PLAN, STOP_CHK = R1T.PAUSED, R1T.STOP_PRE, R1T.STOP_PLAN, R1T.STOP_CHK
    RUNLOG = os.path.join(d, 'run_1u.log')
    R1T.RUNLOG = R1N.RUNLOG = R1P.RUNLOG = RUNLOG
    RL.FREEZE_HASH = R1P.FREEZE_HASH = FREEZE_HASH
    LM.LOG = os.path.join(d, 'access_log.jsonl')
    return d


def say(line):
    print(line, flush=True)
    with open(RUNLOG, 'a', encoding='utf-8') as fh:
        fh.write(str(line) + '\n')


set_run_dir(HERE)
R1N.say = R1T.say = say


# ================================================================== config
def load_cfg_1u(levers=LEVERS):
    cfg = json.load(open(CFG_PATH, encoding='utf-8')) if os.path.exists(CFG_PATH) else {}
    if list(cfg.get('levers') or LEVERS) != list(LEVERS):
        raise SystemExit('REFUSED: 1U runs levers 2 and 3 only, config says %s' % cfg.get('levers'))
    if cfg.get('ag_rule') not in (None, 'v4'):
        raise SystemExit('REFUSED: 1U runs AG v4, config says %r' % cfg.get('ag_rule'))
    if cfg.get('prompt') not in (None, PROMPT_1U):
        raise SystemExit('REFUSED: 1U runs %s' % PROMPT_1U)
    _c, sel = R1P.load_cfg(LEVERS)
    sel['prompt'] = PROMPT_1U
    return cfg, sel


R1T.load_cfg = load_cfg_1u


# ================================================================== AG v4 (change 1)
def ag_map_1u(recs, ann):
    """0 model calls.  SOURCE-SIDE inputs only; no item tag, no judge label."""
    out = {}
    for r in recs:
        a = ann.get(str(r['sid'])) or {}
        wt = dict((r.get('tags') or {}).get('writer_tags') or {})
        d = {}
        for name, (mod, flags) in AG_CFG.items():
            try:
                dec = mod.decide(r['sk'], a, wt, r['answer'], r['reference'], 'primary', flags)
            except Exception as e:                                        # never kills a run
                dec = {'fired': False, 'reason': 'AG ERROR: %s' % e, 'error': True}
            cl = dec.get('clause') if isinstance(dec.get('clause'), dict) else None
            d[name] = {'fired': bool(dec.get('fired')), 'reason': dec.get('reason'),
                       'agent': dec.get('agent'), 'agent_kind': dec.get('agent_kind'),
                       'clause_idx': (cl or {}).get('idx'),
                       'answer_is_agentless_passive':
                           bool(dec.get('answer_is_agentless_passive')),
                       'error': bool(dec.get('error'))}
        out[r['item_id']] = d
    return out


def ag_stats_1u(ag):
    st = {'items': len(ag), 'errors': sum(1 for d in ag.values() if d['primary']['error'])}
    for name in AG_CFG:
        st['fired_' + name] = sum(1 for d in ag.values() if d[name]['fired'])
    st['fired_v4_not_v3'] = sum(1 for d in ag.values()
                                if d['primary']['fired'] and not d['v3']['fired'])
    st['fired_v3_not_v4'] = sum(1 for d in ag.values()
                                if d['v3']['fired'] and not d['primary']['fired'])
    st['abstain_agentless_passive'] = sum(1 for d in ag.values()
                                          if d['primary']['answer_is_agentless_passive']
                                          and not d['primary']['fired'])
    return st


R1T.ag_map, R1T.ag_stats = ag_map_1u, ag_stats_1u


# ================================================================== ledger / cap
def rows_of(path):
    out = []
    if not os.path.exists(path):
        return out
    for ln in open(path, encoding='utf-8'):
        ln = ln.strip()
        if not ln:
            continue
        try:
            out.append(json.loads(ln))
        except Exception:
            continue
    return out


def ledger_state_1u(path=None):
    """counted = HTTP 200 only.  An empty or unparsable 200 reply is a FAILED call: counted, never
    guessed, never silently retried - the item is scored 'failed' and reported."""
    ver, failed, counted = {}, {}, 0
    for row in rows_of(path or CALLS):
        if row.get('http') != 200:
            continue                                      # retried with backoff, counted:false
        counted += 1
        h, v = row.get('req_hash'), str(row.get('verdict') or '').upper()
        if v in VERDICTS:
            ver[h] = v
            failed.pop(h, None)
        elif h not in ver:
            failed[h] = {'item_id': row.get('item_id'), 'reply': str(row.get('reply'))[:200],
                         'why': 'empty or unparsable 200 reply'}
    return ver, failed, counted


def counted_dev(path=LEDGER_DEV):
    return sum(1 for row in rows_of(path) if row.get('http') == 200)


def _tok(row, *names):
    for n in names:
        if isinstance(row.get(n), int):
            return row[n]
    u = row.get('usage') or {}
    for n in names:
        if isinstance(u.get(n), int):
            return u[n]
    return None


def mirror_to_dev(agent, calls_path=None, dev=LEDGER_DEV, state=MIRROR_STATE):
    """Every counted call of this phase lands in phase1u/ledger_dev.jsonl, so the 900 cap is a
    phase budget and not a per-run one.  Append-only, resumable, never rewrites a line."""
    calls_path = calls_path or CALLS
    st = json.load(open(state, encoding='utf-8')) if os.path.exists(state) else {}
    done = int(st.get(calls_path, 0))
    rows = rows_of(calls_path)
    n = 0
    with open(dev, 'a', encoding='utf-8') as fh:
        for row in rows[done:]:
            fh.write(json.dumps(
                {'ts': row.get('ts'), 'agent': agent, 'item': row.get('item_id'),
                 'http': row.get('http'), 'counted': row.get('http') == 200,
                 'reply': str(row.get('reply'))[:200], 'verdict': row.get('verdict'),
                 'tokens_in': _tok(row, 'tokens_in', 'prompt_tokens', 'promptTokenCount'),
                 'tokens_out': _tok(row, 'tokens_out', 'completion_tokens',
                                    'candidatesTokenCount'),
                 'latency_ms': row.get('latency_ms'), 'req_hash': row.get('req_hash'),
                 'try': row.get('try', 1)}, ensure_ascii=False) + '\n')
            n += 1
        flush_log(fh)
    st[calls_path] = len(rows)
    safe_dump(st, state)
    return n


def cap_check(planned, what):
    """HARD CAP: counted lines in phase1u/ledger_dev.jsonl + planned <= 900.  Scope is NEVER
    narrowed to fit; the runner stops and prints the numbers."""
    spent = counted_dev()
    say('[CAP] %s: counted in ledger_dev %d + planned %d = %d   (hard cap %d)'
        % (what, spent, planned, spent + planned, CAP_1U))
    if spent + planned > CAP_1U:
        safe_dump({'what': what, 'counted_ledger_dev': spent, 'planned': planned,
                   'total': spent + planned, 'cap': CAP_1U,
                   'why': 'counted + planned exceeds the 900-call cap; NOTHING was trimmed, no '
                          'call was made, the scope is not narrowed'}, STOP_PLAN)
        raise SystemExit('STOP: %d + %d = %d > cap %d - %s written, 0 calls made'
                         % (spent, planned, spent + planned, CAP_1U, STOP_PLAN))
    return spent


# ================================================================== floors gate (1U key names)
def check_floors_1u(path=None):
    """The gate reads EXACTLY the SPLIT_1U.md key names.  A misspelt or missing key REFUSES."""
    p = path or (FLOORS_JSON if os.path.exists(FLOORS_JSON) else FLOORS_ALT)
    if not os.path.exists(p):
        raise SystemExit('REFUSED: %s does not exist - run set/floors_1u.py first.' % p)
    rep = json.load(open(p, encoding='utf-8'))
    miss = [k for k in FLOOR_KEYS_1U
            if not isinstance(rep.get(k), dict)
            or any(x not in rep[k] for x in ('n', 'min', 'pass'))]
    if miss:
        raise SystemExit('REFUSED: %s does not report the seven floors under their agreed names '
                         '(missing or malformed: %s); expected %s'
                         % (os.path.basename(p), miss, list(FLOOR_KEYS_1U)))
    if 'all_pass' not in rep:
        raise SystemExit('REFUSED: %s has no "all_pass"' % os.path.basename(p))
    bad = [{'floor': k, 'n': rep[k]['n'], 'min': rep[k]['min']} for k in FLOOR_KEYS_1U
           if not rep[k]['pass'] or rep[k]['n'] < rep[k]['min']]
    if bad or not rep['all_pass']:
        raise SystemExit('REFUSED: the floors do not hold: %s (all_pass=%s)'
                         % (json.dumps(bad), rep.get('all_pass')))
    say('[FLOORS] all seven hold: %s'
        % json.dumps({k: rep[k]['n'] for k in FLOOR_KEYS_1U}, sort_keys=True))
    return {k: [rep[k]['n'], rep[k]['min']] for k in FLOOR_KEYS_1U}


# ================================================================== freeze
def loaded_py():
    out = set()
    for m in list(sys.modules.values()):
        f = getattr(m, '__file__', None) or ''
        if f.endswith('.py') and os.path.abspath(f).startswith(os.path.abspath(TOFF) + os.sep):
            out.add(os.path.relpath(os.path.abspath(f), RL.REPO).replace(os.sep, '/'))
    return sorted(out)


def check_freeze_1u():
    if not os.path.exists(FREEZE_HASH):
        raise SystemExit('REFUSED: %s does not exist - freeze the code first.' % FREEZE_HASH)
    if not os.path.exists(FREEZE_FILES):
        raise SystemExit('REFUSED: %s does not exist.' % FREEZE_FILES)
    h = open(FREEZE_HASH, encoding='utf-8').read().strip().split()[0]
    files = [x.strip() for x in open(FREEZE_FILES, encoding='utf-8').read().splitlines()
             if x.strip() and not x.strip().startswith('#')]
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


# ================================================================== build / plan (0 calls)
def build(data_dir, tag, purpose, loader=LM):
    return R1T.build(data_dir, tag, purpose, loader)           # patched ag_map / load_cfg


def chk_degenerate(info):
    """The 1k defect: one accepting chk class for every record means nothing is being measured."""
    dist = info.get('chk_distribution') or {}
    acc = [k for k in dist if k.split('/')[0] in ('correct', 'correct_with_tip')]
    return len(dist) <= 1 and len(acc) == len(dist) and bool(dist)


def plan_ids(st, recs, ag):
    lock_rej, l3 = R1P.l3_eligible(st, recs)
    ag_pre = [i for i in l3 if ag[i]['primary']['fired']]
    planned = [i for i in l3 if not ag[i]['primary']['fired']]
    return lock_rej, l3, planned, ag_pre


def preflight(data_dir=None, tag=SIDE_TAG, purpose='Phase 1U preflight (0 calls)', loader=LM,
              cap=True):
    cfg, sel, st, recs, ann, by, info, ag = build(data_dir, tag, purpose, loader)
    pa = assert_prompt(st, recs[0])
    say('[PROMPT] P-FROZEN-1U = P-FROZEN-1P + 1 line at index %d; sys identical; hash %s -> %s'
        % (pa['added_at_line'], pa['req_hash_1t'], pa['req_hash_1u']))
    lock_rej, l3, planned, ag_pre = plan_ids(st, recs, ag)
    say('[PREFLIGHT] L2 lock firings under BASE: %d   L3-eligible under LOCKTIP: %d   '
        'AG v4 rejects before L3: %d   reach L3: %d'
        % (len(lock_rej), len(l3), len(ag_pre), len(planned)))
    if chk_degenerate(info):
        safe_dump({'tag': tag, 'why': 'every record carries the same ACCEPTING chk - degenerate '
                                      'apparatus; no model call was made',
                   'chk_distribution': info.get('chk_distribution')}, STOP_CHK)
        raise SystemExit('STOP: degenerate chk, %s written, 0 model calls made' % STOP_CHK)
    if not l3:
        safe_dump({'tag': tag, 'lock_rejections_BASE': len(lock_rej), 'l3_eligible_LOCKTIP': 0,
                   'why': 'L3-eligible 0 - degenerate side (the Phase 1k defect); no model call '
                          'was made'}, STOP_PRE)
        raise SystemExit('STOP: L3-eligible 0, %s written, 0 model calls made' % STOP_PRE)
    if not planned:
        safe_dump({'tag': tag, 'l3_eligible_LOCKTIP': len(l3), 'ag_rejected_before_l3': len(ag_pre),
                   'reach_l3': 0, 'why': 'nothing reaches L3 after the deterministic layers'},
                  STOP_PRE)
        raise SystemExit('STOP: nothing reaches L3, %s written, 0 model calls made' % STOP_PRE)
    assert len(lock_rej) > 0, 'PREFLIGHT: L2 fired 0 times - the measuring apparatus is wrong'
    req, hmap = R1P.plan(st, recs, planned, sel['prompt'])
    ver, failed, counted = ledger_state_1u()
    need = [h for h in req if h not in ver and h not in failed]
    say('[PREFLIGHT] unique requests %d   reusable %d   PLANNED NEW CALLS %d   counted here %d   '
        'failed(200, unparsable) %d' % (len(req), len(req) - len(need), len(need), counted,
                                        len(failed)))
    if cap:
        cap_check(len(need), 'preflight')
    return dict(cfg=cfg, sel=sel, st=st, recs=recs, ann=ann, by=by, info=info, ag=ag,
                lock_rej=lock_rej, l3=l3, planned=planned, ag_pre=ag_pre, req=req, hmap=hmap,
                need=need, failed=failed, prompt_assertion=pa)


# ================================================================== rows
def build_rows(recs, res, ag, planned, labels, hmap, failed):
    planned = set(planned)
    rows, agg = {}, collections.Counter()
    for r in recs:
        i = r['item_id']
        m = res[i]
        lv = r.get('_lev') or {}
        accept, layer = R1T.ag_layer(m['accepted'], m['layer'], ag[i]['primary']['fired'])
        lab = (labels or {}).get(i) or {}
        h = hmap.get(i)
        bad = h in failed
        rows[i] = {
            'sid': r['sid'], 'item_id': i, 'kind': r['kind'], 'half': r['half'],
            'level': r['level'], 'tags': list(r.get('tags_list') or []),
            'writer_passive': r.get('passive'), 'intent': r.get('intent'), 'form': r.get('form'),
            'sk': r['sk'], 'answer': r['answer'], 'reference': r['reference'],
            'judged': lab.get('judged'), 'judged_type': lab.get('type'),
            'borderline': bool(lab.get('borderline')), 'confidence': lab.get('confidence'),
            'packet_part': lab.get('packet_part'), 'packet_position': lab.get('packet_position'),
            'dropped': lab.get('dropped'), 'judge_passive': lab.get('passive'),
            'layers': {'main_layer': m['layer'], 'main_verdict': m['verdict'],
                       'model': m.get('model'), 'model_tip': m.get('model_tip'),
                       'reached_l3': m.get('reached_l3'), 'planned_call': i in planned,
                       'req_hash': h},
            'call_failed': bool(bad),
            'call_failed_detail': failed.get(h) if bad else None,
            'ag': ag[i]['primary'],
            'ag_shadow': {n: ag[i][n] for n in AG_SHADOWS_1U},
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
    return {'coverage_kn': cov, 'fa_kn': fa,
            'failed_calls': sum(1 for x in rows.values() if x['call_failed'])}


def call_meta(path=None):
    rows = [r for r in rows_of(path or CALLS) if r.get('http') == 200]
    ti = [_tok(r, 'tokens_in', 'prompt_tokens', 'promptTokenCount') or 0 for r in rows]
    to = [_tok(r, 'tokens_out', 'completion_tokens', 'candidatesTokenCount') or 0 for r in rows]
    lat = [r.get('latency_ms') or 0 for r in rows]
    return {'counted_calls': len(rows), 'tokens_in': sum(ti), 'tokens_out': sum(to),
            'latency_ms_total': sum(lat),
            'latency_ms_mean': round(sum(lat) / len(lat), 1) if lat else None,
            'http_other': collections.Counter(str(r.get('http')) for r in rows_of(path or CALLS)
                                              if r.get('http') != 200)}


# ================================================================== the run
def final_core(out_dir, data_dir=None, tag=SIDE_TAG, loader=LM, call_fn=None, checks=True,
               crash_at=None, results_name='results_1u.json', labels=True, resume=False,
               offline=False):
    set_run_dir(out_dir)
    if os.path.exists(DONE):
        raise SystemExit('REFUSED: %s exists - the fresh set is measured once.' % DONE)
    if os.path.exists(CALLS) and not (resume or offline):
        raise SystemExit('REFUSED: %s already holds verdicts - a second --final is refused.  Use '
                         '--resume after a documented pause, or score_1u.py --recover to recompute '
                         'from the stored verdicts with 0 calls.' % CALLS)
    fh, floors = None, None
    if checks:
        fh = check_freeze_1u()
        floors = check_floors_1u()
    pf = preflight(data_dir, tag, 'Phase 1U final (labels are read last)', loader, cap=checks)
    if pf['info']['n_items'] != FINAL_ITEMS_EXPECTED:
        say('[FINAL] NOTE: %d items, %d expected' % (pf['info']['n_items'], FINAL_ITEMS_EXPECTED))
    if offline and pf['need']:
        raise SystemExit('REFUSED: recovery mode, but %d requests have no stored verdict'
                         % len(pf['need']))
    made = (call_fn or R1N.make_calls)(pf['req'], pf['need']) if pf['need'] else \
        {'ok': 0, 'bad': 0, 'empty': 0, 'skipped': 0, 'wall': False}
    mirrored = mirror_to_dev('final_1u') if not offline else 0
    ver, failed, counted = ledger_state_1u()
    still = [h for h in pf['req'] if h not in ver and h not in failed]
    if made.get('wall') or still:
        safe_dump({'why': 'the quota wall' if made.get('wall') else 'requests without a verdict',
                   'unique_requests': len(pf['req']), 'still_without_verdict': len(still),
                   'counted_calls_1u': counted, 'mirrored_to_ledger_dev': mirrored,
                   'next': 'rerun --final --resume; every stored verdict is reused by request '
                           'hash.  NO judge label was read.'}, PAUSED)
        say('[FINAL] PAUSED: %d requests without a verdict - no label was read.' % len(still))
        return {'status': 'PAUSED', 'still': len(still), 'wall': bool(made.get('wall'))}
    safe_dump({i: ver.get(h) for i, h in pf['hmap'].items()},
              os.path.join(out_dir, 'verdicts_1u.json'))
    vm = {i: ver[h] for i, h in pf['hmap'].items() if h in ver}
    res, guards = R1P.decide(pf['st'], pf['recs'], pf['ann'], vm)
    if crash_at == 'aggregation':
        raise RuntimeError('SELFTEST: simulated crash inside aggregation, after every reply was '
                           'appended to calls.jsonl')
    lab, lmeta = ({}, {})
    if labels:
        lab, lmeta = LM.load_labels('Phase 1U final scoring', caller='runner_1u.py',
                                    data_dir=data_dir)
    rows, agg = build_rows(pf['recs'], res, pf['ag'], pf['planned'], lab, pf['hmap'], failed)
    out = {'phase': '1U', 'side': tag, 'freeze_commit': fh, 'floors': floors,
           'frozen_config': pf['cfg'], 'prompt': PROMPT_1U,
           'prompt_assertion': pf['prompt_assertion'], 'levers': list(LEVERS),
           'ag_rule': {'module': 'phase1u/taskA/agent_drop_v4.py',
                       'flags': list(AG4.ALL_FLAGS),
                       'shadows': list(AG_SHADOWS_1U),
                       'placement': 'with the deterministic guards, BEFORE L3; a rejection is '
                                    'final and costs 0 calls'},
           'model': {'model': P.MODEL, 'temperature': 0, 'thinkingBudget': 0},
           'stub_model': bool(call_fn), 'ts': datetime.datetime.now().isoformat(timespec='seconds'),
           'preflight': {'l2': len(pf['lock_rej']), 'l3_eligible': len(pf['l3']),
                         'ag_rejected_before_l3': len(pf['ag_pre']),
                         'reach_l3': len(pf['planned'])},
           'build': pf['info'], 'label_meta': lmeta, 'accept_table': agg,
           'headline': headline(rows),
           'failed_calls': [dict(failed[h], req_hash=h) for h in failed],
           'calls': dict(call_meta(), unique_main=len(pf['req']), new_main=len(pf['need']),
                         cap=CAP_1U, counted_ledger_dev=counted_dev(),
                         mirrored_to_ledger_dev=mirrored),
           'rows': [rows[k] for k in sorted(rows)]}
    safe_dump(out, os.path.join(out_dir, results_name))
    open(os.path.join(out_dir, results_name.replace('.json', '.md')), 'w',
         encoding='utf-8').write(
        '# Phase 1U - the fresh set (AG v4, P-FROZEN-1U)\n\n'
        '* items %d, planned model calls %d, AG rejections before L3 %d, failed calls %d\n'
        '* coverage k/n %s, false accepts k/n %s (intervals: score_1u.py)\n'
        % (out['build']['n_items'], out['preflight']['reach_l3'],
           out['preflight']['ag_rejected_before_l3'], out['headline']['failed_calls'],
           out['headline']['coverage_kn'], out['headline']['fa_kn']))
    write_done_marker(DONE, meta={'phase': '1U', 'freeze_commit': fh,
                                  'coverage': out['headline']['coverage_kn'],
                                  'fa': out['headline']['fa_kn'], 'counted_calls': counted,
                                  'stub_model': bool(call_fn)})
    say('-- FINAL_RUN_DONE written: %s' % DONE)
    out['status'] = 'DONE'
    return out


# ================================================================== probe (design only)
def probe1t(n=80, out_dir=None, call_fn=None):
    """Re-send closed-1T items through the NEW prompt and tabulate the flips.  Informs the report
    only: the ruling line is the owner's order and is used whatever the probe says."""
    out_dir = out_dir or os.path.join(HERE, 'probe')
    set_run_dir(out_dir)
    if n > 100:
        raise SystemExit('REFUSED: the probe is capped at 100 items')
    data = os.path.join(P1U, 'taskR', 'data_restored')
    pairs = json.load(open(os.path.join(P1U, 'taskR', 'article_pairs.json'),
                           encoding='utf-8'))['pairs']
    art = [p['id'] for p in pairs]
    res1t = json.load(open(os.path.join(P1T_RUN, 'results_1t.json'), encoding='utf-8'))
    stored = {r['item_id']: (r['layers'] or {}).get('model') for r in res1t['rows']
              if (r['layers'] or {}).get('reached_l3')}
    cfg, sel, st, recs, ann, by, info, ag = build(data, 'probe1t',
                                                  'Phase 1U probe of the 1T set (design only)')
    have = {r['item_id'] for r in recs}
    ids = [i for i in art if i in have]
    pool = sorted([i for i in stored if i in have and i not in ids])
    ids += random.Random(20260920).sample(pool, max(0, min(n - len(ids), len(pool))))
    say('[PROBE] %d items (%d article-only, %d seeded 1T L3 sample)'
        % (len(ids), len([i for i in art if i in have]), len(ids) - len([i for i in art if i in have])))
    assert_prompt(st, by[ids[0]])
    req, hmap = R1P.plan(st, recs, ids, PROMPT_1U)
    ver, failed, _c = ledger_state_1u()
    need = [h for h in req if h not in ver and h not in failed]
    cap_check(len(need), 'probe1t')
    if need:
        (call_fn or R1N.make_calls)(req, need)
        mirror_to_dev('probe1t')
    ver, failed, counted = ledger_state_1u()
    tab, per = collections.Counter(), []
    for i in ids:
        new = ver.get(hmap[i])
        old = stored.get(i)
        flip = ('FAILED' if hmap[i] in failed else
                'NEW' if old is None else 'SAME_VERDICT' if new == old else '%s->%s' % (old, new))
        tab[flip] += 1
        tab['new:%s' % new] += 1
        per.append({'item_id': i, 'article_only': i in art, 'verdict_1t': old, 'verdict_1u': new,
                    'flip': flip, 'answer': by[i]['answer'], 'sk': by[i]['sk']})
    rep = {'phase': '1U', 'mode': 'probe1t (design only, informs the report; the ruling line is '
                                 'the owner order and is used whatever the probe says)',
           'n': len(ids), 'article_items': len([p for p in per if p['article_only']]),
           'table': dict(tab),
           'article_table': dict(collections.Counter(p['flip'] for p in per if p['article_only'])),
           'sample_table': dict(collections.Counter(p['flip'] for p in per
                                                    if not p['article_only'])),
           'calls': call_meta(), 'counted_ledger_dev': counted_dev(), 'items': per}
    safe_dump(rep, os.path.join(HERE, 'PROBE_1T_1U.json'))
    open(os.path.join(HERE, 'PROBE_1T_1U.md'), 'w', encoding='utf-8').write(
        '# Phase 1U probe of the closed 1T items under P-FROZEN-1U\n\n'
        '* %d items (%d article-only minimal-pair bare forms, seed 20260920)\n* flips: %s\n'
        '* article-only: %s\n* seeded 1T L3 sample: %s\n\nDesign only - no 1U result.\n'
        % (rep['n'], rep['article_items'], json.dumps(rep['table'], sort_keys=True),
           json.dumps(rep['article_table'], sort_keys=True),
           json.dumps(rep['sample_table'], sort_keys=True)))
    say('[PROBE] %s' % json.dumps(rep['table'], sort_keys=True))
    return rep


# ================================================================== modes
def run_preflight(a):
    set_run_dir(HERE)
    pf = preflight(a.data_dir or None)
    mods = loaded_py()
    safe_dump({'ts': datetime.datetime.now().isoformat(timespec='seconds'),
               'n_items': pf['info']['n_items'], 'l2_firings': len(pf['lock_rej']),
               'l3_eligible': len(pf['l3']), 'ag_rejected_before_l3': len(pf['ag_pre']),
               'reach_l3_planned_calls': len(pf['planned']),
               'unique_requests': len(pf['req']), 'PLANNED_CALLS': len(pf['need']),
               'counted_ledger_dev': counted_dev(), 'cap': CAP_1U,
               'chk': pf['info'].get('chk_distribution'),
               'chk_computed': pf['info'].get('chk_computed'),
               'ag': pf['info']['ag'], 'levers': pf['info']['levers'],
               'prompt_assertion': pf['prompt_assertion'],
               'imported_py': mods}, os.path.join(HERE, 'PREFLIGHT_1U.json'))
    open(os.path.join(HERE, 'MODULES_1U.txt'), 'w', encoding='utf-8').write('\n'.join(mods) + '\n')
    say('[PREFLIGHT] PASS - 0 model calls; PREFLIGHT_1U.json + MODULES_1U.txt written')
    return pf


def run_final(a):
    out = guarded_run(lambda: final_core(HERE, a.data_dir or None, resume=a.resume),
                      DONE + '.attempt',
                      meta_fn=lambda x: {'status': (x or {}).get('status'),
                                         'rows': len((x or {}).get('rows') or [])})
    if isinstance(out, dict) and out.get('status') == 'PAUSED':
        say('-- RUN_PAUSED.txt written, exit 3; no label was read.  Rerun --final --resume.')
        raise SystemExit(3)
    return out


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--preflight', action='store_true')
    g.add_argument('--final', action='store_true')
    g.add_argument('--probe1t', type=int, default=None)
    g.add_argument('--dry-run', dest='dry_run', action='store_true')
    ap.add_argument('--data-dir', dest='data_dir', default=None)
    ap.add_argument('--resume', action='store_true')
    a = ap.parse_args()
    if a.final:
        return guarded_run(lambda: run_final(a), DONE + '.attempt',
                           meta_fn=lambda x: {'status': (x or {}).get('status')})
    if a.probe1t is not None:
        return probe1t(a.probe1t)
    if a.dry_run:
        import selftest_1u_run as S
        return S.main()
    return run_preflight(a)



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


if __name__ == '__main__':
    main()
