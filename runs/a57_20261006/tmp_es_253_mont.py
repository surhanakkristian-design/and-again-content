import sys,glob
from PIL import Image
for i in sys.argv[1:]:
    fs=sorted(glob.glob(f'verify/en/{i}/box_*.jpg'))+[f'verify/en/{i}/slots.jpg']
    ims=[Image.open(f) for f in fs]
    print(i,[im.size for im in ims][:2])
    w=ims[0].size[0]; h=ims[0].size[1]
    s=min(1.0,1800/(4*w))
    tw,th=int(w*s),int(h*s)
    cols=4; rows=(len(ims)+cols-1)//cols
    M=Image.new('RGB',(cols*tw,rows*th),'white')
    for k,im in enumerate(ims):
        M.paste(im.resize((tw,int(im.size[1]*tw/im.size[0]))),((k%cols)*tw,(k//cols)*th))
    M.save(f'tmp_es_253_m{i}.jpg',quality=85)
