#!/usr/bin/env python3
"""Phase 2I Part 0 (0 model calls): clean copies of both upload files under phase2i/upload/.
v=[en] where v is empty; exercise_id written as int; lk kept in structure_json (unused). Originals untouched."""
import json, os, hashlib, collections, openpyxl
TO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(TO, 'phase2i', 'upload')
SRC = {'sk': ('phase2d/out/upload_sk_final.xlsx', 'phase2d/out/annotations_sk_final.jsonl'),
       'cz': ('phase2h/out/upload_cz_final.xlsx', 'phase2h/out/annotations_cz_final.jsonl')}
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
res = {}
for lang, (xp, jp) in SRC.items():
    xp, jp = os.path.join(TO, xp), os.path.join(TO, jp)
    before = (sha(xp), sha(jp))
    wb = openpyxl.load_workbook(xp); ws = wb.worksheets[0]; title = ws.title
    rows = list(ws.iter_rows(values_only=True)); H = list(rows[0]); data = rows[1:]
    ann = [json.loads(l) for l in open(jp, encoding='utf-8') if l.strip()]
    assert len(data) == 4064 and len(ann) == 4064, (lang, len(data), len(ann))
    ix = {h: i for i, h in enumerate(H)}
    by_eid = {int(a['exercise_id']): a for a in ann}
    assert len(by_eid) == 4064, 'exercise_id not unique in jsonl'
    empty_n, empty_eid, mism, sj_diff, sj_style = [], [], [], 0, collections.Counter()
    eid_types = collections.Counter(type(r[ix['exercise_id']]).__name__ for r in data)
    newrows = []
    for r in data:
        r = list(r); eid = int(str(r[ix['exercise_id']]).strip()); r[ix['exercise_id']] = eid
        s = r[ix['structure_json']]; sj = json.loads(s)
        sj_style['compact' if s == json.dumps(sj, ensure_ascii=False, separators=(',', ':')) else
                 'default' if s == json.dumps(sj, ensure_ascii=False) else 'other'] += 1
        a = by_eid[eid]
        if sj != a: sj_diff += 1
        assert sj.get('en') == r[ix['en']], (lang, eid, 'en mismatch xlsx vs structure_json')
        v = sj.get('v')
        if not v:
            sj['v'] = [sj['en']]; empty_n.append(sj['n']); empty_eid.append(eid)
            s = json.dumps(sj, ensure_ascii=False)
            a['v'] = [a['en']]
        elif v[0] != sj['en']:
            mism.append({'n': sj['n'], 'exercise_id': eid, 'en': sj['en'], 'v0': v[0]})
        assert len(s) <= 32767
        r[ix['structure_json']] = s; newrows.append(r)
    # write xlsx + jsonl
    nb = openpyxl.Workbook(); nw = nb.active; nw.title = title; nw.append(H)
    for r in newrows: nw.append(r)
    ox = os.path.join(OUT, 'upload_%s_final.xlsx' % lang); nb.save(ox)
    oj = os.path.join(OUT, 'annotations_%s_fixed.jsonl' % lang)
    with open(oj, 'w', encoding='utf-8') as fh:
        for a in ann: fh.write(json.dumps(a, ensure_ascii=False) + '\n')
    # round-trip
    rb = list(openpyxl.load_workbook(ox, read_only=True).worksheets[0].iter_rows(values_only=True))
    assert list(rb[0]) == H and len(rb) - 1 == 4064
    rj = [json.loads(l) for l in open(oj, encoding='utf-8')]; assert len(rj) == 4064
    rjm = {int(a['exercise_id']): a for a in rj}
    v0bad = 0
    for x in rb[1:]:
        assert isinstance(x[ix['exercise_id']], int)
        sj = json.loads(x[ix['structure_json']])
        assert sj == rjm[x[ix['exercise_id']]] or sj_diff, 'xlsx/jsonl disagree'
        assert sj['v'], 'empty v survived'
        assert 'lk' in sj
        if sj['v'][0] != x[ix['en']]: v0bad += 1
    after = (sha(xp), sha(jp)); assert before == after, 'ORIGINAL CHANGED'
    res[lang] = {'src_xlsx': SRC[lang][0], 'src_jsonl': SRC[lang][1], 'sheet': title, 'columns': H,
                 'rows_xlsx': len(rb) - 1, 'rows_jsonl': len(rj), 'exercise_id_types_before': dict(eid_types),
                 'v_empty_fixed': len(empty_n), 'v_empty_n': sorted(empty_n),
                 'v0_ne_en_nonempty_defects': len(mism), 'v0_ne_en_after': v0bad, 'defect_rows': mism,
                 'structure_json_vs_jsonl_diff_rows': sj_diff, 'structure_json_style': dict(sj_style),
                 'out_xlsx': os.path.relpath(ox, TO), 'out_jsonl': os.path.relpath(oj, TO),
                 'out_sha': {os.path.basename(ox): sha(ox), os.path.basename(oj): sha(oj)},
                 'originals_sha_unchanged': True}
json.dump(res, open(os.path.join(OUT, 'part0_result.json'), 'w'), ensure_ascii=False, indent=1)
for k, v in res.items():
    print(k, {x: v[x] for x in ('rows_xlsx', 'rows_jsonl', 'exercise_id_types_before', 'v_empty_fixed',
                                'v0_ne_en_nonempty_defects', 'v0_ne_en_after', 'structure_json_vs_jsonl_diff_rows',
                                'structure_json_style')})
    print(' empty n:', v['v_empty_n'])
    for d in v['defect_rows'][:8]: print(' defect', d)
