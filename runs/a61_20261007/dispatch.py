# A61: python3 dispatch.py <dir> <batches> [size=40] -> new batch lists <dir>/b_<n>.txt from finished pictures not yet in a batch
import glob, os, sys
D, k = sys.argv[1], int(sys.argv[2]); size = int(sys.argv[3]) if len(sys.argv) > 3 else 40
done = set()
for f in glob.glob(f'{D}/b_*.txt'): done |= set(open(f).read().split())
pics = sorted(p for p in glob.glob(f'{os.path.abspath(D)}/*.jpg') if p not in done and time_ok(p)) if False else sorted(p for p in glob.glob(f'{os.path.abspath(D)}/*.jpg') if p not in done)
n0 = len(glob.glob(f'{D}/b_*.txt'))
made = []
for j in range(k):
    ch = pics[j * size:(j + 1) * size]
    if not ch: break
    open(f'{D}/b_{n0 + j}.txt', 'w').write('\n'.join(ch) + '\n'); made.append(n0 + j)
print(' '.join(map(str, made)))
