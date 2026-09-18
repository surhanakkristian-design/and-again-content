#!/usr/bin/env python3
"""Phase 1c postannot: build the four self-contained review task files (zero model tokens).
   python3 phase1c/scripts/build_review_tasks.py
Inputs: phase1c/annotated/<id>.json (80, after map_alts), phase1b/synonyms/{table,annotator,ng_phase1c}.json,
phase1b/mistakes/<t>.json, phase1b/selection/all230.json, phase1c/selection.json, phase1c/measure/supp_fix_before.json.
Outputs: phase1c/tasks/review_{syn,lib,sample}.md, phase1c/tasks/supp.md (split into _1/_2/... when > MAX_CHARS),
phase1c/tasks/review_manifest.json (counts, sample ids, parts)."""
import json, os, random, re
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
P1C = os.path.dirname(HERE)
ROOT = os.path.dirname(P1C)
P1B = os.path.join(ROOT, 'phase1b')
MAX_CHARS = 68000  # ~20k tokens
SEED = 20260920
REL = lambda p: os.path.relpath(p, ROOT)

rj = lambda p: json.load(open(p))
sel = rj(os.path.join(P1C, 'selection.json'))
batch_of = {}
for b in ('S', 'L'):
    for x in sel['batches'][b]:
        batch_of[int(x['exercise_id'] if isinstance(x, dict) else x)] = b
src = {int(r['exercise_id']): r for r in rj(os.path.join(P1B, 'selection', 'all230.json'))}
ids = sorted(batch_of)
ann = {i: rj(os.path.join(P1C, 'annotated', f'{i}.json')) for i in ids}
groups = {}
for f in ('table.json', 'annotator.json', 'ng_phase1c.json'):
    p = os.path.join(P1B, 'synonyms', f)
    if os.path.exists(p):
        for g in rj(p)['groups']:
            groups[g['id']] = g
lib = {}
for f in os.listdir(os.path.join(P1B, 'mistakes')):
    if re.fullmatch(r'\d+\.json', f):
        d = rj(os.path.join(P1B, 'mistakes', f)); lib[int(d['type_id'])] = d
FLAG_103 = 'NOTE: the Slovak of id 103 does not match its English (annotated from the English only) — do not "fix" 103 to the Slovak.'

SCHEMA = """## Output format (write exactly this JSON, nothing else in the file)
{"changes":[ <change>, ... ], "unchanged": <int>, "notes": "<optional, one line>"}
Every change carries "target", "op" and a one-line "reason". Allowed changes:
- {"target":"syn","op":"set","group":"<id>","set":{"m":[...],"pos":"v|n|a|x","head":0,"irr":{...},"ok":"…","bad":"…"}}  (only the fields you change)
- {"target":"syn","op":"add_members","group":"<id>","members":["lemma", ...]}
- {"target":"syn","op":"remove_members","group":"<id>","members":["lemma", ...]}
- {"target":"syn","op":"remove_group","group":"<id>"}   (annotation anchors pointing to it are dropped)
- {"target":"syn","op":"merge_into","group":"<ng id>","into":"<existing id>"}   (anchors repointed; add members first if needed)
- {"target":"syn","op":"add_group","group":{"id":"<new id>","kind":"contextual","pos":"v|n|a|x","m":[...],"ok":"…","bad":"…"}}
- {"target":"lib","op":"set_item","item":"<libId>","set":{"verdict":"wrong|correct_with_tip","pattern":"…","sk":"…","cz":"…","en":"…","kind":"…","slots":[...]}}
- {"target":"lib","op":"remove_item","item":"<libId>"}
- {"target":"lib","op":"add_item","type_id":<int>,"item":{full item as in the library}}
- {"target":"ann","op":"set","id":<exercise id>,"key":"v|lk|s|g|o|d|p|m","value":<full new value>}
- {"target":"ann","op":"merge","id":<id>,"key":"s|o|d","value":{"anchor":"…"}}   (adds/overwrites entries)
- {"target":"ann","op":"append","id":<id>,"key":"g|p|m","value":[<entries>]}
- {"target":"ann","op":"delete","id":<id>,"key":"s|o|d|g|p|m","entry":"<anchor, or libId for m, or the p string>"}
- {"target":"ann","op":"add_variant","id":<id>,"variant":"<full sentence>","lock":"<locked span in it>"}
- {"target":"ann","op":"remove_variant","id":<id>,"index":<int ≥1>}
Members are LEMMAS (base form) for pos v/n/a; pos x = fixed surface strings (no inflection).
"unchanged" = number of reviewed units (groups / items / sentences / rejections) you left as they are."""

