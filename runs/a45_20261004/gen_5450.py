import json
T=[i*0.5 for i in range(25)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2],2),"h":round(b[3],2)})
    return out
W={0.0:(0.33,0.36,0.67,0.60),0.5:(0.63,0.38,0.37,0.46),1.0:(0.60,0.38,0.40,0.62),1.5:(0.22,0.06,0.78,0.94),
 2.0:(0.0,0.06,1.0,0.94),2.5:(0.30,0.30,0.70,0.26),3.0:(0.38,0.35,0.62,0.22),3.5:(0.32,0.02,0.68,0.98),
 4.0:(0.0,0.03,1.0,0.97),4.5:(0.42,0.0,0.58,1.0),5.0:(0.60,0.0,0.40,1.0),5.5:(0.60,0.0,0.40,1.0),
 6.0:(0.80,0.03,0.20,0.97),6.5:(0.80,0.08,0.20,0.92),7.0:(0.74,0.06,0.26,0.94),7.5:(0.57,0.10,0.43,0.90),
 8.0:(0.40,0.23,0.60,0.77),8.5:(0.14,0.28,0.86,0.72),9.0:(0.20,0.28,0.80,0.72),9.5:(0.27,0.28,0.73,0.72),
 10.0:(0.40,0.42,0.60,0.58),10.5:(0.58,0.42,0.42,0.58),11.0:(0.58,0.42,0.42,0.58),11.5:(0.58,0.42,0.42,0.58),12.0:(0.55,0.40,0.45,0.60)}
F={4.5:(0.0,0.33,0.42,0.67),5.0:(0.06,0.25,0.54,0.75),5.5:(0.04,0.25,0.56,0.75),6.0:(0.08,0.31,0.56,0.69),
 6.5:(0.06,0.32,0.58,0.68),7.0:(0.04,0.33,0.60,0.67),7.5:(0.38,0.38,0.18,0.32)}
c={"mediaId":5450,"level":"B","keyWord":"device","defaultVoice":"female",
"taps":[{"phrase":"to unplug the toaster","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to stretch her arm upwards","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to have a protective grille","target":"the fan","voice":"female","keys":keys(F)}],
"stillS":3.0,
"nouns":[{"word":"a kitchen cupboard","x":0.50,"y":0.14,"voice":"female"},{"word":"a socket","x":0.40,"y":0.41,"voice":"female"},
{"word":"a toaster","x":0.45,"y":0.62,"voice":"female"},{"word":"a worktop","x":0.45,"y":0.88,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","unplugging","all","her","devices."],"answerVoice":"female",
"notes":"Woman used for two phrases (she is the only person); fan is the third target (4.5-7.5 s). At 5.0-5.5 the woman's hand and head overlap the fan, split at x=0.60 so her hand on the fan is outside her box. Socket pill sits next to her hand at 3.0."}
json.dump(c,open('content/5450.json','w'),indent=1)
