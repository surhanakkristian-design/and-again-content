import json
def K(d,times):
    out=[]
    for t in times:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
times=[i*0.5 for i in range(24)]
M={0.0:(0,.25,.50,.41),0.5:(.10,.30,.90,.36),1.0:(.07,.37,.78,.36),1.5:(.08,.33,.84,.43),2.0:(.06,.33,.84,.43),2.5:(.05,.33,.92,.45),
3.0:(.07,.34,.93,.37),3.5:(.06,.34,.94,.37),4.0:(.03,.34,.97,.37),
7.5:(.28,.55,.44,.14),8.0:(.26,.57,.48,.15),8.5:(.26,.58,.52,.15),9.0:(.26,.58,.52,.15),9.5:(.26,.59,.54,.15),
10.0:(.26,.59,.52,.16),10.5:(.28,.59,.54,.16),11.0:(.26,.59,.52,.16),11.5:(.28,.59,.54,.16)}
G={4.5:(.40,.42,.18,.14),5.0:(.40,.42,.18,.14),5.5:(.40,.40,.18,.14),
7.5:(0,.31,.53,.24),8.0:(0,.31,.53,.26),8.5:(0,.31,.53,.27),9.0:(0,.33,.53,.25),9.5:(0,.32,.53,.27),
10.0:(0,.31,.53,.28),10.5:(0,.31,.53,.28),11.0:(0,.31,.53,.28),11.5:(0,.31,.53,.28)}
B={4.5:(0,.43,.18,.19),5.0:(0,.44,.18,.18),5.5:(0,.43,.18,.19),6.0:(0,.43,.18,.19),6.5:(0,.43,.18,.19),7.0:(0,.42,.18,.20),
7.5:(.53,.31,.47,.24),8.0:(.53,.33,.47,.24),8.5:(.53,.33,.47,.25),9.0:(.53,.35,.47,.23),9.5:(.53,.32,.47,.27),
10.0:(.53,.31,.47,.28),10.5:(.53,.31,.47,.28),11.0:(.53,.31,.47,.28),11.5:(.53,.31,.47,.28)}
c={"mediaId":4238,"level":"A","keyWord":"roast","defaultVoice":"male",
"taps":[
{"phrase":"to roast over a fire","target":"the meat","voice":"male","keys":K(M,times)},
{"phrase":"to use an orange pump","target":"the man in the blue jacket","voice":"male","keys":K(B,times)},
{"phrase":"to wear a grey shirt","target":"the man in the grey shirt","voice":"male","keys":K(G,times)}],
"stillS":10.5,
"nouns":[{"word":"meat","x":.52,"y":.64,"voice":"male"},{"word":"a table","x":.52,"y":.78,"voice":"male"},
{"word":"a carpet","x":.25,"y":.93,"voice":"male"}],
"question":"What is roasting over the fire?",
"answer":["The","meat","is","roasting","over","the","fire."],
"answerVoice":"male",
"notes":"Four shots (stream 0-2.5 s, fire 3-4 s, tent outside 4.5-7 s, tent inside 7.5-11.5 s). 'the meat' is boxed in every shot where it is visible (raw, on the fire, served); the roasting itself is only 3-4 s. Inside the tent the two men's boxes cover head and upper body only, because the dish with the meat lies between and below them. The man at the pump is taken to be the man in the blue jacket (same dark hair, dark blue top) and the man holding the tent the man in grey (small figures, 4.5-5.5 s). 'to wear a grey shirt' is a state: both men do the same actions (eat, blow on the meat). Only 3 nouns."}
json.dump(c,open("content/4238.json","w"),indent=1)
