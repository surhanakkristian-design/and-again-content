import json
W={0.5:(.18,.24,.44,.70),1.0:(.07,.19,.78,.81),1.5:(0,.08,.88,.92),2.0:(0,.11,.72,.89),2.5:(0,.06,.80,.94),3.0:(.22,.12,.58,.88),
3.5:(.12,.11,.80,.89),4.0:(.35,.19,.65,.81),4.5:(.38,.18,.50,.82),5.0:(.24,.13,.46,.87),5.5:(.25,.13,.47,.87),6.0:(0,.04,.92,.96),
6.5:(.08,.13,.72,.87),7.0:(.24,.19,.50,.81),7.5:(.31,.20,.29,.52),8.0:(.30,.23,.28,.33),8.5:(.31,.22,.26,.30),9.0:(.35,.24,.25,.27)}
C={7.5:(0,.60,.30,.19),8.0:(.14,.57,.28,.14),8.5:(.19,.53,.27,.14),9.0:(.20,.52,.27,.14)}
T=[i/2 for i in range(19)]
def keys(d): return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
c=dict(mediaId=4345,level="A",keyWord="joy",defaultVoice="female",taps=[
 dict(phrase="to carry the presents",target="the woman in the jacket",voice="female",keys=keys(W)),
 dict(phrase="to hold a phone",target="the woman in the jacket",voice="female",keys=keys(W)),
 dict(phrase="to have candles on top",target="the cake",voice="female",keys=keys(C))],
 stillS=8.0,nouns=[dict(word="balloons",x=.55,y=.07,voice="female"),dict(word="a boy",x=.20,y=.42,voice="male"),
 dict(word="a cake",x=.28,y=.62,voice="female"),dict(word="a table",x=.17,y=.74,voice="female")],
 question="What is the woman carrying?",answer=["She","is","carrying","a","lot","of","presents."],answerVoice="female",
 notes="Key word 'joy' is abstract, so it is not a noun slot. Two phrases share the woman; the children both hug her and both shout, so no phrase fits only one child. Other women appear in the last shot, hence 'the woman in the jacket'. The phone is in her hand from 2.0 s and clearly held up at 6.5-8.0 s.")
json.dump(c,open('content/4345.json','w'),indent=1,ensure_ascii=False)
