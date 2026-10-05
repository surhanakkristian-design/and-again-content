# A55: the English source of the 10 lab videos (src/<id>.json) - the live media_exercise_sets row (src/sets_en.json),
# the A56 carousel + recall rows (lib/labExtras.json of branch a56), the key word per language (word_localizations,
# src/wl.json), description + transcript (data/videos.json). Writers and verifiers read only these files and the frames.
#   python3 build_src.py [path to labExtras.json]
import json, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
EXTRAS = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/Projects/and-again-a56/lib/labExtras.json')
IDS = [8055, 236, 624, 7071, 4265, 461, 62, 8039, 432, 8056]
sets = {r['media_id']: r for r in json.load(open(f'{HERE}/src/sets_en.json'))}
ex = json.load(open(EXTRAS))
vids = {v['id']: v for v in json.load(open(f'{HERE}/data/videos.json'))}
concepts = {r['media_id']: r for r in json.load(open(f'{HERE}/src/concepts.json'))}
wl = {}
for r in json.load(open(f'{HERE}/src/wl.json')): wl[(r['concept_id'], r['language_code'])] = r
def recall_text(row): return ' '.join(p['text'] for p in row['parts'])
for i in IDS:
    s, e, v, c = sets[i], ex[str(i)], vids[i], concepts[i]
    key = {}
    for l in ('en', 'de', 'es', 'fr'):
        w = wl.get((c['concept_id'], l)); key[l] = (w['display_form'] or w['translation']) if w else None
    out = {
        'mediaId': i, 'level': s['level'], 'conceptId': c['concept_id'], 'partOfSpeech': c['part_of_speech'],
        'definition': c['definition'], 'keyWord': key, 'description': v['asset_description'], 'transcript': v['transcript'],
        'defaultVoice': s['default_voice'], 'stillS': s['still_s'], 'width': s['width'], 'height': s['height'],
        'en': {
            'taps': [{'phrase': t['phrase'], 'target': t['target'], 'voice': t['voice']} for t in s['taps']],
            'nouns': [{'word': n['word'], 'x': n['x'], 'y': n['y'], 'voice': n['voice']} for n in s['nouns']],
            'question': s['question'], 'answer': e.get('answer') or s['answer_chips'], 'answerVoice': ('male' if 'daniel' in (e.get('answerVoice') or '') else 'female' if 'samantha' in (e.get('answerVoice') or '') else s['answer_voice']),
            'carousel': [{'caption': p['caption'], 'url': p['url']} for p in (e['carousel'] or {}).get('pictures', [])],
            'recall': [{'from': r['from'], 'text': recall_text(r), 'parts': r['parts']} for r in e['recall']],
        },
        # reference only: the earlier help translations of the ENGLISH texts (not written natively; never copy blindly)
        'oldHelpTranslations': {l: {**(s['tr'].get(l) or {}), 'captions': (e['tr'].get(l) or {}).get('captions', {})} for l in ('de', 'es', 'fr')},
    }
    json.dump(out, open(f'{HERE}/src/{i}.json', 'w'), ensure_ascii=False, indent=1)
print('src written for', len(IDS), 'videos')
