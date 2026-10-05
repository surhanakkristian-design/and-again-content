import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(l): return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,l)]
woman=[(.03,.21,.43,.56),(.07,.20,.38,.58),(.04,.20,.43,.59),(.07,.19,.39,.61),(.06,.19,.42,.62),(.07,.18,.39,.64),(.15,.17,.32,.67),(.05,.17,.41,.67)]
man=[(.47,.27,.39,.29),(.46,.27,.41,.29),(.48,.26,.41,.31),(.47,.25,.42,.32),(.49,.24,.43,.34),(.47,.24,.44,.33),(.48,.24,.44,.26),(.47,.24,.47,.25)]
dog=[(.74,.56,.26,.18),(.73,.56,.27,.17),(.75,.57,.25,.17),(.75,.57,.25,.17),(.76,.58,.24,.17),(.75,.57,.25,.18),(.76,.50,.24,.26),(.77,.49,.23,.24)]
c=dict(mediaId=5600,level="A",keyWord="bad",defaultVoice="female",taps=[
 dict(phrase="to hold up the lid",target="the woman",voice="female",keys=K(woman)),
 dict(phrase="to cover his nose",target="the man",voice="male",keys=K(man)),
 dict(phrase="to lie on the grass",target="the dog",voice="female",keys=K(dog))],
 stillS=0.2,nouns=[dict(word="the sky",x=.50,y=.07,voice="female"),dict(word="trees",x=.60,y=.18,voice="female"),
 dict(word="a dog",x=.86,y=.62,voice="female"),dict(word="a box",x=.15,y=.78,voice="female")],
 question="What is the food like?",answer=["The","food","in","the","box","is","bad."],answerVoice="female",
 notes="One shot. The woman holds the cool-box lid up 0.2-3.2 and pushes it down at 3.7 (her box covers her hands on the lid, not the whole lid). Woman and man touch at x ~.46, split there. The man's bent head reaches x ~.85-.90, right above the dog: split horizontally at the dog's back/head top, so the man's box is his head, arms and shirt (his navy trousers below the split are outside his box) and the dog's box is the whole dog. The dog lies on the grass until 2.7, then gets up (3.2-3.7), so phrase 3 covers most but not the last second. Answer: the mouldy flatbread is clearly visible in the open box; 'a box' = the cool box.")
json.dump(c,open('content/5600.json','w'),indent=1)
