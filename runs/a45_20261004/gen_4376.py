import json
T=[i*0.5 for i in range(21)]
W=[(.30,.42,.44,.46),(.29,.42,.44,.49),(.26,.56,.40,.40),(.12,.32,.62,.66),(.01,.44,.68,.56),(0,.47,.40,.45),(.26,.65,.40,.35),(.26,.50,.47,.47),(.32,.57,.44,.37),(.35,.61,.36,.36),(.33,.68,.33,.32),(.34,.69,.33,.31),(.35,.69,.31,.31),(.39,.68,.32,.32),(.39,.68,.36,.32),(.29,.68,.44,.32),(.32,.66,.39,.34),(.22,.58,.42,.37),(.19,.39,.57,.61),(.20,.38,.64,.60),(.26,.29,.58,.56)]
G=[(0,.07,.29,.52),(0,.10,.38,.32),(0,.11,.38,.45),(0,0,.34,.31),None,None,(0,.24,.25,.62),(.07,.26,.40,.24),(.07,.23,.37,.34),(.02,.34,.33,.48),(.04,.41,.29,.56),(.02,.42,.31,.55),(.04,.41,.31,.46),(.08,.35,.31,.47),(.07,.32,.32,.59),(.09,.29,.33,.39),(.10,.36,.48,.30),(0,.25,.48,.33),(0,0,.33,.39),(0,0,.30,.38),(0,0,.32,.29)]
O=[(.75,.02,.25,.68),(.74,.03,.26,.69),(.74,.08,.26,.75),None,(.70,0,.30,.76),(.41,.11,.59,.89),(.70,.20,.30,.80),(.78,.28,.22,.69),(.77,.27,.23,.73),(.72,.32,.28,.68),(.67,.50,.33,.50),(.68,.40,.32,.60),(.67,.42,.33,.58),(.72,.41,.28,.59),(.76,.46,.24,.54),(.74,.46,.26,.54),(.72,.43,.28,.51),(.65,.31,.35,.54),(.78,.05,.22,.79),(.84,0,.16,.75),(.85,0,.15,.66)]
def keys(B):
    return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,B)]
c={"mediaId":4376,"level":"A","keyWord":"noise","defaultVoice":"female",
"taps":[{"phrase":"to bark at the camera","target":"the white dog","voice":"female","keys":keys(W)},
{"phrase":"to lie on the grass","target":"the woman in orange","voice":"female","keys":keys(O)},
{"phrase":"to wear a pink tag","target":"the grey dog","voice":"female","keys":keys(G)}],
"stillS":5.5,
"nouns":[{"word":"a fence","x":.28,"y":.20,"voice":"female"},{"word":"a tree","x":.80,"y":.10,"voice":"female"},{"word":"grass","x":.18,"y":.90,"voice":"female"},{"word":"a T-shirt","x":.85,"y":.86,"voice":"female"}],
"question":"What is the white dog doing?","answer":["It","is","barking","at","the","camera."],"answerVoice":"female",
"notes":"The two big dogs also bark/howl, but with heads up at the sky, only the white dog barks at the camera. Grey dog: state phrase (pink tag) because every action it does is shared with the black dog; the tag is hidden in some frames. Where the grey dog's legs overlap the white dog, the grey dog's box is cut at the white dog's edge."}
json.dump(c,open('content/4376.json','w'),indent=1)
