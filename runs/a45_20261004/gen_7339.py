import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
B=[(0.28,0.29,0.58,0.30),(0.02,0.17,0.43,0.35),(0.14,0.23,0.38,0.31),(0.09,0.28,0.45,0.28),(0.14,0.32,0.38,0.30),(0.10,0.42,0.82,0.29),(0.58,0.66,0.42,0.29),(0.64,0.48,0.36,0.28)]
def k(L): return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,L)]
b=k(B)
c={"mediaId":7339,"level":"B","keyWord":"martin","defaultVoice":"male",
"taps":[
 {"phrase":"to carry an insect","target":"the bird at the nest","voice":"male","keys":b},
 {"phrase":"to land at the nest","target":"the bird at the nest","voice":"male","keys":b},
 {"phrase":"to poke its head inside","target":"the bird at the nest","voice":"male","keys":b}],
"stillS":2.2,
"nouns":[{"word":"a martin","x":0.30,"y":0.40,"voice":"male"},{"word":"a nest","x":0.10,"y":0.50,"voice":"male"},
 {"word":"a roof","x":0.62,"y":0.20,"voice":"male"},{"word":"a field","x":0.80,"y":0.80,"voice":"male"}],
"question":"What is the martin doing?",
"answer":["It","is","carrying","an","insect","to","its","nest."],"answerVoice":"male",
"notes":"All three phrases on one bird: the other birds only swoop past, blurred, in 0.2-0.7. At 3.2-3.7 a bird with an insect flies in again (possibly another bird); boxes follow it as the insect carrier. Field is blurred in the background."}
json.dump(c,open('content/7339.json','w'),indent=1)
