import json
T=[i*0.5 for i in range(19)]
h=[[.24,.28,.50,.31],[.24,.27,.50,.34],[.23,.28,.49,.31],[.23,.28,.51,.33],[.22,.29,.60,.38],[0,.42,1,.44],[0,.42,1,.41],[0,.42,1,.41],
[0,.42,1,.41],[0,.40,1,.41],[0,.40,1,.39],[.07,.39,.93,.41],[.16,.31,.76,.46],[.15,.19,.75,.54],[.15,.16,.75,.57],[.17,.15,.71,.58],
[.15,.13,.72,.61],[.15,.13,.72,.61],[.17,.14,.70,.59]]
def keys(b): return [{"t":t,"x":x,"y":y,"w":w,"h":hh} for t,(x,y,w,hh) in zip(T,b)]
d={"mediaId":4205,"level":"A","keyWord":"carry","defaultVoice":"male",
"taps":[
 {"phrase":"to carry a white flower","target":"the hamster","voice":"male","keys":keys(h)},
 {"phrase":"to fall on the ground","target":"the hamster","voice":"male","keys":keys(h)},
 {"phrase":"to close its eyes","target":"the hamster","voice":"male","keys":keys(h)}],
"stillS":8.0,
"nouns":[{"word":"a hamster","x":.52,"y":.25,"voice":"male"},{"word":"a flower","x":.52,"y":.45,"voice":"male"},
 {"word":"the ground","x":.50,"y":.85,"voice":"male"}],
"question":"What is the hamster carrying?",
"answer":["It","is","carrying","a","white","flower."],
"answerVoice":"male",
"notes":"Only one possible target (the hamster with its flower), used for all three phrases. 'a hamster' pill sits on the head, 'a flower' on the daisy at its chest: same figure but clearly different places. Background hedge is too blurred for a noun, so only 3 nouns."}
json.dump(d,open("content/4205.json","w"),indent=1,ensure_ascii=False)
