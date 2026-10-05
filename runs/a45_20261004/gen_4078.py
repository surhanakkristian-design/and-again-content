import json
T=[i*0.5 for i in range(27)]
w={0.0:(.25,.86,.30,.14),0.5:(.16,.67,.58,.33),1.0:(.26,.56,.46,.44),1.5:(.20,.54,.52,.46),2.0:(.23,.53,.49,.47),2.5:(.18,.51,.54,.46),
3.0:(.23,.47,.41,.50),3.5:(.31,.46,.35,.52),4.0:(.30,.43,.34,.39),4.5:(.33,.41,.31,.35),5.0:(.34,.40,.30,.36),5.5:(.34,.39,.27,.31),
6.0:(.36,.37,.28,.29),6.5:(.36,.36,.26,.29),7.0:(.36,.35,.25,.26),7.5:(.37,.35,.25,.24),8.0:(.38,.34,.24,.24),8.5:(.36,.34,.26,.22),
9.0:(.37,.33,.24,.23),9.5:(.39,.32,.22,.22),10.0:(.37,.32,.24,.20),10.5:(.38,.31,.24,.20),11.0:(.43,.31,.21,.20),11.5:(.38,.31,.33,.21),
12.0:(.33,.31,.36,.16),12.5:(.33,.31,.36,.19),13.0:(.33,.33,.36,.18)}
wk=[dict(t=t,x=w[t][0],y=w[t][1],w=w[t][2],h=w[t][3]) for t in T]
hk=[dict(t=t,x=.34,y=.07,w=.28,h=.24) for t in T]
d={"mediaId":4078,"level":"B","keyWord":"pillow","defaultVoice":"female",
"taps":[{"phrase":"to crawl across the bed","target":"the woman","voice":"female","keys":wk},
{"phrase":"to spread her arms wide","target":"the woman","voice":"female","keys":wk},
{"phrase":"to hang above the bed","target":"the wall hanging","voice":"female","keys":hk}],
"stillS":5.0,
"nouns":[{"word":"a wall hanging","x":.48,"y":.20,"voice":"female"},{"word":"pillows","x":.50,"y":.37,"voice":"female"},{"word":"a woman","x":.49,"y":.53,"voice":"female"},{"word":"a duvet","x":.50,"y":.82,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","crawling","towards","the","row","of","pillows."],"answerVoice":"female",
"notes":"Only two tap targets. The row of pillows was not used as a third target: from about 7 s the woman is in front of it and at 11-13 s she lies in the middle of the row with pillows on both sides, so one box for the pillows cannot avoid her box. The key word is a noun slot ('pillows', plural for the row) and is in the answer. Both woman phrases share the keys; she spreads her arms only at 11.5-13 s. The woman pill at 5.0 s sits on her back; the duvet pill on the folds behind her."}
json.dump(d,open("content/4078.json","w"),indent=1)
