import json
T=[i*0.5 for i in range(25)]
def K(rows):
    return [{"t":t,"off":True} if r is None else dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) for t,r in zip(T,rows)]
woman=[(0,.23,.72,.77),(0,.18,.8,.82),(0,.15,.72,.85),(0,.18,.72,.82),(0,.18,.66,.82),(0,.18,.7,.82),
 (0,.18,1,.8),(.13,.25,.83,.74),
 (.13,.37,.67,.40),(.3,.39,.38,.36),(.28,.39,.52,.32),(.28,.40,.48,.29),(.24,.40,.54,.28),(.25,.40,.54,.28),
 (0,.1,.92,.9),(0,.1,.93,.9),(0,.09,.95,.91),(0,.09,.97,.91),(0,.09,.97,.91),(0,.08,.96,.92),
 (0,.1,.96,.9),(0,.11,.97,.89),(0,.11,.96,.89),(0,.1,.96,.9),(0,.1,1,.9)]
mill=[None]*8+[(.36,.23,.35,.14),(.38,.25,.32,.14),(.36,.24,.34,.15),(.39,.25,.31,.15),(.36,.24,.34,.16),(.37,.24,.34,.16)]+[None]*11
d={"mediaId":5106,"level":"B","keyWord":"windmill","defaultVoice":"female",
"taps":[
 {"phrase":"to cycle along a canal","target":"the woman","voice":"female","keys":K(woman)},
 {"phrase":"to bite into a waffle","target":"the woman","voice":"female","keys":K(woman)},
 {"phrase":"to turn its sails","target":"the windmill","voice":"female","keys":K(mill)}],
"stillS":6.0,
"nouns":[{"word":"the sky","x":0.50,"y":0.10,"voice":"female"},
 {"word":"a windmill","x":0.55,"y":0.32,"voice":"female"},
 {"word":"a raincoat","x":0.50,"y":0.51,"voice":"female"},
 {"word":"tulips","x":0.22,"y":0.70,"voice":"female"}],
"question":"What is the woman eating?",
"answer":["She","is","eating","a","sticky","caramel","waffle."],
"answerVoice":"female",
"notes":"Three shots: canal bike ride 0-2.5, tulip field 3.0-6.5, waffle stall 7.0-12.0. Windmill stands directly behind her head in the field shot: windmill box = the band above her shoulders (incl. her head), woman box starts at her shoulders. Windmill off at 3.0-3.5 (hidden behind her head / only sail tips). Waffle is a stroopwafel; called 'a caramel waffle' to stay plain."}
json.dump(d,open("content/5106.json","w"),indent=1)
