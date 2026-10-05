import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def keys(times, rows):
    out = []
    for t, r in zip(times, rows):
        if r is None: out.append({"t": t, "off": True})
        else:
            x, y, w, h = r; out.append({"t": t, "x": x, "y": y, "w": w, "h": h})
    return out
def write(mid, level, kw, dv, taps, still, nouns, q, ans, av, notes):
    times = json.load(open(f'{HERE}/frames/{mid}/packet.json'))['times']
    c = {"mediaId": mid, "level": level, "keyWord": kw, "defaultVoice": dv,
         "taps": [{"phrase": p, "target": tg, "voice": v, "keys": keys(times, rows)} for p, tg, v, rows in taps],
         "stillS": still,
         "nouns": [{"word": w, "x": x, "y": y, "voice": v} for w, x, y, v in nouns],
         "question": q, "answer": ans, "answerVoice": av, "notes": notes}
    json.dump(c, open(f'{HERE}/content/{mid}.json', 'w'), indent=1, ensure_ascii=False)
