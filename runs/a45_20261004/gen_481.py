import json
T=[i*0.5 for i in range(21)]
man=[(0,.27,.62,.73),(0,.28,.62,.72),(.13,.3,.42,.7),(.08,.3,.46,.7),(.13,.28,.5,.72),(.18,.28,.5,.72),(.18,.28,.45,.72),(.11,.33,.47,.67),(.09,.33,.48,.67),(.11,.3,.5,.7),(.13,.3,.45,.7),(.08,.3,.45,.7),(.13,.28,.44,.72),(.15,.28,.42,.72),
(.22,.3,.33,.7),(.27,.3,.29,.7),(.30,.33,.22,.67),(.30,.33,.22,.67),(.32,.36,.2,.64),(.25,.35,.27,.65),(0,.34,.52,.40)]
wom=[None]*14+[(0,.38,.22,.62),(0,.44,.27,.56),(0,.40,.30,.60),(0,.40,.30,.60),(0,.5,.32,.5),(0,.5,.25,.5),(0,.74,.28,.26)]
def keys(b):
    return [({"t":t,"x":k[0],"y":k[1],"w":k[2],"h":k[3]} if k else {"t":t,"off":True}) for t,k in zip(T,b)]
d={"mediaId":481,"level":"A","keyWord":"a mirror","defaultVoice":"male",
"taps":[
 {"phrase":"to bend his knees","target":"the young man","voice":"male","keys":keys(man)},
 {"phrase":"to wear grey shorts","target":"the young man","voice":"male","keys":keys(man)},
 {"phrase":"to wear a purple T-shirt","target":"the woman","voice":"female","keys":keys(wom)}],
"stillS":4.5,
"nouns":[{"word":"a mirror","x":.72,"y":.13,"voice":"male"},{"word":"a fan","x":.36,"y":.31,"voice":"male"},{"word":"weights","x":.60,"y":.76,"voice":"male"}],
"question":"What is the young man doing?",
"answer":["He","is","looking","in","the","mirror."],"answerVoice":"male",
"notes":"Mirror clip: the right half is the young man's REFLECTION; boxes cover only the real person on the left. Only two targets: the man in yellow is mostly hidden behind the young man (7.0-9.5 s) and is seen mainly as a reflection, so no clean box for him. From 7.0 s the woman stands in front of the young man and they overlap: split by a vertical line, his head lies partly over her box. At 10.0 s only her arm and shoulder are in frame. The nouns are few because the mirror doubles most things; 'weights' sits on the rack that stands at the mirror edge."}
json.dump(d,open("content/481.json","w"),indent=1,ensure_ascii=False)
