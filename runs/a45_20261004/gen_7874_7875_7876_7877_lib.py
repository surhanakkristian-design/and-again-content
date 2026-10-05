import json, sys
def build(mid, level, kw, dv, taps, still, nouns, q, ans, av, notes, times):
    out_taps = []
    for phrase, target, voice, boxes in taps:
        keys = []
        for t, b in zip(times, boxes):
            if b is None: keys.append({"t": t, "off": True}); continue
            x0, y0, x1, y1 = b
            x0 = max(0, x0); y0 = max(0, y0); x1 = min(1, x1); y1 = min(1, y1)
            keys.append({"t": t, "x": round(x0, 2), "y": round(y0, 2), "w": round(x1 - x0, 2), "h": round(y1 - y0, 2)})
        out_taps.append({"phrase": phrase, "target": target, "voice": voice, "keys": keys})
    d = {"mediaId": mid, "level": level, "keyWord": kw, "defaultVoice": dv, "taps": out_taps, "stillS": still,
         "nouns": [{"word": w, "x": x, "y": y, "voice": v} for w, x, y, v in nouns],
         "question": q, "answer": ans.split(), "answerVoice": av, "notes": notes}
    json.dump(d, open(f"content/{mid}.json", "w"), indent=1, ensure_ascii=False)
