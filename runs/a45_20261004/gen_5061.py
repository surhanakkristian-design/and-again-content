import json
def keys(times, boxes):
    return [{"t":t,"off":True} if boxes.get(t) is None else {"t":t,"x":boxes[t][0],"y":boxes[t][1],"w":boxes[t][2],"h":boxes[t][3]} for t in times]
T=[i*0.5 for i in range(19)]
man={0.0:(0.0,0.28,0.84,0.72),0.5:(0.0,0.29,0.88,0.71),1.0:(0.0,0.24,0.90,0.76),1.5:(0.0,0.20,0.92,0.80),2.0:(0.0,0.23,0.76,0.77),2.5:(0.0,0.24,0.92,0.76),
3.0:(0.04,0.34,0.72,0.66),3.5:(0.25,0.38,0.50,0.62),4.0:(0.29,0.43,0.45,0.57),4.5:(0.29,0.44,0.40,0.56),5.0:(0.30,0.46,0.40,0.54),5.5:(0.32,0.49,0.37,0.51),
6.0:(0.26,0.42,0.40,0.53),6.5:(0.28,0.43,0.38,0.52),7.0:(0.36,0.43,0.33,0.56),7.5:(0.25,0.44,0.60,0.54),8.0:(0.12,0.44,0.70,0.53),8.5:(0.10,0.44,0.74,0.53),9.0:(0.14,0.45,0.72,0.54)}
sh={t:(0.0,0.0,1.0,0.34) for t in [6.0,6.5,7.0,7.5,8.0,8.5,9.0]}
c={"mediaId":5061,"level":"B","keyWord":"aquarium","defaultVoice":"male",
"taps":[
 {"phrase":"to ride up an escalator","target":"the young man","voice":"male","keys":keys(T,man)},
 {"phrase":"to spread his arms wide","target":"the young man","voice":"male","keys":keys(T,man)},
 {"phrase":"to glide through the water","target":"the sharks","voice":"male","keys":keys(T,sh)}],
"stillS":8.0,
"nouns":[{"word":"an aquarium","x":0.50,"y":0.20,"voice":"male"},
 {"word":"a tunnel","x":0.80,"y":0.45,"voice":"male"},
 {"word":"a railing","x":0.82,"y":0.615,"voice":"male"},
 {"word":"an ice rink","x":0.22,"y":0.70,"voice":"male"}],
"question":"What is the young man looking at?",
"answer":["He","is","staring","up","at","the","sharks."],
"answerVoice":"male",
"notes":"Only one person target, so two phrases share the young man; 'to ride up an escalator' is true only 0-2.5 s (then he walks the atrium floor). The sharks are a group target, boxed as the upper tank (y 0-0.34) from 6.0; several sharks, small and moving. Skaters below are tiny and behind the man, not used."}
json.dump(c,open('content/5061.json','w'),indent=1)
