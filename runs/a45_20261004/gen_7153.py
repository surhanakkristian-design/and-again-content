import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True}); continue
        x0,y0,x1,y1=b; out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
woman=[(.65,.37,.95,.75),(.65,.37,.95,.75),(.66,.38,.95,.78),(.66,.39,.95,.80),(.65,.38,.93,.74),(.65,.39,.92,.70),(.55,.41,.87,.66),(.59,.42,.87,.64)]
gen=[(.43,.62,.65,.76),(.43,.62,.65,.76),(.45,.62,.66,.76),(.46,.62,.66,.76),(.45,.62,.65,.76),(.45,.62,.65,.76),None,None]
w=K(woman); g=K(gen)
c={"mediaId":7153,"level":"B","keyWord":"generator","defaultVoice":"female",
"taps":[
 {"phrase":"to crouch on the stage","target":"the woman","voice":"female","keys":w},
 {"phrase":"to operate the fog generator","target":"the woman","voice":"female","keys":w},
 {"phrase":"to pump out thick fog","target":"the fog generator","voice":"female","keys":g}],
"stillS":0.2,
"nouns":[{"word":"a lighting rig","x":0.40,"y":0.08,"voice":"female"},
 {"word":"a drum kit","x":0.56,"y":0.50,"voice":"female"},
 {"word":"a fog generator","x":0.50,"y":0.69,"voice":"female"},
 {"word":"a canister","x":0.90,"y":0.73,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","crouching","next","to","a","fog","generator."],
"answerVoice":"female",
"notes":"Key word 'generator' shown as a fog machine; used 'fog generator'. Generator box split from the woman along her hands/knees; generator set off at 3.2/3.7 s where fog hides it."}
json.dump(c,open('content/7153.json','w'),indent=1)
