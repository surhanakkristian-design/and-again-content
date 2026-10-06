import sys,glob
from PIL import Image
for i in sys.argv[1:]:
    fs=sorted(glob.glob(f'verify/es/{i}/box_*.jpg'))+[f'verify/es/{i}/slots.jpg']
    ims=[Image.open(f) for f in fs]
    w=420; ims=[im.resize((w,int(im.height*w/im.width))) for im in ims]
    cols=min(5,len(ims)); rows=(len(ims)+cols-1)//cols; h=max(im.height for im in ims)
    M=Image.new('RGB',(cols*w,rows*h),'white')
    for k,im in enumerate(ims): M.paste(im,((k%cols)*w,(k//cols)*h))
    M.save(f'tmp_es_221_vm_{i}.jpg',quality=85)
