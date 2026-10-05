import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def build(mid, level, kw, dv, taps, still, nouns, q, ans, av, notes):
    times = json.load(open(f'{HERE}/frames/{mid}/packet.json'))['times']
    out = []
    for phrase, target, voice, boxes in taps:
        keys = []
        for t, b in zip(times, boxes):
            if b is None: keys.append({'t': t, 'off': True})
            else:
                x, y, x2, y2 = b
                x, y, x2, y2 = max(0, x), max(0, y), min(1, x2), min(1, y2)
                keys.append({'t': t, 'x': round(x, 2), 'y': round(y, 2), 'w': round(x2 - x, 2), 'h': round(y2 - y, 2)})
        out.append({'phrase': phrase, 'target': target, 'voice': voice, 'keys': keys})
    c = {'mediaId': mid, 'level': level, 'keyWord': kw, 'defaultVoice': dv, 'taps': out, 'stillS': still,
         'nouns': [{'word': w, 'x': x, 'y': y, 'voice': v} for w, x, y, v in nouns],
         'question': q, 'answer': ans.split(' '), 'answerVoice': av, 'notes': notes}
    json.dump(c, open(f'{HERE}/content/{mid}.json', 'w'), indent=1, ensure_ascii=False)
