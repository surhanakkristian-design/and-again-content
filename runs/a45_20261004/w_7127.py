from gen_7120_7121_7125_7127_w import K,write
T=[0.2,0.7,1.2,1.7,2.2]
win=[(.03,.0,.30,.32),(.05,.0,.29,.31),(.05,.02,.28,.27),(.05,.06,.24,.23),(.05,.13,.20,.21)]
boat=[(.46,.32,.25,.31),(.48,.34,.23,.31),(.48,.43,.25,.30),(.50,.45,.25,.29),(.47,.52,.33,.16)]
dog=[(.27,.47,.19,.18),(.25,.49,.23,.19),(.27,.50,.21,.22),(.29,.53,.21,.24),(.39,.68,.22,.14)]
write(7127,{"mediaId":7127,"level":"A","keyWord":"flood","defaultVoice":"female",
"taps":[
 {"phrase":"to take a bag of bread","target":"the woman in the window","voice":"female","keys":K(T,win)},
 {"phrase":"to reach up to the window","target":"the woman in the boat","voice":"female","keys":K(T,boat)},
 {"phrase":"to look up at the bread","target":"the dog","voice":"female","keys":K(T,dog)}],
"stillS":0.2,
"nouns":[{"word":"a ball","x":0.10,"y":0.82,"voice":"female"},{"word":"apples","x":0.86,"y":0.80,"voice":"female"},
 {"word":"a boat","x":0.47,"y":0.72,"voice":"female"},{"word":"a dog","x":0.38,"y":0.56,"voice":"female"}],
"question":"What is in the street?",
"answer":["There","is","a","flood","in","the","street."],
"answerVoice":"female",
"notes":"Dog sits in front of the boat woman: boxes split at x~0.46-0.50 (her raised arm at 0.2-0.7 falls outside her box); at 2.2 split by height (woman above y 0.68, dog below). Boat woman reaches up only 0.2-0.7, then sits and paddles. Dog looks up at the bag 0.2-1.7."})
