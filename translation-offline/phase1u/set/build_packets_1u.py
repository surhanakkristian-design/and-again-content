#!/usr/bin/env python3
"""Phase 1U blind judge packets — 0 model calls.

    python3 phase1u/set/build_packets_1u.py [--allow-partial]

900 real items + 80 hidden duplicate controls (20 per level, the same item under a second
opaque id), shuffled ACROSS levels with seed 20260920 and split into N <= 5 equal parts
(4 if every part stays under ~19k estimated tokens, otherwise 5):

    set/judge/packet_partK.jsonl   one JSON object per line: {id, slovak, answer}
    set/judge/JUDGE_TASK_1U.md     the judge's only entry point (absolute paths)
    set/packet_key_1u.json         {qid: {item, duplicate_of, sid, level, part, position}}

The key does NOT live under judge/ and is never named in the judge's task file.
"""
import argparse, collections, json, os, random, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))              # phase1u/set
PHASE = os.path.dirname(HERE)
TOFF = os.path.dirname(PHASE)
sys.path.insert(0, os.path.join(TOFF, 'phase1s'))
try:
    from safe_json import safe_dump                            # noqa: E402
except Exception:                                              # pragma: no cover
    def safe_dump(obj, path):
        tmp = path + '.tmp'
        with open(tmp, 'w', encoding='utf-8') as fh:
            json.dump(obj, fh, ensure_ascii=False, indent=1)
        os.replace(tmp, path)

SEED = 20260920
N_ITEMS, PER_LEVEL_DUPS, MAX_PARTS = 900, 20, 5
TOKEN_BUDGET = 19000
CHARS_PER_TOKEN = 3.0          # conservative for Slovak diacritics in JSON


def est_tokens(lines):
    return int(sum(len(x) for x in lines) / CHARS_PER_TOKEN) + len(lines)


