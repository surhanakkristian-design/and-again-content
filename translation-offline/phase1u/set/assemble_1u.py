#!/usr/bin/env python3
"""Phase 1U assembler — adapted from phase1t/set/assemble_1t.py.  0 model calls.

    python3 phase1u/set/assemble_1u.py                 # validate + select + write
    python3 phase1u/set/assemble_1u.py --dry-run       # validate + select, write nothing

INPUT   phase1u/set/writers/writer_<A1|A2|B1|B2>_part{1,2}.json
        part1 = local ids s01-s15, part2 = s16-s29 (29 sentences per level)
        kinds by local id: s01-s09 FR, s10-s16 MC, s17-s23 MN, s24-s29 SKP

SELECTION per level: keep 25 = 8 FR + 6 MC + 6 MN + 5 SKP.
        drop hard-violating and overlapping sentences first; among the rest prefer
        sentences whose S item (w4 / SKP w3) is tagged `missing-article`, then lowest lid.
        A kind that cannot be filled is topped up from another kind and reported LOUDLY.

IDS     public 1U001-1U100, sid 190001-190100, level blocks per SPLIT_1U.md
        (A1 = 1U001-025, A2 = 026-050, B1 = 051-075, B2 = 076-100); inside each block the
        sids alternate parity across the kept sentences so every kind and every level is
        balanced over the odd/even (P1/P2) halves.
        item ids "<C|W>:<sid>:<aid>" (1T scheme).

OUTPUT  <set>/data/{sentences,annotations,items}.json   (also mirrored to phase1u/data/)
        <set>/assemble_1u.json + ASSEMBLE_REPORT_1U.md
"""
import argparse, collections, glob, json, os, re, shutil, sys, unicodedata

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))              # phase1u/set
PHASE = os.path.dirname(HERE)                                  # phase1u
TOFF = os.path.dirname(PHASE)                                  # translation-offline
sys.path.insert(0, os.path.join(TOFF, 'phase1s'))
try:
    from safe_json import safe_dump                            # noqa: E402
except Exception:                                              # pragma: no cover
    def safe_dump(obj, path):
        tmp = path + '.tmp'
        with open(tmp, 'w', encoding='utf-8') as fh:
            json.dump(obj, fh, ensure_ascii=False, indent=1, sort_keys=False)
        os.replace(tmp, path)

WRITERS = os.path.join(HERE, 'writers')
DATA = os.path.join(HERE, 'data')
MIRROR = os.path.join(PHASE, 'data')
JACCARD_MAX = 0.75

LEVELS = ('A1', 'A2', 'B1', 'B2')
PARTS = ((1, 1, 15), (2, 16, 29))
KIND_RANGES = (('FR', 1, 9), ('MC', 10, 16), ('MN', 17, 23), ('SKP', 24, 29))
KIND_ORDER = ('FR', 'MC', 'MN', 'SKP')
KEEP = {'FR': 8, 'MC': 6, 'MN': 6, 'SKP': 5}
TAGS = ('plain', 'determiner', 'aspect', 'paraphrase', 'by-passive', 'skp-passive',
        'drop-fronted', 'drop-misaligned', 'drop-main', 'drop-other', 'time-frame',
        'missing-article', 'agreement', 'preposition', 'word-order', 'wrong-word')
DROP_TAGS = ('drop-fronted', 'drop-misaligned', 'drop-main', 'drop-other')
ANN_FIELDS = ('v', 'lk', 'alt', 'voice_sk', 'agent_nom', 'tf_gold', 'tense_open',
              'perfective_present')
SENT_TAGS = ('agent_clause', 'agent', 'other_subject', 'passivizable',
             'impersonal_or_passive')
VOICES = ('active_agent', 'passive', 'impersonal')
FRAMES = ('past', 'present', 'future')
INTENTS_W = ('T', 'W', 'M', 'S')
AIDS = ('c1', 'c2', 'c3', 'c4', 'w1', 'w2', 'w3', 'w4', 'w5')
AGENT_CLAUSE = {'FR': 'fronted', 'MC': 'misaligned', 'MN': 'main', 'SKP': None}
EXPECT_DROP = {'FR': 'drop-fronted', 'MC': 'drop-misaligned', 'MN': 'drop-main'}
SOFT = ('alt_small', 'intent_long', 'drop_tag_offshape', 'skp_passive_few',
        'tag_slot_unexpected')


