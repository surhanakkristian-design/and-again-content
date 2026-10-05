# writer helper for 7365 7367 7368 7370: boxes given as [x0,y0,x1,y1] per time, None = off
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def keys(times, boxes):
    out = []
    for t, b in zip(times, boxes):
        if b is None: out.append({"t": t, "off": True}); continue
        x0, y0, x1, y1 = [max(0.0, min(1.0, v)) for v in b]
        out.append({"t": t, "x": round(x0, 2), "y": round(y0, 2), "w": round(x1 - x0, 2), "h": round(y1 - y0, 2)})
    return out
def write(mid, level, kw, dv, taps, still, nouns, q, ans, av, notes=""):
    times = json.load(open(f"{HERE}/frames/{mid}/info.json"))["times"]
    T = []
    for phrase, target, voice, boxes in taps:
        T.append({"phrase": phrase, "target": target, "voice": voice, "keys": keys(times, boxes)})
    c = {"mediaId": mid, "level": level, "keyWord": kw, "defaultVoice": dv, "taps": T, "stillS": still,
         "nouns": [{"word": w, "x": x, "y": y, "voice": v} for w, x, y, v in nouns],
         "question": q, "answer": ans.split(), "answerVoice": av, "notes": notes}
    json.dump(c, open(f"{HERE}/content/{mid}.json", "w"), indent=1, ensure_ascii=False)
