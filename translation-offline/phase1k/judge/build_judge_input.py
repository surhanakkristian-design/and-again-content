#!/usr/bin/env python3
"""Phase 1k — build the BLIND judge's input. Prints COUNTS ONLY, never an answer, id or intent.

    PYTHONDONTWRITEBYTECODE=1 python3 phase1k/judge/build_judge_input.py

Sources
  (a) the 490 Phase 1j DEV items, arm-B Slovak
  (b) the fresh answers of `phase1k/fresh/writer_output.jsonl`
      -> `phase1k/fresh/items_fresh.jsonl` ({id, sid, text, intent})
  (c) 60 CONTROL duplicates: 60 fresh items drawn with a fixed seed, a SECOND opaque id,
      forced into a different chunk than their original (they measure judge noise)
  (d) the 490 Phase 1j HOLDOUT items, arm-B Slovak (labelled replay)

Output
  judge/in_1.jsonl .. in_4.jsonl  = (a)+(b)+(c) shuffled with seed "phase1k-judge", equal sizes
  judge/in_5.jsonl                = (d) shuffled
  every line ONLY {"j": "<6-char opaque id>", "sk": "<Slovak>", "en": "<answer>"}
  judge/key.jsonl                 = j -> {id, sid, source: dev|fresh|control|holdout1j, dup_of}
                                    (FORBIDDEN to the judge; gated behind PHASE1K_OPEN_FRESH=1)

`--selftest` fabricates a synthetic writer_output in a temp dir and runs the whole build there.
"""
import argparse
import hashlib
import json
import os
import random
import sys
import zlib

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
K = os.path.dirname(HERE)
sys.path.insert(0, K)
import loader_1k as L  # noqa: E402

PURPOSE = 'judge-input build, counts only'
SEED = 'phase1k-judge'
CONTROL_SEED = 'phase1k-control'
N_CONTROL = 60
N_CHUNKS = 4
INTENTS = ('C', 'T', 'W', 'M', 'S', 'V', 'TF')
MIN_C_PER_SENT = 3
MIN_WRONG_PER_SENT = 4
MIN_V = 30
MIN_TF = 30


def die(msg):
    raise SystemExit('WRITER_OUTPUT ERROR: ' + msg)


def norm(t):
    return ' '.join(str(t).split()).casefold()


def crc(t):
    return zlib.crc32(t.encode('utf-8')) & 0xffffffff


def opaque(seed_str, taken):
    for k in range(1000):
        j = hashlib.sha256(('phase1k|%s|%d' % (seed_str, k)).encode('utf-8')).hexdigest()[:6]
        if j not in taken:
            taken.add(j)
            return j
    die('could not mint a unique opaque id')