# --------------------------------------------------------------------------- #
def norm(s):
    return re.sub(r'\s+', ' ', (s or '').strip().lower()).strip(' .!?…')


def fold(s):
    t = unicodedata.normalize('NFD', norm(s))
    t = ''.join(c for c in t if not unicodedata.combining(c))
    return re.sub(r'[^\w\s]', ' ', t)


def toks(s):
    return frozenset(w for w in fold(s).split() if w)


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / float(len(a | b))


def _pull(obj):
    rows = obj if isinstance(obj, list) else list(obj.values())
    for r in rows:
        if isinstance(r, str):
            yield r, None
        elif isinstance(r, dict):
            for k in ('slovak', 'sk', 'sentence', 'text'):
                if isinstance(r.get(k), str) and r[k].strip():
                    yield r[k], r.get('sid')
                    break


def earlier_slovak():
    """Every Slovak sentence of every earlier phase (1T's corpus + 1T's own 100)."""
    paths = [os.path.join(TOFF, 'phase1n', 'existing_350.json')]
    for pat in ('phase*/data/sentences*.json', 'phase*/set/data/sentences*.json',
                'phase*/fresh/*.json', 'phase*/existing_*.json'):
        paths += sorted(glob.glob(os.path.join(TOFF, pat)))
    idx, sources, seen = {}, [], set()
    for p in paths:
        if not os.path.exists(p) or os.path.abspath(p) in seen:
            continue
        seen.add(os.path.abspath(p))
        rel = os.path.relpath(p, TOFF)
        if rel.startswith('phase1u' + os.sep):          # our own phase: never a reference
            continue
        try:
            obj = json.load(open(p, encoding='utf-8'))
        except Exception:
            continue
        n_new = 0
        for sk, sid in _pull(obj):
            k = norm(sk)
            if k and k not in idx:
                idx[k] = {'src': rel, 'sid': sid, 'toks': toks(sk)}
                n_new += 1
        if n_new:
            sources.append({'source': rel, 'new_sentences': n_new})
    return idx, sources


# --------------------------------------------------------------------------- #
def kind_of(n):
    for k, lo, hi in KIND_RANGES:
        if lo <= n <= hi:
            return k
    return None


