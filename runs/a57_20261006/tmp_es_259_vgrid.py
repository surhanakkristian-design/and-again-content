from PIL import Image;import glob,sys
for i in [259,260,261,262,263]:
    fs=sorted(glob.glob(f'verify/es/{i}/box_*.jpg'))
    n=len(fs);cols=min(4,n);rows=(n+cols-1)//cols
    W,H=453,787
    m=Image.new('RGB',(cols*W,rows*H),'white')
    for k,f in enumerate(fs):
        m.paste(Image.open(f).resize((W,H)),((k%cols)*W,(k//cols)*H))
    m.save(f'tmp_es_259_vgrid_{i}.jpg',quality=85)
