import json
def keys(d, times):
    out=[]
    for t in times:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]
def save(o):
    json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 4321
t=T(19)
w={0.0:(0.18,0,0.74,0.77),0.5:(0.10,0,0.86,0.78),1.0:(0,0,0.97,0.90),1.5:(0.07,0.03,0.86,0.62),
   2.0:(0.07,0.02,0.85,0.62),2.5:(0.17,0.03,0.72,0.66),3.0:(0.17,0.05,0.72,0.84),3.5:(0.17,0.05,0.74,0.86),
   4.0:(0,0,0.64,0.63),4.5:(0,0,0.66,0.64),5.0:(0,0,0.55,0.68),5.5:(0,0,0.56,0.68),6.0:(0,0,0.48,0.58)}
s={}
for x in (6.5,7.0,7.5,8.0,8.5,9.0):
    w[x]=(0,0.48,1.0,0.52); s[x]=(0.25,0,0.67,0.46)
wk=keys(w,t)
save({"mediaId":4321,"level":"B","keyWord":"model","defaultVoice":"female","taps":[
 {"phrase":"to mark a technical drawing","target":"the woman in the headscarf","voice":"female","keys":wk},
 {"phrase":"to adjust a miniature tower","target":"the woman in the headscarf","voice":"female","keys":wk},
 {"phrase":"to reflect the blue sky","target":"the skyscraper","voice":"female","keys":keys(s,t)}],
 "stillS":5.5,
 "nouns":[{"word":"a model","x":0.47,"y":0.74,"voice":"female"},{"word":"a headscarf","x":0.29,"y":0.30,"voice":"female"},
          {"word":"a blazer","x":0.16,"y":0.47,"voice":"female"},{"word":"glasses","x":0.27,"y":0.05,"voice":"female"}],
 "question":"What is the woman adjusting?",
 "answer":["She","is","adjusting","a","tower","on","the","model."],"answerVoice":"female",
 "notes":"Two phrases share the woman in the headscarf (the two colleagues at 2.0-3.5 s do nothing that only one of them does). Skyscraper box = the part above her hard hat only (she stands in front of it), so the boxes do not overlap. Glasses pill sits at the top edge (y 0.05). Another woman (colleague) is visible 2.0-3.5 s, but only the woman in the headscarf adjusts anything."})

# 4324
t=T(25)
m={0.0:(0,0.30,0.67,0.70),0.5:(0.05,0.31,0.65,0.69),1.0:(0.03,0.34,0.61,0.66),1.5:(0,0.37,0.46,0.63),
   2.0:(0,0.36,0.64,0.64),2.5:(0,0.36,0.68,0.64),3.0:(0,0.38,0.76,0.62),3.5:(0,0.20,0.97,0.80),
   8.5:(0.33,0.45,0.36,0.50),9.0:(0.29,0.46,0.40,0.51),9.5:(0.30,0.46,0.41,0.51),10.0:(0.08,0.45,0.88,0.55),
   10.5:(0.02,0.45,0.98,0.55),11.0:(0,0.45,1.0,0.55),11.5:(0,0.45,1.0,0.55),12.0:(0,0.43,1.0,0.57)}
for x in (4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0): m[x]=(0,0.17,1.0,0.83)
c={1.5:(0.47,0.42,0.27,0.21),2.0:(0.65,0.39,0.20,0.23),2.5:(0.69,0.40,0.23,0.22),3.0:(0.77,0.40,0.21,0.22)}
g={8.5:(0,0.20,1.0,0.24),9.0:(0,0.22,1.0,0.23),9.5:(0,0.22,1.0,0.23),10.0:(0,0.20,1.0,0.24),10.5:(0,0.18,1.0,0.26),
   11.0:(0,0.14,1.0,0.30),11.5:(0,0.10,1.0,0.34),12.0:(0,0.05,1.0,0.37)}
save({"mediaId":4324,"level":"B","keyWord":"vast","defaultVoice":"male","taps":[
 {"phrase":"to sip through a metal straw","target":"the man in the scarf","voice":"male","keys":keys(m,t)},
 {"phrase":"to dance in the street","target":"the dancing couple","voice":"male","keys":keys(c,t)},
 {"phrase":"to stretch into the distance","target":"the glacier","voice":"male","keys":keys(g,t)}],
 "stillS":9.5,
 "nouns":[{"word":"a glacier","x":0.22,"y":0.47,"voice":"male"},{"word":"a railing","x":0.80,"y":0.69,"voice":"male"},
          {"word":"a scarf","x":0.50,"y":0.60,"voice":"male"},{"word":"the sky","x":0.50,"y":0.10,"voice":"male"}],
 "question":"Where is the man standing?",
 "answer":["He","is","standing","in","front","of","a","vast","glacier."],"answerVoice":"male",
 "notes":"Glacier box = the band of ice above the man's head only (he stands in front of the ice wall and spreads his arms, so the ice beside and below his arms falls to his box or to no box). Couple is off at 1.0 s (hidden behind his head). At 1.5 s the man's outstretched hand is left out of his box to keep clear of the couple. Scarf pill sits on the man (no 'a man' noun)."})

# 4327
t=T(25)
m={0.0:(0.60,0.14,0.40,0.46),0.5:(0.64,0.13,0.36,0.47),1.0:(0.63,0.11,0.37,0.57),1.5:(0.65,0.08,0.35,0.60),
   8.5:(0.44,0,0.56,0.50),9.0:(0.58,0,0.42,0.62),9.5:(0.60,0,0.40,0.66),10.0:(0.51,0,0.49,0.62),
   10.5:(0.47,0,0.53,0.60),11.0:(0.46,0.18,0.54,0.68),11.5:(0.50,0.10,0.50,0.78),12.0:(0.22,0.05,0.78,0.72)}
