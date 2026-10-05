import json
B={0.0:(.15,.02,.85,.83),0.5:(.15,.02,.85,.83),1.0:(.15,.02,.85,.83),1.5:(.15,.02,.85,.83),2.0:(.15,.02,.85,.83),2.5:(.15,.02,.85,.83),
3.0:(.38,.10,.62,.64),3.5:(.17,.18,.80,.60),4.0:(.28,.15,.67,.60),4.5:(.08,.12,.90,.65),5.0:(.33,.18,.67,.72),5.5:(.33,.15,.67,.75),
6.0:(.27,.16,.73,.70),6.5:(.25,.10,.75,.62),7.0:(.20,.10,.78,.58),7.5:(.15,.08,.83,.66),8.0:(.23,.08,.77,.64),8.5:(.15,.10,.85,.66),
9.0:(.33,.08,.67,.64),9.5:(.23,.08,.77,.67),10.0:(.28,.06,.72,.69),10.5:(.30,.04,.70,.70),11.0:(.30,.08,.70,.67),11.5:(.33,.03,.67,.71),12.0:(.08,.00,.92,.72)}
keys=[dict(t=t,x=v[0],y=v[1],w=v[2],h=v[3]) for t,v in sorted(B.items())]
c=dict(mediaId=5249,level="A",keyWord="to wash",defaultVoice="male",
taps=[dict(phrase=p,target="the man",voice="male",keys=keys) for p in ["to wash a dirty pan","to lift a heavy pan","to wear green gloves"]],
stillS=3.0,nouns=[dict(word="a window",x=.27,y=.33,voice="male"),dict(word="a man",x=.75,y=.40,voice="male"),
dict(word="a tap",x=.20,y=.58,voice="male"),dict(word="a pan",x=.55,y=.74,voice="male")],
question="What is the man doing?",answer=["He","is","washing","a","dirty","pan."],answerVoice="male",
notes="Only one person in the clip, so all three phrases target the man (one shared box). 'to lift a heavy pan' fits 3.5-6.0 (he lifts the sooty pot and scours its underside); 'to wash a dirty pan' covers the whole clip (frying pan, pot, grill pan). Still 3.0: window behind his head, tap with running water, frying pan in the sink.")
json.dump(c,open('content/5249.json','w'),indent=1)
