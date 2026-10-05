import json
def keys(d,T):
    out=[]
    for t in T:
        b=d.get(t)
        if not b: out.append({"t":t,"off":True}); continue
        x0,y0,x1,y1=b
        out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
T=[i*0.5 for i in range(21)]
P={2.5:(0,0,1,1),3.0:(0,0,1,1),3.5:(0,0,1,1),4.0:(.42,0,1,1),4.5:(.41,0,1,1),5.0:(.46,0,1,1),5.5:(.43,0,1,1),6.0:(.43,0,1,1),
6.5:(.49,0,1,1),7.0:(.46,0,1,1),7.5:(.48,0,1,1),8.0:(.45,0,1,1),8.5:(.46,0,1,1),9.0:(.43,0,1,1),9.5:(.44,0,1,1),10.0:(.41,0,1,1)}
S={4.0:(0,0,.41,.80),4.5:(0,0,.40,.85),5.0:(0,0,.45,.60),5.5:(0,0,.42,.55),6.0:(0,0,.42,.72),6.5:(0,0,.48,.75),7.0:(0,0,.45,.72),
7.5:(0,0,.47,.70),8.0:(0,0,.44,.62),8.5:(0,0,.45,.62),9.0:(0,0,.42,.62),9.5:(0,0,.43,.62),10.0:(0,0,.40,.62)}
c={"mediaId":448,"level":"B","keyWord":"lip gloss","defaultVoice":"female",
"taps":[{"phrase":"to apply pink lip gloss","target":"the woman in purple","voice":"female","keys":keys(P,T)},
{"phrase":"to dab her lower lip","target":"the woman in purple","voice":"female","keys":keys(P,T)},
{"phrase":"to peer over her sunglasses","target":"the woman in sunglasses","voice":"female","keys":keys(S,T)}],
"stillS":2.0,
"nouns":[{"word":"a railing","x":0.45,"y":0.14,"voice":"female"},{"word":"a bowl","x":0.62,"y":0.73,"voice":"female"},
{"word":"lip gloss","x":0.38,"y":0.88,"voice":"female"}],
"question":"What is the woman in purple doing?",
"answer":["She","is","applying","lip gloss","to","her","lips."],"answerVoice":"female",
"notes":"Two women from 4.0 on: the close-up woman in the purple cardigan who applies the gloss (2.5-3.5 only her face, wand at her lips -> whole frame) and the woman in sunglasses behind her. 0.0-2.0: a face at the right edge (fringe, white collar, no sunglasses) and hands holding the tube - not clear which of the two women it is, so BOTH targets are off there; verifier please judge. 'to dab her lower lip' = she pats the lip with a finger at 5.0-5.5. 'to peer over her sunglasses' = from 7.0 the glasses sit low and her eyes look over them (4.0-6.5 she looks through them). Boxes split on the line between the two faces; the lower-left corner (white top / purple sleeve) is left to no one below the sunglasses woman's box. Nouns on the 2.0 frame: only 3 (the wand is not a separate noun because 'lip gloss' could label it too); a second small bowl is cut off at the left edge. 'lip gloss' is one chip."}
json.dump(c,open('content/448.json','w'),indent=1)
