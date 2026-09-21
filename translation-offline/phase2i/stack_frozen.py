#!/usr/bin/env python3
"""Phase 2I - the FROZEN 1W stack, called exactly as phase1w/a4/run/runner_1u.py (the 1W runner) calls it.

Nothing is copied: runner_1u.py is imported IN PLACE (read-only) and drives the whole chain:
R1U.build (-> R1T.build -> R1P.build_side, ag_map_1u with stack_1w.decide) -> R1U.plan_ids + R1P.plan
(L3 requests, prompt P-FROZEN-1U) -> [run_2i.py makes the calls] -> R1P.decide (LOCKTIP, TIP-as-rejection,
ROW7 flags) -> R1U.build_rows (AG layer + stack_1w.final_accept: AGv5 rs_nom, tip_det_rule).
Only the 1W runner's side effects are redirected (say() -> stderr, STOP_CHK -> the 2I run dir) and the data come
from memory (MemLoader, same interface as loader_1u) so no earlier-phase file is written.

CLI (run_2i.py spawns one subprocess per stack so the two module graphs never mix):
  stack_frozen.py prepare ITEMS.json OUT.json               -> {jid: {sys, user, gcfg}} (items reaching L3)
  stack_frozen.py finish  ITEMS.json REPLIES.json OUT.json  -> {jid: {accept, layer, tip, l3_reply, l3_calls..}}
  stack_frozen.py native  DATA_DIR VERDICTS.json OUT.json   -> 1W data as stored (test g)
  stack_frozen.py modules OUT.json                          -> the imported .py files
"""
import json, os, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import write_guard  # noqa: E402,F401  stage 2b: every write outside phase2i/ is redirected
TOFF = os.path.dirname(HERE)
RUN_1W = os.path.join(TOFF, 'phase1w', 'a4', 'run')
TAG = 'fresh1u'                                   # runner_1u.SIDE_TAG, as the 1W run used it
VERDICTS = ('SAME', 'TIP', 'DIFF')
ANN_FIELDS = ('agent_nom', 'alt', 'concept_id', 'correct_answer_src', 'embedded_agents', 'en', 'exercise_id',
              'exercise_type_id', 'field_sources', 'flags', 'fragment', 'gender', 'headword', 'language_code',
              'level', 'lk', 'lk_reason', 'lk_supplied', 'lk_verdict', 'main_sentence_index', 'n', 'number',
              'perfective_present', 'person', 'rewrite', 'script_reader_agent', 'script_voice_paths', 'src',
              'subject', 'tense_open', 'tf', 'type_title', 'v', 'voice')
STATE = {'stack': 'frozen', 'R1U': None, 'ann_hook': None, 'post_build': None, 'row_hook': None}


def _say(*a, **k):
    sys.stderr.write(' '.join(str(x) for x in a) + '\n')


def _redirect():
    rd = os.environ.get('P2I_RUN_DIR') or os.path.join(HERE, 'run')
    for m in list(sys.modules.values()):
        f = os.path.abspath(getattr(m, '__file__', None) or '')
        if not f.startswith(TOFF + os.sep):
            continue
        if callable(getattr(m, 'say', None)):
            m.say = _say
        if isinstance(getattr(m, 'STOP_CHK', None), str):
            m.STOP_CHK = os.path.join(rd, 'STOP_CHK_%s.txt' % STATE['stack'])


def load():
    if STATE['R1U'] is None:
        if RUN_1W not in sys.path:
            sys.path.insert(0, RUN_1W)
        import runner_1u as R1U                                                # noqa: E402
        STATE['R1U'] = R1U
        _redirect()
    return STATE['R1U']


def loaded_files():
    out = set()
    for m in list(sys.modules.values()):
        f = getattr(getattr(m, '__spec__', None), 'origin', None) or getattr(m, '__file__', None) or ''
        if f.endswith('.py') and os.path.abspath(f).startswith(TOFF + os.sep):
            out.add(os.path.abspath(f))
    return sorted(out)


class MemLoader(object):
    """loader_1u's interface, from memory (loader_1u would append to phase1w/a4/run/access_log.jsonl)."""
    def __init__(self, sents, ann, items):
        self.s, self.a, self.i = sents, ann, items

    def load_sentences(self, purpose, caller=None, data_dir=None):
        return [dict(x) for x in self.s]

    def load_annotations(self, purpose, caller=None, data_dir=None):
        return self.a

    def load_items(self, purpose, caller=None, data_dir=None):
        return [dict(x) for x in self.i]


def build(sents, ann, items):
    R1U = load()
    if STATE['ann_hook']:
        ann = STATE['ann_hook'](ann)
    cfg, sel, st, recs, ann2, by, info, ag = R1U.build(None, TAG, 'Phase 2I %s stack (0 calls)' % STATE['stack'],
                                                      MemLoader(sents, ann, items))
    if STATE['post_build']:
        STATE['post_build'](st, recs, by)
    lock_rej, l3, planned, ag_pre = R1U.plan_ids(st, recs, ag)
    req, hmap = R1U.R1P.plan(st, recs, planned, sel['prompt'])
    return {'sel': sel, 'st': st, 'recs': recs, 'ann': ann2, 'ag': ag, 'planned': planned, 'req': req,
            'hmap': hmap}


