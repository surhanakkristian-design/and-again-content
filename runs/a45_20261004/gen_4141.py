import json
T=[i*0.5 for i in range(24)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
pink={0.0:(0.06,0.33,0.36,0.67),0.5:(0.0,0.37,0.36,0.63),1.0:(0.0,0.66,0.50,0.34),1.5:(0.0,0.67,0.58,0.30),2.0:(0.0,0.66,0.66,0.27),2.5:(0.0,0.66,0.67,0.27)}
stairs={6.0:(0.15,0.33,0.62,0.67),6.5:(0.18,0.36,0.62,0.64),7.0:(0.15,0.43,0.62,0.57),7.5:(0.18,0.46,0.62,0.54),8.0:(0.15,0.48,0.62,0.52),8.5:(0.18,0.50,0.64,0.50),9.0:(0.12,0.55,0.64,0.45)}
fall={9.5:(0.36,0.35,0.34,0.38),10.0:(0.36,0.34,0.35,0.37),10.5:(0.36,0.34,0.35,0.37),11.0:(0.36,0.34,0.35,0.37),11.5:(0.36,0.34,0.35,0.37)}
c={"mediaId":4141,"level":"B","keyWord":"lie","defaultVoice":"male",
"taps":[
 {"phrase":"to sunbathe in pink shorts","target":"the man in pink shorts","voice":"male","keys":keys(pink)},
 {"phrase":"to descend a steep cliff","target":"the staircase","voice":"male","keys":keys(stairs)},
 {"phrase":"to plunge into a gorge","target":"the waterfall","voice":"male","keys":keys(fall)}],
"stillS":10.5,
"nouns":[{"word":"the sky","x":0.45,"y":0.14,"voice":"male"},{"word":"a waterfall","x":0.50,"y":0.48,"voice":"male"},
 {"word":"a hillside","x":0.82,"y":0.46,"voice":"male"},{"word":"trainers","x":0.50,"y":0.79,"voice":"male"}],
"question":"What are the men doing?",
"answer":["They","are","lying","on","their","backs","beside","a","lake."],
"answerVoice":"male",
"notes":"Key word 'lie' (verb) is in the answer. Six men in the first shot; only one wears pink shorts, his box overlaps his neighbours (no other target there). The second shot (people lying in long grass, 3.0-5.5) has no target. 'the staircase' box includes both railings; the POV legs overlap it. Nouns are on the waterfall shot; 'a hillside' = the green slope on the right."}
json.dump(c,open("content/4141.json","w"),indent=1)
