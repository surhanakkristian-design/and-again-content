import json
T=[i*0.5 for i in range(19)]
W=[(.45,.41,.55,.59),(.45,.42,.55,.58),(.46,.42,.54,.58),(.44,.42,.56,.58),(.49,.42,.51,.58),(.58,.43,.42,.57),(.61,.43,.39,.57),
   (0,.46,.92,.54),(.12,.52,.64,.48),(.29,.57,.46,.43),(.34,.60,.36,.40),(.33,.62,.35,.38),(0,.33,1,.67),(.05,.49,.93,.51),
   (.18,.58,.64,.42),(.23,.63,.54,.37),(.34,.64,.30,.34),(.36,.66,.27,.31),(.36,.67,.26,.29)]
S=[(0,.03,.42,.55),(0,.04,.44,.54),(0,.09,.45,.52),(.03,.13,.40,.48),(.08,.15,.40,.43),(.13,.16,.44,.42),(.21,.17,.39,.41)]+[None]*12
def k(L):
    return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,L)]
c=dict(mediaId=5085,level="A",keyWord="statue",defaultVoice="female",
 taps=[dict(phrase="to point at the sign",target="the woman",voice="female",keys=k(W)),
       dict(phrase="to hold his chin",target="the sitting statue",voice="female",keys=k(S)),
       dict(phrase="to hold up her phone",target="the woman",voice="female",keys=k(W))],
 stillS=0.5,
 nouns=[dict(word="a statue",x=.22,y=.25,voice="female"),dict(word="trees",x=.75,y=.18,voice="female"),
        dict(word="a sign",x=.36,y=.72,voice="female"),dict(word="a phone",x=.67,y=.89,voice="female")],
 question="What is the woman pointing at?",answer="She is pointing at the sign under the statue.".split(),answerVoice="female",
 notes="Three shots: seated bronze statue (0-3.0), column with winged figure (3.5-5.5), huge metal statue with open arms (6.0-9.0). The sitting statue is only in shot 1; the small seated figures at the column base are too small to tap. 'to raise her arms' avoided because the big statue also has raised arms. At 1.5-3.0 the woman's phone hand is in front of the statue; split there, so the woman box leaves out her phone/arm. 'the sign' = the plaque on the stone base.")
json.dump(c,open('content/5085.json','w'),indent=1)
