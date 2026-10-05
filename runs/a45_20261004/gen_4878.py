import json
T=[round(i*0.5,1) for i in range(19)]
def keys(d):
    return [dict(t=t,**dict(zip('xywh',d[t]))) if t in d else {'t':t,'off':True} for t in T]
man={0.5:(.36,.37,.36,.30),1.0:(.24,.32,.70,.20),1.5:(.34,.35,.48,.30),2.0:(.30,.40,.42,.30),2.5:(.48,.42,.35,.28),
 3.0:(.36,.37,.20,.16),3.5:(.36,.36,.25,.17)}
pair={4.0:(.11,.35,.88,.27),4.5:(.10,.37,.87,.36),5.0:(.05,.45,.80,.30)}
crowd={6.5:(.07,.32,.92,.20),7.0:(.04,.30,.94,.20),7.5:(0,.24,1,.40),8.0:(0,.17,1,.37),8.5:(0,.14,1,.36),9.0:(0,.10,1,.35)}
c={"mediaId":4878,"level":"B","keyWord":"pier","defaultVoice":"female",
"taps":[
 {"phrase":"to perform a solo dive","target":"the man in dark shorts","voice":"male","keys":keys(man)},
 {"phrase":"to dive side by side","target":"the two divers","voice":"male","keys":keys(pair)},
 {"phrase":"to leap off in unison","target":"the crowd","voice":"female","keys":keys(crowd)}],
"stillS":7.0,
"nouns":[{"word":"the sky","x":0.50,"y":0.12,"voice":"female"},
 {"word":"teenagers","x":0.50,"y":0.38,"voice":"female"},
 {"word":"a pier","x":0.50,"y":0.50,"voice":"female"},
 {"word":"water","x":0.50,"y":0.82,"voice":"female"}],
"question":"What are the teenagers doing?",
"answer":["They","are","leaping","off","the","pier."],
"answerVoice":"female",
"notes":"Shots: 0.0 woman cannonball (not used, one frame only), 0.5-3.5 first man dives alone and surfaces, 4.0-5.0 two men dive side by side, 6.5-9.0 big crowd jumps off a long pier. Divers are hidden by foam at 5.5 s (off). 'solo dive' chosen because every shot shows head-first diving; only the first man dives alone. Mixed group, evenId true -> default female."}
json.dump(c,open('content/4878.json','w'),indent=1)
