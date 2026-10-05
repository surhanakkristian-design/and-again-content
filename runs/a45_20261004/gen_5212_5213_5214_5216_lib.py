import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def build(vid, level, keyWord, dv, taps, stillS, nouns, q, ans, av, notes):
    times = json.load(open(f'{HERE}/frames/{vid}/info.json'))['times']
    out = []
    for phrase, target, voice, boxes in taps:
        keys = []
        for t in times:
            b = boxes.get(round(t, 1))
            if b is None: keys.append({'t': t, 'off': True})
            else:
                x, y, w, h = b
                w = min(w, 1 - x); h = min(h, 1 - y)
                keys.append({'t': t, 'x': round(x, 2), 'y': round(y, 2), 'w': round(w, 2), 'h': round(h, 2)})
        out.append({'phrase': phrase, 'target': target, 'voice': voice, 'keys': keys})
    c = {'mediaId': vid, 'level': level, 'keyWord': keyWord, 'defaultVoice': dv, 'taps': out, 'stillS': stillS,
         'nouns': [{'word': w, 'x': x, 'y': y, 'voice': v} for w, x, y, v in nouns], 'question': q, 'answer': ans, 'answerVoice': av, 'notes': notes}
    json.dump(c, open(f'{HERE}/content/{vid}.json', 'w'), indent=1, ensure_ascii=False)
