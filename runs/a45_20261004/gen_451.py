import json
def keys(d,T):
    out=[]
    for t in T:
        b=d.get(t)
        if not b: out.append({"t":t,"off":True}); continue
        x0,y0,x1,y1=b
        out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
T=[i*0.5 for i in range(13)]
W={0.0:(.30,.05,.84,.66),1.5:(0,.30,.36,.60),2.0:(0,.52,.15,.71),2.5:(0,.50,.26,.80),3.0:(0,.40,.46,.66),3.5:(0,.40,.45,.67),
4.0:(.29,0,.95,1),4.5:(.05,0,.97,1),5.0:(.12,0,.97,1),5.5:(.15,.08,.85,1),6.0:(.18,.15,.78,1)}
K={0.0:(.50,.67,.74,.84),0.5:(.70,.70,.95,.90),1.0:(.02,.36,.62,.68),1.5:(.37,.36,.64,.61),2.0:(.16,.50,.66,.72),2.5:(.27,.50,.69,.70),
4.0:(.08,.40,.28,.61)}
kw=keys(W,T)
c={"mediaId":451,"level":"A","keyWord":"lock","defaultVoice":"female",
"taps":[{"phrase":"to lock the door","target":"the woman","voice":"female","keys":kw},
{"phrase":"to walk away","target":"the woman","voice":"female","keys":kw},
{"phrase":"to go into the lock","target":"the key","voice":"female","keys":keys(K,T)}],
"stillS":4.0,
"nouns":[{"word":"hair","x":0.60,"y":0.08,"voice":"female"},{"word":"a key","x":0.20,"y":0.46,"voice":"female"},
{"word":"a coat","x":0.50,"y":0.68,"voice":"female"},{"word":"a bag","x":0.82,"y":0.85,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","locking","the","door","with","a","key."],"answerVoice":"female",
"notes":"Cartoon. The key is held by the woman, so the two boxes are split: 0.0 the woman's box ends above the key (her legs are outside), 4.0 her raised arm with the key belongs to the key box. 1.5-3.5 only her hand is in the picture = the woman's box (3.0/3.5 she tests the handle, no key visible -> key off). 0.5 and 1.0: no woman (at 1.0 only a fingertip at the left edge) -> off. Key off from 4.5 (in her pocket). 'to walk away' is seen only at 5.5-6.0. 'hair' and 'a coat' are on the same woman but far apart (head / body); no noun 'a woman'."}
json.dump(c,open('content/451.json','w'),indent=1)
