import glob
from PIL import Image
ims=[]
for i in [8,9,11,12,14]:
    fs=sorted(glob.glob(f'verify/fr/{i}/box_*.jpg')); 
    for f in [fs[0],fs[len(fs)//2],fs[-1],f'verify/fr/{i}/slots.jpg']:
        im=Image.open(f); im=im.resize((300,int(im.height*300/im.width))); ims.append(im)
h=max(x.height for x in ims); M=Image.new('RGB',(1200,h*5),'white')
for k,im in enumerate(ims): M.paste(im,((k%4)*300,(k//4)*h))
M.save('tmp_fr_8_chk.jpg',quality=80)
