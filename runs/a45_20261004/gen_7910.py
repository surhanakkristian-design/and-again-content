import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
man=K([(.35,.0,.45,.52),(.37,.0,.43,.52),(.34,.02,.46,.5),(.28,.04,.52,.48),(.29,.06,.49,.5),(.35,.08,.42,.5),(.37,.11,.42,.5),(.31,.11,.48,.5)])
wom=K([(.03,.16,.31,.33),(.03,.16,.33,.33),(.03,.17,.30,.32),(.03,.18,.24,.30),(.03,.19,.25,.33),(.03,.19,.31,.32),(.04,.21,.32,.32),(.03,.21,.27,.32)])
cat=K([None,None,None,None,(.80,.18,.20,.16),(.78,.22,.22,.15),(.80,.26,.20,.14),(.80,.27,.20,.14)])
c={"mediaId":7910,"level":"A","keyWord":"music","defaultVoice":"female",
"taps":[{"phrase":"to play the saxophone","target":"the man","voice":"male","keys":man},
{"phrase":"to dance to the music","target":"the woman in pink","voice":"female","keys":wom},
{"phrase":"to sleep on the piano","target":"the cat","voice":"female","keys":cat}],
"stillS":3.2,
"nouns":[{"word":"a lamp","x":0.12,"y":0.11,"voice":"female"},{"word":"a cat","x":0.90,"y":0.33,"voice":"female"},
{"word":"a saxophone","x":0.33,"y":0.44,"voice":"female"},{"word":"a piano","x":0.60,"y":0.86,"voice":"female"}],
"question":"What is the man doing?","answer":["He","is","playing","the","saxophone."],"answerVoice":"male",
"notes":"woman in pink sits on a stool and sways her raised hand (seated dancing); cat only visible from 2.2 s at the top right; woman/man boxes split along the sax bell"}
json.dump(c,open('content/7910.json','w'),indent=1)
