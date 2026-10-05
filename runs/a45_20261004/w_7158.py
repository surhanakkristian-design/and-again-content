import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes): return [dict(t=t,**dict(zip('xywh',b))) if b else {"t":t,"off":True} for t,b in zip(T,boxes)]
singer=K([(.30,.08,.42,.71),(.30,.05,.48,.74),(.30,.08,.42,.72),(.30,.07,.48,.73),(.30,.08,.44,.74),(.28,.03,.71,.79),(.28,.26,.71,.62),(.50,.36,.50,.42)])
jeans=K([(0,.43,.28,.40),(0,.43,.28,.40),(0,.44,.28,.40),(0,.45,.28,.39),(0,.46,.28,.38),(0,.46,.26,.38),(0,.46,.26,.42),(0,.42,.30,.44)])
c={"mediaId":7158,"level":"B","keyWord":"get drunk","defaultVoice":"female",
"taps":[{"phrase":"to belt out a song","target":"the singer","voice":"female","keys":singer},
{"phrase":"to flop down onto the sofa","target":"the singer","voice":"female","keys":singer},
{"phrase":"to cover her ears","target":"the woman in jeans","voice":"female","keys":jeans}],
"stillS":0.2,
"nouns":[{"word":"a party hat","x":.49,"y":.14,"voice":"female"},{"word":"a microphone","x":.53,"y":.40,"voice":"female"},
{"word":"a beer bottle","x":.46,"y":.78,"voice":"female"},{"word":"a tambourine","x":.73,"y":.88,"voice":"female"}],
"question":"What is the singer doing?","answer":["She","is","belting","out","a","karaoke","song."],"answerVoice":"female",
"notes":"Singer = woman on the sofa with the mic; she drops down at 3.2-3.7. Woman in jeans covers her ears from 0.7 (laughs at 0.2). At 2.7 the singer's head reaches x .20 but her box starts at .28 to avoid the woman in jeans. A third woman at the far left edge (hand on the singer's leg) is not a target. 'belt out a song' particle could also follow 'song' in theory."}
json.dump(c,open('content/7158.json','w'),indent=1)
