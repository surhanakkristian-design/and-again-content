import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
crow={0.2:(.65,.08,.22,.14),0.7:(.68,.08,.24,.14),1.2:(.65,.08,.22,.14),1.7:(.59,.08,.22,.14),2.2:(.52,.08,.23,.14),2.7:(.51,.08,.22,.14),3.2:(.50,.09,.22,.14),3.7:(.51,.09,.22,.14)}
def k(d): return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
gr={t:(0.0,(.24 if t>=3.2 else .23),.86,(.50-(.24 if t>=3.2 else .23))) for t in T}
gr={t:tuple(round(v,2) for v in b) for t,b in gr.items()}
riv={t:(.63,.64,.37,.20) for t in T}
c=dict(mediaId=7196,level="B",keyWord="griffin",defaultVoice="female",
 taps=[dict(phrase="to perch on a wing",target="the crow",voice="female",keys=k(crow)),
       dict(phrase="to raise a clawed foot",target="the griffin",voice="female",keys=k(gr)),
       dict(phrase="to flow under a stone bridge",target="the river",voice="female",keys=k(riv))],
 stillS=1.2,
 nouns=[dict(word="a crow",x=.76,y=.17,voice="female"),dict(word="a griffin",x=.30,y=.35,voice="female"),
        dict(word="a street lamp",x=.57,y=.45,voice="female"),dict(word="a puddle",x=.75,y=.91,voice="female")],
 question="What is the crow doing?",answer=["It","is","perching","on","the","griffin's","wing."],answerVoice="female",
 notes="Griffin box starts below the crow box (y .23) so the top of the left wing is outside it; crow box is the min size above. River box right of the pillar.")
json.dump(c,open('content/7196.json','w'),indent=1)
