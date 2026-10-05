import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows):
    return [{"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]} for t,r in zip(T,rows)]
woman=K([(0.19,0.18,0.42,0.62),(0.17,0.27,0.46,0.53),(0.14,0.27,0.44,0.57),(0.11,0.17,0.42,0.68),
         (0.09,0.16,0.48,0.68),(0.08,0.11,0.40,0.73),(0.00,0.09,0.47,0.79),(0.00,0.09,0.44,0.79)])
man=K([(0.82,0.27,0.18,0.45),(0.82,0.27,0.18,0.45),(0.82,0.27,0.18,0.47),(0.82,0.28,0.18,0.44),
       (0.82,0.27,0.18,0.45),(0.82,0.26,0.18,0.46),(0.80,0.26,0.20,0.46),(0.80,0.26,0.20,0.46)])
d={"mediaId":6987,"level":"B","keyWord":"cooper","defaultVoice":"female",
 "taps":[
  {"phrase":"to swing a heavy hammer","target":"the young woman","voice":"female","keys":woman},
  {"phrase":"to wipe her brow","target":"the young woman","voice":"female","keys":woman},
  {"phrase":"to watch with folded arms","target":"the old man","voice":"male","keys":man}],
 "stillS":2.7,
 "nouns":[{"word":"flames","x":0.66,"y":0.30,"voice":"female"},
          {"word":"a barrel","x":0.66,"y":0.76,"voice":"female"},
          {"word":"a brick wall","x":0.18,"y":0.08,"voice":"female"},
          {"word":"wood shavings","x":0.25,"y":0.91,"voice":"female"}],
 "question":"What is the young woman doing?",
 "answer":["She","is","swinging","a","heavy","hammer."],
 "answerVoice":"female",
 "notes":"Key word 'cooper' (barrel maker) is a job, not labelled as a noun. The old man folds his arms only at 3.2-3.7 s (earlier his hands hang down). 'a barrel' sits on the burning barrel in front; other barrels stand in the background. She wipes her brow with her forearm at 3.7 s (hand to head already at 3.2 s)."}
json.dump(d,open('content/6987.json','w'),indent=1)
