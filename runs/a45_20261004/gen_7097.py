import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
front=K([(0.08,0.12,0.60,0.60),(0.08,0.11,0.62,0.60),(0.0,0.10,0.50,0.66),(0.0,0.08,0.44,0.68),(0.0,0.07,0.52,0.88),(0.0,0.05,0.54,0.73),(0.0,0.03,0.54,0.80),(0.0,0.0,0.46,0.76)])
clip=K([(0.80,0.26,0.20,0.26),(0.79,0.26,0.21,0.26),(0.78,0.26,0.22,0.27),(0.78,0.25,0.22,0.28),(0.78,0.23,0.22,0.26),(0.78,0.22,0.22,0.27),(0.78,0.21,0.22,0.27),(0.77,0.19,0.23,0.28)])
c={"mediaId":7097,"level":"B","keyWord":"fake","defaultVoice":"female",
"taps":[{"phrase":"to scrub the bust's cheek","target":"the woman in front","voice":"female","keys":front},
{"phrase":"to frown in doubt","target":"the woman in front","voice":"female","keys":front},
{"phrase":"to write on a clipboard","target":"the woman with the clipboard","voice":"female","keys":clip}],
"stillS":0.2,
"nouns":[{"word":"a lab coat","x":0.22,"y":0.55,"voice":"female"},{"word":"a bust","x":0.66,"y":0.58,"voice":"female"},
{"word":"a jar","x":0.90,"y":0.78,"voice":"female"},{"word":"cotton swabs","x":0.17,"y":0.88,"voice":"female"}],
"question":"What is the woman in front doing?","answer":["She","is","rubbing","the","bust","with","a","cotton","swab."],"answerVoice":"female",
"notes":"Three women: the restorer in front (swabs the cheek 0.2-1.7 s, frowns 2.7-3.2 s, touches the white patch 3.2 s), the woman with the clipboard on the right (writes the whole clip), a third woman lifting a bust in the back (not used). Key word 'fake' (noun) is not placed as its own label; the fake bust is labelled 'a bust'."}
json.dump(c,open('content/7097.json','w'),indent=1)
