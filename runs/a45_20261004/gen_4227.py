import json
times=[i*0.5 for i in range(24)]
M={0.0:(.44,.29,.44,.58),0.5:(.44,.29,.44,.58),1.0:(.34,.29,.48,.71),1.5:(.20,.34,.60,.66),2.0:(.17,.30,.58,.70),2.5:(.19,.30,.56,.70),
3.0:(.19,.24,.55,.74),3.5:(.25,.23,.48,.77),4.0:(.05,.21,.52,.77),4.5:(.03,.21,.53,.79),5.0:(.02,.23,.48,.77),5.5:(.04,.23,.48,.77),
6.0:(.04,.23,.48,.77),6.5:(.04,.23,.48,.77),7.0:(.04,.23,.48,.77),7.5:(.12,.30,.42,.68),8.0:(.09,.29,.42,.56),8.5:(.05,.30,.48,.57),
9.0:(.0,.36,.62,.64),9.5:(.0,.31,.95,.69),10.0:(.0,.22,1.0,.78),10.5:(.02,.27,.90,.70),11.0:(.27,.36,.42,.45),11.5:(.36,.39,.30,.29)}
K={0.0:(.48,.14,.38,.15),0.5:(.48,.14,.38,.15),1.0:(.44,.14,.36,.15),1.5:(.55,.17,.25,.17),2.0:(.50,.16,.24,.14),2.5:(.50,.16,.24,.14),
3.0:(.24,.10,.42,.14),3.5:(.30,.09,.43,.14),4.0:(.07,.07,.44,.14),4.5:(.08,.07,.44,.14),5.0:(.10,.09,.46,.14),5.5:(.10,.09,.44,.14),
6.0:(.14,.09,.42,.14),6.5:(.14,.09,.42,.14),7.0:(.14,.09,.42,.14),7.5:(.18,.16,.34,.14),8.0:(.16,.15,.34,.14),8.5:(.20,.16,.34,.14),
9.0:(.30,.22,.24,.14),9.5:(.38,.10,.22,.21),10.0:(.52,.0,.48,.22),10.5:(.14,.08,.62,.19),11.0:(.32,.22,.38,.14),11.5:(.40,.25,.28,.14)}
O={3.0:(.76,.27,.24,.63),3.5:(.73,.24,.27,.68),4.0:(.60,.22,.40,.70),4.5:(.56,.25,.44,.72),5.0:(.50,.26,.48,.74),5.5:(.52,.25,.44,.75),
6.0:(.52,.27,.42,.73),6.5:(.52,.27,.42,.73),7.0:(.52,.27,.42,.73),7.5:(.60,.25,.36,.74),8.0:(.66,.24,.34,.62),8.5:(.76,.34,.24,.50)}
def keys(m):
    out=[]
    for t in times:
        if t in m:
            x,y,w,h=m[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
c={"mediaId":4227,"level":"B","keyWord":"friendly","defaultVoice":"male",
"taps":[{"phrase":"to pedal a yellow bicycle","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to stroke a fluffy dog","target":"the police officer","voice":"female","keys":keys(O)},
{"phrase":"to perch on a backpack","target":"the dog on the backpack","voice":"male","keys":keys(K)}],
"stillS":8.0,
"nouns":[{"word":"a crate","x":.25,"y":.53,"voice":"male"},{"word":"a police officer","x":.84,"y":.52,"voice":"female"},
{"word":"a police car","x":.58,"y":.41,"voice":"male"},{"word":"a bicycle","x":.25,"y":.72,"voice":"male"}],
"question":"What is the police officer doing?",
"answer":["She","is","stroking","a","friendly","dog."],
"answerVoice":"female",
"notes":"The dog in the crate is not a target, so the man's box includes it and the bicycle. The corgi sits on the backpack right behind/above the man's head: the two boxes are split on a horizontal line at about the top of the hat, so the hat crown or the corgi's chest is cut in several frames (1.5, 9.0-10.0 s especially). The officer strokes the dog at 4.5-7.0 s; her reaching arms cross into the man's box. A second officer mentioned in the description is not visible in the frames. 'a bicycle' is a simple word for level B but the clearest fourth thing at 8.0 s."}
json.dump(c,open("content/4227.json","w"),indent=1,ensure_ascii=False)
# second pass: move the split between corgi and man lower (corgi boxes sat too high)
split={0.0:.31,0.5:.31,1.0:.31,3.0:.25,3.5:.25,4.0:.24,4.5:.24,5.0:.25,5.5:.25,6.0:.25,6.5:.25,7.0:.25,8.0:.30,8.5:.32}
for t,s in split.items():
    x,y,w,h=K[t]; K[t]=(x,round(s-.14,2),w,.14)
    x,y,w,h=M[t]; M[t]=(x,s,w,round(y+h-s,2))
c["taps"][0]["keys"]=keys(M); c["taps"][2]["keys"]=keys(K)
json.dump(c,open("content/4227.json","w"),indent=1,ensure_ascii=False)
