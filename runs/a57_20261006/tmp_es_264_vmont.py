import sys
from PIL import Image
for i in sys.argv[1:]:
    ims=[Image.open(f'verify/es/{i}/box_{n:02d}.jpg') for n in range(1,7)]
    w,h=ims[0].size; s=0.5
    W,H=int(w*s),int(h*s)
    M=Image.new('RGB',(W*3+Image.open(f'verify/es/{i}/slots.jpg').size[0],H*2),'white')
    for k,im in enumerate(ims):
        M.paste(im.resize((W,H)),((k%3)*W,(k//3)*H))
    M.paste(Image.open(f'verify/es/{i}/slots.jpg'),(W*3,0))
    M.save(f'tmp_es_264_vm_{i}.jpg',quality=85)
