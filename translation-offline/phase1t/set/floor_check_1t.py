#!/usr/bin/env python3
"""Phase 1T floor check on the JUDGED labels — run BEFORE any model run.  0 model calls.

    python3 phase1t/set/floor_check_1t.py
    python3 phase1t/set/floor_check_1t.py --make-fixture [dir]      # synthetic writer files
    python3 phase1t/set/floor_check_1t.py --make-verdicts [dir]     # synthetic judge verdicts

STOPS (exit 2, writes STOP_FLOOR.txt) unless all five floors hold (SPLIT_1T.md):
    F1 agentdrop-main|agentdrop-embedded judged WRONG    >= 120
    F2 agentdrop-embedded              judged WRONG      >=  60
    F3 timeframe                       judged WRONG      >= 100
    F4 by-passive|by-passive-embedded  judged CORRECT    >=  60
    F5 answers of SKP sentences        judged CORRECT    >=  40
Writes FLOOR_CHECK_1T.md and FLOOR_CHECK_1T.json either way, with the T/W/M/S table of
judged-wrong types and the writer-intent x judged cross-table, overall / per level / per half.
"""
import argparse, collections, json, os, random, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
TOFF = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(TOFF, 'phase1s'))
sys.path.insert(0, HERE)
from safe_json import safe_dump                                # noqa: E402
import assemble_1t as A                                        # noqa: E402

FLOORS = {'F1_agentdrop_any_wrong': 120, 'F2_agentdrop_embedded_wrong': 60,
          'F3_timeframe_wrong': 100, 'F4_by_passive_correct': 60, 'F5_skp_correct': 40}
AGDROP = ('agentdrop-main', 'agentdrop-embedded')
BYPASS = ('by-passive', 'by-passive-embedded')


# --------------------------------------------------------------------------- #
# check
# --------------------------------------------------------------------------- #
def run(data_dir=None, judge_dir=None, out_dir=None):
    data_dir = data_dir or os.path.join(HERE, 'data')
    base = os.path.dirname(data_dir.rstrip(os.sep))
    judge_dir = judge_dir or os.path.join(base, 'judge')
    out_dir = out_dir or base
    sents = {int(s['sid']): s for s in
             json.load(open(os.path.join(data_dir, 'sentences.json'), encoding='utf-8'))}
    items = json.load(open(os.path.join(data_dir, 'items.json'), encoding='utf-8'))
    lp = os.path.join(data_dir, 'labels.json')
    if not os.path.exists(lp):
        A.join_labels(items, judge_dir, data_dir)
    if not os.path.exists(lp):
        print('REFUSED: no judged labels (data/labels.json) — the judge has not delivered')
        return 2
    labels = json.load(open(lp, encoding='utf-8'))

    got = collections.Counter()
    twms = collections.defaultdict(collections.Counter)      # scope -> type
    cross = collections.defaultdict(collections.Counter)     # scope -> "intent/judged"
    per = collections.defaultdict(collections.Counter)       # scope -> floor counts
    unlabelled = 0
    for it in items:
        s = sents[int(it['sid'])]
        lvl, half = s['level'], s['tags'].get('half')
        skp = (s['tags'].get('kind') or (s['tags'].get('writer_tags') or {}).get('kind')) == 'SKP'
        lab = labels.get(it['id'])
        if not lab:
            unlabelled += 1
            continue
        j, t = lab.get('judged'), lab.get('type')
        tags = it.get('tags') or []
        scopes = ('all', 'level:%s' % lvl, 'half:%s' % half)
        hit = []
        if j == 'wrong':
            if [x for x in tags if x in AGDROP]:
                hit.append('F1_agentdrop_any_wrong')
            if 'agentdrop-embedded' in tags:
                hit.append('F2_agentdrop_embedded_wrong')
            if 'timeframe' in tags:
                hit.append('F3_timeframe_wrong')
        elif j == 'correct':
            if [x for x in tags if x in BYPASS]:
                hit.append('F4_by_passive_correct')
            if skp:
                hit.append('F5_skp_correct')
        for k in hit:
            got[k] += 1
        for sc in scopes:
            for k in hit:
                per[sc][k] += 1
            if j == 'wrong':
                twms[sc][t or '?'] += 1
            cross[sc]['%s/%s' % (it.get('intent') or 'C',
                                 j if j != 'wrong' else 'wrong:%s' % (t or '?'))] += 1

    fails = {k: {'got': got[k], 'required': v} for k, v in FLOORS.items() if got[k] < v}
    rep = {'sentences': len(sents), 'items': len(items), 'labelled': len(labels),
           'unlabelled_items': unlabelled,
           'floors_required': FLOORS, 'floors_got': {k: got[k] for k in FLOORS},
           'floors_failed': fails, 'floors_pass': not fails,
           'judged': dict(collections.Counter(v.get('judged') for v in labels.values())),
           'borderline': sum(1 for v in labels.values() if v.get('borderline')),
           'tip': sum(1 for v in labels.values() if v.get('tip')),
           'judged_wrong_TWMS': {k: dict(v) for k, v in sorted(twms.items())},
           'intent_x_judged': {k: dict(v) for k, v in sorted(cross.items())},
           'floors_by_scope': {k: dict(v) for k, v in sorted(per.items())},
           'levels': dict(collections.Counter(s['level'] for s in sents.values())),
           'halves': dict(collections.Counter(s['tags'].get('half') for s in sents.values()))}
    # 1T run gate: runner_1t.py (frozen at b1c85b1) spells floor 4 'F4_bypassive_correct'; this tool
    # spells it 'F4_by_passive_correct'. The alias below is the SAME number under the runner's key,
    # added so the frozen runner need not be edited (0 calls had been made when this was found).
    rep['floors_required'] = dict(rep['floors_required'], F4_bypassive_correct=rep['floors_required']['F4_by_passive_correct'])
    rep['floors_got'] = dict(rep['floors_got'], F4_bypassive_correct=rep['floors_got']['F4_by_passive_correct'])
    safe_dump(rep, os.path.join(out_dir, 'FLOOR_CHECK_1T.json'))
    write_md(rep, out_dir)
    stop = os.path.join(out_dir, 'STOP_FLOOR.txt')
    print(json.dumps({k: rep[k] for k in ('items', 'labelled', 'floors_got', 'floors_failed',
                                          'judged', 'judged_wrong_TWMS')},
                     indent=1, sort_keys=True))
    if fails:
        open(stop, 'w', encoding='utf-8').write(json.dumps(
            {'why': 'a floor is not met; the 1T set may not be run', 'failed': fails},
            indent=1) + '\n')
        print('STOP: floors not met — %s written' % stop)
        return 2
    if os.path.exists(stop):
        os.remove(stop)
    print('FLOORS PASS')
    return 0


