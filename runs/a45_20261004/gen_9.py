import json
def b(t,x,y,w,h): return {"t":t,"x":x,"y":y,"w":w,"h":h}
def off(t): return {"t":t,"off":True}
T=[i*0.5 for i in range(17)]
F=(0,0,1,1)
S={0.0:F,0.5:F,1.0:F,1.5:F,2.0:(.47,.17,.53,.56),2.5:(.37,0,.63,1),3.0:(.37,0,.63,1),3.5:F,4.0:F,4.5:(.38,.05,.62,.95),5.0:(.38,.05,.62,.95),
   5.5:(0,.20,.46,.80),6.0:(.03,.19,.47,.80),6.5:(0,.19,.50,.80),7.0:(0,.18,.50,.82),7.5:(0,.18,.50,.82),8.0:(0,.14,.50,.86)}
Z={5.5:(.46,.05,.54,.92),6.0:(.50,0,.50,1),6.5:(.50,.08,.50,.90),7.0:(.50,0,.50,1),7.5:(.50,0,.50,1),8.0:(.50,0,.50,1)}
k=lambda M:[b(t,*M[t]) if t in M else off(t) for t in T]
c={"mediaId":9,"level":"B","keyWord":"laboratory","defaultVoice":"female",
"taps":[{"phrase":"to pull on purple gloves","target":"the scientist","voice":"female","keys":k(S)},
 {"phrase":"to examine a small tube","target":"the scientist","voice":"female","keys":k(S)},
 {"phrase":"to keep the samples frozen","target":"the freezer","voice":"female","keys":k(Z)}],
"stillS":8.0,
"nouns":[{"word":"safety glasses","x":0.20,"y":0.29,"voice":"female"},{"word":"test tubes","x":0.50,"y":0.47,"voice":"female"},
 {"word":"a lab coat","x":0.18,"y":0.70,"voice":"female"},{"word":"a freezer","x":0.75,"y":0.82,"voice":"female"}],
"question":"What is the scientist doing?",
"answer":["She","is","storing","test","tubes","in","the","freezer."],
"answerVoice":"female",
"notes":"Only one person; in most shots only her hands/coat are visible, I boxed those as 'the scientist'. Key word 'laboratory' is the place, not a placeable thing, so it is not a noun slot. In 5.5-8.0 the scientist and the freezer overlap (her arms reach into it): split at x=0.50 (0.46 at 5.5), so her hands and the rack fall in the freezer box. 'test tubes' = the blue-capped sample tubes on the wire rack. Whether she puts the rack in or takes it out cannot be told from the frames; the description says she stores it."}
json.dump(c,open('content/9.json','w'),indent=1)
