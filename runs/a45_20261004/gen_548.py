import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
W={0.0:(0,.24,.55,.76),0.5:(0,.26,.36,.74),1.0:(0,.30,.60,.70),1.5:(0,.28,.62,.72),2.0:(0,.36,.66,.64),2.5:(0,.33,.68,.67),
3.0:(0,.40,.68,.24),3.5:(0,.39,.66,.24),4.0:(0,.13,.56,.58),4.5:(0,.13,.57,.58),5.0:(0,.17,.56,.56),5.5:(0,.17,.56,.56),
6.0:(0,.05,.52,.95),6.5:(0,.05,.52,.95),7.0:(0,.08,.52,.92),7.5:(0,.08,.52,.92),8.0:(0,.08,.52,.92),8.5:(0,.10,.52,.90),
9.0:(0,.28,.66,.72),9.5:(0,.35,.52,.65),10.0:(0,.37,.34,.63)}
M={0.0:(.60,.33,.34,.42),0.5:(.63,.38,.32,.38),1.0:(.64,.35,.30,.45),4.0:(.58,.38,.24,.32),4.5:(.59,.38,.24,.33),5.0:(.58,.37,.24,.35),5.5:(.58,.37,.24,.35),
6.0:(.54,.10,.46,.90),6.5:(.54,.10,.46,.90),7.0:(.54,.12,.46,.88),7.5:(.54,.14,.46,.86),8.0:(.54,.18,.46,.82),8.5:(.54,.18,.46,.82),
9.0:(.72,.25,.28,.62),9.5:(.82,.36,.18,.64),10.0:(.64,.36,.36,.64)}
c={"mediaId":548,"level":"B","keyWord":"photography","defaultVoice":"female",
"taps":[
 {"phrase":"to peer through the viewfinder","target":"the woman","voice":"female","keys":keys(W)},
 {"phrase":"to pose against the wall","target":"the man","voice":"male","keys":keys(M)},
 {"phrase":"to point at the camera screen","target":"the man","voice":"male","keys":keys(M)}],
"stillS":4.5,
"nouns":[{"word":"a camera","x":.16,"y":.34,"voice":"female"},{"word":"cobblestones","x":.38,"y":.85,"voice":"female"},{"word":"the sky","x":.36,"y":.07,"voice":"female"},{"word":"a man","x":.70,"y":.52,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","posing","against","the","wall."],
"answerVoice":"male",
"notes":"Key word 'photography' is abstract, not used as a noun slot; 'a camera' stands in. 0-3.5 s is a confusing close shot of hands and the camera (AI-odd extra hand from the right); at 2.0-3.5 s the woman is only her forearm with the watch and white sleeve, the man is off 1.5-3.5 s. Woman has the camera at her eye 4.0-5.5 s (viewfinder); man leans on the orange wall 4.0-5.0 s and points at the screen 7.0-8.5 s. At 9.5 s the man is only a sliver at the right edge. Small birds in the sky from 6.0 s not used (their box would collide with the people)."}
json.dump(c,open('content/548.json','w'),indent=1)
