import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
woman=K([(.19,.40,.73,.37),(.20,.41,.73,.37),(.20,.43,.74,.37),(.20,.45,.73,.36),(.21,.47,.48,.51),(.21,.49,.37,.51),(.21,.49,.38,.51),(.20,.51,.36,.49)])
sheet=K([(.38,.08,.53,.32),(.39,.08,.54,.33),(.38,.02,.52,.41),(.35,0,.51,.45),(.36,.01,.47,.46),(.39,.09,.47,.39),(.38,.11,.48,.33),(.48,.19,.40,.24)])
c={"mediaId":6967,"level":"B","keyWord":"come off","defaultVoice":"female",
"taps":[{"phrase":"to cling to the post","target":"the young woman","voice":"female","keys":woman},
{"phrase":"to grit her teeth","target":"the young woman","voice":"female","keys":woman},
{"phrase":"to come off the roof","target":"the metal sheet","voice":"female","keys":sheet}],
"stillS":2.2,
"nouns":[{"word":"a metal sheet","x":0.60,"y":0.22,"voice":"female"},{"word":"waves","x":0.85,"y":0.60,"voice":"female"},
{"word":"a dog","x":0.57,"y":0.74,"voice":"female"},{"word":"sand","x":0.80,"y":0.88,"voice":"female"}],
"question":"What is the metal sheet doing?","answer":["It","is","coming","off","the","roof."],"answerVoice":"female",
"notes":"Only the young woman and the metal sheet are clear targets; the barman and the person with the dog are small and passive, so the woman carries two phrases. The sheet's lower tip and the woman's hair are at the same height at 0.2-1.7: split horizontally at her hair. 'to grit her teeth': she clenches her teeth the whole clip."}
json.dump(c,open('content/6967.json','w'),indent=1)
