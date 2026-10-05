import json
T=[i/2 for i in range(21)]
M={0.0:(0,0,.42,.82),0.5:(0,0,.40,.83),1.0:(0,.20,.40,.67),1.5:(0,.20,.33,.75),2.0:(.06,.26,.40,.74),2.5:(.05,.35,.65,.65),
3.0:(0,.38,.62,.62),5.5:(0,.36,.20,.64),6.0:(0,.08,.45,.92),6.5:(0,.20,.49,.75),7.0:(0,.27,.42,.73),7.5:(0,.31,.44,.69),
8.0:(0,.32,.82,.68),8.5:(0,.32,.55,.68),9.0:(0,.32,.36,.68),9.5:(0,.34,.53,.66),10.0:(.03,.27,.50,.73)}
B={0.0:(.54,.54,.18,.14),0.5:(.50,.55,.18,.14),1.0:(.51,.56,.18,.14),6.0:(.66,.57,.18,.14)}
def keys(D):
    return [dict(t=t,x=D[t][0],y=D[t][1],w=D[t][2],h=D[t][3]) if t in D else dict(t=t,off=True) for t in T]
mk=keys(M); bk=keys(B)
c=dict(mediaId=4831,level="B",keyWord="hit",defaultVoice="male",
 taps=[dict(phrase="to swing an aluminium bat",target="the young man",voice="male",keys=mk),
       dict(phrase="to break into a grin",target="the young man",voice="male",keys=mk),
       dict(phrase="to balance on a batting tee",target="the coloured ball",voice="male",keys=bk)],
 stillS=0.0,
 nouns=[dict(word="a cap",x=.30,y=.17,voice="male"),dict(word="a fence",x=.75,y=.31,voice="male"),
        dict(word="a ball",x=.62,y=.60,voice="male"),dict(word="a batting tee",x=.62,y=.74,voice="male")],
 question="What is the young man doing?",
 answer=["He","is","sending","the","ball","high","over","the","lawn."],answerVoice="male",
 notes="Ball target = the rainbow ball on the tee (0.0-1.0 s); at 6.0 s a rainbow ball is seen again in the air near the tee (kept as a key, likely a replay shot); elsewhere it is only a tiny dot in the sky, so off. The man is off at 3.5-5.0 s (camera follows the ball). 'to break into a grin' = his broad smile at 9.5-10 s. Key word 'hit' (noun) is not a placeable thing.")
json.dump(c,open('content/4831.json','w'),indent=1)