def check_sentence(s, fname, level, viol):
    """Return a row (with .hard = list of hard violation kinds) or None."""
    hard, soft = [], []

    def bad(kind, detail, lid='-', is_soft=False):
        viol.append({'lid': lid, 'level': level, 'kind': kind, 'detail': detail,
                     'file': fname, 'soft': is_soft})
        (soft if is_soft else hard).append(kind)

    if not isinstance(s, dict):
        bad('not_an_object', 'a sentence entry is not an object')
        return None
    raw = str(s.get('lid') or s.get('sid') or '')
    m = re.match(r'^s(\d{2})$', raw)
    if not m:
        bad('bad_lid', 'lid %r (expected s01-s29)' % raw)
        return None
    n = int(m.group(1))
    if not 1 <= n <= 29:
        bad('lid_out_of_range', raw, raw)
        return None
    kind_exp = kind_of(n)
    for k in ('level', 'topic', 'slovak'):
        if not s.get(k):
            bad('missing_field', 'no %r' % k, raw)
    if s.get('level') and s['level'] != level:
        bad('level_mismatch', '%r, %s expected' % (s['level'], level), raw)
    kind = s.get('kind')
    if kind != kind_exp:
        bad('bad_kind', 'kind %r, %s expected for %s' % (kind, kind_exp, raw), raw)
        kind = kind_exp
    st = s.get('tags')
    if not isinstance(st, dict):
        bad('missing_sentence_tags', 'no tags object', raw)
        st = {}
    else:
        for k in SENT_TAGS:
            if k not in st:
                bad('missing_sentence_tag', 'tags.%s' % k, raw)
        if 'agent_clause' in st and st['agent_clause'] != AGENT_CLAUSE[kind_exp]:
            bad('bad_agent_clause', '%r, %r expected' % (st['agent_clause'],
                                                         AGENT_CLAUSE[kind_exp]), raw)
    ann = s.get('annotation') or s.get('ann')
    if not isinstance(ann, dict):
        bad('missing_annotation', 'no annotation object', raw)
        ann = {}
    else:
        for k in ANN_FIELDS:
            if k not in ann:
                bad('missing_annotation_field', k, raw)
        v = [x for x in (ann.get('v') or []) if isinstance(x, str) and x.strip()]
        if len(v) < 2:
            bad('bad_annotation_field', 'v needs two reference translations', raw)
        if not isinstance(ann.get('lk'), list) or not ann.get('lk'):
            bad('bad_annotation_field', 'lk', raw)
        if not isinstance(ann.get('alt'), dict) or not ann.get('alt'):
            bad('bad_annotation_field', 'alt', raw)
        elif len(ann['alt']) < 3:
            bad('alt_small', 'alt has %d entries (3-6 asked)' % len(ann['alt']), raw, True)
        if ann.get('voice_sk') not in VOICES:
            bad('bad_annotation_field', 'voice_sk %r' % ann.get('voice_sk'), raw)
        if ann.get('tf_gold') not in FRAMES:
            bad('bad_annotation_field', 'tf_gold %r' % ann.get('tf_gold'), raw)
        for k in ('agent_nom', 'tense_open', 'perfective_present'):
            if not isinstance(ann.get(k), bool):
                bad('bad_annotation_field', '%s is not a boolean' % k, raw)

    answers = s.get('answers')
    if not isinstance(answers, list):
        bad('missing_answers', 'no answers list', raw)
        answers = []
    by_aid = {}
    nc = nw = 0
    seen_ans = {}
    for a in answers:
        if not isinstance(a, dict):
            bad('bad_answer', 'an answer entry is not an object', raw)
            continue
        aid = a.get('aid')
        if aid not in AIDS:
            bad('bad_aid', repr(aid), raw)
            continue
        if aid in by_aid:
            bad('duplicate_aid', str(aid), raw)
            continue
        by_aid[aid] = a
        if a.get('kind') == 'C':
            nc += 1
        elif a.get('kind') == 'W':
            nw += 1
        else:
            bad('bad_answer_kind', '%s: %r' % (aid, a.get('kind')), raw)
        txt = a.get('answer')
        if not txt or not str(txt).strip():
            bad('empty_answer', str(aid), raw)
            continue
        key = norm(txt)
        if key in seen_ans:
            bad('duplicate_answer', '%s == %s' % (aid, seen_ans[key]), raw)
        seen_ans[key] = aid
        tg = a.get('tags')
        if not isinstance(tg, list) or not tg:
            bad('bad_tags', '%s has no tags' % aid, raw)
            tg = []
        else:
            for t in tg:
                if t not in TAGS:
                    bad('unknown_tag', '%s: %r' % (aid, t), raw)
        if a.get('kind') == 'W':
            if a.get('type') not in INTENTS_W:
                bad('bad_type', '%s: %r' % (aid, a.get('type')), raw)
        elif a.get('kind') == 'C' and a.get('type') is not None:
            bad('bad_type', '%s: type must be null on a correct answer' % aid, raw)
        if isinstance(a.get('intent'), str) and len(a['intent'].split()) > 14:
            bad('intent_long', '%s intent > 14 words' % aid, raw, True)
    missing_aids = [x for x in AIDS if x not in by_aid]
    if missing_aids:
        bad('missing_aids', ','.join(missing_aids), raw)
    if (nc, nw) != (4, 5):
        bad('answer_count_not_4_5', '%d correct + %d wrong' % (nc, nw), raw)

    def tags_of(aid):
        return list((by_aid.get(aid) or {}).get('tags') or [])

    cor_tags = [t for aid in ('c1', 'c2', 'c3', 'c4') for t in tags_of(aid)]
    if kind_exp in ('FR', 'MC', 'MN'):
        n_by = cor_tags.count('by-passive')
        if n_by != 1:
            bad('by_passive_correct_not_one', '%d by-passive correct answers' % n_by, raw)
        for aid in ('w1', 'w2'):
            t = tags_of(aid)
            if not any(x in DROP_TAGS for x in t):
                bad('agent_drop_missing', '%s is not tagged drop-*' % aid, raw)
            elif EXPECT_DROP[kind_exp] not in t:
                bad('drop_tag_offshape', '%s tagged %s, %s expected for %s'
                    % (aid, ','.join(t), EXPECT_DROP[kind_exp], kind_exp), raw, True)
        if 'time-frame' not in tags_of('w3'):
            bad('tag_slot_unexpected', 'w3 is not tagged time-frame', raw, True)
        if 'wrong-word' not in tags_of('w5'):
            bad('tag_slot_unexpected', 'w5 is not tagged wrong-word', raw, True)
    else:
        n_skp = cor_tags.count('skp-passive')
        if n_skp < 3:
            bad('skp_passive_few', 'only %d skp-passive correct answers' % n_skp, raw, True)
        for aid in ('w1', 'w2'):
            if 'time-frame' not in tags_of(aid):
                bad('tag_slot_unexpected', '%s is not tagged time-frame' % aid, raw, True)
        if any(x in DROP_TAGS for x in cor_tags):
            bad('drop_tag_on_correct', 'a correct answer carries a drop-* tag', raw)

    art = [aid for aid in AIDS if 'missing-article' in tags_of(aid)]
    for aid in art:
        if (by_aid.get(aid) or {}).get('kind') != 'W':
            bad('missing_article_correct', '%s tagged missing-article is not wrong' % aid, raw)

    return {'lid': raw, 'n': n, 'level': level, 'kind': kind_exp, 'topic': s.get('topic'),
            'slovak': s.get('slovak') or '', 'wtags': st, 'ann': ann,
            'answers': [by_aid[a] for a in AIDS if a in by_aid],
            'has_article': bool(art), 'hard': hard, 'soft': soft, 'file': fname}


