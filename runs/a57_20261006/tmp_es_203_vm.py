import sys,glob
from PIL import Image
for i in sys.argv[1:]:
    fs=sorted(glob.glob(f'verify/es/{i}/box_*.jpg'))
    ims=[Image.open(f).resize((453,787)) for f in fs]+[Image.open(f'verify/es/{i}/slots.jpg')]
    M=Image.new('RGB',(453*4,787*2),'white')
    for k,x in enumerate(ims):M.paste(x,((k%4)*453,(k//4)*787))
    M.save(f'tmp_es_203_vm_{i}.jpg',quality=85)
