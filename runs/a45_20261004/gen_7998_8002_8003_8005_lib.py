import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
T = [0.2, 0.7, 1.2, 1.7, 2.2, 2.7, 3.2, 3.7]
def keys(boxes):
    out = []
    for t, b in zip(T, boxes):
        if b is None: out.append({"t": t, "off": True})
        else:
            x, y, w, h = b
            w = min(w, round(1 - x, 2)); h = min(h, round(1 - y, 2))
            out.append({"t": t, "x": x, "y": y, "w": round(w, 2), "h": round(h, 2)})
    return out
def write(mid, d):
    for tap in d["taps"]:
        tap["keys"] = keys(tap.pop("boxes"))
    d = {"mediaId": mid, **d}
    json.dump(d, open(f"{HERE}/content/{mid}.json", "w"), indent=1)
