import json, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
def build(vid, spec):
    times = json.load(open(f'{HERE}/frames/{vid}/packet.json'))['times']
    taps = []
    for p in spec['taps']:
        boxes = spec['boxes'][p['target']]
        keys = []
        for t in times:
            b = boxes.get(t, boxes.get('all'))
            if b is None: keys.append({'t': t, 'off': True})
            else:
                x, y, w, h = b
                keys.append({'t': t, 'x': x, 'y': y, 'w': round(w, 2), 'h': round(h, 2)})
        taps.append({'phrase': p['phrase'], 'target': p['target'], 'voice': p['voice'], 'keys': keys})
    out = {k: spec[k] for k in ('mediaId', 'level', 'keyWord', 'defaultVoice')}
    out['taps'] = taps
    for k in ('stillS', 'nouns', 'question', 'answer', 'answerVoice', 'notes'): out[k] = spec[k]
    json.dump(out, open(f'{HERE}/content/{vid}.json', 'w'), indent=1, ensure_ascii=False)
spec = json.load(open(f'{HERE}/scratch/spec_{sys.argv[1]}.json'))
# json keys are strings: convert time keys
spec['boxes'] = {tg: {(float(k) if k != 'all' else 'all'): v for k, v in b.items()} for tg, b in spec['boxes'].items()}
build(int(sys.argv[1]), spec)
