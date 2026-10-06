import sys,glob
from PIL import Image
for i in sys.argv[1:]:
    fs=sorted(glob.glob(f'verify/es/{i}/box_*.jpg'))+[f'verify/es/{i}/slots.jpg']
    ims=[Image.open(f) for f in fs]
    w,h=ims[0].size
    cols=min(4,len(ims)); tw=min(w,1900//cols); th=max(int(im.size[1]*tw/im.size[0]) for im in ims)
    rows=(len(ims)+cols-1)//cols
    M=Image.new('RGB',(cols*tw,rows*th),'white')
    for k,im in enumerate(ims):
        M.paste(im.resize((tw,int(im.size[1]*tw/im.size[0]))),((k%cols)*tw,(k//cols)*th))
    M.save(f'tmp_es_233_vm_{i}.jpg',quality=85); print(i,M.size,ims[0].size)
