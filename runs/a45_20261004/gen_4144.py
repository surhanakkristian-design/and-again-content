import json
T=[i*0.5 for i in range(20)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
fer={1.0:(0.28,0.17,0.28,0.27),1.5:(0.14,0.17,0.78,0.30),2.0:(0.37,0.15,0.63,0.31),5.0:(0.12,0.0,0.18,0.14),5.5:(0.16,0.0,0.18,0.14),
 8.0:(0.01,0.05,0.18,0.14),8.5:(0.10,0.08,0.18,0.14),9.0:(0.16,0.02,0.19,0.15),9.5:(0.15,0.01,0.19,0.14)}
tube={0.0:(0.67,0.61,0.33,0.39),0.5:(0.69,0.62,0.31,0.38),1.0:(0.65,0.61,0.35,0.39),1.5:(0.66,0.58,0.34,0.42),2.0:(0.49,0.46,0.51,0.54),
 2.5:(0.08,0.14,0.92,0.86),3.0:(0.0,0.0,0.45,1.0),3.5:(0.0,0.54,1.0,0.31),4.0:(0.0,0.34,1.0,0.34),4.5:(0.0,0.0,1.0,0.74),
 5.0:(0.36,0.09,0.64,0.70),5.5:(0.38,0.13,0.62,0.73),6.0:(0.08,0.03,0.92,0.67),6.5:(0.0,0.0,0.88,0.62),7.0:(0.0,0.0,0.95,0.61),
 7.5:(0.06,0.02,0.94,0.76),8.0:(0.24,0.14,0.76,0.61),8.5:(0.29,0.20,0.71,0.58),9.0:(0.36,0.20,0.64,0.60),9.5:(0.31,0.17,0.69,0.62)}
c={"mediaId":4144,"level":"A","keyWord":"tube","defaultVoice":"female",
"taps":[
 {"phrase":"to look out of a box","target":"the ferret in the box","voice":"female","keys":keys(fer)},
 {"phrase":"to lie in a circle","target":"the tube","voice":"female","keys":keys(tube)},
 {"phrase":"to be long and grey","target":"the tube","voice":"female","keys":keys(tube)}],
"stillS":0.0,
"nouns":[{"word":"a carpet","x":0.62,"y":0.17,"voice":"female"},{"word":"a box","x":0.45,"y":0.45,"voice":"female"},
 {"word":"the floor","x":0.24,"y":0.86,"voice":"female"},{"word":"a tube","x":0.80,"y":0.80,"voice":"female"}],
"question":"Where is the tube lying?",
"answer":["The","tube","is","lying","on","the","floor."],
"answerVoice":"female",
"notes":"Several ferrets that cannot be told apart run on the floor, so only two targets: the ferret in the box (keys only while a ferret is in / on the box: 1.0 jumping up, 1.5 two ferrets in the box in one region, 2.0 one climbing out, 5.0-5.5 and 8.0-9.5 a head in the peanuts; 5.0 is only a dark spot) and the tube (two phrases). The tube is a loop, so its box is large and contains floor and running ferrets; at 3.0, 4.5, 6.5, 7.0 two separate pieces of the tube are in one box. 'to be long and grey' is a state; the ferrets are dark brown. The pink packing peanuts are not named anywhere (no A-level word)."}
json.dump(c,open("content/4144.json","w"),indent=1)
