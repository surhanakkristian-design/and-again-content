import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage as ndi
P='/Users/kristiansurhanak/Projects/and-again-content/runs/a48_20261005/pilot/'
src=Image.open(P+'out/bow7.png').convert('RGB')
a=np.asarray(src).astype(np.float64)
H,W,_=a.shape
mask=np.zeros((H,W),bool); excl=np.zeros((H,W),bool); core=np.zeros((H,W),bool)
# front-fender contour (float x of the fender's right edge per row)
ey=[1690,1706,1709,1713,1716,1718,1720,1740,1750,1756,1764,1775]; ex=[751.5,751.5,750.2,750.8,754.0,759.0,761.0,761.0,762.0,763.6,765.6,766.5]
xc=lambda y: float(np.interp(y,ey,ex))
for y in range(1690,1775):
    excl[y,:int(np.floor(xc(y)))]=True
for y in range(1699,1767):
    mask[y,int(np.floor(xc(y))):(801 if y<=1704 else 796)]=True
# sticker core (for feather): rough sticker extent
for y in range(1699,1764):
    core[y,int(np.floor(xc(y))):(800 if y<=1704 else 792)]=True
# lettering
for y in range(1666,1687):
    crease=813-(y-1676)*0.35
    mask[y,763:int(crease)-2]=True
    core[y,764:int(crease)-3]=True
excl[1660:1690,:761]=True
excl&=~mask
# Laplace fill (Jacobi with Neumann at excluded pixels)
y0,y1,x0,x1=1650,1785,730,840
sub=a[y0:y1,x0:x1].copy(); m=mask[y0:y1,x0:x1]; ex_=excl[y0:y1,x0:x1]
valid=~ex_
fill=sub.copy()
# init with mean of boundary
bd=ndi.binary_dilation(m)&~m&valid
fill[m]=sub[bd].mean(0)
for it in range(6000):
    acc=np.zeros_like(fill); cnt=np.zeros(m.shape)
    for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
        sh=np.roll(fill,(dy,dx),(0,1)); vv=np.roll(valid,(dy,dx),(0,1))
        acc+=sh*vv[...,None]; cnt+=vv
    new=acc/np.maximum(cnt,1)[...,None]
    fill[m]=new[m]
# grain: match residual statistics of nearby plastic
ref=sub[1700-y0:1760-y0,797-x0:830-x0]
res=ref-ndi.gaussian_filter(ref,(1.5,1.5,0))
sd=res.std((0,1))
rng=np.random.default_rng(7)
n=rng.normal(size=sub.shape)
n=ndi.gaussian_filter(n,(0.6,0.6,0))
n=n/n.std((0,1))*sd
# luminance-correlated grain (mostly shared across channels like the source)
lum=n.mean(2,keepdims=True)
n=0.7*lum/lum.std()*sd+0.3*n
fill[m]+=n[m]
# feather: alpha 1 on core dilated by 1, ramp to 0 at mask edge
c=ndi.binary_dilation(core[y0:y1,x0:x1],iterations=1)&m
d=ndi.distance_transform_edt(~c)
alpha=np.clip(1-(d/3.0),0,1)*m
alpha=ndi.gaussian_filter(alpha,0.7)*m
alpha[c]=1
out=sub*(1-alpha[...,None])+fill*alpha[...,None]
res_img=a.copy(); res_img[y0:y1,x0:x1]=out
for y in range(1699,1767):
    f=xc(y); x=int(np.floor(f)); c=f-x
    res_img[y,x]=c*a[y,x-1]+(1-c)*res_img[y,x]
res_img=np.clip(np.round(res_img),0,255).astype(np.uint8)
orig=np.asarray(src)
res_img[~mask]=orig[~mask]
Image.fromarray(res_img).save(P+'out/bow7_retouched.png')
np.save(P+'retouch/mask.npy',mask)
diff=(res_img.astype(int)!=orig.astype(int)).any(2)
ys,xs=np.nonzero(diff)
print('changed px',diff.sum(),'outside mask',(diff&~mask).sum(),'mask px',mask.sum(),'bbox',xs.min(),ys.min(),xs.max(),ys.max())
# before/after
bx=(700,1620,880,1800)
b=src.crop(bx).resize((540,540),Image.LANCZOS); r=Image.fromarray(res_img).crop(bx).resize((540,540),Image.LANCZOS)
ba=Image.new('RGB',(1090,540),'white'); ba.paste(b,(0,0)); ba.paste(r,(550,0)); ba.save(P+'retouch/before_after.jpg',quality=92)
Image.fromarray(res_img).crop((720,1640,840,1790)).resize((480,600),Image.NEAREST).save(P+'retouch/after_zoom4.png')
Image.fromarray(res_img).crop((600,1550,950,1900)).save(P+'retouch/after_1to1.png')
mk=Image.fromarray((mask*255).astype(np.uint8)).crop((720,1640,840,1790)).resize((480,600),Image.NEAREST); mk.save(P+'retouch/mask_zoom4.png')
