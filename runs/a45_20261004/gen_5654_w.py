import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(l): return [dict(t=t,x=a,y=b,w=round(c-a,2),h=round(d-b,2)) for t,(a,b,c,d) in zip(T,l)]
blue=K([(.13,.20,.48,.97),(.10,.21,.49,1.0),(.10,.23,.53,1.0),(.13,.23,.59,1.0),(.11,.22,.65,1.0),(.07,.21,.68,1.0),(.01,.20,.72,1.0),(.01,.18,.78,1.0)])
white=K([(.50,.17,.87,.80),(.52,.0,.92,.87),(.55,.0,.99,.98),(.62,.0,1.0,1.0),(.68,.0,1.0,1.0),(.74,.0,1.0,1.0),(.78,.0,1.0,1.0),(.80,.0,1.0,1.0)])
c=dict(mediaId=5654,level="B",keyWord="bitter",defaultVoice="female",
 taps=[dict(phrase="to sulk on the podium",target="the woman in blue",voice="female",keys=blue),
       dict(phrase="to raise a gold medal",target="the woman in white",voice="female",keys=white),
       dict(phrase="to fold her arms",target="the woman in blue",voice="female",keys=blue)],
 stillS=0.2,
 nouns=[dict(word="a floodlight",x=0.88,y=0.20,voice="female"),dict(word="a bouquet",x=0.76,y=0.32,voice="female"),
        dict(word="a silver medal",x=0.34,y=0.48,voice="female"),dict(word="a podium",x=0.58,y=0.86,voice="female")],
 question="How does the woman in blue feel?",
 answer="She feels bitter about her silver medal.".split(),
 answerVoice="female",
 notes="Only two people; the woman in white is mostly out of frame at the end (box at the right edge, w 0.20). At 0.2 s she holds the gold medal at her mouth, raises it from 0.7 s. Answer uses the key word 'bitter' (scowl + crossed arms + silver vs gold); stative 'feels' instead of continuous.")
json.dump(c,open('content/5654.json','w'),indent=1)
