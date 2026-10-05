import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
def build(mid, level, kw, dv, taps, still, nouns, q, ans, av, notes):
    info = json.load(open(f'{HERE}/frames/{mid}/packet.json'))
    out_taps = []
    for phrase, target, voice, boxes in taps:
        keys = []
        for t, b in zip(info['times'], boxes):
            if b is None: keys.append({'t': t, 'off': True})
            else:
                x, y, w, h = b
                x = max(0, x); y = max(0, y); w = min(w, 1 - x); h = min(h, 1 - y)
                keys.append({'t': t, 'x': round(x, 2), 'y': round(y, 2), 'w': round(w, 2), 'h': round(h, 2)})
        assert len(keys) == len(info['times'])
        out_taps.append({'phrase': phrase, 'target': target, 'voice': voice, 'keys': keys})
    c = {'mediaId': mid, 'level': level, 'keyWord': kw, 'defaultVoice': dv, 'taps': out_taps, 'stillS': still,
         'nouns': [{'word': w, 'x': x, 'y': y, 'voice': v} for w, x, y, v in nouns],
         'question': q, 'answer': ans.split(), 'answerVoice': av, 'notes': notes}
    json.dump(c, open(f'{HERE}/content/{mid}.json', 'w'), indent=1, ensure_ascii=False)
