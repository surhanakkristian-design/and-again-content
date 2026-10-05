import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
man={0.0:(0,0.22,0.42,0.72),0.5:(0,0.22,0.42,0.72),1.0:(0,0.23,0.42,0.71),1.5:(0,0.23,0.42,0.71),2.0:(0,0.23,0.43,0.71),2.5:(0,0.23,0.43,0.71),
 3.0:(0,0.24,0.42,0.70),3.5:(0,0.23,0.44,0.71),4.0:(0,0.23,0.46,0.71),4.5:(0,0.23,0.48,0.72),5.0:(0,0.23,0.50,0.75),5.5:(0,0.24,0.50,0.74),
 6.0:(0,0.24,0.52,0.74),6.5:(0,0.20,0.50,0.78),7.0:(0,0.24,0.36,0.74),7.5:(0,0.24,0.34,0.72),8.0:(0,0.24,0.42,0.72),8.5:(0,0.24,0.44,0.72),
 9.0:(0,0.24,0.42,0.72),9.5:(0,0.24,0.42,0.72),10.0:(0,0.22,0.43,0.72)}
woman={0.0:(0.42,0.22,0.36,0.60),0.5:(0.42,0.22,0.36,0.60),1.0:(0.42,0.23,0.36,0.60),1.5:(0.42,0.23,0.36,0.60),2.0:(0.43,0.23,0.35,0.60),2.5:(0.43,0.23,0.35,0.60),
 3.0:(0.42,0.24,0.36,0.60),3.5:(0.44,0.22,0.32,0.62),4.0:(0.46,0.22,0.30,0.62),4.5:(0.48,0.22,0.28,0.62),5.0:(0.50,0.22,0.28,0.60),5.5:(0.50,0.23,0.34,0.60),
 6.0:(0.52,0.23,0.34,0.47),6.5:(0.50,0.21,0.36,0.50),7.0:(0.36,0.21,0.31,0.60),7.5:(0.34,0.23,0.42,0.52),8.0:(0.42,0.22,0.38,0.50),8.5:(0.44,0.22,0.35,0.50),
 9.0:(0.42,0.22,0.37,0.52),9.5:(0.42,0.22,0.37,0.52),10.0:(0.43,0.20,0.33,0.52)}
cat={0.0:(0.78,0.23,0.22,0.20),0.5:(0.78,0.23,0.22,0.20),1.0:(0.78,0.24,0.22,0.20),1.5:(0.78,0.24,0.22,0.20),2.0:(0.78,0.24,0.22,0.20),2.5:(0.78,0.24,0.22,0.20),
 3.0:(0.78,0.25,0.22,0.20),3.5:(0.76,0.25,0.22,0.20),4.0:(0.76,0.26,0.20,0.20),4.5:(0.76,0.26,0.20,0.22),5.0:(0.78,0.26,0.18,0.18),
 7.0:(0.67,0.26,0.22,0.22),7.5:(0.76,0.24,0.24,0.24),8.0:(0.80,0.23,0.20,0.22),8.5:(0.79,0.24,0.21,0.22),9.0:(0.79,0.24,0.21,0.22),9.5:(0.79,0.24,0.21,0.22),
 10.0:(0.76,0.24,0.24,0.24)}
c={"mediaId":862,"level":"A","keyWord":"watching","defaultVoice":"female",
"taps":[
 {"phrase":"to hold a pillow","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to hold a blanket","target":"the woman","voice":"female","keys":keys(woman)},
 {"phrase":"to sit behind the woman","target":"the cat","voice":"female","keys":keys(cat)}],
"stillS":2.0,
"nouns":[{"word":"a window","x":0.58,"y":0.08,"voice":"female"},{"word":"a cat","x":0.86,"y":0.33,"voice":"female"},
 {"word":"a blanket","x":0.78,"y":0.53,"voice":"female"},{"word":"popcorn","x":0.55,"y":0.61,"voice":"female"}],
"question":"What are the man and woman doing?",
"answer":["They","are","watching","TV","with","popcorn."],
"answerVoice":"female",
"notes":"The TV is only a dark edge at the right of the picture, so 'watching TV' rests on their stare toward it. The man and woman sit shoulder to shoulder: their boxes are split along a vertical line between them, so the man's reaching arm / the woman's blanket are partly outside their own box. Cat off 5.5-6.5 (only a sliver behind the woman's head). The woman's blanket has a light cream colour; the man's pillow is rust brown (a second patterned cushion lies beside the woman but nobody holds it)."}
json.dump(c,open("content/862.json","w"),indent=1)