def build_fresh_items(fresh_dir, out_dir):
    """writer_output.jsonl -> validated, de-duplicated items_fresh.jsonl. Returns the item list."""
    sents = L.load_fresh_sentences(purpose=PURPOSE,
                                   path=os.path.join(fresh_dir, 'sentences_fresh.jsonl'))
    sk_of = {int(s['sid']): s['sk'] for s in sents}
    wo_path = os.path.join(fresh_dir, 'writer_output.jsonl')
    if not os.path.exists(wo_path):
        die('%s does not exist — the answer writer must produce it first.' % wo_path)
    rows = L.load_fresh_writer_output(purpose=PURPOSE, path=wo_path)

    seen_wid, items = set(), []
    for ln, r in enumerate(rows, 1):
        if not isinstance(r, dict) or 'wid' not in r or 'answers' not in r:
            die('line %d: expected {"wid":…, "answers":[…]}, got keys %s'
                % (ln, sorted(r) if isinstance(r, dict) else type(r).__name__))
        try:
            wid = int(r['wid'])
        except Exception:
            die('line %d: wid %r is not an int' % (ln, r['wid']))
        if wid not in sk_of:
            die('line %d: wid %d is not one of the %d fresh sids' % (ln, wid, len(sk_of)))
        if wid in seen_wid:
            die('line %d: wid %d appears twice' % (ln, wid))
        seen_wid.add(wid)
        if not isinstance(r['answers'], list) or not r['answers']:
            die('line %d (wid %d): "answers" must be a non-empty list' % (ln, wid))
        local, n_c, n_wrong = set(), 0, 0
        for a in r['answers']:
            if not isinstance(a, dict) or 'text' not in a or 'intent' not in a:
                die('line %d (wid %d): every answer needs {"text":…, "intent":…}' % (ln, wid))
            text = str(a['text']).strip()
            intent = str(a['intent']).strip()
            if not text:
                die('line %d (wid %d): empty answer text' % (ln, wid))
            if intent not in INTENTS:
                die('line %d (wid %d): intent %r not in %s' % (ln, wid, intent, list(INTENTS)))
            key = norm(text)
            if key in local:
                continue  # exact duplicate inside one sentence — dropped
            local.add(key)
            if intent == 'C':
                n_c += 1
            else:
                n_wrong += 1
            kind = 'C' if intent == 'C' else 'W'
            items.append({'id': '%s:%d:%d' % (kind, wid, crc(text)), 'sid': wid,
                          'text': text, 'intent': intent})
        if n_c < MIN_C_PER_SENT:
            die('wid %d: only %d correct (intent C) answers after de-duplication, need >= %d'
                % (wid, n_c, MIN_C_PER_SENT))
        if n_wrong < MIN_WRONG_PER_SENT:
            die('wid %d: only %d wrong answers after de-duplication, need >= %d'
                % (wid, n_wrong, MIN_WRONG_PER_SENT))
    missing = sorted(set(sk_of) - seen_wid)
    if missing:
        die('%d fresh sentences have no answers (first missing wid %d)'
            % (len(missing), missing[0]))
    n_v = sum(1 for i in items if i['intent'] == 'V')
    n_tf = sum(1 for i in items if i['intent'] == 'TF')
    if n_v < MIN_V:
        die('only %d V (active->passive recast) answers overall, need >= %d' % (n_v, MIN_V))
    if n_tf < MIN_TF:
        die('only %d TF (time-frame shift) answers overall, need >= %d' % (n_tf, MIN_TF))
    ids = [i['id'] for i in items]
    if len(set(ids)) != len(ids):
        die('duplicate item ids after crc32 — two different texts collided, report this')

    with open(os.path.join(out_dir, 'items_fresh.jsonl'), 'w', encoding='utf-8') as fh:
        for i in items:
            fh.write(json.dumps(i, ensure_ascii=False) + '\n')
    return items, sk_of


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--selftest', action='store_true')
    ap.add_argument('--fresh-dir', default=os.path.join(K, 'fresh'))
    ap.add_argument('--out-dir', default=HERE)
    ap.add_argument('--items-out-dir', default=None)
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    os.environ['PHASE1K_OPEN_FRESH'] = '1'  # needed for the build itself; purpose is logged
    run(a.fresh_dir, a.out_dir, a.items_out_dir or a.fresh_dir)
    return 0


