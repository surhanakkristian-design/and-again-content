import sys,glob
from PIL import Image
for vid in sys.argv[1:]:
    fs=sorted(glob.glob(f'verify/de/{vid}/box_*.jpg'))+[f'verify/de/{vid}/slots.jpg']
    ims=[Image.open(f) for f in fs]
    w=480; ims=[i.resize((w,int(i.height*w/i.width))) for i in ims]
    h=max(i.height for i in ims); cols=5; rows=(len(ims)+cols-1)//cols
    M=Image.new('RGB',(cols*w,rows*h),'white')
    for k,i in enumerate(ims): M.paste(i,((k%cols)*w,(k//cols)*h))
    M.save(f'tmp_de_27_vmont_{vid}.jpg',quality=85)
