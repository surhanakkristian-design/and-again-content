import json
def keys(times,d,size=None):
    out=[]
    for t in times:
        if t in d:
            v=d[t]
            if size and len(v)==2: v=(v[0],v[1],size[0],size[1])
            x,y,w,h=v; out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(w,2),"h":round(h,2)})
        else: out.append({"t":t,"off":True})
    return out
def T(n): return [i*0.5 for i in range(n)]
def save(c): json.dump(c,open("content/%d.json"%c["mediaId"],"w"),indent=1)

# ---------- 4186
t=T(24)
dog={0.0:(.15,.31,.42,.39),0.5:(.04,.32,.64,.47),1.0:(0,.31,.56,.48),1.5:(0,.31,.44,.39),2.0:(0,.24,.41,.46),2.5:(0,.24,.41,.46),
 3.0:(0,.24,.34,.46),3.5:(0,.24,.34,.46),4.0:(0,.24,.37,.46),4.5:(0,.26,.38,.45),5.0:(0,.33,.56,.25),5.5:(.36,.32,.28,.18),
 6.0:(.48,.32,.28,.14),6.5:(.49,.32,.45,.14),7.0:(.38,.31,.36,.16),7.5:(.24,.31,.32,.18),8.0:(.13,.24,.30,.30),8.5:(.06,.32,.47,.38),
 9.0:(0,.32,.66,.48),9.5:(0,.32,.59,.48),10.0:(0,.25,.41,.45),10.5:(0,.24,.41,.46),11.0:(0,.24,.40,.46),11.5:(0,.26,.41,.45)}
man={}
for x in t: man[x]=(.41,.17,.18,.14)
for x in (2.0,2.5,3.0,3.5,4.0,10.0,10.5,11.0,11.5): man[x]=(.41,.17,.18,.16)
man[4.5]=(.43,.17,.18,.16); man[5.0]=(.44,.18,.18,.15); man[5.5]=(.45,.17,.18,.15); man[6.0]=(.43,.17,.18,.15)
man[6.5]=(.44,.17,.18,.15); man[7.0]=(.44,.16,.18,.15); man[7.5]=(.44,.16,.18,.15); man[8.0]=(.43,.17,.18,.15)
save({"mediaId":4186,"level":"A","keyWord":"return","defaultVoice":"female",
"taps":[
 {"phrase":"to run after the ball","target":"the dog","voice":"female","keys":keys(t,dog)},
 {"phrase":"to bring the ball back","target":"the dog","voice":"female","keys":keys(t,dog)},
 {"phrase":"to hit a tennis ball","target":"the man","voice":"male","keys":keys(t,man)}],
"stillS":2.0,
"nouns":[{"word":"trees","x":0.50,"y":0.08,"voice":"female"},{"word":"a net","x":0.76,"y":0.27,"voice":"female"},
 {"word":"a dog","x":0.20,"y":0.45,"voice":"female"},{"word":"a machine","x":0.50,"y":0.68,"voice":"female"}],
"question":"What is the dog doing?",
"answer":["It","is","returning","the","ball","to","the","machine."],
"answerVoice":"female",
"notes":"The man is a very small figure behind the net; he swings his racket at the ball at 3.5-5.0 s (hit visible but tiny). His box is the minimum size and ends at y 0.31-0.33 so that it never overlaps the dog; where the dog stands in front of the net the top of its tail is cut off by that line. 'to return the ball' was avoided as a phrase because in tennis the man also returns balls; the key word is in the answer instead. The dog drops the ball into the machine at 0.5 and 9.0."})

