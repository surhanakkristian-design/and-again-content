# A57: the English source of every video still to do (src/<id>.json): the live media_exercise_sets row (src/sets_en.json),
# the key word per language (word_localizations of the video's first concept_media link: src/concepts.json, src/wl.json),
# description + transcript (data/videos.json, the A45 snapshot). Writers and verifiers read only these files and the frames.
# The 3,034 videos have no English carousel and no English recall rows (those exist for the 10 lab videos only): `carousel`
# is empty, and the recall rows are built by the rule of WRITER_BRIEF.md. Batches: data/bNNN.json (100 ids, A45 order).
#   python3 build_src57.py
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
sets = {r['media_id']: r for r in json.load(open(f'{HERE}/src/sets_en.json'))}
vids = {v['id']: v for v in json.load(open(f'{HERE}/data/videos.json'))}
con = {r['media_id']: r for r in json.load(open(f'{HERE}/src/concepts.json'))}
wl = {(r['concept_id'], r['language_code']): r for r in json.load(open(f'{HERE}/src/wl.json'))}
order = json.load(open(f'{HERE}/data/order.json'))
for i in order:
    s, v, c = sets[i], vids[i], con[i]
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
            'question': s['question'], 'answer': s['answer_chips'], 'answerVoice': s['answer_voice'],
            'carousel': [], 'recall': [],
        },
        # reference only: the earlier word-for-word help translations of the ENGLISH texts (never copy blindly)
        'oldHelpTranslations': {l: (s['tr'] or {}).get(l) or {} for l in ('de', 'es', 'fr')},
    }
    json.dump(out, open(f'{HERE}/src/{i}.json', 'w'), ensure_ascii=False, indent=1)
for n in range(0, len(order), 100):
    b = f'b{n // 100 + 1:03d}'
    p = f'{HERE}/data/{b}.json'
    if not os.path.exists(p): json.dump({'batch': b, 'ids': order[n:n + 100]}, open(p, 'w'))
print('src written for', len(order), 'videos;', (len(order) + 99) // 100, 'batches')
