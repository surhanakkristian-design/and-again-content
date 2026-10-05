import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def k(d): return [dict(t=t,x=round(d[t][0],2),y=round(d[t][1],2),w=round(d[t][2]-d[t][0],2),h=round(d[t][3]-d[t][1],2)) for t in T]
# split line between man (feet) and calf
sp={0.2:.71,0.7:.71,1.2:.69,1.7:.68,2.2:.67,2.7:.66,3.2:.64,3.7:.63}
man={0.2:(.05,.33,.55),0.7:(.08,.30,.63),1.2:(.05,.27,.61),1.7:(.05,.24,.63),2.2:(.04,.18,.69),2.7:(.04,.14,.70),3.2:(.01,.08,.71),3.7:(.01,.04,.74)}
man={t:(v[0],v[1],v[2],sp[t]) for t,v in man.items()}
calfx={0.2:.55,0.7:.58,1.2:.59,1.7:.61,2.2:.65,2.7:.66,3.2:.68,3.7:.71}
calf={t:(0.0,sp[t],calfx[t],.91) for t in T}
lan={0.2:(.80,.40,.98,.60),0.7:(.81,.39,.99,.60),1.2:(.82,.38,1.0,.63),1.7:(.82,.36,1.0,.59),2.2:(.80,.33,1.0,.55),2.7:(.82,.31,1.0,.47),3.2:(.82,.29,1.0,.43),3.7:(.82,.26,1.0,.40)}
c=dict(mediaId=7199,level="B",keyWord="guardian",defaultVoice="male",
 taps=[dict(phrase="to lift a large tarpaulin",target="the young man",voice="male",keys=k(man)),
       dict(phrase="to lie under a checked blanket",target="the elephant calf",voice="male",keys=k(calf)),
       dict(phrase="to hold a glowing lantern",target="the man with the lantern",voice="male",keys=k(lan))],
 stillS=1.2,
 nouns=[dict(word="an acacia tree",x=.60,y=.22,voice="male"),dict(word="a lantern",x=.86,y=.44,voice="male"),
        dict(word="a tarpaulin",x=.64,y=.58,voice="male"),dict(word="an elephant calf",x=.30,y=.80,voice="male")],
 question="What is the young man doing?",answer=["He","is","lifting","a","large","tarpaulin."],answerVoice="male",
 notes="Key word guardian is abstract, not a noun slot. The man with the lantern is small in the background and only partly in frame from 2.7 s (arm + lantern at the right edge); his box stays at the right edge.")
json.dump(c,open('content/7199.json','w'),indent=1)
