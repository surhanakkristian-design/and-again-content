import sys,glob
from PIL import Image
for vid in sys.argv[1:]:
    fs=sorted(glob.glob(f'verify/en/{vid}/box_*.jpg'))+[f'verify/en/{vid}/slots.jpg']
    ims=[Image.open(f) for f in fs]
    w=360; ims=[i.resize((w,int(i.height*w/i.width))) for i in ims]
    h=max(i.height for i in ims); cols=5; rows=(len(ims)+cols-1)//cols
    M=Image.new('RGB',(cols*w,rows*h),'white')
    for k,i in enumerate(ims): M.paste(i,((k%cols)*w,(k//cols)*h))
    M.save(f'tmp_de_27_mont_{vid}.jpg',quality=80)
