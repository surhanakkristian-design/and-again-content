import json, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
T = [0.2, 0.7, 1.2, 1.7, 2.2, 2.7, 3.2, 3.7]
def keys(boxes):
    out = []
    for t, b in zip(T, boxes):
        if b is None: out.append({"t": t, "off": True})
        else:
            x, y, w, h = b
            out.append({"t": t, "x": round(x, 2), "y": round(y, 2), "w": round(w, 2), "h": round(h, 2)})
    return out
def write(c):
    json.dump(c, open(f"{HERE}/content/{c['mediaId']}.json", "w"), indent=1, ensure_ascii=False)