def write_md(rep, out_dir):
    L = ['# FLOOR_CHECK_1T — judged-label floors before the run (0 model calls)', '',
         '- items %d · labelled %d · unlabelled %d' % (rep['items'], rep['labelled'],
                                                       rep['unlabelled_items']),
         '- verdict: **%s**' % ('FLOORS PASS' if rep['floors_pass'] else 'STOP — floor not met'),
         '', '## floors', '', '| floor | required | got | ok |', '| --- | ---: | ---: | --- |']
    for k, v in sorted(rep['floors_required'].items()):
        g = rep['floors_got'][k]
        L.append('| %s | %d | %d | %s |' % (k, v, g, 'yes' if g >= v else 'NO'))
    L += ['', '## judged-wrong types (T/W/M/S)', '',
          '| scope | ' + ' | '.join(('T', 'W', 'M', 'S', '?')) + ' |',
          '| --- | ---: | ---: | ---: | ---: | ---: |']
    for sc, d in sorted(rep['judged_wrong_TWMS'].items()):
        L.append('| %s | %s |' % (sc, ' | '.join(str(d.get(t, 0)) for t in ('T', 'W', 'M', 'S', '?'))))
    L += ['', '## writer intent x judged', '', '| scope | cell | n |', '| --- | --- | ---: |']
    for sc, d in sorted(rep['intent_x_judged'].items()):
        for cell, n in sorted(d.items()):
            L.append('| %s | %s | %d |' % (sc, cell, n))
    L += ['', '## floors per scope', '', '| scope | floor | n |', '| --- | --- | ---: |']
    for sc, d in sorted(rep['floors_by_scope'].items()):
        for k, n in sorted(d.items()):
            L.append('| %s | %s | %d |' % (sc, k, n))
    open(os.path.join(out_dir, 'FLOOR_CHECK_1T.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')


# --------------------------------------------------------------------------- #
# fixture (never a measurement)
# --------------------------------------------------------------------------- #
LV = (('W1', 1, 25, 'A1'), ('W2', 26, 50, 'A2'), ('W3', 51, 75, 'B1'), ('W4', 76, 100, 'B2'))


def _sentence(n, lvl):
    """A synthetic 1T sentence: 5 SKP + 20 ACT per level, 12 EMB of which 6 are EMB2."""
    k = (n - 1) % 25 + 1                       # 1..25 inside the level
    skp = k <= 5
    emb = (not skp) and 6 <= k <= 17           # 12 ACT sentences with an embedded clause
    emb2 = emb and k <= 11                     # 6 of them carry a second embedded agent drop
    sk = ('Fixtur fx%03d sa tu kazdy den nieco robi bez konatela.' % n if skp else
          'Fixtur fx%03d Peter zamyka bránu a sused opravuje plot.' % n)
    v = ['Fixture %d reference translation one.' % n, 'Fixture %d reference translation two.' % n]
    ann = {'v': v, 'lk': ['locks'], 'alt': {'locks': ['shuts'], 'gate': ['door']},
           'voice_sk': 'passive' if skp else 'active_agent', 'agent_nom': not skp,
           'tf_gold': ('past', 'present', 'future')[n % 3], 'tense_open': False,
           'perfective_present': False}
    tags = {'nom_agent': not skp, 'agent': None if skp else 'Peter',
            'emb_agent': 'sused' if emb else None, 'emb_type': 'že' if emb else None,
            'passivizable': True, 'impersonal_or_passive': skp}
    A_ = []
    if skp:
        for i, tg in enumerate((['skp-passive'], ['skp-passive'], ['skp-passive'], ['plain']), 1):
            A_.append({'aid': 'c%d' % i, 'kind': 'C', 'intent': 'C', 'form': None, 'tags': tg,
                       'answer': 'Fixture %d correct SKP answer number %d.' % (n, i)})
        wr = (('T', ['timeframe']), ('T', ['timeframe']), ('W', ['plain']), ('M', ['plain']),
              ('S', ['plain']))
    else:
        cs = (['plain'], ['determiner'],
              ['by-passive-embedded'] if emb and k % 2 == 0 else ['by-passive'], ['aspect'])
        for i, tg in enumerate(cs, 1):
            A_.append({'aid': 'c%d' % i, 'kind': 'C', 'intent': 'C', 'form': None, 'tags': tg,
                       'answer': 'Fixture %d correct ACT answer number %d.' % (n, i)})
        wr = (('T', ['timeframe']), ('M', ['agentdrop-main']),
              ('M', ['agentdrop-embedded']) if emb else ('W', ['plain']),
              ('M', ['agentdrop-embedded']) if emb2 else ('M', ['plain']),
              ('S', ['plain']))
    for i, (intent, tg) in enumerate(wr, 1):
        A_.append({'aid': 'w%d' % i, 'kind': 'W', 'intent': intent, 'form': None, 'tags': tg,
                   'answer': 'Fixture %d wrong answer number %d (%s).' % (n, i, intent)})
    return {'sid': '1T%03d' % n, 'level': lvl, 'topic': 'selftest', 'slovak': sk,
            'kind': 'SKP' if skp else 'ACT', 'emb': emb, 'tags': tags, 'annotation': ann,
            'answers': A_}


def make_fixture(d, violate=None):
    """Writer files under <d>; `violate` injects exactly one refusal condition."""
    os.makedirs(d, exist_ok=True)
    rows = {}
    for w, lo, hi, lvl in LV:
        rows[w] = [_sentence(n, lvl) for n in range(lo, hi + 1)]
    if violate == 'counts':
        rows['W1'][0]['answers'].pop()
    elif violate == 'dupanswer':
        rows['W1'][0]['answers'][1]['answer'] = rows['W1'][0]['answers'][0]['answer']
    elif violate == 'unknowntag':
        rows['W1'][0]['answers'][0]['tags'] = ['agentless']
    elif violate == 'missingann':
        rows['W1'][0]['annotation'].pop('voice_sk')
    elif violate == 'dupslovak':
        rows['W1'][1]['slovak'] = rows['W1'][0]['slovak']
    elif violate in ('overlap', 'jaccard'):
        ex = json.load(open(os.path.join(TOFF, 'phase1n', 'existing_350.json'), encoding='utf-8'))
        s = ex[0]['slovak'] if isinstance(ex[0], dict) else ex[0]
        rows['W1'][0]['slovak'] = s if violate == 'overlap' else (s.rsplit(' ', 1)[0] + ' inokedy.')
    for w, lo, hi, lvl in LV:
        for pi, (plo, phi) in enumerate(A.PARTS, 1):
            part = rows[w][plo - 1:phi]
            safe_dump(part, os.path.join(d, 'writer_%s_part%d.json' % (w, pi)))
    print('fixture written to %s (violate=%s): %d sentences'
          % (d, violate, sum(len(v) for v in rows.values())))


def make_verdicts(d, break_floor=None):
    """Synthetic judge verdicts for the fixture, derived from judge/_private/_key.json.
    C -> correct, W -> wrong with the writer's intent as the type.  `break_floor` flips
    just enough labels of one floor's population to push it under its threshold."""
    base = os.path.dirname(d.rstrip(os.sep))
    judge_dir = os.path.join(base, 'judge')
    key = json.load(open(os.path.join(judge_dir, '_private', '_key.json'), encoding='utf-8'))
    items = {i['id']: i for i in json.load(open(os.path.join(d, 'items.json'), encoding='utf-8'))}
    sents = {int(s['sid']): s for s in
             json.load(open(os.path.join(d, 'sentences.json'), encoding='utf-8'))}
    need = {'F1': (lambda i, s: [t for t in i['tags'] if t in AGDROP], 'correct'),
            'F2': (lambda i, s: 'agentdrop-embedded' in i['tags'], 'correct'),
            'F3': (lambda i, s: 'timeframe' in i['tags'], 'correct'),
            'F4': (lambda i, s: [t for t in i['tags'] if t in BYPASS], 'wrong'),
            'F5': (lambda i, s: s['tags']['kind'] == 'SKP' and i['kind'] == 'C', 'wrong')}
    room = {'F1': 120, 'F2': 60, 'F3': 100, 'F4': 60, 'F5': 40}
    flipped, targets = 0, []
    if break_floor:
        pred, _ = need[break_floor]
        pop = [iid for iid, i in sorted(items.items())
               if pred(i, sents[int(i['sid'])])
               and ((i['kind'] == 'W') if break_floor in ('F1', 'F2', 'F3') else (i['kind'] == 'C'))]
        n_flip = len(pop) - room[break_floor] + 1
        targets = set(pop[:max(0, n_flip)])
    rng = random.Random(7)
    out = collections.defaultdict(list)
    for jid, k in sorted(key.items()):
        it = items[k['item']]
        judged = 'correct' if it['kind'] == 'C' else 'wrong'
        typ = None if judged == 'correct' else (it.get('intent') or 'M')
        if break_floor and k['item'] in targets:
            judged = 'wrong' if judged == 'correct' else 'correct'
            typ = 'M' if judged == 'wrong' else None
            flipped += 1
        if k.get('duplicate_of') and rng.random() < 0.05:          # a little judge noise
            judged = 'wrong' if judged == 'correct' else 'correct'
            typ = 'S' if judged == 'wrong' else None
        jn = int(jid[1:])
        p = 'P%d' % (min(4, (jn - 1) // 245 + 1))
        out[p].append({'jid': jid, 'judged': judged, 'type': typ,
                       'passive': ('agentless' if [t for t in it['tags'] if t in AGDROP] else
                                   'by' if [t for t in it['tags'] if t in BYPASS] else None),
                       'agent_drop': ('embedded' if 'agentdrop-embedded' in it['tags'] else
                                      'main' if 'agentdrop-main' in it['tags'] else None),
                       'dropped': '', 'tip': False, 'borderline': False, 'note': ''})
    for p, rowsp in sorted(out.items()):
        safe_dump(rowsp, os.path.join(judge_dir, 'verdicts_%s.json' % p))
    lp = os.path.join(d, 'labels.json')
    if os.path.exists(lp):
        os.remove(lp)
    print('verdicts written for %d jids (break=%s, flipped=%d)'
          % (sum(len(v) for v in out.values()), break_floor, flipped))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--make-fixture', dest='fx', nargs='?',
                    const=os.path.join(HERE, 'selftest', 'fx', 'data'))
    ap.add_argument('--make-verdicts', dest='vd', nargs='?',
                    const=os.path.join(HERE, 'selftest', 'fx', 'data'))
    ap.add_argument('--violate')
    ap.add_argument('--break-floor')
    ap.add_argument('--data-dir')
    ap.add_argument('--judge-dir')
    ap.add_argument('--out-dir')
    a = ap.parse_args()
    if a.fx:
        make_fixture(a.fx, a.violate)
    elif a.vd:
        make_verdicts(a.vd, a.break_floor)
    else:
        raise SystemExit(run(a.data_dir, a.judge_dir, a.out_dir))
