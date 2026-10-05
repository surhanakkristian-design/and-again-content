import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def K(t, b):
    if b is None: return {"t": t, "off": True}
    x0,y0,x1,y1 = [max(0.0,min(1.0,v)) for v in b]
    return {"t": t, "x": round(x0,2), "y": round(y0,2), "w": round(x1-x0,2), "h": round(y1-y0,2)}
def build(mid, level, kw, dv, taps, still, nouns, q, ans, av, notes, times):
    out = {"mediaId": mid, "level": level, "keyWord": kw, "defaultVoice": dv, "taps": [], "stillS": still,
           "nouns": [{"word": w, "x": x, "y": y, "voice": v} for w,x,y,v in nouns],
           "question": q, "answer": ans.split(), "answerVoice": av, "notes": notes}
    for phrase, target, voice, boxes in taps:
        out["taps"].append({"phrase": phrase, "target": target, "voice": voice,
                            "keys": [K(t, b) for t, b in zip(times, boxes)]})
    json.dump(out, open(f"{HERE}/content/{mid}.json", "w"), indent=1, ensure_ascii=False)
