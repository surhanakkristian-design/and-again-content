"""Remaining genderless / vocative rejections, old wave-2 run vs retry run (same heuristic for both).
genderless FR = a false rejection whose answer uses he/she/his/her/him/hers/himself/herself (tr/hu never mark gender;
every such answer's pronoun gender is free by decision 22). vocative FR = a false rejection whose source contains a
listed address term and whose answer drops it (no dude/bro/honey/dear/girl/daughter/sis/... in the answer) or whose
content-check word IS the address term."""
import json, re, sys, os
W1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, W1 + '/common'); import prompts_w1 as P
G = re.compile(r"\b(he|she|his|her|him|hers|himself|herself)\b", re.I)
EN_VOC = re.compile(r"\b(bro|dude|man|mate|buddy|pal|girl|girlie|babe|honey|dear|darling|sweetie|sweetheart|love|daughter|kid|friend|sis|bestie|boss|miss|teacher|everyone|guys|folks|brother|sister)\b", re.I)
def run(path, lang):
    h = json.load(open(path))
    voc = [v.lower() for v in P.VOC[lang].split(', ')]
    out = {'fr_total': h['false_rejections']['n'], 'genderless': [], 'vocative': []}
    for it in h['false_rejections']['items']:
        s, a = it['source'], it['answer']
        if G.search(a):
            out['genderless'].append((it['aid'], it['layer'], it.get('cc_word')))
        sv = [v for v in voc if re.search(r'(?i)(^|\W)' + re.escape(v) + r'(\W|$)', s)]
        if sv and (not EN_VOC.search(a) or (it.get('cc_word') or '').lower() in sv):
            out['vocative'].append((it['aid'], it['layer'], it.get('cc_word')))
    return out
res = {}
for lang in ('tr', 'hu'):
    for tag, p in (('wave2', f'{W1}/{lang}/partD/analysis/HEADLINE.json'), ('retry', f'{W1}/retry_trhu/{lang}/partD/analysis/HEADLINE.json')):
        if os.path.exists(p):
            r = run(p, lang); res[f'{lang}_{tag}'] = r
            print(lang, tag, 'FR', r['fr_total'], 'genderless', len(r['genderless']), 'vocative', len(r['vocative']), r['genderless'], r['vocative'])
json.dump(res, open(W1 + '/retry_trhu/CLUSTERS.json', 'w'), indent=1, ensure_ascii=False)
