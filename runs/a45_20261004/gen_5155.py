import json
T=[i*0.5 for i in range(25)]
O=None
Wo=[(.14,.06,.80,.74),(.08,.02,.92,.86),(.10,.04,.90,.88),(.12,.02,.88,.90)]+[O]*15+[(.30,0,.50,.20),(.30,0,.47,.24),(.35,0,.40,.31),(.29,.04,.48,.34),(.28,.08,.48,.33),(.32,.15,.39,.29)]
Sp=[O]*6+[(.38,0,.32,.38),(.18,0,.60,.42),(.18,0,.62,.44),(.18,0,.57,.42),(.10,0,.72,.44)]+[O]*14
def k(L): return [dict(t=t,off=True) if v is None else dict(t=t,x=v[0],y=v[1],w=v[2],h=v[3]) for t,v in zip(T,L)]
c={"mediaId":5155,"level":"A","keyWord":"lunch","defaultVoice":"female",
"taps":[{"phrase":"to put down a big plate","target":"the woman in blue","voice":"female","keys":k(Wo)},
 {"phrase":"to open her arms","target":"the woman in blue","voice":"female","keys":k(Wo)},
 {"phrase":"to put pasta on the plate","target":"the big spoon","voice":"female","keys":k(Sp)}],
"stillS":12.0,
"nouns":[{"word":"a window","x":0.50,"y":0.08,"voice":"female"},{"word":"flowers","x":0.72,"y":0.24,"voice":"female"},
 {"word":"plates","x":0.50,"y":0.50,"voice":"female"},{"word":"a fork","x":0.30,"y":0.68,"voice":"female"}],
"question":"What is the woman in blue doing?","answer":["She","is","putting","down","a","big","plate."],"answerVoice":"female",
"notes":"Woman visible 0-1.5 and 9.5-12.0 (at 9.5/10.0 only her torso at the top edge). A hand reaches in at 6.5/7.0 (probably hers, not certain) -> marked off. The spoon is visible 3.0-5.0 only; at 2.5 pasta falls from above with no tool visible, at 2.0 only the rim of a pan. 'to put pasta on the plate' is done by the spoon (its holder is off screen). The family (grey-haired man, boy, girl, second woman) appear only at 11.0-12.0, so no phrase for them. A second woman (dark top) sits at the right edge at 11.0-12.0, hence 'the woman in blue'; no noun 'a woman'. Still 12.0: 'flowers' on the yellow flowers right of her head; fork pill on the fork in front of the nearest plate."}
json.dump(c,open('content/5155.json','w'),indent=1)
