# helper for 7131/7132/7134/7136
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def K(times, boxes):
    out = []
    for t, b in zip(times, boxes):
        if b is None: out.append({"t": t, "off": True})
        else:
            x, y, w, h = b
            w = min(w, round(1 - x, 2)); h = min(h, round(1 - y, 2))
            out.append({"t": t, "x": x, "y": y, "w": round(w, 2), "h": round(h, 2)})
    return out
def write(mid, level, kw, dv, taps, still, nouns, q, ans, av, notes):
    times = json.load(open(f'{HERE}/frames/{mid}/packet.json'))['times']
    c = {"mediaId": mid, "level": level, "keyWord": kw, "defaultVoice": dv,
         "taps": [{"phrase": p, "target": tg, "voice": v, "keys": K(times, bx)} for p, tg, v, bx in taps],
         "stillS": still, "nouns": [{"word": w, "x": x, "y": y, "voice": vv} for w, x, y, vv in nouns],
         "question": q, "answer": ans.split(' '), "answerVoice": av, "notes": notes}
    json.dump(c, open(f'{HERE}/content/{mid}.json', 'w'), indent=1, ensure_ascii=False)
