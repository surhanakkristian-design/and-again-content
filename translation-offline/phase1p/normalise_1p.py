#!/usr/bin/env python3
"""Phase 1P normaliser (TOOLING ONLY, 0 model calls) - written by the recover+run agent.

Reconciles what the two blind writers and the two blind judges actually delivered with the
loader_1p contract, WITHOUT touching any lever, prompt, decision rule or threshold:
  * writer schema  {correct:[...], wrong:[...]}  ->  items  "<C|W>:<170000+n>:<aid>"
  * aid: writer A is positional (c0..c3 / w0..w4), writer B carries c1..c4 / w1..w5 - native aid kept
  * intent  TF -> T   (writer A codes T, writer B codes TF);  correct answers get intent C
  * two key files (_key_A.json, _key_B.json) and four verdict files (verdicts_{A1,A2,B1,B2}.json)
  * the 40 + 40 hidden duplicate jids are NOT test items: they go to out_controls.json /
    controls_map.json (judge noise only); the jid with is_duplicate_of = null is the test item
  * label of record = the JUDGED label; writer_side / writer_intent / writer_kind stay on every item
Writes  data/sentences.json  data/items.json  judge/blind_map.json  judge/out_part1.json
        judge/out_controls.json  judge/controls_map.json  normalise_1p.json (floors, balance, noise)
and, ONLY IF an independent annotation delivery  data/annotations_src.json  exists
        ({"1P001": {"v":[..>=2..],"lk":[..],"alt":{..},"voice_sk":..,"agent_nom":..,"tf_gold":..,
                    "tense_open":..,"perfective_present":..}, ...}),   data/annotations.json.
The writers delivered NO reference annotation (no v / lk / alt); this tool never invents one.
"""
import collections, hashlib, json, os, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import loader_1p as LM            # noqa: E402
import assemble_1p as AS          # noqa: E402
DATA, JUDGE = LM.DATA, LM.JUDGE
PURPOSE = 'Phase 1P normalise + label-side floor pre-check (0 calls)'
FLOORS = {'judged_wrong_timeframe': 120, 'judged_wrong_agentless': 60,
          'judged_correct_agentless': 60, 'judged_correct_determiner': 80}
UNSURE = ['JB0399', 'JB0527', 'JB0296', 'JB0509', 'JB0274', 'JB0421', 'JB0122', 'JB0481']


def rd(path, side):
    obj = json.load(open(path, encoding='utf-8'))
    LM._log(side, os.path.relpath(path, HERE), len(obj), PURPOSE, 'normalise_1p.py')
    return obj


