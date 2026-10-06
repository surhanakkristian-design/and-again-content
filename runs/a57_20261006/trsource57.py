# A57: tr/<batch>/source_<lang>.json from the VERIFIED content files (verdict PASS / FIXED) of one batch and learning language.
#   python3 trsource57.py <batch> <lang> [<lang> ...]
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
def verdict(lang, vid):
    p = f'{HERE}/verify/{lang}/{vid}.md'
    return open(p).readline().strip() if os.path.exists(p) else ''
batch = sys.argv[1]; ids = json.load(open(f'{HERE}/data/{batch}.json'))['ids']
skip = set(json.load(open(f'{HERE}/data/skipped.json'))) if os.path.exists(f'{HERE}/data/skipped.json') else set()
for lang in sys.argv[2:]:
    out = {}
    for vid in ids:
        if f'{lang}:{vid}' in skip: continue
        v = verdict(lang, vid)
        if v not in ('VERDICT: PASS', 'VERDICT: FIXED'): print(lang, vid, 'not verified:', v or 'no verdict'); continue
        s = json.load(open(f'{HERE}/src/{vid}.json')); c = json.load(open(f'{HERE}/content/{lang}/{vid}.json'))
        en = s['en']
        out[str(vid)] = {
            'about': s['description'], 'level': s['level'],
            'english': {'phrases': [t['phrase'] for t in en['taps']], 'nouns': [n['word'] for n in en['nouns']], 'question': en['question'],
                        'answer': ' '.join(en['answer'])},
            'phrases': [{'text': t['phrase'], 'target': t['target']} for t in c['taps']],
            'nouns': [n['word'] for n in c['nouns']], 'question': c['question'], 'answer': ' '.join(c['answer']),
            'captions': [x['caption'] for x in c.get('carousel', [])],
            'recall': [' '.join(p['text'] for p in r['parts']) for r in c['recall']],
        }
    os.makedirs(f'{HERE}/tr/{batch}/{lang}', exist_ok=True)
    json.dump(out, open(f'{HERE}/tr/{batch}/source_{lang}.json', 'w'), ensure_ascii=False, indent=1)
    print(batch, lang, len(out), 'videos in tr/' + batch + '/source_' + lang + '.json')
