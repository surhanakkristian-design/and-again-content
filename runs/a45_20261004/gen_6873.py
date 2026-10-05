import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) for t,r in zip(T,rows)]
woman=K([(.35,.44,.47,.56),(.34,.46,.49,.54),(.31,.49,.47,.51),(.28,.52,.50,.48),(.23,.54,.55,.46),(.18,.53,.62,.47),(.12,.50,.80,.50),(.11,.49,.81,.51)])
horn=K([(.47,.09,.47,.24),(.48,.09,.48,.26),(.47,.11,.48,.26),(.46,.11,.52,.28),(.43,.11,.57,.29),(.42,.08,.58,.30),(.43,.04,.57,.32),(.41,.01,.59,.35)])
c=dict(mediaId=6873,level="B",keyWord="blast",defaultVoice="female",taps=[
 dict(phrase="to tug on a rope",target="the woman",voice="female",keys=woman),
 dict(phrase="to blast out steam",target="the brass horn",voice="female",keys=horn),
 dict(phrase="to yell at the horn",target="the woman",voice="female",keys=woman)],
 stillS=1.2,
 nouns=[dict(word="a brass horn",x=.76,y=.22,voice="female"),dict(word="steam",x=.35,y=.23,voice="female"),
        dict(word="a knitted hat",x=.42,y=.55,voice="female"),dict(word="a coiled rope",x=.82,y=.78,voice="female")],
 question="What is the brass horn doing?",
 answer=["It","is","blasting","out","steam."],answerVoice="female",
 notes="Crew members behind cover their ears, but they stand right behind/against the woman, so no crew target (boxes would overlap); two targets only. Steam comes out 0.2-1.7 s; she yells up at the horn 2.7-3.7 s.")
json.dump(c,open('content/6873.json','w'),indent=1)
