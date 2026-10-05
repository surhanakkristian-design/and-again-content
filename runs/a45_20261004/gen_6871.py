import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) for t,r in zip(T,rows)]
horse=K([(0,.20,.68,.18),(0,.20,.70,.20),(0,.19,.84,.18),(0,.15,.81,.21),(0,.08,.76,.28),(0,.03,.72,.32),(0,.01,.68,.34),(0,.01,.69,.33)])
bishop=K([(.48,.38,.42,.53),(.48,.40,.42,.51),(.47,.37,.43,.54),(.47,.36,.45,.57),(.45,.36,.49,.62),(.44,.35,.52,.65),(.42,.35,.54,.65),(.41,.34,.59,.66)])
woman=K([(.25,.43,.22,.42),(.23,.43,.24,.42),(.21,.43,.24,.43),(.18,.43,.25,.45),(.17,.43,.26,.48),(.14,.43,.22,.48),(.08,.43,.30,.53),(.05,.43,.31,.55)])
c=dict(mediaId=6871,level="B",keyWord="bishop",defaultVoice="male",taps=[
 dict(phrase="to grab the bishop's mitre",target="the horse",voice="male",keys=horse),
 dict(phrase="to give a blessing",target="the bishop",voice="male",keys=bishop),
 dict(phrase="to cover her mouth",target="the young woman",voice="female",keys=woman)],
 stillS=3.2,
 nouns=[dict(word="a mitre",x=.55,y=.15,voice="male"),dict(word="a horse",x=.15,y=.30,voice="male"),
        dict(word="a bishop",x=.68,y=.62,voice="male"),dict(word="a goat",x=.40,y=.72,voice="male")],
 question="What is the horse doing?",
 answer=["It","is","grabbing","the","bishop's","mitre."],answerVoice="male",
 notes="Horse head reaches over the woman and bishop: horse box split horizontally above the people's heads, so the horse's lower body/legs (far left) are outside its box. Woman covers her mouth 0.2-1.7 s, later holds the lead at her chest. Altar boy also gasps, so 'gasp' avoided.")
json.dump(c,open('content/6871.json','w'),indent=1)
