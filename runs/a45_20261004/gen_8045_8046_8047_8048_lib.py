import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def keys(times, boxes):
    out = []
    for t, b in zip(times, boxes):
        if b is None: out.append({"t": t, "off": True})
        else:
            x, y, w, h = b
            x = max(0, round(x, 2)); y = max(0, round(y, 2))
            w = round(min(w, 1 - x), 2); h = round(min(h, 1 - y), 2)
            out.append({"t": t, "x": x, "y": y, "w": w, "h": h})
    return out
def write(mid, level, kw, dv, taps, still, nouns, q, ans, av, notes):
    times = json.load(open(f'{HERE}/frames/{mid}/packet.json'))['times']
    c = {"mediaId": mid, "level": level, "keyWord": kw, "defaultVoice": dv,
         "taps": [{"phrase": p, "target": tg, "voice": v, "keys": keys(times, b)} for p, tg, v, b in taps],
         "stillS": still, "nouns": [{"word": w, "x": x, "y": y, "voice": v} for w, x, y, v in nouns],
         "question": q, "answer": ans.split(" "), "answerVoice": av, "notes": notes}
    json.dump(c, open(f'{HERE}/content/{mid}.json', 'w'), indent=1, ensure_ascii=False)
