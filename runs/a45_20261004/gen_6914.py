import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) for t,r in zip(T,rows)]
car=K([(0,.20,.84,.80),(0,.26,.70,.74),(0,.29,.60,.71),(0,.30,.52,.70),(0,.29,.55,.60),(0,.30,.55,.58),(0,.30,.56,.58),(0,.30,.62,.58)])
man=K([(.85,.18,.15,.81),(.71,.24,.29,.68),(.61,.26,.39,.60),(.52,.30,.46,.54),(.55,.28,.39,.49),(.55,.31,.30,.45),(.56,.30,.28,.46),(.62,.28,.25,.48)])
d={"mediaId":6914,"level":"B","keyWord":"bus","defaultVoice":"male",
"taps":[
 {"phrase":"to kick the car door","target":"the man","voice":"male","keys":man},
 {"phrase":"to laugh up at the sky","target":"the man","voice":"male","keys":man},
 {"phrase":"to give off clouds of steam","target":"the old car","voice":"male","keys":car}],
"stillS":3.7,
"nouns":[{"word":"steam","x":0.42,"y":0.26,"voice":"male"},{"word":"a lorry","x":0.86,"y":0.32,"voice":"male"},
 {"word":"a wing mirror","x":0.58,"y":0.81,"voice":"male"},{"word":"a spare tyre","x":0.27,"y":0.93,"voice":"male"}],
"question":"What is pouring out of the car?",
"answer":["Steam","is","pouring","out","of","the","car."],
"answerVoice":"male",
"notes":"KEY WORD MISMATCH: the clip shows a station wagon, no bus anywhere (only a distant lorry), so 'bus' is not used as a noun. Man and car overlap (his kicking leg at 1.7 s, his hand on the roof at 2.2-3.2 s): split vertically, so the man's box cuts his foot/hand there. Man is cut by the right edge at 0.2 s."}
json.dump(d,open('content/6914.json','w'),indent=1)
