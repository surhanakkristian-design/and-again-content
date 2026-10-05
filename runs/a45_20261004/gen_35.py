import json
T=[i*0.5 for i in range(21)]
def b(t,v):
    if v is None: return {"t":t,"off":True}
    x0,y0,x1,y1=v; return {"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)}
A={0.0:(.22,.20,1,1),0.5:(.18,.22,1,1),1.0:(.08,.23,.95,1),1.5:(.25,.20,.78,1),2.0:(.40,.24,.81,1),2.5:(.42,.26,.88,1),3.0:(.30,.25,.85,1),
3.5:(.22,.25,.66,1),4.0:(.25,.23,.79,1),4.5:(.25,.21,.80,1),5.0:(.28,.29,.77,1),5.5:(.30,.24,.79,1),6.0:(.29,.25,.80,1),6.5:(.28,.24,.81,1),
7.0:(.27,.22,.81,1),7.5:(.28,.20,.83,1),8.0:(.25,.22,.81,1),8.5:(.26,.20,.76,1),9.0:(.19,.57,.72,1),9.5:(.31,.42,.97,1),10.0:(.34,.23,.66,1)}
C={2.0:(.82,.38,1,.72),4.0:(.04,.37,.24,.78),4.5:(.04,.37,.24,.78),5.0:(.02,.37,.27,.80),5.5:(.02,.37,.29,.62),6.0:(0,.37,.28,.62),
6.5:(0,.37,.27,.60),7.0:(0,.37,.26,.61),7.5:(0,.37,.27,.60),8.0:(0,.37,.24,.74),8.5:(0,.37,.25,.56),9.0:(.02,.35,.31,.56),
9.5:(.08,.34,.30,.59),10.0:(.12,.35,.33,.72)}
K={4.0:(.80,.41,1,.72),4.5:(.81,.41,1,.72),5.0:(.78,.41,1,.72),5.5:(.80,.41,1,.66),6.0:(.81,.41,1,.60),6.5:(.82,.41,1,.60),7.0:(.82,.41,1,.61),
7.5:(.84,.41,1,.56),8.0:(.82,.41,1,.62),8.5:(.77,.39,1,.63),9.0:(.73,.31,1,.84),9.5:(.70,.27,.92,.41),10.0:(.67,.31,.90,.70)}
c={"mediaId":35,"level":"A","keyWord":"actor","defaultVoice":"male",
"taps":[{"phrase":"to cry and shout","target":"the young man","voice":"male","keys":[b(t,A[t]) for t in T]},
{"phrase":"to hold a big camera","target":"the man with the camera","voice":"male","keys":[b(t,C.get(t)) for t in T]},
{"phrase":"to clap his hands","target":"the man in the cap","voice":"male","keys":[b(t,K.get(t)) for t in T]}],
"stillS":4.0,
"nouns":[{"word":"a microphone","x":.52,"y":.12,"voice":"male"},{"word":"a camera","x":.22,"y":.47,"voice":"male"},
{"word":"an actor","x":.52,"y":.58,"voice":"male"},{"word":"a chair","x":.86,"y":.68,"voice":"male"}],
"question":"What is the actor doing?",
"answer":["He","is","crying","in","front","of","the","camera."],
"answerVoice":"male",
"notes":"Three men: the actor's box is cut at the sides from 4.0 s where his arms cross the two crew men behind him. The camera man's box at 2.0 s is a (probably different) camera operator in the background, also holding a camera. Crew men are not visible before 4.0 s. The chair at 4.0 s is partly hidden behind the actor's arm; a hand with a make-up brush (0-1 s) and the clapperboard (2.5-3.5 s) are not targets."}
json.dump(c,open('content/35.json','w'),indent=1,ensure_ascii=False)
