import sys,glob
from PIL import Image
for i in sys.argv[1:]:
    fs=sorted(glob.glob(f'verify/de/{i}/box_*.jpg'))
    ims=[Image.open(f) for f in fs]
    s=0.45; w,h=int(906*s),int(1574*s)
    cols=min(4,len(ims)); rows=(len(ims)+cols-1)//cols
    M=Image.new('RGB',(cols*w,rows*h),'white')
    for k,im in enumerate(ims): M.paste(im.resize((w,h)),((k%cols)*w,(k//cols)*h))
    M.save(f'tmp_de_259_vm_{i}.jpg',quality=85); print(i,len(ims),M.size)
