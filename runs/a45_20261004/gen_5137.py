import json
T=[i*0.5 for i in range(25)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
woman={0.0:(.29,.34,.29,.32),0.5:(.29,.33,.28,.33),1.0:(.24,.34,.33,.33),1.5:(.23,.34,.34,.33)}
man={6.5:(.55,.51,.19,.15),7.0:(.56,.50,.19,.15),7.5:(.62,.51,.18,.16),8.0:(.60,.51,.19,.15),8.5:(.59,.51,.19,.15),
 9.0:(.59,.51,.19,.16),9.5:(.58,.51,.19,.16),10.0:(.57,.51,.19,.15),10.5:(.56,.51,.19,.15),11.0:(.55,.51,.19,.16),
 11.5:(.55,.51,.19,.16),12.0:(.55,.53,.19,.16)}
c={"mediaId":5137,"level":"B","keyWord":"parliament","defaultVoice":"male",
"taps":[
 {"phrase":"to gesture with both hands","target":"the woman in the black suit","voice":"female","keys":K(woman)},
 {"phrase":"to stand among seated members","target":"the woman in the black suit","voice":"female","keys":K(woman)},
 {"phrase":"to speak from the podium","target":"the man at the podium","voice":"male","keys":K(man)}],
"stillS":12.0,
"nouns":[{"word":"a balcony","x":0.30,"y":0.25,"voice":"male"},{"word":"steps","x":0.72,"y":0.42,"voice":"male"},
 {"word":"a podium","x":0.51,"y":0.63,"voice":"male"}],
"question":"What is happening at the podium?",
"answer":["A","man","is","speaking","from","the","podium."],"answerVoice":"male",
"notes":"Only two clear targets: the woman in the black suit (0-1.5 s, two phrases) and the small man at the central podium (6.5-12.0 s, min-size box). Raising a hand is avoided because dozens of members raise hands from 1.5 s on. 2.0-6.0 s are wide shots of the rows where neither target can be found, so both are off. A second man sits at the high desk to the right of the podium (not a target, outside the box). Key word parliament is not a single-place noun, so it is not a slot; only 3 nouns because the crowded rows leave few separable things."}
json.dump(c,open('content/5137.json','w'),indent=1)
