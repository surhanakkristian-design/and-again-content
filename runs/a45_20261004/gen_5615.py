import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(b): return [dict(t=t,x=v[0],y=v[1],w=v[2],h=v[3]) if v else dict(t=t,off=True) for t,v in zip(T,b)]
cook=K([(.32,.33,.44,.67),(.31,.34,.49,.66),(.30,.33,.50,.67),(.33,.32,.49,.68),(.32,.31,.50,.69),(.31,.29,.51,.71),(.28,.28,.54,.72),(.30,.29,.52,.71)])
wom=K([(.76,.45,.24,.55),(.80,.44,.20,.56),(.80,.43,.20,.57),(.82,.42,.18,.58),(.82,.40,.18,.60),(.82,.40,.18,.60),(.82,.55,.18,.45),(.82,.62,.18,.38)])
c=dict(mediaId=5615,level="A",keyWord="be famous for",defaultVoice="male",
 taps=[dict(phrase="to throw noodles into the air",target="the cook",voice="male",keys=cook),
       dict(phrase="to cook noodles in a pan",target="the cook",voice="male",keys=cook),
       dict(phrase="to pour soup into cups",target="the woman",voice="female",keys=wom)],
 stillS=2.2,
 nouns=[dict(word="lanterns",x=.62,y=.20,voice="male"),dict(word="people",x=.15,y=.55,voice="male"),
        dict(word="a pan",x=.30,y=.74,voice="male"),dict(word="cups",x=.80,y=.92,voice="male")],
 question="What is the cook doing?",
 answer=["He","is","cooking","noodles","in","a","pan."],answerVoice="male",
 notes="The woman is cut off at the right edge from 2.7 s; at 3.2/3.7 s only her arm with the ladle is visible, box kept on it. Cook box stops at x .82 so it does not overlap hers. Wok called 'a pan' for level A.")
json.dump(c,open("content/5615.json","w"),indent=1)
