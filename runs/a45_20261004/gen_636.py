import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
woman={0.0:(0.3,0,0.7,0.5),0.5:(0.25,0,0.75,0.65),1.0:(0.12,0,0.88,0.76),1.5:(0.08,0,0.92,0.75),2.0:(0.07,0,0.93,0.46),
2.5:(0.3,0,0.7,0.45),3.0:(0.07,0,0.93,0.66),3.5:(0.08,0,0.92,0.6),4.0:(0.1,0,0.9,0.55),4.5:(0.1,0,0.9,0.62),
5.0:(0.42,0,0.58,0.76),5.5:(0.47,0,0.53,0.7),6.0:(0.47,0,0.53,0.62),6.5:(0.08,0,0.92,0.74),7.0:(0.05,0,0.95,0.86),
7.5:(0.03,0,0.97,0.9),8.0:(0.46,0,0.54,0.8),8.5:(0.4,0.03,0.6,0.87),9.0:(0.39,0.12,0.61,0.88),9.5:(0.38,0.1,0.62,0.9),
10.0:(0.32,0.12,0.68,0.75)}
duck={8.0:(0.2,0.3,0.25,0.22),8.5:(0.18,0.4,0.21,0.22),9.0:(0.18,0.43,0.2,0.22),9.5:(0.19,0.44,0.19,0.22)}
c={"mediaId":636,"level":"A","keyWord":"sandwich","defaultVoice":"female",
"taps":[{"phrase":"to make a sandwich","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to cut the sandwich","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to stand behind the basket","target":"the duck","voice":"female","keys":keys(duck)}],
"stillS":9.0,
"nouns":[{"word":"trees","x":0.22,"y":0.2,"voice":"female"},{"word":"a duck","x":0.3,"y":0.54,"voice":"female"},
{"word":"a basket","x":0.13,"y":0.7,"voice":"female"},{"word":"a sandwich","x":0.16,"y":0.88,"voice":"female"}],
"question":"What is the woman making?","answer":["She","is","making","a","sandwich."],"answerVoice":"female",
"notes":"Until 7.5 s only the woman's hands, arms and dress are in the picture; the box holds those. Two phrases share the woman (the duck is the only other target; a bearded man appears only at 9.5-10.0 s at the right edge and is no target, he overlaps the woman's box there). Duck: visible 8.0-9.5 s, at 10.0 s hidden behind a hand -> off. 'a sandwich' pill sits on the half on the board; the woman holds the other half."}
json.dump(c,open('content/636.json','w'),ensure_ascii=False,indent=1)
