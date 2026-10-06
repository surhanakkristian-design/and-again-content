import sys,glob
from PIL import Image
i=sys.argv[1]
fs=sorted(glob.glob(f'verify/en/{i}/box_*.jpg'))
ims=[Image.open(f) for f in fs]
w,h=ims[0].size
for k in range(0,len(ims),3):
  m=Image.new('RGB',(w*3,h),'white')
  for j,im in enumerate(ims[k:k+3]): m.paste(im,(j*w,0))
  m=m.resize((w*3*2//3,h*2//3)); m.save(f'tmp_es_13_mont_{i}_{k//3}.jpg')
print(len(ims))
