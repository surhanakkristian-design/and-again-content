import json
T=[i*0.5 for i in range(19)]
man=[(.1,.35,.5,.65),(.05,.4,.57,.6),(0,.37,.6,.63),(0,.35,.56,.65),(0,.35,.6,.65),(0,.32,.69,.68),(0,.3,.66,.7),(0,.31,.87,.69),
(.03,.32,.85,.68),(.05,.32,.83,.68),(0,.3,.84,.7),(.03,.31,.84,.69),(.16,.35,.7,.65),(.27,.39,.5,.61),(.27,.41,.43,.56),(.33,.43,.38,.48),
(.37,.44,.36,.42),(.37,.46,.3,.38),(.37,.47,.26,.35)]
train=[(.6,.37,.32,.19),(.62,.33,.19,.2),(.6,.3,.3,.28),(.56,.3,.44,.32),(.6,.27,.4,.42),(.69,.26,.31,.4),(.66,.3,.34,.45)]+[None]*12
def keys(b): return [dict(t=t,off=True) if v is None else dict(t=t,x=v[0],y=v[1],w=v[2],h=v[3]) for t,v in zip(T,b)]
c={"mediaId":5337,"level":"B","keyWord":"rail","defaultVoice":"male",
"taps":[{"phrase":"to film himself","target":"the young man","voice":"male","keys":keys(man)},
{"phrase":"to gaze up at the roof","target":"the young man","voice":"male","keys":keys(man)},
{"phrase":"to pull into the station","target":"the train","voice":"male","keys":keys(train)}],
"stillS":8.0,
"nouns":[{"word":"a glass roof","x":0.5,"y":0.15,"voice":"male"},{"word":"rails","x":0.14,"y":0.64,"voice":"male"},
{"word":"a backpack","x":0.66,"y":0.61,"voice":"male"},{"word":"a platform","x":0.5,"y":0.88,"voice":"male"}],
"question":"What is the young man looking at?",
"answer":["He","is","gazing","up","at","the","glass","roof."],"answerVoice":"male",
"notes":"Train only in the first shot (0-3 s); where the train sits right behind his head the train box covers only the part beside his head, so the man's box leaves out the croissant hand at 0.0-2.0 s. Rails also run on the right side; the pill sits on the left tracks."}
json.dump(c,open('content/5337.json','w'),indent=1)
