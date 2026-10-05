import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def build(mid, level, key, dv, taps, still, nouns, q, ans, av, notes):
    times = json.load(open(f'{HERE}/frames/{mid}/packet.json'))['times']
    boxes = {}
    out = []
    for phrase, target, voice, bx in taps:
        if isinstance(bx, str): bx = boxes[bx]
        boxes[target] = bx
        keys = []
        for t, b in zip(times, bx):
            if b is None: keys.append({'t': t, 'off': True})
            else: keys.append({'t': t, 'x': b[0], 'y': b[1], 'w': b[2], 'h': b[3]})
        out.append({'phrase': phrase, 'target': target, 'voice': voice, 'keys': keys})
    c = {'mediaId': mid, 'level': level, 'keyWord': key, 'defaultVoice': dv, 'taps': out, 'stillS': still,
         'nouns': [{'word': w, 'x': x, 'y': y, 'voice': v} for w, x, y, v in nouns],
         'question': q, 'answer': ans, 'answerVoice': av, 'notes': notes}
    json.dump(c, open(f'{HERE}/content/{mid}.json', 'w'), indent=1, ensure_ascii=False)
