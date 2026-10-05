import json
T=[i*0.5 for i in range(25)]
bow=[[.12,.21,.80,.47],[.12,.20,.80,.47],[.10,.20,.80,.46],[.07,.20,.85,.47],[.12,.18,.80,.49],[.12,.17,.82,.50],[.09,.17,.86,.51],[.07,.16,.89,.52],[.07,.16,.89,.53],
[0,.25,.71,.50],[0,.26,.66,.46],[0,.22,.60,.50],[0,.21,.53,.53],[.02,.20,.48,.54],[.03,.21,.47,.52],[.05,.21,.46,.53],[.03,.21,.47,.56]]+[None]*8
gl=[None]*10+[[.67,.26,.33,.52],[.61,.24,.39,.70],[.54,.24,.46,.58],[.51,.24,.49,.60],[.51,.24,.49,.60],[.52,.25,.48,.60],[.51,.24,.49,.60]]+[None]*8
def keys(b): return [({"t":t,"x":k[0],"y":k[1],"w":k[2],"h":k[3]} if k else {"t":t,"off":True}) for t,k in zip(T,b)]
d={"mediaId":4207,"level":"B","keyWord":"deliver","defaultVoice":"male",
"taps":[
 {"phrase":"to deliver a pizza","target":"the hamster in glasses","voice":"male","keys":keys(gl)},
 {"phrase":"to scroll on a phone","target":"the hamster in the bow","voice":"male","keys":keys(bow)},
 {"phrase":"to lounge on a sofa","target":"the hamster in the bow","voice":"male","keys":keys(bow)}],
"stillS":0.0,
"nouns":[{"word":"a bow","x":.42,"y":.27,"voice":"male"},{"word":"a lampshade","x":.88,"y":.35,"voice":"male"},
 {"word":"a pizza box","x":.66,"y":.64,"voice":"male"},{"word":"a rug","x":.40,"y":.90,"voice":"male"}],
"question":"What is the hamster in glasses doing?",
"answer":["It","is","delivering","a","pizza."],
"answerVoice":"male",
"notes":"Last shot (8.5-12.0 s): both hamsters sit under a blanket without bow or glasses and cannot be told apart, so both targets are off there. Continuity flaw of the clip: a pizza box already lies on the table in the first shot, before the hamster in glasses brings one (5.0-6.0 s). 'to lounge on a sofa' fits only the bow hamster in the shots where the two can be told apart (0-8 s); in the last shot both sit together. During the hug (6.5-8.0 s) the boxes are split on the vertical line between the two faces. Animals -> default voice (odd id -> male)."}
json.dump(d,open("content/4207.json","w"),indent=1,ensure_ascii=False)
