import json
T=[i/2 for i in range(21)]
M={0.0:(.08,0,.92,.48),0.5:(.45,0,.55,.48),1.0:(.45,0,.55,.48),1.5:(0,0,1,.48),2.0:(0,0,1,.45),2.5:(0,0,1,.44),3.0:(0,0,1,.42),3.5:(0,0,1,.42),
4.0:(0,0,1,.55),4.5:(0,0,1,.65)}
W={5.0:(0,.12,1,.76),5.5:(0,.12,1,.78),6.0:(.12,.08,.80,.48),6.5:(0,.09,1,.50),7.0:(0,.10,1,.52),7.5:(0,.12,1,.50),8.0:(0,.08,1,.55),
8.5:(0,.06,1,.57),9.0:(0,.12,1,.52),9.5:(0,.08,1,.88),10.0:(0,.14,1,.70)}
def keys(d): return [({"t":t,"off":True} if t not in d else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3])) for t in T]
c={"mediaId":4429,"level":"A","keyWord":"restaurant","defaultVoice":"male",
"taps":[{"phrase":"to eat with a spoon","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to pick up noodles","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to hold a big bowl","target":"the woman","voice":"female","keys":keys(W)}],
"stillS":7.0,
"nouns":[{"word":"chopsticks","x":.22,"y":.33,"voice":"male"},{"word":"noodles","x":.42,"y":.48,"voice":"male"},
{"word":"a bowl","x":.50,"y":.78,"voice":"male"},{"word":"a woman","x":.68,"y":.21,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","picking","up","noodles","with","chopsticks."],"answerVoice":"female",
"notes":"Two shots: 0-4.5 s a man in a black hoodie with a bowl of cereal at home (only chin / chest visible until 3.5 s, face with the spoon at 4.0-4.5 s), 5-10 s the woman with the ramen bowl in the restaurant. Only two targets (man, woman): bowls / lanterns do nothing of their own. defaultVoice male: a man and a woman share the clip, evenId false. The woman's box covers the bowl only where she holds it in her hands (5.0, 5.5, 9.5, 10.0 s). Key word 'restaurant' is the place, not a placeable noun, and is not used in the texts. 'to hold a big bowl': the man never holds his bowl."}
json.dump(c,open('content/4429.json','w'),indent=1)
