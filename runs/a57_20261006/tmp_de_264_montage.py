import sys,glob
from PIL import Image
lang=sys.argv[1]
for vid in sys.argv[2:]:
    fs=sorted(glob.glob(f'verify/{lang}/{vid}/box_*.jpg'))+[f'verify/{lang}/{vid}/slots.jpg']
    ims=[Image.open(f) for f in fs]
    h=900; ims=[i.resize((int(i.width*h/i.height),h)) for i in ims]
    W=sum(i.width for i in ims); m=Image.new('RGB',(W,h),'white'); x=0
    for i in ims: m.paste(i,(x,0)); x+=i.width
    m.save(f'tmp_de_264_mont_{lang}_{vid}.jpg',quality=85); print(vid, m.size)
