import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=x,y=y,w=w,h=h) for t,(x,y,w,h) in zip(T,rows)]
wo=K([(.14,.15,.42,.66),(.12,.08,.44,.77),(.13,.09,.42,.79),(.13,.09,.45,.80),(.13,.21,.45,.67),(.10,.22,.43,.65),(.14,.20,.38,.67),(.08,.18,.44,.69)])
dog=K([(.70,.39,.21,.19),(.70,.44,.21,.17),(.71,.48,.21,.16),(.69,.48,.23,.16),(.69,.48,.22,.16),(.70,.46,.21,.18),(.70,.46,.20,.17),(.71,.45,.20,.18)])
man=K([(.81,.25,.19,.14),(.80,.29,.20,.14),(.80,.33,.20,.14),(.80,.33,.20,.14),(.80,.32,.20,.15),(.80,.31,.20,.14),(.80,.31,.20,.14),(.80,.30,.20,.14)])
c=dict(mediaId=6892,level="B",keyWord="brass",defaultVoice="female",
taps=[dict(phrase="to empty a heavy wheelbarrow",target="the young woman",voice="female",keys=wo),
      dict(phrase="to sit on the heap",target="the dog",voice="female",keys=dog),
      dict(phrase="to cover his ears",target="the man on the right",voice="male",keys=man)],
stillS=3.7,
nouns=[dict(word="an apron",x=.25,y=.52,voice="female"),dict(word="a terrier",x=.80,y=.52,voice="female"),
       dict(word="brass",x=.86,y=.63,voice="female"),dict(word="a wheelbarrow",x=.45,y=.74,voice="female")],
question="What is the woman doing?",answer=["She","is","emptying","a","heavy","wheelbarrow."],answerVoice="female",
notes="Man on the right covers his ears only 0.2-1.7 s, hands down after. Dog box and man box are split horizontally where the dog's head nears the seated man. Woman box leaves out the raised wheelbarrow.")
json.dump(c,open('content/6892.json','w'),indent=1)
