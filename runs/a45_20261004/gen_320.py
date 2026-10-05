import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
W={1.0:(.13,.10,.38,.76),1.5:(.20,.25,.32,.52),2.0:(.23,.34,.28,.47),4.5:(0,.34,.72,.48),5.0:(0,.39,1.0,.58),
7.5:(0,.46,.70,.36),8.0:(0,.56,.52,.26),8.5:(0,0,.42,.86),9.0:(0,0,.22,.60)}
M={1.0:(.52,.03,.40,.76),1.5:(.53,.21,.33,.54),2.0:(.52,.32,.28,.49),5.5:(.35,0,.65,1.0),6.0:(.35,0,.65,1.0),
6.5:(.40,0,.60,1.0),7.0:(.40,0,.60,1.0)}
C={2.5:(.34,.28,.50,.44),3.0:(.24,.28,.62,.50),3.5:(.16,.10,.72,.74),4.0:(.10,.03,.84,.88),4.5:(.12,.05,.38,.25),
5.0:(0,0,.34,.27),7.5:(.06,.04,.40,.27),8.0:(.22,.07,.30,.24),9.0:(.23,.15,.32,.28),9.5:(.21,.20,.34,.28),10.0:(.19,.20,.34,.27)}
c={"mediaId":320,"level":"B","keyWord":"frost","defaultVoice":"female",
"taps":[
{"phrase":"to wipe the frosty bench","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to touch a frozen leaf","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to hang between two posts","target":"the cobweb","voice":"female","keys":keys(C)}],
"stillS":10.0,
"nouns":[{"word":"a cobweb","x":.34,"y":.31,"voice":"female"},{"word":"a bench","x":.60,"y":.68,"voice":"female"},
{"word":"the sun","x":.56,"y":.22,"voice":"female"}],
"question":"What is the woman wiping?",
"answer":["She","is","wiping","the","frost","off","the","bench."],
"answerVoice":"female",
"notes":"Many cuts. The boot at 0-0.5 s cannot be tied to the man or the woman: both OFF. Woman = red coat: back view 1.0-2.0 s, red sleeve and glove wiping the bench 4.5-5.0 s, red sleeve drawing in the frost 7.5-8.0 s, head and arm 8.5 s, hair/face at the left edge 9.0 s. At 8.0 s her box holds only the arm (her hair at the top left overlaps the cobweb). Man = dark jacket: back view 1.0-2.0 s, face and finger on the leaf 5.5-7.0 s (his box is the right 60-65 % of the picture: face, finger and chest; the leaf lies partly inside). Cobweb: OFF at 8.5 s (hidden behind her head). Key word 'frost' is not a noun slot (it covers everything, no single place); it is in the answer. The sun at 10.0 s is the glow just right of the post; a small black bird stands on the grass at (.40,.51), not used."}
json.dump(c,open("content/320.json","w"),indent=1,ensure_ascii=False)
