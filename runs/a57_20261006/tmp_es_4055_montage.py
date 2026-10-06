import sys,glob
from PIL import Image
for i in sys.argv[2:]:
    fs=sorted(glob.glob(f'verify/{sys.argv[1]}/{i}/box_*.jpg'))+[f'verify/{sys.argv[1]}/{i}/slots.jpg']
    ims=[Image.open(f) for f in fs]
    w=max(x.size[0] for x in ims);h=max(x.size[1] for x in ims)
    cols=5;rows=(len(ims)+cols-1)//cols
    M=Image.new('RGB',(w*cols,h*rows),'white')
    for k,x in enumerate(ims):M.paste(x,((k%cols)*w,(k//cols)*h))
    M.thumbnail((2400,2400*rows));M.save(f'tmp_es_{i}_mont_{sys.argv[1]}.jpg',quality=85)
