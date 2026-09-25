"""Collects the Stage C numbers for TINDER_FINISH_REPORT.md: rows per language, rejections by reason, 10 examples per language, tokens."""
import json, glob, os, collections, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build
H = os.path.dirname(os.path.abspath(__file__))
EN = {r['media_id']: r for r in build.en_rows()}
M = build.meta()
out = []
langs = [l for l in ['sk', 'cz', 'de', 'ua', 'es', 'fr', 'tr', 'hu'] if os.path.isdir(os.path.join(H, 'slices', l))]
tok = collections.defaultdict(int)
for line in open(os.path.join(H, 'tokens.tsv')):
    p = line.rstrip('\n').split('\t')
    if len(p) == 4 and p[3].isdigit():
        tok[(p[0], p[2])] += int(p[3])
summary = {}
for l in langs:
    D = os.path.join(H, 'slices', l)
    final = {}
    for p in sorted(glob.glob(os.path.join(D, 't*_final.jsonl'))) + [os.path.join(D, 'r1_final.jsonl')]:
        if os.path.exists(p):
            for x in open(p):
                r = json.loads(x); final[r['id']] = r
    r1 = collections.Counter(); r1_rows = 0; hard = collections.Counter()
    for p in glob.glob(os.path.join(D, 't*_left.json')):
        for x in json.load(open(p)):
            r1_rows += 1
            (hard if x['stage'] == 'check' else r1).update(x['r'] or ['?'])
    r2 = collections.Counter(); left2 = []
    p = os.path.join(D, 'r1_left.json')
    if os.path.exists(p):
        for x in json.load(open(p)):
            r2.update(x['r']); left2.append(x)
    retried = os.path.exists(os.path.join(D, 'r1_final.jsonl'))
    missing = sorted(set(EN) - set(final))
    summary[l] = dict(rows=len(final), r1_rows=r1_rows, r1=dict(r1.most_common()), hard=dict(hard.most_common()), r2=dict(r2.most_common()), retried=retried, missing=missing,
                      left2=[{'id': x['id'], 'r': x['r'], 'note': x.get('note', '')} for x in left2],
                      tx=tok[(l, 'tx')], txv=tok[(l, 'txv')])
    random.seed(131)
    ids = random.sample(sorted(final), min(10, len(final)))
    summary[l]['examples'] = [{'id': i, 'word': M[i]['words'].split(' (')[0], 'en': EN[i], 'tx': final[i]} for i in sorted(ids)]
summary['_tokens_A'] = tok[('A', 'all')]
summary['_tokens_total'] = sum(tok.values())
json.dump(summary, open(os.path.join(H, 'report_parts.json'), 'w'), ensure_ascii=False, indent=1)
for l in langs:
    s = summary[l]
    print(l, s['rows'], 'r1 rows', s['r1_rows'], 'missing', len(s['missing']), 'tok', s['tx'] + s['txv'])
print('total tokens', summary['_tokens_total'])
