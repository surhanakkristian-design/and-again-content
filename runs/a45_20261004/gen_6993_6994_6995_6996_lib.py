import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def build(mid, level, kw, dv, times, taps, still, nouns, q, ans, av, notes):
    out = {"mediaId": mid, "level": level, "keyWord": kw, "defaultVoice": dv, "taps": [], "stillS": still,
           "nouns": [{"word": w, "x": x, "y": y, "voice": v} for w, x, y, v in nouns],
           "question": q, "answer": ans.split(), "answerVoice": av, "notes": notes}
    for phrase, target, voice, boxes in taps:
        keys = []
        for t, b in zip(times, boxes):
            if b is None: keys.append({"t": t, "off": True})
            else:
                x, y, w, h = b
                w = min(w, round(1 - x, 2)); h = min(h, round(1 - y, 2))
                keys.append({"t": t, "x": x, "y": y, "w": round(w, 2), "h": round(h, 2)})
        out["taps"].append({"phrase": phrase, "target": target, "voice": voice, "keys": keys})
    json.dump(out, open(f"{HERE}/content/{mid}.json", "w"), indent=1, ensure_ascii=False)
