import json
def K(d,times):
    out=[]
    for t in times:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
times=[i*0.5 for i in range(24)]
L={0.0:(.03,.33,.30,.52),0.5:(.03,.33,.31,.52),1.0:(.04,.34,.32,.53),1.5:(.04,.34,.33,.53),2.0:(.04,.33,.31,.52),2.5:(.03,.33,.30,.52),
3.0:(0,.33,.29,.54),3.5:(0,.33,.28,.54),4.0:(0,.33,.27,.52),4.5:(0,.33,.31,.52),5.0:(.05,.34,.30,.54),5.5:(.07,.32,.31,.54),
6.0:(.08,.27,.30,.57),6.5:(.08,.28,.32,.56),7.0:(.10,.27,.31,.60),7.5:(.08,.28,.32,.57),8.0:(.05,.27,.30,.57),8.5:(.02,.27,.29,.57),
9.0:(0,.28,.28,.58),9.5:(0,.28,.28,.59),10.0:(0,.27,.26,.56),10.5:(0,.27,.31,.56),11.0:(.05,.28,.36,.59),11.5:(.08,.28,.28,.57)}
R={0.0:(.45,.33,.33,.42),0.5:(.57,.34,.23,.41),1.0:(.61,.35,.19,.40),1.5:(.50,.40,.30,.35),2.0:(.46,.33,.25,.42),2.5:(.45,.33,.32,.44),
3.0:(.42,.33,.32,.44),3.5:(.38,.33,.32,.44),4.0:(.38,.33,.34,.42),4.5:(.40,.33,.28,.42),5.0:(.47,.30,.18,.14),5.5:(.67,.33,.19,.44),
6.0:(.71,.29,.14,.43),6.5:(.67,.29,.20,.44),7.0:(.65,.30,.22,.46),7.5:(.65,.29,.22,.46),8.0:(.46,.29,.18,.42),8.5:(.44,.29,.31,.44),
9.0:(.38,.30,.33,.45),9.5:(.34,.30,.36,.45),10.0:(.36,.29,.34,.44),10.5:(.42,.29,.33,.44),11.0:(.45,.30,.25,.45),11.5:(.46,.30,.40,.45)}
W={0.5:(.38,.30,.19,.14),1.0:(.41,.30,.20,.15),1.5:(.60,.26,.22,.14),2.0:(.71,.29,.19,.34),2.5:(.77,.29,.22,.37),
3.0:(.78,.30,.22,.50),3.5:(.78,.29,.22,.55),4.0:(.76,.29,.24,.44),4.5:(.68,.31,.32,.47),5.0:(.47,.44,.35,.45),5.5:(.43,.36,.24,.53),
6.0:(.42,.31,.29,.44),6.5:(.41,.31,.26,.44),7.0:(.41,.33,.24,.42),7.5:(.41,.32,.24,.46),8.0:(.64,.30,.22,.48),8.5:(.75,.30,.22,.46),
9.0:(.76,.29,.24,.43),9.5:(.75,.29,.25,.42),10.0:(.73,.28,.22,.38),10.5:(.75,.28,.18,.35),11.0:(.70,.30,.18,.44)}
c={"mediaId":4236,"level":"B","keyWord":"attract","defaultVoice":"male",
"taps":[
{"phrase":"to stroll along the pavement","target":"the woman","voice":"female","keys":K(W,times)},
{"phrase":"to stand with hands on hips","target":"the man on the right","voice":"male","keys":K(R,times)},
{"phrase":"to drop his work gloves","target":"the man on the left","voice":"male","keys":K(L,times)}],
"stillS":3.0,
"nouns":[{"word":"a van","x":.25,"y":.20,"voice":"male"},{"word":"a television","x":.38,"y":.53,"voice":"male"},
{"word":"a handbag","x":.86,"y":.43,"voice":"male"},{"word":"high heels","x":.87,"y":.62,"voice":"male"}],
"question":"Who attracts the men's attention?",
"answer":["The","woman","in","high","heels","attracts","their","attention."],
"answerVoice":"female",
"notes":"The woman overlaps the man on the right from 0.5 s to 8.0 s; boxes are split along the line between them (5.0 s: the man is almost hidden, only a small box on his head, the woman's box starts below it). The men look up while lifting and only stare after the woman at the end (8.5-11.5 s); 'attracts their attention' rests on that. Gloves are dropped only at 11.5 s. defaultVoice male: two men are the main people."}
json.dump(c,open("content/4236.json","w"),indent=1)