# ---------- 4187
t=T(21)
hand={0.0:(.10,.52,.70,.48),0.5:(.10,.53,.72,.47),1.0:(.12,.54,.70,.46),1.5:(.14,.63,.70,.37),2.0:(.10,.61,.70,.39),
 2.5:(.26,.57,.70,.43),3.0:(.20,.58,.70,.42),3.5:(.20,.58,.72,.42),4.0:(.16,.56,.72,.44),4.5:(.14,.55,.72,.45),
 5.0:(.20,.54,.72,.46),5.5:(.18,.54,.72,.46),6.0:(.18,.53,.72,.47),6.5:(.14,.53,.72,.47),7.0:(.30,.53,.70,.47),
 7.5:(.26,.53,.72,.47),8.0:(.26,.53,.72,.47),8.5:(.28,.53,.72,.47),9.0:(.28,.54,.70,.46),9.5:(.30,.55,.70,.45),10.0:(.30,.55,.70,.45)}
grey={0.0:(.26,.19,.31,.33),0.5:(.26,.18,.32,.34),1.0:(.26,.18,.32,.35),1.5:(0,.34,.56,.28),2.0:(0,.29,.55,.31),
 2.5:(0,.32,.35,.24),3.0:(0,.33,.31,.24),3.5:(0,.33,.33,.24),4.0:(0,.33,.24,.22),4.5:(0,.33,.18,.14)}
green={2.5:(.82,.32,.18,.20),3.0:(.82,.31,.18,.20),3.5:(.82,.32,.18,.20),4.0:(.82,.30,.18,.20),4.5:(.80,.24,.20,.28),
 5.0:(.64,.25,.26,.28),5.5:(.64,.24,.27,.29),6.0:(.63,.23,.28,.28),6.5:(.58,.22,.29,.28),7.0:(.39,.23,.26,.29),
 7.5:(.37,.22,.27,.29),8.0:(.39,.22,.26,.29),8.5:(.39,.22,.27,.29),9.0:(.34,.32,.33,.18),9.5:(.38,.33,.37,.18),10.0:(.40,.33,.37,.18)}
save({"mediaId":4187,"level":"A","keyWord":"dead","defaultVoice":"male",
"taps":[
 {"phrase":"to hold a toy gun","target":"the hand","voice":"male","keys":keys(t,hand)},
 {"phrase":"to lie on its back","target":"the grey parrot","voice":"male","keys":keys(t,grey)},
 {"phrase":"to fall over last","target":"the green parrot","voice":"male","keys":keys(t,green)}],
"stillS":0.0,
"nouns":[{"word":"curtains","x":0.25,"y":0.10,"voice":"male"},{"word":"parrots","x":0.60,"y":0.35,"voice":"male"},
 {"word":"a sofa","x":0.78,"y":0.62,"voice":"male"},{"word":"a hand","x":0.48,"y":0.90,"voice":"male"}],
"question":"What are the parrots doing?",
"answer":["They","are","playing","dead","on","the","sofa."],
"answerVoice":"male",
"notes":"All four parrots fall over, so the parrot phrases use what only one bird does: the grey one lies on its back with its feet in the air (2.0-4.5; the white and the macaw lie on their side/front), the green one is the last to fall (9.0). The grey parrot leaves the frame after 4.5 (camera pans right); at 4.0-4.5 only its feet/belly show beside the white parrot. The green parrot enters at the right edge from 2.5. The hand box holds hand and toy; at 1.5-2.0 its top is lowered so it does not overlap the lying grey parrot (the white tip of the toy is outside). The toy pistol is seen from the front and looks like a blue-white tube, so it is not used as a noun. Only a hand is seen: defaultVoice by odd id."})

# ---------- 4188
t=T(20)
sk={0.0:(.33,.35),0.5:(.33,.35),1.0:(.29,.34),1.5:(.27,.34),2.0:(.30,.35),2.5:(.34,.36),3.0:(.37,.37),3.5:(.36,.37),
 4.0:(.31,.36),4.5:(.26,.36),5.0:(.30,.37),5.5:(.35,.39),6.0:(.36,.40),6.5:(.35,.43),7.0:(.35,.46),7.5:(.36,.49),
 8.0:(.39,.53),8.5:(.43,.56),9.0:(.46,.57),9.5:(.49,.59)}
