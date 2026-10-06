import sys,glob
from PIL import Image
for i in sys.argv[2:]:
    fs=sorted(glob.glob(f'verify/{sys.argv[1]}/{i}/box_*.jpg'))+[f'verify/{sys.argv[1]}/{i}/slots.jpg']
    ims=[Image.open(f) for f in fs]
    w=max(x.size[0] for x in ims);h=max(x.size[1] for x in ims)
    cols=len(ims);rows=1
    M=Image.new('RGB',(w*cols,h*rows),'white')
    for k,x in enumerate(ims):M.paste(x,((k%cols)*w,(k//cols)*h))
    M.thumbnail((2400,1400));M.save(f'tmp_es_198_mont_{sys.argv[1]}_{i}.jpg',quality=85)
