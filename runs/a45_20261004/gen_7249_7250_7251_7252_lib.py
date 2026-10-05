import json, sys
def build(mid, level, kw, dv, taps, still, nouns, q, ans, av, notes, times):
    out = {"mediaId": mid, "level": level, "keyWord": kw, "defaultVoice": dv, "taps": [], "stillS": still,
           "nouns": [dict(word=w, x=x, y=y, voice=v) for (w, x, y, v) in nouns],
           "question": q, "answer": ans.split(" "), "answerVoice": av, "notes": notes}
    for phrase, target, voice, boxes in taps:
        keys = []
        for t, b in zip(times, boxes):
            if b is None: keys.append({"t": t, "off": True})
            else:
                x, y, w, h = b; keys.append({"t": t, "x": x, "y": y, "w": w, "h": h})
        out["taps"].append({"phrase": phrase, "target": target, "voice": voice, "keys": keys})
    json.dump(out, open(f"content/{mid}.json", "w"), indent=1, ensure_ascii=False)
