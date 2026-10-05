import json
G={0.0:(.40,.55,.60,.45),0.5:(0,.30,1,.70),1.0:(.03,.42,.97,.58),1.5:(.03,.44,.87,.56),2.0:(0,.47,.82,.45),2.5:(.33,.44,.47,.46),
3.0:(.30,.30,.47,.70),3.5:(.36,.27,.49,.73),4.0:(.46,.17,.36,.73),4.5:(.58,.32,.40,.66),5.0:(.48,.30,.47,.70),5.5:(.36,.30,.50,.70),6.0:(.27,.28,.56,.72)}
M={2.5:(.15,.52,.18,.22),3.0:(.12,.64,.18,.28),3.5:(.15,.54,.21,.26),4.0:(.03,.34,.42,.48)}
T=[i*0.5 for i in range(13)]
def keys(d): return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
c=dict(mediaId=594,level="B",keyWord="qualify",defaultVoice="female",
taps=[dict(phrase="to clear the bar",target="the girl",voice="female",keys=keys(G)),
dict(phrase="to wave a green flag",target="the man with the flag",voice="male",keys=keys(M)),
dict(phrase="to pump her fists",target="the girl",voice="female",keys=keys(G))],
stillS=2.5,
nouns=[dict(word="a crossbar",x=.60,y=.14,voice="female"),dict(word="a flag",x=.68,y=.37,voice="female"),
dict(word="a ponytail",x=.40,y=.585,voice="female"),dict(word="a mat",x=.50,y=.90,voice="female")],
question="How does the girl qualify?",
answer=["She","clears","the","bar","and","lands","on","the","mat."],answerVoice="female",
notes="Flag man: set off at 1.5 and 2.0 (small, behind the girl, no flag visible yet; his figure lies inside her box there) and at 4.5+ (the large man in white at 4.0-4.5 is a second official, not the target). At 3.0 he is mostly hidden behind the girl. Rival jumpers applaud only at 5.0-5.5 (1 s), so not used as a target. 'a ponytail' sits on the girl; no other noun labels her. Fist pump is visible only from 5.5.")
json.dump(c,open('content/594.json','w'),indent=1)
