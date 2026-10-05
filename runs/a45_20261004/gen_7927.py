import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
dog=[(.18,.42,.52,.37),(.18,.41,.54,.38),(.26,.41,.46,.39),(.23,.41,.49,.39),(.23,.39,.49,.40),(.25,.41,.49,.38),(.19,.47,.55,.37),(.17,.51,.57,.34)]
wom=[(.75,.21,.25,.26),(.75,.20,.25,.27),(.76,.19,.24,.27),(.76,.19,.24,.27),(.77,.18,.23,.27),(.77,.17,.23,.28),(.78,.15,.22,.29),(.78,.13,.22,.29)]
def K(b): return [dict(t=t,x=x,y=y,w=w,h=h) for t,(x,y,w,h) in zip(T,b)]
c=dict(mediaId=7927,level="A",keyWord="out",defaultVoice="female",
 taps=[dict(phrase="to wait at the door",target="the dog",voice="female",keys=K(dog)),
       dict(phrase="to carry a box",target="the dog",voice="female",keys=K(dog)),
       dict(phrase="to hold a cup",target="the woman",voice="female",keys=K(wom))],
 stillS=1.2,
 nouns=[dict(word="a door",x=.22,y=.18,voice="female"),dict(word="a woman",x=.87,y=.31,voice="female"),
        dict(word="a dog",x=.45,y=.53,voice="female"),dict(word="a box",x=.39,y=.65,voice="female")],
 question="What is the dog doing?",answer=["The","dog","is","waiting","at","the","door."],answerVoice="female",
 notes="Key word 'out' (nobody home) is not a visible noun. Only two living targets; the dog has two phrases (waits at the door the whole clip, carries a parcel/box on its neck). The woman holds a mug (called 'a cup' for level A) and drinks at 3.7 s. 'a dog' and 'a box' pills are on the same animal area but on different things (head vs parcel).")
json.dump(c,open('content/7927.json','w'),indent=1)
