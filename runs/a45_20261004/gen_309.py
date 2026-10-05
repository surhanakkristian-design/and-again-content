from gen_306 import keys,run
N=None
W=[(.04,0,.58,.50),(.16,0,.68,.47),(.04,0,.58,.70),(.20,0,.90,.82),(0,0,.52,.62),(.06,0,.62,.50),N,(.18,.16,.64,.68),(0,.20,.50,.78),(0,.22,.40,.76),
   N,N,N,N,(0,.40,.56,1),(0,.40,.94,1),(0,.23,.97,.86),(0,.26,1,.86),(.22,.32,.76,.93),(.22,.30,.82,.93),(.30,.28,.86,.88)]
B=[(.39,.50,.69,.68),(.38,.47,.68,.63),(.58,.44,.78,.62),N,(.56,.56,.86,.75),(.21,.50,.56,.70),(.66,.58,.92,.77),(.50,.68,.74,.84),(.56,.61,.80,.78),(.40,.62,.60,.79),
   (.61,.27,.79,.41),(.60,.26,.78,.40),(.78,.38,.96,.52),(.72,.38,.90,.52)]+[N]*7
G=[N]*10+[(.53,.41,.82,.61),(.29,.40,.67,.64),(.28,.35,.78,.60),(.46,.52,1,.67)]+[N]*7
d=dict(mediaId=309,level="A",keyWord="football",defaultVoice="female",
 taps=[dict(phrase="to score a goal",target="the woman",voice="female",keys=keys(W)),
       dict(phrase="to jump for the ball",target="the man in the goal",voice="male",keys=keys(G)),
       dict(phrase="to fly into the goal",target="the ball",voice="female",keys=keys(B))],
 stillS=5.0,
 nouns=[dict(word="a football",x=0.70,y=0.32,voice="female"),
        dict(word="a man",x=0.67,y=0.46,voice="male"),
        dict(word="the sea",x=0.22,y=0.44,voice="female"),
        dict(word="sand",x=0.50,y=0.85,voice="female")],
 question="What are they playing?",
 answer=["They","are","playing","football","on","the","sand."],answerVoice="female",
 notes="Woman in the green shirt: off at 3.0 s (hidden behind the man in blue) and 5.0-6.5 s (goal shots). Where the ball lies at her feet the two boxes are split, which cuts her feet in a few frames. The man in the goal is boxed only 5.0-6.5 s; one of the two men who hug her from 8.5 s (dark shirt, blue shorts) may be the same person, but he is not in the goal there and cannot be told for sure, so he is off. Ball at 6.0-6.5 s is small and faint in the net. Other men (defenders, man in blue) are not targets. Key word 'football' is the noun on the ball.")
run(309,d)
