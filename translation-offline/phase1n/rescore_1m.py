#!/usr/bin/env python3
"""Phase 1N / TASK A (label `rescore-1m`) — 0 model calls.

A1  merge taskA/out_part1.json + out_part2.json through taskA/blind_map.json, validate them,
    and tabulate the re-judge MOVEMENT (overall + by 1M form) plus the filler drift diagnostic.
A2  re-score the STORED 1M verdicts with F8 removed (deciding nothing) and the NEW labels.
A3  the two passive sub-cases (by / agentless) counted separately in the stored verdicts.

Nothing is called, nothing is written outside phase1n.  Every read goes to access_log.jsonl.
"""
import sys, os, json, collections, traceback

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import runner_1n as RM                                     # noqa: E402

RL, R1K, P, LM = RM.RL, RM.R1K, RM.P, RM.LM
TASKA = os.path.join(HERE, 'taskA')
PURPOSE = 'Phase 1N TASK A: re-judge movement + offline re-score of the CLOSED 1M verdicts'
TYPES4 = ('T', 'W', 'M', 'S')
TYPES_1M = tuple(RM.TYPES_1M)
FORMS = ('passive', 'cleft', 'reported', 'dropped')
BASE_1M = {'coverage': (547, 614), 'fa': (69, 646),
           'fa_by_type': {'T': (11, 242), 'W': (0, 89), 'M': (1, 62), 'S': (2, 82), 'V': (55, 171)}}


def rd(name, what=None):
    path = os.path.join(TASKA, name)
    if not os.path.exists(path):
        return None, 'missing file %s' % name
    try:
        d = json.load(open(path, encoding='utf-8'))
    except Exception as e:
        return None, 'unparsable %s: %s' % (name, e)
    n = len(d) if hasattr(d, '__len__') else 0
    try:
        LM._log('1n:taskA', what or ('taskA/' + name), n, PURPOSE, caller='rescore_1m.py')
    except Exception:
        pass
    return d, None


def pct(k, n):
    return P.rate(k, n)


def r(d):
    return RL._r(d)


# ===================================================================== A1 merge + validation
def a1_merge():
    blind, err = rd('blind_map.json')
    problems = {'part1': [], 'part2': []}
    if blind is None:
        return None, None, {'part1': [err], 'part2': [err]}, ['part1', 'part2'], None
    expected = {}
    for part in ('part1', 'part2'):
        inp, e = rd('in_%s.json' % part)
        if inp is None:
            expected[part] = None
            problems[part].append('input side: ' + e)
            continue
        rows = inp if isinstance(inp, list) else inp.get('items', [])
        expected[part] = [x['jid'] if isinstance(x, dict) else x for x in rows]
    merged, passive_by_jid, seen = {}, {}, {}
    for part in ('part1', 'part2'):
        out, e = rd('out_%s.json' % part)
        if out is None:
            problems[part].append(e)
            continue
        if not isinstance(out, list):
            problems[part].append('not a JSON list')
            continue
        got = []
        for row in out:
            if not isinstance(row, dict) or 'jid' not in row:
                problems[part].append('row without jid: %r' % (row,))
                continue
            jid = row['jid']
            got.append(jid)
            if jid not in blind:
                problems[part].append('unknown jid %s (not in blind_map.json)' % jid)
                continue
            if jid in seen:
                problems[part].append('duplicate jid %s (also in %s)' % (jid, seen[jid]))
            seen[jid] = part
            judged, typ = row.get('judged'), row.get('type')
            if judged not in ('correct', 'wrong'):
                problems[part].append('%s: judged=%r' % (jid, judged))
                continue
            if judged == 'wrong' and typ not in TYPES4:
                problems[part].append('%s: wrong with type=%r (not in T/W/M/S)' % (jid, typ))
                continue
            if judged == 'correct':
                typ = None
            pv = row.get('passive')
            if pv not in (None, 'by', 'agentless'):
                problems[part].append('%s: passive=%r' % (jid, pv))
                pv = None
            passive_by_jid[jid] = pv
            merged[jid] = {'judged': judged, 'type': typ, 'note': row.get('note'),
                           'passive': pv, 'part': part}
        if expected.get(part):
            miss = [j for j in expected[part] if j not in got]
            if miss:
                problems[part].append('missing jids (%d): %s' % (len(miss), ', '.join(miss[:20])))
    # jids of blind_map covered by neither part
    uncovered = [j for j in blind if j not in merged]
    if uncovered:
        for part in ('part1', 'part2'):
            owed = [j for j in uncovered if expected.get(part) and j in expected[part]]
            if owed:
                problems[part].append('uncovered jids (%d)' % len(owed))
        orphan = [j for j in uncovered
                  if not any(expected.get(p) and j in expected[p] for p in ('part1', 'part2'))]
        if orphan:
            problems['part1'].append('jids in blind_map but in no input part: %d' % len(orphan))
    bad = sorted(p for p in ('part1', 'part2') if problems[p])
    return blind, merged, problems, bad, passive_by_jid