def read_rows(viol):
    rows, files = [], []
    for level in LEVELS:
        for pi, plo, phi in PARTS:
            fname = 'writer_%s_part%d.json' % (level, pi)
            path = os.path.join(WRITERS, fname)
            if not os.path.exists(path):
                viol.append({'lid': '-', 'level': level, 'kind': 'missing_file',
                             'detail': fname, 'file': fname, 'soft': False})
                continue
            files.append(fname)
            try:
                obj = json.load(open(path, encoding='utf-8'))
            except Exception as e:
                viol.append({'lid': '-', 'level': level, 'kind': 'bad_json',
                             'detail': str(e)[:140], 'file': fname, 'soft': False})
                continue
            if isinstance(obj, dict):
                obj = obj.get('sentences') or list(obj.values())
            if not isinstance(obj, list) or not obj:
                viol.append({'lid': '-', 'level': level, 'kind': 'not_a_list',
                             'detail': fname, 'file': fname, 'soft': False})
                continue
            got = set()
            for s in obj:
                r = check_sentence(s, fname, level, viol)
                if r:
                    if r['n'] in got:
                        viol.append({'lid': r['lid'], 'level': level, 'kind': 'duplicate_lid',
                                     'detail': 'seen twice', 'file': fname, 'soft': False})
                        r['hard'].append('duplicate_lid')
                    got.add(r['n'])
                    rows.append(r)
            miss = sorted(set(range(plo, phi + 1)) - got)
            extra = sorted(got - set(range(plo, phi + 1)))
            if miss:
                viol.append({'lid': '-', 'level': level, 'kind': 'part_lid_missing',
                             'detail': ','.join('s%02d' % x for x in miss), 'file': fname,
                             'soft': False})
            if extra:
                viol.append({'lid': '-', 'level': level, 'kind': 'part_lid_unexpected',
                             'detail': ','.join('s%02d' % x for x in extra), 'file': fname,
                             'soft': False})
    return rows, files


# --------------------------------------------------------------------------- #
def passive_of(tags):
    if 'by-passive' in tags:
        return 'by'
    if any(t in DROP_TAGS for t in tags):
        return 'agentless'
    return None


