import json
T=[i*0.5 for i in range(25)]
def seg(t):
    if t<=3.0: return ([0,0.18,1,0.48],[0.15,0.66,0.40,0.34])
    if t<=6.5: return ([0.27,0.20,0.73,0.72],[0,0.08,0.27,0.80])
    if t<=10.0: return ([0,0.22,1,0.52],[0.08,0.74,0.70,0.26])
    if t==10.5: return ([0.07,0.17,0.86,0.39],[0.38,0.56,0.62,0.44])
    if t<=11.5: return ([0.07,0.20,0.86,0.43],[0.35,0.63,0.65,0.37])
    return ([0.05,0.18,0.90,0.40],[0.33,0.58,0.67,0.42])
def keys(i): return [dict(t=t,x=seg(t)[i][0],y=seg(t)[i][1],w=seg(t)[i][2],h=seg(t)[i][3]) for t in T]
c={"mediaId":4267,"level":"B","keyWord":"neat","defaultVoice":"male","taps":[
 {"phrase":"to pant with its tongue out","target":"the dog","voice":"male","keys":keys(0)},
 {"phrase":"to squeeze its eyes shut","target":"the dog","voice":"male","keys":keys(0)},
 {"phrase":"to cup the dog's chin","target":"the hands","voice":"male","keys":keys(1)}],
 "stillS":4.0,
 "nouns":[{"word":"scissors","x":0.22,"y":0.72,"voice":"male"},{"word":"a tongue","x":0.80,"y":0.50,"voice":"male"},{"word":"a lawn","x":0.62,"y":0.20,"voice":"male"},{"word":"a table","x":0.68,"y":0.93,"voice":"male"}],
 "question":"What is the dog doing?",
 "answer":["It","is","panting","with","its","tongue","out."],"answerVoice":"male",
 "notes":"Only the groomer's hands and arms are ever visible (gender not identifiable), so defaultVoice follows evenId=false -> male. Target 'the hands' = the groomer's hands/arms; they overlap the dog in every shot, so boxes are split along a line (0-3 s: the hands box holds the forearm below the dog's head, the hand on the cheek itself lies in the dog box). The hands cup the cheek at 0-3 s and the chin from 7 s. Key word 'neat' (adjective) is not in the answer."}
json.dump(c,open('content/4267.json','w'),indent=1,ensure_ascii=False)