def run(fresh_dir, out_dir, items_dir):
    os.makedirs(out_dir, exist_ok=True)
    fresh_items, sk_of = build_fresh_items(fresh_dir, items_dir)

    dev = L.load_dev_items(purpose=PURPOSE)
    hold = L.load_holdout1j_items(purpose=PURPOSE)

    taken = set()
    rows, key = [], []

    def add(src, item_id, sk, en, dup_of=None, sid=None):
        j = opaque('%s|%s|%s' % (src, item_id, dup_of or ''), taken)
        rows.append({'j': j, 'sk': sk, 'en': en, '_src': src, '_dup': dup_of})
        key.append({'j': j, 'id': item_id, 'sid': sid, 'source': src, 'dup_of': dup_of})
        return j

    for it in dev:
        add('dev', it['item_id'], it['sk'], it['answer'], sid=it['sid'])
    jof = {}
    for it in fresh_items:
        jof[it['id']] = add('fresh', it['id'], sk_of[it['sid']], it['text'], sid=it['sid'])

    rndc = random.Random(CONTROL_SEED)
    picks = rndc.sample(sorted(fresh_items, key=lambda i: i['id']),
                        min(N_CONTROL, len(fresh_items)))
    ctrl_js = []
    for it in picks:
        ctrl_js.append(add('control', it['id'], sk_of[it['sid']], it['text'],
                           dup_of=jof[it['id']], sid=it['sid']))

    rnd = random.Random(SEED)
    rnd.shuffle(rows)
    n = len(rows)
    sizes = [n // N_CHUNKS + (1 if i < n % N_CHUNKS else 0) for i in range(N_CHUNKS)]
    chunks, pos = [], 0
    for s in sizes:
        chunks.append(rows[pos:pos + s])
        pos += s
    where = {r['j']: ci for ci, ch in enumerate(chunks) for r in ch}

    # force every control duplicate into a different chunk than its original
    moved = 0
    for j in ctrl_js:
        ci = where[j]
        orig = next(r['_dup'] for ch in chunks for r in ch if r['j'] == j)
        if where[orig] != ci:
            continue
        target = next(t for t in range(N_CHUNKS) if t != ci)
        swap = None
        for r in chunks[target]:
            if r['_src'] == 'dev':
                swap = r
                break
        if swap is None:
            raise SystemExit('BUILD ERROR: no dev item available to swap a control with')
        cr = next(r for r in chunks[ci] if r['j'] == j)
        chunks[ci].remove(cr)
        chunks[target].remove(swap)
        chunks[ci].append(swap)
        chunks[target].append(cr)
        where[j], where[swap['j']] = target, ci
        moved += 1
    for j in ctrl_js:
        orig = next(r['_dup'] for ch in chunks for r in ch if r['j'] == j)
        assert where[j] != where[orig], 'control landed in its original chunk'

    hrows = []
    for it in hold:
        j = opaque('holdout1j|%s|' % it['item_id'], taken)
        hrows.append({'j': j, 'sk': it['sk'], 'en': it['answer']})
        key.append({'j': j, 'id': it['item_id'], 'sid': it['sid'],
                    'source': 'holdout1j', 'dup_of': None})
    random.Random(SEED + '|holdout').shuffle(hrows)

    def dump(path, rs):
        with open(path, 'w', encoding='utf-8') as fh:
            for r in rs:
                fh.write(json.dumps({'j': r['j'], 'sk': r['sk'], 'en': r['en']},
                                    ensure_ascii=False) + '\n')

    for i, ch in enumerate(chunks, 1):
        dump(os.path.join(out_dir, 'in_%d.jsonl' % i), ch)
    dump(os.path.join(out_dir, 'in_5.jsonl'), hrows)
    with open(os.path.join(out_dir, 'key.jsonl'), 'w', encoding='utf-8') as fh:
        for k in key:
            fh.write(json.dumps(k, ensure_ascii=False) + '\n')

    print('fresh sentences      ', len(sk_of))
    print('fresh items          ', len(fresh_items),
          '(C %d / wrong %d; V %d, TF %d)'
          % (sum(1 for i in fresh_items if i['intent'] == 'C'),
             sum(1 for i in fresh_items if i['intent'] != 'C'),
             sum(1 for i in fresh_items if i['intent'] == 'V'),
             sum(1 for i in fresh_items if i['intent'] == 'TF')))
    print('dev items (1j, armB) ', len(dev))
    print('control duplicates   ', len(ctrl_js), '(re-chunked %d)' % moved)
    print('chunks in_1..in_4    ', [len(c) for c in chunks])
    print('in_5 (1j holdout)    ', len(hrows))
    print('key rows             ', len(key))
    return 0


def selftest():
    import shutil
    import tempfile
    tmp = tempfile.mkdtemp(prefix='p1k_selftest_')
    try:
        fd = os.path.join(tmp, 'fresh')
        od = os.path.join(tmp, 'judge')
        os.makedirs(fd)
        os.makedirs(od)
        shutil.copy(os.path.join(K, 'fresh', 'sentences_fresh.jsonl'), fd)
        os.environ['PHASE1K_OPEN_FRESH'] = '1'
        sents = L.load_fresh_sentences(purpose='selftest', path=os.path.join(
            fd, 'sentences_fresh.jsonl'))
        with open(os.path.join(fd, 'writer_output.jsonl'), 'w', encoding='utf-8') as fh:
            for i, s in enumerate(sents):
                ans = [{'text': 'synthetic correct %d-%d' % (s['sid'], k), 'intent': 'C'}
                       for k in range(3)]
                ans.append({'text': 'synthetic correct %d-0' % s['sid'], 'intent': 'C'})  # dup
                for k, t in enumerate(['T', 'W', 'M', 'S']):
                    ans.append({'text': 'synthetic %s %d-%d' % (t, s['sid'], k), 'intent': t})
                if i % 2 == 0:
                    ans.append({'text': 'synthetic V %d' % s['sid'], 'intent': 'V'})
                if i % 2 == 1:
                    ans.append({'text': 'synthetic TF %d' % s['sid'], 'intent': 'TF'})
                if i < 6:
                    ans.append({'text': 'synthetic V2 %d' % s['sid'], 'intent': 'V'})
                    ans.append({'text': 'synthetic TF2 %d' % s['sid'], 'intent': 'TF'})
                fh.write(json.dumps({'wid': s['sid'], 'answers': ans}, ensure_ascii=False) + '\n')
        run(fd, od, fd)
        # checks
        chunks = [[json.loads(l) for l in open(os.path.join(od, 'in_%d.jsonl' % i),
                                               encoding='utf-8')] for i in range(1, 5)]
        five = [json.loads(l) for l in open(os.path.join(od, 'in_5.jsonl'), encoding='utf-8')]
        key = {json.loads(l)['j']: json.loads(l)
               for l in open(os.path.join(od, 'key.jsonl'), encoding='utf-8')}
        allr = [r for c in chunks for r in c] + five
        assert all(set(r) == {'j', 'sk', 'en'} for r in allr), 'leaky line keys'
        assert len({r['j'] for r in allr}) == len(allr) == len(key), 'id collision'
        assert max(len(c) for c in chunks) - min(len(c) for c in chunks) <= 1, 'unequal chunks'
        assert len(five) == 490, 'in_5 must be the 490 holdout items'
        assert sum(1 for k in key.values() if k['source'] == 'control') == N_CONTROL
        where = {r['j']: i for i, c in enumerate(chunks) for r in c}
        for k in key.values():
            if k['source'] == 'control':
                assert where[k['j']] != where[k['dup_of']], 'control in original chunk'
        items = [json.loads(l) for l in open(os.path.join(fd, 'items_fresh.jsonl'),
                                             encoding='utf-8')]
        assert len({i['id'] for i in items}) == len(items)
        assert all(i['id'].startswith('C:') == (i['intent'] == 'C') for i in items)
        # the duplicate text must have been dropped: 3 C, not 4
        per = {}
        for i in items:
            per.setdefault(i['sid'], []).append(i)
        assert all(sum(1 for x in v if x['intent'] == 'C') == 3 for v in per.values()), 'dedupe'
        # loud failure on a bad writer_output
        with open(os.path.join(fd, 'writer_output.jsonl'), 'a', encoding='utf-8') as fh:
            fh.write(json.dumps({'wid': 1, 'answers': [{'text': 'x', 'intent': 'C'}]}) + '\n')
        try:
            run(fd, od, fd)
        except SystemExit as e:
            assert 'WRITER_OUTPUT ERROR' in str(e), str(e)
        else:
            raise AssertionError('bad writer_output did not fail')
        print('SELFTEST OK')
        return 0
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == '__main__':
    sys.exit(main())
