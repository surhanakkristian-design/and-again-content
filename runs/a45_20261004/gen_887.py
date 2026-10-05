import json
T=[i*0.5 for i in range(17)]
def keys(d):
    return [dict(t=t, x=d[t][0], y=d[t][1], w=d[t][2], h=d[t][3]) if t in d else dict(t=t, off=True) for t in T]
H={0.0:(.71,.43,.29,.50),0.5:(.55,.45,.45,.50),1.0:(.54,.45,.46,.50),1.5:(.22,0,.78,.28),2.0:(.20,.03,.80,.26),2.5:(.26,.02,.74,.23),
3.0:(.15,0,.85,.14),3.5:(.18,0,.82,.11),4.0:(.08,0,.92,.10),4.5:(.10,0,.90,.11),5.0:(.33,0,.67,.07),6.5:(.78,.52,.22,.46),7.0:(.68,.49,.32,.50)}
P={0.0:(.71,.28,.29,.14),0.5:(.55,.30,.20,.14),1.0:(.54,.30,.20,.14),1.5:(.38,.29,.24,.20),2.0:(.42,.30,.26,.20),2.5:(.44,.26,.28,.20),
3.0:(.40,.15,.36,.30),3.5:(.50,.12,.40,.32),4.0:(.40,.11,.40,.31),4.5:(.43,.12,.42,.30),5.0:(.54,.08,.40,.34),6.5:(.78,.36,.22,.15),
7.0:(.68,.34,.20,.14),7.5:(.70,.36,.30,.42),8.0:(.70,.36,.30,.41)}
B={0.0:(0,.18,.70,.74),0.5:(0,.16,.54,.76),1.0:(0,.16,.53,.78),1.5:(0,.50,1,.50),2.0:(0,.51,1,.49),2.5:(0,.47,1,.53),3.0:(0,.46,1,.54),
3.5:(0,.45,1,.55),4.0:(0,.43,1,.57),4.5:(0,.43,1,.57),5.0:(0,.43,1,.57),5.5:(0,.08,1,.92),6.0:(0,.05,1,.95),6.5:(0,.20,.77,.78),
7.0:(0,.23,.67,.72),7.5:(0,.24,.69,.70),8.0:(0,.21,.69,.69)}
c=dict(mediaId=887,level="A",keyWord="write",defaultVoice="female",taps=[
 dict(phrase="to write with a pen",target="the hand",voice="female",keys=keys(H)),
 dict(phrase="to lie on the book",target="the pen",voice="female",keys=keys(P)),
 dict(phrase="to have white pages",target="the book",voice="female",keys=keys(B))],
 stillS=1.0,
 nouns=[dict(word="a table",x=.50,y=.08,voice="female"),dict(word="a pen",x=.63,y=.40,voice="female"),
        dict(word="a hand",x=.76,y=.57,voice="female"),dict(word="a book",x=.28,y=.72,voice="female")],
 question="What is the hand doing?",
 answer=["It","is","writing","in","a","book."],answerVoice="female",
 notes="No whole person is shown, only a woman's hand, a pen and a book: three things as targets. They lie on top of each other, so the boxes are split: the book box is the page area left of / below the pen and hand; the pen box is the free part of the pen (its tip end), the hand box the fingers and sleeve. In the close-ups (1.5-5.0 s) the hand is only a strip at the top (h below the minimum at 3.5-5.0 s). The pen lies on the book at 0.0-1.0 s and 6.5-8.0 s (at 7.5-8.0 s its lower end hangs over the book edge onto the table); the book phrase is a state because 'to lie on the table' would also fit the pen there. Question avoids 'the woman' because only the hand is visible.")
json.dump(c,open('content/887.json','w'),indent=1,ensure_ascii=False)