def spec_rules():
    return """## Format rules (condensed from FORMAT_SPEC.md)
- Synonym group: `kind` safe (swapped everywhere, ~30 groups, do not grow) or contextual (only where an annotation's `s` points to it; needs `ok` = valid example "A = B" and `bad` = invalid example "A ≠ B"). `m` = lemmas; forms are generated (v: base/3sg/past/pp/-ing; n: sg/pl; a: base/-er/-est), a swap keeps the form. pos x = invariant surface strings.
- Library item: verdict `wrong` or `correct_with_tip` (grammatical, same meaning, but not the practised structure / clearly more natural). Feedback: only what is wrong, no praise, English tense names, gender-neutral sk/cz, never the whole reference sentence, ≤150 chars after filling; `{right}`/`{wrong}` filled automatically.
- Annotation: `v` variants (v[0] = reference; ≤3 more, each STRUCTURALLY different — never only a word/determiner/pronoun/optional-word swap), `lk` locked span per variant (the practised grammar; nothing changes inside it), `s` anchor→group, `g` gender chains (only when the Slovak does not fix gender), `o` pronoun alternatives, `d` determiner freedom (A = the|a/an|this|that, P = the|these|those|∅, Z = the|∅, or explicit list; only where the Slovak has no article/demonstrative), `p` optional words (+w insert / -anchor drop; meaning-neutral only), `m` library mistakes [libId, wrongText(, anchor)]. `alt` = the annotator's free-text alternatives (mapped by script into `s`)."""

def ann_line(a, keys=('v', 'lk', 's', 'g', 'o', 'd', 'p', 'm', 'alt')):
    return json.dumps({k: a[k] for k in keys if k in a}, ensure_ascii=False)

def group_line(g):
    keep = {k: g[k] for k in ('id', 'kind', 'pos', 'm', 'head', 'irr', 'ok', 'bad') if k in g and g[k] not in ('', None)}
    return json.dumps(keep, ensure_ascii=False)

def sent_ref(i):
    s = src[i]
    return f"{i} [{batch_of[i]} {s['level']}] EN: {ann[i]['v'][0]} | SK: {s['sk']}"

def write_parts(name, header, units, footer, out_rel):
    """units: list of text blocks; split into parts ≤ MAX_CHARS each."""
    parts, cur = [], []
    base = len(header) + len(footer) + 600
    for u in units:
        if cur and base + sum(len(x) + 1 for x in cur) + len(u) > MAX_CHARS:
            parts.append(cur); cur = []
        cur.append(u)
    if cur: parts.append(cur)
    files = []
    for k, p in enumerate(parts, 1):
        suffix = f'_{k}' if len(parts) > 1 else ''
        out = out_rel.replace('.json', f'{suffix}.json')
        fn = os.path.join(P1C, 'tasks', f'{name}{suffix}.md')
        part_note = f'\n**Part {k} of {len(parts)}** — review only the units in this file; write `{out}`.\n' if len(parts) > 1 else ''
        text = header.replace('{OUT}', out) + part_note + '\n' + '\n'.join(p) + '\n\n' + footer.replace('{OUT}', out) + '\n'
        open(fn, 'w').write(text)
        files.append({'file': REL(fn), 'chars': len(text), 'est_tokens': round(len(text) / 3.4), 'units': len(p), 'output': out})
    return files

manifest = {}

# ---------- 4.1 synonym review ----------
used = defaultdict(list)  # gid -> [(id, anchor)]
for i in ids:
    for anchor, gid in ann[i].get('s', {}).items():
        used[gid].append((i, anchor))
ng_all = [g for g in groups.values() if str(g['id']).startswith('ng1c_')]
existing_used = sorted(g for g in used if g in groups and not g.startswith('ng1c_'))
units = []
for gid in existing_used:
    uses = '; '.join(f"{i} “{a}”" for i, a in used[gid])
    units.append(f"- {group_line(groups[gid])}\n  used by: {uses}")
units.append('\n### B. Proposed NEW groups (ng) — ok/bad are EMPTY; accept (set ok+bad, fix m/pos), merge_into an existing group, or remove\n')
for g in ng_all:
    basis = groups.get(g.get('basis') or '', None)
    srcs = ' || '.join(sent_ref(i) for i in g['sources'] if i in ann)
    alts = {i: ann[i].get('alt', {}) for i in g['sources'] if i in ann}
    units.append(f"- {json.dumps({k: g[k] for k in ('id', 'pos', 'm', 'anchor')}, ensure_ascii=False)}"
                 + (f"\n  nearest existing group: {group_line(basis)}" if basis else '')
                 + f"\n  sentence(s): {srcs}\n  annotator alt: {json.dumps(alts, ensure_ascii=False)}")
