import json
times=[i*0.5 for i in range(25)]
M={0.0:(.10,.08,.90,.92),0.5:(.12,.12,.88,.88),1.0:(.12,.15,.88,.85),1.5:(.12,.16,.88,.84),2.0:(.13,.11,.87,.89),
2.5:(0,0,.82,.36),3.0:(0,0,.62,.23),3.5:(0,0,.78,.49),4.0:(.05,.02,.90,.98),4.5:(.08,.16,.90,.84),5.0:(.06,.16,.94,.84),
5.5:(.06,.17,.94,.83),6.0:(.06,.17,.94,.83),6.5:(.08,.15,.92,.85),7.0:(.08,.16,.92,.84),7.5:(.08,.15,.92,.85),
8.0:(.09,.14,.91,.86),8.5:(.11,.14,.89,.86),9.0:(.13,.11,.87,.89),9.5:(.13,.04,.87,.96),10.0:(.13,0,.87,.90),
10.5:(.08,0,.92,.76),11.0:(.08,0,.92,.68),11.5:(.06,0,.94,.60),12.0:(.06,0,.94,.60)}
G={2.5:(.38,.37,.48,.48),3.0:(.14,.24,.50,.48),3.5:(.36,.50,.48,.50)}
def ks(d): return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in times]
c=dict(mediaId=5075,level="B",keyWord="sticky",defaultVoice="male",
 taps=[dict(phrase="to lick a dripping cone",target="the man",voice="male",keys=ks(M)),
       dict(phrase="to get sticky hands",target="the man",voice="male",keys=ks(M)),
       dict(phrase="to be full of ice",target="the glass of water",voice="male",keys=ks(G))],
 stillS=5.0,
 nouns=[dict(word="an ice cream",x=.56,y=.45,voice="male"),dict(word="sunglasses",x=.50,y=.19,voice="male"),
        dict(word="an umbrella",x=.82,y=.36,voice="male"),dict(word="cobblestones",x=.13,y=.88,voice="male")],
 question="What are the man's hands like?",answer=["His","hands","are","sticky."],answerVoice="male",
 notes="Ice cream not used as a tap target because it sits in front of the man in every frame (boxes would overlap). The glass of iced water appears only in the cut-in shots 2.5-3.5 s; man box there is cut above the glass. Glass rim at the bottom edge at 10.5-12.0 s left off (only a sliver). Phrase 3 is a state (no action fits the glass).")
json.dump(c,open('content/5075.json','w'),indent=1)
