import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
fox={0.0:(.30,.34,.70,.34),0.5:(.27,.27,.73,.42),1.0:(.18,.30,.82,.50),1.5:(.23,.27,.77,.45),2.0:(.29,.25,.71,.46),
2.5:(.38,.25,.62,.48),3.0:(.31,.25,.69,.48),3.5:(.29,.27,.71,.45),4.0:(.29,.27,.66,.46),4.5:(.29,.26,.69,.47),
5.0:(.28,.26,.72,.44),5.5:(.29,.26,.71,.42),6.0:(.31,.10,.53,.50),6.5:(.23,.07,.56,.69),7.0:(.18,0,.58,.86),
7.5:(.18,.13,.58,.60),8.0:(.04,.20,.75,.54),8.5:(0,.20,.76,.56),9.0:(0,.29,.82,.67),9.5:(.04,.33,.96,.67),10.0:(.38,.33,.62,.61)}
c={"mediaId":314,"level":"A","keyWord":"fox","defaultVoice":"female",
"taps":[
{"phrase":"to walk in the grass","target":"the fox","voice":"female","keys":keys(fox)},
{"phrase":"to jump very high","target":"the fox","voice":"female","keys":keys(fox)},
{"phrase":"to shake its body","target":"the fox","voice":"female","keys":keys(fox)}],
"stillS":0.5,
"nouns":[{"word":"a fox","x":.62,"y":.42,"voice":"female"},{"word":"a tree","x":.13,"y":.20,"voice":"female"},{"word":"grass","x":.50,"y":.88,"voice":"female"}],
"question":"What is the fox doing?",
"answer":["It","is","walking","in","the","cold","grass."],
"answerVoice":"female",
"notes":"Only one possible target (the fox) for all three phrases. The jump is at 6.0-7.0 s, the shake at 7.5-8.0 s. 'a tree' sits on the birch trunk at the left; a small pine stands far back at the right."}
json.dump(c,open("content/314.json","w"),indent=1,ensure_ascii=False)
