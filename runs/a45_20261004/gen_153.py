import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
bottle={0.0:(.30,.38,.45,.62),0.5:(.28,.39,.47,.61),1.0:(.27,.40,.45,.60),1.5:(.28,.30,.45,.70),2.0:(.38,.38,.34,.55),
2.5:(.37,.33,.36,.57),3.0:(.42,.31,.33,.62),3.5:(.42,.29,.33,.60),4.0:(.44,.50,.34,.48),4.5:(.55,.82,.30,.18),5.0:(.60,.84,.30,.16),
5.5:(.47,.23,.40,.14),6.0:(.53,.19,.33,.14),6.5:(.60,.25,.33,.14),7.0:(.33,.84,.30,.16),7.5:(.37,.80,.25,.17),8.0:(.40,.63,.22,.16),
8.5:(.40,.60,.22,.15),9.0:(.40,.58,.22,.15),9.5:(.40,.58,.22,.15),10.0:(.40,.56,.22,.15)}
glasses={0.0:(0,0,.48,.37),0.5:(0,0,.40,.38),1.0:(0,0,.38,.39),1.5:(0,.03,.27,.37),2.0:(0,.24,.37,.33),2.5:(.03,.39,.33,.31),
3.0:(.04,.55,.37,.39),3.5:(.05,.64,.36,.36),4.0:(.20,.86,.23,.14),5.5:(.15,.38,.62,.55),6.0:(.13,.34,.66,.52),6.5:(.10,.40,.66,.53),
7.0:(.30,.20,.27,.56),7.5:(.25,.08,.37,.60),8.0:(.20,.30,.45,.25),8.5:(.18,.33,.55,.20),9.0:(.20,.33,.57,.17),9.5:(.20,.33,.58,.17),10.0:(.25,.36,.47,.16)}
dog={8.5:(0,.70,.18,.20),9.0:(0,.67,.24,.20),9.5:(0,.67,.24,.20),10.0:(0,.64,.22,.21)}
c={"mediaId":153,"level":"B","keyWord":"champagne","defaultVoice":"male",
"taps":[
 {"phrase":"to chill in an ice bucket","target":"the bottle","voice":"male","keys":keys(bottle)},
 {"phrase":"to fill up with champagne","target":"the glasses","voice":"male","keys":keys(glasses)},
 {"phrase":"to wander across the terrace","target":"the dog","voice":"male","keys":keys(dog)}],
"stillS":6.0,
"nouns":[{"word":"champagne","x":.30,"y":.50,"voice":"male"},{"word":"a tray","x":.50,"y":.86,"voice":"male"},
 {"word":"a napkin","x":.88,"y":.38,"voice":"male"},{"word":"a light bulb","x":.50,"y":.16,"voice":"male"}],
"question":"What are the glasses filling up with?",
"answer":["The","glasses","are","filling","up","with","champagne."],
"answerVoice":"male",
"notes":"People are inconsistent between shots (who holds the tray / raises the glass changes), so targets are things and the dog. Bottle is out of the bucket 2.5-6.5 (poured), back in the bucket from 7.0; at 4.5-5.0 only its top is in frame. Glasses box after 7.0 covers the glasses in the friends' hands (overlaps their faces). Dog only from 8.5. defaultVoice male: mixed group, odd id."}
json.dump(c,open("content/153.json","w"),indent=1)
