import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(l): return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,l)]
boxer=[(.33,.29,.25,.57),(.34,.27,.26,.61),(.32,.27,.35,.67),(.34,.25,.35,.71),(.32,.24,.36,.75),(.25,.22,.39,.78),(.18,.20,.45,.80),(.23,.19,.40,.81)]
man=[(.58,.25,.36,.58),(.60,.25,.34,.61),(.67,.26,.27,.63),(.69,.25,.24,.63),(.68,.25,.25,.68),(.64,.25,.27,.69),(.63,.25,.28,.70),(.63,.25,.27,.70)]
white=[(0,.26,.33,.61),(0,.25,.34,.63),(0,.28,.24,.36),(0,.38,.18,.14),None,None,None,None]
c=dict(mediaId=5599,level="B",keyWord="backing",defaultVoice="female",taps=[
 dict(phrase="to keep her guard up",target="the boxer",voice="female",keys=K(boxer)),
 dict(phrase="to grin at the boxer",target="the man",voice="male",keys=K(man)),
 dict(phrase="to wear a loose T-shirt",target="the woman in white",voice="female",keys=K(white))],
 stillS=0.7,nouns=[dict(word="boxing gloves",x=.45,y=.44,voice="female"),dict(word="a vest",x=.80,y=.53,voice="female"),
 dict(word="a corner pad",x=.24,y=.64,voice="female"),dict(word="a towel",x=.24,y=.82,voice="female")],
 question="What is the boxer doing?",answer=["She","is","keeping","her","guard","up."],answerVoice="female",
 notes="One shot. The man stands right behind the boxer: her right glove covers his shoulder/head area, so the split runs near her right glove (x .58-.69); from 2.2 his head is partly in her box. The woman in white is outside the ropes on the left, only her arm and leg at 1.2 and only her hand on the corner post at 1.7 (weak, min-size box), gone from 2.2; phrase 3 is a state because her only action (hand on the boxer's shoulder) is shared with the man. Key word 'backing' (support) is not used: the support is shown only by the hands on the shoulders at 0.2-0.7, too abstract for the answer.")
json.dump(c,open('content/5599.json','w'),indent=1)
