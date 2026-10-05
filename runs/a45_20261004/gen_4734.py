import json
T=[i*0.5 for i in range(19)]
def keys(d):
    return [{"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
Y={0.0:(0,0.23,0.46,0.77),0.5:(0,0.24,0.52,0.76),1.0:(0,0.25,0.47,0.75),1.5:(0,0.26,0.48,0.74),2.0:(0,0.25,0.50,0.75),
2.5:(0,0.26,0.52,0.74),3.0:(0,0.26,0.52,0.74),3.5:(0,0.26,0.52,0.74),4.0:(0,0.27,0.53,0.73),4.5:(0,0.27,0.46,0.73),
5.0:(0,0.29,0.44,0.71),5.5:(0,0.29,0.44,0.71),6.0:(0,0.28,0.41,0.72),6.5:(0,0.29,0.41,0.71),7.0:(0,0.30,0.55,0.70),
7.5:(0,0.30,0.50,0.70),8.0:(0,0.29,0.42,0.71),8.5:(0,0.30,0.42,0.70),9.0:(0,0.31,0.42,0.69)}
O={0.0:(0.47,0.14,0.53,0.48),0.5:(0.53,0.14,0.47,0.48),1.0:(0.48,0.15,0.52,0.48),1.5:(0.49,0.15,0.51,0.48),2.0:(0.51,0.15,0.49,0.47),
2.5:(0.53,0.15,0.47,0.48),3.0:(0.53,0.16,0.47,0.48),3.5:(0.53,0.16,0.47,0.48),4.0:(0.54,0.15,0.46,0.48),4.5:(0.47,0.16,0.53,0.47),
5.0:(0.45,0.18,0.55,0.60),5.5:(0.45,0.20,0.55,0.55),6.0:(0.42,0.20,0.58,0.45),6.5:(0.42,0.18,0.58,0.42),7.0:(0.57,0.17,0.43,0.55),
7.5:(0.52,0.20,0.48,0.50),8.0:(0.43,0.18,0.57,0.45),8.5:(0.43,0.19,0.57,0.45),9.0:(0.43,0.21,0.57,0.45)}
L={0.0:(0.58,0,0.38,0.14),0.5:(0.58,0,0.38,0.14),1.0:(0.57,0,0.36,0.15),1.5:(0.56,0,0.35,0.15),2.0:(0.55,0,0.36,0.15),
2.5:(0.54,0,0.36,0.15),3.0:(0.53,0,0.36,0.16),3.5:(0.54,0,0.36,0.16),4.0:(0.54,0,0.36,0.15),4.5:(0.54,0,0.36,0.16),
5.0:(0.55,0,0.36,0.18),5.5:(0.55,0,0.36,0.19),6.0:(0.56,0,0.38,0.19),6.5:(0.58,0,0.38,0.18),7.0:(0.60,0,0.38,0.17),
7.5:(0.62,0,0.38,0.19),8.0:(0.62,0,0.38,0.18),8.5:(0.62,0,0.38,0.18),9.0:(0.61,0,0.38,0.20)}
d={"mediaId":4734,"level":"A","keyWord":"care","defaultVoice":"female",
"taps":[
 {"phrase":"to lie under a blanket","target":"the young woman","voice":"female","keys":keys(Y)},
 {"phrase":"to take care of her","target":"the older woman","voice":"female","keys":keys(O)},
 {"phrase":"to light the room","target":"the lamp","voice":"female","keys":keys(L)}],
"stillS":3.5,
"nouns":[{"word":"a lamp","x":0.74,"y":0.06,"voice":"female"},{"word":"a pillow","x":0.33,"y":0.26,"voice":"female"},
 {"word":"a blanket","x":0.50,"y":0.75,"voice":"female"}],
"question":"What is the older woman doing?",
"answer":["She","is","taking","care","of","the","young","woman."],
"answerVoice":"female",
"notes":"Key word 'care' is used as 'to take care of' (phrase 2 and the answer); 'her' in phrase 2 = the sick young woman. The older woman holds/reads thermometers, feels the forehead (4.5-6.5 s) and lays a blue cloth on it (7-9 s). Box limits: the young woman's box is her head plus the left part of the blanket (a rectangle cannot hold the whole blanket without the older woman); when the older woman's hand lies on the forehead (5-6.5 s, 8-9 s) the split runs through her forearm, so the hand itself falls into the young woman's box. The lamp box is the shade and upper stem only, ending where the older woman's head begins. Only 3 nouns: other visible things (thermometer, cloth) are above level A or move; 'a pillow' = the cream pillow behind the young woman's head (a grey one lies to the right of it)."}
json.dump(d,open("content/4734.json","w"),ensure_ascii=False,indent=1)
