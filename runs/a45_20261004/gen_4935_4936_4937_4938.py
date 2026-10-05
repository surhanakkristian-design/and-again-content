import json, sys
T=[round(i*0.5,1) for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=b; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
    return out
def write(mid, doc):
    json.dump(doc, open(f"content/{mid}.json","w"), indent=1, ensure_ascii=False)

def c4935():
    woman={0.0:(.30,.15,.43,.58),0.5:(.28,.14,.50,.72),1.0:(.20,.09,.58,.91),1.5:(.40,.26,.60,.40),
      2.0:(.11,.20,.89,.40),2.5:(.00,.10,.97,.82),3.0:(.06,.11,.82,.86),3.5:(.00,.78,.30,.22),
      4.0:(.65,.70,.30,.30),4.5:(.40,.32,.60,.38),5.0:(0,0,1,1),5.5:(0,0,1,1),6.0:(.05,.15,.95,.48),
      7.5:(0,.15,1,.85),8.0:(0,.12,1,.88),8.5:(0,.08,1,.92),9.0:(0,.06,1,.94)}
    gulls={6.5:(.03,.08,.97,.74),7.0:(0,.05,1,.95)}
    kw=keys(woman); kg=keys(gulls)
    write(4935,{"mediaId":4935,"level":"B","keyWord":"compass","defaultVoice":"female",
     "taps":[
      {"phrase":"to steer the boat","target":"the woman","voice":"female","keys":kw},
      {"phrase":"to peer through binoculars","target":"the woman","voice":"female","keys":kw},
      {"phrase":"to soar in the sky","target":"the seagulls","voice":"female","keys":kg}],
     "stillS":6.0,
     "nouns":[{"word":"a compass","x":0.80,"y":0.64,"voice":"female"},
              {"word":"a lever","x":0.30,"y":0.52,"voice":"female"},
              {"word":"a hand","x":0.24,"y":0.26,"voice":"female"}],
     "question":"What is the woman looking through?",
     "answer":["She","is","peering","through","a","pair","of","binoculars."],
     "answerVoice":"female",
     "notes":"Only one person; woman box covers her hand/arm in close-ups (1.5-2.0, 3.5-4.5, 6.0). Seagulls only at 6.5-7.0. Still 6.0: compass partly cropped at right edge."})
def c4936():
    cook={0.0:(.20,.01,.72,.76),0.5:(.20,.00,.78,.80),1.0:(.18,.28,.80,.70),1.5:(.22,.01,.76,.88),
      2.0:(0,0,1,.62),2.5:(.08,0,.92,.52),3.0:(.13,0,.87,.55),3.5:(.15,0,.83,.75),4.0:(0,0,1,.33),
      4.5:(.08,0,.92,.30),5.0:(.05,0,.95,.30),5.5:(.03,0,.97,.30)}
    for t in (6.0,6.5,7.0,7.5,8.0,8.5,9.0): cook[t]=(0,0,1,1)
    k=keys(cook)
    write(4936,{"mediaId":4936,"level":"A","keyWord":"kitchen","defaultVoice":"female",
     "taps":[
      {"phrase":"to cut green herbs","target":"the cook","voice":"female","keys":k},
      {"phrase":"to taste the sauce","target":"the cook","voice":"female","keys":k},
      {"phrase":"to blow a kiss","target":"the cook","voice":"female","keys":k}],
     "stillS":0.0,
     "nouns":[{"word":"a hat","x":0.57,"y":0.10,"voice":"female"},
              {"word":"pots","x":0.22,"y":0.28,"voice":"female"},
              {"word":"bottles","x":0.12,"y":0.40,"voice":"female"},
              {"word":"a pan","x":0.45,"y":0.56,"voice":"female"}],
     "question":"What is the cook tasting?",
     "answer":["She","is","tasting","the","sauce."],
     "answerVoice":"female",
     "notes":"The cook is the only person; all three phrases on her (pan/fire overlap her body, esp. the big flame at 1.0). Key word 'kitchen' is the whole setting, not a placeable noun. 'to blow a kiss' = hand at mouth at 8.0 (chef's kiss)."})
def c4937():
    man={0.0:(0,0,1,.60),0.5:(0,0,1,.48),1.0:(0,0,1,.50),1.5:(.06,0,.92,.72),2.0:(.18,0,.82,.75),
      2.5:(.20,0,.80,.75),3.0:(.22,.02,.74,.72),3.5:(.12,.04,.88,.96),4.0:(.02,.02,.98,.96),
      4.5:(0,0,.75,.40),5.0:(0,0,.82,.45),5.5:(0,0,.82,.42),6.0:(0,0,.80,.40),6.5:(0,0,.80,.40),
      7.0:(0,.64,.18,.24),7.5:(0,.47,.48,.32),8.0:(0,0,.82,.71),8.5:(0,0,1,.75),9.0:(0,.02,.95,.75)}
    k=keys(man)
    write(4937,{"mediaId":4937,"level":"A","keyWord":"ring","defaultVoice":"male",
     "taps":[
      {"phrase":"to break an egg","target":"the man","voice":"male","keys":k},
      {"phrase":"to put butter on pancakes","target":"the man","voice":"male","keys":k},
      {"phrase":"to ring a bell","target":"the man","voice":"male","keys":k}],
     "stillS":8.5,
     "nouns":[{"word":"a man","x":0.58,"y":0.14,"voice":"male"},
              {"word":"a window","x":0.88,"y":0.30,"voice":"male"},
              {"word":"pancakes","x":0.86,"y":0.54,"voice":"male"},
              {"word":"a bell","x":0.57,"y":0.70,"voice":"male"}],
     "question":"What is the man ringing?",
     "answer":["He","is","ringing","a","bell."],
     "answerVoice":"male",
     "notes":"Only one person; all three phrases on the man. The flying pancake (2.0-4.0) was not used as a target because it lies in front of his body. 7.0: only a bit of his hand at the left edge. Ring moment = 8.0 (hand over bell)."})
def c4938():
    w={0.0:(.33,.08,.35,.58),0.5:(.31,.13,.34,.51),1.0:(.33,.16,.34,.51),1.5:(0,0,1,.55),2.0:(0,0,1,.55),
      3.5:(0,.20,1,.80),4.0:(0,.08,1,.92),4.5:(0,.09,1,.91),5.0:(0,0,1,1),5.5:(0,0,.92,1),
      6.0:(0,.25,1,.75),6.5:(.25,0,.75,1),7.0:(0,.12,1,.88),7.5:(.30,.12,.60,.88),8.0:(.10,.10,.90,.90),
      8.5:(.08,.08,.92,.92),9.0:(.20,.18,.62,.82)}
    c={2.5:(0,.12,1,.52),3.0:(0,.14,1,.52)}
    kw=keys(w); kc=keys(c)
    write(4938,{"mediaId":4938,"level":"A","keyWord":"waitress","defaultVoice":"female",
     "taps":[
      {"phrase":"to carry plates of food","target":"the waitress","voice":"female","keys":kw},
      {"phrase":"to write an order","target":"the waitress","voice":"female","keys":kw},
      {"phrase":"to drink coffee together","target":"the couple","voice":"female","keys":kc}],
     "stillS":5.5,
     "nouns":[{"word":"a waitress","x":0.26,"y":0.15,"voice":"female"},
              {"word":"flowers","x":0.88,"y":0.50,"voice":"female"},
              {"word":"a table","x":0.70,"y":0.74,"voice":"female"}],
     "question":"What is the waitress carrying?",
     "answer":["She","is","carrying","plates","of","food."],
     "answerVoice":"female",
     "notes":"Couple (2.5-3.0) is a two-person group target; a third diner's hand with a cup at the right edge is left out of their box. Pouring hands at 1.5-2.0 assigned to the waitress (striped apron visible behind). Writing hand at 6.0 assumed hers (striped apron at 6.5). The couple at 0.5 may be the same pair but is not certain, so off there."})
{"4935":c4935,"4936":c4936,"4937":c4937,"4938":c4938}[sys.argv[1]]()
