import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
J={0.0:(0.03,0.36,0.47,0.64),0.5:(0.06,0.36,0.46,0.64),1.0:(0.03,0.36,0.47,0.64),1.5:(0.0,0.36,0.53,0.64),
2.0:(0.0,0.37,0.50,0.63),2.5:(0.06,0.37,0.48,0.63),3.0:(0.0,0.39,0.53,0.61),3.5:(0.0,0.39,0.52,0.61),
4.0:(0.0,0.42,0.50,0.58),4.5:(0.15,0.40,0.45,0.60),5.0:(0.13,0.44,0.47,0.54),5.5:(0.10,0.42,0.42,0.56),
6.0:(0.0,0.22,0.40,0.73),6.5:(0.0,0.18,0.42,0.82),7.0:(0.0,0.27,0.48,0.73),7.5:(0.0,0.37,0.72,0.63),
8.0:(0.0,0.29,0.63,0.71),8.5:(0.0,0.25,0.66,0.75),9.0:(0.0,0.30,0.66,0.70),9.5:(0.0,0.30,0.73,0.70),10.0:(0.0,0.27,0.74,0.73)}
H={0.0:(0.50,0.23,0.50,0.77),0.5:(0.52,0.23,0.48,0.77),1.0:(0.50,0.24,0.50,0.76),1.5:(0.53,0.23,0.47,0.77),
2.0:(0.50,0.24,0.50,0.76),2.5:(0.54,0.25,0.46,0.75),3.0:(0.53,0.27,0.47,0.73),3.5:(0.56,0.26,0.44,0.74),
4.0:(0.57,0.27,0.43,0.73),4.5:(0.60,0.30,0.40,0.70),5.0:(0.62,0.32,0.38,0.68),5.5:(0.56,0.31,0.44,0.69),
6.0:(0.40,0.10,0.60,0.85),6.5:(0.42,0.02,0.58,0.98),7.0:(0.48,0.11,0.52,0.89),7.5:(0.76,0.38,0.24,0.62),
8.0:(0.64,0.24,0.36,0.76),8.5:(0.67,0.22,0.33,0.78),9.0:(0.67,0.08,0.33,0.92),9.5:(0.74,0.10,0.26,0.90),10.0:(0.75,0.11,0.25,0.89)}
S={3.5:(0.27,0.18,0.28,0.21),4.0:(0.30,0.20,0.27,0.22),4.5:(0.30,0.20,0.28,0.20),5.0:(0.38,0.27,0.24,0.17),5.5:(0.38,0.27,0.18,0.15)}
d={"mediaId":4729,"level":"A","keyWord":"afraid","defaultVoice":"female",
"taps":[
 {"phrase":"to hold her friend's arm","target":"the woman in the jacket","voice":"female","keys":keys(J)},
 {"phrase":"to wear a green hoodie","target":"the woman in green","voice":"female","keys":keys(H)},
 {"phrase":"to stand behind the women","target":"the skeleton","voice":"female","keys":keys(S)}],
"stillS":9.0,
"nouns":[{"word":"the sky","x":0.11,"y":0.10,"voice":"female"},{"word":"a curtain","x":0.60,"y":0.22,"voice":"female"},
 {"word":"a hoodie","x":0.82,"y":0.62,"voice":"female"},{"word":"a jacket","x":0.16,"y":0.71,"voice":"female"}],
"question":"How do the two women feel?",
"answer":["They","are","afraid","of","the","skeleton."],
"answerVoice":"female",
"notes":"The packet says 'masked figure in a white mask'; the frames show a plastic skeleton standing in the corridor (3.5-5.5 s, blurred and small at 5.5 s). The woman in the jacket grips the other's arm 0-4.5 s; outside they hold hands (mutual), so 'arm' fits only her. The hoodie woman has no action that only she does, so a state phrase. The two women overlap all the time; boxes split along the line between them. At 7.5-8.5 s the hoodie woman is only a headless green body at the right edge. Question is a state (feel), so present simple."}
json.dump(d,open("content/4729.json","w"),ensure_ascii=False,indent=1)
