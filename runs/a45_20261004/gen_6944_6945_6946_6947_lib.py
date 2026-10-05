import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def r2(v): return round(v + 1e-9, 2)
def keys(times, boxes):
    out = []
    for t, b in zip(times, boxes):
        if b is None: out.append({"t": t, "off": True}); continue
        x, y, x2, y2 = b
        x, y = max(0, x), max(0, y); x2, y2 = min(1, x2), min(1, y2)
        out.append({"t": t, "x": r2(x), "y": r2(y), "w": r2(x2 - x), "h": r2(y2 - y)})
    return out
def write(mid, level, kw, dv, taps, still, nouns, q, ans, av, notes):
    times = json.load(open(f'{HERE}/frames/{mid}/packet.json'))['times']
    c = {"mediaId": mid, "level": level, "keyWord": kw, "defaultVoice": dv,
         "taps": [{"phrase": p, "target": tg, "voice": v, "keys": keys(times, b)} for p, tg, v, b in taps],
         "stillS": still, "nouns": [{"word": w, "x": x, "y": y, "voice": v} for w, x, y, v in nouns],
         "question": q, "answer": ans.split(), "answerVoice": av, "notes": notes}
    json.dump(c, open(f'{HERE}/content/{mid}.json', 'w'), indent=1)
