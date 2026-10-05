import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def keys(times, boxes):
    out = []
    for t in times:
        b = boxes.get(t)
        if b is None: out.append({"t": t, "off": True})
        else:
            x, y, w, h = b
            x = max(0, round(x, 2)); y = max(0, round(y, 2))
            w = round(min(w, 1 - x), 2); h = round(min(h, 1 - y), 2)
            out.append({"t": t, "x": x, "y": y, "w": w, "h": h})
    return out
def write(mid, d):
    times = json.load(open(f'{HERE}/frames/{mid}/packet.json'))['times']
    for tap in d['taps']:
        tap['keys'] = keys(times, tap.pop('boxes'))
    json.dump(d, open(f'{HERE}/content/{mid}.json', 'w'), indent=1, ensure_ascii=False)
