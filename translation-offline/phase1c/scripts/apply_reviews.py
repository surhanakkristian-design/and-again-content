#!/usr/bin/env python3
"""Phase 1c: apply the review outputs (syn / lib / sample / supp) to Phase 1c COPIES. Zero model tokens.
   python3 phase1c/scripts/apply_reviews.py [--reviews DIR] [--out-root DIR] [--no-forms]
Reads   <reviews>/{syn,lib,sample,supp}*.json   (default phase1c/review; split parts syn_1.json … are all picked up)
        phase1b/synonyms/{table,annotator,ng_phase1c}.json, phase1c/annotated/<id>.json (80), phase1c/selection.json
Writes  <out-root>/synonyms/{table,annotator,ng_phase1c,review_added}.json + forms.json (via build_forms.ts, SYN_DIR)
        <out-root>/annotated_after/<id>.json      (copies of the 80 annotations with ann ops + group repoints/drops)
        <out-root>/overlay/library.json           ({items:{libId: item|null}, added:[{type_id,item}]}; read via LIB_OVERLAY)
        <out-root>/review/applied.json            (counts per file/target/op, supp fix types, errors)
Never touches phase1b/. Order: syn (all files) → lib → ann, files in the order syn, lib, sample, supp.
AFTER measurement (from translation-offline/):
  ANN_DIR=$PWD/phase1c/annotated_after SYN_DIR=$PWD/phase1c/synonyms LIB_OVERLAY=$PWD/phase1c/overlay/library.json \\
    node phase1b/scripts/measure.ts coverage phase1c/inputs/cov_heldout.json phase1c/measure/cov_after.json"""
import copy, glob, json, os, subprocess, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
P1C = os.path.dirname(HERE)
ROOT = os.path.dirname(P1C)
P1B = os.path.join(ROOT, 'phase1b')
args = sys.argv[1:]
opt = lambda n, d: args[args.index(n) + 1] if n in args else d
REV = opt('--reviews', os.path.join(P1C, 'review'))
OUT = opt('--out-root', P1C)
rj = lambda p: json.load(open(p))

def wj(path, data, lines=False):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    txt = json.dumps(data, ensure_ascii=False)
    if lines and isinstance(data, dict) and 'groups' in data:
        txt = '{"groups":[\n' + ',\n'.join(json.dumps(g, ensure_ascii=False) for g in data['groups']) + '\n]}'
    open(path, 'w').write(txt + '\n')

# ---- load sources
syn_files = {f: rj(os.path.join(P1B, 'synonyms', f)) for f in ('table.json', 'annotator.json', 'ng_phase1c.json')
             if os.path.exists(os.path.join(P1B, 'synonyms', f))}
syn_files['review_added.json'] = {'groups': []}
where = {}  # gid -> file
for f, d in syn_files.items():
    for g in d['groups']: where[g['id']] = f
def grp(gid):
    f = where.get(gid)
    return next((g for g in syn_files[f]['groups'] if g['id'] == gid), None) if f else None
sel = rj(os.path.join(P1C, 'selection.json'))['batches']
ids = [int(i) for b in ('S', 'L') for i in sel[b]]
ann = {i: rj(os.path.join(P1C, 'annotated', f'{i}.json')) for i in ids}
lib_items, lib_type = {}, {}
for f in glob.glob(os.path.join(P1B, 'mistakes', '*.json')):
    b = os.path.basename(f)
    if b[:-5].isdigit():
        d = rj(f)
        for it in d['items']: lib_items[it['id']] = it; lib_type[it['id']] = d['type_id']
overlay = {'items': {}, 'added': []}

log = {'files': {}, 'by_target_op': Counter(), 'errors': [], 'supp': {}, 'irr_normalised': []}
def err(src, ch, msg): log['errors'].append({'file': src, 'change': ch, 'error': msg})

def gid_refs(gid):
    return [(i, a) for i in ids for a, g in ann[i].get('s', {}).items() if g == gid]

