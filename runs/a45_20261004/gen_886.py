import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [dict(t=t, x=d[t][0], y=d[t][1], w=d[t][2], h=d[t][3]) if t in d else dict(t=t, off=True) for t in T]
F={0.0:(0,.15,1,.85),0.5:(0,.15,1,.85),1.0:(0,.17,1,.83),1.5:(0,.17,.97,.83),2.0:(0,.14,.85,.86),2.5:(0,.16,.77,.84),3.0:(0,.21,.46,.79),
3.5:(0,.20,.45,.80),4.0:(0,.17,.45,.83),4.5:(0,.17,.44,.83),5.0:(0,.17,.45,.83),5.5:(0,.17,.30,.83),6.0:(0,.17,.19,.83),6.5:(0,.17,.20,.83),
7.0:(0,.17,.18,.83),7.5:(0,.17,.18,.83),8.0:(0,.17,.19,.83),8.5:(0,.15,.22,.85),9.0:(0,.19,.27,.81),9.5:(0,.15,.28,.85),10.0:(0,.12,.38,.88)}
O={3.0:(.61,.21,.39,.79),3.5:(.46,.20,.54,.80),4.0:(.46,.19,.54,.81),4.5:(.45,.17,.55,.83),5.0:(.46,.17,.54,.83),5.5:(.40,.17,.60,.83),
6.0:(.37,.15,.63,.85),6.5:(.36,.15,.64,.85),7.0:(.35,.15,.65,.85),7.5:(.34,.14,.66,.86),8.0:(.36,.14,.64,.86),8.5:(.40,.13,.60,.87),
9.0:(.50,.13,.50,.87),9.5:(.41,.16,.59,.84),10.0:(.60,.16,.40,.84)}
B={2.0:(.86,.42,.14,.24),2.5:(.78,.25,.22,.50),3.0:(.46,.25,.15,.33),5.5:(.30,.21,.10,.36),6.0:(.20,.18,.17,.30),6.5:(.20,.18,.16,.32),
7.0:(.19,.18,.16,.38),7.5:(.19,.17,.15,.36),8.0:(.20,.18,.16,.30),8.5:(.23,.17,.17,.31),9.0:(.28,.18,.22,.40),9.5:(.29,.18,.12,.40),10.0:(.39,.18,.21,.34)}
c=dict(mediaId=886,level="B",keyWord="wrinkle",defaultVoice="female",taps=[
 dict(phrase="to frown at the camera",target="the woman in front",voice="female",keys=keys(F)),
 dict(phrase="to point at her wrinkles",target="the old woman",voice="female",keys=keys(O)),
 dict(phrase="to sit in the background",target="the woman at the back",voice="female",keys=keys(B))],
 stillS=8.5,
 nouns=[dict(word="grapes",x=.62,y=.07,voice="female"),dict(word="wrinkles",x=.75,y=.32,voice="female"),
        dict(word="pomegranates",x=.22,y=.52,voice="female"),dict(word="a glass of tea",x=.35,y=.62,voice="female")],
 question="What is the old woman pointing at?",
 answer=["She","is","pointing","at","her","wrinkles."],answerVoice="female",
 notes="Three women. The woman in front frowns (wrinkled forehead) only at 0.0-0.5 s, then laughs. The old woman points at her own face at 5.5-8.0 s; from 8.5 s the woman in front puts her hand on the old woman's cheek (her arm crosses into the old woman's box) - not used as a phrase. The woman at the back is squeezed between the two faces: her box is narrow (below the 0.18 minimum) at 5.5-9.5 s so that it never overlaps; she is off at 3.5-5.0 s where only a sliver/half of her face shows behind the others. The old woman's pointing hand partly lies left of her box at 5.5-8.0 s (free space, belongs to no other box). Still 8.5 s: a second small tea glass stands behind the labelled one; grapes hang at the top edge (dark bunches).")
json.dump(c,open('content/886.json','w'),indent=1,ensure_ascii=False)