def select(rows, loud):
    """Keep 25 per level (8 FR, 6 MC, 6 MN, 5 SKP); return kept rows + a selection report."""
    kept, sel = [], {}
    for level in LEVELS:
        pool = [r for r in rows if r['level'] == level]
        eligible = collections.defaultdict(list)
        for r in pool:
            if r['hard'] or r.get('overlap'):
                continue
            eligible[r['kind']].append(r)
        for k in eligible:
            eligible[k].sort(key=lambda r: (0 if r['has_article'] else 1, r['n']))
        take, short, fill = {}, {}, []
        for k in KIND_ORDER:
            want = KEEP[k]
            have = eligible[k][:want]
            take[k] = have
            if len(have) < want:
                short[k] = want - len(have)
        for k, need in short.items():
            loud.append('LEVEL %s: kind %s short by %d (only %d usable sentences) — '
                        'topping up from other kinds' % (level, k, need, len(eligible[k])))
            for _ in range(need):
                donors = sorted(KIND_ORDER,
                                key=lambda d: -(len(eligible[d]) - len(take[d])))
                for d in donors:
                    spare = [r for r in eligible[d] if r not in take[d]]
                    if spare:
                        take[d].append(spare[0])
                        fill.append({'level': level, 'short_kind': k, 'filled_with': d,
                                     'lid': spare[0]['lid']})
                        loud.append('LEVEL %s: filled a %s slot with %s sentence %s'
                                    % (level, k, d, spare[0]['lid']))
                        break
                else:
                    loud.append('LEVEL %s: NO sentence left to fill a %s slot — the level is '
                                'SHORT' % (level, k))
        chosen = [r for k in KIND_ORDER for r in sorted(take[k], key=lambda r: r['n'])]
        kept += chosen
        sel[level] = {
            'eligible_by_kind': {k: len(eligible[k]) for k in KIND_ORDER},
            'kept_by_kind': dict(collections.Counter(r['kind'] for r in chosen)),
            'kept': [r['lid'] for r in chosen],
            'dropped': [{'lid': r['lid'], 'kind': r['kind'],
                         'why': ('hard:' + ','.join(sorted(set(r['hard'])))) if r['hard']
                         else (r.get('overlap') or 'not selected (surplus)')}
                        for r in sorted(pool, key=lambda r: r['n']) if r not in chosen],
            'kept_total': len(chosen), 'short_by_kind': short, 'fills': fill}
        if len(chosen) != 25:
            loud.append('LEVEL %s: %d sentences kept, 25 required' % (level, len(chosen)))
    return kept, sel


def assign_ids(kept):
    """Level blocks per SPLIT_1U.md; inside a block parity alternates over the kept order."""
    out = []
    for li, level in enumerate(LEVELS):
        base = 25 * li
        block = [r for r in kept if r['level'] == level]
        odd = [base + p for p in range(1, 26) if (base + p) % 2 == 1]
        even = [base + p for p in range(1, 26) if (base + p) % 2 == 0]
        pools = [odd, even] if len(odd) >= len(even) else [even, odd]
        block.sort(key=lambda r: (KIND_ORDER.index(r['kind']), r['n']))
        for j, r in enumerate(block):
            pool = pools[j % 2] or pools[(j + 1) % 2]
            r['num'] = pool.pop(0)
            r['pid'] = '1U%03d' % r['num']
            r['sid'] = 190000 + r['num']
            r['half'] = 'P1' if r['num'] % 2 == 1 else 'P2'
            out.append(r)
    out.sort(key=lambda r: r['sid'])
    return out