g={0.0:(0,0.25,0.59,0.27),0.5:(0,0.26,0.63,0.26),1.0:(0,0.25,0.62,0.27),1.5:(0,0.24,0.64,0.26),
   2.0:(0.12,0.05,0.88,0.27),2.5:(0.12,0.05,0.88,0.22),3.0:(0.10,0.05,0.90,0.32),3.5:(0.10,0.03,0.90,0.25),
   4.0:(0.10,0.02,0.90,0.28),4.5:(0.10,0.02,0.90,0.26),5.0:(0.10,0.02,0.60,0.26),5.5:(0.10,0,0.80,0.27),
   6.0:(0.10,0,0.90,0.22),6.5:(0.08,0,0.72,0.22),8.0:(0.08,0,0.90,0.22),
   8.5:(0,0.10,0.43,0.22),9.0:(0,0.10,0.57,0.33),9.5:(0,0.12,0.59,0.30),10.0:(0,0.15,0.50,0.20),
   10.5:(0,0.22,0.46,0.17),11.0:(0,0.27,0.45,0.22),11.5:(0,0.27,0.49,0.25),12.0:(0,0.38,0.21,0.22)}
e={0.0:(0.15,0.75,0.70,0.22),0.5:(0.15,0.77,0.72,0.20),1.0:(0.15,0.78,0.70,0.20),1.5:(0.12,0.80,0.75,0.19),
   2.0:(0,0.72,1.0,0.28),2.5:(0,0.72,1.0,0.28),8.5:(0,0.80,1.0,0.20),9.0:(0,0.85,1.0,0.15),9.5:(0,0.85,1.0,0.15)}
for x in (3.0,3.5,4.0,6.0,6.5,7.0,7.5,8.0): e[x]=(0,0.75,1.0,0.25)
for x in (4.5,5.0,5.5): e[x]=(0,0.78,1.0,0.22)
save({"mediaId":4327,"level":"B","keyWord":"barbecue","defaultVoice":"male","taps":[
 {"phrase":"to carve the grilled meat","target":"the cook","voice":"male","keys":keys(m,t)},
 {"phrase":"to applaud the cook","target":"the guests","voice":"male","keys":keys(g,t)},
 {"phrase":"to glow under the grill","target":"the embers","voice":"male","keys":keys(e,t)}],
 "stillS":1.5,
 "nouns":[{"word":"a barbecue","x":0.55,"y":0.76,"voice":"male"},{"word":"sausages","x":0.18,"y":0.66,"voice":"male"},
          {"word":"a tablecloth","x":0.33,"y":0.46,"voice":"male"},{"word":"the sky","x":0.30,"y":0.07,"voice":"male"}],
 "question":"What is the cook doing?",
 "answer":["He","is","carving","the","meat","on","the","barbecue."],"answerVoice":"male",
 "notes":"Cook is 'off' in the close-ups 2.0-8.0 s where only his hand / the tongs reach into the picture (his hand there overlaps the guests behind). Guests are off at 7.0-7.5 s (hidden by flames). Guests clap from 9.0 s. Embers: visible under the grill bars in the close-ups, off from 10.0 s. 'a barbecue' pill is on the front rim of the grill, 'sausages' on the left group of sausages - the two are close in meaning of place; verifier please check. The cook and the guests stand close at 9.0-12.0 s: boxes split along the cook's left edge, so his hand / the lifted meat reaching left is partly outside his box."})

# 4329
t=T(25)
y={0.0:(0,0,1.0,1.0),0.5:(0,0.12,1.0,0.88)}
for x in (1.0,1.5,2.0,2.5,3.0): y[x]=(0,0.14,1.0,0.86)
w={3.5:(0,0.18,0.84,0.82),4.0:(0,0.25,1.0,0.75),4.5:(0,0.24,1.0,0.76),5.0:(0,0.24,1.0,0.76),5.5:(0,0.24,1.0,0.76),
   6.0:(0,0.23,1.0,0.77),6.5:(0,0.23,1.0,0.77)}
o={7.0:(0,0,1.0,1.0),7.5:(0,0.15,1.0,0.85)}
for i in range(16,25): o[i*0.5]=(0,0.20,1.0,0.80)
save({"mediaId":4329,"level":"A","keyWord":"furniture","defaultVoice":"male","taps":[
 {"phrase":"to sit on a small chair","target":"the young man","voice":"male","keys":keys(y,t)},
 {"phrase":"to relax on a sofa","target":"the woman","voice":"female","keys":keys(w,t)},
 {"phrase":"to stretch out his legs","target":"the old man","voice":"male","keys":keys(o,t)}],
 "stillS":5.5,
 "nouns":[{"word":"a sofa","x":0.58,"y":0.86,"voice":"male"},{"word":"a plant","x":0.40,"y":0.18,"voice":"male"},
          {"word":"a window","x":0.85,"y":0.14,"voice":"male"},{"word":"a sweater","x":0.55,"y":0.58,"voice":"male"}],
 "question":"What is the woman doing?",
 "answer":["She","is","relaxing","on","a","sofa."],"answerVoice":"female",
 "notes":"Three shots, one person each; every box is the person together with the seat around them (the person fills the frame). Key word 'furniture' is not a countable thing at one place, so it is not a noun slot; 'a sofa' stands for it. Several plants in the still: the pill is on the big one in the middle. defaultVoice male: no single main person, evenId false."})