def build(data_dir=None, judge_dir=None, allow_partial=False):
    data_dir = data_dir or os.path.join(HERE, 'data')
    judge_dir = judge_dir or os.path.join(HERE, 'judge')
    items = json.load(open(os.path.join(data_dir, 'items.json'), encoding='utf-8'))
    sents = {int(s['sid']): s for s in
             json.load(open(os.path.join(data_dir, 'sentences.json'), encoding='utf-8'))}
    if len(items) != N_ITEMS and not allow_partial:
        print('REFUSED: %d items, %d expected (use --allow-partial to override)'
              % (len(items), N_ITEMS))
        return 2
    by_level = collections.defaultdict(list)
    for it in items:
        by_level[sents[int(it['sid'])]['level']].append(it['id'])
    rng = random.Random(SEED)
    dups = []
    for lvl in sorted(by_level):
        pool = sorted(by_level[lvl])
        dups += rng.sample(pool, min(PER_LEVEL_DUPS, len(pool)))
    entries = [(it['id'], False) for it in items] + [(iid, True) for iid in dups]
    rng.shuffle(entries)

    ans = {it['id']: it['answer'] for it in items}
    rows, first = [], {}
    for n, (iid, is_dup) in enumerate(entries, 1):
        if not is_dup:
            first[iid] = 'Q%04d' % n
    for n, (iid, is_dup) in enumerate(entries, 1):
        qid = 'Q%04d' % n
        sid = int(iid.split(':')[1])
        rows.append({'qid': qid, 'iid': iid, 'sid': sid, 'level': sents[sid]['level'],
                     'dup_of': first[iid] if is_dup else None,
                     'line': json.dumps({'id': qid, 'slovak': sents[sid]['slovak'],
                                         'answer': ans[iid]}, ensure_ascii=False)})

    n_parts = 4
    while n_parts <= MAX_PARTS:
        size = -(-len(rows) // n_parts)
        worst = max(est_tokens([r['line'] for r in rows[i:i + size]])
                    for i in range(0, len(rows), size))
        if worst <= TOKEN_BUDGET or n_parts == MAX_PARTS:
            break
        n_parts += 1

    os.makedirs(judge_dir, exist_ok=True)
    base, rest = divmod(len(rows), n_parts)
    key, sizes, i = {}, [], 0
    for p in range(n_parts):
        n = base + (1 if p < rest else 0)
        chunk = rows[i:i + n]
        i += n
        path = os.path.join(judge_dir, 'packet_part%d.jsonl' % (p + 1))
        tmp = path + '.tmp'
        with open(tmp, 'w', encoding='utf-8') as fh:
            fh.write('\n'.join(r['line'] for r in chunk) + '\n')
        os.replace(tmp, path)
        for pos, r in enumerate(chunk, 1):
            key[r['qid']] = {'item': r['iid'], 'duplicate_of': r['dup_of'], 'sid': r['sid'],
                             'level': r['level'], 'part': p + 1, 'position': pos}
        sizes.append({'part': p + 1, 'items': len(chunk),
                      'bytes': os.path.getsize(path),
                      'est_tokens': est_tokens([r['line'] for r in chunk]),
                      'path': path})
    safe_dump(key, os.path.join(HERE, 'packet_key_1u.json'))

    brief = os.path.join(judge_dir, 'JUDGE_BRIEF_1U.md')
    T = ['# JUDGE_TASK_1U — your whole task (Phase 1U)', '',
         'You are the blind judge. Read ONLY the files named below; open nothing else and do '
         'not search the repository.', '',
         '1. Read the brief: `%s`' % brief, '',
         '2. Then, for each part K = 1..%d in order: read the packet part, judge every item in '
         'it, and IMMEDIATELY write its verdict file before reading the next part.' % n_parts,
         '']
    for s in sizes:
        T.append('   - part %d — packet `%s` (%d items) → verdicts `%s`'
                 % (s['part'], s['path'], s['items'],
                    os.path.join(judge_dir, 'verdicts_part%d.json' % s['part'])))
    T += ['',
          '3. Each packet part is JSON Lines: one object per line with `id`, `slovak` '
          '(the Slovak sentence) and `answer` (the learner\'s English). Nothing else exists '
          'about an item — no reference translation, no intent, no tags.', '',
          '4. Each verdict file is a JSON LIST, one object per packet item, in packet order, '
          'in the format of the brief:', '',
          '```json',
          '{"id": "Q0001", "label": "correct"|"wrong", "type": null|"T"|"W"|"M"|"S",',
          ' "borderline": true|false, "confidence": 1|2|3|4|5,',
          ' "dropped": "<Slovak = English of what is missing, or empty>",',
          ' "passive": null|"by"|"agentless", "agent_drop": null|"main"|"fronted"|"other"'
          '|"both", "note": "<= 12 words, optional"}',
          '```', '',
          '   MANDATORY on EVERY item: `id`, `label`, `borderline`, `confidence` (integer '
          '1-5), `dropped`. `type` is mandatory whenever `label` is `"wrong"` and must be '
          '`null` when `label` is `"correct"`. An item without `confidence` cannot be scored '
          'and the join will refuse the whole run.', '',
          '5. Judge every item; never skip one; never leave a file half-written. Some items '
          'look alike on purpose — judge each on its own, never try to be consistent with a '
          'remembered earlier item or to balance your verdicts.', '',
          '6. BUDGET: at most 12 tool calls in total. One Read per packet part, one Write per '
          'verdict file, one Read for the brief — that is %d; the rest is your margin. Do not '
          'list directories, do not re-read what you have read.' % (2 * n_parts + 1), '',
          'Total items: %d.' % len(rows)]
    open(os.path.join(judge_dir, 'JUDGE_TASK_1U.md'), 'w',
         encoding='utf-8').write('\n'.join(T) + '\n')

    clean = all(set(json.loads(r['line'])) == {'id', 'slovak', 'answer'} for r in rows)
    rep = {'items': len(items), 'duplicate_controls': len(dups),
           'duplicates_per_level': dict(collections.Counter(
               sents[int(d.split(':')[1])]['level'] for d in dups)),
           'total_qids': len(rows), 'parts': n_parts, 'part_sizes': sizes, 'seed': SEED,
           'packet_fields_clean': clean,
           'levels_per_part': [dict(collections.Counter(
               r['level'] for r in rows if key[r['qid']]['part'] == p + 1))
               for p in range(n_parts)],
           'key_path': os.path.join(HERE, 'packet_key_1u.json'),
           'judge_task': os.path.join(judge_dir, 'JUDGE_TASK_1U.md')}
    safe_dump(rep, os.path.join(HERE, 'build_packets_1u.json'))
    print(json.dumps(rep, indent=1, sort_keys=True, ensure_ascii=False))
    return 0 if clean else 2


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--data-dir')
    ap.add_argument('--judge-dir')
    ap.add_argument('--allow-partial', action='store_true')
    a = ap.parse_args()
    raise SystemExit(build(a.data_dir, a.judge_dir, a.allow_partial))
