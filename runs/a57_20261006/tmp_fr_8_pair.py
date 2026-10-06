import sys,glob
from PIL import Image
lang=sys.argv[1]
for i in sys.argv[2:]:
    fs=sorted(glob.glob(f'verify/{lang}/{i}/box_*.jpg'))+[f'verify/{lang}/{i}/slots.jpg']
    ims=[Image.open(f) for f in fs]
    ims=[im.resize((im.width//2,im.height//2)) for im in ims]
    for k in range(0,len(ims),3):
        g=ims[k:k+3]; W=sum(x.width for x in g); H=max(x.height for x in g)
        M=Image.new('RGB',(W,H),'white'); x=0
        for im in g: M.paste(im,(x,0)); x+=im.width
        M.save(f'tmp_fr_8_p_{lang}_{i}_{k//3}.jpg',quality=80)
