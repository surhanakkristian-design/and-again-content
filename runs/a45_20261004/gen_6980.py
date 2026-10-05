import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
B=[(.22,.10,.53,.73),(.22,.12,.52,.71),(.21,.13,.52,.70),(.22,.16,.51,.67),(.19,.33,.56,.52),(.20,.33,.56,.53),(.19,.34,.55,.52),(.24,.38,.52,.50)]
keys=[dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,B)]
taps=[dict(phrase=p,target="the climber",voice="female",keys=keys) for p in ["to crouch on a boulder","to examine the overhanging rock","to rub her hands together"]]
c=dict(mediaId=6980,level="B",keyWord="consider",defaultVoice="female",taps=taps,stillS=2.7,
 nouns=[dict(word="the sky",x=.15,y=.20,voice="female"),dict(word="an overhanging rock",x=.68,y=.15,voice="female"),
        dict(word="a tank top",x=.38,y=.60,voice="female"),dict(word="climbing shoes",x=.42,y=.81,voice="female")],
 question="What is the climber doing?",answer="She is examining the overhanging rock.".split(),answerVoice="female",
 notes="Only one person in the clip, so all three phrases target the climber. Key word 'consider' is a verb, not placed as a noun.")
json.dump(c,open('content/6980.json','w'),indent=1)
