import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(b): return [dict(t=t,x=v[0],y=v[1],w=v[2],h=v[3]) if v else dict(t=t,off=True) for t,v in zip(T,b)]
blue=K([(.31,.19,.29,.58),(.40,.17,.30,.59),(.40,.22,.32,.54),(.31,.24,.31,.53),(.31,.20,.32,.57),(.28,.20,.31,.61),(.29,.21,.27,.58),(.28,.19,.28,.61)])
left=K([(0,.56,.31,.44),(0,.56,.40,.44),(0,.56,.40,.44),(0,.56,.31,.44),(0,.56,.31,.44),(0,.56,.28,.44),(0,.58,.29,.42),(0,.58,.28,.42)])
jug=K([(.60,.78,.40,.22),(.53,.78,.47,.22),(.53,.78,.47,.22),(.53,.78,.47,.22),(.53,.78,.47,.22),(.53,.82,.47,.18),(.56,.60,.44,.40),(.56,.60,.44,.40)])
c=dict(mediaId=5618,level="B",keyWord="be in a good mood",defaultVoice="female",
 taps=[dict(phrase="to swing her friend around",target="the woman in blue",voice="female",keys=blue),
       dict(phrase="to applaud her friends",target="the woman on the left",voice="female",keys=left),
       dict(phrase="to pour iced coffee",target="the woman with the jug",voice="female",keys=jug)],
 stillS=3.2,
 nouns=[dict(word="an olive tree",x=.22,y=.20,voice="female"),dict(word="rooftops",x=.78,y=.24,voice="female"),
        dict(word="a cushion",x=.78,y=.52,voice="female"),dict(word="a jug",x=.62,y=.93,voice="female")],
 question="What is the woman in blue doing?",
 answer=["She","is","lifting","her","friend","off","the","ground."],answerVoice="female",
 notes="Woman in blue lifts and swings her friend 0.2-1.7 s, then hugs her. Boxes of the clapping woman (left) and the pouring woman (right) are cut to avoid the blue woman's box: the left box covers head, hands and torso but not her knees; the jug box covers hands, jug and legs and leaves out her head at 0.2-2.7 s. The woman in cream is no target.")
json.dump(c,open("content/5618.json","w"),indent=1)
