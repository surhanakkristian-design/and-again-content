import json
T=[i*0.5 for i in range(21)]
# split x per frame: man 0..mx, woman wx..1
sp={0.0:(.56,.57),0.5:(.56,.57),1.0:(.56,.57),1.5:(.56,.57),2.0:(.76,.77),2.5:(.71,.72),3.0:(.62,.63),3.5:(.62,.63),4.0:(.56,.57),4.5:(.62,.63),5.0:(.62,.63),5.5:(.62,.63),6.0:(.62,.63),6.5:(.62,.63),7.0:(.70,.71),7.5:(.66,.67),8.0:(.58,.60),8.5:(.57,.60),9.0:(.60,.62),9.5:(.62,.64),10.0:(.50,.52)}
mtop={0.0:.08,0.5:.08,1.0:.08,1.5:.08,10.0:.05}
man=[];wom=[]
for t in T:
    mx,wx=sp[t]; y=mtop.get(t,0.0)
    man.append({"t":t,"x":0,"y":y,"w":mx,"h":round(0.9-y,2)})
    wom.append({"t":t,"x":wx,"y":0.29,"w":round(1-wx,2),"h":0.35})
c={"mediaId":239,"level":"B","keyWord":"doubt","defaultVoice":"male",
"taps":[
 {"phrase":"to examine a gold ring","target":"the man","voice":"male","keys":man},
 {"phrase":"to grin at the customer","target":"the old woman","voice":"female","keys":wom},
 {"phrase":"to frown in doubt","target":"the man","voice":"male","keys":man}],
"stillS":10.0,
"nouns":[{"word":"a ring","x":0.54,"y":0.79,"voice":"male"},{"word":"a headscarf","x":0.88,"y":0.36,"voice":"male"},{"word":"a jacket","x":0.22,"y":0.52,"voice":"male"},{"word":"clouds","x":0.62,"y":0.14,"voice":"male"}],
"question":"What is the man examining?",
"answer":["He","is","examining","a","gold","ring."],
"answerVoice":"male",
"notes":"Man and old woman stand close; boxes split along a vertical line between them, so the woman's box may cut her near arm. 'to frown in doubt' uses the key word; the woman smiles throughout."}
json.dump(c,open('content/239.json','w'),indent=1,ensure_ascii=False)
