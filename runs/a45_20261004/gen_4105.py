import json
times=[i*0.5 for i in range(27)]
def box(b): return dict(x=round(b[0],2),y=round(b[1],2),w=round(b[2]-b[0],2),h=round(b[3]-b[1],2))
wom={0.0:(0,.05,.95,1),0.5:(.04,.05,.97,1),1.0:(0,.05,.98,1),1.5:(0,.04,.90,1),2.0:(0,.02,.86,1),2.5:(0,.02,1,1),3.0:(0,.02,.90,1),3.5:(0,.02,.93,1),
9.0:(0,.14,.45,.62),9.5:(0,.18,.54,.62),10.0:(0,.22,.56,.60),10.5:(0,.22,.56,.60),11.0:(0,.17,.56,.62),11.5:(0,.15,.52,.62),12.0:(0,.14,.52,.60),12.5:(0,.14,.52,.60),13.0:(0,.14,.52,.60)}
for t in (6.5,7.0,7.5,8.0,8.5): wom[t]=(0,0,1,1)
man={4.5:(.29,.27,.98,.95),5.0:(.27,.28,.98,.96),5.5:(.29,.27,1,.96),6.0:(.35,.24,1,.97),
9.0:(.58,.05,1,.62),9.5:(.54,.05,1,.62),10.0:(.56,.04,1,.60),10.5:(.56,.04,1,.60),11.0:(.56,.05,1,.62),11.5:(.52,.05,1,.62),12.0:(.52,.04,1,.60),12.5:(.52,.04,1,.60),13.0:(.52,.04,1,.60)}
def keys(d): return [dict(t=t,**box(d[t])) if t in d else dict(t=t,off=True) for t in times]
c=dict(mediaId=4105,level="A",keyWord="boyfriend",defaultVoice="female",
 taps=[dict(phrase="to touch her hair",target="the woman",voice="female",keys=keys(wom)),
       dict(phrase="to wait by the car",target="the man",voice="male",keys=keys(man)),
       dict(phrase="to cover her mouth",target="the woman",voice="female",keys=keys(wom))],
 stillS=5.0,
 nouns=[dict(word="a car",x=.16,y=.62,voice="female"),dict(word="flowers",x=.78,y=.47,voice="female"),
        dict(word="a man",x=.52,y=.36,voice="male")],
 question="Who is waiting by the car?",
 answer=["Her","boyfriend","is","waiting","by","the","car."],answerVoice="male",
 notes="4.0 s is a blurred pan over the car: both targets off. The man's box in the street shot includes the flowers he holds. In the last shot the two heads are close: boxes split on a vertical line, bodies are hidden behind the flowers. 'boyfriend' cannot be placed as a noun without guessing (the still shows him alone), so it is in the answer; answerVoice male because the subject is the boyfriend. Only 3 nouns: the rest of the still is blurred building.")
json.dump(c,open("content/4105.json","w"),indent=1,ensure_ascii=False)
