import sys,glob
from PIL import Image
for vid in sys.argv[1:]:
    fs=sorted(glob.glob(f'verify/en/{vid}/box_*.jpg'))+[f'verify/en/{vid}/slots.jpg']
    ims=[Image.open(f) for f in fs]
    h=700; ims=[i.resize((int(i.width*h/i.height),h)) for i in ims]
    W=sum(i.width for i in ims); m=Image.new('RGB',(W,h),'white'); x=0
    for i in ims: m.paste(i,(x,0)); x+=i.width
    m.save(f'tmp_de_773_mont_{vid}.jpg',quality=85)
