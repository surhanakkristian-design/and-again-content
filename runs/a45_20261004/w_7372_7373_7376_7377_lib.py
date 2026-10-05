import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def keys(times, boxes):
    out = []
    for t, b in zip(times, boxes):
        if b is None: out.append({"t": t, "off": True})
        else:
            x, y, w, h = b
            x = max(0, x); y = max(0, y); w = min(w, 1 - x); h = min(h, 1 - y)
            out.append({"t": t, "x": round(x, 2), "y": round(y, 2), "w": round(w, 2), "h": round(h, 2)})
    return out
def write(mid, level, kw, dv, taps, still, nouns, q, ans, av, notes):
    times = json.load(open(f'{HERE}/frames/{mid}/packet.json'))['times']
    d = {"mediaId": mid, "level": level, "keyWord": kw, "defaultVoice": dv,
         "taps": [{"phrase": p, "target": tg, "voice": v, "keys": keys(times, bx)} for p, tg, v, bx in taps],
         "stillS": still, "nouns": [{"word": w, "x": x, "y": y, "voice": v} for w, x, y, v in nouns],
         "question": q, "answer": ans.split(" "), "answerVoice": av, "notes": notes}
    json.dump(d, open(f'{HERE}/content/{mid}.json', 'w'), indent=1)
