#!/usr/bin/env python3
"""Phase 1P assembler — adapted from phase1n/assemble_1n.py.

    python3 phase1p/assemble_1p.py            # build data/*.json from the writer files
    python3 phase1p/assemble_1p.py --labels   # additionally join the judge verdicts

INPUT CONTRACT (declared before any data exists)
  data/writer_A.json  SIDs 1P001-1P060 (A1 then A2)
  data/writer_B.json  SIDs 1P061-1P120 (B1 then B2)
  1N writer schema + a per-answer `tags` list.  A writer file is a list of sentence objects:
      {"sid": "1P001", "level": "A1", "topic": "...", "slovak": "...",
       "annotation": {"v": [...], "lk": [...], "alt": {...},
                      "voice_sk": "active_agent|passive|impersonal", "agent_nom": true|false,
                      "tf_gold": "past|present|future", "tense_open": bool,
                      "perfective_present": bool},
       "answers": [{"aid": 1, "kind": "C"|"W", "intent": "C|TF|...", "form": null,
                    "tags": ["agentless"|"by-passive"|"determiner"|"aspect"|"timeframe"|
                             "number"|"plain", ...],
                    "answer": "..."}]}      4 kind C + 5 kind W per sentence.
  The reader is tolerant about the container key (`answers` / `items`) and the annotation key
  (`annotation` / `ann` / `hygienised`); everything else must be as above or it REFUSES.

OUTPUT   data/sentences.json, data/annotations.json, data/items.json  (loader_1p schema)
  numeric sid = 170000 + the number in the writer SID; item id  "<C|W>:<sid>:<aid>".
CHECKS   no overlap with the existing 450 sentences, no internal duplicate Slovak, 4+5 per
  sentence, tags known, half by the SPLIT_1P rule.  0 model calls.
"""
import argparse, collections, json, os, re, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
TOFF = os.path.dirname(HERE)
DATA, JUDGE = os.path.join(HERE, 'data'), os.path.join(HERE, 'judge')
TAGS = ('agentless', 'by-passive', 'determiner', 'aspect', 'timeframe', 'number', 'plain')
SID_RE = re.compile(r'^1P(\d{3})$')


def norm(s):
    return re.sub(r'\s+', ' ', (s or '').strip().lower()).strip(' .!?')


def half_of(sid):
    """SPLIT_1P.md: within each level, odd SID number -> P1, even -> P2."""
    return 'P1' if int(sid) % 2 == 1 else 'P2'


def existing_slovak():
    """The 450 sentences already used (phase1n/existing_350.json + the 100 of the 1N set)."""
    out = {}
    p350 = os.path.join(TOFF, 'phase1n', 'existing_350.json')
    if os.path.exists(p350):
        obj = json.load(open(p350, encoding='utf-8'))
        rows = obj if isinstance(obj, list) else (obj.get('sentences') or list(obj.values()))
        for s in rows:
            if isinstance(s, dict):
                for k in ('slovak', 'sk', 'text'):
                    if s.get(k):
                        out[norm(s[k])] = s.get('sid')
                        break
            elif isinstance(s, str):
                out[norm(s)] = None
    pn = os.path.join(TOFF, 'phase1n', 'data', 'sentences.json')
    if os.path.exists(pn):
        for s in json.load(open(pn, encoding='utf-8')):
            out[norm(s['slovak'])] = s['sid']
    return out


def read_writer(path, lo, hi):
    if not os.path.exists(path):
        raise SystemExit('REFUSED: %s does not exist (the writer has not delivered)' % path)
    rows = json.load(open(path, encoding='utf-8'))
    if not isinstance(rows, list) or not rows:
        raise SystemExit('REFUSED: %s is not a non-empty list' % path)
    out = []
    for s in rows:
        m = SID_RE.match(str(s.get('sid', '')))
        if not m:
            raise SystemExit('REFUSED: %s: bad sid %r (expected 1Pnnn)' % (path, s.get('sid')))
        n = int(m.group(1))
        if not (lo <= n <= hi):
            raise SystemExit('REFUSED: %s: sid %s outside %d..%d' % (path, s['sid'], lo, hi))
        ann = s.get('annotation') or s.get('ann') or s.get('hygienised')
        if not isinstance(ann, dict) or not [v for v in (ann.get('v') or []) if isinstance(v, str)]:
            raise SystemExit('REFUSED: %s: sid %s has no annotation "v"' % (path, s['sid']))
        answers = s.get('answers') or s.get('items')
        if not isinstance(answers, list):
            raise SystemExit('REFUSED: %s: sid %s has no answers list' % (path, s['sid']))
        nc = sum(1 for a in answers if a.get('kind') == 'C')
        nw = sum(1 for a in answers if a.get('kind') == 'W')
        if (nc, nw) != (4, 5):
            raise SystemExit('REFUSED: %s: sid %s has %d correct + %d wrong (4 + 5 required)'
                             % (path, s['sid'], nc, nw))
        for a in answers:
            tg = a.get('tags')
            if not isinstance(tg, list) or not tg or [t for t in tg if t not in TAGS]:
                raise SystemExit('REFUSED: %s: sid %s answer %r has bad tags %r'
                                 % (path, s['sid'], a.get('aid'), tg))
            if not a.get('answer'):
                raise SystemExit('REFUSED: %s: sid %s answer %r is empty' % (path, s['sid'], a.get('aid')))
        for k in ('level', 'topic', 'slovak'):
            if not s.get(k):
                raise SystemExit('REFUSED: %s: sid %s has no %r' % (path, s['sid'], k))
        out.append({'n': n, 'raw_sid': s['sid'], 'sid': 170000 + n, 'level': s['level'],
                    'topic': s['topic'], 'slovak': s['slovak'], 'ann': ann, 'answers': answers})
    return out


