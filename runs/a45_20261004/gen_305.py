import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
fly={0.0:(.34,.08,.38,.23),0.5:(.25,.08,.31,.18),1.0:(.36,.12,.40,.22),1.5:(.25,.10,.31,.19),2.0:(.12,.11,.25,.17),
2.5:(.28,.12,.42,.23),3.0:(.24,.30,.46,.27),3.5:(.28,.44,.38,.23),4.0:(.26,.43,.41,.24),4.5:(.26,.43,.40,.22),
5.0:(.28,.44,.38,.23),5.5:(.29,.44,.37,.22),6.0:(.24,.43,.42,.24),6.5:(.26,.24,.28,.17),7.5:(.62,.13,.31,.14),
8.0:(.17,.16,.26,.15),8.5:(.38,.09,.38,.24),9.0:(.07,.17,.40,.17),9.5:(.16,.25,.33,.17),10.0:(.16,.25,.33,.17)}
hand={7.0:(.36,.02,.64,.52),7.5:(.43,.28,.57,.42)}
c={"mediaId":305,"level":"A","keyWord":"fly","defaultVoice":"male",
"taps":[
{"phrase":"to land on the bread","target":"the fly","voice":"male","keys":keys(fly)},
{"phrase":"to fly over the table","target":"the fly","voice":"male","keys":keys(fly)},
{"phrase":"to wave a napkin","target":"the hand","voice":"male","keys":keys(hand)}],
"stillS":5.0,
"nouns":[{"word":"a fly","x":.50,"y":.52,"voice":"male"},{"word":"a jar","x":.17,"y":.41,"voice":"male"},{"word":"tea","x":.55,"y":.30,"voice":"male"},{"word":"bread","x":.24,"y":.71,"voice":"male"}],
"question":"What is the fly doing?",
"answer":["It","is","sitting","on","the","bread."],
"answerVoice":"male",
"notes":"The hand is visible only at 7.0 and 7.5 s (box = hand with the napkin); at 6.5 and 8.0 s only the napkin shows, so OFF. The fly is hidden behind the napkin at 7.0 s (OFF). 'napkin' is the hardest word for level A. The key word 'fly' appears as noun (a fly) and as verb in one phrase."}
json.dump(c,open("content/305.json","w"),indent=1,ensure_ascii=False)
