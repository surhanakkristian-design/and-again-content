import sys,glob
from PIL import Image
lang,i=sys.argv[1],sys.argv[2]
fs=sorted(glob.glob(f'verify/{lang}/{i}/box_*.jpg'))
ims=[Image.open(f) for f in fs]
s=0.5
ims=[im.resize((int(im.width*s),int(im.height*s))) for im in ims]
per=3
for k in range(0,len(ims),per):
    g=ims[k:k+per]
    W=sum(x.width for x in g)+5*(len(g)-1); H=max(x.height for x in g)
    out=Image.new('RGB',(W,H),'white'); x=0
    for im in g: out.paste(im,(x,0)); x+=im.width+5
    out.save(f'tmp_es_4190_vm_{i}_{k//per}.jpg',quality=85)
    print(f'tmp_es_4190_vm_{i}_{k//per}.jpg')
