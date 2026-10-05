# A55: tr/source_<lang>.json from the VERIFIED content files (verdict PASS / FIXED) of a learning language.
#   python3 trsource.py <lang> [...]
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
IDS = [8055, 236, 624, 7071, 4265, 461, 62, 8039, 432, 8056]
def verdict(lang, vid):
    p = f'{HERE}/verify/{lang}/{vid}.md'
    return open(p).readline().strip() if os.path.exists(p) else ''
for lang in sys.argv[1:]:
    out = {}
    for vid in IDS:
        v = verdict(lang, vid)
        if v not in ('VERDICT: PASS', 'VERDICT: FIXED'): print(lang, vid, 'not verified:', v or 'no verdict'); continue
        s = json.load(open(f'{HERE}/src/{vid}.json')); c = json.load(open(f'{HERE}/content/{lang}/{vid}.json'))
        en = s['en']
        out[str(vid)] = {
            'about': s['description'], 'level': s['level'],
            'english': {'phrases': [t['phrase'] for t in en['taps']], 'nouns': [n['word'] for n in en['nouns']], 'question': en['question'],
                        'answer': ' '.join(en['answer']), 'captions': [x['caption'] for x in en['carousel']],
                        'recall': [r['text'] for r in en['recall']]},
            'phrases': [{'text': t['phrase'], 'target': t['target']} for t in c['taps']],
            'nouns': [n['word'] for n in c['nouns']], 'question': c['question'], 'answer': ' '.join(c['answer']),
            'captions': [x['caption'] for x in c['carousel']],
            'recall': [' '.join(p['text'] for p in r['parts']) for r in c['recall']],
        }
    os.makedirs(f'{HERE}/tr/{lang}', exist_ok=True)
    json.dump(out, open(f'{HERE}/tr/source_{lang}.json', 'w'), ensure_ascii=False, indent=1)
    print(lang, len(out), 'videos in tr/source_' + lang + '.json')
