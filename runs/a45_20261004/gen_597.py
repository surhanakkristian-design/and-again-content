import json
F=(0,.03,1,.97)
W=[F,F,F,F,(.08,.11,.92,.89),(.06,.08,.94,.92),(.18,.06,.82,.94),(.15,.02,.85,.98),(.15,.02,.85,.98),(.15,.02,.85,.98),(.16,.04,.84,.96),(.28,.06,.72,.94),(.33,.16,.67,.84),
(.48,.23,.52,.77),(.47,.36,.53,.64),(.41,.33,.54,.67),(.40,.34,.50,.66),(.34,.27,.62,.73),(.38,.24,.56,.76),(.06,.16,.94,.84),(0,.12,1,.88)]
M={6.5:(.01,.31,.22,.30),7.0:(.17,.36,.23,.28),7.5:(.15,.42,.24,.19),8.0:(.22,.40,.18,.27),8.5:(.15,.38,.19,.28),9.0:(.14,.40,.22,.25)}
T=[i*0.5 for i in range(21)]
kw=[dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,W)]
km=[dict(t=t,x=M[t][0],y=M[t][1],w=M[t][2],h=M[t][3]) if t in M else dict(t=t,off=True) for t in T]
c=dict(mediaId=597,level="A",keyWord="racket",defaultVoice="female",
taps=[dict(phrase="to look through a racket",target="the woman",voice="female",keys=kw),
dict(phrase="to stand behind the net",target="the man",voice="male",keys=km),
dict(phrase="to smile at the camera",target="the woman",voice="female",keys=kw)],
stillS=6.0,
nouns=[dict(word="flowers",x=.50,y=.08,voice="female"),dict(word="a ball",x=.42,y=.40,voice="female"),
dict(word="a net",x=.14,y=.53,voice="female"),dict(word="a racket",x=.45,y=.67,voice="female")],
question="What is the woman holding?",
answer=["She","is","holding","a","black","racket."],answerVoice="female",
notes="The man is small and far away (6.5-9.0); set off at 9.5 where only his head shows behind the woman's shoulder. At 7.5-9.0 the woman's box is cut on the left so it does not overlap the man's box (her reaching hand / braid tip / hands with the ball fall outside). Still 6.0 has a second ball in her hand (0.72, 0.78) and tiny balls on the ground; the 'a ball' pill is on the big ball in the air. The woman looks through the racket at 0-1.5 only.")
json.dump(c,open('content/597.json','w'),indent=1)
