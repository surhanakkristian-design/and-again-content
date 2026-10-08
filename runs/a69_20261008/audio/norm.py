# A69: level the lab's sounds. Voices -> -19 LUFS (the median of the 116 recordings; only files more than 0.5 LU off are
# re-encoded), the two feedback sounds -> -22 LUFS measured while they sound (looped), 3 LU under the voices.
# True peak at most -1.0 dBTP (a limiter only where the gain would push past it). Iterates the gain until within 0.2 LU.
import subprocess, sys, csv, re, pathlib
VOICE_T, FEED_T, TP = -19.0, -22.0, -1.0
def measure(path, loop=False):
    cmd = ['ffmpeg', '-nostats', '-hide_banner'] + (['-stream_loop', '19'] if loop else []) + ['-i', str(path), '-af', 'ebur128=peak=true', '-f', 'null', '-']
    out = subprocess.run(cmd, capture_output=True, text=True).stderr
    out = out[out.rfind('Summary'):]
    return float(re.search(r'I:\s+(-?[\d.]+)', out).group(1)), float(re.search(r'Peak:\s+(-?[\d.]+)', out).group(1))
def render(src, dst, gain, codec):
    af = f'volume={gain:.2f}dB,alimiter=limit={10 ** ((TP - 0.3) / 20):.4f}:attack=1:release=30:level=disabled'
    enc = ['-c:a', 'aac', '-b:a', '96k', '-movflags', '+faststart'] if codec == 'aac' else ['-c:a', 'libmp3lame', '-b:a', '160k']
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', str(src), '-af', af, '-ar', '44100'] + enc + [str(dst)], check=True)
rows = []
for line in open('before.tsv'):
    name, I, tp, _ = line.rstrip('\n').split('\t')
    feed = name.endswith('answer.mp3')
    target = FEED_T if feed else VOICE_T
    I0, tp0 = measure(f'orig/{name}', loop=feed)
    if not feed and abs(I0 - target) <= 0.5:
        rows.append((name, I0, tp0, I0, tp0, 'kept')); continue
    dst = pathlib.Path('norm') / (name.replace('-answer', '-answer-lab') if feed else name.replace('.m4a', '_a69.m4a'))
    gain = target - I0
    for _ in range(4):
        render(f'orig/{name}', dst, gain, 'mp3' if feed else 'aac')
        I1, tp1 = measure(dst, loop=feed)
        if abs(I1 - target) <= 0.2: break
        gain += target - I1
    rows.append((name, I0, tp0, I1, tp1, dst.name))
with open('levels.tsv', 'w') as f:
    f.write('file\tLUFS before\tdBTP before\tLUFS after\tdBTP after\tnew file\n')
    for r in rows: f.write('\t'.join(str(x) for x in r) + '\n')
print(sum(1 for r in rows if r[5] != 'kept'), 'rendered')
