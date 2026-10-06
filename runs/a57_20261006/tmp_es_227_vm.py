import sys,glob
from PIL import Image
for i in sys.argv[1:]:
    fs=sorted(glob.glob(f'verify/es/{i}/box_*.jpg'))+[f'verify/es/{i}/slots.jpg']
    ims=[Image.open(f) for f in fs]
    w=ims[0].size[0]
    s=min(1.0,2400/(3*w)); tw=int(w*s)
    hs=[int(im.size[1]*tw/im.size[0]) for im in ims]
    cols=3; rows=(len(ims)+cols-1)//cols
    th=max(hs)
    M=Image.new('RGB',(cols*tw,rows*th),'white')
    for k,im in enumerate(ims):
        M.paste(im.resize((tw,hs[k])),((k%cols)*tw,(k//cols)*th))
    M.save(f'tmp_es_227_vm_{i}.jpg',quality=85); print(i,M.size,[im.size for im in ims])
