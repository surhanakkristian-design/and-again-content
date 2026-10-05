import json
T=[i*0.5 for i in range(25)]
W=[(.40,.15,.46,.55),(.40,.12,.46,.52),(.38,.10,.46,.55),(.34,.11,.52,.60),(.30,.11,.55,.64),(.30,.13,.53,.62),
(.50,.16,.49,.47),(.48,.15,.51,.45),(.40,.15,.57,.44),(.36,.16,.50,.40),(.30,.17,.52,.40),(.33,.18,.52,.38),
(.60,.15,.39,.32),(.48,.18,.38,.30),(.44,.20,.40,.28),(.48,.20,.46,.26),(.52,.27,.30,.28),(.53,.27,.28,.27),
(.52,.29,.27,.27),(.46,.29,.39,.27),(.10,.12,.86,.42),(.28,.30,.55,.25),(.35,.38,.52,.18),(.36,.37,.38,.17),(.36,.35,.36,.17)]
keys=[dict(t=t,x=a,y=b,w=c,h=d) for t,(a,b,c,d) in zip(T,W)]
c={"mediaId":5152,"level":"A","keyWord":"bedroom","defaultVoice":"female",
"taps":[{"phrase":p,"target":"the woman","voice":"female","keys":keys} for p in
 ["to put down a white pillow","to throw pillows on the bed","to fall into the pillows"]],
"stillS":9.0,
"nouns":[{"word":"a curtain","x":0.12,"y":0.25,"voice":"female"},{"word":"a wall","x":0.45,"y":0.15,"voice":"female"},
 {"word":"a woman","x":0.66,"y":0.38,"voice":"female"},{"word":"pillows","x":0.50,"y":0.75,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","throwing","pillows","on","the","bed."],"answerVoice":"female",
"notes":"Only one person, so all three phrases target the woman (pillows are things that do nothing by themselves). From 10.5 s she lies in the heap: only her head, hair and jeans show, small boxes there. 'bedroom' itself is not a placeable noun."}
json.dump(c,open('content/5152.json','w'),indent=1)
