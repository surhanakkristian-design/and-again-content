import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def box(x0, y0, x1, y1):
    x0, y0 = max(0, x0), max(0, y0); x1, y1 = min(1, x1), min(1, y1)
    return dict(x=round(x0, 2), y=round(y0, 2), w=round(x1 - x0, 2), h=round(y1 - y0, 2))
def keys(times, spec):
    out = []
    for t in times:
        b = spec(t) if callable(spec) else spec
        out.append({'t': t, 'off': True} if b is None else dict(t=t, **box(*b)))
    return out
def write(vid, d):
    json.dump(d, open(f'{HERE}/content/{vid}.json', 'w'), indent=1, ensure_ascii=False)
