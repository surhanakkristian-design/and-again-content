import json, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
T = [0.2, 0.7, 1.2, 1.7, 2.2, 2.7, 3.2, 3.7]
def keys(rows):
    out = []
    for t, r in zip(T, rows):
        if r is None: out.append({"t": t, "off": True}); continue
        x, y, w, h = r
        w = min(w, round(1 - x, 2)); h = min(h, round(1 - y, 2))
        out.append({"t": t, "x": x, "y": y, "w": round(w, 2), "h": round(h, 2)})
    return out
def write(mid, level, kw, dv, taps, still, nouns, q, ans, av, notes):
    c = {"mediaId": mid, "level": level, "keyWord": kw, "defaultVoice": dv,
         "taps": [{"phrase": p, "target": tg, "voice": v, "keys": keys(k)} for p, tg, v, k in taps],
         "stillS": still, "nouns": [{"word": w, "x": x, "y": y, "voice": v} for w, x, y, v in nouns],
         "question": q, "answer": ans.split(" "), "answerVoice": av, "notes": notes}
    json.dump(c, open(f"{HERE}/content/{mid}.json", "w"), indent=1)
