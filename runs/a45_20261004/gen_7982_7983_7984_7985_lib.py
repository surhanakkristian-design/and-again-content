import json, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
def K(times, boxes):
    out = []
    for t, b in zip(times, boxes):
        if b is None: out.append({"t": t, "off": True})
        else:
            x, y, w, h = b
            out.append({"t": t, "x": round(x,2), "y": round(y,2), "w": round(w,2), "h": round(h,2)})
    return out
def write(mid, level, kw, dv, taps, still, nouns, q, ans, av, notes):
    times = json.load(open(f'{HERE}/frames/{mid}/packet.json'))['times']
    c = {"mediaId": mid, "level": level, "keyWord": kw, "defaultVoice": dv,
         "taps": [{"phrase": p, "target": tg, "voice": v, "keys": K(times, b)} for p, tg, v, b in taps],
         "stillS": still, "nouns": [{"word": w, "x": x, "y": y, "voice": v} for w, x, y, v in nouns],
         "question": q, "answer": ans.split(' '), "answerVoice": av, "notes": notes}
    json.dump(c, open(f'{HERE}/content/{mid}.json', 'w'), indent=1, ensure_ascii=False)
