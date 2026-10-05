import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
T = [0.2, 0.7, 1.2, 1.7, 2.2, 2.7, 3.2, 3.7]
def keys(boxes):
    out = []
    for t, b in zip(T, boxes):
        if b is None: out.append({"t": t, "off": True})
        else:
            x, y, x2, y2 = b
            out.append({"t": t, "x": round(x, 2), "y": round(y, 2), "w": round(x2 - x, 2), "h": round(y2 - y, 2)})
    return out
def write(c):
    json.dump(c, open(f"{HERE}/content/{c['mediaId']}.json", "w"), indent=1)
