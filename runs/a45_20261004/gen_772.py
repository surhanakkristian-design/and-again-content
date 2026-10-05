import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} if b else {"t":t,"off":True})
    return out
Y={0.0:(.08,.07,.67,.93),0.5:(.08,.07,.68,.93),1.0:(.08,.07,.68,.93),1.5:(.08,.07,.67,.93),2.0:(.08,.07,.68,.93),2.5:(0,.06,.95,.94),
 3.0:(0,.06,.86,.94),3.5:(0,.06,.79,.94),4.0:(0,.04,.85,.96),4.5:(0,.04,.84,.96),5.0:(0,.05,.9,.95),5.5:(0,.05,.9,.95),
 6.0:(0,.02,.88,.98),6.5:(0,.02,.9,.98),7.0:(.02,.28,.64,.7),7.5:(.02,.28,.61,.7),8.0:(.02,.28,.62,.7),8.5:(.02,.28,.61,.7),
 9.0:(.14,.32,.46,.66),9.5:(.15,.2,.41,.8),10.0:(.1,.13,.48,.87)}
Th={0.0:(.76,.14,.24,.86),0.5:(.76,.14,.24,.86),1.0:(.76,.17,.24,.83),1.5:(.75,.15,.25,.85),2.0:(.76,.14,.24,.86),
 3.0:(.86,.64,.14,.36),3.5:(.8,.5,.2,.5),4.0:(.85,.18,.15,.82),4.5:(.84,.58,.16,.42),
 7.0:(.66,.28,.34,.72),7.5:(.63,.26,.37,.74),8.0:(.64,.25,.36,.75),8.5:(.63,.25,.37,.75),9.0:(.6,.3,.4,.7),9.5:(.56,.28,.44,.72),10.0:(.58,.3,.4,.7)}
c={"mediaId":772,"level":"B","keyWord":"therapy","defaultVoice":"female",
"taps":[{"phrase":"to clutch a cushion","target":"the young woman","voice":"female","keys":keys(Y)},
{"phrase":"to wipe away her tears","target":"the young woman","voice":"female","keys":keys(Y)},
{"phrase":"to hand over the tissues","target":"the therapist","voice":"female","keys":keys(Th)}],
"stillS":4.0,
"nouns":[{"word":"a cushion","x":.3,"y":.73,"voice":"female"},{"word":"a headband","x":.47,"y":.2,"voice":"female"},
{"word":"a cardigan","x":.25,"y":.5,"voice":"female"},{"word":"tissues","x":.78,"y":.6,"voice":"female"}],
"question":"What is the young woman clutching?","answer":["She","is","clutching","a","cushion","on","her","lap."],"answerVoice":"female",
"notes":"Two targets only (young woman, therapist). In the close-ups 2.5-6.5 s the therapist is mostly out of frame: she is boxed only at 3.0-4.5 s where her hand passes the tissue box (small box at the right edge), off at 2.5 and 5.0-6.5 s although a sliver of glasses/hand shows at the edge. In the wide shots the boxes are split at a vertical line; the therapist's notebook and knees left of the line fall outside her box. Key word 'therapy' is not a visible noun and is not in the answer (a 'therapy session' would be an inference)."}
json.dump(c,open('content/772.json','w'),indent=1,ensure_ascii=False)
