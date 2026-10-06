import sys,glob
from PIL import Image
lang=sys.argv[1]
for i in sys.argv[2:]:
    fs=sorted(glob.glob(f'verify/{lang}/{i}/box_*.jpg'))
    ims=[Image.open(f) for f in fs]
    s=0.5; tw,th=int(ims[0].size[0]*s),int(ims[0].size[1]*s)
    cols=3; rows=(len(ims)+cols-1)//cols
    M=Image.new('RGB',(cols*tw,rows*th),'white')
    for k,im in enumerate(ims): M.paste(im.resize((tw,th)),((k%cols)*tw,(k//cols)*th))
    M.save(f'tmp_fr_289_m_{lang}_{i}.jpg',quality=80)
