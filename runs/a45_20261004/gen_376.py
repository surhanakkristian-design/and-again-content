import json
T=[i*0.5 for i in range(20)]
R=[(.27,.27,.63,1),(.27,.27,.64,1),(.26,.28,.62,1),(.30,.27,.63,1),(.27,.27,.60,1),(.25,.27,.62,1),(.18,.29,.63,1),(.17,.29,.70,1),
(.20,.28,.62,1),(.20,.28,.65,1),(.18,.29,.62,1),(.18,.28,.65,1),(.20,.28,.70,1),(.22,.28,.72,1),(.20,.29,.87,1),(.27,.29,.87,1),
(.18,.28,.78,1),(.20,.28,.65,1),(.25,.29,.70,1),(.23,.29,.70,1)]
Mn=[(0,0,1,.13)]*12+[(.10,0,.80,.17)]*8
def K(L): return [{"t":t,"x":round(a,2),"y":round(b,2),"w":round(c-a,2),"h":round(d-b,2)} for t,(a,b,c,d) in zip(T,L)]
c={"mediaId":376,"level":"B","keyWord":"wilderness","defaultVoice":"female",
"taps":[
{"phrase":"to rush through the gorge","target":"the river","voice":"female","keys":K(R)},
{"phrase":"to foam over the rocks","target":"the river","voice":"female","keys":K(R)},
{"phrase":"to rise in the distance","target":"the distant mountains","voice":"female","keys":K(Mn)}],
"stillS":6.0,
"nouns":[{"word":"a forest","x":.72,"y":.25,"voice":"female"},
{"word":"a cliff","x":.20,"y":.48,"voice":"female"},
{"word":"a river","x":.45,"y":.80,"voice":"female"}],
"question":"What is the river doing?",
"answer":["It","is","rushing","through","the","wilderness."],
"answerVoice":"female",
"notes":"Pure landscape, no person or animal. Two phrases share the river; the third target is the far mountain ridge at the top (a top band), the weakest one: please check that band. The forest was not used as a tap target because it lies on both sides of the river. Key word 'wilderness' is abstract, so it is not a noun slot; it is in the answer. Only 3 nouns."}
json.dump(c,open("content/376.json","w"),indent=1,ensure_ascii=False)
