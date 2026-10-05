import json
def T(n=31): return [round(i*0.5,1) for i in range(n)]
def keys(d, times):
    out=[]
    for t in times:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=v
            out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(w,2),"h":round(h,2)})
    return out
def save(o):
    json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# ---------- 4091
t=T()
wom={0.0:(.27,.07,.44,.51),0.5:(.25,.06,.45,.53),1.0:(.26,.05,.48,.56),1.5:(.26,.05,.49,.57),2.0:(.27,.06,.48,.56),
     2.5:(.25,.08,.46,.52),3.0:(.29,.17,.44,.40),3.5:(.30,.16,.45,.38),4.0:(.29,.10,.46,.40),
     4.5:(.19,0,.81,1),5.0:(.45,0,.55,1),5.5:(.45,0,.55,1),6.0:(.45,0,.55,1),6.5:(.45,0,.55,1),
     7.0:(.50,0,.50,1),7.5:(.50,0,.50,1),8.0:(.50,0,.50,1),8.5:(.50,0,.50,1),9.0:(.50,0,.50,1),9.5:(.50,0,.50,1),
     14.5:(.15,0,.45,.15),15.0:(.17,0,.45,.22)}
ice={}
for k,v in wom.items():
    x,y,w,h=v
    if k<=4.0: ice[k]=(0,round(y+h+.01,2),1,round(1-(y+h+.01),2))
    elif k<=9.5: ice[k]=(0,0,x,1)
    else: ice[k]=(0,round(y+h,2),1,round(1-(y+h),2))
for k in [10.0,10.5,11.0,11.5,12.0,12.5,13.0,13.5,14.0]: ice[k]=(0,0,1,1)
kw=keys(wom,t); ki=keys(ice,t)
save({"mediaId":4091,"level":"B","keyWord":"crack","defaultVoice":"female",
 "taps":[{"phrase":"to crouch on the frozen lake","target":"the woman","voice":"female","keys":kw},
         {"phrase":"to pour out steaming tea","target":"the woman","voice":"female","keys":kw},
         {"phrase":"to crack in every direction","target":"the ice","voice":"female","keys":ki}],
 "stillS":9.0,
 "nouns":[{"word":"a beanie","x":.80,"y":.06,"voice":"female"},{"word":"sunglasses","x":.80,"y":.19,"voice":"female"},
          {"word":"a flask","x":.78,"y":.44,"voice":"female"},{"word":"steam","x":.46,"y":.34,"voice":"female"}],
 "question":"What is happening to the ice?",
 "answer":["The","ice","is","cracking","in","every","direction."],
 "answerVoice":"female",
 "notes":"The ice is everywhere around the woman; its box is the strip below her (0-4 s), the left part beside her and the flask (4.5-9.5 s), the whole top-down picture (10-14 s). The flask and her hands are inside the woman's box. From 10 s only her reflection shows (off) until the boots enter at 14.5 s. New cracks only appear from 12 s; old ridges are visible from the start."})

# ---------- 4092
sunc={}
for k in t: sunc[k]=(.23,.14)
for k in [8.0,8.5,9.0,9.5,10.0,10.5,11.0,11.5]: sunc[k]=(.22,.14)
sunc.update({12.0:(.21,.15),12.5:(.21,.17),13.0:(.22,.19),13.5:(.23,.21),14.0:(.24,.22),14.5:(.25,.23),15.0:(.25,.25)})
sun={k:(max(0,c[0]-.15),c[1]-.10,.30,.20) for k,c in sunc.items()}
bike={k:(0,.64,1,.36) for k in t}
for k in [13.0,13.5,14.0,14.5,15.0]: bike[k]=(0,.58,1,.42)
steps={k:(.18,.40,.66,.24) for k in t if k<=11.5}
steps[12.0]=(.20,.48,.66,.16)
save({"mediaId":4092,"level":"A","keyWord":"down","defaultVoice":"female",
 "taps":[{"phrase":"to go down the steps","target":"the bike","voice":"female","keys":keys(bike,t)},
         {"phrase":"to shine over the sea","target":"the sun","voice":"female","keys":keys(sun,t)},
         {"phrase":"to lead to the sea","target":"the steps","voice":"female","keys":keys(steps,t)}],
 "stillS":4.0,
 "nouns":[{"word":"the sun","x":.23,"y":.14,"voice":"female"},{"word":"the sea","x":.30,"y":.33,"voice":"female"},
          {"word":"steps","x":.52,"y":.53,"voice":"female"},{"word":"a bike","x":.50,"y":.83,"voice":"female"}],
 "question":"Where is the bike going?",
 "answer":["The","bike","is","going","down","the","steps."],
 "answerVoice":"female",
 "notes":"Helmet-camera view: only the rider's arms show, gender not certain, so defaultVoice follows evenId (female). The bike box holds the handlebars and the rider's arms. The steps box is the stretch of steps above the handlebars; off from 12.5 s when the steps end. From 13 s the bike rolls on the flat path (box kept, the bike is still visible)."})

