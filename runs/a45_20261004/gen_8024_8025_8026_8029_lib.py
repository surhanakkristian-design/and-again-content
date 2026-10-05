import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def build(mid, level, key, dv, taps, still, nouns, q, ans, av, notes):
    times = json.load(open(f'{HERE}/frames/{mid}/packet.json'))['times']
    out = []
    for phrase, target, voice, boxes in taps:
        keys = []
        for t, b in zip(times, boxes):
            if b is None: keys.append({'t': t, 'off': True})
            else:
                x, y, w, h = b
                keys.append({'t': t, 'x': round(x, 2), 'y': round(y, 2), 'w': round(w, 2), 'h': round(h, 2)})
        assert len(boxes) == len(times)
        out.append({'phrase': phrase, 'target': target, 'voice': voice, 'keys': keys})
    c = {'mediaId': mid, 'level': level, 'keyWord': key, 'defaultVoice': dv, 'taps': out, 'stillS': still,
         'nouns': [{'word': w, 'x': x, 'y': y, 'voice': v} for w, x, y, v in nouns],
         'question': q, 'answer': ans.split(' '), 'answerVoice': av, 'notes': notes}
    json.dump(c, open(f'{HERE}/content/{mid}.json', 'w'), indent=1, ensure_ascii=False)