def build(dry_run=False):
    viol, loud = [], []
    rows, files = read_rows(viol)

    ex, sources = earlier_slovak()
    ex_tok = [(v['toks'], v) for v in ex.values()]
    seen_sk = {}
    overlaps = []
    for r in sorted(rows, key=lambda r: (r['level'], r['n'])):
        k = norm(r['slovak'])
        if not k:
            continue
        if k in seen_sk:
            r['overlap'] = 'duplicate of %s (this set)' % seen_sk[k]
            overlaps.append({'lid': r['lid'], 'level': r['level'], 'kind': 'internal_exact',
                             'detail': r['overlap']})
            continue
        best_in, bj_in = None, 0.0
        for o in rows:
            if o is r or not o.get('slovak'):
                continue
            j = jaccard(toks(r['slovak']), toks(o['slovak']))
            if j > bj_in:
                bj_in, best_in = j, o
        if bj_in >= JACCARD_MAX and best_in is not None and norm(best_in['slovak']) in seen_sk:
            r['overlap'] = 'J=%.2f with %s/%s (this set)' % (bj_in, best_in['level'],
                                                             best_in['lid'])
            overlaps.append({'lid': r['lid'], 'level': r['level'], 'kind': 'internal_jaccard',
                             'detail': r['overlap']})
            continue
        if k in ex:
            r['overlap'] = 'exact collision with %s (%s)' % (ex[k]['sid'], ex[k]['src'])
            overlaps.append({'lid': r['lid'], 'level': r['level'], 'kind': 'overlap_exact',
                             'detail': r['overlap']})
            continue
        t = toks(r['slovak'])
        best, bj = None, 0.0
        for et, ev in ex_tok:
            j = jaccard(t, et)
            if j > bj:
                bj, best = j, ev
        if bj >= JACCARD_MAX:
            r['overlap'] = 'J=%.2f with %s (%s)' % (bj, best['sid'], best['src'])
            overlaps.append({'lid': r['lid'], 'level': r['level'], 'kind': 'overlap_jaccard',
                             'detail': r['overlap']})
            continue
        seen_sk[k] = '%s/%s' % (r['level'], r['lid'])

    kept, sel = select(rows, loud)
    kept = assign_ids(kept)

    sents, ann, items = [], {}, []
    for r in kept:
        sents.append({'sid': r['sid'], 'pid': r['pid'], 'slovak': r['slovak'],
                      'level': r['level'], 'topic': r['topic'],
                      'tags': {'half': r['half'], 'level': r['level'], 'kind': r['kind'],
                               'emb': r['kind'] in ('FR', 'MC'),
                               'tf_gold': (r['ann'] or {}).get('tf_gold'),
                               'writer_tags': dict(r['wtags'] or {}, kind=r['kind'],
                                                   lid=r['lid'])}})
        a = dict(r['ann'])
        core = {k: a[k] for k in ('v', 'lk', 'alt', 'm', 'lv', 't', 'id') if k in a}
        core.setdefault('id', r['sid'])
        core.setdefault('lv', r['level'])
        ann[str(r['sid'])] = dict({k: v for k, v in a.items() if k not in core},
                                  hygienised=core, raw=core)
        for x in r['answers']:
            tg = list(x.get('tags') or [])
            items.append({'id': '%s:%d:%s' % (x.get('kind'), r['sid'], x['aid']),
                          'sid': r['sid'], 'kind': x.get('kind'),
                          'intent': x.get('type') if x.get('kind') == 'W' else 'C',
                          'form': None, 'tags': tg, 'passive': passive_of(tg),
                          'answer': x['answer'], 'writer_intent': x.get('intent')})

    hard = [v for v in viol if not v.get('soft')]
    ze = sum(1 for s in sents if s['tags']['kind'] == 'MC'
             and re.search(r'\bže\b', s['slovak'] or '', re.I))
    tag_counts = collections.Counter(t for i in items for t in i['tags'])
    tag_by_level = collections.defaultdict(collections.Counter)
    sid_level = {s['sid']: s['level'] for s in sents}
    for i in items:
        for t in i['tags']:
            tag_by_level[sid_level[i['sid']]][t] += 1
    floors_by_construction = {
        'F1_agent_drops': sum(tag_counts[t] for t in DROP_TAGS),
        'F1a_drop_fronted': tag_counts['drop-fronted'],
        'F1b_drop_misaligned': tag_counts['drop-misaligned'],
        'F2_time_frame': tag_counts['time-frame'],
        'F3_by_passive': tag_counts['by-passive'],
        'F4_skp_passive': tag_counts['skp-passive'],
        'F5_missing_article': tag_counts['missing-article']}
    rep = {'writer_files_read': len(files), 'sentences_read': len(rows),
           'sentences_kept': len(sents), 'items': len(items),
           'levels': dict(collections.Counter(s['level'] for s in sents)),
           'halves': dict(collections.Counter(s['tags']['half'] for s in sents)),
           'kinds': dict(collections.Counter(s['tags']['kind'] for s in sents)),
           'kind_by_half': {h: dict(collections.Counter(
               s['tags']['kind'] for s in sents if s['tags']['half'] == h))
               for h in ('P1', 'P2')},
           'level_by_half': {h: dict(collections.Counter(
               s['level'] for s in sents if s['tags']['half'] == h)) for h in ('P1', 'P2')},
           'ze_clause_sentences': ze,
           'answer_kinds': dict(collections.Counter(i['kind'] for i in items)),
           'answer_tags': dict(sorted(tag_counts.items())),
           'answer_tags_by_level': {k: dict(sorted(v.items()))
                                    for k, v in sorted(tag_by_level.items())},
           'wrong_types': dict(collections.Counter(i['intent'] for i in items
                                                   if i['kind'] == 'W')),
           'tf_gold': dict(collections.Counter(s['tags']['tf_gold'] for s in sents)),
           'floor_counts_by_construction': floors_by_construction,
           'earlier_sentences_checked_against': len(ex), 'overlap_sources': sources,
           'overlaps': overlaps, 'overlaps_total': len(overlaps),
           'violations_total': len(viol), 'hard_violations': len(hard),
           'violations_by_kind': dict(collections.Counter(v['kind'] for v in viol)),
           'hard_violations_by_kind': dict(collections.Counter(v['kind'] for v in hard)),
           'violations': viol, 'selection': sel, 'loud': loud,
           'outputs_written': False}

    ok = len(sents) == 100 and len(items) == 900
    if not ok:
        loud.append('SET INCOMPLETE: %d sentences / %d items (100 / 900 required)'
                    % (len(sents), len(items)))
    if not dry_run and ok:
        for d in (DATA, MIRROR):
            os.makedirs(d, exist_ok=True)
            safe_dump(sents, os.path.join(d, 'sentences.json'))
            safe_dump(ann, os.path.join(d, 'annotations.json'))
            safe_dump(items, os.path.join(d, 'items.json'))
        rep['outputs_written'] = True
        rep['data_dirs'] = [DATA, MIRROR]
    safe_dump(rep, os.path.join(HERE, 'assemble_1u.json'))
    write_report(rep)
    slim = {k: v for k, v in rep.items()
            if k not in ('violations', 'selection', 'overlap_sources')}
    print(json.dumps(slim, indent=1, sort_keys=True, ensure_ascii=False))
    for line in loud:
        print('LOUD: ' + line)
    return 0 if ok else 2


