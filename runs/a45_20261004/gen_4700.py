import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
man={0.0:(0,0.05,0.58,0.85),0.5:(0,0.05,0.58,0.85),1.0:(0,0.13,0.57,0.87),1.5:(0,0.18,0.54,0.82),
2.0:(0.34,0.26,0.48,0.47),2.5:(0.36,0.26,0.46,0.47),3.0:(0.34,0.26,0.48,0.47),3.5:(0.38,0.26,0.41,0.47),
4.0:(0.38,0.26,0.31,0.46),4.5:(0.40,0.26,0.29,0.46),5.0:(0.40,0.26,0.24,0.45),
5.5:(0.03,0.30,0.50,0.32),6.0:(0.03,0.29,0.52,0.36),6.5:(0.05,0.29,0.50,0.36),7.0:(0.05,0.31,0.51,0.35),
7.5:(0.07,0.32,0.52,0.35),8.0:(0.07,0.33,0.51,0.36),8.5:(0.03,0.34,0.55,0.36),9.0:(0,0.35,0.58,0.37)}
rob={0.0:(0.59,0.28,0.41,0.67),0.5:(0.59,0.28,0.41,0.67),1.0:(0.58,0.22,0.42,0.78),1.5:(0.55,0.25,0.45,0.72),
2.0:(0.82,0.30,0.18,0.44),2.5:(0.82,0.30,0.18,0.44),3.0:(0.82,0.30,0.18,0.46),3.5:(0.80,0.30,0.20,0.48),
4.0:(0.70,0.30,0.30,0.44),4.5:(0.70,0.30,0.30,0.44),5.0:(0.65,0.39,0.35,0.39),
5.5:(0.54,0.46,0.42,0.24),6.0:(0.56,0.38,0.34,0.33),6.5:(0.56,0.38,0.34,0.33),7.0:(0.57,0.40,0.34,0.33),
7.5:(0.61,0.42,0.33,0.31),8.0:(0.60,0.43,0.32,0.31),8.5:(0.60,0.44,0.32,0.31),9.0:(0.60,0.46,0.32,0.32)}
j={"mediaId":4700,"level":"B","keyWord":"robot","defaultVoice":"male",
"taps":[
{"phrase":"to tighten a screw","target":"the man at the laptop","voice":"male","keys":keys(man)},
{"phrase":"to sip from a mug","target":"the man at the laptop","voice":"male","keys":keys(man)},
{"phrase":"to hold out a mug","target":"the robot arm","voice":"male","keys":keys(rob)}],
"stillS":4.5,
"nouns":[{"word":"a robot","x":0.84,"y":0.50,"voice":"male"},{"word":"a laptop","x":0.20,"y":0.63,"voice":"male"},
{"word":"a mug","x":0.56,"y":0.77,"voice":"male"},{"word":"cables","x":0.30,"y":0.91,"voice":"male"}],
"question":"What is the robot doing?",
"answer":["It","is","holding","out","a","mug."],
"answerVoice":"male",
"notes":"Two targets only (main man, robot arm); the two colleagues in the background are tiny and both cheer, so no phrase for them. 'to tighten a screw': he works on the gripper with a screwdriver at 0-0.5 (the screw itself is not visible). In the close shot (0-1.5) his right hand holds the gripper inside the robot's box (split at x 0.58). In shot 2 the arm stands in front of his left shoulder: boxes split in x, so his shoulder right of the arm is in the robot's box. From 6.0 the mug is in his hands / the man's box. 'a robot' pill sits on the robot arm; 'the robot' in question and answer = the arm."}
json.dump(j,open("content/4700.json","w"),indent=1)
