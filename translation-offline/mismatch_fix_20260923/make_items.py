# Builds the proposer input files. Keys: P1-<eid>-es, P2-<eid>-<lang>.
import json, collections, fixlib
by = fixlib.load('before')
types = {int(k): v for k, v in json.load(open('work/types.json')).items()}
c = json.load(open(fixlib.TO + '/mismatch_scan_20260923/confirmed.json'))
EXTRA = {331: (['de', 'ua', 'es', 'fr', 'tr', 'hu'], "the native adds a clause like 'that is the worst' / 'and that is the worst part' which the English (and sk/cz) lack", "drop the added clause; the English stays unchanged"),
         354: (['de', 'ua', 'tr', 'hu', 'sk', 'cz'], "the native adds 'and she laughed' which the English (and es/fr) lack", "drop 'and she laughed'; the English stays unchanged"),
         17991: (['ua', 'es', 'fr', 'tr', 'hu', 'sk', 'cz'], "English 'snacks' vs native 'packets/bags (of snacks)'", "change the native to plain 'snacks' (the English stays 'How many snacks are there on the couch?'); if this native already says just 'snacks', answer NOCHANGE"),
         18387: (['ua', 'es', 'fr', 'tr', 'hu', 'sk', 'cz'], "English 'sits' vs native 'basks / warms itself'", "change the native verb to plain 'sits' (the English stays 'It sits on the warm stone wall.'); if this native already says 'sits', answer NOCHANGE")}

def rowline(r):
    s = f"{r['full_sentence']}  [gap: {r['correct_answer'] or ''}]"
    return s

def block(key, eid, lang, issues, full_context=True):
    e = by[eid]; r = e[lang]
    t = r['exercise_type_id']
    out = [f"@@ {key} {eid} {lang} level-type: {types.get(t, t)} (type {t})",
           f"en: {rowline(e['en'])}  [en intro: {e['en']['intro_text']}]  [en distractors: {e['en']['distractor_1']} | {e['en']['distractor_2']}]",
           f"{lang} CURRENT full: {r['full_sentence']}",
           f"{lang} CURRENT intro_text: {r['intro_text']}",
           f"{lang} CURRENT correct_answer: {r['correct_answer'] or ''}",
           f"{lang} CURRENT distractors: {r['distractor_1'] or ''} | {r['distractor_2'] or ''}"]
    for w, f in issues:
        out.append(f"ISSUE: {w}  -> suggested: {f}")
    if full_context:
        for l in fixlib.LANGS:
            if l not in ('en', lang) and l in e:
                out.append(f"  (context) {l}: {rowline(e[l])}")
    return '\n'.join(out) + '\n'

items = collections.defaultdict(list)       # (eid, lang) -> issues
for x in c:
    if x['L'] == 'en':
        continue
    items[(x['id'], x['L'])].append((x['what'], x['fix']))
    items[(x['id'], x['L'])].append((x['rwhat'], x['rfix']))
for eid, (langs, w, f) in EXTRA.items():
    for l in langs:
        items[(eid, l)].append((w, f))
p1, p2a, p2b = [], [], []
keys = {}
for (eid, lang), iss in sorted(items.items()):
    pron = lang == 'es' and any(x['id'] == eid and x['L'] == 'es' and x['rcat'] == 'number_person_gender' for x in c)
    if pron:
        key = f'P1-{eid}-es'
        p4 = None
        p1.append(block(key, eid, lang, iss, full_context=False))
    else:
        key = f'P2-{eid}-{lang}'
        (p2a if lang in ('de', 'es', 'fr', 'tr') else p2b).append(block(key, eid, lang, iss))
    keys[key] = [eid, lang]
json.dump(keys, open('work/item_keys.json', 'w'))
for n, L in (('p1', p1), ('p2a', p2a), ('p2b', p2b)):
    open(f'agents/{n}_items.txt', 'w').write('\n'.join(L))
    print(n, len(L), sum(map(len, L)))