def norm_irr(g, src):
    """FORMAT_SPEC §1: irr = {lemma: [3sg, past, pp, ing]} (verbs). Reviewers sometimes wrote {lemma: {past, pp, ing}}:
    convert when all four forms are given, else drop the entry so forms.ts falls back to its built-in irregular table
    (which covers every head the syn review used: let see keep come wake awake find hold have get take stand fall)."""
    irr = g.get('irr')
    if not isinstance(irr, dict): return
    for k, v in list(irr.items()):
        if isinstance(v, dict):
            keys = ('3sg', 'past', 'pp', 'ing')
            if all(v.get(x) for x in keys): irr[k] = [v[x] for x in keys]; log['irr_normalised'].append(f"{g['id']}:{k}:converted")
            else: del irr[k]; log['irr_normalised'].append(f"{g['id']}:{k}:dropped(built-in table)")
    if not irr: del g['irr']

def apply_syn(ch, src):
    op = ch.get('op')
    if op == 'add_group':
        g = dict(ch['group']); g.setdefault('kind', 'contextual')
        if g['id'] in where: return err(src, ch, 'group id exists')
        norm_irr(g, src); syn_files['review_added.json']['groups'].append(g); where[g['id']] = 'review_added.json'; return True
    g = grp(ch.get('group'))
    if g is None: return err(src, ch, 'unknown group')
    if op == 'set':
        for k, v in ch.get('set', {}).items():
            if k == 'id': continue
            g[k] = v
        norm_irr(g, src)
    elif op == 'add_members':
        g['m'] = g['m'] + [m for m in ch['members'] if m not in g['m']]
    elif op == 'remove_members':
        g['m'] = [m for m in g['m'] if m not in ch['members']]
        if len(g['m']) < 2: return apply_syn({**ch, 'op': 'remove_group'}, src)
    elif op == 'remove_group':
        syn_files[where[g['id']]]['groups'].remove(g); del where[g['id']]
        for i, a in gid_refs(g['id']): del ann[i]['s'][a]
    elif op == 'merge_into':
        if grp(ch.get('into')) is None: return err(src, ch, 'unknown target group')
        for i, a in gid_refs(g['id']): ann[i]['s'][a] = ch['into']
        syn_files[where[g['id']]]['groups'].remove(g); del where[g['id']]
    else:
        return err(src, ch, 'unknown syn op')
    return True

def apply_lib(ch, src):
    op = ch.get('op'); iid = ch.get('item')
    if op == 'add_item':
        it = ch['item']
        if it.get('id') in lib_items: return err(src, ch, 'item id exists')
        overlay['added'].append({'type_id': ch['type_id'], 'item': it}); lib_items[it['id']] = it; lib_type[it['id']] = ch['type_id']; return True
    if iid not in lib_items: return err(src, ch, 'unknown item')
    if op == 'set_item':
        it = copy.deepcopy(overlay['items'].get(iid) or lib_items[iid]); it.update({k: v for k, v in ch.get('set', {}).items() if k != 'id'})
        overlay['items'][iid] = it
    elif op == 'remove_item':
        overlay['items'][iid] = None
        for i in ids:  # annotations must not reference a removed item
            if 'm' in ann[i]: ann[i]['m'] = [m for m in ann[i]['m'] if m[0] != iid]
    else:
        return err(src, ch, 'unknown lib op')
    return True

