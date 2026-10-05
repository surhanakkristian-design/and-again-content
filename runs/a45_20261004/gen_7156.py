import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True}); continue
        x0,y0,x1,y1=b; out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
red=[(.39,.24,.60,.75),(.39,.25,.60,.75),(.37,.27,.58,.77),(.37,.29,.62,.79),(.38,.27,.64,.81),(.42,.27,.70,.83),(.46,.27,.73,.87)]
blue=[(.13,.35,.39,.63),(.13,.36,.39,.63),(.11,.37,.37,.67),(.11,.42,.37,.69),(.11,.39,.38,.67),(.11,.39,.42,.70),(.10,.40,.46,.72)]
woman=[(.60,.32,.93,.90),(.60,.32,.95,.90),(.58,.33,.97,1.0),(.62,.34,.97,1.0),(.64,.35,.99,1.0),(.70,.35,1.0,1.0),(.73,.36,1.0,1.0)]
c={"mediaId":7156,"level":"B","keyWord":"get down","defaultVoice":"male",
"taps":[
 {"phrase":"to swallow a hot dog","target":"the man in the red cap","voice":"male","keys":K(red)},
 {"phrase":"to pour water from a jug","target":"the woman","voice":"female","keys":K(woman)},
 {"phrase":"to puff out his cheeks","target":"the man in the blue top","voice":"male","keys":K(blue)}],
"stillS":0.2,
"nouns":[{"word":"bunting","x":0.50,"y":0.10,"voice":"male"},
 {"word":"a grill","x":0.12,"y":0.40,"voice":"male"},
 {"word":"a glass bowl","x":0.50,"y":0.79,"voice":"male"},
 {"word":"hot dogs","x":0.55,"y":0.92,"voice":"male"}],
"question":"What is the woman doing?",
"answer":["She","is","pouring","water","from","a","jug."],
"answerVoice":"female",
"notes":"Red-cap man's box starts right of the blue-top man, so his raised fist (left, above the blue-top man) is outside his box. Woman's jug arm reaches into the red-cap man's box edge at 2.2-3.2 s."}
json.dump(c,open('content/7156.json','w'),indent=1)
