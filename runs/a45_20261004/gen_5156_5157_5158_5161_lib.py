import json, sys
def build(mid, level, kw, dv, taps, still, nouns, q, ans, av, notes, times):
    out_taps = []
    for phrase, target, voice, boxes in taps:
        keys = []
        for t in times:
            b = boxes.get(t)
            if b is None: keys.append({"t": t, "off": True})
            else:
                x, y, w, h = b
                x = max(0, round(x, 2)); y = max(0, round(y, 2))
                w = round(min(w, 1 - x), 2); h = round(min(h, 1 - y), 2)
                keys.append({"t": t, "x": x, "y": y, "w": w, "h": h})
        out_taps.append({"phrase": phrase, "target": target, "voice": voice, "keys": keys})
    c = {"mediaId": mid, "level": level, "keyWord": kw, "defaultVoice": dv, "taps": out_taps, "stillS": still,
         "nouns": [{"word": w, "x": x, "y": y, "voice": v} for w, x, y, v in nouns],
         "question": q, "answer": ans, "answerVoice": av, "notes": notes}
    json.dump(c, open(f"content/{mid}.json", "w"), indent=1)
