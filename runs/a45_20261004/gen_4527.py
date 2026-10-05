import json
def keys(d, times):
    return [dict(t=t, x=d[t][0], y=d[t][1], w=d[t][2], h=d[t][3]) if d.get(t) else dict(t=t, off=True) for t in times]
times=[i*0.5 for i in range(25)]
C={0.0:(.11,0,.85,.73),0.5:(.11,0,.87,.78),1.0:(.09,0,.85,.83),1.5:(.13,0,.87,.78),2.0:(.11,0,.88,.54),2.5:(.07,0,.93,.63),3.0:(.05,0,.93,.60),3.5:(.08,0,.87,.72),
4.0:(.08,0,.80,.66),4.5:(.06,0,.82,.60),5.0:(.02,0,.83,.78),5.5:(.02,0,.85,.82),6.0:(.02,0,.85,.63),6.5:(0,0,.97,.73),7.0:(0,0,.87,.63),7.5:(0,0,.90,.66),
8.0:(0,0,.87,.49),8.5:(0,0,.87,.66),9.0:(0,0,.87,.72),9.5:(0,0,.87,.78),10.0:(0,0,.84,.70),10.5:(0,0,.87,.68),11.0:(0,0,.84,.78),11.5:(0,0,.82,.75),12.0:(.06,.02,.53,.60)}
Fi={0.0:(0,.27,.11,.17),0.5:(0,.27,.11,.17),1.0:(0,.24,.09,.19),1.5:(0,.22,.13,.17),2.0:(0,.10,.11,.20),2.5:(0,.08,.07,.17),3.0:(0,.10,.05,.18),3.5:(0,.17,.08,.18),
4.0:(0,.23,.08,.16),4.5:(0,.27,.06,.17)}
kc=keys(C,times)
c={"mediaId":4527,"level":"A","keyWord":"vegetable","defaultVoice":"male",
"taps":[
 {"phrase":"to cut the vegetables","target":"the cook","voice":"male","keys":kc},
 {"phrase":"to hold a big knife","target":"the cook","voice":"male","keys":kc},
 {"phrase":"to burn behind the cook","target":"the fire","voice":"male","keys":keys(Fi,times)}],
"stillS":5.5,
"nouns":[{"word":"a hat","x":.61,"y":.06,"voice":"male"},{"word":"a T-shirt","x":.33,"y":.38,"voice":"male"},
 {"word":"a knife","x":.63,"y":.565,"voice":"male"},{"word":"vegetables","x":.42,"y":.76,"voice":"male"}],
"question":"What is the cook doing?",
"answer":["He","is","cutting","vegetables","with","a","big","knife."],
"answerVoice":"male",
"notes":"Only two targets: the cook (two phrases) and the fire at the left edge. The fire is at the very edge of the picture, so its box is narrower than 0.18 (it must not overlap the cook's arm); from 5.0 on it is a sliver or out of the picture (off). The cook's box holds his body, hands and the knife, not the board. The crowd was not used as a target (a group)."}
json.dump(c,open('content/4527.json','w'),indent=1,ensure_ascii=False)
