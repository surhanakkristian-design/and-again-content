import sys,glob
from PIL import Image
lang=sys.argv[1]
for vid in sys.argv[2:]:
    fs=sorted(glob.glob(f'verify/{lang}/{vid}/box_*.jpg'))+[f'verify/{lang}/{vid}/slots.jpg']
    ims=[Image.open(f) for f in fs]
    h=760; ims=[i.resize((int(i.width*h/i.height),h)) for i in ims]
    rows=[ims[:5],ims[5:]] if len(ims)>5 else [ims]
    W=max(sum(i.width for i in r) for r in rows); m=Image.new('RGB',(W,h*len(rows)),'white')
    for ri,r in enumerate(rows):
        x=0
        for i in r: m.paste(i,(x,ri*h)); x+=i.width
    m.save(f'tmp_de_269_mont_{lang}_{vid}.jpg',quality=85)
