import sys,glob
from PIL import Image
lang=sys.argv[1]
for i in sys.argv[2:]:
    fs=sorted(glob.glob(f'verify/{lang}/{i}/box_*.jpg'))+[f'verify/{lang}/{i}/slots.jpg']
    ims=[Image.open(f) for f in fs]
    w,h=ims[0].size
    cols=6; tw=1800//cols; th=int(h*tw/w)
    rows=(len(ims)+cols-1)//cols
    M=Image.new('RGB',(cols*tw,rows*th),'white')
    for k,im in enumerate(ims):
        M.paste(im.resize((tw,th)),((k%cols)*tw,(k//cols)*th))
    M.save(f'tmp_fr_300_m_{lang}_{i}.jpg',quality=85)
    print(i,len(ims),M.size)
