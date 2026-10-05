import json, sys
def build(mid, level, kw, dv, times, taps, stillS, nouns, q, ans, av, notes):
    out = {"mediaId": mid, "level": level, "keyWord": kw, "defaultVoice": dv, "taps": [], "stillS": stillS,
           "nouns": [{"word": w, "x": x, "y": y, "voice": v} for w, x, y, v in nouns],
           "question": q, "answer": ans.split(" "), "answerVoice": av, "notes": notes}
    for phrase, target, voice, boxes in taps:
        keys = []
        for t, b in zip(times, boxes):
            keys.append({"t": t, "off": True} if b is None else {"t": t, "x": b[0], "y": b[1], "w": b[2], "h": b[3]})
        out["taps"].append({"phrase": phrase, "target": target, "voice": voice, "keys": keys})
    json.dump(out, open(f"content/{mid}.json", "w"), indent=1, ensure_ascii=False)
