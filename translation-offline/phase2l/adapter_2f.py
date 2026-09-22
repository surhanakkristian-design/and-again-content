#!/usr/bin/env python3
"""Phase 2I stage 2b - the 2F production -> 1W annotation SHAPE adapter, copied VERBATIM (no edit) from
phase2f/p3/probe/p3_probe.py (sha256 7325f4f26fc016772b8326d4473e29d8c93f98dc9e105103f0f6f6734c55051e, last commit 3c63368):
  line 55 SID_LO/SID_HI; jdump 121-128; alt_dict 286-294; build_data 297-322.
This is exactly the code that wrote phase2f/p3/probe/data/{sentences,annotations}.json (2F ran production rows
through the 1U/1W stack with it). Only convert() at the bottom is new: it hands build_data the `sel` shape that
p3_probe.pick_sentences built ({"rows": [{sid, exercise_id, level, topic, slovak, ann}]}). Shape adapter only;
it changes no annotation value (lk passes through into hygienised/raw; the TRANSLATION-ONLY stack strips it
from the row BEFORE the adapter and from the result after it)."""
import json
import os


# ---- verbatim, p3_probe.py:55
SID_LO, SID_HI = 220001, 220060


# ---- verbatim, p3_probe.py:121-128
def jdump(o, p):
    d = os.path.dirname(p)
    if d and not os.path.isdir(d):
        os.makedirs(d, exist_ok=True)
    tmp = p + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as fh:
        json.dump(o, fh, indent=1, ensure_ascii=False, default=str)
    os.replace(tmp, p)


# ---- verbatim, p3_probe.py:286-294
def alt_dict(ann):
    out = {}
    for a in (ann.get('alt') or []):
        tok = a.get('tok')
        cand = [c for c in (a.get('groups_or_candidates') or [])
                if isinstance(c, str) and c.strip() and c.strip().lower() != str(tok).lower()]
        if tok and cand:
            out[tok] = cand
    return out


# ---- verbatim, p3_probe.py:297-322
def build_data(sel, data_dir):
    """sentences.json / annotations.json in the 1U shapes, from production rows."""
    sents, anns = [], {}
    for r in sel['rows']:
        d, sid = r['ann'], r['sid']
        sents.append({
            'sid': sid, 'pid': 'P31%03d' % (sid - SID_LO + 1), 'slovak': r['slovak'],
            'level': r['level'], 'topic': r['topic'],
            'tags': {'half': 'P1' if sid % 2 else 'P2', 'level': r['level'], 'kind': 'PROD',
                     'emb': bool(d.get('embedded_agents')), 'tf_gold': d.get('tf'),
                     'writer_tags': {'agent_clause': 'main', 'agent': d.get('subject'),
                                     'other_subject': None, 'subordinator': None,
                                     'passivizable': None,
                                     'impersonal_or_passive': d.get('voice') != 'active_agent',
                                     'kind': 'PROD', 'lid': 'p%03d' % (sid - SID_LO + 1)}}})
        hy = {'v': [x for x in (d.get('v') or []) if isinstance(x, str) and x.strip()],
              'lk': [x for x in (d.get('lk') or []) if isinstance(x, str) and x.strip()],
              'alt': alt_dict(d), 'id': sid, 'lv': r['level']}
        anns[str(sid)] = {'voice_sk': d.get('voice'), 'agent_nom': d.get('agent_nom'),
                          'tf_gold': d.get('tf'), 'tense_open': d.get('tense_open'),
                          'perfective_present': d.get('perfective_present'),
                          'hygienised': hy, 'raw': dict(hy)}
    os.makedirs(data_dir, exist_ok=True)
    jdump(sents, os.path.join(data_dir, 'sentences.json'))
    jdump(anns, os.path.join(data_dir, 'annotations.json'))
    return sents, anns


# ---- new (stage 2b): the call site
def convert(rows, data_dir):
    """rows = [{sid, exercise_id, level, topic, slovak, ann=production row}] -> (sentences, annotations), 1W shape."""
    return build_data({'rows': rows}, data_dir)