def write_report(rep):
    p = os.path.join(HERE, 'ASSEMBLE_REPORT_1U.md')
    L = ['# ASSEMBLE_REPORT_1U (0 model calls)', '',
         '- writer files read: %d · sentences read: %d · kept: %d · items: %d'
         % (rep['writer_files_read'], rep['sentences_read'], rep['sentences_kept'],
            rep['items']),
         '- earlier sentences checked against: %d · overlaps found: %d'
         % (rep['earlier_sentences_checked_against'], rep['overlaps_total']),
         '- violations: %d (hard %d) · outputs written: %s'
         % (rep['violations_total'], rep['hard_violations'], rep['outputs_written']), '',
         '## tag counts (written items)', '']
    for k, v in sorted(rep['answer_tags'].items()):
        L.append('- %s: %d' % (k, v))
    L += ['', '## violations', '', '| level | lid | kind | detail | file | soft |',
          '| --- | --- | --- | --- | --- | --- |']
    for v in rep['violations']:
        L.append('| %s | %s | %s | %s | %s | %s |'
                 % (v.get('level', ''), v['lid'], v['kind'], str(v['detail'])[:110],
                    v.get('file', ''), v.get('soft', False)))
    if not rep['violations']:
        L.append('| — | — | none | the set is clean | | |')
    L += ['', '## overlaps', '']
    for o in rep['overlaps']:
        L.append('- %s/%s — %s: %s' % (o['level'], o['lid'], o['kind'], o['detail']))
    if not rep['overlaps']:
        L.append('- none')
    L += ['', '## dropped per level', '']
    for lvl, s in sorted(rep['selection'].items()):
        L.append('- **%s** kept %d %s; dropped: %s' % (
            lvl, s['kept_total'], s['kept_by_kind'],
            ', '.join('%s (%s)' % (d['lid'], d['why']) for d in s['dropped']) or 'none'))
    L += ['', '## loud', ''] + (['- ' + x for x in rep['loud']] or ['- nothing'])
    open(p, 'w', encoding='utf-8').write('\n'.join(L) + '\n')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args()
    raise SystemExit(build(a.dry_run))
