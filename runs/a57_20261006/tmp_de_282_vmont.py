import sys
from PIL import Image
for i in sys.argv[1:]:
    ims=[Image.open(f'verify/de/{i}/box_0{k}.jpg') for k in range(1,7)]+[Image.open(f'verify/de/{i}/slots.jpg')]
    w,h=453,787
    M=Image.new('RGB',(w*4,h*2),'white')
    for n,im in enumerate(ims):
        M.paste(im.resize((w,h)),((n%4)*w,(n//4)*h))
    M.save(f'tmp_de_282_vmont_{i}.jpg',quality=88)
