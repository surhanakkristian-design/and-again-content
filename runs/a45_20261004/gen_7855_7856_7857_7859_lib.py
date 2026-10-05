import json, sys
def build(mid, level, kw, dv, taps, still, nouns, q, ans, av, notes, times):
    out = []
    for phrase, target, voice, boxes in taps:
        keys = []
        for t, b in zip(times, boxes):
            if b is None: keys.append({"t": t, "off": True})
            else: keys.append({"t": t, "x": b[0], "y": b[1], "w": b[2], "h": b[3]})
        out.append({"phrase": phrase, "target": target, "voice": voice, "keys": keys})
    c = {"mediaId": mid, "level": level, "keyWord": kw, "defaultVoice": dv, "taps": out, "stillS": still,
         "nouns": [{"word": w, "x": x, "y": y, "voice": v} for w, x, y, v in nouns],
         "question": q, "answer": ans.split(), "answerVoice": av, "notes": notes}
    json.dump(c, open(f"content/{mid}.json", "w"), indent=1)
