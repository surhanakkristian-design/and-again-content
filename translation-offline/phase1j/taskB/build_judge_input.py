#!/usr/bin/env python3
"""Task B step 3 — build the BLIND judge's input. Prints counts only; never prints an answer,
a label or a type. Run:

    PYTHONDONTWRITEBYTECODE=1 PHASE1J_LABEL_PREP=1 python3 taskB/build_judge_input.py

Items to re-judge = every item (judged-correct and judged-wrong, both sides) of every REWRITTEN
sentence, plus 60 control items drawn with seed 1 from UNTOUCHED DEV sentences (unchanged Slovak;
they measure judge noise). Output judge_input.jsonl (+ parts), shuffled with seed 1, lines carry
only {k, sk, answer, level}. judge_keymap.json holds the mapping and is forbidden to the judge.
"""
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
P1J = os.path.dirname(HERE)
sys.path.insert(0, P1J)
from loader_1j import load_items  # noqa: E402

PURPOSE = 'Task B judge-input build (script only, counts printed)'
N_CONTROL = 60
MAX_PART = 300


def main():
    rw = {}
    untouched_dev = set()
    for line in open(os.path.join(HERE, 'rewrites.jsonl'), encoding='utf-8'):
        r = json.loads(line)
        if r['status'] == 'rewritten':
            rw[r['sid']] = r['new_sk']
        elif r['side'] == 'dev':
            untouched_dev.add(r['sid'])

    pool, controls = [], []
    for side in ('dev', 'holdout'):
        for it in load_items(side, purpose=PURPOSE):
            if it['sid'] in rw:
                pool.append((it, rw[it['sid']], False))
            elif side == 'dev' and it['sid'] in untouched_dev:
                controls.append((it, it['sk'], True))

    rnd = random.Random(1)
    picked = rnd.sample(controls, N_CONTROL)
    rows = pool + picked
    rnd.shuffle(rows)

    lines, keymap = [], {}
    for i, (it, sk, ctrl) in enumerate(rows, 1):
        k = 'j%04d' % i
        lines.append({'k': k, 'sk': sk, 'answer': it['answer'], 'level': it['level']})
        keymap[k] = {'item_id': it['item_id'], 'sid': it['sid'], 'side': it['side'],
                     'old_label': it['judged'], 'old_type': it['wrong_type'], 'control': ctrl}

    def dump(path, rs):
        with open(path, 'w', encoding='utf-8') as fh:
            for r in rs:
                fh.write(json.dumps(r, ensure_ascii=False) + '\n')

    dump(os.path.join(HERE, 'judge_input.jsonl'), lines)
    json.dump(keymap, open(os.path.join(HERE, 'judge_keymap.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)

    parts = []
    if len(lines) > 400:
        n = -(-len(lines) // -(-len(lines) // MAX_PART))  # balanced parts, each <= MAX_PART
        for j in range(0, len(lines), n):
            p = 'judge_input_part%d.jsonl' % (j // n + 1)
            dump(os.path.join(HERE, p), lines[j:j + n])
            parts.append((p, len(lines[j:j + n])))

    sides = {s: sum(1 for it, _, c in rows if not c and it['side'] == s) for s in ('dev', 'holdout')}
    sids = {s: len({it['sid'] for it, _, c in rows if not c and it['side'] == s})
            for s in ('dev', 'holdout')}
    print('rewritten sentences', len(rw), '| items from rewritten sentences: dev %d (%d sids), '
          'holdout %d (%d sids)' % (sides['dev'], sids['dev'], sides['holdout'], sids['holdout']))
    print('controls (untouched DEV sentences)', len(picked), 'from a pool of', len(controls),
          'items /', len(untouched_dev), 'sids')
    print('judge_input.jsonl lines', len(lines))
    print('parts', parts if parts else 'none')


if __name__ == '__main__':
    main()
