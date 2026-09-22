#!/usr/bin/env python3
"""Phase 2L Part D - 1T's Czech gold validation (phase1t/taskB/cz_validate.py, source executed UNCHANGED, as 1V Track C
ran it) ONCE on the ASSEMBLED Czech readers of stack_2l_cz: f9 / V2 / V3 = the cz_reader modules bound into the AG
chain by cz_assemble, CK.sk_features = the f4fix.build_fixed(CK, 'cz') reader F4v2/F4v3 use.  Slovak control side =
the validator's own Slovak modules.  0 model calls.  Beside it: stored Slovak figures (1T / 1V Track C, identical)."""
import contextlib, io, json, os, sys, types
sys.dont_write_bytecode = True
PD = os.path.dirname(os.path.abspath(__file__)); HERE = os.path.dirname(PD); TOFF = os.path.dirname(HERE)
os.environ['P2I_RUN_DIR'] = os.path.join(PD, '_run'); os.makedirs(os.environ['P2I_RUN_DIR'], exist_ok=True)
sys.path.insert(0, HERE)
import stack_source_cz as SCZ  # noqa: E402
ST = SCZ.load('cz'); X = ST['CZ']; fx = ST['fx']
CKA = types.ModuleType('cz_ck_assembled_2l'); CKA.__dict__.update(vars(X['CK'])); CKA.sk_features = fx['sk_features']
VAL = os.path.join(TOFF, 'phase1t', 'taskB', 'cz_validate.py')
SRC = open(VAL, encoding='utf-8').read()
head, tail = SRC.split("\nout = []\n", 1); tail = "out = []\n" + tail
for old, new in (("        text = r[lang]\n", "        text = r[lang]\n        _swap(lang)\n"),
                 ('os.path.join(HERE, "cz_validation.json")', "OUTPATH")):
    assert tail.count(old) == 1, old
    tail = tail.replace(old, new)
ns = {'__name__': 'cz_validate_2l', '__file__': VAL}
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    exec(compile(head, VAL, 'exec'), ns)
    sk_mods = {k: ns[k] for k in ('f9', 'CK', 'V2', 'V3')}
    cz_mods = {'f9': X['f9'], 'CK': CKA, 'V2': X['V2'], 'V3': X['V3']}
    ns['_swap'] = lambda lang: ns.update(cz_mods if lang == 'cz' else sk_mods)
    ns['OUTPATH'] = os.path.join(PD, 'cz_validation_2l.json')
    exec(compile(tail, VAL, 'exec'), ns)
summary, out = ns['summary'], ns['out']
GUARDS = [('g1 F9', 'g1_f9', 'no (F9 not a SOURCE-ONLY layer)'), ('g2 F4v2', 'g2_f4v2', 'yes (F4v2/F4v3 reader)'),
          ('g3 AG v2', 'g3_v2', 'yes (AG agent reader)'), ('g3 AG v3', 'g3_v3', 'yes (AG agent reader)'),
          ('g4 voice v2', 'g4_v2', 'yes (AG voice reader)'), ('g4 voice v3', 'g4_v3', 'yes (AG voice reader)')]


def cell(s, key, lang):
    d = (s.get(key) or {}).get(lang) or {}
    return {'agree': d.get('AGREE', 0), 'conservative': d.get('CONSERVATIVE', 0),
            'error': sum(v for k, v in d.items() if k.startswith('ERROR')),
            'error_split': {k: v for k, v in d.items() if k.startswith('ERROR_')}}


