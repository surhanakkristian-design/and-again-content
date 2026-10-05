import json
T=[i*0.5 for i in range(21)]
B=[(0,.08,1,.92),(0,.11,1,.89),(0,.14,1,.86),(0,.13,.97,.87),(0,.10,1,.85),(0,.32,1,.51),(0,.45,1,.45),(.04,.45,.84,.41),(.24,.42,.72,.26),(.33,.38,.67,.27),(.06,.38,.91,.44),(.15,.41,.85,.28),(.38,.18,.62,.35),(.42,.10,.58,.36),(.46,.18,.51,.54),(.36,.36,.48,.54),(.07,.34,.64,.49),(.2,0,.48,.58),(.34,.24,.34,.44),(.32,.31,.36,.42),None]
keys=[{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,B)]
d={"mediaId":542,"level":"A","keyWord":"penguin","defaultVoice":"female",
"taps":[{"phrase":p,"target":"the penguin","voice":"female","keys":keys} for p in ["to walk on the snow","to slide on its belly","to swim under the ice"]],
"stillS":4.0,
"nouns":[{"word":"the sky","x":.5,"y":.08,"voice":"female"},{"word":"water","x":.68,"y":.35,"voice":"female"},{"word":"a penguin","x":.62,"y":.55,"voice":"female"},{"word":"snow","x":.45,"y":.82,"voice":"female"}],
"question":"What is the penguin doing?","answer":["It","is","sliding","on","the","snow."],"answerVoice":"female",
"notes":"One target only (the big penguin); the far penguins in the background are tiny dots. Walks 0-2 s, slides 2.5-5 s, swims under the ice 5.5-9 s, jumps out 9.5 s; at 10.0 s only a splash is left (off). At 5.5 s the picture is dark and the penguin is hard to see. The answer describes the middle part of the clip."}
json.dump(d,open("content/542.json","w"),indent=1,ensure_ascii=False)
