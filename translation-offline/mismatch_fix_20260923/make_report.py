import json, collections, fixlib
b = fixlib.load('before'); a = fixlib.load('after')
ch = json.load(open('work/changed.json'))
P = {**json.load(open('work/proposals.json')), **json.load(open('work/proposals_r2.json'))}
r2 = set(json.load(open('work/proposals_r2.json')))
conf = json.load(open(fixlib.TO + '/mismatch_scan_20260923/confirmed.json'))
esc = lambda s: (s or '').replace('|', '\\|')
rows = []
for e in sorted(ch, key=int):
    for l in ch[e]:
        o, n = b[int(e)][l], a[int(e)][l]
        if l == 'en':
            reason = 'Part 3: the English said something different from all 8 natives; rewritten to the natives (gap, distractors, chunks updated)'
            part = 'P3'
        else:
            key = ('P1' if f'P1-{e}-{l}' in P else 'P2') + f'-{e}-{l}'
            p = P[key]; part = key[:2] + (' r2' if key in r2 else '')
            reason = f"{p['mode']}: {p['note']}"
        gap = '' if (o['correct_answer'] or '') == (n['correct_answer'] or '') else f" gap {o['correct_answer']!r}→{n['correct_answer']!r}"
        dis = '' if (o['distractor_1'], o['distractor_2']) == (n['distractor_1'], n['distractor_2']) else f" distractors {o['distractor_1']} / {o['distractor_2']} → {n['distractor_1']} / {n['distractor_2']}"
        rows.append(f"| {e} | {l} | {part} | {esc(o['full_sentence'])} | {esc(n['full_sentence'])} | {esc(reason + gap + dis)} |")
open('work/change_table.md', 'w').write('| exercise_id | lang | part | old full_sentence | new full_sentence | reason |\n|---|---|---|---|---|---|\n' + '\n'.join(rows) + '\n')
print(len(rows))
