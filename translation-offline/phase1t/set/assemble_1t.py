#!/usr/bin/env python3
"""Phase 1T assembler — adapted from phase1p/assemble_1p.py.  0 model calls.

    python3 phase1t/set/assemble_1t.py             # REFUSE (exit 2) on any violation
    python3 phase1t/set/assemble_1t.py --report    # write ASSEMBLE_REPORT_1T.md instead of refusing
    python3 phase1t/set/assemble_1t.py --labels    # additionally join the judge verdicts

INPUT (declared in WRITER_SPEC_1T.md / SPLIT_1T.md, before any data exists)
  data/writer_W{1,2,3,4}_part{1,2,3}.json     W1=1T001-025 A1, W2=026-050 A2,
                                              W3=051-075 B1, W4=076-100 B2
                                              parts = sentences 1-9, 10-17, 18-25 of the range
  numeric sid = 180000 + the number in the writer SID; item id "<C|W>:<sid>:<aid>".

OUTPUT (loader_1p schema)  data/sentences.json, data/annotations.json, data/items.json
  sentences[].tags = {half, level, kind, emb, tf_gold, writer_tags{...}}
  items[].tags     = the writer's answer tags (WRITER_SPEC_1T.md list)

REFUSALS: not 4 C + 5 W · duplicate answer strings inside a sentence · unknown tag ·
  missing annotation field · duplicate Slovak inside the set · overlap with any earlier
  phase (exact normalised match OR token-Jaccard >= 0.75).
"""
import argparse, collections, glob, json, os, re, sys, unicodedata

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))              # phase1t/set
TOFF = os.path.dirname(os.path.dirname(HERE))                  # translation-offline
sys.path.insert(0, os.path.join(TOFF, 'phase1s'))
from safe_json import safe_dump                                # noqa: E402

DATA = os.path.join(HERE, 'data')
JUDGE = os.path.join(HERE, 'judge')
SID_RE = re.compile(r'^1T(\d{3})$')
JACCARD_MAX = 0.75

TAGS = ('plain', 'determiner', 'aspect', 'by-passive', 'by-passive-embedded', 'skp-passive',
        'timeframe', 'agentdrop-main', 'agentdrop-embedded', 'number')
ANN_FIELDS = ('v', 'lk', 'alt', 'voice_sk', 'agent_nom', 'tf_gold', 'tense_open',
              'perfective_present')
SENT_TAGS = ('nom_agent', 'agent', 'emb_agent', 'emb_type', 'passivizable',
             'impersonal_or_passive')
VOICES = ('active_agent', 'passive', 'impersonal')
FRAMES = ('past', 'present', 'future')
INTENTS_W = ('T', 'W', 'M', 'S')
LEVELS = ((1, 25, 'A1', 'W1'), (26, 50, 'A2', 'W2'), (51, 75, 'B1', 'W3'), (76, 100, 'B2', 'W4'))
PARTS = ((1, 9), (10, 17), (18, 25))


# --------------------------------------------------------------------------- #
# normalisation / overlap
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
    """Yield Slovak strings out of any earlier-phase container shape."""
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
    """Every Slovak sentence of every earlier phase.  Returns (index, sources)."""
    paths = [os.path.join(TOFF, 'phase1n', 'existing_350.json')]
    for pat in ('phase*/data/sentences*.json', 'phase*/fresh/*.json', 'phase*/existing_*.json'):
        paths += sorted(glob.glob(os.path.join(TOFF, pat)))
    idx, sources, seen = {}, [], set()
    for p in paths:
        if not os.path.exists(p) or os.path.abspath(p) in seen:
            continue
        seen.add(os.path.abspath(p))
        rel = os.path.relpath(p, TOFF)
        if rel.startswith('phase1t' + os.sep):
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
        sources.append({'source': rel, 'new_sentences': n_new})
    return idx, sources


# --------------------------------------------------------------------------- #
# reading the writer files
# --------------------------------------------------------------------------- #
def half_of(n):
    return 'P1' if int(n) % 2 == 1 else 'P2'


