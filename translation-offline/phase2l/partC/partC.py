#!/usr/bin/env python3
"""Phase 2L Part C (0 calls): configuration table, SAFETY STOP, freeze."""
import hashlib, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P2L = os.path.dirname(HERE); sys.path.insert(0, P2L)
import score_2l as SC
data = SC.load(); cc = SC.load_cc()
CFG = [('reference-based stack (2I tonly / 2J fixed)', lambda r: r['old_acc'], False),
       ('2K SOURCE-ONLY, TIP rejected', lambda r: SC.acc_2k(r, False), False),
       ('2K SOURCE-ONLY, TIP accepted (Part A)', lambda r: SC.acc_2k(r, True), False),
       ('SOURCE-ONLY + B, TIP rejected', lambda r: SC.acc_b(r, False, cc), True),
       ('SOURCE-ONLY + B, TIP accepted', lambda r: SC.acc_b(r, True, cc), True)]
tab = {n: SC.table(data, f) for n, f, _ in CFG}
pa = lambda n, k: tab[n]['pooled']['all'][k]
assert pa(CFG[0][0], 'cov')[:2] == [893, 995] and pa(CFG[0][0], 'fa')[:2] == [43, 805]
assert pa(CFG[1][0], 'cov')[:2] == [951, 995] and pa(CFG[1][0], 'fa')[:2] == [73, 805]
cands = [n for n, _, c in CFG if c]
elig = [n for n in cands if pa(n, 'fa')[2] < 5.0]
ok = [n for n in elig if pa(n, 'cov')[2] >= 90.0]
chosen = max(elig, key=lambda n: (pa(n, 'cov')[0], -pa(n, 'fa')[0])) if ok else None
dec = {'eligible_fa_below_5': elig, 'meeting_both': ok, 'chosen': chosen, 'safety_stop': chosen is None}
L = ['# Phase 2L Part C: the configuration, and the stop', '',
     '**CLOSED-SET, IN-SAMPLE** (both Slovak sets pooled, existing judge labels, 0 extra calls). Part B failed calls keep the L3 verdict.', '',
     '| configuration | set | level | coverage | FA |', '|---|---|---|---|---|']
for n, _, _ in CFG:
    for g in SC.GROUPS:
        for lv in ('all',) + SC.LEVELS:
            if g != 'pooled' and lv != 'all':
                continue
            L.append('| %s | %s | %s | %s | %s |' % (n, g, lv, SC.fmt(tab[n][g][lv]['cov']), SC.fmt(tab[n][g][lv]['fa'])))
L += ['', 'Rule: among SOURCE-ONLY + B with TIP rejected / TIP accepted, pick the higher pooled coverage among those with pooled FA < 5 % on the point; '
      'SAFETY STOP if none has pooled coverage >= 90 % AND FA < 5 % on the point.', '',
      'FA < 5 %% on the point: %s. Both targets on the point: %s.' % (elig or 'none', ok or 'none'), '']
if chosen is None:
    L.append('**SAFETY STOP FIRED** - STOP_partC.md written; no freeze, no Czech.')
    open(os.path.join(P2L, 'STOP_partC.md'), 'w', encoding='utf-8').write(
        '# STOP part C\n\nNo SOURCE-ONLY + B configuration reaches pooled coverage >= 90 %% AND pooled FA < 5 %% on the point '
        '(closed-set, in-sample): %s. Stop here; no Czech (brief Part C).\n' % '; '.join(
            '%s: coverage %s, FA %s' % (n, SC.fmt(pa(n, 'cov')), SC.fmt(pa(n, 'fa'))) for n in cands))
else:
    tipacc = 'TIP accepted' in chosen
    for n in cands:
        c, f = pa(n, 'cov'), pa(n, 'fa')
        L.append('- %s: coverage %s (interval target %s), FA %s (interval target %s)' % (n, SC.fmt(c), 'MET' if c[3][0] >= 90 else 'missed',
                 SC.fmt(f), 'MET' if f[3][1] < 5 else 'missed'))
    L += ['', '**Chosen: %s.** Frozen as stack_2l.py (TIP_ACCEPT = %s); FROZEN_SHA_C.txt; commit in FREEZE_COMMIT_C.txt.' % (chosen, tipacc)]
    open(os.path.join(P2L, 'stack_2l.py'), 'w', encoding='utf-8').write('''#!/usr/bin/env python3
"""Phase 2L FROZEN configuration (Part C, 22.9.2026): %s.
= the 2K SOURCE-ONLY stack (stack_source.py, byte copy of phase2k/stack_source.py: AG / F4v2 / F4v3 source-side guards,
then L3 gemini-3.1-flash-lite judged against the SOURCE sentence only) + the Part B content check (content_check.py,
spec/content_check_prompt.txt) on every answer L3 accepted; MISSING -> reject; a failed check call keeps the L3 verdict.
TIP handling: L3 TIP is %s.  Chosen on the CLOSED-SET, IN-SAMPLE Slovak re-score (partC/partC.md)."""
import os, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import run_2l as R  # noqa: E402
TIP_ACCEPT = %s


def run(items, run_dir, stage, lang, ledger_path=R.LEDGER, key=None, spend_dirs=()):
    return R.run_full(items, run_dir, stage, lang, TIP_ACCEPT, ledger_path, key, spend_dirs)
''' % (chosen, 'ACCEPTED (then content-checked)' if tipacc else 'REJECTED', tipacc))
    files = ['stack_2l.py', 'run_2l.py', 'content_check.py', 'run_2k.py', 'run_2i_base.py', 'stack_source.py', 'adapter_2f.py',
             'write_guard.py', 'f4fix.py', 'spec/content_check_prompt.txt', 'spec/l3_system_sk.txt', 'spec/l3_user_sk.txt',
             'spec/l3_system_cz.txt', 'spec/l3_user_cz.txt']
    lines = ['%s  %s' % (hashlib.sha256(open(os.path.join(P2L, f), 'rb').read()).hexdigest(), f) for f in files]
    open(os.path.join(P2L, 'FROZEN_SHA_C.txt'), 'w').write(
        '# Phase 2L Part C freeze: %s (TIP_ACCEPT = %s). The 1W chain the AG guard loads (phase1w/...) is read-only and covered by SHA_before.txt.\n'
        % (chosen, tipacc) + '\n'.join(lines) + '\n')
    dec['tip_accept'] = tipacc
json.dump({'label': 'CLOSED-SET, IN-SAMPLE', 'table': tab, 'decision': dec}, open(os.path.join(HERE, 'partC.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
open(os.path.join(HERE, 'partC.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('PARTC', json.dumps(dec))
for n, _, _ in CFG:
    print('ROW', n, '| cov', SC.fmt(pa(n, 'cov')), '| FA', SC.fmt(pa(n, 'fa')))
