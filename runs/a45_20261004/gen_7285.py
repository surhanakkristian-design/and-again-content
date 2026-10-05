import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows):
    out=[]
    for t,r in zip(T,rows):
        if r is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=r; out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(min(w,1-x),2),"h":round(min(h,1-y),2)})
    return out
chef=[(.33,.16,.61,.26),(.34,.15,.61,.27),(.32,.15,.63,.27),(.31,.13,.67,.29),(.30,.11,.66,.31),(.31,.10,.69,.32),(.33,.09,.65,.33),(.42,.09,.57,.33)]
woman=[(.56,.43,.22,.26),(.57,.43,.23,.26),(.56,.43,.22,.26),(.57,.43,.23,.26),(.56,.43,.23,.26),(.57,.43,.25,.26),(.58,.43,.23,.26),(.57,.43,.25,.26)]
old=[(.0,.44,.24,.33),(.0,.45,.24,.33),(.0,.45,.24,.33),(.0,.45,.23,.33),(.0,.44,.22,.33),(.0,.43,.20,.34),(.0,.43,.19,.34),(.0,.43,.19,.34)]
c={"mediaId":7285,"level":"B","keyWord":"layer","defaultVoice":"male",
"taps":[
 {"phrase":"to tip a heavy pot","target":"the chef","voice":"male","keys":K(chef)},
 {"phrase":"to shield her eyes","target":"the woman in the blouse","voice":"female","keys":K(woman)},
 {"phrase":"to lean over the rope","target":"the old man","voice":"male","keys":K(old)}],
"stillS":1.2,
"nouns":[{"word":"a marquee","x":0.75,"y":0.10,"voice":"male"},
 {"word":"bunting","x":0.18,"y":0.42,"voice":"male"},
 {"word":"a stepladder","x":0.77,"y":0.60,"voice":"male"},
 {"word":"a trifle","x":0.40,"y":0.82,"voice":"male"}],
"question":"What is the chef doing?",
"answer":["He","is","pouring","cream","over","the","trifle."],
"answerVoice":"male",
"notes":"Single shot. Chef box cut at y~0.42 (his legs on the ladder are behind/next to the woman in the blouse, so the box holds head, arms and apron only). Woman shields her eyes 0.2-2.2, then lowers her hands and laughs (2.7-3.7). Old man leans over the rope 0.2-2.2, stands up laughing at the end. Ladder man at the right edge not used (overlaps the chef's legs)."}
json.dump(c,open('content/7285.json','w'),indent=1)
