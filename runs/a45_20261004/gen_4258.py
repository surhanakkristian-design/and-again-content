import json
def K(rows):
    out=[]
    for r in rows:
        if r[1] is None: out.append({"t":r[0],"off":True})
        else: out.append({"t":r[0],"x":r[1],"y":r[2],"w":r[3],"h":r[4]})
    return out
def save(d): json.dump(d,open(f"content/{d['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# ---------- 4258
fawn=[(0.0,.34,.37,.26,.13),(0.5,.34,.37,.26,.13),(1.0,.31,.39,.27,.13),(1.5,.26,.38,.34,.14),(2.0,.27,.35,.33,.17),
(2.5,.30,.29,.34,.24),(3.0,.30,.29,.35,.28),(3.5,.31,.30,.37,.30),(4.0,.33,.31,.37,.30),(4.5,.33,.32,.38,.30),
(5.0,.34,.32,.37,.31),(5.5,.35,.33,.37,.30),(6.0,.35,.31,.39,.32),(6.5,.29,.23,.59,.43),(7.0,.27,.32,.50,.34),
(7.5,.18,.28,.70,.29),(8.0,.33,.42,.46,.23),(8.5,.34,.39,.43,.20),(9.0,.24,.32,.49,.28),(9.5,.24,.17,.48,.43),
(10.0,.26,.21,.59,.38),(10.5,.50,.25,.23,.25),(11.0,.54,.27,.18,.19),(11.5,.51,.28,.18,.16)]
slide=[]; trees=[]
for t,x,y,w,h in fawn:
    b=round(y+h,2)
    if t>=10.5: b=round(max(b,.46),2)
    slide.append((t,0.0,b,1.0,round(1-b,2)))
    top=.30 if t<1.0 else (.27 if t<2.0 else .22)
    top=round(min(top,y),2)
    trees.append((t,0.0,0.0,1.0,top))
save({"mediaId":4258,"level":"B","keyWord":"steel","defaultVoice":"female",
"taps":[{"phrase":"to scramble to its feet","target":"the fawn","voice":"female","keys":K(fawn)},
{"phrase":"to reflect the pale sky","target":"the steel slide","voice":"female","keys":K(slide)},
{"phrase":"to tower over the meadow","target":"the pine trees","voice":"female","keys":K(trees)}],
"stillS":4.5,
"nouns":[{"word":"steel","x":.50,"y":.76,"voice":"female"},{"word":"a fawn","x":.52,"y":.50,"voice":"female"},
{"word":"a meadow","x":.24,"y":.33,"voice":"female"},{"word":"a forest","x":.50,"y":.10,"voice":"female"}],
"question":"What is the fawn doing?","answer":["It","is","lying","on","a","steel","slide."],"answerVoice":"female",
"notes":"Fawn lies inside the slide chute, so the slide box starts at the lower edge of the fawn box (rims beside the fawn are not in the slide box). Trees box is the top band, cut at the fawn's box top when it stands up (9.5-10.0). 'steel' pill sits on the slide surface (no separate 'a slide' noun). The fawn scrambles up at 6.5-9.5."})

# ---------- 4259
sheep=[(t/2,0.0,0.03,1.0,0.97) if t/2<6.5 else (t/2,0.0,0.0,1.0,1.0) for t in range(17)]
save({"mediaId":4259,"level":"A","keyWord":"face","defaultVoice":"male",
"taps":[{"phrase":"to open its mouth","target":"the sheep","voice":"male","keys":K(sheep)},
{"phrase":"to wear an orange scarf","target":"the sheep","voice":"male","keys":K(sheep)},
{"phrase":"to make an angry face","target":"the sheep","voice":"male","keys":K(sheep)}],
"stillS":4.0,
"nouns":[{"word":"a face","x":.48,"y":.50,"voice":"male"},{"word":"a scarf","x":.48,"y":.74,"voice":"male"},
{"word":"the sky","x":.84,"y":.27,"voice":"male"},{"word":"wool","x":.45,"y":.90,"voice":"male"}],
"question":"What is the sheep doing?","answer":["It","is","making","an","angry","face."],"answerVoice":"male",
"notes":"Only one target (the sheep fills the frame), so all three phrases share it. From 6.5 s the close-up shows only the face: box = whole picture. 'wool' is on the body fleece below the scarf; the head tuft is also wool."})

# ---------- 4260
man=[];dog=[];fig=[]
for i in range(19):
    t=i/2
    if t<=3.0 or t in (8.0,8.5):
        man.append((t,0.0,.29,.42,.43)); dog.append((t,.42,.37,.26,.16))
    elif t==3.5:
        man.append((t,0.0,.36,.44,.30)); dog.append((t,.44,.38,.30,.16))
    elif t==9.0:
        man.append((t,0.0,.29,.41,.43)); dog.append((t,.41,.35,.26,.18))
    else:
        man.append((t,0.0,.36,.42,.30)); dog.append((t,.42,.36,.30,.17))
    if 2.5<=t<=5.0: fig.append((t,.48,.05,.23,.31))
    elif t==5.5: fig.append((t,.43,.05,.22,.31))
    else: fig.append((t,None))
save({"mediaId":4260,"level":"B","keyWord":"figure","defaultVoice":"male",
"taps":[{"phrase":"to grin at a tablet","target":"the man","voice":"male","keys":K(man)},
{"phrase":"to rest beside its owner","target":"the dog","voice":"male","keys":K(dog)},
{"phrase":"to lurk in the doorway","target":"the dark figure","voice":"male","keys":K(fig)}],
"stillS":4.5,
"nouns":[{"word":"a figure","x":.60,"y":.27,"voice":"male"},{"word":"a lamp","x":.28,"y":.19,"voice":"male"},
{"word":"a tablet","x":.45,"y":.66,"voice":"male"},{"word":"a blanket","x":.52,"y":.87,"voice":"male"}],
"question":"Who is standing in the doorway?","answer":["A","dark","figure","is","standing","in","the","doorway."],"answerVoice":"male",
"notes":"The dog's head lies on the man's shoulder: boxes split at x 0.42, so the man's box misses his right hand and the right end of the tablet. The figure is only visible 2.5-5.5 s (faint at 2.5, shifted left and fading at 5.5). The man grins at the tablet in 0-3 s and 8-9 s, he sleeps in between."})

# ---------- 4261
d1=[(0.0,.52,.24,.42,.30),(0.5,.58,.22,.36,.32),(1.0,.57,.22,.30,.36),(1.5,.47,.31,.33,.21),(2.0,.38,.29,.25,.15),
(2.5,.31,.23,.18,.18),(3.0,.32,.23,.18,.16),(3.5,.35,.21,.18,.16),(4.0,.40,.13,.20,.14),(4.5,.41,.13,.19,.14),
(5.0,.38,.14,.20,.14),(5.5,.35,.14,.20,.14),(6.0,.30,.13,.22,.15),(6.5,.26,.14,.24,.15),(7.0,.26,.16,.25,.14),
(7.5,.28,.16,.28,.15),(8.0,.31,.17,.29,.14),(8.5,.29,.17,.33,.18),(9.0,.27,.19,.35,.19),(9.5,.25,.26,.44,.16),
(10.0,.20,.25,.53,.35),(10.5,.10,.28,.66,.17),(11.0,.10,.29,.60,.14),(11.5,0.0,.30,.82,.14)]
ball=[(0.0,None),(0.5,.38,.22,.18,.14),(1.0,.38,.23,.18,.14),(1.5,.42,.17,.18,.14),(2.0,.42,.15,.18,.14),
(2.5,.49,.22,.18,.14),(3.0,.50,.23,.18,.14),(3.5,.53,.23,.18,.14),(4.0,.44,.27,.18,.14),(4.5,.41,.27,.18,.14),
(5.0,.40,.28,.18,.14),(5.5,.38,.28,.18,.14),(6.0,.32,.28,.19,.14),(6.5,.31,.29,.20,.14),(7.0,.33,.30,.21,.14),
(7.5,.34,.31,.23,.14),(8.0,.38,.31,.27,.14),(8.5,.33,.35,.31,.14),(9.0,.42,.38,.33,.19),(9.5,.44,.42,.46,.21),
(10.0,.44,.60,.56,.35),(10.5,.20,.45,.78,.47),(11.0,0.0,.43,1.0,.57),(11.5,0.0,.44,1.0,.56)]
d2=[(t/2,None) for t in range(10)]+[(5.0,.59,.20,.21,.14),(5.5,.58,.19,.24,.14),(6.0,.59,.18,.21,.14),(6.5,.62,.17,.19,.14),
(7.0,.62,.17,.19,.14),(7.5,.61,.17,.19,.14),(8.0,.62,.14,.19,.14),(8.5,.63,.12,.19,.14),(9.0,.63,.12,.20,.15),
(9.5,.58,.11,.24,.15),(10.0,.53,.10,.25,.15),(10.5,.48,.10,.34,.18),(11.0,.55,.12,.30,.17),(11.5,.63,.13,.27,.17)]
save({"mediaId":4261,"level":"A","keyWord":"sunny","defaultVoice":"male",
"taps":[{"phrase":"to push a red ball","target":"the dog in front","voice":"male","keys":K(d1)},
{"phrase":"to swim behind its friend","target":"the dog at the back","voice":"male","keys":K(d2)},
{"phrase":"to float on the water","target":"the red ball","voice":"male","keys":K(ball)}],
"stillS":1.0,
"nouns":[{"word":"a dog","x":.72,"y":.42,"voice":"male"},{"word":"a ball","x":.50,"y":.29,"voice":"male"},
{"word":"trees","x":.45,"y":.17,"voice":"male"},{"word":"water","x":.40,"y":.65,"voice":"male"}],
"question":"What are the dogs doing?","answer":["They","are","swimming","on","a","sunny","day."],"answerVoice":"male",
"notes":"Second dog only appears at 5.0 s; the still (1.0 s) shows one dog only, so 'a dog' is unambiguous there. Dog and ball touch from 1.5 s: boxes split along the line between them (from 9.0 s the front dog's box holds mainly its head, the body left of the ball is outside). Ball barely visible at the top edge at 0.0 s: off. Key word 'sunny' is an adjective, used in the answer."})
