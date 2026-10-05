import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
watch={0.0:(0.30,0.36,0.36,0.46),0.5:(0.22,0.34,0.46,0.50),1.0:(0.20,0.33,0.40,0.46),1.5:(0.24,0.28,0.40,0.34),2.0:(0.36,0.36,0.38,0.28),
 2.5:(0.30,0.37,0.38,0.33),3.0:(0.28,0.30,0.38,0.33),3.5:(0.33,0.30,0.38,0.33),4.0:(0.34,0.30,0.38,0.31),4.5:(0.32,0.40,0.32,0.24),
 5.0:(0.26,0.52,0.30,0.16),5.5:(0.28,0.53,0.30,0.16)}
man={0.0:(0.63,0.12,0.37,0.24),0.5:(0.62,0.12,0.38,0.20),1.0:(0.60,0.13,0.40,0.18),1.5:(0.60,0.12,0.40,0.15),2.0:(0.60,0.10,0.40,0.26),
 2.5:(0.58,0.10,0.42,0.26),3.0:(0.55,0.08,0.45,0.22),3.5:(0.52,0.04,0.48,0.26),4.0:(0.50,0.0,0.50,0.30),4.5:(0.50,0.06,0.50,0.34),
 5.0:(0.38,0.19,0.57,0.33),5.5:(0.36,0.18,0.60,0.35),6.0:(0.24,0.08,0.72,0.84),6.5:(0.50,0.23,0.46,0.67),7.0:(0.44,0.21,0.34,0.60),
 7.5:(0.53,0.21,0.24,0.58),8.0:(0.46,0.14,0.34,0.54),8.5:(0.50,0.27,0.26,0.50)}
cat={0.0:(0.45,0.14,0.18,0.14),0.5:(0.44,0.15,0.18,0.14),1.0:(0.42,0.16,0.18,0.14),1.5:(0.42,0.14,0.18,0.14),2.0:(0.42,0.16,0.18,0.14),
 2.5:(0.40,0.16,0.18,0.14),3.0:(0.37,0.16,0.18,0.14),3.5:(0.33,0.16,0.18,0.14),4.0:(0.31,0.16,0.19,0.14),4.5:(0.32,0.25,0.18,0.14),
 5.0:(0.19,0.36,0.18,0.14),5.5:(0.17,0.37,0.18,0.14),7.0:(0.80,0.38,0.20,0.14),7.5:(0.79,0.35,0.21,0.14),8.5:(0.78,0.40,0.20,0.14),
 9.0:(0.72,0.41,0.24,0.14),9.5:(0.72,0.40,0.24,0.14),10.0:(0.72,0.39,0.24,0.14)}
c={"mediaId":861,"level":"A","keyWord":"watch","defaultVoice":"male",
"taps":[
 {"phrase":"to show the time","target":"the watch","voice":"male","keys":keys(watch)},
 {"phrase":"to look at the watch","target":"the blond man","voice":"male","keys":keys(man)},
 {"phrase":"to sit by the window","target":"the cat","voice":"male","keys":keys(cat)}],
"stillS":5.0,
"nouns":[{"word":"a window","x":0.33,"y":0.15,"voice":"male"},{"word":"a man","x":0.70,"y":0.32,"voice":"male"},
 {"word":"a watch","x":0.42,"y":0.59,"voice":"male"},{"word":"a cup","x":0.86,"y":0.92,"voice":"male"}],
"question":"What is the blond man looking at?",
"answer":["He","is","looking","at","the","watch."],
"answerVoice":"male",
"notes":"The watch wearer (red sweater, dark bob) is mostly a POV arm and of unclear gender, so the watch itself is a target instead. From 0.0 to 3.0 the blond man is only a blurry headless grey torso behind the arm; his box sits on the torso above the arm (he really looks at the watch from about 3.5). The cat is small and blurry early on; boxes at minimum size, squeezed against the man's box. Cat off at 6.0, 6.5, 8.0 (hidden / not identifiable). Watch off from 6.0 (motion blur, then out of view)."}
json.dump(c,open("content/861.json","w"),indent=1)