def check_sentence(s, fname, level_expected, viol):
    def bad(kind, detail, sid='-'):
        viol.append({'sid': sid, 'kind': kind, 'detail': detail, 'file': fname})

    if not isinstance(s, dict):
        bad('not_an_object', 'a sentence entry is not an object')
        return None
    raw = str(s.get('sid', ''))
    m = SID_RE.match(raw)
    if not m:
        bad('bad_sid', 'sid %r (expected 1Tnnn)' % raw)
        return None
    n = int(m.group(1))
    sid = raw
    if not 1 <= n <= 100:
        bad('sid_out_of_range', 'sid outside 1T001-1T100', sid)
        return None
    for k in ('level', 'topic', 'slovak'):
        if not s.get(k):
            bad('missing_field', 'no %r' % k, sid)
    if s.get('level') and s['level'] != level_expected:
        bad('level_mismatch', 'level %r, %s expected for this SID range' % (s['level'],
                                                                           level_expected), sid)
    kind = s.get('kind')
    if kind not in ('ACT', 'SKP'):
        bad('bad_kind', 'kind %r (ACT|SKP)' % kind, sid)
    if not isinstance(s.get('emb'), bool):
        bad('bad_emb', 'emb is not a boolean', sid)
    st = s.get('tags')
    if not isinstance(st, dict):
        bad('missing_sentence_tags', 'no tags object', sid)
        st = {}
    else:
        for k in SENT_TAGS:
            if k not in st:
                bad('missing_sentence_tag', 'tags.%s' % k, sid)

    ann = s.get('annotation') or s.get('ann') or s.get('hygienised')
    if not isinstance(ann, dict):
        bad('missing_annotation', 'no annotation object', sid)
        ann = {}
    else:
        for k in ANN_FIELDS:
            if k not in ann:
                bad('missing_annotation_field', k, sid)
        v = [x for x in (ann.get('v') or []) if isinstance(x, str) and x.strip()]
        if len(v) < 2:
            bad('bad_annotation_field', 'v needs two reference translations', sid)
        if not isinstance(ann.get('lk'), list) or not ann.get('lk'):
            bad('bad_annotation_field', 'lk', sid)
        if not isinstance(ann.get('alt'), dict) or not ann.get('alt'):
            bad('bad_annotation_field', 'alt', sid)
        if ann.get('voice_sk') not in VOICES:
            bad('bad_annotation_field', 'voice_sk %r' % ann.get('voice_sk'), sid)
        if ann.get('tf_gold') not in FRAMES:
            bad('bad_annotation_field', 'tf_gold %r' % ann.get('tf_gold'), sid)
        for k in ('agent_nom', 'tense_open', 'perfective_present'):
            if not isinstance(ann.get(k), bool):
                bad('bad_annotation_field', '%s is not a boolean' % k, sid)

    answers = s.get('answers') or s.get('items')
    if not isinstance(answers, list):
        bad('missing_answers', 'no answers list', sid)
        answers = []
    nc = sum(1 for a in answers if isinstance(a, dict) and a.get('kind') == 'C')
    nw = sum(1 for a in answers if isinstance(a, dict) and a.get('kind') == 'W')
    if (nc, nw) != (4, 5):
        bad('answer_count_not_4_5', '%d correct + %d wrong' % (nc, nw), sid)
    seen_aid, seen_ans = set(), {}
    for a in answers:
        if not isinstance(a, dict):
            bad('bad_answer', 'an answer entry is not an object', sid)
            continue
        aid = a.get('aid')
        if not aid:
            bad('bad_answer', 'an answer has no aid', sid)
            continue
        if aid in seen_aid:
            bad('duplicate_aid', str(aid), sid)
        seen_aid.add(aid)
        if not a.get('answer') or not str(a.get('answer')).strip():
            bad('empty_answer', str(aid), sid)
            continue
        key = norm(a['answer'])
        if key in seen_ans:
            bad('duplicate_answer', '%s == %s' % (aid, seen_ans[key]), sid)
        seen_ans[key] = aid
        tg = a.get('tags')
        if not isinstance(tg, list) or not tg:
            bad('bad_tags', '%s has no tags' % aid, sid)
        else:
            for t in tg:
                if t not in TAGS:
                    bad('unknown_tag', '%s: %r' % (aid, t), sid)
        if a.get('kind') == 'W':
            if a.get('intent') not in INTENTS_W:
                bad('bad_intent', '%s: %r' % (aid, a.get('intent')), sid)
        elif a.get('kind') == 'C':
            if a.get('intent') not in ('C', None):
                bad('bad_intent', '%s: %r' % (aid, a.get('intent')), sid)
        else:
            bad('bad_answer_kind', '%s: %r' % (aid, a.get('kind')), sid)
    return {'n': n, 'raw_sid': sid, 'sid': 180000 + n, 'level': s.get('level') or level_expected,
            'topic': s.get('topic'), 'slovak': s.get('slovak') or '', 'kind': kind,
            'emb': bool(s.get('emb')), 'wtags': st, 'ann': ann, 'answers': answers}


