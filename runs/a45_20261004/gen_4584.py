import json
def K(rows):
    return [{"t":r[0],"x":r[1],"y":r[2],"w":r[3],"h":r[4]} for r in rows]
tu=[(0.22,0.42,0.62,0.19),(0.19,0.43,0.62,0.19),(0.18,0.45,0.69,0.19),(0.18,0.46,0.66,0.19),(0.16,0.47,0.66,0.19),(0.23,0.49,0.63,0.20),
(0.16,0.52,0.63,0.19),(0.23,0.53,0.59,0.20),(0.16,0.54,0.62,0.19),(0.18,0.57,0.62,0.19),(0.18,0.59,0.64,0.20),(0.14,0.61,0.62,0.19),
(0.14,0.61,0.62,0.20),(0.18,0.62,0.58,0.20),(0.14,0.64,0.56,0.18),(0.14,0.64,0.58,0.18),(0.20,0.65,0.52,0.18),(0.16,0.65,0.53,0.18),
(0.18,0.67,0.51,0.17),(0.21,0.67,0.50,0.17),(0.23,0.66,0.44,0.18),(0.26,0.67,0.46,0.18),(0.28,0.68,0.38,0.18),(0.28,0.68,0.41,0.16),(0.28,0.67,0.48,0.16)]
wo=[(0.50,0,0.50,0.33),(0.50,0,0.50,0.33),(0.50,0,0.50,0.34),(0.50,0,0.50,0.35),(0.50,0,0.50,0.36),(0.50,0,0.50,0.37),
(0.50,0,0.50,0.38),(0.50,0,0.50,0.39),(0.50,0,0.50,0.41),(0.50,0,0.50,0.42),(0.51,0,0.49,0.43),(0.51,0,0.49,0.43),
(0.51,0,0.49,0.44),(0.51,0,0.49,0.44),(0.53,0,0.47,0.45),(0.53,0,0.47,0.45),(0.54,0,0.46,0.45),(0.54,0,0.46,0.45),
(0.56,0,0.44,0.45),(0.56,0,0.44,0.45),(0.58,0,0.42,0.46),(0.58,0,0.42,0.46),(0.56,0,0.44,0.46),(0.56,0,0.44,0.46),(0.54,0,0.46,0.45)]
T=K([(i/2,)+b for i,b in enumerate(tu)]); W=K([(i/2,)+b for i,b in enumerate(wo)])
d={"mediaId":4584,"level":"B","keyWord":"trail","defaultVoice":"female",
"taps":[
 {"phrase":"to lead the other turtles","target":"the first turtle","voice":"female","keys":T},
 {"phrase":"to gasp in delight","target":"the woman","voice":"female","keys":W},
 {"phrase":"to kneel on the sand","target":"the woman","voice":"female","keys":W}],
"stillS":9.5,
"nouns":[{"word":"a headband","x":0.80,"y":0.06,"voice":"female"},{"word":"foam","x":0.24,"y":0.53,"voice":"female"},
 {"word":"a turtle","x":0.47,"y":0.74,"voice":"female"},{"word":"a trail","x":0.50,"y":0.91,"voice":"female"}],
"question":"What are the turtles leaving behind?",
"answer":["They","are","leaving","a","trail","in","the","sand."],
"answerVoice":"female",
"notes":"One take, the camera slowly rises. The first turtle = the big hatchling nearest the camera, in front of the line of smaller ones; its box follows it down the frame. The woman: at 0-3.5 s only her knees, arms and hands at the mouth are in the picture (face out of frame), her face comes in from 4 s; both woman phrases share her keys. Only two targets: a third one (the wave, the trail, another turtle) could not get a box clear of the first turtle and the line of hatchlings, so the woman has two phrases. 'a turtle' pill sits on the first turtle (several turtles in the picture, no other noun is on them). 'foam' = the white edge of the wave on the left at 9.5 s; 'a trail' = the track of flipper prints in front of the first turtle. The answer's subject is 'They' (the turtles) -> default voice."}
json.dump(d,open("content/4584.json","w"),indent=1,ensure_ascii=False)
