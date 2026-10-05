import json
def K(times, rows):
    return [({"t": t, "off": True} if r is None else {"t": t, "x": r[0], "y": r[1], "w": round(r[2],2), "h": round(r[3],2)}) for t, r in zip(times, rows)]
T8 = [0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
SX = [.34,.34,.34,.34,.33,.32,.34,.33]   # man | dog split x
man = [(0,.45,s,.48) for s in SX]
dog = [(.34,.60,.25,.17),(.34,.60,.27,.17),(.34,.61,.27,.17),(.34,.61,.27,.17),(.33,.60,.28,.18),(.32,.59,.30,.20),(.34,.61,.24,.19),(.33,.61,.28,.19)]
wom = [(.51,.19,.48,.40),(.51,.19,.48,.40),(.51,.19,.48,.41),(.51,.18,.48,.42),(.51,.17,.48,.42),(.51,.17,.48,.41),(.52,.17,.47,.43),(.34,.16,.65,.42)]
d = {"mediaId":5632,"level":"B","keyWord":"be supposed to","defaultVoice":"male","taps":[
 {"phrase":"to lounge in a hammock","target":"the man","voice":"male","keys":K(T8,man)},
 {"phrase":"to curl up on his chest","target":"the dog","voice":"male","keys":K(T8,dog)},
 {"phrase":"to frown down at him","target":"the woman","voice":"female","keys":K(T8,wom)}],
 "stillS":0.7,
 "nouns":[{"word":"a fence","x":0.30,"y":0.33,"voice":"male"},{"word":"a paint tin","x":0.46,"y":0.53,"voice":"male"},{"word":"a plant pot","x":0.88,"y":0.79,"voice":"male"},{"word":"a hammock","x":0.20,"y":0.86,"voice":"male"}],
 "question":"Where is the man lounging?",
 "answer":["He","is","lounging","in","a","rope","hammock."],
 "answerVoice":"male",
 "notes":"Heavy overlaps: the dog lies on the man's chest, so the man's box is only his left part (head, shoulders, torso, x 0-0.34) and his legs/knees on the right are outside; the woman's lower legs behind the hammock are outside her box (box ends y about 0.58-0.60, above the dog). At 3.7 s her box widens left to her raised hand (frustrated gesture). The man takes a cap at 3.2 s and pulls it onto his head at 3.7 s (not over his face). Key phrase 'be supposed to' (he should be painting the fence) needs inference, not used."}
json.dump(d, open('content/5632.json','w'), indent=1, ensure_ascii=False)
