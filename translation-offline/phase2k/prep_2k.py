#!/usr/bin/env python3
"""Phase 2K S1 (0 model calls): SOURCE-ONLY guards + prepare over 2I's 900 and 2J's 900 items -> how many reach L3,
guard agreement with the 2J stack's own results on the same items, the AG reference probe (reference = PoisonVal),
and the removed-layer grep table (analysis/REMOVED_LAYERS.md)."""
import collections, json, os, re, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
TOFF = os.path.dirname(HERE)
os.environ['P2I_RUN_DIR'] = os.path.join(HERE, '_prep')
sys.path.insert(0, HERE)
import run_2k as K
S = K.S
SETS = {'2I': ('phase2i/set/items.jsonl', 'phase2i/judge/labels.jsonl', 'phase2j/run_S2c/results.jsonl'),
        '2J': ('phase2j/partD/set/items.jsonl', 'phase2j/partD/judge/labels.jsonl', 'phase2j/partD/run/results.jsonl')}
SITES = [
    ('L1 exact-reference accept: route', 'phase2j/tonly/lib_prev.py', r"def route|'L1'"),
    ('L1 accept inside decide', 'phase1i/checker_1i.py', r"lay, why = base\.route\(it\)|if lay == 'L1'"),
    ('F3 deletion vs reference', 'phase1i/checker_1i.py', r"def f3_deletion|if flags\.get\('F3'\)"),
    ('F5 adjunct deletion / subsequence vs reference', 'phase1i/checker_1i.py', r"def f5_adjunct_deletion|if flags\.get\('F5'\)|def _subseq_positions"),
    ('L2 mistake / F1 / F2 (locks from lk)', 'phase1i/checker_1i.py', r"def f1_lock_ok|def f2_equivalent|def f2_tip|if flags\.get\('F1'\)|flags\.get\('F2'\)|it\['step'\] == 'mistake'"),
    ('F2B (reads alt en_span_tokens)', 'phase1i/checker_1i.py', r"def f2_boundary_violation|if flags\.get\('F2B'\)|def en_span_tokens"),
    ('ROW7 flags (F1,F2,F3,F4v2,F5,F2B)', 'phase2j/tonly/pipeline_1i.py', r"ROW7_FLAGS"),
    ('reference / refs into records', 'phase2j/tonly/runner_1p.py', r"'reference'|\['v'\]|'refs'|\['alt'\]|\['en'\]"),
    ('reference into checker item', 'phase2j/tonly/pipeline_1i.py', r"'reference'|'refs'|\['alt'\]"),
    ('P-FROZEN L3 prompt: SYS + Reference English line', 'phase2j/tonly/lib_prev.py', r"Reference English|^SYS = |the reference"),
    ('GROUND_LINE / WORDING_LINE', 'phase2j/tonly/pipeline_1i.py', r"GROUND_LINE =|WORDING_LINE =|GENDER_TMPL ="),
    ('LOCKTIP', 'phase1k/runner_1k.py', r"def locktip_decide"),
    ('L1 offline checker (chk)', 'phase1n/runner_1l.py', r"def compute_chk"),
    ('lever 3 prompt line (reads v[0])', 'phase1p/lever3.py', r"v\[0\]|reference"),
    ('lever 2 prompt line', 'phase1p/lever2.py', r"v\[0\]|reference"),
    ('AG gets r[reference]; build_rows / final_accept', 'phase1w/a4/run/runner_1u.py', r"r\['reference'\]|def build_rows|final_accept\("),
    ('AGv5 refsubj rs_nom + TIPdet', 'phase1v/trackA_loop/stack_1v.py', r"def ref_subject_heads|def refsubj|r = refsubj\(|def tip_det_rule|def final_accept|refsubj\(row|tip_det_rule\(row"),
    ('AG v4 reference reads', 'phase1u/taskA/agent_drop_v4.py', r"reference|\['v'\]|'alt'"),
    ('AG v3 reference reads', 'phase1t/taskA/agent_drop_v3.py', r"reference|\['v'\]"),
    ('AG v2 reference reads', 'phase1s/taskC/agent_drop_v2.py', r"reference|\['v'\]"),
    ('reader_nom', 'phase1w/reader_nom.py', r"reference|\['v'\]|'alt'|\['en'\]"),
    ('F4v3 (guards_c)', 'phase1i/taskC/guards_c.py', r"def f4v3_subject_mismatch|def sk_features_v3|reference"),
    ('F4v2 (checker_1i)', 'phase1i/checker_1i.py', r"def f4v2_subject_mismatch|def sk_features\(|def en_subjects"),
    ('F9 readout (lk)', 'phase1n/f9.py', r"\['lk'\]"),
    ('2F adapter', 'phase2j/adapter_2f.py', r"'v'|'alt'|'en'|'lk'"),
]


def jl(p):
    return [json.loads(l) for l in open(os.path.join(TOFF, p), encoding='utf-8') if l.strip()]


