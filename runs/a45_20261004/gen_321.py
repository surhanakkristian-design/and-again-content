import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
W={0.0:(.14,.18,.86,.82),0.5:(.11,.16,.89,.84),1.0:(.10,.16,.90,.84),1.5:(.08,.16,.92,.84),2.0:(0,.22,.88,.78),
2.5:(.08,.17,.90,.83),3.0:(.06,.16,.92,.84),3.5:(.11,.16,.89,.84),4.0:(.18,.14,.82,.86),4.5:(.11,.16,.89,.84),
5.0:(.08,.24,.92,.76),5.5:(.04,.08,.96,.92),6.5:(.34,0,.66,1.0),7.0:(.18,.13,.82,.87),7.5:(.20,.14,.80,.86),
8.0:(.22,.10,.78,.90),8.5:(0,.07,1.0,.93),9.0:(.27,.16,.73,.84),9.5:(.20,.20,.80,.80),10.0:(.29,.14,.71,.86)}
M={6.5:(0,.13,.33,.40),7.0:(0,.26,.18,.36),7.5:(0,.26,.20,.32),8.0:(0,.27,.22,.26),9.0:(0,.28,.26,.20),
9.5:(0,.29,.20,.31),10.0:(0,.30,.27,.30)}
c={"mediaId":321,"level":"A","keyWord":"fruit","defaultVoice":"female",
"taps":[
{"phrase":"to eat a peach","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to carry a basket","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to stand behind the table","target":"the man in the apron","voice":"male","keys":keys(M)}],
"stillS":6.0,
"nouns":[{"word":"a pineapple","x":.48,"y":.38,"voice":"female"},{"word":"grapes","x":.72,"y":.50,"voice":"female"},
{"word":"a peach","x":.82,"y":.67,"voice":"female"},{"word":"a basket","x":.45,"y":.86,"voice":"female"}],
"question":"What is the woman eating?",
"answer":["She","is","eating","a","peach."],
"answerVoice":"female",
"notes":"Key word 'fruit' is not a noun slot (the whole still is fruit; the slots name single fruits) and not in the answer. The man in the apron stands behind the fruit table in the background 6.5-10 s (hidden behind the peach at 8.5 s: OFF); a tiny shopper in the background at 0-1.5 s is why the target is named 'the man in the apron'. At 6.0 s only fruit and two headless torsos: both OFF. Woman boxes are cut on the left where the man stands: at 6.5 s her forearm (x<.34) and at 9.0 s her hand with the peach (x<.27, below the man, whose box ends at y .48 above the peach) fall outside her box. A dog walks under the table 9.0-10 s, not used."}
json.dump(c,open("content/321.json","w"),indent=1,ensure_ascii=False)
