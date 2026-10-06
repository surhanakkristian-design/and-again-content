import sys,glob
from PIL import Image
lang=sys.argv[1]
for i in sys.argv[2:]:
    fs=sorted(glob.glob(f'verify/{lang}/{i}/box_*.jpg'))+[f'verify/{lang}/{i}/slots.jpg']
    ims=[Image.open(f) for f in fs]
    h=900
    ims=[im.resize((int(im.width*h/im.height),h)) for im in ims]
    cols=4
    rows=(len(ims)+cols-1)//cols
    W=max(sum(im.width for im in ims[r*cols:(r+1)*cols]) for r in range(rows))
    out=Image.new('RGB',(W,h*rows),'white')
    for k,im in enumerate(ims):
        r,c=divmod(k,cols); x=sum(m.width for m in ims[r*cols:r*cols+c]); out.paste(im,(x,r*h))
    out.thumbnail((2000,2000)); out.save(f'tmp_es_587_m{lang}_{i}.jpg',quality=85)
    print(i,[ (Image.open(f).size) for f in fs][:2])