def build(labels=False):
    rows = read_writer(os.path.join(DATA, 'writer_A.json'), 1, 60) + \
        read_writer(os.path.join(DATA, 'writer_B.json'), 61, 120)
    rows.sort(key=lambda r: r['sid'])
    seen_sid, seen_sk, report = set(), {}, {}
    ex = existing_slovak()
    overlap, dup = [], []
    for r in rows:
        if r['sid'] in seen_sid:
            raise SystemExit('REFUSED: duplicate sid %s' % r['raw_sid'])
        seen_sid.add(r['sid'])
        k = norm(r['slovak'])
        if k in ex:
            overlap.append({'sid': r['raw_sid'], 'collides_with': ex[k]})
        if k in seen_sk:
            dup.append({'sid': r['raw_sid'], 'same_as': seen_sk[k]})
        seen_sk[k] = r['raw_sid']
    if overlap:
        raise SystemExit('REFUSED: %d sentences overlap the existing 450: %s'
                         % (len(overlap), json.dumps(overlap[:10])))
    if dup:
        raise SystemExit('REFUSED: %d internal duplicate sentences: %s' % (len(dup), json.dumps(dup[:10])))
    if len(rows) != 120:
        print('NOTE: %d sentences, 120 expected' % len(rows))
    sents, ann, items = [], {}, []
    for r in rows:
        sents.append({'sid': r['sid'], 'slovak': r['slovak'], 'level': r['level'],
                      'topic': r['topic'], 'tags': {'half': half_of(r['sid'])}})
        a = dict(r['ann'])
        core = {k: a[k] for k in ('v', 'lk', 'alt', 'm', 'lv', 't', 'id') if k in a}
        core.setdefault('id', r['sid'])
        ann[str(r['sid'])] = dict({k: v for k, v in a.items() if k not in core},
                                  hygienised=core, raw=core)
        for x in r['answers']:
            items.append({'id': '%s:%d:%s' % (x['kind'], r['sid'], x.get('aid')),
                          'sid': r['sid'], 'kind': x['kind'], 'intent': x.get('intent'),
                          'form': x.get('form'), 'tags': list(x['tags']),
                          'passive': ('agentless' if 'agentless' in x['tags'] else
                                      'by' if 'by-passive' in x['tags'] else None),
                          'answer': x['answer']})
    os.makedirs(DATA, exist_ok=True)
    for name, obj in (('sentences.json', sents), ('annotations.json', ann), ('items.json', items)):
        json.dump(obj, open(os.path.join(DATA, name), 'w', encoding='utf-8'), indent=1,
                  ensure_ascii=False)
    report = {'sentences': len(sents), 'items': len(items),
              'levels': dict(collections.Counter(s['level'] for s in sents)),
              'halves': dict(collections.Counter(s['tags']['half'] for s in sents)),
              'tags': dict(collections.Counter(t for i in items for t in i['tags'])),
              'kinds': dict(collections.Counter(i['kind'] for i in items)),
              'overlap_with_the_existing_450': 0, 'internal_duplicates': 0,
              'existing_sentences_checked_against': len(ex)}
    if labels:
        report['labels'] = join_labels(items)
    json.dump(report, open(os.path.join(HERE, 'assemble_1p.json'), 'w', encoding='utf-8'),
              indent=1, ensure_ascii=False)
    print(json.dumps(report, indent=1, sort_keys=True))
    return report


def join_labels(items):
    """Judge verdicts + judge noise from the hidden duplicate jids in judge/_key.json."""
    import glob
    bm = os.path.join(JUDGE, 'blind_map.json')
    if not os.path.exists(bm):
        return {'note': 'judge/blind_map.json absent — labels not joined'}
    blind = json.load(open(bm, encoding='utf-8'))
    key = {}
    kp = os.path.join(JUDGE, '_key.json')
    if os.path.exists(kp):
        key = json.load(open(kp, encoding='utf-8'))
    ids = {i['id'] for i in items}
    per = collections.defaultdict(list)
    n_rows = 0
    for p in sorted(glob.glob(os.path.join(JUDGE, 'verdicts_*.json')) +
                    glob.glob(os.path.join(JUDGE, 'out_part*.json'))):
        for r in json.load(open(p, encoding='utf-8')):
            n_rows += 1
            iid = blind.get(r['jid'])
            if iid is None and r['jid'] in key:
                k = key[r['jid']]
                iid = '%s:%s:%s' % (k.get('kind', 'C'), k.get('sid'), k.get('aid'))
            if iid in ids:
                per[iid].append((r.get('judged'), r.get('type') if r.get('judged') == 'wrong' else None))
    dupes = {i: v for i, v in per.items() if len(v) > 1}
    disagree = sum(1 for v in dupes.values() if len({x[0] for x in v}) > 1)
    return {'rows_read': n_rows, 'items_labelled': len(per), 'unlabelled': len(ids) - len(per),
            'duplicate_items': len(dupes), 'duplicate_disagreements': disagree,
            'judge_noise_pct': round(100.0 * disagree / len(dupes), 2) if dupes else None,
            'judged': dict(collections.Counter(v[0][0] for v in per.values())),
            'types': dict(collections.Counter(v[0][1] for v in per.values() if v[0][0] == 'wrong'))}


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--labels', action='store_true')
    build(ap.parse_args().labels)
