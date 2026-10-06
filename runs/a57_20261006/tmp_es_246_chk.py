from PIL import Image
ids=[246,248,250,251,252]
ims=[]
for i in ids:
    ims.append(Image.open(f'verify/es/{i}/slots.jpg')); ims.append(Image.open(f'verify/es/{i}/box_03.jpg'))
tw=360
th=max(int(im.size[1]*tw/im.size[0]) for im in ims)
M=Image.new('RGB',(5*tw,2*th),'white')
for k,im in enumerate(ims):
    M.paste(im.resize((tw,int(im.size[1]*tw/im.size[0]))),((k//2)*tw,(k%2)*th))
M.save('tmp_es_246_chk.jpg',quality=85)