def grep_table():
    L = ['# Phase 2K - every reference-reading layer of the 2J stack (grep, line numbers as of 21.9.2026)', '',
         'Removed from the SOURCE-ONLY verdict path unless marked KEPT. stack_source.py never imports the verdict code',
         'below (it calls only AG and the fixed F4v2/F4v3 functions), so every reference read listed here is outside the path.', '',
         '| layer | file:line | text |', '|---|---|---|']
    for lab, f, pat in SITES:
        p = os.path.join(TOFF, f)
        if not os.path.exists(p):
            L.append('| %s | %s | (file missing) |' % (lab, f)); continue
        n = 0
        for i, ln in enumerate(open(p, encoding='utf-8'), 1):
            if re.search(pat, ln):
                n += 1
                if n <= 25:
                    L.append('| %s | %s:%d | `%s` |' % (lab, f, i, ln.strip()[:110].replace('|', '/').replace('`', "'")))
        if n > 25:
            L.append('| %s | %s | ... %d more hits |' % (lab, f, n - 25))
        if n == 0:
            L.append('| %s | %s | 0 hits |' % (lab, f))
    open(os.path.join(HERE, 'analysis', 'REMOVED_LAYERS_GREP.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')


def main():
    os.makedirs(os.path.join(HERE, 'analysis'), exist_ok=True)
    grep_table()
    res = {'ag_how': None}
    for name, (ip, lp, rp) in SETS.items():
        items = jl(ip)
        labels = jl(lp)
        clean = [K.clean_item(it, 'sk') for it in items]
        h0 = len(S.HITS)
        g = S.guards(clean, 'sk')
        hits_real = len(S.HITS) - h0
        reqs = S.prepare(clean, 'sk')
        keys = {K.B.req_key(q) for q in reqs.values()}
        old = {r['jid']: r for r in jl(rp)}
        lab = {it['jid']: it.get('judge_label') for it in items}
        lay = collections.Counter(str(v['guard_layer']) for v in g.values())
        ag_dis = [{'jid': j, 'ours': g[j]['ag_fired'], 'twoJ': bool(old[j].get('ag_fired')), 'label': lab[j],
                   'ours_reason': g[j]['ag_reason'], 'twoJ_reason': old[j].get('ag_reason')}
                  for j in g if bool(g[j]['ag_fired']) != bool(old[j].get('ag_fired'))]
        f4x = collections.Counter('2J %s / ours %s' % (old[j]['layer'] if old[j]['layer'] in ('F4v2', 'F4v3') else 'other',
                                                       g[j]['guard_layer'] if g[j]['guard_layer'] in ('F4v2', 'F4v3') else 'other')
                                  for j in g)
        h1 = len(S.HITS)
        probe = S.guards(clean, 'sk', reference=S.PoisonVal())
        probe_hits = S.HITS[h1:]
        res[name] = {
            'items': len(items), 'labels_file_rows': len(labels), 'label_counts': dict(collections.Counter(lab.values())),
            'guard_layers': dict(lay), 'reach_l3': len(reqs), 'unique_requests': len(keys),
            'guard_rejected_by_label': dict(collections.Counter('%s/%s' % (g[j]['guard_layer'], lab[j]) for j in g if g[j]['guard_layer'])),
            'ag_errors': sum(1 for v in g.values() if v['ag_error']), 'ag_ref_read_attempts': sum(v['ag_ref_read'] for v in g.values()),
            'f4_errors': sum(1 for v in g.values() if v['f4_error']), 'poison_hits_real_path': hits_real,
            'ag_agree_with_2J_stack': len(g) - len(ag_dis), 'ag_disagree': ag_dis,
            'f4_crosstab': dict(f4x), 'twoJ_layers': dict(collections.Counter(old[j]['layer'] for j in g)),
            'probe_reference_poison': {'reads': sum(v['ag_ref_read'] for v in probe.values()),
                                       'errors': dict(collections.Counter((v['ag_error'] or '')[:80] for v in probe.values() if v['ag_error'])),
                                       'verdict_changes_vs_empty_ref': sum(1 for j in g if probe[j]['ag_fired'] != g[j]['ag_fired']),
                                       'first_hits': probe_hits[:3]},
            'paths': {'items': ip, 'labels': lp, 'reference_based_results_2J_stack': rp}}
        res['ag_how'] = S.ST.get('ag_how')
    json.dump(res, open(os.path.join(HERE, 'analysis', 's1_prep.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=str)
    for name in SETS:
        r = res[name]
        print(name, {k: r[k] for k in ('items', 'label_counts', 'guard_layers', 'reach_l3', 'unique_requests', 'guard_rejected_by_label',
                                     'ag_errors', 'ag_ref_read_attempts', 'f4_errors', 'poison_hits_real_path', 'ag_agree_with_2J_stack',
                                     'f4_crosstab', 'probe_reference_poison')})
        for d in r['ag_disagree'][:6]:
            print('   AGDIS', d)
    print('AG entry:', res['ag_how'])


if __name__ == '__main__':
    main()
