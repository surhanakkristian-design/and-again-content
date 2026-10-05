import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(l): return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,l)]
dog=[(.17,.35,.53,.23),(.14,.36,.61,.22),(.14,.36,.63,.24),(.08,.36,.71,.24),(.02,.37,.75,.23),(.02,.46,.91,.15),(.19,.46,.78,.28),(.68,.40,.29,.45)]
man=[(.70,.35,.24,.63),(.75,.36,.20,.62),(.77,.37,.16,.61),(.79,.37,.16,.61),(.77,.36,.17,.62),(.63,.32,.18,.14),(.54,.32,.20,.14),(.36,.32,.32,.66)]
hand=[(0,.58,.36,.42),(0,.58,.36,.42),(0,.60,.32,.40),(0,.60,.30,.40),(0,.60,.28,.38),(0,.61,.25,.39),(0,.58,.19,.40),(0,.58,.20,.40)]
c=dict(mediaId=5598,level="A",keyWord="back",defaultVoice="male",taps=[
 dict(phrase="to lick his face",target="the dog",voice="male",keys=K(dog)),
 dict(phrase="to laugh out loud",target="the man",voice="male",keys=K(man)),
 dict(phrase="to hold the front seat",target="the hand",voice="male",keys=K(hand))],
 stillS=3.7,nouns=[dict(word="a man",x=.52,y=.50,voice="male"),dict(word="a dog",x=.82,y=.62,voice="male"),
 dict(word="a bag",x=.37,y=.71,voice="male"),dict(word="trees",x=.82,y=.06,voice="male")],
 question="Where is the dog?",answer=["The","dog","is","on","the","back","seat."],answerVoice="male",
 notes="One shot from the front seat. Dog licks the man's face 0.2-1.7, then walks over the bags and sits by him. Dog and man overlap all the time: up to 2.2 the split is near the dog's head/man's face (man box = right strip, his left leg partly outside); 2.7/3.2 the dog stands in front of him, so his box is only his head above the dog's back; 3.7 split at x .68 (dog's tail and rear outside its box). Dog box ends where the front-seat hand box starts (dog legs behind the seat partly outside). 'the hand' = the rust-sleeved hand on the front headrest; gender unknown -> defaultVoice.")
json.dump(c,open('content/5598.json','w'),indent=1)
