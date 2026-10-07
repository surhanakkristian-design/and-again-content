# A61: a second, motion-aware cut signal per frame (decoded at 72x128 grey + 3 colour histograms):
#   d[k]  = mean |frame k - frame k-1| (0..255)
#   h[k]  = histogram distance (0..1) between k-1 and k (16 bins per RGB channel, half L1)
#   r[k]  = d[k] / (median of d in k-4..k+4 without k, floor 0.5): a cut stands out from the motion around it
import json, subprocess, sys, numpy as np
W, H = 72, 128
def series(src):
    p = subprocess.run(['ffmpeg', '-v', 'error', '-nostdin', '-i', src, '-an', '-vf', f'scale={W}:{H}', '-vsync', '0', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True, timeout=300)
    a = np.frombuffer(p.stdout, np.uint8)
    n = a.size // (W * H * 3)
    f = a[: n * W * H * 3].reshape(n, H, W, 3).astype(np.float32)
    g = f.mean(axis=3)
    d = np.zeros(n); h = np.zeros(n)
    hist = np.stack([np.concatenate([np.histogram(f[i, :, :, c], 16, (0, 256))[0] for c in range(3)]) for i in range(n)]) / (W * H)
    for k in range(1, n):
        d[k] = np.abs(g[k] - g[k - 1]).mean()
        h[k] = np.abs(hist[k] - hist[k - 1]).sum() / 6
    r = np.zeros(n)
    for k in range(1, n):
        nb = [d[j] for j in range(max(1, k - 4), min(n, k + 5)) if j != k]
        r[k] = d[k] / max(0.5, float(np.median(nb))) if nb else 0
    return d, h, r
if __name__ == '__main__':
    d, h, r = series(sys.argv[1])
    top = np.argsort(-r)[:5]
    print([(int(k), round(float(r[k]), 1), round(float(d[k]), 1), round(float(h[k]), 3)) for k in top])
