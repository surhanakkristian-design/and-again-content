#!/usr/bin/env python3
"""Phase 2L B2 input (0 calls): every item the SOURCE-ONLY stack accepted under either TIP variant (L3 SAME or L3 TIP),
both closed Slovak sets; fields jid (set|jid), src (Slovak), answer, level, l3 ONLY - no reference field."""
import collections, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P2L = os.path.dirname(HERE); sys.path.insert(0, P2L)
import score_2l as SC, content_check as CC, run_2i_base as B
data = SC.load(); out = []
for s in ('2I', '2J'):
    for r in data[s]:
        if CC.l3_ok(r['r'], True):
            out.append({'jid': r['key'], 'src': r['src'], 'answer': r['answer'], 'level': r['level'], 'l3': r['r']['l3_reply']})
keys = {B.req_key(CC.request('sk', x['src'], x['answer'])) for x in out}
with open(os.path.join(HERE, 'items_b2.jsonl'), 'w', encoding='utf-8') as fh:
    for x in out:
        fh.write(json.dumps(x, ensure_ascii=False, sort_keys=True) + '\n')
meta = {'items': len(out), 'unique_requests': len(keys), 'by_set_l3': {str(k): v for k, v in collections.Counter((x['jid'][:2], x['l3']) for x in out).items()}}
json.dump(meta, open(os.path.join(HERE, 'items_b2_meta.json'), 'w'), indent=1)
print('B2ITEMS', json.dumps(meta))
