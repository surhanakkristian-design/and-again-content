import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2]
def K(l): return [dict(t=t,off=True) if v is None else dict(t=t,x=v[0],y=v[1],w=round(v[2]-v[0],2),h=round(v[3]-v[1],2)) for t,v in zip(T,l)]
horse=K([(.0,.03,.68,.99),(.0,.02,.53,.40),(.0,.07,.47,.98),(.02,.16,.47,.96),(.08,.19,.50,.86),(.14,.21,.48,.85),(.18,.22,.50,.89)])
woman=K([None,(.02,.40,.74,.99),(.47,.30,.81,.99),(.47,.32,.86,.98),(.50,.34,.89,.90),(.48,.35,.90,.86),(.50,.37,.89,.85)])
c=dict(mediaId=5655,level="B",keyWord="bizarre",defaultVoice="female",
 taps=[dict(phrase="to carry a striped sock",target="the horse",voice="female",keys=horse),
       dict(phrase="to burst out laughing",target="the woman",voice="female",keys=woman),
       dict(phrase="to pull out a towel",target="the woman",voice="female",keys=woman)],
 stillS=2.2,
 nouns=[dict(word="a sock",x=0.44,y=0.44,voice="female"),dict(word="a horse",x=0.27,y=0.58,voice="female"),
        dict(word="a washing machine",x=0.88,y=0.67,voice="female"),dict(word="trainers",x=0.63,y=0.84,voice="female")],
 question="What is the horse carrying?",
 answer="The horse is carrying a striped sock.".split(),
 answerVoice="female",
 notes="Woman stands in front of the horse: at 0.2 s only her arm is visible (off); at 0.7 s boxes split horizontally (horse head above y 0.40, woman below, her head partly in no box); later split at x ~0.47-0.50, so her shorts' left edge falls in the horse box. Horse 'carries' the sock in its mouth.")
json.dump(c,open('content/5655.json','w'),indent=1)
