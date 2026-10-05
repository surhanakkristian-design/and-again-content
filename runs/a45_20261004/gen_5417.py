import json
T=[i*0.5 for i in range(19)]
W={0.0:(.77,.31,.23,.69),0.5:(.57,.36,.43,.64),1.0:(.47,.38,.53,.62),1.5:(.34,.21,.66,.79),2.0:(.28,.22,.64,.78),
   2.5:(0,.2,1,.8),3.0:(0,.18,.78,.82),3.5:(0,.28,.7,.72),4.0:(0,.32,.52,.68),4.5:(0,.42,.36,.58),
   7.0:(.8,.56,.2,.44),7.5:(.46,.4,.54,.6),8.0:(.4,.4,.6,.6),8.5:(.33,.42,.52,.58),9.0:(.38,.43,.44,.57)}
TR={0.0:(.2,.2,.57,.5),0.5:(.08,.15,.49,.6),1.0:(0,.05,.46,.9),1.5:(0,0,.33,1),2.0:(0,.05,.27,.9),
    5.0:(.82,.5,.18,.3),5.5:(.8,.08,.2,.92),6.0:(.78,0,.22,1),6.5:(.78,0,.22,1),7.0:(.75,0,.25,.55),7.5:(.8,0,.2,.4),8.0:(.8,0,.2,.4),8.5:(.85,0,.15,1),9.0:(.82,0,.18,1)}
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
c=dict(mediaId=5417,level="B",keyWord="depot",defaultVoice="female",
 taps=[dict(phrase="to board a vintage tram",target="the woman",voice="female",keys=keys(W)),
       dict(phrase="to pick up a passenger",target="the old tram",voice="female",keys=keys(TR)),
       dict(phrase="to look around the depot",target="the woman",voice="female",keys=keys(W))],
 stillS=8.0,
 nouns=[dict(word="overhead wires",x=.3,y=.2,voice="female"),dict(word="rails",x=.17,y=.72,voice="female"),
        dict(word="a tote bag",x=.6,y=.88,voice="female"),dict(word="a plait",x=.88,y=.64,voice="female")],
 question="What is she doing at the end?",
 answer=["She","is","looking","around","the","tram","depot."],answerVoice="female",
 notes="Key word 'depot' is the whole last scene, so it is used in a phrase and the answer, not as a noun pill. Old tram is off during the interior shots (2.5-4.5 s); in the depot shots it is the red/cream carriage side at the right edge. Woman and old tram overlap in the picture at 0.5-2.0 s and 7.0-9.0 s; boxes are split.")
json.dump(c,open('content/5417.json','w'),indent=1,ensure_ascii=False)
