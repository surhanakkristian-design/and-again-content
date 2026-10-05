import json
times=[i*0.5 for i in range(24)]
L={0.0:(.25,.34,.42,.36),0.5:(.25,.33,.46,.39),1.0:(.21,.34,.50,.43),1.5:(.20,.30,.53,.50),2.0:(.18,.26,.55,.54),2.5:(.18,.25,.55,.55),
3.0:(.17,.28,.56,.52),3.5:(.18,.28,.55,.52),4.0:(.17,.25,.56,.55),4.5:(.17,.29,.36,.51),
10.0:(.18,.36,.32,.44),10.5:(.14,.24,.59,.56),11.0:(.17,.20,.57,.60),11.5:(.13,.25,.60,.55)}
D={}
for t in times:
    if t<=4.0: D[t]=(.73,.08,.18,.72)
    elif t==4.5: D[t]=(.53,.08,.31,.42)
    elif t<=9.5: D[t]=(.19,.07,.62,.72)
    elif t==10.0: D[t]=(.50,.08,.32,.71)
    elif t==11.0: D[t]=(.74,.08,.18,.71)
    else: D[t]=(.73,.08,.18,.71)
R={t:(.05,.80,.90,.12) for t in times}
def keys(m):
    out=[]
    for t in times:
        if t in m:
            x,y,w,h=m[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
c={"mediaId":4224,"level":"A","keyWord":"toilet","defaultVoice":"female",
"taps":[{"phrase":"to go to the toilet","target":"the lizard","voice":"female","keys":keys(L)},
{"phrase":"to open and close","target":"the door","voice":"female","keys":keys(D)},
{"phrase":"to lie on the floor","target":"the rug","voice":"female","keys":keys(R)}],
"stillS":11.5,
"nouns":[{"word":"a lizard","x":.46,"y":.52,"voice":"female"},{"word":"a door","x":.72,"y":.18,"voice":"female"},
{"word":"a rug","x":.76,"y":.86,"voice":"female"},{"word":"a plant","x":.12,"y":.60,"voice":"female"}],
"question":"Where is the lizard going?",
"answer":["The","lizard","is","going","to","the","toilet."],
"answerVoice":"female",
"notes":"Key word toilet is only shown through the WC sign on the door; the lizard walks in through that door (0-4.5 s) and comes out slim. Where the lizard overlaps the open door the boxes are split on a vertical line (x 0.72-0.74), so the lizard's right hand at 10.5-11.5 s is slightly cut; at 4.5 s the tail lies outside the lizard box. The lizard's feet stand on the rug at 10.5-11.5 s, split at y 0.80."}
json.dump(c,open("content/4224.json","w"),indent=1,ensure_ascii=False)