def read_rows(data_dir, viol):
    rows = []
    for lo, hi, lvl, w in LEVELS:
        base = lo - 1
        for pi, (plo, phi) in enumerate(PARTS, 1):
            fname = 'writer_%s_part%d.json' % (w, pi)
            path = os.path.join(data_dir, fname)
            if not os.path.exists(path):
                viol.append({'sid': '-', 'kind': 'missing_file', 'detail': fname, 'file': fname})
                continue
            try:
                obj = json.load(open(path, encoding='utf-8'))
            except Exception as e:
                viol.append({'sid': '-', 'kind': 'bad_json', 'detail': str(e)[:120],
                             'file': fname})
                continue
            if not isinstance(obj, list) or not obj:
                viol.append({'sid': '-', 'kind': 'not_a_list', 'detail': fname, 'file': fname})
                continue
            got = set()
            for s in obj:
                r = check_sentence(s, fname, lvl, viol)
                if r:
                    rows.append(r)
                    got.add(r['n'])
            expect = set(range(base + plo, base + phi + 1))
            miss, extra = sorted(expect - got), sorted(got - expect)
            if miss:
                viol.append({'sid': '-', 'kind': 'part_sid_missing',
                             'detail': ','.join('1T%03d' % x for x in miss), 'file': fname})
            if extra:
                viol.append({'sid': '-', 'kind': 'part_sid_unexpected',
                             'detail': ','.join('1T%03d' % x for x in extra), 'file': fname})
    return rows


# --------------------------------------------------------------------------- #
# build
# --------------------------------------------------------------------------- #
def passive_of(tags):
    if 'by-passive' in tags or 'by-passive-embedded' in tags:
        return 'by'
    if 'agentdrop-main' in tags or 'agentdrop-embedded' in tags:
        return 'agentless'
    return None


