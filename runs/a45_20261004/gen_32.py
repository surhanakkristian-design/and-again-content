import json
# t: (split, man top, woman top, woman bottom)
F={0.0:(.51,.20,.25,.78),0.5:(.47,.20,.21,.78),1.0:(.46,.20,.24,.78),1.5:(.47,.20,.23,.78),2.0:(.45,.19,.22,.78),2.5:(.47,.20,.24,.78),
3.0:(.46,.31,.31,.78),3.5:(.47,.31,.31,.78),4.0:(.45,.31,.31,.78),4.5:(.47,.20,.23,.78),5.0:(.47,.31,.31,.78),5.5:(.47,.31,.31,.78),
6.0:(.46,.22,.25,.78),6.5:(.47,.22,.25,.78),7.0:(.47,.25,.27,.78),7.5:(.47,.25,.27,.78),8.0:(.46,.25,.26,.78),8.5:(.47,.25,.26,.78),
9.0:(.45,.27,.27,.78),9.5:(.47,.27,.27,.78),10.0:(.45,.25,.27,.78),10.5:(.47,.25,.27,.78),11.0:(.46,.27,.29,.78),11.5:(.47,.27,.29,.78),
12.0:(.48,.25,.27,.78),12.5:(.46,.25,.27,.78),13.0:(.38,.28,.20,.80),13.5:(.40,.27,.20,.80),14.0:(.36,.30,.06,.80),14.5:(.38,.25,.27,.75),15.0:(.41,.20,.24,.80)}
Bt=[3.0,3.5,4.0,5.0,5.5]
T=[i/2 for i in range(31)]
r=lambda v: round(v,2)
man=[{"t":t,"x":0,"y":F[t][1],"w":r(F[t][0]-.01),"h":r(1-F[t][1])} for t in T]
wom=[{"t":t,"x":F[t][0],"y":F[t][2],"w":r(1-F[t][0]),"h":r(F[t][3]-F[t][2])} for t in T]
let=[({"t":t,"x":.34,"y":.06,"w":.33,"h":.24} if t in Bt else {"t":t,"off":True}) for t in T]
o={"mediaId":32,"level":"A","keyWord":"word","defaultVoice":"female",
"taps":[{"phrase":"to touch his beard","target":"the man","voice":"male","keys":man},
{"phrase":"to have long hair","target":"the woman","voice":"female","keys":wom},
{"phrase":"to be big and white","target":"the letter","voice":"female","keys":let}],
"stillS":3.5,
"nouns":[{"word":"a letter","x":.50,"y":.20,"voice":"female"},{"word":"a beard","x":.20,"y":.54,"voice":"female"},
{"word":"a woman","x":.75,"y":.43,"voice":"female"}],
"question":"What is the man touching?","answer":["He","is","touching","his","beard."],"answerVoice":"male",
"notes":"Two people sit close together: boxes split along a vertical line between the heads; the man's arm that reaches to the lower right (in front of the woman) is below the woman's box and in nobody's box. The man touches his beard/chin at 8.5-12.5 s. The woman's phrase is a state ('to have long hair'): her only own action (raising her arm, 13.0-14.0) is short and blurred. Key word 'word' is not a visible noun (only the letter B is shown), so it is not a slot; 3 nouns. defaultVoice female by evenId (mixed pair)."}
json.dump(o,open("content/32.json","w"),indent=1)
