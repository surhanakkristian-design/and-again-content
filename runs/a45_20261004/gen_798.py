import json
T=[i*0.5 for i in range(21)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=v; out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
W={0.0:(0,0,1,1),0.5:(0,0,1,1),1.0:(0,0,1,1),1.5:(0,0,1,1),
2.0:(0,0,.87,1),2.5:(.08,.03,.85,1),3.0:(.05,.06,.69,1),3.5:(.08,.07,.71,1),
4.0:(0,.12,.72,1),4.5:(.03,.18,.71,1),5.0:(.05,.24,.76,1),5.5:(.15,.24,.78,1),
6.0:(.44,.24,.88,.88),6.5:(.62,.33,1,.84),7.0:(.66,.28,1,.90),7.5:(.68,.21,.99,.90),
8.0:(.70,.20,1,.80),8.5:(.72,.15,1,.84),9.0:(.77,.18,1,1),9.5:(.87,.08,1,1)}
O={2.0:(.87,.42,1,.66),2.5:(.85,.40,1,.62),3.0:(.69,.39,.93,.64),3.5:(.71,.36,.95,.60),
4.0:(.72,.36,.95,.69),4.5:(.71,.34,.95,.68),5.0:(.76,.44,.97,.77),5.5:(.78,.42,1,.77),6.0:(.88,.34,1,.65)}
M={5.5:(0,.25,.15,.95),6.0:(0,.12,.44,.87),6.5:(.31,.32,.62,.80),7.0:(.34,.28,.66,.88),7.5:(.33,.20,.67,.90),
8.0:(.32,.18,.69,.80),8.5:(.29,.13,.71,.84),9.0:(.25,.14,.77,1),9.5:(.10,0,.86,1)}
c={"mediaId":798,"level":"B","keyWord":"tracksuit","defaultVoice":"female",
"taps":[
{"phrase":"to zip up a jacket","target":"the young woman","voice":"female","keys":K(W)},
{"phrase":"to water the potted plants","target":"the elderly woman","voice":"female","keys":K(O)},
{"phrase":"to have a thick moustache","target":"the man with the moustache","voice":"male","keys":K(M)}],
"stillS":4.0,
"nouns":[{"word":"laundry","x":.22,"y":.25,"voice":"female"},
{"word":"a scooter","x":.16,"y":.57,"voice":"female"},
{"word":"a tracksuit","x":.42,"y":.73,"voice":"female"},
{"word":"a watering can","x":.80,"y":.52,"voice":"female"}],
"question":"What is the young woman doing?",
"answer":["She","is","dancing","in","a","turquoise","tracksuit."],
"answerVoice":"female",
"notes":"Boxes of the young woman are cut on the right (3.0-5.5 s) where the elderly woman stands behind her pulled-out trousers / arm. Elderly woman set off at 6.5-7.0 (only a sliver at the right edge) and 9.5 (tiny, far). 10.0 s is an unidentifiable trouser close-up: all off. Moustache phrase is a state: both men do the same actions. Watering can is small at 4.0 s."}
json.dump(c,open("content/798.json","w"),indent=1,ensure_ascii=False)