def build(report=False, labels=False, data_dir=None, out_dir=None, judge_dir=None):
    data_dir = data_dir or DATA
    out_dir = out_dir or data_dir
    judge_dir = judge_dir or (JUDGE if data_dir == DATA else
                              os.path.join(os.path.dirname(data_dir), 'judge'))
    viol = []
    rows = read_rows(data_dir, viol)
    rows.sort(key=lambda r: r['sid'])

    seen_sid, seen_sk = {}, {}
    ex, sources = earlier_slovak()
    ex_tok = [(v['toks'], k, v) for k, v in ex.items()]
    for r in rows:
        if r['n'] in seen_sid:
            viol.append({'sid': r['raw_sid'], 'kind': 'duplicate_sid',
                         'detail': 'seen twice', 'file': ''})
        seen_sid[r['n']] = r['raw_sid']
        k = norm(r['slovak'])
        if k in seen_sk:
            viol.append({'sid': r['raw_sid'], 'kind': 'duplicate_slovak',
                         'detail': 'same as %s' % seen_sk[k], 'file': ''})
        seen_sk[k] = r['raw_sid']
        if k in ex:
            viol.append({'sid': r['raw_sid'], 'kind': 'overlap_exact',
                         'detail': 'collides with %s (%s)' % (ex[k]['sid'], ex[k]['src']),
                         'file': ''})
            continue
        t = toks(r['slovak'])
        best, bj = None, 0.0
        for et, ek, ev in ex_tok:
            j = jaccard(t, et)
            if j > bj:
                bj, best = j, ev
        if bj >= JACCARD_MAX:
            viol.append({'sid': r['raw_sid'], 'kind': 'overlap_jaccard',
                         'detail': 'J=%.2f with %s (%s)' % (bj, best['sid'], best['src']),
                         'file': ''})

    sents, ann, items = [], {}, []
    for r in rows:
        sents.append({'sid': r['sid'], 'slovak': r['slovak'], 'level': r['level'],
                      'topic': r['topic'],
                      'tags': {'half': half_of(r['n']), 'level': r['level'], 'kind': r['kind'],
                               'emb': r['emb'], 'tf_gold': (r['ann'] or {}).get('tf_gold'),
                               'writer_tags': dict(r['wtags'] or {},
                                                   kind=r['kind'], emb=r['emb'])}})
        a = dict(r['ann'])
        core = {k: a[k] for k in ('v', 'lk', 'alt', 'm', 'lv', 't', 'id') if k in a}
        core.setdefault('id', r['sid'])
        core.setdefault('lv', r['level'])
        ann[str(r['sid'])] = dict({k: v for k, v in a.items() if k not in core},
                                  hygienised=core, raw=core)
        for x in r['answers']:
            if not isinstance(x, dict) or not x.get('aid') or not x.get('answer'):
                continue
            tg = list(x.get('tags') or [])
            items.append({'id': '%s:%d:%s' % (x.get('kind'), r['sid'], x['aid']),
                          'sid': r['sid'], 'kind': x.get('kind'), 'intent': x.get('intent'),
                          'form': x.get('form'), 'tags': tg, 'passive': passive_of(tg),
                          'answer': x['answer']})

    by_kind = collections.Counter(v['kind'] for v in viol)
    rep = {'writer_files_read': 12 - by_kind.get('missing_file', 0),
           'sentences': len(sents), 'items': len(items),
           'levels': dict(collections.Counter(s['level'] for s in sents)),
           'halves': dict(collections.Counter(s['tags']['half'] for s in sents)),
           'kinds_sentence': dict(collections.Counter(s['tags']['kind'] for s in sents)),
           'emb_sentences': sum(1 for s in sents if s['tags']['emb']),
           'answer_kinds': dict(collections.Counter(i['kind'] for i in items)),
           'answer_tags': dict(collections.Counter(t for i in items for t in i['tags'])),
           'intents_wrong': dict(collections.Counter(i['intent'] for i in items
                                                     if i['kind'] == 'W')),
           'earlier_sentences_checked_against': len(ex),
           'overlap_sources': sources,
           'violations_total': len(viol), 'violations_by_kind': dict(by_kind)}

    if viol and not report:
        print(json.dumps({'REFUSED': True, 'violations_by_kind': dict(by_kind),
                          'violations_total': len(viol),
                          'sids': sorted({v['sid'] for v in viol if v['sid'] != '-'})},
                         indent=1, sort_keys=True))
        print('REFUSED: %d violations — rerun with --report for the per-sid list' % len(viol))
        return 2

    if not viol:
        os.makedirs(out_dir, exist_ok=True)
        safe_dump(sents, os.path.join(out_dir, 'sentences.json'))
        safe_dump(ann, os.path.join(out_dir, 'annotations.json'))
        safe_dump(items, os.path.join(out_dir, 'items.json'))
        rep['outputs_written'] = True
    else:
        rep['outputs_written'] = False
        rep['note'] = 'outputs NOT written: violations must be sent back to the writer first'

    if labels:
        rep['labels'] = join_labels(items, judge_dir, out_dir)

    if report:
        write_report(rep, viol, out_dir)
    safe_dump(rep, os.path.join(os.path.dirname(out_dir.rstrip(os.sep)) or HERE,
                                'assemble_1t.json'))
    print(json.dumps(rep, indent=1, sort_keys=True))
    return 0


