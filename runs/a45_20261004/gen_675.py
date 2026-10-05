import json
OFF=None
def keys(d):
    out=[]
    for t in sorted(d):
        b=d[t]
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2],2),"h":round(b[3],2)})
    return out
M={0.0:(.50,.41,.37,.50),0.5:(.68,.42,.28,.52),1.0:(.68,.42,.32,.58),1.5:(.72,.39,.28,.61),2.0:(.50,.40,.50,.55),2.5:(.55,.42,.43,.50),
3.0:(.44,.41,.44,.56),3.5:(.38,.41,.46,.58),4.0:(0,.50,.34,.42),4.5:(.02,.40,.50,.47),5.0:(.12,.42,.34,.54),5.5:(.16,.44,.37,.53),
6.0:(.08,.40,.35,.58),6.5:(.07,.47,.18,.27),7.0:(.11,.48,.18,.32),7.5:(.10,.48,.18,.31),8.0:(.09,.47,.18,.22),8.5:(.10,.48,.18,.24),
9.0:(.09,.47,.18,.20),9.5:(.08,.48,.18,.21),10.0:(.07,.47,.18,.19)}
W={0.0:(.87,.42,.13,.35),0.5:OFF,1.0:OFF,1.5:OFF,2.0:OFF,2.5:OFF,3.0:OFF,3.5:OFF,4.0:OFF,4.5:OFF,5.0:OFF,5.5:OFF,
6.0:(.78,.44,.20,.36),6.5:(.61,.47,.39,.53),7.0:(.60,.44,.40,.56),7.5:(.50,.43,.33,.57),8.0:(.48,.45,.30,.44),8.5:(.44,.43,.25,.41),
9.0:(.40,.45,.23,.37),9.5:(.34,.46,.23,.31),10.0:(.29,.46,.19,.28)}
B={0.0:(0,0,1,.40),0.5:(0,0,1,.40),1.0:(0,0,1,.40),1.5:(0,0,1,.38),2.0:(0,0,1,.39),2.5:(0,0,1,.40),3.0:(0,0,1,.40),3.5:(0,0,.85,.40),
4.0:(.05,0,.95,.46),4.5:(.15,0,.85,.39),5.0:(.10,0,.90,.41),5.5:(0,0,1,.43),6.0:(0,0,1,.39),6.5:(.22,0,.78,.46),7.0:(.12,0,.88,.43),
7.5:(.10,0,.90,.42),8.0:(.10,0,.90,.44),8.5:(.10,0,.90,.42),9.0:(.10,0,.90,.44),9.5:(.10,0,.90,.45),10.0:(.10,0,.90,.45)}
c={"mediaId":675,"level":"A","keyWord":"side","defaultVoice":"male",
"taps":[
{"phrase":"to bend over a bucket","target":"the man with blond hair","voice":"male","keys":keys(M)},
{"phrase":"to wear glasses","target":"the woman in glasses","voice":"female","keys":keys(W)},
{"phrase":"to turn bright blue","target":"the boat","voice":"male","keys":keys(B)}],
"stillS":3.5,
"nouns":[{"word":"a boat","x":.30,"y":.22,"voice":"male"},{"word":"a net","x":.88,"y":.54,"voice":"male"},
{"word":"a man","x":.60,"y":.64,"voice":"male"},{"word":"buckets","x":.88,"y":.77,"voice":"male"}],
"question":"What is the blond man doing?",
"answer":["He","is","painting","the","side","of","a","boat."],
"answerVoice":"male",
"notes":"The blond man bends over the paint bucket only at 4.0 s. Two women wear a bandana; only the one seen from the front wears glasses (0.0 s behind the man, 6.0 s on the right, then at the front of the line). The woman seen from behind at 4.0-5.5 s cannot be identified as her, so the woman's box is off there, and off at 0.5 s where she is almost out of the frame. A state phrase for her because every action she does (painting, smiling at the camera) is also done by others. The boat box is the hull above the people's heads only, to stay clear of the people boxes. In the line (6.5-10 s) the blond man is small; his box touches his neighbours. Key word 'side' is not placed as a noun (it would label the same place as 'a boat'); it is used in the answer."}
json.dump(c,open('content/675.json','w'),indent=1,ensure_ascii=False)