# ---------- 4093
t3=T(30)
ext={0.5:(.03,.10),1.0:(.08,.20),1.5:(.10,.23),2.0:(.14,.30),2.5:(.20,.33),3.0:(.23,.41),3.5:(.27,.43),4.0:(.30,.44),4.5:(.33,.47),
 5.0:(.37,.49),5.5:(.40,.51),6.0:(.43,.53),6.5:(.46,.55),7.0:(.50,.57),7.5:(.52,.59),8.0:(.55,.61),8.5:(.58,.63),9.0:(.60,.65),
 9.5:(.63,.66),10.0:(.66,.68),10.5:(.68,.70),11.0:(.70,.72),11.5:(.71,.74),12.0:(.74,.76),12.5:(.75,.77),13.0:(.77,.79),
 13.5:(.78,.81),14.0:(.80,.83),14.5:(.82,.85)}
moon={k:(0,0,max(.18,v[0]+.04),max(.14,v[1]+.04)) for k,v in ext.items()}
km=keys(moon,t3)
save({"mediaId":4093,"level":"B","keyWord":"round","defaultVoice":"male",
 "taps":[{"phrase":"to grow steadily larger","target":"the moon","voice":"male","keys":km},
         {"phrase":"to glow against the darkness","target":"the moon","voice":"male","keys":km},
         {"phrase":"to reveal its craters","target":"the moon","voice":"male","keys":km}],
 "stillS":14.5,
 "nouns":[{"word":"the moon","x":.30,"y":.45,"voice":"male"},{"word":"craters","x":.63,"y":.80,"voice":"male"},
          {"word":"the sky","x":.60,"y":.93,"voice":"male"}],
 "question":"What is the moon doing?",
 "answer":["The","round","moon","is","glowing","against","the","darkness."],
 "answerVoice":"male",
 "notes":"Only one possible target (the moon), used for all three phrases; the stars are single pixels. The moon is not in the picture at 0.0 s (off). 'craters' is placed on the row of craters at the lower edge of the moon, well away from the 'the moon' pill, but both are on the moon. The moon is not a full disc (gibbous); 'round' follows the key word and the description."})

# ---------- 4094
t4=T()
bl={0.0:(0,0,.92,.63),0.5:(0,0,.92,.63),1.0:(0,0,.93,.68),1.5:(0,0,1,.58),2.0:(0,0,.96,.58),2.5:(0,0,.86,.61),3.0:(0,0,.76,.64),
 3.5:(0,0,.60,.64),4.0:(0,0,.52,.64),4.5:(0,0,.70,.52),5.0:(0,0,1,.59),5.5:(0,0,1,.60),6.0:(0,0,.68,.60),6.5:(0,0,.42,.55),
 7.0:(0,0,.64,.63),7.5:(0,0,.66,.63),8.0:(0,0,.62,.57),8.5:(0,0,.59,.52),9.0:(0,0,.57,.55),9.5:(0,0,.55,.56),10.0:(0,0,.53,.53),
 10.5:(0,0,.52,.52),11.0:(0,0,.49,.55),11.5:(0,0,.48,.57),12.0:(0,0,.44,.46),12.5:(0,0,.47,.52),13.0:(0,0,.46,.52),
 13.5:(0,0,.38,.48),14.0:(0,0,.39,.48),14.5:(0,0,.41,.50),15.0:(0,0,.44,.50)}
br={7.0:(.76,.17,.24,.47),7.5:(.70,.17,.30,.38),8.0:(.65,.19,.35,.36),8.5:(.60,.17,.40,.39),9.0:(.58,.15,.42,.41),
 9.5:(.55,.17,.45,.40),10.0:(.53,.18,.47,.37),10.5:(.52,.19,.48,.36),11.0:(.49,.20,.51,.36),11.5:(.50,.19,.50,.39)}
kb=keys(bl,t4)
save({"mediaId":4094,"level":"A","keyWord":"feed","defaultVoice":"female",
 "taps":[{"phrase":"to drink some water","target":"the black horse","voice":"female","keys":kb},
         {"phrase":"to walk down the road","target":"the black horse","voice":"female","keys":kb},
         {"phrase":"to have a brown head","target":"the brown horse","voice":"female","keys":keys(br,t4)}],
 "stillS":6.5,
 "nouns":[{"word":"a horse","x":.17,"y":.25,"voice":"female"},{"word":"bags","x":.62,"y":.48,"voice":"female"},
          {"word":"a shovel","x":.78,"y":.80,"voice":"female"}],
 "question":"What are the two horses doing?",
 "answer":["The","horses","are","eating","their","feed."],
 "answerVoice":"female",
 "notes":"The brown horse does nothing the black horse does not also do (both eat the hay), so its phrase is a state. The key word 'feed' is not a nameable object in the still (the bags hold it), so it is used in the model answer (the hay the two horses eat) and the bags are labelled 'bags'; there are also plain brown sacks at the far left of the still. 'a shovel' may be a little above A level. No person in the clip: defaultVoice follows evenId."})
