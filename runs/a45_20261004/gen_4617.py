import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
B={0.0:(0.0,0.12,1.0,0.88),0.5:(0.0,0.06,0.64,0.94),1.0:(0.0,0.03,0.72,0.97),1.5:(0.0,0.02,1.0,0.98),
 2.0:(0.36,0.28,0.32,0.46),2.5:(0.33,0.26,0.33,0.48),3.0:(0.30,0.29,0.38,0.47),3.5:(0.30,0.28,0.42,0.48),
 4.0:(0.31,0.28,0.48,0.52),4.5:(0.24,0.22,0.39,0.63),5.0:(0.04,0.26,0.58,0.65),5.5:(0.08,0.26,0.68,0.66),
 6.0:(0.14,0.25,0.65,0.65),6.5:(0.17,0.23,0.60,0.67),7.0:(0.17,0.21,0.62,0.74),7.5:(0.04,0.17,0.66,0.81),
 8.0:(0.05,0.17,0.47,0.81),8.5:(0.08,0.19,0.50,0.81),9.0:(0.05,0.15,0.48,0.85)}
FL={t:(0.0,0.0,1.0,0.09) for t in (2.0,2.5,3.0,3.5)}
F={6.0:(0.80,0.66,0.20,0.20),6.5:(0.78,0.68,0.22,0.20),7.0:(0.80,0.70,0.20,0.18),7.5:(0.71,0.70,0.29,0.18),
 8.0:(0.54,0.74,0.46,0.16),8.5:(0.60,0.77,0.40,0.17),9.0:(0.54,0.80,0.46,0.19)}
c={"mediaId":4617,"level":"B","keyWord":"fight","defaultVoice":"male",
"taps":[
 {"phrase":"to grip a blue shield","target":"the bald man","voice":"male","keys":keys(B)},
 {"phrase":"to flutter in the wind","target":"the flags","voice":"male","keys":keys(FL)},
 {"phrase":"to lie motionless on the grass","target":"the man on the ground","voice":"male","keys":keys(F)}],
"stillS":7.5,
"nouns":[{"word":"spectators","x":0.50,"y":0.09,"voice":"male"},{"word":"a helmet","x":0.80,"y":0.27,"voice":"male"},
 {"word":"a shield","x":0.55,"y":0.58,"voice":"male"},{"word":"armor","x":0.20,"y":0.82,"voice":"male"}],
"question":"What are the men doing?",
"answer":["The","men","are","fighting","in","front","of","spectators."],
"answerVoice":"male",
"notes":"Bald red-bearded man = the only one with the blue shield (the shield vanishes from his hand at 8.0-9.0, generated clip). The man on the ground lies BEHIND the fighters' legs from 6.0; his box is the visible part right of the bald man's box (split along x), weak at 6.0-7.0. Flags only in the wide shots 2.0-3.5. Still 7.5: 'a shield' pill is on the blue shield (a second, white shield at the right edge), 'a helmet' on the right fighter (another helmet far left). US spelling 'armor' (key words in this set are US: colorful)."}
json.dump(c,open('content/4617.json','w'),indent=1)
