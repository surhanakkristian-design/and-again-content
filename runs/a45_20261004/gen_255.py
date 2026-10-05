import json
T=[i*0.5 for i in range(21)]
def mk(d):
    out=[]
    for t in T:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=b
            out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
W={0.0:(.34,.33,1,1),0.5:(.34,.34,1,1),1.0:(.36,.33,1,1),1.5:(.40,.33,1,1),2.0:(.38,.33,1,1)}
P={2.5:(.15,.44,1,.80),3.0:(.15,.44,1,.80),3.5:(.13,.45,1,.80),4.0:(.12,.45,1,.80),4.5:(.13,.45,1,.80),5.0:(.13,.45,1,.79)}
S={}
for t in T:
    if t>=5.5:
        P[t]=(.13,.52,.99,.78); S[t]=(.37,.37,.59,.51)
c={"mediaId":255,"level":"A","keyWord":"east","defaultVoice":"female",
"taps":[
 {"phrase":"to point at the sky","target":"the woman","voice":"female","keys":mk(W)},
 {"phrase":"to rise in the east","target":"the sun","voice":"female","keys":mk(S)},
 {"phrase":"to raise their cups","target":"the people","voice":"female","keys":mk(P)}],
"stillS":8.0,
"nouns":[{"word":"the sky","x":0.50,"y":0.18,"voice":"female"},{"word":"the sun","x":0.48,"y":0.48,"voice":"female"},{"word":"people","x":0.50,"y":0.60,"voice":"female"},{"word":"rocks","x":0.50,"y":0.86,"voice":"female"}],
"question":"What is the sun doing?",
"answer":["The","sun","is","rising","over","the","clouds."],
"answerVoice":"female",
"notes":"Cut at 2.5. 'the woman' = the close-up woman of shot 1 (0-2.0); in shot 2 she is probably the braid figure in the middle of the group, seen small from behind, so she is set off there and the whole row is 'the people'. Sun box sits directly above the people box (split at y 0.51/0.52, which trims the tops of the two tallest heads): the raised hands and cups at 9.0-10.0 reach into the sun box. 'to rise in the east' carries the key word (east itself is not visible, only the sunrise). She points at the red stripe low in the sky/horizon."}
json.dump(c,open('content/255.json','w'),indent=1,ensure_ascii=False)
