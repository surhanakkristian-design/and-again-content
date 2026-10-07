"""usage: python3 draw60.py <name>  -> verify/<name>_boxes.jpg, verify/<name>_slots.jpg"""
import sys, json, os
from PIL import Image, ImageDraw, ImageFont
R=os.path.dirname(os.path.abspath(__file__)); n=sys.argv[1]
j=json.load(open(f"{R}/content/{n}.json"))
im=Image.open(f"{R}/pics/{n}.png").convert("RGB"); H=900; W=round(im.width*H/im.height); im=im.resize((W,H))
try: F=ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc",16)
except Exception: F=ImageFont.load_default()
def zones(d):
    cx=0.055*W; d.line([(cx,0),(cx,H)],fill=(255,255,255),width=1); d.line([(W-cx,0),(W-cx,H)],fill=(255,255,255),width=1)
    d.line([(0,0.82*H),(W,0.82*H)],fill=(255,255,255),width=1)
    d.rectangle([0.86*W,0.40*H,W,0.75*H],outline=(200,200,200),width=1)
a=im.copy(); d=ImageDraw.Draw(a); zones(d)
for t,c in zip(j["taps"],[(255,0,0),(0,220,0),(0,90,255)]):
    b=t["box"]; d.rectangle([b["x"]*W,b["y"]*H,(b["x"]+b["w"])*W-1,(b["y"]+b["h"])*H-1],outline=c,width=4)
    d.text((b["x"]*W+6,b["y"]*H+6),t["phrase"],fill=c,font=F,stroke_width=2,stroke_fill=(0,0,0))
a.save(f"{R}/verify/{n}_boxes.jpg",quality=88)
s=im.copy(); d=ImageDraw.Draw(s); zones(d)
for nn in j["nouns"]:
    x,y=nn["x"]*W,nn["y"]*H; w,h=0.30*W,0.05*H
    d.rounded_rectangle([x-w/2,y-h/2,x+w/2,y+h/2],radius=h/2,fill=(255,255,255),outline=(0,0,0),width=2)
    d.text((x,y),nn["word"],fill=(0,0,0),font=F,anchor="mm")
    d.ellipse([x-3,y-3,x+3,y+3],fill=(255,0,0))
s.save(f"{R}/verify/{n}_slots.jpg",quality=88)
