import json
T=[i*0.5 for i in range(25)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
hen={1.0:(0.18,0.27,0.32,0.21),1.5:(0.06,0.14,0.88,0.60),2.0:(0.16,0.21,0.66,0.49),2.5:(0.18,0.29,0.62,0.45),3.0:(0.05,0.35,0.72,0.55),
 3.5:(0.0,0.23,0.93,0.38),4.0:(0.25,0.29,0.54,0.41),4.5:(0.21,0.25,0.48,0.46),5.5:(0.23,0.32,0.60,0.31),
 6.0:(0.25,0.42,0.54,0.21),6.5:(0.25,0.37,0.54,0.25),7.0:(0.17,0.35,0.64,0.28),7.5:(0.07,0.32,0.74,0.33),8.0:(0.02,0.25,0.85,0.46),
 8.5:(0.28,0.17,0.70,0.58),9.0:(0.17,0.24,0.83,0.66),9.5:(0.06,0.36,0.94,0.56),10.0:(0.09,0.35,0.91,0.47),10.5:(0.09,0.35,0.91,0.48),
 11.0:(0.09,0.35,0.91,0.60),11.5:(0.09,0.35,0.91,0.60),12.0:(0.11,0.35,0.89,0.47)}
fire={0.0:(0.0,0.12,1.0,0.21),0.5:(0.0,0.10,1.0,0.23),1.0:(0.0,0.05,1.0,0.22),1.5:(0.0,0.0,1.0,0.14),2.0:(0.0,0.0,1.0,0.21),
 2.5:(0.0,0.02,1.0,0.27),3.0:(0.0,0.05,1.0,0.30),
 9.0:(0.0,0.07,0.22,0.16),9.5:(0.0,0.05,0.25,0.18),10.0:(0.0,0.0,0.33,0.23),10.5:(0.0,0.0,0.33,0.23),11.0:(0.0,0.0,0.33,0.23),
 11.5:(0.0,0.0,0.33,0.23),12.0:(0.0,0.0,0.33,0.23)}
c={"mediaId":4172,"level":"A","keyWord":"escape","defaultVoice":"female",
"taps":[
 {"phrase":"to walk through the water","target":"the hen","voice":"female","keys":keys(hen)},
 {"phrase":"to lie down on the stones","target":"the hen","voice":"female","keys":keys(hen)},
 {"phrase":"to burn in the field","target":"the fire","voice":"female","keys":keys(fire)}],
"stillS":8.0,
"nouns":[{"word":"a hill","x":0.55,"y":0.16,"voice":"female"},{"word":"a nest","x":0.26,"y":0.44,"voice":"female"},
 {"word":"a hen","x":0.58,"y":0.57,"voice":"female"},{"word":"a river","x":0.50,"y":0.85,"voice":"female"}],
"question":"What is the hen doing?",
"answer":["She","is","carrying","a","nest","through","the","river."],
"answerVoice":"female",
"notes":"Key word 'escape' (noun) is abstract, not used as a label. The hen box includes the nest while she carries it (1.5-8.0). Hen is a tiny dark dot at 0.0-0.5 (off) and hidden by the splash at 5.0 (off). Fire: in the first shot it fills the background behind the hen, its box is the band above the hen (side flames next to her are outside); in the last shot it is the small glow top left, where it burns on a hillside rather than in the field - 'to burn in the field' is true for 0.0-3.0. Fire is not visible 3.5-8.5."}
json.dump(c,open("content/4172.json","w"),indent=1)
