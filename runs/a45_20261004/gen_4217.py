import json
# t: (car x0, car x1, car y0, split y)
D={0.0:(.34,.54,.11,.25),0.5:(.36,.56,.11,.25),1.0:(.37,.59,.13,.27),1.5:(.39,.61,.13,.27),
2.0:(.39,.62,.13,.27),2.5:(.39,.63,.13,.27),3.0:(.38,.63,.13,.27),3.5:(.38,.62,.12,.26),
4.0:(.37,.64,.12,.26),4.5:(.38,.65,.12,.27),5.0:(.37,.66,.12,.29),5.5:(.36,.69,.12,.31),
6.0:(.34,.69,.10,.31),6.5:(.31,.71,.09,.31),7.0:(.28,.72,.09,.32),7.5:(.26,.75,.08,.32),
8.0:(.22,.79,.06,.33),8.5:(.18,.84,.04,.33),9.0:(.12,.92,.02,.33),9.5:(.03,.99,.0,.33),
10.0:(.0,1.0,.0,.31),10.5:(.0,1.0,.0,.27),11.0:(.05,.97,.01,.26),11.5:(.12,.91,.02,.28)}
ck=[];dk=[]
for t in sorted(D):
    x0,x1,y0,s=D[t]
    ck.append({"t":t,"x":x0,"y":y0,"w":round(x1-x0,2),"h":round(s-y0,2)})
    dk.append({"t":t,"x":0.27,"y":s,"w":0.46,"h":round(0.64-s,2)})
c={"mediaId":4217,"level":"A","keyWord":"police","defaultVoice":"male",
"taps":[
 {"phrase":"to sit in a green car","target":"the dog","voice":"male","keys":dk},
 {"phrase":"to follow the dog","target":"the police car","voice":"male","keys":ck},
 {"phrase":"to come closer","target":"the police car","voice":"male","keys":ck}],
"stillS":7.5,
"nouns":[{"word":"the sky","x":0.30,"y":0.06,"voice":"male"},{"word":"a police car","x":0.52,"y":0.22,"voice":"male"},
 {"word":"a dog","x":0.50,"y":0.41,"voice":"male"},{"word":"a road","x":0.50,"y":0.88,"voice":"male"}],
"question":"What is the police car doing?",
"answer":["It","is","following","the","dog."],"answerVoice":"male",
"notes":"The green go-kart is called 'a green car' for level A. The dog box is the dog only (not the kart). From about 8.0 s the police car is right behind the dog and overlaps it in the picture: the boxes are split on a horizontal line at the top of the dog's ears, so the car box covers only the part of the car above the dog. No person in the clip, evenId false -> male voice."}
json.dump(c,open('content/4217.json','w'),indent=1,ensure_ascii=False)
