import json, sys
RUN = '/Users/kristiansurhanak/Projects/and-again-content/runs/a45_20261004'
def K(rows):
    out = []
    for r in rows:
        if len(r) == 1 or r[1] is None:
            out.append({"t": float(r[0]), "off": True})
        else:
            t, x, y, w, h = r
            x = max(0.0, round(x, 2)); y = max(0.0, round(y, 2))
            w = round(min(w, 1 - x), 2); h = round(min(h, 1 - y), 2)
            out.append({"t": float(t), "x": x, "y": y, "w": w, "h": h})
    return out
def write(d):
    with open(f"{RUN}/content/{d['mediaId']}.json", "w") as f:
        json.dump(d, f, indent=1, ensure_ascii=False)