def a1_movement(blind, merged):
    rows = []
    for jid, meta in blind.items():
        if jid not in merged:
            continue
        m = merged[jid]
        rows.append({'jid': jid, 'item_id': meta['item_id'], 'sid': meta.get('sid'),
                     'intent': meta.get('intent'), 'form': meta.get('form'),
                     'filler': bool(meta.get('filler')), 'old_judged': meta['old_judged'],
                     'old_type': meta.get('old_type'), 'new_judged': m['judged'],
                     'new_type': m['type'], 'note': m.get('note'), 'passive': m.get('passive')})
    rows.sort(key=lambda x: x['jid'])
    real = [x for x in rows if not x['filler']]
    fill = [x for x in rows if x['filler']]

    def cells(items):
        c = {'n': len(items), 'wrong_to_correct': [], 'wrong_to_wrong': [],
             'correct_to_wrong': [], 'correct_to_correct': []}
        for x in items:
            key = ('%s_to_%s' % (x['old_judged'], x['new_judged'])).replace('correct_to_correct',
                                                                           'correct_to_correct')
            c.setdefault(key, []).append(x)
        return c

    def summarise(items):
        c = cells(items)
        out = {'n': len(items)}
        for k in ('wrong_to_correct', 'wrong_to_wrong', 'correct_to_wrong', 'correct_to_correct'):
            out[k] = len(c.get(k, []))
        old_w = out['wrong_to_correct'] + out['wrong_to_wrong']
        old_c = out['correct_to_wrong'] + out['correct_to_correct']
        out['old_wrong'] = old_w
        out['old_correct'] = old_c
        out['flip_rate_old_wrong_to_correct'] = pct(out['wrong_to_correct'], old_w)
        out['flip_rate_old_correct_to_wrong'] = pct(out['correct_to_wrong'], old_c)
        out['new_wrong'] = out['wrong_to_wrong'] + out['correct_to_wrong']
        out['new_type_hist'] = dict(collections.Counter(
            x['new_type'] or '?' for x in items if x['new_judged'] == 'wrong'))
        return out, c

    overall, ocells = summarise(real)
    by_form = {}
    for f in FORMS:
        sub = [x for x in real if x['form'] == f]
        by_form[f], _ = summarise(sub)
    other = [x for x in real if x['form'] not in FORMS]
    if other:
        by_form['(other/none)'], _ = summarise(other)

    agree = [x for x in fill if x['old_judged'] == x['new_judged']]
    filler = {'n': len(fill), 'agreements': len(agree),
              'agreement': pct(len(agree), len(fill)),
              'disagreements': [{'jid': x['jid'], 'item_id': x['item_id'],
                                 'old': x['old_judged'], 'new': x['new_judged'],
                                 'new_type': x['new_type'], 'note': x['note']}
                                for x in fill if x['old_judged'] != x['new_judged']],
              'old_correct_new_wrong': sum(1 for x in fill if x['old_judged'] == 'correct'
                                           and x['new_judged'] == 'wrong'),
              'old_wrong_new_correct': sum(1 for x in fill if x['old_judged'] == 'wrong'
                                           and x['new_judged'] == 'correct')}
    lists = {k: [{'jid': x['jid'], 'item_id': x['item_id'], 'form': x['form'],
                  'intent': x['intent'], 'old_type': x['old_type'], 'new_type': x['new_type'],
                  'passive': x['passive'], 'note': x['note']} for x in v]
             for k, v in ocells.items() if isinstance(v, list)}
    return rows, real, fill, overall, by_form, filler, lists


