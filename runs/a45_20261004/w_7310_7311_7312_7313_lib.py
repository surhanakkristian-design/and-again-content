import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def build(mid, level, kw, dv, taps, still, nouns, q, ans, av, notes):
    times = json.load(open(f'{HERE}/frames/{mid}/packet.json'))['times']
    out = {"mediaId": mid, "level": level, "keyWord": kw, "defaultVoice": dv, "taps": []}
    for phrase, target, voice, boxes in taps:
        keys = []
        for t, b in zip(times, boxes):
            keys.append({"t": t, "off": True} if b is None else {"t": t, "x": b[0], "y": b[1], "w": b[2], "h": b[3]})
        assert len(boxes) == len(times)
        out["taps"].append({"phrase": phrase, "target": target, "voice": voice, "keys": keys})
    out["stillS"] = still
    out["nouns"] = [{"word": w, "x": x, "y": y, "voice": v} for w, x, y, v in nouns]
    out["question"] = q; out["answer"] = ans.split(); out["answerVoice"] = av; out["notes"] = notes
    json.dump(out, open(f'{HERE}/content/{mid}.json', 'w'), indent=1, ensure_ascii=False)
