import json, sys
def K(times, rows):
    out = []
    for t, r in zip(times, rows):
        if r is None: out.append({"t": t, "off": True})
        else:
            x0, y0, x1, y1 = r
            x0, y0 = max(0, x0), max(0, y0); x1, y1 = min(1, x1), min(1, y1)
            out.append({"t": t, "x": round(x0, 2), "y": round(y0, 2), "w": round(x1 - x0, 2), "h": round(y1 - y0, 2)})
    return out
def write(mid, d):
    json.dump(d, open(f'content/{mid}.json', 'w'), indent=1, ensure_ascii=False)