def requests(b):
    return {i: {'sys': b['req'][h][0], 'user': b['req'][h][1], 'gcfg': b['req'][h][2]} for i, h in b['hmap'].items()}


def decide(b, vm, failed_ids=()):
    R1U = load()
    res, _g = R1U.R1P.decide(b['st'], b['recs'], b['ann'], dict(vm))
    failed = {b['hmap'][i]: {'item_id': i, 'why': 'empty or unparsable 200 reply'}
              for i in failed_ids if i in b['hmap']}
    rows, _agg = R1U.build_rows(b['recs'], res, b['ag'], b['planned'], {}, b['hmap'], failed)
    out = {}
    for r in b['recs']:
        i = r['item_id']
        row, m = rows[i], res[i]
        out[i] = {'accept': bool(row['final_accept']), 'layer': row['final_layer'], 'tip': bool(m.get('tip')),
                  'model_tip': bool(m.get('model_tip')), 'main_layer': m.get('layer'),
                  'pre_final_layer': (row.get('stack_in') or {}).get('final_layer'),
                  'ag_fired': bool(b['ag'][i]['primary']['fired']), 'ag_reason': b['ag'][i]['primary']['reason'],
                  'l3_reply': vm.get(i), 'l3_calls': 1 if i in b['hmap'] else 0,
                  'call_failed': bool(row.get('call_failed')), 'reached_l3': bool(m.get('reached_l3')),
                  'req_hash': b['hmap'].get(i)}
    return out


def from_2i(items):
    """2I items -> the 1W data shapes. The annotation conversion is the 2F adapter (adapter_2f.py = verbatim
    p3_probe.alt_dict/build_data), exactly as 2F ran production rows through the 1W stack (stage 2b)."""
    import adapter_2f as A2F
    rows, nat, idmap, seen = [], [], {}, set()
    if len({it['jid'] for it in items}) != len(items):
        raise SystemExit('REFUSED: duplicate jid')
    for k, it in enumerate(items):
        sid = int(it['sid'])
        a = it['annotation'] if isinstance(it.get('annotation'), dict) else \
            {f: it[f] for f in ANN_FIELDS if f in it}
        if sid not in seen:
            seen.add(sid)
            if STATE['row_hook']:
                a = STATE['row_hook'](a)
            rows.append({'sid': sid, 'exercise_id': a.get('exercise_id'), 'level': it['level'],
                         'topic': it.get('topic') or a.get('type_title') or 'general',
                         'slovak': it['slovak'], 'ann': a})
        iid = 'C:%d:j%05d' % (sid, k)
        nat.append({'id': iid, 'sid': sid, 'kind': 'C', 'intent': None, 'form': None, 'tags': [],
                    'passive': None, 'answer': it['answer']})
        idmap[iid] = it['jid']
    rd = os.environ.get('P2I_RUN_DIR') or os.path.join(HERE, 'run')
    sents, ann = A2F.convert(rows, os.path.join(rd, '_adapter_%s' % STATE['stack']))
    return sents, ann, nat, idmap


def prepare_2i(items):
    s, a, n, idm = from_2i(items)
    return {idm[i]: q for i, q in requests(build(s, a, n)).items()}


def finish_2i(items, replies, failed):
    s, a, n, idm = from_2i(items)
    b = build(s, a, n)
    failed = set(failed)
    vm = {i: replies[idm[i]] for i in b['hmap'] if replies.get(idm[i]) in VERDICTS}
    fids = [i for i in b['hmap'] if idm[i] in failed]
    res = decide(b, vm, fids)
    return {idm[i]: r for i, r in res.items() if i not in b['hmap'] or i in vm or idm[i] in failed}


def native(data_dir, verdicts):
    J = lambda f: json.load(open(os.path.join(data_dir, f), encoding='utf-8'))
    b = build(J('sentences.json'), J('annotations.json'), J('items.json'))
    vm = {i: v for i, v in verdicts.items() if v in VERDICTS}
    return decide(b, vm, [i for i in b['hmap'] if i not in vm])


def cli(argv):
    cmd = argv[1]
    if cmd == 'prepare':
        out = prepare_2i(json.load(open(argv[2], encoding='utf-8')))
    elif cmd == 'finish':
        rp = json.load(open(argv[3], encoding='utf-8'))
        out = finish_2i(json.load(open(argv[2], encoding='utf-8')), rp.get('replies') or {}, rp.get('failed') or [])
    elif cmd == 'native':
        out = native(argv[2], json.load(open(argv[3], encoding='utf-8')))
    elif cmd == 'modules':
        load()
        out = loaded_files()
    else:
        raise SystemExit('unknown command %r' % cmd)
    with open(argv[-1], 'w', encoding='utf-8') as fh:
        json.dump(out, fh, ensure_ascii=False, sort_keys=True)


if __name__ == '__main__':
    cli(sys.argv)
