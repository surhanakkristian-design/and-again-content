import json
times=[i*0.5 for i in range(31)]
def keys(d):
    return [dict(t=t, **({"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"off":True})) for t in times]
man={t:(0.41,0.36,0.26,0.20) for t in (4.5,5.0,5.5,6.0,6.5,7.0)}
rec={2.5:(0.16,0.41,0.60,0.18),3.0:(0.10,0.42,0.68,0.19),3.5:(0.06,0.43,0.75,0.20),4.0:(0.02,0.44,0.82,0.22)}
lan={7.5:(0.22,0.0,0.56,0.37),8.0:(0.24,0.0,0.58,0.36),8.5:(0.27,0.0,0.59,0.35),9.0:(0.32,0.0,0.60,0.35),9.5:(0.37,0.0,0.63,0.34)}
c={"mediaId":4017,"level":"B","keyWord":"a lantern","defaultVoice":"male",
"taps":[
 {"phrase":"to prepare a meal","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to spin on a turntable","target":"the record","voice":"male","keys":keys(rec)},
 {"phrase":"to hang above the bed","target":"the orange lantern","voice":"male","keys":keys(lan)}],
"stillS":8.0,
"nouns":[{"word":"a lantern","x":0.52,"y":0.16,"voice":"male"},
 {"word":"the skyline","x":0.22,"y":0.38,"voice":"male"},
 {"word":"pillows","x":0.74,"y":0.63,"voice":"male"},
 {"word":"a blanket","x":0.18,"y":0.67,"voice":"male"}],
"question":"What is glowing above the bed?",
"answer":["A","paper","lantern","is","glowing","above","the","bed."],
"answerVoice":"male",
"notes":"Clip is a tour with cuts: red standing lantern 0-2.0 s (not used as target; phrase 'to hang above the bed' fits only the orange ceiling lantern at 7.5-9.5 s). Man seen from behind at the kitchen counter with steam rising, 'to prepare a meal' is read from that. Record: spinning judged from the changing label highlights between frames. Two candles in the still, so 'a candle' was not used as a noun."}
json.dump(c,open("content/4017.json","w"),indent=1)
