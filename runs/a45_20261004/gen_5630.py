import json
def K(times, rows):
    return [({"t": t, "off": True} if r is None else {"t": t, "x": r[0], "y": r[1], "w": round(r[2],2), "h": round(r[3],2)}) for t, r in zip(times, rows)]
T8 = [0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
#        woman right edge (=dancers left), woman/dog split y
R = [.64,.62,.61,.62,.64,.64,.61,.61]
S = [.69,.68,.69,.70,.70,.71,.71,.71]
L = [.30,.32,.33,.32,.30,.34,.35,.35]
wom = [(l,.19,r-l,s-.19) for l,r,s in zip(L,R,S)]
dan = [(r,.35,.88-r,.27) for r in R]
DL = [.18,.18,.18,.19,.17,.17,.17,.26]
DR = [.83,.82,.82,.83,.82,.82,.82,.82]
dog = [(l,s,r-l,.92-s) for l,r,s in zip(DL,DR,S)]
d = {"mediaId":5630,"level":"B","keyWord":"be responsible for","defaultVoice":"female","taps":[
 {"phrase":"to balance a tiered cake","target":"the woman in cream","voice":"female","keys":K(T8,wom)},
 {"phrase":"to crouch at her feet","target":"the dog","voice":"female","keys":K(T8,dog)},
 {"phrase":"to dance under the pergola","target":"the women in the back","voice":"female","keys":K(T8,dan)}],
 "stillS":1.2,
 "nouns":[{"word":"a pergola","x":0.62,"y":0.14,"voice":"female"},{"word":"a tiered cake","x":0.66,"y":0.29,"voice":"female"},{"word":"shutters","x":0.13,"y":0.37,"voice":"female"},{"word":"a wicker armchair","x":0.18,"y":0.62,"voice":"female"}],
 "question":"What is the woman in cream carrying?",
 "answer":["She","is","carrying","a","tiered","cake."],
 "answerVoice":"female",
 "notes":"Overlaps split (the dog looks up with its head next to her skirt at 2.7-3.7 s, so part of its head lies in her box): the woman stands over the dog, so her box ends at about y 0.69-0.71 (her lower legs and feet fall into the dog's box); the right half of the cake hangs above the left dancer, so the woman's box ends at x 0.61-0.64 and the cake's right part lies in the dancers' box. The two dancers are one target. The dog crouches in a play bow at her feet the whole clip (sits up a bit at the end). Key phrase 'be responsible for' is abstract, not used."}
json.dump(d, open('content/5630.json','w'), indent=1, ensure_ascii=False)
