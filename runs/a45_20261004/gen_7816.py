import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(b): return [dict(t=t,x=x0,y=y0,w=round(x1-x0,2),h=round(y1-y0,2)) for t,(x0,y0,x1,y1) in zip(T,b)]
woman=K([(.32,.32,.68,.92),(.47,.31,.72,.92),(.37,.33,.70,.99),(.35,.32,.71,.99),(.40,.31,.72,.99),(.32,.31,.73,.99),(.29,.33,.76,.99),(.32,.34,.80,.99)])
blue=K([(.69,.40,.86,.74),(.72,.40,.88,.74),(.71,.40,.88,.77),(.72,.40,.90,.77),(.73,.42,.90,.78),(.74,.43,.92,.80),(.76,.44,.92,.81),(.80,.44,.96,.83)])
c={"mediaId":7816,"level":"A","keyWord":"easy","defaultVoice":"female",
"taps":[{"phrase":"to carry a big chair","target":"the woman","voice":"female","keys":woman},
{"phrase":"to walk down the street","target":"the woman","voice":"female","keys":woman},
{"phrase":"to wear a blue T-shirt","target":"the man in blue","voice":"male","keys":blue}],
"stillS":0.2,
"nouns":[{"word":"a chair","x":0.70,"y":0.20,"voice":"female"},{"word":"a tree","x":0.30,"y":0.08,"voice":"female"},
{"word":"houses","x":0.12,"y":0.33,"voice":"female"},{"word":"a box","x":0.12,"y":0.62,"voice":"female"}],
"question":"What is the woman carrying?","answer":["She","is","carrying","a","big","chair."],"answerVoice":"female",
"notes":"Blue-shirt man uses a state phrase: both men handle the mattress, so no action fits only him. His box is narrow where the woman's raised arm covers him (split along her torso edge)."}
json.dump(c,open('content/7816.json','w'),indent=1)
