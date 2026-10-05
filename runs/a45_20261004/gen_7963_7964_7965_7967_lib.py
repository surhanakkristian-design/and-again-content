import json, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
def build(mid, level, kw, dv, taps, still, nouns, q, ans, av, notes):
    times = json.load(open(f'{HERE}/frames/{mid}/packet.json'))['times']
    out = []
    for phrase, target, voice, boxes in taps:
        keys = []
        for t, b in zip(times, boxes):
            if b is None: keys.append({"t": t, "off": True})
            else:
                x0, y0, x1, y1 = b
                x0 = max(0, round(x0, 2)); y0 = max(0, round(y0, 2)); x1 = min(1, round(x1, 2)); y1 = min(1, round(y1, 2))
                keys.append({"t": t, "x": x0, "y": y0, "w": round(x1 - x0, 2), "h": round(y1 - y0, 2)})
        out.append({"phrase": phrase, "target": target, "voice": voice, "keys": keys})
    c = {"mediaId": mid, "level": level, "keyWord": kw, "defaultVoice": dv, "taps": out, "stillS": still,
         "nouns": [{"word": w, "x": x, "y": y, "voice": v} for w, x, y, v in nouns],
         "question": q, "answer": ans.split(" "), "answerVoice": av, "notes": notes}
    json.dump(c, open(f'{HERE}/content/{mid}.json', 'w'), indent=1, ensure_ascii=False)
