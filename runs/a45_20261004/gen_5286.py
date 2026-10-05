import json
D={0.0:(0,.12,.48,.86),0.5:(0,.18,.48,.80),1.0:(0,.26,.64,.74),1.5:(0,.14,.48,.86),2.0:(0,.17,.44,.83),2.5:(0,.22,.38,.78),3.0:(0,.22,.62,.78),3.5:(0,.22,.50,.78),
4.0:(0,.25,.60,.75),4.5:(0,.15,.64,.85),5.0:(0,.12,.62,.88),5.5:(0,.28,.58,.72),6.0:(0,.08,.55,.85),6.5:(0,.16,.57,.76),7.0:(0,.17,.60,.75),7.5:(0,.18,.58,.74),
8.0:(0,.22,.52,.70),8.5:(0,.24,.50,.66),9.0:(0,.22,.50,.70),9.5:(0,.19,.52,.73),10.0:(0,.24,.54,.76)}
R={0.0:(.52,.22,.48,.76),0.5:(.52,.17,.48,.81),1.0:(.66,.36,.34,.64),1.5:(.52,.18,.48,.82),2.0:(.47,.17,.53,.83),2.5:(.52,.21,.48,.79),3.0:(.63,.19,.37,.81),3.5:(.51,.17,.49,.83),
4.0:(.61,.24,.39,.76),4.5:(.65,.24,.35,.76),5.0:(.63,.23,.37,.77),5.5:(.59,.06,.41,.94),6.0:(.56,.00,.44,.92),6.5:(.58,.05,.42,.88),7.0:(.62,.06,.38,.86),7.5:(.60,.08,.40,.84),
8.0:(.53,.12,.47,.80),8.5:(.52,.19,.48,.70),9.0:(.52,.19,.48,.72),9.5:(.53,.17,.47,.75),10.0:(.55,.20,.45,.70)}
def keys(d): return [dict(t=t,x=v[0],y=v[1],w=v[2],h=v[3]) for t,v in sorted(d.items())]
c=dict(mediaId=5286,level="A",keyWord="sweatshirt",defaultVoice="female",taps=[
 dict(phrase="to do her friend's hair",target="the red-haired girl",voice="female",keys=keys(R)),
 dict(phrase="to hold the phone",target="the dark-haired girl",voice="female",keys=keys(D)),
 dict(phrase="to give a thumbs-up",target="the dark-haired girl",voice="female",keys=keys(D))],
 stillS=2.0,nouns=[dict(word="a sweatshirt",x=.72,y=.66,voice="female"),dict(word="a phone",x=.35,y=.54,voice="female"),
 dict(word="lights",x=.50,y=.15,voice="female")],
 question="What is the red-haired girl doing?",answer=["She","is","doing","her","friend's","hair."],answerVoice="female",
 notes="Two girls, both pull the sweatshirt and pull faces, so phrases use only exclusive actions: red-haired girl plaits (5.5-10.0), dark-haired girl holds the selfie phone (2.0-5.0, 10.0) and gives the thumbs-up (9.0-9.5). Bodies overlap in the selfie and hug shots: split along the line between them; the sweatshirt held between them falls partly into both boxes. 'the phone' at the still is small (in the dark-haired girl's hand). Only 3 nouns.")
json.dump(c,open('content/5286.json','w'),indent=1)
