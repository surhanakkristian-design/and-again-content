import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def keys(times, boxes):
    out = []
    for t in times:
        b = boxes.get(t)
        if b is None: out.append({"t": t, "off": True}); continue
        x, y, x2, y2 = b
        x, y = max(0, x), max(0, y); x2, y2 = min(1, x2), min(1, y2)
        out.append({"t": t, "x": round(x, 2), "y": round(y, 2), "w": round(x2 - x, 2), "h": round(y2 - y, 2)})
    return out
def write(vid, d):
    json.dump(d, open(f"{HERE}/content/{vid}.json", "w"), indent=1, ensure_ascii=False)
def times(vid):
    return json.load(open(f"{HERE}/frames/{vid}/packet.json"))["times"]
