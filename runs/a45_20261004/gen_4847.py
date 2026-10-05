import json
T=[round(i*0.5,1) for i in range(21)]
def keys(d):
    return [dict(t=t,**dict(zip('xywh',d[t]))) if t in d else {'t':t,'off':True} for t in T]
ware={7.0:(.47,.3,.2,.2),7.5:(.41,.28,.2,.2),8.0:(.36,.25,.26,.22),8.5:(.26,.26,.48,.22),9.0:(.17,.25,.65,.38),9.5:(.03,.23,.93,.42),10.0:(0,.22,1,.66)}
old={5.5:(.38,.16,.24,.35),6.0:(.35,.18,.24,.32),6.5:(.28,.18,.42,.42)}
pud={2.5:(0,0,.62,.55),3.0:(0,0,.82,.57)}
c={"mediaId":4847,"level":"A","keyWord":"floor","defaultVoice":"female",
"taps":[
 {"phrase":"to sit on the floor","target":"the woman in the big hall","voice":"female","keys":keys(ware)},
 {"phrase":"to clean between the shelves","target":"the woman with white hair","voice":"female","keys":keys(old)},
 {"phrase":"to clean up dirty water","target":"the woman near the brown water","voice":"female","keys":keys(pud)}],
"stillS":9.5,
"nouns":[{"word":"lights","x":0.5,"y":0.10,"voice":"female"},
 {"word":"a door","x":0.33,"y":0.28,"voice":"female"},
 {"word":"a woman","x":0.5,"y":0.42,"voice":"female"},
 {"word":"the floor","x":0.4,"y":0.75,"voice":"female"}],
"question":"Where is the woman sitting?",
"answer":["She","is","sitting","on","the","floor."],
"answerVoice":"female",
"notes":"All people are women -> female. The description's 'woman in a grey shirt in a cream-tiled corridor' is the woman by the brown puddle (2.5-3.0 s); the warehouse woman also wears a grey T-shirt, so she is named by place ('in the big hall' = the warehouse). 'the floor' on the still used with 'the' (one floor, like 'the sky'). Kitchen shot (0-2 s) shows only legs and a spin mop, not a target. Warehouse woman is small at 7.0-8.0 s (minimum box)."}
json.dump(c,open('content/4847.json','w'),indent=1)
