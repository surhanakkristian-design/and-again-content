import sys,glob
from PIL import Image
for i in [275,276,279,280,281]:
    fs=sorted(glob.glob(f'verify/es/{i}/box_*.jpg'))+[f'verify/es/{i}/slots.jpg']
    ims=[Image.open(f) for f in fs]
    w,h=ims[0].size
    sc=480/w
    ims=[im.resize((int(im.size[0]*sc),int(im.size[1]*sc))) for im in ims]
    cols=4; rows=(len(ims)+cols-1)//cols
    H=max(im.size[1] for im in ims)
    out=Image.new('RGB',(cols*480,rows*H),'white')
    for k,im in enumerate(ims): out.paste(im,((k%cols)*480,(k//cols)*H))
    out.save(f'tmp_es_275_vmv_{i}.jpg',quality=85)
    print(i,w,h,len(ims),out.size)
