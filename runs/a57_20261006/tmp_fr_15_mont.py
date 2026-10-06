import sys,glob
from PIL import Image
lang=sys.argv[1]
for i in sys.argv[2:]:
    fs=sorted(glob.glob(f'verify/{lang}/{i}/box_*.jpg'))+[f'verify/{lang}/{i}/slots.jpg']
    ims=[Image.open(f) for f in fs]
    w=450; ims=[im.resize((w,int(im.height*w/im.width))) for im in ims]
    cols=4; rows=(len(ims)+cols-1)//cols
    h=max(im.height for im in ims)
    M=Image.new('RGB',(cols*w,rows*h),'white')
    for k,im in enumerate(ims): M.paste(im,((k%cols)*w,(k//cols)*h))
    M.save(f'tmp_fr_15_m_{lang}_{i}.jpg',quality=85)
