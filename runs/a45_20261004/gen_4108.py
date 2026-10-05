import json
times=[i*0.5 for i in range(26)]
def mk(d):
    out=[]
    for t in times:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
B={0.0:(0,.29,.45,.47),0.5:(0,.29,.45,.47),1.0:(0,.36,.43,.42),1.5:(0,.34,.57,.44),2.0:(0,.37,.52,.40),2.5:(0,.34,.53,.43),3.0:(0,.32,.50,.46),
3.5:(0,.24,.20,.38),4.0:(0,.20,.25,.40),4.5:(0,.17,.27,.43),5.0:(0,.18,.30,.42),5.5:(0,.17,.30,.43),
6.0:(0,.10,.92,.90),6.5:(0,.08,1,.92),7.0:(0,.10,1,.90),7.5:(0,.10,1,.90),
8.5:(.19,.36,.18,.14),9.0:(.19,.36,.18,.14),9.5:(.19,.36,.19,.14),
11.5:(.29,.29,.45,.20),12.0:(.29,.29,.45,.20),12.5:(.29,.29,.45,.20)}
W={0.0:(.45,.38,.55,.44),0.5:(.45,.38,.55,.44),1.0:(.43,.38,.57,.46),1.5:(.57,.36,.43,.48),2.0:(.52,.38,.48,.45),2.5:(.53,.38,.47,.45),3.0:(.50,.38,.50,.46),
3.5:(.20,.08,.80,.82),4.0:(.25,.10,.75,.80),4.5:(.27,.10,.73,.80),5.0:(.30,.07,.70,.83),5.5:(.30,.08,.70,.82),
8.5:(.37,.36,.18,.14),9.0:(.37,.36,.18,.14),9.5:(.39,.37,.18,.14),
10.0:(.38,.40,.62,.45),10.5:(.59,.44,.41,.42),11.0:(.59,.46,.41,.42),11.5:(.59,.50,.41,.38),12.0:(.59,.49,.41,.38),12.5:(.59,.49,.41,.38)}
c={"mediaId":4108,"level":"A","keyWord":"husband","defaultVoice":"female",
"taps":[{"phrase":"to wave from the car","target":"the blue bird","voice":"female","keys":mk(B)},
{"phrase":"to hold the wheel","target":"the white bird","voice":"female","keys":mk(W)},
{"phrase":"to stand next to the car","target":"the white bird","voice":"female","keys":mk(W)}],
"stillS":12.0,
"nouns":[{"word":"a car","x":.24,"y":.57,"voice":"female"},{"word":"a wheel","x":.13,"y":.76,"voice":"female"},{"word":"a house","x":.62,"y":.14,"voice":"female"}],
"question":"What is the white bird doing?",
"answer":["It","is","standing","next","to","the","car."],"answerVoice":"female",
"notes":"Only two targets (the two birds); the car would overlap both. Key word 'husband' is only written on the car door ('I'm her husband.'), no person/noun slot can carry it without guessing, so it is not among the nouns or in the answer. The blue bird waves only at 11.5-12.5 s; the white bird holds the steering wheel at 3.5-5.5 s and stands beside the car from 10.5 s. Voices follow the rule (birds -> defaultVoice female, evenId true) although the blue bird is the husband. In the two-shot (0-5.5 s) the birds touch, boxes split along a vertical line; the white bird's left glove at 3.5 s is outside its box. 8.0 s is motion blur (both off). 'a house' = the brick building behind."}
json.dump(c,open("content/4108.json","w"),indent=1)
