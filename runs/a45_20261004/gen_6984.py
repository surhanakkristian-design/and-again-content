import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows):
    out=[]
    for t,r in zip(T,rows):
        out.append({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]})
    return out
woman=K([(0.20,0.40,0.58,0.40)]*6+[(0.14,0.40,0.68,0.50),(0.14,0.40,0.74,0.55)])
lman=K([(0.00,0.22,0.47,0.18)]*5+[(0.00,0.17,0.42,0.23),(0.00,0.08,0.40,0.32),(0.00,0.06,0.38,0.34)])
rman=K([(0.51,0.22,0.49,0.18)]*5+[(0.55,0.17,0.45,0.23),(0.60,0.12,0.40,0.28),(0.62,0.12,0.38,0.28)])
d={"mediaId":6984,"level":"B","keyWord":"controller","defaultVoice":"female",
 "taps":[
  {"phrase":"to circle a figure in red","target":"the woman","voice":"female","keys":woman},
  {"phrase":"to massage his neck","target":"the man on the left","voice":"male","keys":lman},
  {"phrase":"to gulp down his coffee","target":"the man on the right","voice":"male","keys":rman}],
 "stillS":1.7,
 "nouns":[{"word":"a calculator","x":0.15,"y":0.86,"voice":"female"},
          {"word":"a takeaway box","x":0.82,"y":0.86,"voice":"female"},
          {"word":"binders","x":0.12,"y":0.68,"voice":"female"},
          {"word":"a desk lamp","x":0.88,"y":0.42,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","circling","a","figure","in","red."],
 "answerVoice":"female",
 "notes":"Key word 'controller' (a finance job) is not labelled as a noun: the woman's job cannot be seen for sure. Woman's box starts at y .40 to stay clear of the men leaning over her (her forehead is cut slightly). The man on the left rubs his neck and the man on the right drinks only at 3.2-3.7 s; the left man also holds a coffee cup but never drinks."}
json.dump(d,open('content/6984.json','w'),indent=1)
