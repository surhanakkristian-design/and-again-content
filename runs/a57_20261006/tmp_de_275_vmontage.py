import sys,glob
from PIL import Image
for i in sys.argv[1:]:
    fs=sorted(glob.glob(f"verify/de/{i}/box_*.jpg"))
    ims=[Image.open(f) for f in fs]
    w,h=ims[0].size; s=min(1.0,560/w); W,H=int(w*s),int(h*s)
    cols=min(4,len(ims)); rows=(len(ims)+cols-1)//cols
    m=Image.new("RGB",(W*cols,H*rows),"white")
    for k,im in enumerate(ims): m.paste(im.resize((W,H)),((k%cols)*W,(k//cols)*H))
    m.save(f"tmp_de_275_vm_{i}.jpg",quality=85); print(i,len(ims),m.size)
