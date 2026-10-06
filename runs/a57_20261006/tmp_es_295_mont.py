import sys,glob
from PIL import Image
lang=sys.argv[1]
for i in sys.argv[2:]:
    fs=sorted(glob.glob(f'verify/{lang}/{i}/box_*.jpg'))+[f'verify/{lang}/{i}/slots.jpg']
    ims=[Image.open(f) for f in fs]
    w,h=ims[0].size
    s=min(1.0,1800/(4*w)); tw,th=int(w*s),int(h*s)
    cols=4; rows=(len(ims)+cols-1)//cols
    M=Image.new('RGB',(cols*tw,rows*th),'white')
    for k,im in enumerate(ims):
        M.paste(im.resize((tw,int(im.size[1]*tw/im.size[0]))),((k%cols)*tw,(k//cols)*th))
    M.save(f'tmp_es_295_m_{lang}_{i}.jpg',quality=85)
