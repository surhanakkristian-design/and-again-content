import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def K(times, boxes):
    out = []
    for t in times:
        b = boxes.get(t)
        if b is None: out.append({"t": t, "off": True})
        else:
            x, y, w, h = b
            x = max(0.0, x); y = max(0.0, y); w = min(w, 1 - x); h = min(h, 1 - y)
            out.append({"t": t, "x": round(x, 2), "y": round(y, 2), "w": round(w, 2), "h": round(h, 2)})
    return out
def write(mid, level, key, dv, taps, still, nouns, q, ans, av, notes):
    times = json.load(open(f'{HERE}/frames/{mid}/packet.json'))['times']
    T = []
    for ph, tg, v, boxes in taps:
        T.append({"phrase": ph, "target": tg, "voice": v, "keys": K(times, boxes)})
    c = {"mediaId": mid, "level": level, "keyWord": key, "defaultVoice": dv, "taps": T, "stillS": still,
         "nouns": [{"word": w, "x": x, "y": y, "voice": v} for w, x, y, v in nouns],
         "question": q, "answer": ans.split(' '), "answerVoice": av, "notes": notes}
    json.dump(c, open(f'{HERE}/content/{mid}.json', 'w'), indent=1, ensure_ascii=False)
