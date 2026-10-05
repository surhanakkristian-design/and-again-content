import json
T=[i*0.5 for i in range(25)]
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":round(d[t][2],2),"h":round(d[t][3],2)} if t in d else {"t":t,"off":True}) for t in T]
b={0.0:(.23,.17,.52,.65),0.5:(.23,.14,.57,.7),1.0:(.2,.12,.6,.86),1.5:(.18,.09,.66,.91),2.0:(.12,.05,.72,.86),2.5:(.13,.02,.78,.92),
9.5:(.08,.1,.68,.85),10.0:(.08,.23,.7,.75),10.5:(.2,.48,.6,.38),11.0:(.1,.55,.72,.43),11.5:(.06,.55,.76,.43),12.0:(.1,.55,.74,.41)}
for t in (5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5): b[t]=(0,0,1,1)
g={3.0:(.7,.26,.3,.74),3.5:(.68,.24,.32,.76),9.5:(.78,.29,.22,.6),10.0:(.8,.28,.2,.47),10.5:(.82,.27,.18,.45),
11.0:(.86,.37,.14,.45),11.5:(.85,.33,.15,.48),12.0:(.86,.29,.14,.4)}
c={"mediaId":836,"level":"B","keyWord":"prepared","defaultVoice":"male",
"taps":[{"phrase":"to haul a huge backpack","target":"the boy with the backpack","voice":"male","keys":keys(b)},
{"phrase":"to collapse onto a sleeping bag","target":"the boy with the backpack","voice":"male","keys":keys(b)},
{"phrase":"to fold her arms","target":"the girl in the striped sweater","voice":"female","keys":keys(g)}],
"stillS":5.5,
"nouns":[{"word":"books","x":.50,"y":.09,"voice":"male"},{"word":"a backpack","x":.20,"y":.28,"voice":"male"},
{"word":"glasses","x":.50,"y":.40,"voice":"male"},{"word":"a hoodie","x":.50,"y":.73,"voice":"male"}],
"question":"What is the boy in front carrying?","answer":["He","is","hauling","a","huge","backpack."],"answerVoice":"male",
"notes":"Only two targets: the classmates all stare / laugh alike, so no action fits only one of them except the folded arms of the girl in the striped sweater (arms folded at 3.0, 3.5, 9.5, 10.0; from 10.5 she laughs with a hand on her chest but is still boxed). The boy's box includes his backpack. Everything is OFF at 4.0/4.5 (close-up of the blonde girl) and 9.0 (close-up of the boy in the black T-shirt). The green roll is called 'a sleeping bag' in phrase 2 (the description says sleeping mat/roll). Pill 'a backpack' sits on the blue pack visible left of his head. Key word 'prepared' is an adjective, not used in the texts."}
json.dump(c,open('content/836.json','w'),indent=1)
