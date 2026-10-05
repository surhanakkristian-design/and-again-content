import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
T = [0.2, 0.7, 1.2, 1.7, 2.2, 2.7, 3.2, 3.7]
def keys(boxes):
    out = []
    for t, b in zip(T, boxes):
        if b is None: out.append({"t": t, "off": True})
        else: out.append({"t": t, "x": b[0], "y": b[1], "w": b[2], "h": b[3]})
    return out
def write(mid, level, kw, dv, taps, still, nouns, q, a, av, notes):
    d = {"mediaId": mid, "level": level, "keyWord": kw, "defaultVoice": dv,
         "taps": [{"phrase": p, "target": tg, "voice": v, "keys": keys(b)} for p, tg, v, b in taps],
         "stillS": still,
         "nouns": [{"word": w, "x": x, "y": y, "voice": v} for w, x, y, v in nouns],
         "question": q, "answer": a.split(), "answerVoice": av, "notes": notes}
    json.dump(d, open(f"{HERE}/content/{mid}.json", "w"), indent=1)
