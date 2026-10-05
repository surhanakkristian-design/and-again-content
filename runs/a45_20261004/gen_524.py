import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
w={0.0:(.07,.15,.86,.85),0.5:(.09,.14,.86,.86),1.0:(.15,.18,.80,.82),1.5:(.04,.17,.90,.83),2.0:(.04,.27,.80,.73),2.5:(.19,.24,.71,.76),
3.0:(.05,.17,.87,.72),3.5:(.07,.10,.77,.76),4.0:(.16,.05,.80,.64),4.5:(.14,0,.77,.62),5.0:(.13,.05,.78,.95),5.5:(.11,.15,.83,.85),
6.0:(.18,.19,.78,.81),6.5:(.18,.20,.58,.80),7.0:(.13,.29,.82,.71),7.5:(.18,.34,.62,.66),8.0:(.04,.26,.84,.74),8.5:(.04,.21,.96,.79),
9.0:(.03,.21,.97,.79),9.5:(0,.20,1,.80),10.0:(0,.18,1,.82)}
c={"mediaId":524,"level":"B","keyWord":"panic","defaultVoice":"female",
"taps":[
{"phrase":"to pat her pockets frantically","target":"the woman","voice":"female","keys":keys(w)},
{"phrase":"to rummage through her bag","target":"the woman","voice":"female","keys":keys(w)},
{"phrase":"to clutch her head","target":"the woman","voice":"female","keys":keys(w)}],
"stillS":4.5,
"nouns":[{"word":"a tote bag","x":.25,"y":.66,"voice":"female"},{"word":"a wallet","x":.44,"y":.74,"voice":"female"},
{"word":"a hairbrush","x":.76,"y":.82,"voice":"female"},{"word":"keys","x":.28,"y":.90,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","rummaging","through","her","tote","bag."],
"answerVoice":"female",
"notes":"Only one clear tap target: the woman is the single person; the train is the whole background behind her and the bag hangs on her / lies in front of her, so neither can get a box that does not overlap hers. All three phrases use the woman. Key word 'panic' is not a visible noun, so it is not among the nouns. Nouns at 4.5 s lie close together on the floor (wallet next to a phone, keys next to a small bottle)."}
json.dump(c,open("content/524.json","w"),indent=1)