# ===================================================================== A2 / A3 re-score
def build_stored():
    os.environ.setdefault('PHASE1J_FINAL', '1')
    os.environ['PHASE1K_OPEN_FRESH'] = '1'
    st, recs, ann, by, info = RM.fresh1m_side(PURPOSE)
    labels_1m, controls, lmeta = RM.fresh1m_labels(PURPOSE)
    for rec in recs:
        if rec['item_id'] in labels_1m:
            rec['judged'], rec['wrong_type'] = labels_1m[rec['item_id']]
    lock_rej, l3 = RL.lock_counts(st, recs)
    hmap = RL.hashes_for(st, recs, l3, RM.DEV_PROMPT)
    rep, ver, failed, _cl = RL.ledger_state()
    vm = {i: ver[h] for i, h in hmap.items() if h in ver}
    return st, recs, ann, by, info, labels_1m, controls, lmeta, lock_rej, l3, vm


def score(st, recs, ann, vm, f8_mod, f8_on, labels, types):
    RM.select_f8(f8_mod) if f8_mod else None
    g = R1K.guard_readouts(recs, ann, False)
    res = R1K.configure_row(st, recs, vm, True, g, f8_on, False, True)
    RL.TYPES = tuple(types)
    m = RL.col_metrics(recs, res, labels)
    return g, res, m


