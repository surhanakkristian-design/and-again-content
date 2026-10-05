import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
green=[(0.40,0.18,0.37,0.82)]*8
wall=[(0.77,0.38,0.19,0.30)]*5+[(0.77,0.44,0.19,0.26)]*3
floor=[(0.0,0.67,0.40,0.30)]*6+[(0.0,0.57,0.40,0.40)]*2
c={"mediaId":8015,"level":"B","keyWord":"take ages","defaultVoice":"female",
"taps":[
 {"phrase":"to pose for a mirror selfie","target":"the woman in green","voice":"female","keys":K(green)},
 {"phrase":"to yawn against the wall","target":"the woman by the wall","voice":"female","keys":K(wall)},
 {"phrase":"to sprawl across the carpet","target":"the woman on the floor","voice":"female","keys":K(floor)}],
"stillS":0.2,
"nouns":[{"word":"a bedside lamp","x":0.26,"y":0.40,"voice":"female"},
 {"word":"a bedspread","x":0.20,"y":0.61,"voice":"female"},
 {"word":"a satin dress","x":0.62,"y":0.72,"voice":"female"},
 {"word":"high heels","x":0.84,"y":0.88,"voice":"female"}],
"question":"What is the woman in green doing?",
"answer":["She","is","posing","for","a","mirror","selfie."],
"answerVoice":"female",
"notes":"Whole clip is a mirror reflection. Woman by the wall yawns 0.2-2.2, from 2.7 she is mostly hidden behind the green dress (only head/shoulder peeks out); her box is split from the green woman's at x 0.77, so the green woman's hair edge is cut a little. Floor woman's legs continue behind the green dress at the right (not boxed). The woman asleep on the bed is not a target."}
json.dump(c,open('content/8015.json','w'),indent=1)
