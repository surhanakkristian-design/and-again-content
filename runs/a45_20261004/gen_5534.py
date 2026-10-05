import json,sys
def K(rows):
    out=[]
    for r in rows:
        if r[1] is None: out.append({"t":r[0],"off":True}); continue
        t,x0,y0,x1,y1=r
        out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
wr=[0.58,0.56,0.60,0.60,0.60,0.59,0.56,0.58]
ml=[0.60,0.57,0.64,0.64,0.64,0.60,0.57,0.59]
W=K([(t,0.0,0.21,r,0.96) for t,r in zip(T,wr)])
M=K([(t,l,0.21,1.0,1.0) for t,l in zip(T,ml)])
d={"mediaId":5534,"level":"B","keyWord":"affordable","defaultVoice":"female",
"taps":[
 {"phrase":"to accept a huge bouquet","target":"the woman","voice":"female","keys":W},
 {"phrase":"to sniff the fragrant peonies","target":"the woman","voice":"female","keys":W},
 {"phrase":"to gesture with both hands","target":"the young man","voice":"male","keys":M}],
"stillS":1.2,
"nouns":[{"word":"an awning","x":0.50,"y":0.10,"voice":"female"},
 {"word":"a wicker basket","x":0.48,"y":0.63,"voice":"female"},
 {"word":"an apron","x":0.88,"y":0.70,"voice":"female"},
 {"word":"tulips","x":0.80,"y":0.92,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","sniffing","the","fragrant","peonies."],
"answerVoice":"female",
"notes":"Key word 'affordable' not visible as noun. Woman and stallholder boxes split along the line between bouquet and his reaching hand (0.56-0.64). The man box also covers the background stall worker behind him (she is not a target). Man gestures with both hands from t=2.7; at 0.2-0.7 he hands over the bouquet."}
json.dump(d,open("content/5534.json","w"),indent=1)