hdr = f"""# Review task §4.1 — synonym groups used or proposed by the 80 Phase 1c sentences
[STEP: review-syn] One read (this file), one write: `{{OUT}}` (under ~/Projects/and-again-content/translation-offline/).
Budget: no other reads, no tools besides the one Write.

## What to do
For every group below decide: keep, change or remove. A group is WRONG when a member is not interchangeable with the others in
the sentences that use it (see `ok`/`bad`), when a member changes the meaning, or when a lemma/pos is wrong (pos x ng groups hold
raw surfaces — convert to lemma + pos v/n/a when they inflect, so the checker generates the forms; keep x for invariant phrases).
For the ng proposals (section B): accept only real everyday alternatives for the anchor in THAT sentence; write `ok`/`bad`; merge into
the nearest existing group when it fits; remove members that change the meaning. Be strict: a wrong member causes false acceptances.
{FLAG_103}

{spec_rules()}

{SCHEMA}

## Units ({len(existing_used)} existing groups + {len(ng_all)} ng proposals = {len(existing_used) + len(ng_all)})
### A. Existing groups used by these sentences
"""
manifest['syn'] = {'existing_groups': len(existing_used), 'ng_groups': len(ng_all), 'total': len(existing_used) + len(ng_all),
                   'parts': write_parts('review_syn', hdr, units, 'Write the JSON to `{OUT}` now. "unchanged" counts groups left as they are.', 'phase1c/review/syn.json')}

# ---------- 4.2 library review ----------
topics = set()
for i in ids:
    topics.add(int(ann[i]['t']))
    for m in ann[i].get('m', []):
        topics.add(int(str(m[0]).split('.')[0]))
topics = sorted(t for t in topics if t in lib)
units, n_items = [], 0
for t in topics:
    d = lib[t]
    users = [i for i in ids if int(ann[i]['t']) == t or any(str(m[0]).startswith(f'{t}.') for m in ann[i].get('m', []))]
    block = [f"\n### Topic {t} — {d.get('topic', '')} ({d.get('level', '')}), {len(d['items'])} items; used by {len(users)} sentences, e.g. {ann[users[0]]['v'][0]!r}"]
    for it in d['items']:
        block.append(json.dumps(it, ensure_ascii=False)); n_items += 1
    units.append('\n'.join(block))
hdr = f"""# Review task §4.2 — mistake-library topics used by the 80 Phase 1c sentences
[STEP: review-lib] One read (this file), one write: `{{OUT}}` (under ~/Projects/and-again-content/translation-offline/).
Budget: no other reads, no tools besides the one Write.

## What to do
Check every item: is the `verdict` right (a real error = wrong; grammatical + same meaning but not the practised structure = correct_with_tip),
does the `pattern` describe one clear learner error, are the sk/cz/en feedbacks correct, natural, gender-neutral, ≤150 chars after filling,
only about what is wrong, English grammar names, never the whole reference sentence? Fix with set_item; remove duplicates or items that
describe correct English as wrong. Do not add items unless a frequent learner error of the topic is clearly missing.

{spec_rules()}

{SCHEMA}

## Units ({len(topics)} topics, {n_items} items)
"""
manifest['lib'] = {'topics': len(topics), 'items': n_items, 'topic_ids': topics,
                   'parts': write_parts('review_lib', hdr, units, 'Write the JSON to `{OUT}` now. "unchanged" counts ITEMS left as they are.', 'phase1c/review/lib.json')}

# ---------- 4.3 sample review ----------
rng = random.Random(SEED)
by = defaultdict(list)
for i in ids:
    if i != 103: by[(batch_of[i], src[i]['level'])].append(i)
pick = []
for lv in rng.sample(['A1', 'A2', 'B1', 'B2'], 2):
    pick.append(rng.choice(by[('S', lv)]))
for lv in ['A1', 'A2', 'B1', 'B2', 'B1', 'B2']:
    pool = [i for i in by[('L', lv)] if i not in pick]
    if lv == 'B2' and not any(str(src[x]['new_long']).lower() == 'true' for x in pick):
        pool = [i for i in pool if str(src[i]['new_long']).lower() == 'true'] or pool
    pick.append(rng.choice(pool))
units = []
for i in pick:
    a = ann[i]; s = src[i]
    gl = {gid: groups[gid]['m'] for gid in a.get('s', {}).values() if gid in groups}
    ml = {m[0]: lib[int(m[0].split('.')[0])]['items'] for m in a.get('m', []) if int(m[0].split('.')[0]) in lib}
    mk = {k: next((it['kind'] + ' / ' + it['verdict'] for it in v if it['id'] == k), '?') for k, v in ml.items()}
    units.append(f"\n### {i} [{batch_of[i]} {s['level']}{' long' if str(s['new_long']).lower() == 'true' else ''}] topic {s['topic']} — answer span “{s['en_answer']}”\n"
                 f"EN: {s['en']}\nSK: {s['sk']}\nannotation: {json.dumps(a, ensure_ascii=False)}\n"
                 f"synonym groups (members): {json.dumps(gl, ensure_ascii=False)}\nmistake items used (kind / verdict): {json.dumps(mk, ensure_ascii=False)}")
