import json
OFF=None
def keys(d):
    out=[]
    for t in sorted(d):
        b=d[t]
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2],2),"h":round(b[3],2)})
    return out
W={0.0:(.03,.13,.92,.63),0.5:(0,0,1,.72),1.0:(0,0,1,.68),1.5:(0,.28,1,.72),2.0:(0,.12,1,.88),2.5:(0,.12,1,.88),3.0:(0,.28,1,.72),
3.5:(0,.25,1,.75),4.0:(0,.22,1,.78),4.5:OFF,5.0:(0,.38,.85,.52),5.5:(.10,0,.78,.30),6.0:(0,0,.95,1),6.5:(.06,.19,.84,.66),
7.0:(0,.31,.95,.60),7.5:(.03,.28,.90,.60),8.0:(.02,.27,.90,.65),8.5:(.02,.30,.92,.66),9.0:(.02,.29,.90,.69)}
L={t/2:OFF for t in range(19)}
L.update({0.0:(.22,0,.56,.12),6.5:(.22,0,.58,.16),7.0:(.22,0,.60,.15),7.5:(.24,0,.58,.16),8.0:(.22,0,.60,.20),8.5:(.24,0,.59,.20),9.0:(.22,0,.62,.22)})
c={"mediaId":679,"level":"A","keyWord":"silver","defaultVoice":"female",
"taps":[
{"phrase":"to clean silver with a cloth","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to put on earrings","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to shine above her head","target":"the lamp","voice":"female","keys":keys(L)}],
"stillS":9.0,
"nouns":[{"word":"a lamp","x":.52,"y":.11,"voice":"female"},{"word":"silver","x":.70,"y":.57,"voice":"female"},
{"word":"a woman","x":.28,"y":.76,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","cleaning","silver","with","a","cloth."],
"answerVoice":"female",
"notes":"Only one person. In the close-ups (1.5-4.0 s, 5.0-6.0 s) only her hands (and at 6.0 s her ear) are in the picture: the woman's box is on these visible parts; at 3.0-4.0 s her face is a reflection in the silver disc, inside the same box. 4.5 s shows only the discs: woman off. The lamp is in the picture at 0.0 s and 6.5-9.0 s. She rubs with the cloth at 2.0-3.0 s and 5.0-6.0 s, puts the earrings on at 7.0 s. 'silver' = the shiny discs in her hands at 9.0 s (that they are silver is the key word of the clip, the picture shows shiny silver-coloured metal). Only 3 nouns: the chain is there twice at 9.0 s (neck and table), the earrings are two."}
json.dump(c,open('content/679.json','w'),indent=1,ensure_ascii=False)
