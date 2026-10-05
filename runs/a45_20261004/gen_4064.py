import json
def K(times,f):
    o=[]
    for t in times:
        b=f.get(t)
        o.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return o
T=[i*0.5 for i in range(21)]
bird={0.0:(0.33,0.34,0.45,0.50),0.5:(0.30,0.34,0.45,0.50),1.0:(0.28,0.36,0.45,0.50),1.5:(0.10,0.66,0.80,0.34),
2.0:(0.05,0.60,0.90,0.40),2.5:(0.05,0.62,0.90,0.38),3.0:(0.05,0.68,0.90,0.32),3.5:(0.05,0.67,0.90,0.33),4.0:(0.0,0.63,1.0,0.37),
4.5:(0.18,0.39,0.70,0.61),5.0:(0.23,0.42,0.68,0.58),5.5:(0.23,0.43,0.57,0.57),6.0:(0.0,0.60,0.90,0.40),6.5:(0.0,0.60,1.0,0.40),
7.0:(0.15,0.61,0.75,0.39),7.5:(0.20,0.60,0.75,0.40),8.0:(0.10,0.60,0.85,0.40),8.5:(0.05,0.60,0.95,0.40),9.0:(0.0,0.69,1.0,0.31),
9.5:(0.05,0.67,0.95,0.33),10.0:(0.05,0.58,0.90,0.42)}
pole={0.0:(0.38,0.12,0.20,0.22),0.5:(0.38,0.13,0.20,0.21),1.0:(0.38,0.13,0.20,0.23),1.5:(0.36,0.24,0.20,0.36),
2.0:(0.36,0.27,0.20,0.33),2.5:(0.36,0.32,0.20,0.30),3.0:(0.35,0.40,0.20,0.28),3.5:(0.35,0.46,0.20,0.21),4.0:(0.33,0.51,0.24,0.12)}
nest={0.0:(0.35,0.0,0.26,0.12),0.5:(0.35,0.0,0.26,0.13),1.0:(0.35,0.0,0.26,0.13),1.5:(0.33,0.09,0.31,0.15),
2.0:(0.30,0.13,0.34,0.14),2.5:(0.27,0.16,0.39,0.16),3.0:(0.24,0.20,0.45,0.20),3.5:(0.18,0.21,0.56,0.25),4.0:(0.10,0.17,0.78,0.34),
4.5:(0.0,0.0,1.0,0.39),5.0:(0.0,0.0,1.0,0.42),5.5:(0.0,0.0,1.0,0.43)}
d={"mediaId":4064,"level":"B","keyWord":"pole","defaultVoice":"female",
"taps":[
 {"phrase":"to support a huge nest","target":"the pole","voice":"female","keys":K(T,pole)},
 {"phrase":"to balance on the pole","target":"the nest","voice":"female","keys":K(T,nest)},
 {"phrase":"to carry a tiny camera","target":"the parakeet with the camera","voice":"female","keys":K(T,bird)}],
"stillS":2.5,
"nouns":[{"word":"a nest","x":0.47,"y":0.25,"voice":"female"},{"word":"power lines","x":0.78,"y":0.35,"voice":"female"},{"word":"a pole","x":0.46,"y":0.44,"voice":"female"},{"word":"a field","x":0.22,"y":0.54,"voice":"female"}],
"question":"Where is the parakeet flying?",
"answer":["It","is","flying","towards","the","nest","on","the","pole."],
"answerVoice":"female",
"notes":"Pole box = the shaft below the nest only, nest box above it (split at the nest's lower edge). 4.5-5.5 s the camera is at the nest entrance: nest box = the twigs above the bird; from 6.0 s (inside, straw tunnel/chamber) nest is off. The parakeet with the camera is seen from behind (blurred green back at the bottom) 1.5-4.0 and 6.0-9.5 s, almost black at 7.0-8.0 s. Hands at 0-1.0 s are not a target (two hands on both sides of the bird). Four other parakeets at 8.5-10 s carry no camera."}
json.dump(d,open("content/4064.json","w"),indent=1)
