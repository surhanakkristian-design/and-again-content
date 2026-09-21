#!/usr/bin/env python3
"""Phase 2I: build phase2i/tonly/ (TRANSLATION-ONLY copies) from the frozen originals, write tonly.diff and
TONLY_CHANGES.md.  Originals are only READ.  Every edit must match exactly once inside its function scope."""
import os, re, subprocess, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
TOFF = os.path.dirname(HERE)
OUT = os.path.join(HERE, 'tonly')


def ml(*lines):
    return ''.join(r'(?m)^' if k == 0 else '' for k in [0]) + ''.join(r'[ \t]*' + re.escape(l) + r'\n' for l in lines)


# (original, scope marker, kind, pattern, replacement, why)
EDITS = [
    ('phase1i/lib_prev.py', 'def route(it):', 're',
     ml("if not it['lock_ok']:",
        "return 'L2', 'practised grammar span not present (lock %s)' % ' | '.join(it['locks'][:3])"), '',
     'L2 structure lock removed: route() no longer vetoes on lock_ok / reads locks'),
    ('phase1i/lib_prev.py', 'def prompt(it, variant):', 're',
     ml("if variant == 'P-B':",
        "lines.insert(3, 'Practised grammar: %s — ALREADY VERIFIED as correct in this answer; judge meaning and '",
        "'vocabulary only.' % it['topic'])"), '',
     'the L3 prompt line naming the practised grammar and declaring it ALREADY VERIFIED removed'),
    ('phase1i/pipeline_1i.py', 'def to_item(r):', 're',
     r"'wrong_why': '', 'locks': r\['locks'\],\n[ \t]*'lock_ok': r\['lock_ok'\], "
     r"'lock_released_2_1': r\['lock_released_2_1'\],\n", "'wrong_why': '',\n",
     'the checker item no longer carries locks / lock_ok / lock_released_2_1'),
    ('phase1i/pipeline_1i.py', 'ROW7_FLAGS', 're',
     r"'F2B': 1\}", "'F2B': 0}", 'F2B switched off (reads the lock span)'),
    ('phase1p/runner_1p.py', 'def build_side(', 're',
     ml("lk = []", "for x in (hy.get('lk') or []):",
        "lk += [x] if isinstance(x, str) else [y for y in x if isinstance(y, str)]"), '',
     'the one place that turns annotation lk into locks removed'),
    ('phase1p/runner_1p.py', 'def build_side(', 'lit',
     "'half': half_of(sid), 'locks': lk,", "'half': half_of(sid),", 'record no longer carries locks'),
    ('phase1p/runner_1p.py', 'def build_side(', 'lit',
     "'rows': [], 'lock_ok': True, 'lock_released_2_1': None}", "'rows': []}",
     'record no longer carries lock_ok / lock_released_2_1'),
    ('phase1p/runner_1p.py', 'def build_side(', 're',
     ml("try:", "nrm = C.base.norm",
        "r['lock_ok'] = (not lk) or any(nrm(x).strip() in nrm(r['answer']) for x in lk)",
        "if not r['lock_ok']:", "ok, tr = C.lock_equivalent_ok(P.to_item(r))", "if ok:",
        "r['lock_ok'], r['lock_released_2_1'] = True, tr", "except Exception:", "pass"), '',
     'lock_ok / lock_equivalent_ok computation removed'),
    ('phase1p/runner_1p.py', 'def decide(st, recs, ann, vm', 're',
     ml("g = R1K.guard_readouts(recs, ann, False)",
        "guards = {i: {'f8': None, 'f9': g[i]['f9']} for i in g}     # F8 CANNOT decide, F9 does not"),
     "    guards = {}\n", 'F8/F9 readouts dropped (F9 reads lk; neither decides: f8_on=f9_on=False)'),
    ('phase1p/runner_1p.py', 'def decide(st, recs, ann, vm', 'lit',
     "R1K.configure_row(stx, recs, vm, True, guards, False, False, True)",
     "R1K.configure_row(stx, recs, vm, False, guards, False, False, True)", 'LOCKTIP off (locktip=False)'),
    ('phase1p/runner_1p.py', 'def l3_eligible(', 're',
     ml("lock_rej, l3 = RL.lock_counts(st, recs)", "return lock_rej, l3"),
     "    return [], RL.l3_ids(st, False)\n", 'L3 plan without LOCKTIP / lock counts'),
]


def scope(src, marker):
    a = src.index(marker)
    m = re.search(r'\n(def |class )', src[a + len(marker):]) if marker.startswith(('def ', 'class ')) \
        else re.search(r'\n\n', src[a:])
    b = (a + len(marker) + m.start()) if marker.startswith(('def ', 'class ')) else (a + m.start())
    return a, b


