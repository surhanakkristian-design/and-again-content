import sys,glob,os
from PIL import Image
lang=sys.argv[1]
for i in sys.argv[2:]:
    fs=sorted(glob.glob(f'verify/{lang}/{i}/box_*.jpg'))+[f'verify/{lang}/{i}/slots.jpg']
    ims=[Image.open(f) for f in fs]
    h=900
    ims=[im.resize((int(im.width*h/im.height),h)) for im in ims]
    cols=4
    rows=(len(ims)+cols-1)//cols
    w=max(im.width for im in ims)
    M=Image.new('RGB',(w*cols,h*rows),'white')
    for k,im in enumerate(ims):
        M.paste(im,((k%cols)*w,(k//cols)*h))
    M.save(f'tmp_es_275_m_{lang}_{i}.jpg',quality=85)
    print(i,len(ims),M.size)
