import json
T=[i*0.5 for i in range(21)]
def bx(t,x0,y0,x1,y1): return {"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)}
man={0.0:(0,.36,.57,1),0.5:(0,.36,.56,1),1.0:(0.0,.40,.52,1),1.5:(0,.44,.47,1),2.0:(.05,.48,.33,.97),2.5:(.08,.49,.34,.98),
3.0:(.11,.50,.36,1),3.5:(.13,.50,.38,1),4.0:(.15,.50,.39,.94),4.5:(.14,.50,.39,.95),5.0:(.15,.50,.39,.97),5.5:(.15,.50,.39,.97),
6.0:(.16,.50,.39,.95),6.5:(.15,.50,.39,.95),7.0:(.15,.50,.39,.95),7.5:(.15,.50,.39,.95),8.0:(.14,.50,.39,.95),8.5:(.14,.50,.39,.95),
9.0:(.14,.50,.39,.95),9.5:(.14,.50,.39,.95),10.0:(.14,.50,.39,.95)}
sun={0.0:(.57,.42,.75,.56),0.5:(.56,.42,.74,.56),1.0:(.52,.42,.70,.56),1.5:(.47,.40,.65,.56),2.0:(.46,.38,.64,.52),2.5:(.45,.39,.63,.53)}
for t in T:
    if 3.0<=t<=8.5: sun[t]=(.45,.39,.63,.53)
bare={1.0:(.70,.41,1,1),1.5:(.65,.46,.93,1),2.0:(.49,.52,.82,1),2.5:(.45,.53,.73,1),3.0:(.44,.53,.69,1),3.5:(.46,.53,.71,1),
4.0:(.48,.53,.72,.99),4.5:(.48,.53,.73,1),5.0:(.48,.53,.72,1),5.5:(.48,.53,.73,1),6.0:(.48,.53,.72,1),6.5:(.48,.53,.73,1),
7.0:(.48,.53,.72,1),7.5:(.48,.53,.73,1),8.0:(.48,.53,.72,1),8.5:(.48,.53,.73,1),9.0:(.49,.53,.72,1),9.5:(.48,.53,.73,1),10.0:(.48,.53,.72,1)}
def keys(d): return [bx(t,*d[t]) if t in d else {"t":t,"off":True} for t in T]
c={"mediaId":870,"level":"A","keyWord":"west","defaultVoice":"male",
"taps":[
{"phrase":"to point at the sun","target":"the man pointing","voice":"male","keys":keys(man)},
{"phrase":"to go down in the west","target":"the sun","voice":"male","keys":keys(sun)},
{"phrase":"to stand without a shirt","target":"the man without a shirt","voice":"male","keys":keys(bare)}],
"stillS":0.0,
"nouns":[{"word":"the sky","x":0.50,"y":0.18,"voice":"male"},{"word":"the sun","x":0.64,"y":0.47,"voice":"male"},
{"word":"the sea","x":0.70,"y":0.63,"voice":"male"},{"word":"a man","x":0.20,"y":0.72,"voice":"male"}],
"question":"What is the sun doing?",
"answer":["The","sun","is","going","down","in","the","west."],
"answerVoice":"male",
"notes":"Five men seen from behind from 2.0 s; the pointing man is the second from the left (arm stays raised). From about 6.5 s all are silhouettes, so the man without a shirt is only recognisable by position (fourth from left, centre). Sun box off from 9.0 s (sun has set). 'in the west' = key word; a setting sun is in the west, not readable from the picture otherwise. Pointing man's box from 4.0 s ends at x 0.39 (finger tip reaches 0.42) so that it does not swallow the third man. Third phrase is a state: no action is unique to another target."}
json.dump(c,open("content/870.json","w"),indent=1)
