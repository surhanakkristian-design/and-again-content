import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,boxes)]
woman=[(0.02,0.48,0.98,0.30),(0.04,0.49,0.96,0.31),(0.02,0.51,0.98,0.30),(0.02,0.50,0.98,0.35),(0.0,0.50,1.0,0.39),(0.0,0.49,0.72,0.43),(0.0,0.49,0.64,0.48),(0.0,0.49,0.65,0.48)]
swim=[(0.18,0.78,0.82,0.20),(0.18,0.80,0.82,0.19),(0.20,0.81,0.80,0.19),None,None,(0.72,0.48,0.21,0.14),(0.64,0.44,0.35,0.18),(0.65,0.47,0.34,0.16)]
ball=[(0.44,0.27,0.27,0.21),(0.47,0.27,0.24,0.22),(0.47,0.28,0.26,0.23),(0.49,0.27,0.26,0.23),(0.52,0.25,0.26,0.25),(0.59,0.25,0.24,0.23),(0.68,0.23,0.22,0.21),(0.71,0.22,0.22,0.25)]
c={"mediaId":8017,"level":"A","keyWord":"take it easy","defaultVoice":"female",
"taps":[
 {"phrase":"to hold a pink drink","target":"the woman in blue","voice":"female","keys":K(woman)},
 {"phrase":"to swim under the water","target":"the man in the pool","voice":"male","keys":K(swim)},
 {"phrase":"to hold a beach ball","target":"the man with the ball","voice":"male","keys":K(ball)}],
"stillS":2.2,
"nouns":[{"word":"the sky","x":0.45,"y":0.07,"voice":"female"},
 {"word":"a ball","x":0.60,"y":0.34,"voice":"female"},
 {"word":"a drink","x":0.68,"y":0.66,"voice":"female"},
 {"word":"a pool","x":0.25,"y":0.90,"voice":"female"}],
"question":"What is the woman in blue holding?",
"answer":["She","is","holding","a","pink","drink."],
"answerVoice":"female",
"notes":"Man in the pool swims underwater 0.2-1.2, only a dark blur under the ring at 1.7-2.2 (off), comes up behind the ring from 2.7. From 2.7 the woman's box is cut at the left edge of the swimmer's box (her legs/ring and the drink on the right are outside at 3.2-3.7); the ball man's legs are cut where the swimmer's head is. Another woman in a bikini and a man at the bar stand in the back but hold neither a drink in a ring nor the ball (the bar man pours juice from a jug)."}
json.dump(c,open('content/8017.json','w'),indent=1)
