import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
T = [0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def keys(L):
    out = []
    for t, b in zip(T, L):
        if b is None: out.append({"t": t, "off": True})
        else:
            x, y, w, h = b
            x = max(0, round(x, 2)); y = max(0, round(y, 2))
            w = round(min(w, 1 - x), 2); h = round(min(h, 1 - y), 2)
            out.append({"t": t, "x": x, "y": y, "w": w, "h": h})
    return out
def write(vid, c):
    for tp in c["taps"]: tp["keys"] = keys(tp["keys"])
    json.dump(c, open(f"{HERE}/content/{vid}.json", "w"), indent=1)
