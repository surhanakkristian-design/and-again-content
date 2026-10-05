import json
T=[i*0.5 for i in range(25)]
M={0.0:(0,0,.92,.67),0.5:(0,0,.95,.66),1.0:(0,0,.95,.68),1.5:(.03,0,.92,.69),2.0:(0,0,.90,.69),2.5:(.14,0,.82,.69),
3.0:(.05,.03,.88,.66),3.5:(.14,.02,.82,.67),4.0:(0,.02,.95,.70),4.5:(.02,0,.98,.70),5.0:(.02,.13,.95,.58),5.5:(0,.12,.95,.59),
6.0:(.08,0,.84,.69),6.5:(.06,0,.90,.68),7.0:(.08,.03,.84,.66),7.5:(.03,.02,.90,.67),8.0:(.06,.06,.86,.60),
8.5:(.10,0,.90,.70),9.0:(.14,.05,.86,.70),9.5:(.15,.03,.85,.72),10.0:(.15,0,.85,.90),10.5:(.40,.03,.60,.86),
11.0:(.45,.10,.55,.68),11.5:(.29,.12,.71,.70),12.0:(.43,.08,.57,.76)}
Wt={0.0:(.03,.68,.88,.20),0.5:(.03,.67,.88,.19),1.0:(.03,.69,.88,.19),1.5:(.03,.70,.88,.18),2.0:(.03,.69,.92,.22),
2.5:(.03,.69,.94,.23),3.0:(.02,.69,.92,.24),3.5:(.03,.69,.94,.24),4.0:(.03,.73,.94,.20),4.5:(.03,.72,.94,.21),
5.0:(.02,.72,.94,.21),5.5:(.02,.72,.94,.21),6.0:(.03,.70,.93,.23),6.5:(.03,.70,.94,.22),7.0:(.02,.70,.93,.23),
7.5:(.03,.70,.94,.22),8.0:(.02,.67,.94,.24)}
def keys(b):
    return [{"t":t,"off":True} if b.get(t) is None else dict(zip("txywh",(t,)+b[t])) for t in T]
mk=keys(M)
c={"mediaId":5296,"level":"A","keyWord":"traditional","defaultVoice":"male",
"taps":[{"phrase":"to stir with a wooden spoon","target":"the young man","voice":"male","keys":mk},
{"phrase":"to hold a piece of cheese","target":"the young man","voice":"male","keys":mk},
{"phrase":"to boil in a big pot","target":"the water","voice":"male","keys":keys(Wt)}],
"stillS":12.0,
"nouns":[{"word":"a hat","x":0.72,"y":0.18,"voice":"male"},{"word":"a spoon","x":0.26,"y":0.45,"voice":"male"},
{"word":"a bowl","x":0.25,"y":0.66,"voice":"male"},{"word":"a table","x":0.45,"y":0.86,"voice":"male"}],
"question":"What is the young man doing?","answer":["He","is","cooking","a","traditional","dish."],"answerVoice":"male",
"notes":"The hikers in the back (8.5-12.0) are small and blurred, so the third target is the boiling water in the pot (clearly boiling 0.0-3.5, covered by cheese and bacon from 4.0; box kept while the pot is visible, off from 8.5 when the clip cuts to the bowl). Man and water boxes are split at the pot rim (~y .69); his spoon/hands reaching into the pot are left in the water box. 'to stir with a wooden spoon' best at 2.0-3.5 and 6.5-8.0; 'to hold a piece of cheese' at 2.0-3.5."}
json.dump(c,open('content/5296.json','w'),indent=1)
