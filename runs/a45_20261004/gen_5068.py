import sys; sys.path.insert(0,'.')
from gen_5065_5066_5068_5070_lib import write
# split x per time between bride (left) and groom (right): (split, bride_y, groom_y, bride_x0, groom_x1)
S={0.0:(.5,.29,.21),0.5:(.5,.29,.2),1.0:(.5,.3,.21),1.5:(.5,.3,.2),2.0:(.46,.29,.2),2.5:(.5,.29,.19),3.0:(.5,.3,.21),
 3.5:(.5,.3,.21),4.0:(.5,.3,.2),4.5:(.5,.3,.2),5.0:(.38,.24,.08),5.5:(.33,.24,.09),6.0:(.59,.22,.06),6.5:(.45,.3,.24),
 7.0:(.48,.32,.25),7.5:(.47,.33,.25),8.0:(.48,.34,.26),8.5:(.48,.35,.27),9.0:(.48,.36,.28),9.5:(.47,.36,.28),
 10.0:(.44,.36,.29),10.5:(.46,.36,.28),11.0:(.5,.36,.29),11.5:(.5,.29,.28),12.0:(.46,.27,.29)}
bride={};groom={}
for t,(s,by,gy) in S.items():
    bride[t]=(0,by,s,round(1-by,2)); groom[t]=(s,gy,round(1-s,2),round(1-gy,2))
write(5068,{"mediaId":5068,"level":"A","keyWord":"bride","defaultVoice":"female",
"taps":[
 {"phrase":"to wear a long veil","target":"the bride","voice":"female","box":bride},
 {"phrase":"to kiss the bride","target":"the groom","voice":"male","box":dict(groom)},
 {"phrase":"to lift her veil","target":"the groom","voice":"male","box":dict(groom)}],
"stillS":0.0,
"nouns":[{"word":"roses","x":0.3,"y":0.08,"voice":"female"},{"word":"the sea","x":0.45,"y":0.41,"voice":"female"},
 {"word":"a bride","x":0.15,"y":0.7,"voice":"female"},{"word":"sand","x":0.52,"y":0.88,"voice":"female"}],
"question":"What are the bride and groom doing?",
"answer":["They","are","kissing","on","the","beach."],
"answerVoice":"female",
"notes":"Bride (left) and groom (right) stand close all the time: boxes split along a vertical line between them; at 5.0-6.0 his arms reach over her (veil lift, then hug), so his arms on her side and her hand at the bottom fall outside the boxes. Guests clap in the background (8.0-11.0) but are not a target. 'to lift her veil' = 5.0-5.5 only; 'to kiss the bride' = 6.5-10.0."})
