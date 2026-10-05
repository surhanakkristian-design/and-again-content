import json
T=[i*0.5 for i in range(21)]
wom={0.0:(0.52,0.48,0.48,0.52),0.5:(0.48,0.48,0.52,0.52),1.5:(0.47,0.52,0.53,0.26),2.0:(0.72,0.41,0.28,0.21),
2.5:(0.80,0.15,0.20,0.35),3.0:(0.82,0.10,0.18,0.42),3.5:(0.48,0.33,0.52,0.67),4.0:(0.48,0.0,0.52,1.0),4.5:(0.50,0.0,0.50,1.0),
5.0:(0.40,0.0,0.60,0.74),5.5:(0.56,0.0,0.44,0.55),6.0:(0.56,0.0,0.44,0.56),6.5:(0.62,0.0,0.38,0.70),7.0:(0.28,0.03,0.72,0.60),
7.5:(0.43,0.15,0.57,0.66),8.0:(0.55,0.12,0.45,0.72),8.5:(0.34,0.20,0.66,0.66),9.0:(0.04,0.29,0.96,0.71),9.5:(0.0,0.29,1.0,0.71),
10.0:(0.0,0.30,1.0,0.57)}
rob={5.0:(0.16,0.74,0.62,0.26),5.5:(0.28,0.55,0.52,0.21),6.0:(0.31,0.56,0.50,0.21),6.5:(0.08,0.71,0.72,0.29),
7.0:(0.70,0.75,0.30,0.25),7.5:(0.58,0.81,0.34,0.19),8.0:(0.50,0.84,0.22,0.16),8.5:(0.46,0.86,0.26,0.14),10.0:(0.65,0.87,0.25,0.13)}
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":round(min(w,1-x),2),"h":round(min(h,1-y),2)})
        else: out.append({"t":t,"off":True})
    return out
c={"mediaId":5434,"level":"B","keyWord":"electricity","defaultVoice":"female",
"taps":[{"phrase":"to flick a light switch","target":"the woman","voice":"female","keys":keys(wom)},
{"phrase":"to fling her arms wide","target":"the woman","voice":"female","keys":keys(wom)},
{"phrase":"to glide across the floor","target":"the robot vacuum","voice":"female","keys":keys(rob)}],
"stillS":8.5,
"nouns":[{"word":"fairy lights","x":0.55,"y":0.15,"voice":"female"},{"word":"a floor lamp","x":0.20,"y":0.37,"voice":"female"},
{"word":"a power strip","x":0.15,"y":0.74,"voice":"female"},{"word":"a robot vacuum","x":0.60,"y":0.90,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","flinging","her","arms","wide."],"answerVoice":"female",
"notes":"Key word 'electricity' is abstract, not placed as a noun. Woman is only a hand/arm at 0-3.5 and absent at 1.0 (off). Robot vacuum off at 9.0-9.5 (hidden behind her legs) and before 5.0; at 10.0 the boxes are split at y 0.87 (vacuum right behind her feet). Blender (3.5-4.5) not used."}
json.dump(c,open('content/5434.json','w'),indent=1)
