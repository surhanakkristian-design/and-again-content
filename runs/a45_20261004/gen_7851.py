import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,boxes)]
wom=K([(0.66,0.31,0.34,0.34),(0.72,0.30,0.28,0.35),(0.82,0.27,0.18,0.36),None,None,None,None,None])
light=K([(0.27,0.17,0.20,0.15),(0.27,0.17,0.20,0.15),(0.26,0.16,0.20,0.15),(0.27,0.15,0.20,0.15),(0.25,0.11,0.20,0.15),(0.18,0.02,0.23,0.18),None,None])
hands=K([(0.15,0.66,0.70,0.34),(0.18,0.67,0.70,0.33),(0.15,0.67,0.70,0.33),(0.17,0.67,0.70,0.33),(0.17,0.67,0.70,0.33),(0.17,0.67,0.70,0.33),(0.17,0.67,0.70,0.33),(0.19,0.67,0.70,0.33)])
d={"mediaId":7851,"level":"B","keyWord":"green light","defaultVoice":"male",
"taps":[{"phrase":"to wave the karts on","target":"the woman in orange","voice":"female","keys":wom},
{"phrase":"to glow bright green","target":"the green light","voice":"male","keys":light},
{"phrase":"to grip the steering wheel","target":"the gloved hands","voice":"male","keys":hands}],
"stillS":0.7,
"nouns":[{"word":"a green light","x":0.37,"y":0.24,"voice":"male"},{"word":"a marshal","x":0.84,"y":0.42,"voice":"male"},
{"word":"a kerb","x":0.82,"y":0.67,"voice":"male"},{"word":"a steering wheel","x":0.50,"y":0.82,"voice":"male"}],
"question":"What is the driver gripping?",
"answer":["The","driver","is","gripping","the","steering","wheel."],
"answerVoice":"male",
"notes":"POV clip; the driver is the viewer (only gloved hands visible, gender unknown -> default voice). Red and yellow karts both race away, so neither is used as a target. Marshal leaves the frame after 1.2 s; the start light leaves after 2.7 s. 'a marshal' is the woman in the hi-vis vest."}
json.dump(d,open("content/7851.json","w"),indent=1)