tc = json.load(open(os.path.join(TOFF, 'phase1v', 'trackC', 'trackC_results.json'), encoding='utf-8'))
old = json.load(open(os.path.join(TOFF, 'phase1t', 'taskB', 'cz_validation.json'), encoding='utf-8'))
stored = {(t['guard'], t['lang'], t['run']): t for t in tc['table']}
after1v = json.load(open(os.path.join(TOFF, 'phase1v', 'trackC', 'cz_validation_after.json'), encoding='utf-8'))
rows = []
for g, key, instack in GUARDS:
    sk_st = stored[(g, 'sk', 'after')]; cz1v = stored[(g, 'cz', 'after')]
    rows.append({'guard': g, 'in_stack': instack, 'cz_assembled_2l': cell(summary, key, 'cz'),
                 'cz_1v_after_stored': {k: cz1v[k] for k in ('agree', 'conservative', 'error', 'error_split')},
                 'cz_1t_before_stored': cell(old['summary'], key, 'cz'),
                 'sk_stored_1t_1v': {k: sk_st[k] for k in ('agree', 'conservative', 'error', 'error_split')},
                 'sk_control_this_run': cell(summary, key, 'sk')})
changes = {}
for gname, key, sub in (('g1', 'g1', 'class'), ('g2', 'g2', 'class'), ('g3_v2', 'g3_v2', 'class'), ('g3_v3', 'g3_v3', 'class'),
                        ('g4_v2', 'g4', 'class_v2'), ('g4_v3', 'g4', 'class_v3')):
    lst = []
    for ra, rb in zip(after1v['rows'], out):
        ca, cb = ((ra['cz'].get(key) or {}).get(sub)), ((rb['cz'].get(key) or {}).get(sub))
        if ca != cb:
            lst.append([rb['n'], ca, cb])
    changes[gname] = lst
res = {'model_calls': 0, 'runs': 1, 'validator': 'phase1t/taskB/cz_validate.py (unchanged source, 1V Track C harness)',
       'n_rows': len(out), 'czech_side': 'assembled stack_2l_cz readers (cz_assemble + f4fix cz sk_features)',
       'sk_control_equals_stored': all(r['sk_control_this_run'] == r['sk_stored_1t_1v'] for r in rows),
       'table': rows, 'cz_class_changes_vs_1v_after': changes, 'rebound': len(__import__('cz_assemble').REBOUND),
       'summary_cz_e2e': {'rejections': summary.get('e2e_rejections'), 'crashes': summary.get('e2e_crashes')}}
json.dump(res, open(os.path.join(PD, 'gold_validation.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=str)
f = lambda c: '%d / %d / %d%s' % (c['agree'], c['conservative'], c['error'], (' %s' % c['error_split']) if c['error_split'] else '')
md = ['# Phase 2L Part D - Czech gold validation (1T validator, run ONCE, 0 model calls)', '',
      'Validator `phase1t/taskB/cz_validate.py` executed unchanged (1V Track C harness), %d gold rows. Czech side = the '
      'ASSEMBLED readers of `stack_2l_cz` (cz_reader four fixes bound into the AG chain; F4v2 reader = '
      '`f4fix.build_fixed(CK, \'cz\')`). Slovak = stored 1T/1V figures (the validator\'s Slovak control this run equals '
      'them: %s). Cells: agree / conservative / ERROR.' % (len(out), res['sk_control_equals_stored']), '',
      '| guard | in SOURCE-ONLY stack | CZ assembled (2L) | CZ 1V after (stored) | CZ 1T before (stored) | SK (stored) |',
      '|---|---|---|---|---|---|']
for r in rows:
    md.append('| %s | %s | %s | %s | %s | %s |' % (r['guard'], r['in_stack'], f(r['cz_assembled_2l']), f(r['cz_1v_after_stored']),
                                                f(r['cz_1t_before_stored']), f(r['sk_stored_1t_1v'])))
md += ['', 'Czech class changes vs 1V Track C `after` (row, 1V, 2L): ' + json.dumps(changes, ensure_ascii=False), '',
       'Note: g2 for Czech uses the 2J-fixed reader (PP shadow + non-verb list + em) that F4v2/F4v3 run; the stored '
       'Slovak g2 is the unfixed checker_1i reader. AG in the stack is AG v4 via stack_1w (reader_nom); the validator '
       'measures its V2/V3 agent and voice readers.']
open(os.path.join(PD, 'gold_validation.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')
print('\n'.join(md))
