import sys,glob
from PIL import Image
for i in sys.argv[1:]:
    fs=sorted(glob.glob(f'verify/es/{i}/box_*.jpg'))
    ims=[Image.open(f) for f in fs]
    w,h=ims[0].size
    cols=3; rows=(len(ims)+cols-1)//cols
    M=Image.new('RGB',(w*cols,h*rows),'white')
    for k,im in enumerate(ims): M.paste(im,((k%cols)*w,(k//cols)*h))
    M.thumbnail((1800,2400)); M.save(f'tmp_es_289_vm_{i}.jpg',quality=85)
