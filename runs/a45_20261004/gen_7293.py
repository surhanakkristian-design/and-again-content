import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes): return [dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,boxes)]
cube=K([(0.38,0.51,0.20,0.14)]*8)
flame=K([(0.38,0.24,0.20,0.27),(0.38,0.24,0.20,0.27),(0.37,0.24,0.22,0.27),(0.36,0.20,0.24,0.31),
         (0.33,0.18,0.31,0.33),(0.34,0.18,0.32,0.33),(0.30,0.17,0.35,0.34),(0.30,0.17,0.36,0.34)])
door=K([(0.0,0.14,0.17,0.57)]*8)
c=dict(mediaId=7293,level="B",keyWord="lighter",defaultVoice="male",
 taps=[dict(phrase="to burn beneath the kindling",target="the firelighter",voice="male",keys=cube),
       dict(phrase="to blaze up inside the stove",target="the flame",voice="male",keys=flame),
       dict(phrase="to hang wide open",target="the stove door",voice="male",keys=door)],
 stillS=0.7,
 nouns=[dict(word="a firelighter",x=0.48,y=0.57,voice="male"),
        dict(word="kindling",x=0.30,y=0.40,voice="male"),
        dict(word="a dustpan",x=0.80,y=0.81,voice="male"),
        dict(word="gloves",x=0.15,y=0.91,voice="male")],
 question="What is happening inside the stove?",
 answer=["The","firelighter","is","burning","beneath","the","kindling."],
 answerVoice="male",
 notes="No people; evenId false -> male. Key word 'lighter' shown as a firelighter cube (pill 'a firelighter'). Flame box ends where the cube box starts (split line y=0.51). Stove door = open door panel at the left edge.")
json.dump(c,open('content/7293.json','w'),indent=1)
