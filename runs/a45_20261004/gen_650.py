import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
man={0.0:(0,0.05,0.56,0.9),0.5:(0,0.08,0.61,0.87),1.0:(0,0.08,0.6,0.87),1.5:(0.05,0.25,0.95,0.7),2.0:(0.25,0.2,0.75,0.8),
2.5:(0,0,0.7,0.95),3.5:(0,0,0.42,0.8),4.0:(0,0,0.4,0.62),4.5:(0,0.33,0.74,0.67),5.0:(0,0.36,0.78,0.64),
5.5:(0.58,0.1,0.42,0.75),6.0:(0.6,0.05,0.4,0.75),6.5:(0.55,0.25,0.45,0.6),
8.0:(0,0.1,0.52,0.9),8.5:(0,0.17,0.64,0.83),9.0:(0,0.27,0.66,0.73),9.5:(0,0.29,0.7,0.71),10.0:(0,0.27,0.64,0.73)}
woman={0.0:(0.57,0.15,0.43,0.68),0.5:(0.62,0.15,0.38,0.68),1.0:(0.61,0.27,0.39,0.6),
8.0:(0.6,0.17,0.4,0.43),8.5:(0.66,0.16,0.34,0.45),9.0:(0.68,0.19,0.27,0.3),9.5:(0.71,0.19,0.25,0.3),10.0:(0.65,0.19,0.27,0.28)}
dog={3.0:(0.7,0.25,0.3,0.5),4.5:(0.68,0.02,0.32,0.3),5.0:(0.66,0.02,0.34,0.33),
8.0:(0.72,0.61,0.28,0.39),8.5:(0.66,0.62,0.34,0.38),9.0:(0.67,0.68,0.33,0.32),9.5:(0.71,0.63,0.29,0.37),10.0:(0.65,0.6,0.35,0.4)}
c={"mediaId":650,"level":"B","keyWord":"screw","defaultVoice":"male",
"taps":[{"phrase":"to crawl across the floor","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to wear a long braid","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to peer over the box","target":"the dog","voice":"male","keys":keys(dog)}],
"stillS":5.0,
"nouns":[{"word":"a screw","x":0.5,"y":0.46,"voice":"male"},{"word":"a cardboard box","x":0.25,"y":0.34,"voice":"male"},
{"word":"a golden retriever","x":0.8,"y":0.17,"voice":"male"},{"word":"a thumb","x":0.25,"y":0.75,"voice":"male"}],
"question":"What is the man looking for?","answer":["He","is","looking","for","a","missing","screw."],"answerVoice":"male",
"notes":"The woman does no action that only she does (both hold the chair), so her phrase is a state (braid). 4.5-6.5 s: close-ups of a hand with the screw, boxed as the man (his hand per the description). 7.0-7.5 s: only a sliver of hand / the screwdriver tip -> man off. 9.0-10.0 s: the woman stands behind the seated man, her box covers only head and upper body so it does not take his shoulder. 'a thumb' on the big thumb at the left; the fingers on the right are not labelled."}
json.dump(c,open('content/650.json','w'),ensure_ascii=False,indent=1)
