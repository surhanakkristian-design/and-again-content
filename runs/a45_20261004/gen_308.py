from gen_306 import keys,run
N=None
W=[(.62,.12,1,.52),(.64,.04,1,.55),(.50,.04,1,.58),N,N,N,N,(.78,.07,1,.50),(.78,.08,1,.42),(.62,.13,1,.48),(.68,.18,1,.58),(.68,.22,1,.60),
   (.68,.23,1,.52),(.70,.06,1,.42),(.72,.10,1,.42),(.64,.18,1,.50),(.74,.24,1,.60),(.56,.28,1,.58),(.58,.31,.92,.70),(.57,.33,.76,.57),(.53,.34,.71,.50)]
C=[N]*19+[(.52,.88,.90,1),(.52,.74,.87,1)]
d=dict(mediaId=308,level="A",keyWord="food",defaultVoice="female",
 taps=[dict(phrase="to have long curly hair",target="the woman with curly hair",voice="female",keys=keys(W)),
       dict(phrase="to stand under the table",target="the cat",voice="female",keys=keys(C)),
       dict(phrase="to look up at them",target="the cat",voice="female",keys=keys(C))],
 stillS=4.5,
 nouns=[dict(word="cheese",x=0.37,y=0.73,voice="female"),
        dict(word="grapes",x=0.60,y=0.62,voice="female"),
        dict(word="a woman",x=0.85,y=0.24,voice="female"),
        dict(word="a wall",x=0.40,y=0.17,voice="female")],
 question="What is on the table?",
 answer=["The","table","is","full","of","food."],answerVoice="female",
 notes="Difficult clip: fast camera moves, everybody eats and laughs, several bearded men, so no action fits only one person. Targets kept to what is unambiguous: the curly-haired woman (a state; off 1.5-3.0 s where only hands/arms show) and the cat, which is only in the last two frames (9.5 s head only, 10.0 s whole) and carries two phrases. Weak spots: at 9.5-10.0 s more women appear (one at the left with dark, slightly curly hair at 10.0 s); the box stays on the woman at the back of the table. 'to look up at them': the cat looks up towards the people at the right. Key word 'food' is general, so it is not a noun slot; it is in the answer. defaultVoice: mixed group, evenId true -> female.")
run(308,d)
