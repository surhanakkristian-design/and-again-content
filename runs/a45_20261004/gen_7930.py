import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
wom=[(.15,.22,.85,.78),(.12,.10,.88,.75),(.09,.25,.89,.50),(.14,.11,.84,.52),(.16,.12,.70,.43),(.28,.20,.62,.35),(.38,.24,.52,.30),(.20,.20,.68,.27)]
man=[None,(.72,.86,.28,.14),(.58,.76,.42,.24),(.52,.65,.48,.35),(.47,.57,.53,.42),(.43,.57,.57,.38),(.38,.56,.57,.40),(.33,.48,.64,.46)]
def K(b): return [dict(t=t,off=True) if v is None else dict(t=t,x=v[0],y=v[1],w=v[2],h=v[3]) for t,v in zip(T,b)]
c=dict(mediaId=7930,level="B",keyWord="partially",defaultVoice="female",
 taps=[dict(phrase="to scrub a dusty van",target="the woman",voice="female",keys=K(wom)),
       dict(phrase="to refill a metal bucket",target="the man",voice="male",keys=K(man)),
       dict(phrase="to crouch beside the van",target="the man",voice="male",keys=K(man))],
 stillS=3.7,
 nouns=[dict(word="a sponge",x=.25,y=.27,voice="female"),dict(word="a camper van",x=.22,y=.42,voice="female"),
        dict(word="a stone wall",x=.60,y=.06,voice="female"),dict(word="concrete",x=.25,y=.90,voice="female")],
 question="What is the woman doing?",answer=["She","is","scrubbing","a","dusty","camper","van."],answerVoice="female",
 notes="The camera pulls back; the man crouches in front of the woman, so the boxes are split horizontally (woman above, man below); his head is partly cut off from his box at 1.2-3.7 s and her legs from hers. At 0.2 s only his hand is at the very edge -> off; at 0.7 s only his arm and bucket show. He pours water from one bucket into another (1.2-2.2 s) and later lifts a bucket up. Key word 'partially' is not a noun and not used in the answer (adverb position would be ambiguous).")
json.dump(c,open('content/7930.json','w'),indent=1)