sun={8.5:(.76,.25,.24,.18),9.0:(.66,.25,.24,.18),9.5:(.58,.24,.24,.18)}
save({"mediaId":4188,"level":"B","keyWord":"slope","defaultVoice":"male",
"taps":[
 {"phrase":"to descend a steep slope","target":"the skier","voice":"male","keys":keys(t,sk,(.18,.14))},
 {"phrase":"to throw up powder snow","target":"the skier","voice":"male","keys":keys(t,sk,(.18,.14))},
 {"phrase":"to glow above the peaks","target":"the sun","voice":"male","keys":keys(t,sun)}],
"stillS":9.0,
"nouns":[{"word":"peaks","x":0.25,"y":0.42,"voice":"male"},{"word":"the sun","x":0.77,"y":0.34,"voice":"male"},
 {"word":"a skier","x":0.55,"y":0.65,"voice":"male"},{"word":"a slope","x":0.30,"y":0.85,"voice":"male"}],
"question":"What is the skier doing?",
"answer":["He","is","skiing","down","a","steep","slope."],
"answerVoice":"male",
"notes":"The skier is a tiny figure the whole clip: minimum-size box centred on him (the snow plume behind him is partly outside). His gender cannot be seen; 'He' follows the clip description. The sun disc is only in the picture from 8.5 (before that just an orange glow), so the sun target is off until then. Only two possible targets; the skier carries two phrases."})

# ---------- 4189
t=T(25)
dog={1.5:(.48,0,.28,.26),2.0:(.42,0,.34,.27),2.5:(.36,0,.40,.28),3.0:(.34,0,.42,.30),3.5:(.32,0,.44,.30),4.0:(.29,0,.46,.46),
 4.5:(.16,0,.60,.57),5.0:(.06,0,.72,.67),5.5:(.08,0,.88,.78),6.0:(0,0,1,.83),6.5:(0,0,1,.86),7.0:(0,0,1,.83),7.5:(0,0,1,.84),
 8.0:(0,0,1,.87),8.5:(0,0,1,.86),9.0:(0,0,.78,.40),9.5:(.04,0,.80,.60),10.0:(.08,0,.82,.92),10.5:(.08,0,.82,1),
 11.0:(.09,0,.78,1),11.5:(.10,0,.78,1),12.0:(.08,0,.78,1)}
pill={0.0:(.39,.37),0.5:(.37,.59),1.0:(.35,.59),1.5:(.38,.62),2.0:(.38,.61),9.0:(.40,.67),9.5:(.40,.86)}
save({"mediaId":4189,"level":"A","keyWord":"empty","defaultVoice":"male",
"taps":[
 {"phrase":"to eat from a bowl","target":"the dog","voice":"male","keys":keys(t,dog)},
 {"phrase":"to sit by the door","target":"the dog","voice":"male","keys":keys(t,dog)},
 {"phrase":"to stay in the bowl","target":"the pill","voice":"male","keys":keys(t,pill,(.18,.14))}],
"stillS":1.5,
"nouns":[{"word":"a dog","x":0.62,"y":0.12,"voice":"male"},{"word":"a bowl","x":0.50,"y":0.52,"voice":"male"},
 {"word":"a pill","x":0.47,"y":0.69,"voice":"male"},{"word":"food","x":0.50,"y":0.83,"voice":"male"}],
"question":"What is in the empty bowl?",
"answer":["There","is","a","white","pill","in","it."],
"answerVoice":"male",
"notes":"The pill is the second target: visible 0.0-2.0 (in the fingers, then on the food), hidden under the yoghurt and the dog's head 2.5-8.5, alone in the empty bowl at 9.0 and blurred at the bottom edge at 9.5; minimum-size box. The dog is off before 1.5 (not in the picture) and its box covers almost the whole picture while it eats (5.5-8.5). At 9.0-9.5 only the dog's legs are seen. Only hands of a person are seen: defaultVoice by odd id. 'a bowl' pill sits on the black inner wall of the bowl above the food."})
