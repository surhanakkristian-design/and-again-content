from gen_5592_5593_5595_5596_lib import keys, write
T=[0.2,0.7,1.2,1.7,2.2,2.7]
def b(x0,y0,x1,y1): return (x0,y0,x1-x0,y1-y0)
man=[b(.03,.36,.34,.95),b(.05,.36,.34,.95),b(.03,.35,.34,.95),b(.05,.35,.35,.95),b(.03,.35,.40,.96),b(.04,.35,.40,.96)]
wom=[b(.56,.52,.97,.88),b(.51,.52,.97,.88),b(.51,.52,.97,.88),b(.49,.52,.97,.88),b(.52,.52,.97,.88),b(.49,.52,.97,.88)]
cus=[b(.48,.88,.78,1),b(.48,.88,.78,1),b(.48,.88,.78,1),b(.48,.88,.78,1),b(.48,.88,.78,1),b(.47,.88,.78,1)]
write(5596,{"mediaId":5596,"level":"B","keyWord":"awkward","defaultVoice":"male",
 "taps":[{"phrase":"to lean against the wall","target":"the man","voice":"male","keys":keys([(t,)+man[i] for i,t in enumerate(T)])},
         {"phrase":"to push the lower end","target":"the woman","voice":"female","keys":keys([(t,)+wom[i] for i,t in enumerate(T)])},
         {"phrase":"to lie on a stone step","target":"the cushion","voice":"male","keys":keys([(t,)+cus[i] for i,t in enumerate(T)])}],
 "stillS":0.2,
 "nouns":[{"word":"a sofa","x":0.38,"y":0.48,"voice":"male"},
          {"word":"a mural","x":0.88,"y":0.44,"voice":"male"},
          {"word":"geraniums","x":0.36,"y":0.76,"voice":"male"},
          {"word":"a cushion","x":0.63,"y":0.93,"voice":"male"}],
 "question":"What is the woman doing?",
 "answer":["She","is","pushing","the","lower","end","of","the","sofa."],
 "answerVoice":"female",
 "notes":"Key word 'awkward' is an adjective, not placed. The sofa itself is not a tap target: it touches both people's hands, so its box would overlap theirs; the fallen cushion is used instead (a state phrase). The woman's box stops at y=0.88 so it does not overlap the cushion box (her trainers end right at the cushion's top edge); the cushion box is only 0.12 high because it sits at the bottom edge. 'the lower end' in the phrase refers to the sofa, made explicit in the answer."})