hdr = f"""# Review task §4.3 — 10 % annotation sample (8 sentences)
[STEP: review-sample] One read (this file), one write: `{{OUT}}` (under ~/Projects/and-again-content/translation-offline/).
Budget: no other reads, no tools besides the one Write.

## What to do
For each sentence check the full annotation against the Slovak: missing or wrong variants (a correct learner answer the checker would
reject), wrong locks, missing/wrong gender (`g` only when the Slovak does not fix gender), determiner freedom (`d` only where the Slovak has
no article/demonstrative), optional words, synonym anchors (wrong group = false acceptance), and whether the `m` mistakes are real and
correctly placed. Output ann changes (or syn changes when a group is wrong). Sampling: seed {SEED}, stratified by batch and level
(2 from S, 6 from L; id 103 excluded — its Slovak does not match).

{spec_rules()}

{SCHEMA}

## Units (8 sentences: {', '.join(map(str, pick))})
"""
manifest['sample'] = {'ids': pick, 'seed': SEED,
                      'parts': write_parts('review_sample', hdr, units, 'Write the JSON to `{OUT}` now. "unchanged" counts SENTENCES needing no change.', 'phase1c/review/sample.json')}

# ---------- 4.5 supplementary pass ----------
rows = rj(os.path.join(P1C, 'measure', 'supp_fix_before.json'))['rows']
rej = [r for r in rows if r['verdict'] == 'wrong']
units = []
last = None
for k, r in enumerate(rej, 1):
    i = r['exercise_id']
    if i != last:
        a = ann[i]
        gl = {gid: groups[gid]['m'] for gid in a.get('s', {}).values() if gid in groups}
        units.append(f"\n### {sent_ref(i)}\nannotation: {ann_line(a, ('v', 'lk', 's', 'g', 'o', 'd', 'p'))}\ngroups: {json.dumps(gl, ensure_ascii=False)}")
        last = i
    units[-1] += f"\n- R{k}: “{r['answer']}” → checker: {r['feedback']} (step {r['step']})"
hdr = f"""# Supplementary pass §4.5 — rejections of the independent (fix-split) translations
[STEP: supp] One read (this file), one write: `{{OUT}}` (under ~/Projects/and-again-content/translation-offline/).
Budget: no other reads, no tools besides the one Write.

Scope: the fix-pass split `phase1c/inputs/supp_fix.json` ({len(rows)} translations of the supp ids) was run through checker v2 with the
Phase 1c annotations: {len(rows) - len(rej)} accepted, {len(rej)} rejected (all listed below as R1…R{len(rej)}). The held-out coverage
translations (step 3) are NOT in this split by design, so none of their rejections appear here.

## What to do — per rejection R<n>
1. Is the translation really a correct rendering of the Slovak (same meaning, grammatical, practised structure kept or acceptable)?
2. If NO: record it as "correctly rejected".
3. If YES: give the fix, preferring in this order: `synonym_table` (add a member / group — generalises to other sentences),
   `annotation` (d/g/o/p/s entry for this sentence), `new_variant` (a structurally different variant + its lock). Give the EXACT change
   in the change format below. One fix may cover several rejections — list all their R numbers.
{FLAG_103}

## Output format (write exactly this JSON)
{{"verdicts":[{{"r":"R1","really_correct":true|false,"fix_type":"synonym_table|annotation|new_variant|null","change_idx":[0],"reason":"…"}}, ...],
 "changes":[ <change objects as below; referenced by index from verdicts> ],
 "unchanged": <number of rejections judged correctly rejected>}}

{SCHEMA.split(chr(10), 1)[1]}

{spec_rules()}

## Rejections ({len(rej)} in {len(set(r['exercise_id'] for r in rej))} sentences)
"""
manifest['supp'] = {'fix_translations': len(rows), 'accepted': len(rows) - len(rej), 'rejected': len(rej),
                    'step3_rejections_in_fix_split': 0,
                    'parts': write_parts('supp', hdr, units, 'Write the JSON to `{OUT}` now.', 'phase1c/review/supp.json')}

json.dump(manifest, open(os.path.join(P1C, 'tasks', 'review_manifest.json'), 'w'), indent=1)
print(json.dumps({k: {kk: vv for kk, vv in v.items() if kk not in ('topic_ids',)} for k, v in manifest.items()}, indent=0))
