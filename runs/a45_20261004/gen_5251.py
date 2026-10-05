import json
B={0.0:(.18,.17,.80,.47),0.5:(.18,.18,.62,.45),1.0:(.20,.20,.55,.45),1.5:(.20,.20,.56,.45),2.0:(.20,.19,.54,.45),2.5:(.20,.19,.56,.45),
3.0:(.14,.11,.62,.55),3.5:(.15,.11,.65,.55),4.0:(.10,.11,.70,.52),4.5:(.12,.10,.68,.53),5.0:(.04,.11,.76,.50),5.5:(.11,.11,.72,.50),
6.0:(.04,.10,.76,.50),6.5:(.07,.10,.73,.50),7.0:(.08,.21,.76,.50),7.5:(.04,.21,.94,.50),8.0:(.00,.21,.85,.53),8.5:(.00,.21,.77,.53),9.0:(.02,.21,.65,.53)}
keys=[dict(t=t,x=v[0],y=v[1],w=v[2],h=v[3]) for t,v in sorted(B.items())]
T="the woman with white hair"
c=dict(mediaId=5251,level="A",keyWord="type",defaultVoice="female",
taps=[dict(phrase=p,target=T,voice="female",keys=keys) for p in ["to talk on the phone","to write in a notebook","to use a stamp"]],
stillS=4.5,nouns=[dict(word="a window",x=.17,y=.14,voice="female"),dict(word="folders",x=.14,y=.38,voice="female"),
dict(word="a keyboard",x=.12,y=.60,voice="female"),dict(word="a notebook",x=.60,y=.63,voice="female")],
question="What is the woman doing?",answer=["She","is","talking","on","the","phone."],answerVoice="female",
notes="Only the receptionist is a stable target; background office workers change between shots and some sit at computers, so 'to type on a keyboard' was avoided (a background woman at a desk may also type). All three phrases target her (shared box). 'to use a stamp' = 5.0-6.5. Phone talk 1.0-6.5. Still 4.5: windows top left, row of folders on a shelf, keyboard at left edge of the counter, open ring notebook.")
json.dump(c,open('content/5251.json','w'),indent=1)
