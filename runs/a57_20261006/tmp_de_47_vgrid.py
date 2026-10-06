import sys,glob
from PIL import Image
lang=sys.argv[1]
for vid in sys.argv[2:]:
    fs=sorted(glob.glob(f'verify/{lang}/{vid}/box_*.jpg'))+[f'verify/{lang}/{vid}/slots.jpg']
    ims=[Image.open(f) for f in fs]
    w=420; ims=[i.resize((w,int(i.height*w/i.width))) for i in ims]
    cols=4; rows=(len(ims)+cols-1)//cols; h=max(i.height for i in ims)
    m=Image.new('RGB',(w*cols,h*rows),'white')
    for k,i in enumerate(ims): m.paste(i,((k%cols)*w,(k//cols)*h))
    m.save(f'tmp_de_47_vgrid_{vid}.jpg',quality=88); print(vid,m.size)