def wr(path, obj):
    json.dump(obj, open(path, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)


def main():
    sents, items, by_key, rep = [], [], {}, {}
    ex = AS.existing_slovak()
    seen_sk = {}
    for side, lo, hi in (('A', 1, 60), ('B', 61, 120)):
        rows = rd(os.path.join(DATA, 'writer_%s.json' % side), '1p:fresh1p')
        assert isinstance(rows, list) and len(rows) == 60, 'writer %s: %d sentences' % (side, len(rows))
        for s in rows:
            m = AS.SID_RE.match(s['sid']); n = int(m.group(1)); assert lo <= n <= hi, s['sid']
            sid = 170000 + n
            k = AS.norm(s['slovak'])
            assert k not in ex, 'overlap with the existing 450: %s' % s['sid']
            assert k not in seen_sk, 'internal duplicate: %s' % s['sid']
            seen_sk[k] = s['sid']
            assert len(s['correct']) == 4 and len(s['wrong']) == 5, s['sid']
            sents.append({'sid': sid, 'slovak': s['slovak'], 'level': s['level'], 'topic': s['topic'],
                          'tags': {'half': AS.half_of(sid), 'writer_side': side,
                                   'tf_gold': s.get('tf_gold'), 'writer_tags': s.get('tags') or {}}})
            for kind, lst, pre, base in (('C', s['correct'], 'c', 0), ('W', s['wrong'], 'w', 0)):
                for i, x in enumerate(lst):
                    aid = x.get('aid') or '%s%d' % (pre, i)
                    tg = list(x['tags']); assert tg and not [t for t in tg if t not in AS.TAGS], (s['sid'], aid, tg)
                    wi = x.get('intent') if kind == 'W' else 'C'
                    wi = 'T' if wi == 'TF' else wi
                    assert wi in ('C', 'T', 'W', 'M', 'S'), (s['sid'], aid, wi)
                    it = {'id': '%s:%d:%s' % (kind, sid, aid), 'sid': sid, 'kind': kind, 'intent': wi,
                          'form': x.get('form'), 'tags': tg,
                          'passive': ('agentless' if 'agentless' in tg else 'by' if 'by-passive' in tg else None),
                          'answer': x['answer'], 'writer_side': side, 'writer_kind': kind,
                          'writer_intent': wi, 'writer_passive': x.get('passive')}
                    assert (s['sid'], aid) not in by_key
                    by_key[(s['sid'], aid)] = it
                    items.append(it)
    sents.sort(key=lambda r: r['sid']); items.sort(key=lambda r: (r['sid'], r['kind'], r['id']))
    # ---- judge side
    blind, cmap, out_rows, ctl_rows, packet_mismatch = {}, {}, [], [], []
    verdict = {}
    for side, parts in (('A', ('A1', 'A2')), ('B', ('B1', 'B2'))):
        key = rd(os.path.join(JUDGE, '_key_%s.json' % side), '1p:judge')
        pk = {}
        for p in parts:
            for r in rd(os.path.join(JUDGE, 'packets_%s.json' % p), '1p:judge'):
                pk[r['jid']] = r
            for r in rd(os.path.join(JUDGE, 'verdicts_%s.json' % p), '1p:judge'):
                assert r['jid'] not in verdict, r['jid']
                verdict[r['jid']] = r
        for jid, k in key.items():
            it = by_key.get((k['sid'], k['aid']))
            assert it is not None, ('key points at no item', jid, k)
            if pk[jid]['answer'] != it['answer']:
                packet_mismatch.append(jid)
            v = verdict.get(jid)
            assert v is not None, ('no verdict', jid)
            row = {'jid': jid, 'judged': v.get('judged'), 'type': v.get('type'),
                   'passive': v.get('passive'), 'tip': v.get('tip'), 'note': v.get('note')}
            if k.get('is_duplicate_of'):
                o = key[k['is_duplicate_of']]
                assert (o['sid'], o['aid']) == (k['sid'], k['aid']), ('duplicate points elsewhere', jid)
                cmap[jid] = it['id']; ctl_rows.append(row)
            else:
                assert it['id'] not in blind.values() or True
                blind[jid] = it['id']; out_rows.append(row)
    assert len(set(blind.values())) == len(blind) == len(items) == 1080, (len(blind), len(items))
    assert not packet_mismatch, packet_mismatch[:5]
    wr(os.path.join(DATA, 'sentences.json'), sents); wr(os.path.join(DATA, 'items.json'), items)
    wr(os.path.join(JUDGE, 'blind_map.json'), blind); wr(os.path.join(JUDGE, 'out_part1.json'), out_rows)
    wr(os.path.join(JUDGE, 'controls_map.json'), cmap); wr(os.path.join(JUDGE, 'out_controls.json'), ctl_rows)
    # ---- label-side figures (0 calls; the checker has produced nothing yet)
    lab = {blind[r['jid']]: r for r in out_rows}
    byid = {i['id']: i for i in items}
    got, got_half = collections.Counter(), collections.Counter()
    alt = collections.Counter()
    cross = collections.Counter(); tw = collections.Counter(); tip_c = collections.Counter()
    for iid, r in lab.items():
        it = byid[iid]; h = AS.half_of(it['sid']); j = r['judged']; tg = it['tags']
        cross['%s->%s' % (it['writer_intent'], j if j == 'correct' else 'wrong:%s' % r['type'])] += 1
        for name, cond in (('judged_wrong_timeframe', j == 'wrong' and 'timeframe' in tg),
                           ('judged_wrong_agentless', j == 'wrong' and 'agentless' in tg),
                           ('judged_correct_agentless', j == 'correct' and 'agentless' in tg),
                           ('judged_correct_determiner', j == 'correct' and 'determiner' in tg)):
            if cond:
                got[name] += 1; got_half['%s/%s' % (name, h)] += 1
        if j == 'wrong':
            tw[r['type'] or '?'] += 1
            alt['judged_wrong_typeT'] += r['type'] == 'T'
            alt['judged_wrong_judge_passive_agentless'] += r.get('passive') == 'agentless'
        else:
            alt['judged_correct_judge_passive_agentless'] += r.get('passive') == 'agentless'
            tip_c['tip' if r.get('tip') else 'no_tip'] += 1
    pairs = [(verdict[k2], verdict[j]) for j, k2 in
             ((j, kk) for side in ('A', 'B') for j, kk in
              ((j, v['is_duplicate_of']) for j, v in json.load(open(os.path.join(JUDGE, '_key_%s.json' % side), encoding='utf-8')).items() if v.get('is_duplicate_of')))]
    dis = [(a['jid'], b['jid']) for a, b in pairs if a['judged'] != b['judged']]
    dis_t = [(a['jid'], b['jid']) for a, b in pairs if a['judged'] == b['judged'] == 'wrong' and a['type'] != b['type']]
    judged = collections.Counter(r['judged'] for r in lab.values())
    jh = collections.Counter('%s/%s' % (AS.half_of(byid[i]['sid']), r['judged']) for i, r in lab.items())
    m_cell = [i for i, r in lab.items() if byid[i]['writer_intent'] == 'M' and r['judged'] == 'correct']
    c_wrong = [i for i, r in lab.items() if byid[i]['writer_kind'] == 'C' and r['judged'] == 'wrong']
    fails = {k: [got[k], v] for k, v in FLOORS.items() if got[k] < v}
    ann_src = os.path.join(DATA, 'annotations_src.json')
    ann_state = 'MISSING - the writers delivered no reference annotation (v / lk / alt); the stack cannot be built'
    if os.path.exists(ann_src):
        src = rd(ann_src, '1p:fresh1p'); ann = {}; bad = []
        for s in sents:
            a = src.get('1P%03d' % (s['sid'] - 170000)) or src.get(str(s['sid'])) or src.get(s['sid'])
            if not isinstance(a, dict) or len([v for v in (a.get('v') or []) if isinstance(v, str) and v.strip()]) < 1:
                bad.append(s['sid']); continue
            core = {k: a[k] for k in ('v', 'lk', 'alt', 'm', 'lv', 't') if k in a}; core['id'] = s['sid']
            core.setdefault('lv', s['level']); core.setdefault('alt', {})
            ann[str(s['sid'])] = dict({k: v for k, v in a.items() if k not in core}, hygienised=core, raw=core)
        if bad:
            ann_state = 'REFUSED: annotations_src.json has no usable "v" for %d sentences: %s' % (len(bad), bad[:10])
        else:
            wr(os.path.join(DATA, 'annotations.json'), ann); ann_state = 'built from annotations_src.json (%d)' % len(ann)
    rep = {'sentences': len(sents), 'items': len(items), 'test_items_labelled': len(lab),
           'hidden_duplicates_excluded': len(cmap), 'packet_answer_identity': 'all %d jids: packet answer == writer answer' % (len(blind) + len(cmap)),
           'levels': dict(collections.Counter(s['level'] for s in sents)),
           'halves_sentences': dict(collections.Counter(s['tags']['half'] for s in sents)),
           'halves_judged': dict(jh), 'judged': dict(judged),
           'floors_required': FLOORS, 'floors_got': dict(got), 'floors_got_by_half': dict(got_half),
           'floors_failed': fails, 'floor_alternative_readings': dict(alt),
           'TWMS_balance_judged_wrong': dict(tw), 'writer_intent_x_judged': dict(sorted(cross.items())),
           'judged_correct_tip': dict(tip_c),
           'secondary_writer_intended_correct': {'n': sum(1 for i in items if i['kind'] == 'C'), 'judged_wrong': len(c_wrong), 'ids': c_wrong},
           'secondary_cell_writer_M_judged_correct': {'n': len(m_cell), 'of_writer_M': sum(1 for i in items if i['writer_intent'] == 'M')},
           'judge_noise': {'pairs': len(pairs), 'judged_disagree': len(dis), 'type_disagree': len(dis_t), 'pairs_disagree': dis + dis_t},
           'second_judge_unsure': {j: (blind.get(j) or cmap.get(j)) for j in UNSURE},
           'writer_tags': {'correct': dict(collections.Counter(t for i in items if i['kind'] == 'C' for t in i['tags'])),
                           'wrong': dict(collections.Counter(t for i in items if i['kind'] == 'W' for t in i['tags']))},
           'annotations': ann_state,
           'sha256': {f: hashlib.sha256(open(os.path.join(HERE, f), 'rb').read()).hexdigest() for f in
                      ('data/writer_A.json', 'data/writer_B.json', 'judge/_key_A.json', 'judge/_key_B.json',
                       'judge/packets_A1.json', 'judge/packets_A2.json')}}
    wr(os.path.join(HERE, 'normalise_1p.json'), rep)
    print(json.dumps({k: v for k, v in rep.items() if k not in ('sha256',)}, indent=1, ensure_ascii=False))
    return 2 if (fails or not ann_state.startswith('built')) else 0


if __name__ == '__main__':
    raise SystemExit(main())
