import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
dog={1.5:(0.40,0.43,0.18,0.14),2.0:(0.37,0.41,0.25,0.19),2.5:(0.33,0.39,0.36,0.25),3.0:(0.29,0.37,0.45,0.34),3.5:(0.22,0.34,0.60,0.40),
4.0:(0.17,0.30,0.66,0.48),4.5:(0.15,0.30,0.70,0.49),5.0:(0.15,0.29,0.73,0.51),5.5:(0.12,0.29,0.78,0.51),6.0:(0.14,0.29,0.75,0.51),
6.5:(0.14,0.29,0.75,0.52),7.0:(0.12,0.29,0.76,0.52),7.5:(0.12,0.29,0.78,0.52),8.0:(0.12,0.30,0.78,0.52),8.5:(0.12,0.30,0.78,0.52),
9.0:(0.14,0.31,0.76,0.53),9.5:(0.14,0.71,0.80,0.15)}
blind={9.0:(0.12,0.0,0.80,0.24),9.5:(0.14,0.0,0.80,0.71),10.0:(0.10,0.0,0.82,0.85)}
dk=keys(dog)
d={"mediaId":4054,"level":"B","keyWord":"keyboard","defaultVoice":"female",
"taps":[
{"phrase":"to type on a keyboard","target":"the dog","voice":"female","keys":dk},
{"phrase":"to sit upright at a desk","target":"the dog","voice":"female","keys":dk},
{"phrase":"to block the view","target":"the blind","voice":"female","keys":keys(blind)}],
"stillS":6.0,
"nouns":[{"word":"glasses","x":0.68,"y":0.38,"voice":"female"},{"word":"a keyboard","x":0.80,"y":0.53,"voice":"female"},
{"word":"a desk","x":0.78,"y":0.66,"voice":"female"},{"word":"an office chair","x":0.36,"y":0.74,"voice":"female"}],
"question":"What is the dog doing?",
"answer":["The","dog","is","typing","on","a","keyboard."],
"answerVoice":"female",
"notes":"Only one living target (the dog), so two phrases share it; third target is the blind that comes down at 9.0-10.0 s (visible only in the last three frames). Dog is off at 0-1.0 s (too small to see) and at 10.0 s (only a shadow behind the blind); at 9.5 s the dog box is the strip of legs below the blind. Keyboard and desk are small and dark at the right edge of the window; chair pill is on the seat/base."}
json.dump(d,open("content/4054.json","w"),indent=1,ensure_ascii=False)
