import sys,glob
from PIL import Image
for i in [233,235,237,238,239]:
    fs=sorted(glob.glob(f'verify/de/{i}/box_*.jpg'))+[f'verify/de/{i}/slots.jpg']
    ims=[Image.open(f) for f in fs]
    w,h=453,787
    M=Image.new('RGB',(w*len(ims),h),'white')
    for k,im in enumerate(ims): M.paste(im.resize((w,h)),(k*w,0))
    M.save(f'tmp_de_233_vmont_{i}.jpg',quality=85)
