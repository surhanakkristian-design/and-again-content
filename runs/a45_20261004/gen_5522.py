import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,**dict(zip('xywh',r))) if r else {"t":t,"off":True} for t,r in zip(T,rows)]
man=[(.13,.51,.34),(.14,.51,.34),(.14,.52,.33),(.14,.52,.33),(.13,.53,.31),(.13,.53,.30),(.12,.54,.29),(.12,.55,.29)]
dog=[(.09,.33,.68,.87),(.10,.33,.67,.87),(.08,.29,.68,.86),(.09,.29,.66,.86),(.09,.28,.66,.86),(.08,.28,.68,.86),(.09,.29,.68,.87),(.08,.30,.68,.87)]
wom=[(.56,.86,.36),(.56,.85,.36),(.57,.87,.36),(.56,.88,.35),(.58,.90,.34),(.59,.90,.32),(.59,.92,.31),(.60,.93,.31)]
r=lambda v:round(v,2)
D=K([(r(a-.03),r(c-.02),r(b-a+.06),r(d-c+.04)) for a,b,c,d in dog])
M=K([(r(a-.02),r(y-.02),r(b-a+.04),r(dog[i][2]-.02-(y-.02))) for i,(a,b,y) in enumerate(man)])
W=K([(r(a-.02),r(y-.02),r(min(1,b+.03)-(a-.02)),r(.89-(y-.02))) for a,b,y in wom])
c={"mediaId":5522,"level":"B","keyWord":"acknowledge","defaultVoice":"male",
"taps":[{"phrase":"to raise an open palm","target":"the man","voice":"male","keys":M},
{"phrase":"to shelter under an umbrella","target":"the woman","voice":"female","keys":W},
{"phrase":"to shake off the rainwater","target":"the terrier","voice":"male","keys":D}],
"stillS":1.2,
"nouns":[{"word":"an umbrella","x":0.66,"y":0.33,"voice":"male"},{"word":"a street lamp","x":0.34,"y":0.18,"voice":"male"},
{"word":"a raincoat","x":0.75,"y":0.56,"voice":"male"},{"word":"a terrier","x":0.20,"y":0.77,"voice":"male"}],
"question":"What is the woman doing?","answer":["She","is","sheltering","under","a","blue","umbrella."],"answerVoice":"female",
"notes":"Terrier stands in front of the man's legs: man's box is cut at the dog's top (legs below excluded) so boxes do not overlap. Dog shakes from ~2.7 s."}
json.dump(c,open('content/5522.json','w'),indent=1)