def write_report(rep, viol, out_dir):
    base = os.path.dirname(out_dir.rstrip(os.sep)) or HERE
    p = os.path.join(base, 'ASSEMBLE_REPORT_1T.md')
    by_sid = collections.defaultdict(list)
    for v in viol:
        by_sid[v['sid']].append(v)
    L = ['# ASSEMBLE_REPORT_1T — violations by sid (0 model calls)', '',
         '- sentences read: %d · items: %d · violations: %d'
         % (rep['sentences'], rep['items'], rep['violations_total']),
         '- earlier sentences checked against: %d' % rep['earlier_sentences_checked_against'],
         '- outputs written: %s' % rep['outputs_written'], '',
         '## by kind', '']
    for k, n in sorted(rep['violations_by_kind'].items()):
        L.append('- %s: %d' % (k, n))
    L += ['', '## by sid (send these single sentences back to the writer)', '',
          '| sid | kind | detail | file |', '| --- | --- | --- | --- |']
    for sid in sorted(by_sid):
        for v in by_sid[sid]:
            L.append('| %s | %s | %s | %s |' % (sid, v['kind'], v['detail'], v.get('file', '')))
    if not viol:
        L.append('| — | none | the set is clean | |')
    open(p, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    return p


# --------------------------------------------------------------------------- #
# judge labels
# --------------------------------------------------------------------------- #
def load_key(judge_dir):
    for p in (os.path.join(judge_dir, '_private', '_key.json'),
              os.path.join(judge_dir, '_key.json')):
        if os.path.exists(p):
            return json.load(open(p, encoding='utf-8')), p
    return {}, None


def join_labels(items, judge_dir, out_dir):
    key, kp = load_key(judge_dir)
    if not key:
        return {'note': 'no judge key found — labels not joined'}
    paths = sorted(set(glob.glob(os.path.join(judge_dir, 'verdicts_P*.json')) +
                       glob.glob(os.path.join(judge_dir, 'verdicts_*.json'))))
    ids = {i['id'] for i in items}
    rows, n_rows = {}, 0
    for p in paths:
        try:
            obj = json.load(open(p, encoding='utf-8'))
        except Exception:
            continue
        for r in (obj if isinstance(obj, list) else obj.get('verdicts') or []):
            if isinstance(r, dict) and r.get('jid'):
                n_rows += 1
                rows[r['jid']] = r

    def rec(r):
        return {'judged': r.get('judged'),
                'type': r.get('type') if r.get('judged') == 'wrong' else None,
                'passive': r.get('passive'), 'agent_drop': r.get('agent_drop'),
                'tip': bool(r.get('tip')), 'borderline': bool(r.get('borderline'))}

    labels, dup_pairs, missing = {}, [], []
    for jid, k in key.items():
        iid = k.get('item') or k.get('iid') or k.get('id')
        if iid not in ids:
            continue
        r = rows.get(jid)
        if r is None:
            missing.append(jid)
            continue
        if k.get('duplicate_of'):
            dup_pairs.append((k['duplicate_of'], jid, iid))
        else:
            labels[iid] = rec(r)
    dis, type_dis, judged_dups = 0, 0, 0
    for orig, dup, iid in dup_pairs:
        a, b = rows.get(orig), rows.get(dup)
        if not a or not b:
            continue
        judged_dups += 1
        if a.get('judged') != b.get('judged'):
            dis += 1
        elif a.get('judged') == 'wrong' and a.get('type') != b.get('type'):
            type_dis += 1
    safe_dump(labels, os.path.join(out_dir, 'labels.json'))
    return {'key': os.path.relpath(kp, HERE), 'verdict_files': len(paths),
            'verdict_rows': n_rows, 'items_labelled': len(labels),
            'unlabelled_items': len(ids) - len(labels), 'missing_verdicts': len(missing),
            'duplicate_controls': len(dup_pairs), 'duplicate_controls_judged': judged_dups,
            'label_disagreements': dis,
            'judge_noise_pct': round(100.0 * dis / judged_dups, 2) if judged_dups else None,
            'type_only_disagreements': type_dis,
            'judged': dict(collections.Counter(v['judged'] for v in labels.values())),
            'types': dict(collections.Counter(v['type'] for v in labels.values()
                                              if v['judged'] == 'wrong'))}


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--report', action='store_true')
    ap.add_argument('--labels', action='store_true')
    ap.add_argument('--data-dir')
    ap.add_argument('--out-dir')
    ap.add_argument('--judge-dir')
    a = ap.parse_args()
    raise SystemExit(build(a.report, a.labels, a.data_dir, a.out_dir, a.judge_dir))
