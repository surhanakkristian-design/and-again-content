import json
T=[i*0.5 for i in range(25)]
wo={0.0:(.27,.05,.67,.64),0.5:(.30,.07,.68,.65),1.0:(.28,.16,.72,.75),1.5:(.28,.06,.70,.70),
 2.0:(.36,.16,.38,.43),2.5:(.30,.21,.43,.38),3.0:(.25,.24,.44,.38),3.5:(.15,.28,.50,.37),4.0:(.30,.22,.40,.40),
 4.5:(.35,.23,.36,.36),5.0:(.21,.32,.43,.32),5.5:(.33,.26,.32,.34),6.0:(.21,.32,.40,.30),6.5:(.31,.33,.32,.30)}
fa={}
for t in T:
    if t>=7.0: wo[t]=(.36,.28,.25,.30) if t<10 else (.36,.31,.25,.27)
    if 2.0<=t<6.0: fa[t]=(.38,0,.50,.14)
    elif 6.0<=t<7.0: fa[t]=(.38,0,.50,.16)
    elif 7.0<=t<8.0: fa[t]=(.38,0,.50,.20)
    elif t==8.0: fa[t]=(.38,.03,.50,.20)
    elif t>8.0: fa[t]=(.38,.05,.50,.20)
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":round(min(w,1-x),2),"h":round(min(h,1-y),2)})
        else: out.append({"t":t,"off":True})
    return out
wk=keys(wo); fk=keys(fa)
c={"mediaId":5165,"level":"B","keyWord":"plastic","defaultVoice":"female",
 "taps":[{"phrase":"to fish out a bottle","target":"the woman","voice":"female","keys":wk},
         {"phrase":"to give off thick smoke","target":"the factory","voice":"female","keys":fk},
         {"phrase":"to cry in despair","target":"the woman","voice":"female","keys":wk}],
 "stillS":10.0,
 "nouns":[{"word":"a chimney","x":.59,"y":.17,"voice":"female"},{"word":"a pipe","x":.25,"y":.27,"voice":"female"},
          {"word":"a woman","x":.47,"y":.42,"voice":"female"},{"word":"plastic","x":.33,"y":.76,"voice":"female"}],
 "question":"What is floating in the river?","answer":["Plastic","rubbish","is","floating","in","the","river."],"answerVoice":"female",
 "notes":"0-1.5 s is a close-up (no factory in view, factory OFF); from 2.0 s a wide shot with the factory chimney and smoke at the top. The smoke plume rises left of the tall chimney; the factory box covers chimney, plant and smoke. 'plastic' pill sits on the floating bottles/cups near the bank. The woman cries all through the clip, so 'to cry in despair' is visible without sound."}
json.dump(c,open('content/5165.json','w'),indent=1)
