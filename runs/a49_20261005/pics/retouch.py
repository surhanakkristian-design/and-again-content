# A49: free local retouch of a small leftover (letter, badge, sticker) - clone stamp: the box is replaced by the nearby
# patch whose surrounding ring matches best, blended with a feathered edge. Only pixels inside the box (+ 6 px feather) change.
#   python3 retouch.py <in.png> <out.png> x0,y0,x1,y1 [x0,y0,x1,y1 ...]
import sys
import numpy as np
from PIL import Image
src, dst, boxes = sys.argv[1], sys.argv[2], [tuple(map(int, b.split(','))) for b in sys.argv[3:]]
a = np.asarray(Image.open(src).convert('RGB')).astype(np.float64); H, W, _ = a.shape; out = a.copy(); changed = 0
for x0, y0, x1, y1 in boxes:
    F = 6; r = 10; w, h = x1 - x0, y1 - y0
    X0, Y0, X1, Y1 = max(0, x0 - r), max(0, y0 - r), min(W, x1 + r), min(H, y1 + r)
    ring = np.ones((Y1 - Y0, X1 - X0), bool); ring[y0 - Y0:y1 - Y0, x0 - X0:x1 - X0] = False
    target = a[Y0:Y1, X0:X1]; best = None
    for dy in range(-3 * h, 3 * h + 1, max(1, h // 4)):
        for dx in range(-3 * w, 3 * w + 1, max(1, w // 4)):
            if abs(dx) < w + r and abs(dy) < h + r: continue
            sy0, sx0 = Y0 + dy, X0 + dx
            if sy0 < 0 or sx0 < 0 or sy0 + (Y1 - Y0) > H or sx0 + (X1 - X0) > W: continue
            cand = a[sy0:sy0 + (Y1 - Y0), sx0:sx0 + (X1 - X0)]
            d = ((cand - target) ** 2)[ring].mean()
            if best is None or d < best[0]: best = (d, cand)
    patch = best[1]
    m = np.zeros((Y1 - Y0, X1 - X0)); yy, xx = np.mgrid[Y0:Y1, X0:X1]
    dist = np.minimum.reduce([xx - (x0 - F), (x1 + F) - xx, yy - (y0 - F), (y1 + F) - yy]).astype(float)
    m = np.clip(dist / F, 0, 1)[..., None]
    out[Y0:Y1, X0:X1] = m * patch + (1 - m) * out[Y0:Y1, X0:X1]
    changed += int((np.abs(out - a).sum(axis=2) > 0).sum())
Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(dst); print(dst, 'pixels changed', changed)
