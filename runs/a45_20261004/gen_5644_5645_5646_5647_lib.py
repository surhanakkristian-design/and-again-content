import json, sys
T = [0.2, 0.7, 1.2, 1.7, 2.2, 2.7, 3.2, 3.7]
def keys(rows):
    out = []
    for t, r in zip(T, rows):
        if r is None: out.append({"t": t, "off": True})
        else:
            x, y, w, h = r
            x = max(0, x); y = max(0, y); w = min(w, 1 - x); h = min(h, 1 - y)
            out.append({"t": t, "x": round(x, 2), "y": round(y, 2), "w": round(w, 2), "h": round(h, 2)})
    return out
def write(mid, level, kw, dv, taps, still, nouns, q, ans, av, notes):
    c = {"mediaId": mid, "level": level, "keyWord": kw, "defaultVoice": dv,
         "taps": [{"phrase": p, "target": tg, "voice": v, "keys": keys(k)} for p, tg, v, k in taps],
         "stillS": still, "nouns": [{"word": w, "x": x, "y": y, "voice": v} for w, x, y, v in nouns],
         "question": q, "answer": ans.split(), "answerVoice": av, "notes": notes}
    json.dump(c, open(f"content/{mid}.json", "w"), indent=1, ensure_ascii=False)
