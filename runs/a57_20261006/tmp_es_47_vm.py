import sys,glob
from PIL import Image
for i in [47,48,49,50,51]:
    fs=sorted(glob.glob(f'verify/es/{i}/box_*.jpg'))+[f'verify/es/{i}/slots.jpg']
    ims=[Image.open(f) for f in fs]
    h=900
    ims=[im.resize((int(im.width*h/im.height),h)) for im in ims]
    per=5 if len(ims)>8 else 4
    rows=[ims[k:k+per] for k in range(0,len(ims),per)]
    W=max(sum(im.width for im in r) for r in rows)
    out=Image.new('RGB',(W,h*len(rows)),'white')
    for ri,r in enumerate(rows):
        x=0
        for im in r: out.paste(im,(x,ri*h)); x+=im.width
    out.save(f'tmp_es_47_vm_{i}.jpg',quality=85)
    print(i,out.size,Image.open(fs[0]).size)
