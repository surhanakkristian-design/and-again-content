import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
man={0.0:(.36,0,.64,.52),0.5:(0,0,1,.32),1.0:(.66,0,.34,.52),1.5:(.2,0,.8,.7),2.0:(.38,.02,.62,.78),2.5:(.5,.12,.5,.72),
3.0:(.45,.08,.55,.8),3.5:(.34,.05,.66,.82),4.0:(.48,.08,.52,.78),4.5:(.47,.13,.53,.72),5.0:(.44,.27,.56,.68),5.5:(.41,.12,.59,.74),
6.0:(.56,.18,.44,.62),6.5:(.44,.22,.56,.68),7.0:(.38,0,.62,.72),7.5:(.37,0,.63,.72),8.0:(.5,.01,.5,.66),8.5:(.44,.01,.56,.62),
9.0:(.5,.18,.5,.62),9.5:(.47,.28,.53,.56),10.0:(.46,.29,.54,.20)}
wom={3.0:(0,0,.22,.47),3.5:(0,.18,.33,.5),4.0:(0,.22,.38,.4),4.5:(.06,.18,.40,.44),5.0:(.04,.22,.39,.46),5.5:(0,.15,.4,.53),
6.0:(.02,.16,.5,.44),6.5:(0,.13,.43,.46),7.0:(0,.02,.37,.56),7.5:(0,0,.36,.52),8.0:(.03,.09,.42,.31),8.5:(.06,.15,.37,.37),
9.0:(.05,.23,.43,.44),9.5:(.1,.25,.36,.4),10.0:(.08,.34,.37,.15)}
cat={9.5:(0,.67,.42,.33),10.0:(.22,.5,.38,.36)}
c={"mediaId":833,"level":"A","keyWord":"unpacking","defaultVoice":"male",
"taps":[{"phrase":"to open the suitcase","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to put on a hat","target":"the woman","voice":"female","keys":keys(wom)},
{"phrase":"to walk over the clothes","target":"the cat","voice":"male","keys":keys(cat)}],
"stillS":6.0,
"nouns":[{"word":"a hat","x":.40,"y":.46,"voice":"male"},{"word":"clothes","x":.30,"y":.58,"voice":"male"},
{"word":"a suitcase","x":.50,"y":.76,"voice":"male"},{"word":"shoes","x":.86,"y":.92,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","taking","clothes","out","of","a","suitcase."],"answerVoice":"male",
"notes":"t=0.0-1.0: only the man's arms/hands are visible (boxed). The cat is visible only at 9.5 and 10.0. At 10.0 the cat stands in front of the lying couple, so the man's and the woman's boxes hold only head and upper body (legs are behind/next to the cat box). At 8.0 the man's reaching arm passes below the woman; his box holds body, not the arm tip. Hat at stillS 6.0 is in the woman's hands (slightly motion-blurred)."}
json.dump(c,open('content/833.json','w'),indent=1)
