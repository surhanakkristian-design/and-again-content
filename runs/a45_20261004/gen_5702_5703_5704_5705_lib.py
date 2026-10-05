import json, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
def K(rows):
    out = []
    for r in rows:
        if r[1] is None: out.append({"t": r[0], "off": True})
        else:
            t, x, y, w, h = r
            x = max(0, round(x, 2)); y = max(0, round(y, 2))
            w = round(min(w, 1 - x), 2); h = round(min(h, 1 - y), 2)
            out.append({"t": t, "x": x, "y": y, "w": w, "h": h})
    return out
def write(mid, level, kw, dv, taps, still, nouns, q, ans, av, notes):
    c = {"mediaId": mid, "level": level, "keyWord": kw, "defaultVoice": dv,
         "taps": [{"phrase": p, "target": t, "voice": v, "keys": K(k)} for p, t, v, k in taps],
         "stillS": still, "nouns": [{"word": w, "x": x, "y": y, "voice": v} for w, x, y, v in nouns],
         "question": q, "answer": ans.split(" "), "answerVoice": av, "notes": notes}
    json.dump(c, open(f"{HERE}/content/{mid}.json", "w"), indent=1, ensure_ascii=False)
