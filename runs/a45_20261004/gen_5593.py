from gen_5592_5593_5595_5596_lib import keys, write
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
d=[(0.07,0.50,0.42,0.32),(0.07,0.50,0.43,0.32),(0.06,0.50,0.45,0.32),(0.06,0.50,0.44,0.32),
   (0.05,0.50,0.48,0.33),(0.05,0.53,0.54,0.30),(0.07,0.56,0.57,0.29),(0.07,0.62,0.61,0.23)]
dog=keys([(t,)+d[i] for i,t in enumerate(T)])
rower=keys([(t,0.24,0.36,0.38,0.14) for t in T])
dock=keys([(t,0.80,0.33,0.20,0.15) for t in T])
write(5593,{"mediaId":5593,"level":"A","keyWord":"away","defaultVoice":"male",
 "taps":[{"phrase":"to lift its paw","target":"the dog","voice":"male","keys":dog},
         {"phrase":"to row a small boat","target":"the person in the boat","voice":"male","keys":rower},
         {"phrase":"to stand on a small dock","target":"the person on the dock","voice":"male","keys":dock}],
 "stillS":0.2,
 "nouns":[{"word":"mountains","x":0.25,"y":0.25,"voice":"male"},
          {"word":"a boat","x":0.43,"y":0.45,"voice":"male"},
          {"word":"a dog","x":0.28,"y":0.66,"voice":"male"},
          {"word":"a bowl","x":0.70,"y":0.80,"voice":"male"}],
 "question":"What is the dog doing?",
 "answer":["The","dog","is","watching","the","boat."],
 "answerVoice":"male",
 "notes":"Key word 'away' is an adjective, not placed. Rower and the person on the far dock are tiny and of unclear gender, so default (male) voice. The dog lifts its paw at 0.2 s and again about 2.7 s, then lies down. Person on the dock bends over rather than standing straight; 'to stand on a small dock' still fits only them (dog sits on the jetty, rower sits in the boat)."})