def apply_ann(ch, src):
    i = int(ch.get('id', -1)); op = ch.get('op'); k = ch.get('key')
    if i not in ann: return err(src, ch, 'unknown id')
    a = ann[i]
    if op == 'set':
        a[k] = ch['value']
    elif op == 'merge':
        a.setdefault(k, {}).update(ch['value'])
    elif op == 'append':
        a.setdefault(k, []).extend(x for x in ch['value'] if x not in a[k])
    elif op == 'delete':
        e = ch.get('entry')
        if k in ('s', 'o', 'd'): a.get(k, {}).pop(e, None)
        elif k == 'm': a[k] = [m for m in a.get(k, []) if m[0] != e]
        elif k == 'p': a[k] = [p for p in a.get(k, []) if p != e]
        elif k == 'g': a[k] = [c for c in a.get(k, []) if e not in c]
        else: return err(src, ch, 'bad key')
    elif op == 'add_variant':
        if ch['lock'] not in ch['variant'] and ' .. ' not in ch['lock']: return err(src, ch, 'lock not in variant')
        if len(a['v']) >= 4: return err(src, ch, 'already 4 variants')
        a['v'].append(ch['variant']); a.setdefault('lk', [None] * (len(a['v']) - 1)).append(ch['lock'])
    elif op == 'remove_variant':
        x = int(ch['index'])
        if x < 1 or x >= len(a['v']): return err(src, ch, 'bad index')
        a['v'].pop(x); a.get('lk', []).pop(x) if len(a.get('lk', [])) > x else None
    else:
        return err(src, ch, 'unknown ann op')
    for key in ('s', 'o', 'd', 'g', 'p', 'm'):
        if key in a and not a[key]: del a[key]
    return True

APPLY = {'syn': apply_syn, 'lib': apply_lib, 'ann': apply_ann}
files = []
for kind in ('syn', 'lib', 'sample', 'supp'):
    files += sorted(glob.glob(os.path.join(REV, f'{kind}.json')) + glob.glob(os.path.join(REV, f'{kind}_[0-9]*.json')))
loaded = []
for f in files:
    try: d = rj(f)
    except Exception as e: log['errors'].append({'file': f, 'error': f'unreadable: {e}'}); continue
    loaded.append((os.path.basename(f), d))
    log['files'][os.path.basename(f)] = {'changes': len(d.get('changes', [])), 'unchanged': d.get('unchanged'), 'applied': 0}
for target in ('syn', 'lib', 'ann'):
    for name, d in loaded:
        for ch in d.get('changes', []):
            if ch.get('target') != target: continue
            if APPLY[target](ch, name):
                log['files'][name]['applied'] += 1; log['by_target_op'][f"{target}.{ch.get('op')}"] += 1
    for name, d in loaded:
        if name.startswith('supp') and 'verdicts' in d:
            v = d['verdicts']
            log['supp'][name] = {'rejections': len(v), 'really_correct': sum(1 for x in v if x.get('really_correct')),
                                 'correctly_rejected': sum(1 for x in v if x.get('really_correct') is False),
                                 'fix_types': dict(Counter(x.get('fix_type') for x in v if x.get('really_correct')))}

# dangling s anchors → error list (a group removed by name without remove_group)
for i in ids:
    for a_, g in list(ann[i].get('s', {}).items()):
        if g not in where: log['errors'].append({'id': i, 'error': f'anchor {a_} → missing group {g}; dropped'}); del ann[i]['s'][a_]

for f, d in syn_files.items():
    wj(os.path.join(OUT, 'synonyms', f), d, lines=True)
for i, a in ann.items():
    wj(os.path.join(OUT, 'annotated_after', f'{i}.json'), a)
wj(os.path.join(OUT, 'overlay', 'library.json'), overlay)
log['by_target_op'] = dict(log['by_target_op'])
log['groups'] = {f: len(d['groups']) for f, d in syn_files.items()}
if '--no-forms' not in args:
    r = subprocess.run(['node', os.path.join(P1B, 'scripts', 'build_forms.ts')], cwd=ROOT, capture_output=True, text=True,
                       env={**os.environ, 'SYN_DIR': os.path.join(OUT, 'synonyms')})
    log['build_forms'] = (r.stdout.strip() or r.stderr.strip())[-400:]
wj(os.path.join(OUT, 'review', 'applied.json'), log)
print(json.dumps({k: log[k] for k in ('by_target_op', 'supp', 'groups', 'irr_normalised')}, ensure_ascii=False), f"errors={len(log['errors'])}")