def main():
    os.makedirs(OUT, exist_ok=True)
    files = sorted({e[0] for e in EDITS})
    log, diffs = [], []
    for rel in files:
        orig_path = os.path.join(TOFF, rel)
        orig = open(orig_path, encoding='utf-8').read()
        src = orig
        pins = [orig[:m.start()].count('\n') + 1 for m in re.finditer(r'__file__', orig)]
        for (f, marker, kind, pat, rep, why) in [e for e in EDITS if e[0] == rel]:
            a, b = scope(src, marker)
            body = src[a:b]
            if kind == 'lit':
                n = body.count(pat)
                if n != 1:
                    raise SystemExit('EDIT FAILED %s %s: %d hits for %r' % (rel, marker, n, pat))
                i = body.index(pat); removed = pat; new = body.replace(pat, rep)
            else:
                ms = list(re.finditer(pat, body))
                if len(ms) != 1:
                    raise SystemExit('EDIT FAILED %s %s: %d hits for %r' % (rel, marker, len(ms), pat))
                i = ms[0].start(); removed = ms[0].group(0)
                new = body[:ms[0].start()] + ms[0].expand(rep) + body[ms[0].end():]
            oi = orig.index(removed) if orig.count(removed) == 1 else orig.index(removed, orig.index(marker))
            l0 = orig[:oi].count('\n') + 1
            l1 = l0 + removed.rstrip('\n').count('\n')
            log.append({'file': rel, 'lines': '%d-%d' % (l0, l1) if l1 > l0 else '%d' % l0,
                        'removed': removed.rstrip('\n'),
                        'replacement': (ms[0].expand(rep) if kind == 're' else rep).rstrip('\n'),
                        'why': why})
            src = src[:a] + new + src[b:]
        src = src.replace('__file__', repr(orig_path))
        dst = os.path.join(OUT, os.path.basename(rel))
        open(dst, 'w', encoding='utf-8').write(src)
        log.append({'file': rel, 'lines': ','.join(map(str, pins)), 'removed': '__file__',
                    'replacement': repr(orig_path),
                    'why': 'path pin only: the copy resolves every path exactly like the original '
                           '(same data, config and sys.path dirs); no verdict effect'})
        d = subprocess.run(['diff', '-u', '--label', 'a/translation-offline/' + rel, '--label',
                            'b/translation-offline/phase2i/tonly/' + os.path.basename(rel), orig_path, dst],
                           capture_output=True, text=True).stdout
        diffs.append(d)
    open(os.path.join(HERE, 'tonly.diff'), 'w', encoding='utf-8').write(''.join(diffs))
    md = ['# TRANSLATION-ONLY stack: every change against the frozen 1W originals', '',
          'Generated by `phase2i/make_tonly.py`; the full unified diff is `phase2i/tonly.diff`. Line numbers are '
          'those of the ORIGINAL file. The originals are imported nowhere by the TRANSLATION-ONLY stack: '
          '`stack_tonly.py` loads the three copies under their original module names before anything else, '
          'every other module of the 1W chain is imported in place, unchanged. Also: `stack_tonly.py` and '
          '`run_2i.py` strip `lk` and every `lk_*` key from the annotation (top level, `hygienised`, `raw`) '
          'before the stack sees it.', '']
    for k, e in enumerate(log, 1):
        md += ['## %d. %s:%s' % (k, e['file'], e['lines']), '', 'Why: ' + e['why'], '', 'Removed / replaced text:',
               '```', e['removed'], '```', 'Replacement: ' + ('(nothing)' if not e['replacement'] else ''), '']
        if e['replacement']:
            md += ['```', e['replacement'], '```', '']
    md += ['## Why nothing else changed', '',
           '- Only three modules are copied (lib_prev, pipeline_1i, runner_1p); `tonly.diff` shows the complete '
           'difference and contains no hunk outside the edits above plus the `__file__` path pins.',
           '- Kept unchanged, imported in place: checker_1i (F3, F5, F4v2, L3 verdict map, TIP handling), '
           'runner_1k.configure_row / apply_guards, runner_1u (build_req_1u: GROUND, WORDING, VOICE_SAME, '
           'lever 2/3 lines, ARTICLE_LINE_1U; ag_map_1u; build_rows -> stack_1w.final_accept = AG v4 + v5 rs_nom '
           '+ tip_det_rule), stack_1v, reader_nom, agent_drop_v4, lever2/3, SYS text, GEN_CFG, the model.',
           '- `stack_tonly.py` sets the loaded lib_prev copy\'s `__file__` to phase1i/lib_prev.py after loading it, '
           'because checker_1i.py:32 asserts `lib_prev` lives in phase1i/ (a location check, no verdict effect); '
           '`__spec__.origin` keeps the copy path, which IMPORT_GRAPH.json reports.',
           '- TIP-as-rejection stays ON: `configure_row(..., tip_reject=True)` (last argument unchanged).',
           '- F1 and F2 flags are left True: they live only in the L2 lock branch of checker_1i.decide, which '
           'is unreachable once route() has no lock line (a mistake-pattern L2 returns before them). The '
           'poisoned-item test proves they are never reached (f1_lock_ok / f2_equivalent read it["locks"]).',
           '- phase1i/taskB/lock_fix.py still patches C.f1_lock_ok / C.lock_equivalent_ok at state build; '
           'nothing calls them in this stack (no lock read, proven by the same test).',
           '- The test suite (test_2i.py (f)) asserts the TONLY user prompt equals the FROZEN prompt minus '
           'exactly the one Practised-grammar line, with identical system text and generation config.', '']
    open(os.path.join(HERE, 'TONLY_CHANGES.md'), 'w', encoding='utf-8').write('\n'.join(md))
    print('tonly built: %d edits in %d files' % (len([e for e in log if e['removed'] != '__file__']), len(files)))


if __name__ == '__main__':
    main()
