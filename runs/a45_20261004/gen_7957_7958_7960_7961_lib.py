import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def write(mid, level, kw, dv, taps, still, nouns, q, a, av, notes=''):
    info = json.load(open(f'{HERE}/frames/{mid}/packet.json'))
    out = {"mediaId": mid, "level": level, "keyWord": kw, "defaultVoice": dv, "taps": [], "stillS": still,
           "nouns": [{"word": w, "x": x, "y": y, "voice": v} for w, x, y, v in nouns],
           "question": q, "answer": a.split(' '), "answerVoice": av, "notes": notes}
    for phrase, target, voice, boxes in taps:
        keys = []
        for t, b in zip(info['times'], boxes):
            if b is None: keys.append({"t": t, "off": True})
            else:
                x, y, w, h = b
                keys.append({"t": t, "x": x, "y": y, "w": w, "h": h})
        assert len(boxes) == len(info['times'])
        out['taps'].append({"phrase": phrase, "target": target, "voice": voice, "keys": keys})
    json.dump(out, open(f'{HERE}/content/{mid}.json', 'w'), indent=1)
