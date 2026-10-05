import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def keys(rows):
    out = []
    for r in rows:
        if r[1] is None: out.append({"t": r[0], "off": True})
        else:
            t, x, y, w, h = r
            x = max(0, round(x, 2)); y = max(0, round(y, 2))
            w = round(min(w, 1 - x), 2); h = round(min(h, 1 - y), 2)
            out.append({"t": t, "x": x, "y": y, "w": w, "h": h})
    return out
def write(mid, d):
    json.dump(d, open(f'{HERE}/content/{mid}.json', 'w'), indent=1, ensure_ascii=False)
