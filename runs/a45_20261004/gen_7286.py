import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows):
    out=[]
    for t,r in zip(T,rows):
        if r is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=r; out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(min(w,1-x),2),"h":round(min(h,1-y),2)})
    return out
lect=[(.61,.38,.27,.24),(.66,.38,.25,.24),(.67,.37,.25,.25),(.67,.37,.25,.25),(.66,.36,.27,.26),(.67,.36,.28,.26),(.67,.36,.29,.29),(.69,.35,.31,.29)]
stud=[(.13,.40,.24,.21),(.14,.40,.24,.21),(.17,.39,.22,.21),(.17,.39,.22,.21),(.18,.38,.22,.21),(.18,.38,.23,.21),(.18,.38,.23,.21),(.18,.37,.23,.21)]
clock=[(.24,.14,.18,.14),(.26,.13,.18,.14),(.27,.13,.18,.14),(.27,.13,.18,.14),(.29,.12,.18,.14),(.30,.11,.18,.14),(.30,.11,.18,.14),(.31,.11,.18,.14)]
c={"mediaId":7286,"level":"B","keyWord":"lecturer","defaultVoice":"female",
"taps":[
 {"phrase":"to gesture at the blackboard","target":"the lecturer","voice":"female","keys":K(lect)},
 {"phrase":"to raise her hand","target":"the student in grey","voice":"female","keys":K(stud)},
 {"phrase":"to hang above the door","target":"the clock","voice":"female","keys":K(clock)}],
"stillS":1.7,
"nouns":[{"word":"a blackboard","x":0.68,"y":0.10,"voice":"female"},
 {"word":"a clock","x":0.36,"y":0.20,"voice":"female"},
 {"word":"a lecturer","x":0.80,"y":0.46,"voice":"female"},
 {"word":"a pointer","x":0.76,"y":0.59,"voice":"female"}],
"question":"What is the lecturer watching?",
"answer":["She","is","watching","a","student","raise","her","hand."],
"answerVoice":"female",
"notes":"Single static shot, slight push-in. The lecturer only gestures/points at the blackboard at the very end (3.2-3.7, arm out at 3.7); before that she rests a hand on the bench and watches the student. 'to raise her hand' is simple for B; it is the only clear action of the student in grey. Clock box is the minimum size around a small clock."}
json.dump(c,open('content/7286.json','w'),indent=1)
