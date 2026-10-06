import sys,glob
from PIL import Image
lang=sys.argv[1]
for i in sys.argv[2:]:
    fs=sorted(glob.glob(f'verify/{lang}/{i}/box_*.jpg'))+[f'verify/{lang}/{i}/slots.jpg']
    ims=[Image.open(f) for f in fs]
    w=ims[0].size[0]; h=max(im.size[1] for im in ims)
    s=min(1.0,1800/(4*w))
    tw=int(w*s); th=int(h*s)
    cols=4; rows=(len(ims)+cols-1)//cols
    M=Image.new('RGB',(cols*tw,rows*th),'white')
    for k,im in enumerate(ims):
        M.paste(im.resize((tw,int(im.size[1]*tw/im.size[0]))),((k%cols)*tw,(k//cols)*th))
    M.save(f'tmp_fr_240_m_{lang}_{i}.jpg',quality=85)
    print(i,ims[0].size,M.size)
