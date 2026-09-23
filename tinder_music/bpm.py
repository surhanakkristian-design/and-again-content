"""Pure-Python tempo estimate: ffmpeg -> 8 kHz mono s16, onset-strength envelope (positive
energy flux, hop 128 = 16 ms), autocorrelation in 60-200 BPM, peak folded into 100-180."""
import subprocess,struct,sys,math
def bpm(path):
    raw=subprocess.run(["ffmpeg","-v","quiet","-i",path,"-ac","1","-ar","8000","-f","s16le","-"],capture_output=True).stdout
    n=len(raw)//2; s=struct.unpack("<%dh"%n,raw); H=128
    e=[sum(abs(x) for x in s[i:i+H]) for i in range(0,n-H,H)]
    le=[math.log1p(x) for x in e]
    o=[max(0.0,le[i]-le[i-1]) for i in range(1,len(le))]
    m=sum(o)/len(o); o=[x-m for x in o]
    fps=8000/H; best=None
    for b10 in range(600,2001,5):
        b=b10/10; lag=fps*60/b; L=int(lag); fr=lag-L
        acc=0.0
        for k in (1,2,4):
            l=L*k; 
            acc+=sum(o[i]*o[i+l] for i in range(0,len(o)-l,2))/k
        if best is None or acc>best[0]: best=(acc,b)
    b=best[1]
    while b<100: b*=2
    while b>185: b/=2
    return round(b), round(n/8000)
for f in sys.argv[1:]:
    print(f, *bpm(f))
