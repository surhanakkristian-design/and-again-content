import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows):
    out=[]
    for t,r in zip(T,rows):
        if r is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=r; out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(min(w,1-x),2),"h":round(min(h,1-y),2)})
    return out
woman=[(.0,.33,.77,.66),(.0,.32,.67,.67),(.0,.32,.61,.68),(.0,.32,.66,.68),(.0,.31,.60,.69),(.0,.30,.80,.70),(.0,.30,.60,.70),(.0,.27,.40,.73)]
man=[(.78,.22,.22,.78),(.78,.20,.22,.80),(.78,.19,.22,.81),(.77,.18,.23,.82),(.68,.18,.32,.82),(.81,.14,.19,.86),(.84,.17,.16,.83),(.78,.13,.22,.87)]
c={"mediaId":7287,"level":"B","keyWord":"left","defaultVoice":"female",
"taps":[
 {"phrase":"to throw a straight left","target":"the woman","voice":"female","keys":K(woman)},
 {"phrase":"to grin behind her gloves","target":"the woman","voice":"female","keys":K(woman)},
 {"phrase":"to wear protective headgear","target":"the man in headgear","voice":"male","keys":K(man)}],
"stillS":1.2,
"nouns":[{"word":"fairy lights","x":0.25,"y":0.15,"voice":"female"},
 {"word":"headgear","x":0.88,"y":0.29,"voice":"female"},
 {"word":"a boxing glove","x":0.47,"y":0.51,"voice":"female"},
 {"word":"shorts","x":0.22,"y":0.72,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","throwing","a","straight","left."],
"answerVoice":"female",
"notes":"Single shot. She punches at 0.2 and 2.7 (glove reaches the man's arm at 2.7: boxes split at x 0.80/0.81), grins at 3.2-3.7. Only her left hand wears a gold glove, the right hand is wrapped in white. The man is only partly visible at the right edge (narrow box at 3.2); 'headgear' is a state phrase because his only other action (guard up) is shared with her."}
json.dump(c,open('content/7287.json','w'),indent=1)
