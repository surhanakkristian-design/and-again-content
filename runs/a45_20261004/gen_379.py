import json
def K(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def T(n,step=0.5): return [round(i*step,1) for i in range(n)]
def save(o):
    json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# ---------- 379
t=T(20)
w={0.0:(0,.02,1,.98),0.5:(0,.05,1,.95),1.0:(0,.07,1,.93),1.5:(.08,.06,.92,.94),2.0:(.08,.04,.92,.96),
   2.5:(.10,.04,.90,.96),3.0:(.08,.06,.92,.94),3.5:(.08,.07,.92,.93),4.0:(0,.05,1,.95),4.5:(0,.05,1,.95),
   5.0:(.05,.07,.95,.93),5.5:(.05,.07,.95,.93),6.0:(0,.04,1,.96),6.5:(0,.04,1,.96),7.0:(0,.02,1,.98),
   7.5:(0,0,1,1),8.0:(0,0,1,1),8.5:(0,0,1,1),9.0:(0,.07,1,.93),9.5:(0,.07,1,.93)}
k=K(t,w)
save({"mediaId":379,"level":"B","keyWord":"vlog","defaultVoice":"female",
 "taps":[{"phrase":"to wave at the camera","target":"the woman","voice":"female","keys":k},
         {"phrase":"to tuck her hair back","target":"the woman","voice":"female","keys":k},
         {"phrase":"to record a vlog","target":"the woman","voice":"female","keys":k}],
 "stillS":2.0,
 "nouns":[{"word":"curtains","x":0.17,"y":0.14,"voice":"female"},
          {"word":"figurines","x":0.17,"y":0.39,"voice":"female"},
          {"word":"freckles","x":0.62,"y":0.34,"voice":"female"},
          {"word":"a laptop","x":0.12,"y":0.58,"voice":"female"}],
 "question":"What is the young woman doing?",
 "answer":["She","is","recording","a","vlog","in","her","bedroom."],
 "answerVoice":"female",
 "notes":"Only one clear target (the woman fills the frame), so all three phrases use her. 'to record a vlog' rests on the selfie framing (arm stretched to the camera). Laptop is small and dark at the left edge; figurines are two small toys on the book pile."})

# ---------- 380
t=T(40)
w={}
for x in (0.0,0.5): w[x]=(.18,.18,.70,.52)
for x in (1.0,1.5,2.0): w[x]=(.18,.20,.70,.50)
w.update({2.5:(.28,0,.72,.75),3.0:(.82,.05,.18,.60),3.5:(.47,.36,.28,.62),4.0:(.49,.35,.28,.58),4.5:(.46,.35,.29,.58),
 5.0:(.49,.36,.28,.62),5.5:(0,0,1,1),6.0:(.30,.05,.60,.95),6.5:(.33,.21,.38,.79),7.0:(.38,.28,.26,.68),
 7.5:(0,.10,1,.90),8.0:(0,.05,1,.95),8.5:(0,.02,1,.98),9.0:(0,.07,1,.93),9.5:(0,.07,1,.93),
 10.0:(.22,.30,.60,.70),10.5:(.22,.30,.60,.70),11.0:(.22,.31,.60,.69),11.5:(.22,.28,.60,.72),
 12.0:(.22,.27,.60,.73),12.5:(.22,.27,.60,.73),13.0:(.22,.27,.60,.73),
 13.5:(.39,.42,.26,.50),14.0:(.41,.40,.29,.60),14.5:(.38,.38,.32,.62),15.0:(.38,.37,.32,.63),15.5:(.39,.37,.33,.63),
 16.0:(.39,.37,.32,.63),16.5:(.42,.84,.28,.16),17.0:(.22,0,.44,.67),17.5:(.27,0,.62,.75),18.0:(.60,.05,.40,.70),
 18.5:(.40,.46,.32,.54),19.0:(.33,.45,.42,.55),19.5:(.08,.33,.92,.67)})
cup={x:(.30,.71,.55,.29) for x in (0.0,0.5,1.0,1.5,2.0)}
umb={16.5:(.20,.37,.62,.46),18.5:(.25,.33,.58,.13),19.0:(.03,.27,.92,.18),19.5:(0,0,1,.33)}
save({"mediaId":380,"level":"B","keyWord":"journey","defaultVoice":"female",
 "taps":[{"phrase":"to pass through a turnstile","target":"the woman","voice":"female","keys":K(t,w)},
         {"phrase":"to stand in the foreground","target":"the paper cup","voice":"female","keys":K(t,cup)},
         {"phrase":"to keep the rain off","target":"the checked umbrella","voice":"female","keys":K(t,umb)}],
 "stillS":10.0,
 "nouns":[{"word":"a backpack","x":0.15,"y":0.76,"voice":"female"},
          {"word":"glasses","x":0.50,"y":0.40,"voice":"female"},
          {"word":"a smartphone","x":0.55,"y":0.91,"voice":"female"},
          {"word":"a window","x":0.50,"y":0.14,"voice":"female"}],
 "question":"What is the woman passing through?",
 "answer":["She","is","passing","through","a","subway","turnstile."],
 "answerVoice":"female",
 "notes":"Frames cover only 0-19.5 s of the 30 s clip. Woman: at 2.5, 3.0, 17.0-18.0 only her legs/shoes are shown, at 5.5 a close-up of her hand at the pocket (box = whole frame). Umbrella: boxed only where it is open (16.5, 18.5-19.5); at 14.0-16.0 it is a folded dark bundle in her hands, not recognisable, left off. At 17.5 a blurred second umbrella of a passer-by is cut off top left. Where umbrella and woman overlap the boxes are split along the canopy edge. Key word 'journey' is abstract, so it is not a noun slot; the question uses the turnstile phrase."})

# ---------- 381
t=T(13)
m={0.0:(0,.27,.45,.68),0.5:(.05,.17,.54,.83),1.0:(0,.17,.62,.83),1.5:(0,.10,.81,.90),2.0:(0,.12,.77,.88),
   2.5:(0,.11,.79,.89),3.0:(0,.12,.78,.88),3.5:(0,.12,.79,.88),4.0:(0,.13,.77,.87),4.5:(0,.13,.79,.87),
   5.0:(0,.12,.78,.88),5.5:(0,.12,.79,.88),6.0:(0,.15,.79,.85)}
b={0.5:(.60,.33,.25,.19),1.0:(.63,.38,.28,.21),1.5:(.82,.36,.18,.22),2.0:(.78,.37,.22,.21),2.5:(.80,.37,.20,.21),
   3.0:(.80,.37,.20,.21),3.5:(.80,.37,.20,.21),4.0:(.78,.37,.22,.21),4.5:(.80,.37,.20,.21),5.0:(.80,.37,.20,.21),
   5.5:(.80,.37,.20,.21),6.0:(.81,.37,.19,.21)}
km=K(t,m)
save({"mediaId":381,"level":"A","keyWord":"scare","defaultVoice":"male",
 "taps":[{"phrase":"to hold a green grape","target":"the man","voice":"male","keys":km},
         {"phrase":"to look very scared","target":"the man","voice":"male","keys":km},
         {"phrase":"to show many photos","target":"the photo board","voice":"male","keys":K(t,b)}],
 "stillS":2.0,
 "nouns":[{"word":"a man","x":0.30,"y":0.60,"voice":"male"},
          {"word":"a grape","x":0.72,"y":0.74,"voice":"male"},
          {"word":"photos","x":0.88,"y":0.47,"voice":"male"},
          {"word":"a sink","x":0.84,"y":0.91,"voice":"male"}],
 "question":"What is the man holding?",
 "answer":["The","scared","man","is","holding","a","grape."],
 "answerVoice":"male",
 "notes":"The person who scares him is never in the picture, so the verb 'scare' appears as 'scared'. Man box is cut on the right where the photo board is close (his grape hand is partly outside at 1.0-2.5). 'a man' and 'a grape' are on the same person but well apart (chest vs. fingers)."})

# ---------- 382
t=T(21)
w={0.0:(0,.34,.75,.66),0.5:(0,.35,1,.65),1.0:(0,.37,.92,.63),1.5:(0,.39,.64,.61)}
p={2.0:(0,.71,1,.29),2.5:(0,.69,1,.31),3.0:(0,.80,1,.20),3.5:(0,.78,1,.22),4.0:(0,.66,1,.34),4.5:(0,.65,1,.35),5.0:(0,.79,1,.21)}
for i in range(11,21): p[round(i*0.5,1)]=(.40,.14,.19,.15)
kw=K(t,w)
save({"mediaId":382,"level":"A","keyWord":"high","defaultVoice":"female",
 "taps":[{"phrase":"to clean a window","target":"the woman","voice":"female","keys":kw},
         {"phrase":"to hold a yellow tool","target":"the woman","voice":"female","keys":kw},
         {"phrase":"to hang very high","target":"the platform","voice":"female","keys":K(t,p)}],
 "stillS":0.5,
 "nouns":[{"word":"a helmet","x":0.27,"y":0.44,"voice":"female"},
          {"word":"the sky","x":0.72,"y":0.20,"voice":"female"},
          {"word":"the city","x":0.72,"y":0.80,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","cleaning","a","high","window."],
 "answerVoice":"female",
 "notes":"Platform: boxed as rail + floor in the look-down shot (2.0-5.0) and as the small hanging basket from 5.5; in 0-1.5 only a piece of its railing shows, left off. The woman is not identifiable on the far platform (two tiny silhouettes), so she is off from 2.0. A second worker in blue stands half hidden at the left edge in 0-1.5 (inside the woman's box, no phrase on him); his helmet is a second, smaller helmet at the far left. The shoes in 2.0-5.0 belong to the camera person."})
