import json
T=[i*0.5 for i in range(25)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
M={0.0:(.04,.20,.76,.53),0.5:(0,.10,1,.78),1.0:(0,.04,1,.62),1.5:(0,.05,1,.62),2.0:(0,.04,.88,.58),
 5.5:(0,0,.78,.48),6.0:(0,0,.80,.55),6.5:(0,.02,1,.71),7.0:(0,.02,1,.70),7.5:(0,.02,1,.65),8.0:(0,.03,.85,.60),8.5:(0,.02,.95,.62),
 9.0:(0,.08,1,.56),9.5:(0,.06,1,.62),10.0:(0,0,1,.78),10.5:(0,0,1,.80),11.0:(0,.05,1,.80),11.5:(0,.05,1,.90),12.0:(0,0,1,.92)}
c={"mediaId":5171,"level":"A","keyWord":"add","defaultVoice":"male",
"taps":[{"phrase":"to add some vegetables","target":"the man","voice":"male","keys":K(M)},
{"phrase":"to put the lid on","target":"the man","voice":"male","keys":K(M)},
{"phrase":"to stir the soup","target":"the man","voice":"male","keys":K(M)}],
"stillS":9.0,
"nouns":[{"word":"an apron","x":0.50,"y":0.45,"voice":"male"},{"word":"soup","x":0.50,"y":0.75,"voice":"male"},
{"word":"a pot","x":0.50,"y":0.95,"voice":"male"}],
"question":"What is he adding to the pot?","answer":["He","is","adding","some","vegetables."],"answerVoice":"male",
"notes":"Only one person, so all three phrases share the man. 2.5-5.0 s are close-ups of the pot with only the bowl/jug and a sliver of his shirt at the left edge -> off. 5.5-6.0 s only his gloved hand (boxed). The dish is a vegetable stew; called 'soup' for level A since it looks liquid. Only 3 nouns: nothing else separate and clear at 9.0 s."}
json.dump(c,open('content/5171.json','w'),indent=1)
