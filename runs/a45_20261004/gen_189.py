import json
def keys(d): return [({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]}) for t,v in sorted(d.items())]
def tap(p,t,v,d): return {"phrase":p,"target":t,"voice":v,"keys":keys(d)}
def noun(w,x,y,v): return {"word":w,"x":x,"y":y,"voice":v}
N=None

G={0.0:(.15,.43,.42,.19),0.5:(.14,.43,.43,.20),1.0:(.13,.43,.44,.22),1.5:(.11,.43,.46,.22),2.0:(.09,.43,.48,.22),2.5:(.05,.43,.50,.22),3.0:(0,.43,.53,.24),3.5:(0,.43,.51,.24),4.0:(0,.42,.46,.28),
4.5:(0,.46,.34,.17),5.0:(0,.47,.34,.17),5.5:N,6.0:N,6.5:N,7.0:(0,.05,1,.82),7.5:(0,.05,1,.82),8.0:(0,0,1,.72),8.5:N,9.0:N,9.5:(.02,.48,.34,.15),10.0:N,10.5:N,11.0:N}
K={0.0:(.57,.42,.19,.14),0.5:(.57,.42,.19,.14),1.0:(.57,.43,.19,.15),1.5:(.57,.43,.19,.15),2.0:(.57,.43,.19,.15),2.5:(.55,.43,.21,.15),3.0:(.53,.42,.22,.16),3.5:(.51,.42,.24,.17),4.0:(.46,.42,.29,.17),
4.5:(.34,.45,.31,.19),5.0:(.34,.47,.32,.18),5.5:(0,.03,1,.80),6.0:(0,.03,1,.74),6.5:(0,0,1,.75),7.0:N,7.5:N,8.0:N,8.5:N,9.0:(0,.12,1,.58),9.5:(.36,.48,.30,.17),10.0:(0,0,1,.58),10.5:(0,.30,.97,.41),11.0:(0,.42,1,.41)}
W={0.0:(.77,.41,.19,.14),0.5:(.77,.42,.19,.14),1.0:(.77,.43,.18,.14),1.5:(.77,.43,.18,.14),2.0:(.77,.43,.19,.14),2.5:(.77,.43,.20,.14),3.0:(.76,.42,.22,.15),3.5:(.76,.42,.24,.15),4.0:(.76,.41,.24,.16),
4.5:(.65,.46,.35,.17),5.0:(.66,.47,.34,.17),5.5:N,6.0:N,6.5:N,7.0:N,7.5:N,8.0:N,8.5:(0,.13,1,.62),9.0:N,9.5:(.66,.48,.34,.15),10.0:N,10.5:N,11.0:N}
c={"mediaId":189,"level":"B","keyWord":"convoy","defaultVoice":"male",
"taps":[tap("to lead the convoy","the grey car","male",G),tap("to park between two vehicles","the black car","male",K),tap("to bring up the rear","the white car","male",W)],
"stillS":2.0,
"nouns":[noun("a convoy",.55,.50,"male"),noun("trees",.28,.20,"male"),noun("asphalt",.40,.78,"male"),noun("the sky",.75,.12,"male")],
"question":"What are the three cars doing?","answer":["They","are","driving","in","a","convoy."],"answerVoice":"male",
"notes":"No people; default voice male (odd id). Close-ups 5.5-8.0 and 9.0-11.0 show one car each: 5.5/6.0 grille and 6.5 bronze wheel = black car (dark matte paint), 7.0/7.5 wheel and 8.0 headlight = grey car (colour judged from the light matte paint; 8.0 could also be read as the white car - doubt), 8.5 open door = white car, 9.0/10.0-11.0 rear with spoiler = black car. 'to lead the convoy' and 'to bring up the rear' hold in the driving part 0.0-4.0; 'to park between two vehicles' holds at 4.5, 5.0, 9.5. The noun 'a convoy' labels the line of three cars as a group. In the driving part the grey and the black car overlap slightly, boxes split between them."}
json.dump(c,open('content/189.json','w'),indent=1)
