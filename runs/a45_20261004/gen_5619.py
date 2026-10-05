import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows):
    out=[]
    for t,r in zip(T,rows):
        out.append({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]})
    return out
chef=K([(0.03,0.30,0.53,0.70),(0.06,0.30,0.53,0.70),(0.05,0.31,0.56,0.69),(0.06,0.32,0.57,0.68),(0.04,0.30,0.58,0.70),(0.18,0.32,0.44,0.68),(0.28,0.40,0.21,0.48),(0.26,0.40,0.20,0.48)])
man=K([None,None,None,None,None,(0.63,0.62,0.37,0.38),(0.50,0.22,0.50,0.78),(0.47,0.20,0.53,0.80)])
blonde=K([(0.58,0.39,0.30,0.41),(0.62,0.40,0.30,0.40),(0.63,0.40,0.27,0.40),(0.65,0.40,0.28,0.40),(0.64,0.40,0.29,0.38),(0.67,0.40,0.29,0.21),None,None])
c={"mediaId":5619,"level":"B","keyWord":"be in charge of","defaultVoice":"female",
"taps":[{"phrase":"to raise her arm high","target":"the head chef","voice":"female","keys":chef},
{"phrase":"to bring in another dish","target":"the young cook","voice":"male","keys":man},
{"phrase":"to toss a frying pan","target":"the blonde cook","voice":"female","keys":blonde}],
"stillS":1.2,
"nouns":[{"word":"copper pans","x":0.82,"y":0.28,"voice":"female"},{"word":"a pendant lamp","x":0.14,"y":0.24,"voice":"female"},
{"word":"roast chicken","x":0.15,"y":0.65,"voice":"female"},{"word":"a checked floor","x":0.78,"y":0.90,"voice":"female"}],
"question":"What is the head chef doing?",
"answer":["She","is","raising","her","arm","high."],"answerVoice":"female",
"notes":"young cook enters only at 2.7 (arms only); blonde cook hidden behind him at 3.2/3.7; boxes split where cook's arms cross the chef."}
json.dump(c,open('content/5619.json','w'),indent=1)
