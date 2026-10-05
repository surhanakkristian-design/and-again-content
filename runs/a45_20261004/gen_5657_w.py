import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(l): return [dict(t=t,x=a,y=b,w=round(c-a,2),h=round(d-b,2)) for t,(a,b,c,d) in zip(T,l)]
priest=K([(.14,.30,.50,.83),(.12,.32,.49,.84),(.09,.32,.43,.85),(.06,.31,.39,.86),(.0,.30,.32,.91),(.0,.29,.29,.94),(.0,.29,.24,1.0),(.0,.27,.20,1.0)])
woman=K([(.64,.35,.89,.77),(.64,.35,.89,.78),(.64,.33,.89,.76),(.61,.33,.89,.77),(.58,.32,.88,.80),(.58,.32,.87,.83),(.57,.31,.88,.95),(.54,.30,.89,.97)])
c=dict(mediaId=5657,level="B",keyWord="bless",defaultVoice="male",
 taps=[dict(phrase="to sprinkle holy water",target="the priest",voice="male",keys=priest),
       dict(phrase="to press her palms together",target="the woman",voice="female",keys=woman),
       dict(phrase="to bless the woman",target="the priest",voice="male",keys=priest)],
 stillS=0.7,
 nouns=[dict(word="a church",x=0.25,y=0.20,voice="male"),dict(word="a priest",x=0.27,y=0.55,voice="male"),
        dict(word="nets",x=0.64,y=0.70,voice="male"),dict(word="a fishing boat",x=0.72,y=0.88,voice="male")],
 question="What is the priest doing?",
 answer="He is blessing the woman on the boat.".split(),
 answerVoice="male",
 notes="defaultVoice male: the priest performs the key-word action. Woman presses palms together 0.2-1.7 s, then a hand on her chest. Priest drifts out of the left edge at the end (box w 0.20 at 3.7 s). 'nets' pill sits on the orange nets next to her legs.")
json.dump(c,open('content/5657.json','w'),indent=1)
