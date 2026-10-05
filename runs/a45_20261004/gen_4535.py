import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
glasses={0.0:(0,0.03,0.64,0.67),0.5:(0,0,0.68,0.70),1.0:(0,0,0.72,0.83),1.5:(0,0,0.72,0.83),2.0:(0,0.03,0.74,0.72),
2.5:(0,0.13,0.62,0.52),3.0:(0,0.13,0.55,0.65),3.5:(0,0.13,0.52,0.65),4.0:(0,0.10,0.60,0.58),4.5:(0,0.12,0.55,0.55),5.0:(0,0.15,0.52,0.62)}
black={5.5:(0.30,0.20,0.30,0.46),6.0:(0.31,0.11,0.27,0.44),6.5:(0.25,0.0,0.27,0.38),7.0:(0.17,0.03,0.26,0.47),7.5:(0.02,0.17,0.26,0.39)}
grey={5.5:(0.60,0.30,0.36,0.55),6.0:(0.58,0.20,0.36,0.45),6.5:(0.52,0.0,0.42,0.52),7.0:(0.43,0.11,0.36,0.58),7.5:(0.28,0.22,0.27,0.42),
8.0:(0.09,0.30,0.34,0.45),8.5:(0.05,0.36,0.34,0.42),9.0:(0.0,0.44,0.42,0.44),9.5:(0,0.45,0.40,0.42),10.0:(0,0.46,0.34,0.42)}
c={"mediaId":4535,"level":"A","keyWord":"lesson","defaultVoice":"male",
"taps":[
 {"phrase":"to hold a grey bag","target":"the boy in glasses","voice":"male","keys":keys(glasses)},
 {"phrase":"to throw a ball","target":"the boy in black","voice":"male","keys":keys(black)},
 {"phrase":"to clap his hands","target":"the boy at the desk","voice":"male","keys":keys(grey)}],
"stillS":7.0,
"nouns":[{"word":"a bin","x":0.25,"y":0.75,"voice":"male"},{"word":"a chair","x":0.72,"y":0.43,"voice":"male"},
 {"word":"a bag","x":0.88,"y":0.53,"voice":"male"},{"word":"a desk","x":0.68,"y":0.34,"voice":"male"}],
"question":"What is the boy in black doing?",
"answer":["He","is","throwing","a","ball","into","the","bin."],
"answerVoice":"male",
"notes":"Key word 'lesson' is not a visible noun. Three boys: in glasses (shot 1, grey hoodie, grey backpack on his lap from 2.5 s), in black (thrower, 5.5-7.5 s, then off), at the front desk (grey jumper, claps 7.5-8.5 s). The thrown thing looks like paper at 5.5 s and a yellow ball from 6.0 s; called 'a ball'."}
json.dump(c,open("content/4535.json","w"),indent=1)