def main():
    out = {'phase': '1N', 'task': 'A', 'label': 'rescore-1m', 'model_calls': 0}

    # ---------------- A1
    blind, merged, problems, bad, passive_by_jid = a1_merge()
    out['bad_parts'] = bad
    out['judge_file_problems'] = {k: v for k, v in problems.items() if v}
    if bad:
        out['stopped'] = 'judge file(s) BAD: %s' % ', '.join(bad)
        json.dump(out, open(os.path.join(HERE, 'rescore_1m.json'), 'w'), indent=1,
                  ensure_ascii=False)
        open(os.path.join(HERE, 'TASKA_REJUDGE.md'), 'w', encoding='utf-8').write(
            '# Phase 1N — TASK A re-judge (STOPPED)\n\nBAD judge parts: %s\n\n```\n%s\n```\n'
            % (', '.join(bad), json.dumps(problems, indent=1, ensure_ascii=False)))
        print('STOP bad_parts=%s' % bad)
        return 0

    rows, real, fill, overall, by_form, filler, lists = a1_movement(blind, merged)
    out['a1'] = {'jids_in_blind_map': len(blind), 'jids_merged': len(merged),
                 'non_filler': len(real), 'fillers': len(fill),
                 'movement_overall': overall, 'movement_by_form': by_form,
                 'filler_agreement': filler, 'movement_lists': lists}

    # ---------------- A2 / A3
    st, recs, ann, by, info, labels_1m, controls, lmeta, lock_rej, l3, vm = build_stored()
    id_of = {x['jid']: x['item_id'] for x in rows}
    new_by_item = {}
    for x in rows:
        new_by_item[x['item_id']] = (x['new_judged'], x['new_type'])
    labels_new = dict(labels_1m)
    applied, unknown = 0, []
    for iid, lab in new_by_item.items():
        if iid in by:
            labels_new[iid] = lab
            applied += 1
        else:
            unknown.append(iid)

    # (a) faithful 1M reproduction: F8v2 decides, OLD labels, 1M type set
    g_v2, res_1m, m_1m = score(st, recs, ann, vm, 'f8v2', True, labels_1m, TYPES_1M)
    repro = {'coverage': (m_1m['coverage']['k'], m_1m['coverage']['n']),
             'fa': (m_1m['fa']['k'], m_1m['fa']['n']),
             'fa_by_type': {t: (m_1m['fa_by_type'][t]['k'], m_1m['fa_by_type'][t]['n'])
                            for t in TYPES_1M}}
    faithful = (repro['coverage'] == BASE_1M['coverage'] and repro['fa'] == BASE_1M['fa']
                and all(repro['fa_by_type'].get(t) == v for t, v in BASE_1M['fa_by_type'].items()))

    # (b) F8 removed, OLD labels (decomposition step)
    _g0, res_head, m_nof8_old = score(st, recs, ann, vm, None, False, labels_1m, TYPES_1M)
    # (c) F8 removed, NEW labels  <- the headline re-score
    RL.TYPES = TYPES4
    m_new = RL.col_metrics(recs, res_head, labels_new)

    # F8 shadows under the NEW labels
    ids_sh = [i for i in by if i in labels_new and i in res_head]
    lab_sh = {i: labels_new[i] for i in ids_sh}
    shadows = {}
    for mod, key in (('f8', 'F8v1'), ('f8v2', 'F8v2')):
        g, res_on, m_on = score(st, recs, ann, vm, mod, True, labels_new, TYPES4)
        shadows[key] = RM.f8_shadow(ids_sh, lab_sh, g, res_head, res_on, m_on, mod)
    RM.select_f8('f8v2')

    out['a2'] = {
        'what_this_is': 'A RE-SCORE OF A CLOSED SET — ranking evidence, not a measurement.',
        'caveat_stored_L3': 'The stored L3 verdicts were produced by the OLD 1M prompt, which '
                            'still carried the voice line. Only the LABELS and the F8 switch '
                            'change here; not one model verdict was re-taken.',
        'reproduction_of_1M': {'expected': BASE_1M, 'observed': repro, 'faithful': faithful},
        'baseline_1M': {'coverage': r(m_1m['coverage']), 'fa': r(m_1m['fa']),
                        'fa_by_type': {t: r(m_1m['fa_by_type'][t]) for t in TYPES_1M},
                        'fa_by_layer': {k: r(v) for k, v in m_1m['fa_by_layer'].items()},
                        'fr_by_layer': {k: r(v) for k, v in m_1m['fr_by_layer'].items()}},
        'f8_removed_old_labels': {'coverage': r(m_nof8_old['coverage']), 'fa': r(m_nof8_old['fa']),
                                  'fa_by_type': {t: r(m_nof8_old['fa_by_type'][t])
                                                 for t in TYPES_1M}},
        'rescore_f8_removed_new_labels': {
            'coverage': r(m_new['coverage']), 'fa': r(m_new['fa']),
            'fa_by_type': {t: r(m_new['fa_by_type'][t]) for t in TYPES4},
            'fa_by_layer': {k: r(v) for k, v in m_new['fa_by_layer'].items()},
            'fr_by_layer': {k: r(v) for k, v in m_new['fr_by_layer'].items()},
            'n_items': m_new['n_items']},
        'labels_replaced': applied, 'labels_not_in_side': unknown,
        'stored_verdicts_reused': len(vm), 'l3_eligible': len(l3),
        'lock_rejections_BASE': len(lock_rej),
        'f8_shadows_under_new_labels': shadows}
    out['rescore_coverage'] = r(m_new['coverage'])
    out['rescore_fa'] = r(m_new['fa'])

    # ---------------- A3 passive sub-cases
    tag_of_item = {}
    for x in rows:
        if x['passive'] in ('by', 'agentless'):
            tag_of_item[x['item_id']] = x['passive']
    a3 = {'source_of_the_tag': 'the judge rows of taskA/out_part*.json (re-judged items only)',
          'rejects_nothing': 'counts only; no item is rejected because of a passive tag'}
    for tag in ('by', 'agentless'):
        ids = sorted(i for i, t in tag_of_item.items() if t == tag and i in by)
        cell = {'n': len(ids),
                'judged_correct': sum(1 for i in ids if labels_new[i][0] == 'correct'),
                'judged_wrong': sum(1 for i in ids if labels_new[i][0] == 'wrong'),
                'new_type_hist': dict(collections.Counter(
                    labels_new[i][1] or '?' for i in ids if labels_new[i][0] == 'wrong')),
                'stored_1M_config_f8v2': RM.passive_cell(ids, res_1m),
                'rescore_config_f8_removed': RM.passive_cell(ids, res_head),
                'ids': ids}
        for key, res in (('stored_1M_config_f8v2', res_1m), ('rescore_config_f8_removed', res_head)):
            for grp, sel_ids in (('judged_correct', [i for i in ids if labels_new[i][0] == 'correct']),
                                 ('judged_wrong', [i for i in ids if labels_new[i][0] == 'wrong'])):
                cell[key][grp + '_split'] = {
                    'n': len(sel_ids),
                    'accepted': sum(1 for i in sel_ids if res[i]['accepted']),
                    'rejected_by_layer': dict(collections.Counter(
                        str(res[i]['layer']) for i in sel_ids if not res[i]['accepted']))}
        if tag == 'agentless':
            for key, res in (('stored_1M_config_f8v2', res_1m),
                             ('rescore_config_f8_removed', res_head)):
                tipm = [i for i in ids if res[i].get('model_tip')]
                tipa = [i for i in ids if res[i].get('tip') or res[i].get('model_tip')]
                cell[key]['tip_share_model_TIP'] = pct(len(tipm), len(ids))
                cell[key]['tip_share_any_TIP'] = pct(len(tipa), len(ids))
                cell[key]['tip_ids_model'] = tipm
        a3[tag] = cell
    a3['items_tagged_but_not_in_side'] = sorted(i for i in tag_of_item if i not in by)
    out['a3'] = a3

    json.dump(out, open(os.path.join(HERE, 'rescore_1m.json'), 'w'), indent=1, ensure_ascii=False)
    write_md(out, overall, by_form, filler, lists, real, fill, m_1m, m_nof8_old, m_new,
             shadows, a3, repro, faithful, applied, unknown, len(vm))
    print('OK  bad_parts=[]  coverage %s  FA %s' % (out['rescore_coverage'], out['rescore_fa']))
    print('1M reproduced faithfully: %s' % faithful)
    return 0


