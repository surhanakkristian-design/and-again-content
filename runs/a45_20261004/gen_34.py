import json
T=[i*0.5 for i in range(21)]
def b(t,v):
    if v is None: return {"t":t,"off":True}
    x0,y0,x1,y1=v; return {"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)}
W={0.0:(0,.19,.53,.85),0.5:(0,.19,.53,.85),1.0:(0,.19,.53,.85),1.5:(0,.19,.53,.85),2.0:(.06,.34,.46,.80),2.5:(.10,.24,.54,.61),
3.0:(.13,.31,.50,.99),3.5:(.11,.33,.53,.84),4.0:(.12,.33,.44,.78),4.5:(.08,.36,.52,.77),5.0:(.08,.42,.47,.76),5.5:(.05,.29,.46,.69),
6.0:(.04,.34,.52,.77),6.5:(.03,.30,.45,.74),7.0:(0,.40,.37,.75),7.5:(.11,.37,.44,.73),8.0:(.17,.33,.47,.68),8.5:(.06,.40,.52,.68),
9.0:(0,.59,.80,.96),9.5:(0,.48,.48,1.0),10.0:(0,.43,.46,.93)}
M={0.0:(.54,.24,1,.75),0.5:(.54,.24,1,.75),1.0:(.54,.24,1,.75),1.5:(.54,.24,1,.75),2.0:(.47,.30,1,.68),2.5:(.56,.31,1,.61),
3.0:(.51,.31,.93,.98),3.5:(.55,.31,.90,.84),4.0:(.55,.37,.87,.78),4.5:(.53,.41,.97,.81),5.0:(.55,.45,1,.82),5.5:(.48,.44,1,.66),
6.0:(.53,.49,1,.73),6.5:(.50,.45,1,.76),7.0:(.42,.40,.89,.78),7.5:(.59,.34,.94,.78),8.0:(.55,.26,.95,.79),8.5:(.53,.36,1,.65),
9.0:(.42,.33,.97,.58),9.5:(.49,.41,1,.64),10.0:(.47,.41,1,.61)}
D={9.0:(0,.40,.18,.58),9.5:(.25,.31,.48,.47),10.0:(.36,.25,.56,.40)}
c={"mediaId":34,"level":"A","keyWord":"activity","defaultVoice":"female",
"taps":[{"phrase":"to wear a white T-shirt","target":"the woman","voice":"female","keys":[b(t,W[t]) for t in T]},
{"phrase":"to have a short beard","target":"the man","voice":"male","keys":[b(t,M[t]) for t in T]},
{"phrase":"to run on four legs","target":"the dog","voice":"female","keys":[b(t,D.get(t)) for t in T]}],
"stillS":9.5,
"nouns":[{"word":"a dog","x":.38,"y":.39,"voice":"female"},{"word":"a man","x":.80,"y":.50,"voice":"male"},
{"word":"a woman","x":.28,"y":.66,"voice":"female"},{"word":"grass","x":.68,"y":.88,"voice":"female"}],
"question":"What are the man and woman doing?",
"answer":["They","are","playing","badminton","on","the","grass."],
"answerVoice":"female",
"notes":"Man and woman do the same things all through the clip (lie on the sofa, run, play, fall), so their two phrases are states (clothes, beard). The dog is only visible from 9.0 s. At 9.0 the woman's raised leg crosses the dog: dog box is narrow there and the woman's box starts below it. Key word 'activity' is abstract, not used as a noun slot; 'badminton' in the answer is not in the phrases/nouns."}
json.dump(c,open('content/34.json','w'),indent=1,ensure_ascii=False)
