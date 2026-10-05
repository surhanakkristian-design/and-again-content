import json
T=[0.2,0.7,1.2,1.7,2.2,2.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":round(r[0],2),"y":round(r[1],2),"w":round(r[2]-r[0],2),"h":round(r[3]-r[1],2)}) for t,r in zip(T,rows)]
woman=[(0.17,0.49,1.0,0.73),(0.18,0.49,1.0,0.73),(0.17,0.50,1.0,0.76),(0.30,0.31,1.0,0.80),(0.21,0.31,1.0,0.81),(0.19,0.36,1.0,0.82)]
man=[None,None,None,None,(0.62,0.0,1.0,0.21),(0.56,0.0,1.0,0.28)]
lamp=[(0.40,0.0,0.68,0.14),(0.31,0.0,0.57,0.14),(0.21,0.04,0.45,0.20),(0.16,0.11,0.38,0.27),(0.12,0.16,0.34,0.31),(0.12,0.21,0.38,0.35)]
c={"mediaId":7444,"level":"A","keyWord":"pop","defaultVoice":"female",
 "taps":[{"phrase":"to lie under a motorbike","target":"the woman","voice":"female","keys":K(woman)},
         {"phrase":"to look down at her","target":"the old man","voice":"male","keys":K(man)},
         {"phrase":"to shine brightly","target":"the lamp","voice":"female","keys":K(lamp)}],
 "stillS":2.2,
 "nouns":[{"word":"a lamp","x":0.23,"y":0.27,"voice":"female"},{"word":"tools","x":0.84,"y":0.26,"voice":"female"},
          {"word":"a motorbike","x":0.14,"y":0.42,"voice":"female"},{"word":"a dog","x":0.85,"y":0.57,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","lying","under","a","motorbike."],"answerVoice":"female",
 "notes":"Key word 'pop' is not a visible noun (not used). The old man is only in the last two frames (top right). Woman lies under the bike 0.2-1.2 and sits up 1.7-2.7; at 2.2-2.7 her box is cut at the top where the lamp box ends. The dog lying on the rug (right) is not a target, but is the 'a dog' noun at 2.2. The thing in her hand looks like a sweet wrapper at 0.2-1.2 and a small metal part later, so it is not named."}
json.dump(c,open('content/7444.json','w'),indent=1)
