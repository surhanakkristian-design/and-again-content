import json
B=[(0.0,(0,.04,.72,.80)),(0.5,(0,.04,.76,.80)),(1.0,(0,.03,.77,.80)),(1.5,(0,0,.67,.80)),(2.0,(0,0,.52,1)),(2.5,(0,0,.52,1)),(3.0,(0,0,.53,1)),
(3.5,(0,0,.60,1)),(4.0,(0,0,.60,1)),(4.5,(0,0,.70,1)),(5.0,(0,0,.70,1)),(5.5,(0,0,.72,1)),(6.0,(0,0,.68,1)),(6.5,(0,0,.70,1)),(7.0,(0,0,.68,1)),
(7.5,(0,0,.75,1)),(8.0,(0,0,.82,1)),(8.5,(0,0,.73,1)),(9.0,(0,0,.64,1)),(9.5,(0,0,.66,1)),(10.0,(0,0,.64,1))]
K=[{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in B]
c={"mediaId":5199,"level":"B","keyWord":"follow","defaultVoice":"female",
"taps":[{"phrase":"to follow a handwritten recipe","target":"the woman","voice":"female","keys":K},
{"phrase":"to slice cherry tomatoes","target":"the woman","voice":"female","keys":K},
{"phrase":"to drizzle olive oil","target":"the woman","voice":"female","keys":K}],
"stillS":6.0,
"nouns":[{"word":"a headscarf","x":.45,"y":.17,"voice":"female"},{"word":"an apron","x":.12,"y":.72,"voice":"female"},
{"word":"a salad bowl","x":.56,"y":.79,"voice":"female"},{"word":"a red pepper","x":.85,"y":.62,"voice":"female"}],
"question":"What is the woman following?","answer":["She","is","following","a","handwritten","recipe."],"answerVoice":"female",
"notes":"only one person; all three phrases on the woman (the recipe page only leans/is held). Her body runs off the left and bottom edges, so boxes start at x 0. 'recipe' is inferred from the handwritten page she reads while cooking."}
json.dump(c,open('content/5199.json','w'),indent=1)
