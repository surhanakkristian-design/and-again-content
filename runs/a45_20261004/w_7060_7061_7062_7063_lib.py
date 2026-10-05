import json, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
def keys(times, boxes):
    out = []
    for t, b in zip(times, boxes):
        if b is None: out.append({"t": t, "off": True}); continue
        x0, y0, x1, y1 = b
        x0 = max(0, x0); y0 = max(0, y0); x1 = min(1, x1); y1 = min(1, y1)
        out.append({"t": t, "x": round(x0, 2), "y": round(y0, 2), "w": round(x1 - x0, 2), "h": round(y1 - y0, 2)})
    return out
def write(vid, level, kw, dv, taps, still, nouns, q, ans, av, notes):
    times = json.load(open(f'{HERE}/frames/{vid}/packet.json'))['times']
    c = {"mediaId": vid, "level": level, "keyWord": kw, "defaultVoice": dv,
         "taps": [{"phrase": p, "target": tg, "voice": v, "keys": keys(times, bx)} for p, tg, v, bx in taps],
         "stillS": still, "nouns": [{"word": w, "x": x, "y": y, "voice": v} for w, x, y, v in nouns],
         "question": q, "answer": ans.split(), "answerVoice": av, "notes": notes}
    json.dump(c, open(f'{HERE}/content/{vid}.json', 'w'), indent=1, ensure_ascii=False)
