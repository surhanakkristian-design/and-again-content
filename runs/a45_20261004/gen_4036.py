import json
T=[i*0.5 for i in range(31)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else:
            x1,y1,x2,y2=v
            out.append({"t":t,"x":x1,"y":y1,"w":round(x2-x1,2),"h":round(y2-y1,2)})
    return out
W={0.0:(0,.15,.47,1.0),0.5:(0,.17,.48,1.0),1.0:(0,.17,.48,1.0),1.5:(0,.16,.49,1.0),
4.0:(0,.11,1.0,1.0),4.5:(0,.10,1.0,1.0),5.0:(0,.11,1.0,1.0),5.5:(0,.11,1.0,1.0),
6.0:(.52,.22,1.0,1.0),6.5:(.53,.22,1.0,1.0),7.0:(.50,.23,1.0,1.0),7.5:(.50,.23,1.0,1.0),8.0:(.49,.23,1.0,1.0),8.5:(.50,.23,1.0,1.0),
9.0:(.50,.21,1.0,1.0),9.5:(.50,.21,1.0,1.0),10.0:(.53,.19,1.0,1.0),10.5:(.50,.18,1.0,1.0),11.0:(.52,.18,1.0,1.0),
11.5:(.49,.16,1.0,1.0),12.0:(.49,.15,1.0,.90),12.5:(.55,.15,.92,.80),13.0:(.52,.19,.96,.73),13.5:(.48,.22,.80,.74),
14.0:(.44,.26,.76,.76),14.5:(.41,.29,.71,.79),15.0:(.39,.32,.71,.82)}
M={0.0:(.47,.39,.97,.93),0.5:(.48,.37,.97,.92),1.0:(.48,.34,.97,.90),1.5:(.49,.33,.99,.88),
6.0:(0,.19,.52,1.0),6.5:(0,.19,.53,1.0),7.0:(0,.19,.50,1.0),7.5:(0,.19,.50,1.0),8.0:(0,.19,.49,1.0),8.5:(0,.19,.50,1.0),
9.0:(0,.20,.50,1.0),9.5:(0,.20,.50,1.0),10.0:(0,.17,.52,1.0),10.5:(0,.15,.49,1.0),11.0:(0,.13,.51,1.0),
11.5:(0,.11,.49,.98),12.0:(0,.10,.49,.94),12.5:(0,.11,.54,.94),13.0:(0,.14,.51,.98),13.5:(0,.17,.46,1.0),
14.0:(0,.20,.43,1.0),14.5:(0,.22,.41,1.0),15.0:(0,.23,.39,1.0)}
for t in (2.0,2.5,3.0,3.5):
    M[t]=(.14,.46,.37,.61); W[t]=(.39,.41,.59,.59)
kw=K(W)
d={"mediaId":4036,"level":"A","keyWord":"smile","defaultVoice":"female",
"taps":[{"phrase":"to touch her hair","target":"the woman","voice":"female","keys":kw},
{"phrase":"to take a photo","target":"the man","voice":"male","keys":K(M)},
{"phrase":"to give a thumbs up","target":"the woman","voice":"female","keys":kw}],
"stillS":4.5,
"nouns":[{"word":"a smile","x":.43,"y":.53,"voice":"female"},{"word":"hair","x":.70,"y":.20,"voice":"female"},
{"word":"a dress","x":.62,"y":.88,"voice":"female"},{"word":"a hand","x":.13,"y":.44,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","smiling","at","the","camera."],"answerVoice":"female",
"notes":"Only two targets (woman, man); two phrases share the woman. In the first shot (0-1.5 s) her raised arm reaches over the man: boxes are split along a vertical line, so her elbow lies in the man's box. 2.0-3.5 s is a wide shot with both people tiny (minimum-size boxes, close together). 4.0-5.5 s is a close-up of the woman only (man off). Key word 'smile' is a noun; the answer uses the verb 'smiling'. 'to give a thumbs up' is the least beginner-like phrase."}
json.dump(d,open("content/4036.json","w"),indent=1)
