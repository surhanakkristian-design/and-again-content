import json
W={0.0:(.28,.12,.62,.43),0.5:(.15,.06,.85,.46),1.0:(.10,.07,.85,.44),1.5:(.08,.07,.90,.44),2.0:(.05,.08,.93,.43),2.5:(.00,.00,.58,.30),3.0:None,3.5:None,
4.0:(.30,.35,.70,.45),4.5:(.36,.40,.64,.42),5.0:(.16,.37,.84,.63),5.5:(.48,.40,.52,.60),6.0:(.62,.00,.38,.62),6.5:(.62,.28,.38,.55),7.0:(.56,.33,.44,.55),
7.5:(.30,.00,.70,.45),8.0:(.36,.00,.64,.32),8.5:(.50,.05,.50,.27),9.0:(.50,.00,.50,.36),9.5:(.64,.00,.36,.36),10.0:(.05,.00,.95,.60),10.5:(.55,.00,.45,.60),
11.0:(.60,.00,.40,.53),11.5:(.40,.00,.60,.52),12.0:(.38,.00,.62,.52)}
T={0.0:(.17,.56,.60,.44),0.5:(.17,.53,.62,.47),1.0:(.15,.52,.62,.48),1.5:(.15,.52,.62,.48),2.0:(.15,.52,.62,.48),2.5:None,3.0:(.00,.27,.90,.73),3.5:(.00,.26,.95,.74),
4.0:(.00,.42,.18,.38),4.5:(.00,.42,.18,.36),5.0:(.00,.42,.15,.36),5.5:(.10,.42,.37,.45),6.0:(.00,.31,.56,.48),6.5:(.00,.36,.60,.46),7.0:(.00,.42,.55,.45)}
def keys(d):
    out=[]
    for t in [x/2 for x in range(25)]:
        v=d.get(t)
        out.append(dict(t=t,x=v[0],y=v[1],w=v[2],h=v[3]) if v else dict(t=t,off=True))
    return out
c=dict(mediaId=5283,level="A",keyWord="tower",defaultVoice="female",taps=[
 dict(phrase="to wash the plates",target="the woman",voice="female",keys=keys(W)),
 dict(phrase="to wipe the sink",target="the woman",voice="female",keys=keys(W)),
 dict(phrase="to stand in the sink",target="the tower of plates",voice="female",keys=keys(T))],
 stillS=2.0,nouns=[dict(word="a woman",x=.40,y=.38,voice="female"),dict(word="a window",x=.82,y=.25,voice="female"),
 dict(word="a tower",x=.45,y=.78,voice="female")],
 question="What is the woman doing?",answer=["She","is","washing","the","plates."],answerVoice="female",
 notes="Woman is often only hands/arm (close-ups 2.5-10.5); her box follows the hands. Tower of plates shrinks as she washes; from 4.0 on only the remaining stack in the sink, small at the left edge (5.0 box only 0.15 wide to avoid her box); plate she holds is left out of both boxes where needed; 6.5/7.0 her hand rests over the stack top, split so the stack keeps it. Tower off from 7.5 (sink empty/out of shot). Only 3 nouns: the tap at 2.0 sits at the left edge.")
json.dump(c,open('content/5283.json','w'),indent=1)
