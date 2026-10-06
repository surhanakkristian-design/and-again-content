import sys,glob
from PIL import Image
lang=sys.argv[1]
for i in [int(a) for a in sys.argv[2:]] or [27,28,29,32,33]:
    fs=sorted(glob.glob(f'verify/{lang}/{i}/box_*.jpg'))+[f'verify/{lang}/{i}/slots.jpg']
    ims=[Image.open(f) for f in fs]
    w,h=ims[0].size
    cols=5; rows=(len(ims)+cols-1)//cols
    s=0.45
    W,H=int(w*s),int(h*s)
    m=Image.new('RGB',(W*cols,H*rows),'white')
    for k,im in enumerate(ims):
        m.paste(im.resize((W,H)),((k%cols)*W,(k//cols)*H))
    m.save(f'tmp_fr_27_m_{lang}_{i}.jpg',quality=85)
    print(i,len(ims),w,h,m.size)
