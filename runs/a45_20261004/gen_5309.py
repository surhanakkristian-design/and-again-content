import json
def keys(rows):
    out=[]
    for r in rows:
        if r[1] is None: out.append({"t":r[0],"off":True})
        else: out.append({"t":r[0],"x":r[1],"y":r[2],"w":r[3],"h":r[4]})
    return out
w=[(0.0,.74,.27,.26,.55),(0.5,.38,.24,.55,.56),(1.0,.37,.19,.58,.60),(1.5,0,0,1.0,.85),(2.0,0,0,1.0,.80),
(2.5,.03,0,.97,.85),(3.0,.05,.07,.95,.93),(3.5,.05,.09,.95,.91),(4.0,.05,.10,.95,.88),
(4.5,.35,.33,.32,.32),(5.0,.37,.33,.31,.34),(5.5,.39,.33,.32,.34),
(6.0,.28,.11,.62,.89),(6.5,.23,.14,.64,.86),(7.0,.19,.14,.66,.86),(7.5,.21,.15,.66,.85),
(8.0,.21,.29,.74,.71),(8.5,.33,.27,.67,.73),(9.0,.37,.27,.60,.73)]
d={"mediaId":5309,"level":"A","keyWord":"note","defaultVoice":"female",
"taps":[{"phrase":"to look at a small note","target":"the woman","voice":"female","keys":keys(w)},
{"phrase":"to hold a coffee cup","target":"the woman","voice":"female","keys":keys(w)},
{"phrase":"to look around the office","target":"the woman","voice":"female","keys":keys(w)}],
"stillS":2.5,
"nouns":[{"word":"glasses","x":0.58,"y":0.18,"voice":"female"},{"word":"a cup","x":0.20,"y":0.47,"voice":"female"},
{"word":"a note","x":0.46,"y":0.62,"voice":"female"},{"word":"a keyboard","x":0.15,"y":0.73,"voice":"female"}],
"question":"What is the woman looking at?","answer":["She","is","looking","at","a","small","note."],"answerVoice":"female",
"notes":"Only one clear target (the woman); colleagues in the background are many and small, so all three phrases use her. She looks at the note 2.0-4.0, holds the cup 2.0-9.0, looks around 4.0-8.0."}
json.dump(d,open("content/5309.json","w"),indent=1)
