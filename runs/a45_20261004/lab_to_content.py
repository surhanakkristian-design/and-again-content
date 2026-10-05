# A45 stage 1: the 10 lab videos (A44, lib/labExercises.json) -> content/<id>.json in the A45 format, texts unchanged.
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
lab = json.load(open(os.path.expanduser('~/Projects/and-again-a45/lib/labExercises.json')))
FEMALE = {'the woman', 'the girl', 'a woman', 'a girl'}
MALE = {'the man', 'the young man', 'the duke', 'a man', 'a duke'}
def g(name):
    return 'female' if name in FEMALE else 'male' if name in MALE else None
for v in lab:
    genders = [g(t['target']) for t in v['taps']]
    first = next((x for x in genders if x), None)
    default = first or ('female' if v['mediaId'] % 2 == 0 else 'male')
    subj = v['answer'][0].lower()
    out = {
        'mediaId': v['mediaId'], 'level': v['level'], 'keyWord': v['keyWord'], 'defaultVoice': default,
        'stillS': v['stillS'], 'answerS': v.get('answerS'),
        'taps': [{'phrase': t['phrase'], 'target': t['target'], 'voice': g(t['target']) or default, 'keys': t['keys']} for t in v['taps']],
        'nouns': [{'word': n['word'], 'x': n['x'], 'y': n['y'], 'voice': g(n['word']) or default} for n in v['nouns'] if n.get('correct', True)],
        'question': v['question'], 'answer': v['answer'],
        'answerVoice': 'female' if subj == 'she' else 'male' if subj == 'he' else default,
        'tr': v['tr'], 'source': 'a44',
    }
    json.dump(out, open(f'{HERE}/content/{v["mediaId"]}.json', 'w'), ensure_ascii=False, indent=1)
    print(v['mediaId'], default, [t['voice'] for t in out['taps']], [n['voice'] for n in out['nouns']], out['answerVoice'])