# ===================================================================== markdown
def tbl(head, lines):
    return ['| ' + ' | '.join(head) + ' |',
            '|' + '|'.join(['---'] * len(head)) + '|'] + \
           ['| ' + ' | '.join(str(c) for c in ln) + ' |' for ln in lines]


def write_md(out, overall, by_form, filler, lists, real, fill, m_1m, m_nof8_old, m_new,
             shadows, a3, repro, faithful, applied, unknown, n_vm):
    t = ['# Phase 1N — TASK A: the re-judge movement (label `rescore-1m`)', '',
         '0 model calls. Sources: `taskA/blind_map.json`, `taskA/out_part1.json`, '
         '`taskA/out_part2.json` (merged by `rescore_1m.py`; every read is in `access_log.jsonl`).',
         '', '**Judge files: both OK** — parsable, every jid known, no jid missing, no wrong '
         'without a type in T/W/M/S. `bad_parts = []`.', '',
         '## 1. Movement of the %d non-filler items' % len(real), '']
    t += tbl(['cell', 'n'],
             [['old wrong -> new correct', overall['wrong_to_correct']],
              ['old wrong -> still wrong', overall['wrong_to_wrong']],
              ['old correct -> new wrong', overall['correct_to_wrong']],
              ['old correct -> still correct', overall['correct_to_correct']],
              ['**old wrong (total)**', overall['old_wrong']],
              ['**old correct (total)**', overall['old_correct']],
              ['**new wrong (total)**', overall['new_wrong']]])
    t += ['', 'Rehabilitation rate of the old-wrong items: %s.' % r(overall['flip_rate_old_wrong_to_correct']),
          'Opposite direction, old-correct items now called wrong: %s.'
          % r(overall['flip_rate_old_correct_to_wrong']),
          '', 'New wrong-type histogram (non-fillers): `%s`.' % json.dumps(overall['new_type_hist'], sort_keys=True),
          '', '## 2. The same, by 1M form', '']
    t += tbl(['form', 'n', 'w->c', 'w->w', 'c->w', 'c->c', 'old-wrong rehabilitated'],
             [[f, d['n'], d['wrong_to_correct'], d['wrong_to_wrong'], d['correct_to_wrong'],
               d['correct_to_correct'], r(d['flip_rate_old_wrong_to_correct'])]
              for f, d in by_form.items()])
    t += ['', '## 3. Old wrong -> STILL wrong, item by item',
          '', 'The reason is the judge\'s note, i.e. the ground other than voice on which the item '
          'stays wrong.', '']
    ww = lists.get('wrong_to_wrong', [])
    t += tbl(['jid', 'item_id', 'form', 'old type', 'new type', 'passive', 'reason (judge note)'],
             [[x['jid'], x['item_id'], x['form'], x['old_type'] or '-', x['new_type'] or '-',
               x['passive'] or '-', (x['note'] or '-').replace('|', '/')] for x in ww])
    t += ['', '## 4. The other direction: old correct -> new wrong', '']
    cw = lists.get('correct_to_wrong', [])
    t += (tbl(['jid', 'item_id', 'form', 'new type', 'passive', 'judge note'],
              [[x['jid'], x['item_id'], x['form'], x['new_type'] or '-', x['passive'] or '-',
                (x['note'] or '-').replace('|', '/')] for x in cw])
          if cw else ['_none._'])
    t += ['', '## 5. Old wrong -> new correct (the released items)', '']
    wc = lists.get('wrong_to_correct', [])
    t += (tbl(['jid', 'item_id', 'form', 'old type', 'passive'],
              [[x['jid'], x['item_id'], x['form'], x['old_type'] or '-', x['passive'] or '-']
               for x in wc]) if wc else ['_none._'])
    t += ['', '## 6. Filler agreement — the judge-drift diagnostic', '',
          '%d fillers, re-judged blind alongside the real items. Old versus new verdict:' % filler['n'], '']
    t += tbl(['cell', 'value'],
             [['agreements', '%d / %d' % (filler['agreements'], filler['n'])],
              ['**agreement, exact 95 % CP**', r(filler['agreement'])],
              ['old correct -> new wrong', filler['old_correct_new_wrong']],
              ['old wrong -> new correct', filler['old_wrong_new_correct']]])
    if filler['disagreements']:
        t += ['', 'The disagreeing fillers:', '']
        t += tbl(['jid', 'item_id', 'old', 'new', 'new type', 'note'],
                 [[d['jid'], d['item_id'], d['old'], d['new'], d['new_type'] or '-',
                   (d['note'] or '-').replace('|', '/')] for d in filler['disagreements']])
    t += ['', 'Read it as drift of the judging instrument, not as a result: the fillers were meant '
          'to be re-confirmed, so every disagreement here is noise that also sits inside the '
          'movement table above.', '']
    open(os.path.join(HERE, 'TASKA_REJUDGE.md'), 'w', encoding='utf-8').write('\n'.join(t) + '\n')

    a = out['a2']
    s = ['# Phase 1N — re-score of the CLOSED Phase 1M verdicts (label `rescore-1m`)', '',
         '> **This is a RE-SCORE of a closed set: ranking evidence, not a measurement.** '
         'No model was called (0 calls). The 1M pipeline was replayed offline over the stored '
         'verdicts with two changes: **F8 decides nothing** and the **new labels** from the '
         're-judge (1M labels, replaced wherever an item was re-judged).', '',
         '> **Caveat that limits every number below:** the stored L3 verdicts were produced by the '
         '**OLD 1M prompt, which still carried the voice line**. The re-score therefore shows what '
         'the 1M *stack* would have scored under the corrected labels — not what a run under the '
         '1N prompt will score. A fresh measurement is still owed.', '',
         '## 1. Faithfulness of the replay', '',
         '`--f8 f8v2` + old labels reproduces 1M exactly: **%s** '
         '(coverage %s, FA %s, by type %s).' % (
             'YES' if faithful else 'NO', '%d/%d' % repro['coverage'], '%d/%d' % repro['fa'],
             json.dumps({k: '%d/%d' % v for k, v in repro['fa_by_type'].items()}, sort_keys=True)),
         '', '%d stored verdicts reused, %d labels replaced by the re-judge%s.' % (
             n_vm, applied, (', %d re-judged ids not in the side' % len(unknown)) if unknown else ''),
         '', '## 2. Headline, side by side', '']
    s += tbl(['cell', '1M as measured (F8v2 decides, old labels)',
              'F8 removed, old labels', '**re-score: F8 removed + new labels**'],
             [['coverage', r(m_1m['coverage']), r(m_nof8_old['coverage']), '**%s**' % r(m_new['coverage'])],
              ['FA', r(m_1m['fa']), r(m_nof8_old['fa']), '**%s**' % r(m_new['fa'])]])
    s += ['', '## 3. FA by type, exact 95 % Clopper-Pearson', '']
    s += tbl(['type', '1M as measured', 're-score (F8 removed + new labels)'],
             [[ty, r(m_1m['fa_by_type'][ty]) if ty in m_1m['fa_by_type'] else '-',
               r(m_new['fa_by_type'][ty]) if ty in m_new['fa_by_type'] else '— (type retired)']
              for ty in ('T', 'W', 'M', 'S', 'V')])
    s += ['', 'Type **V** is retired in 1N: the voice class no longer exists, its items carry a '
          'T/W/M/S type or are judged correct.', '',
          '## 4. FA and false rejections by layer', '']
    layers = sorted(set(list(m_1m['fa_by_layer']) + list(m_new['fa_by_layer'])
                        + list(m_1m['fr_by_layer']) + list(m_new['fr_by_layer'])), key=str)
    s += tbl(['layer', 'FA 1M', 'FA re-score', 'false rejections 1M', 'false rejections re-score'],
             [[L, r(m_1m['fa_by_layer'][L]) if L in m_1m['fa_by_layer'] else '0',
               r(m_new['fa_by_layer'][L]) if L in m_new['fa_by_layer'] else '0',
               r(m_1m['fr_by_layer'][L]) if L in m_1m['fr_by_layer'] else '0',
               r(m_new['fr_by_layer'][L]) if L in m_new['fr_by_layer'] else '0'] for L in layers])
    s += ['', '## 5. What the removed F8 would have done under the new labels', '',
          'Both modules are read out and decide nothing. COST = judged-correct items the module '
          'would reject; CATCHES = judged-wrong items it would reject; UNIQUE = of those, the ones '
          'the headline stack (every other layer incl. L3) accepts.', '']
    s += tbl(['module', 'reject readouts', 'COST (correct rejected)', 'CATCHES (wrong rejected)',
              'UNIQUE', 'headline under it: coverage', 'FA'],
             [[k, v['reject_readouts'], v['COST_judged_correct_it_would_reject'],
               v['CATCHES_judged_wrong_it_would_reject'], v['UNIQUE_caught_by_no_other_layer'],
               r(v['headline_under_this_guard']['coverage']), r(v['headline_under_this_guard']['fa'])]
              for k, v in shadows.items()])
    for k, v in shadows.items():
        s += ['', '* **%s** unique catches: %s' % (k, ', '.join(v['unique_ids']) or 'none'),
              '  cost ids: %s' % (', '.join(v['cost_ids'][:40]) or 'none')]
    s += ['', '## 6. The two passive sub-cases, counted separately', '',
          'Tag source: the judge\'s `passive` key on the re-judged items. **Nothing is rejected '
          'because of the tag** — this is a count.', '']
    for tag in ('by', 'agentless'):
        c = a3[tag]
        s += ['### (%s) passive *%s*' % ('i' if tag == 'by' else 'ii', tag), '',
              '%d items — judged correct %d, judged wrong %d %s.' % (
                  c['n'], c['judged_correct'], c['judged_wrong'],
                  json.dumps(c['new_type_hist'], sort_keys=True) if c['new_type_hist'] else ''), '']
        s += tbl(['stored verdicts under', 'accepted', 'accept rate', 'rejected', 'rejected by layer'],
                 [[key.replace('_', ' '), c[key]['accepted'], r(c[key]['accept_rate']),
                   c[key]['rejected'], json.dumps(c[key]['rejected_by_layer'], sort_keys=True)]
                  for key in ('stored_1M_config_f8v2', 'rescore_config_f8_removed')])
        s += ['', 'Split by the new label:', '']
        s += tbl(['config', 'group', 'n', 'accepted', 'rejected by layer'],
                 [[key.replace('_', ' '), grp, c[key][grp + '_split']['n'],
                   c[key][grp + '_split']['accepted'],
                   json.dumps(c[key][grp + '_split']['rejected_by_layer'], sort_keys=True)]
                  for key in ('stored_1M_config_f8v2', 'rescore_config_f8_removed')
                  for grp in ('judged_correct', 'judged_wrong')])
        if tag == 'agentless':
            s += ['', 'Share the M machinery already surfaces as a TIP:', '']
            s += tbl(['config', 'model TIP', 'any TIP'],
                     [[key.replace('_', ' '), r(c[key]['tip_share_model_TIP']),
                       r(c[key]['tip_share_any_TIP'])]
                      for key in ('stored_1M_config_f8v2', 'rescore_config_f8_removed')])
        s += ['']
    s += ['## 7. How to read this', '',
          '* The re-score ranks configurations on a closed set; it cannot decide a target.',
          '* Every L3 verdict inside it was taken under the old, voice-carrying prompt.',
          '* The label change alone moves FA; the F8 removal alone moves it the other way. '
          'Column 3 of section 2 isolates the label effect, column 4 the joint effect.', '']
    open(os.path.join(HERE, 'RESCORE_1M.md'), 'w', encoding='utf-8').write('\n'.join(s) + '\n')


if __name__ == '__main__':
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception:
        traceback.print_exc()
        sys.exit(2)
