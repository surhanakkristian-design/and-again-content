import json
T=[i*0.5 for i in range(25)]
def keys(d):
    return [{"t":t,"x":d(t)[0],"y":d(t)[1],"w":d(t)[2],"h":d(t)[3]} for t in T]
def W(t):
    if t<=0.5: return (0.0,0.14,0.73,0.51)
    if t==1.0: return (0.0,0.14,0.64,0.50)
    if t==1.5: return (0.0,0.17,0.44,0.47)
    if t==2.0: return (0.0,0.17,0.24,0.83)
    if t<=9.5: return (0.0,0.13,0.26,0.87)
    if t==10.0: return (0.0,0.11,0.26,0.89)
    if t==10.5: return (0.0,0.14,0.24,0.70)
    if t==11.0: return (0.0,0.16,0.30,0.66)
    if t==11.5: return (0.0,0.18,0.36,0.64)
    return (0.0,0.18,0.48,0.64)
def R(t):
    if t<=0.5: return (0.25,0.66,0.75,0.29)
    if t<=1.5: return (0.21,0.65,0.79,0.30)
    if t==2.0: return (0.25,0.65,0.75,0.29)
    if t<=9.5: return (0.27,0.63,0.73,0.31)
    if t==10.0: return (0.27,0.62,0.73,0.27)
    if t==10.5: return (0.25,0.45,0.56,0.17)
    if t==11.0: return (0.31,0.44,0.42,0.15)
    if t==11.5: return (0.37,0.43,0.38,0.15)
    return (0.49,0.42,0.28,0.15)
w=keys(W); r=keys(R)
c={"mediaId":5178,"level":"B","keyWord":"a headscarf","defaultVoice":"female",
"taps":[
 {"phrase":"to open the oven door","target":"the woman","voice":"female","keys":w},
 {"phrase":"to slide the tray in","target":"the woman","voice":"female","keys":w},
 {"phrase":"to rest on the counter","target":"the baking tray","voice":"female","keys":r}],
"stillS":6.0,
"nouns":[{"word":"a headscarf","x":0.10,"y":0.22,"voice":"female"},
 {"word":"a microwave","x":0.55,"y":0.17,"voice":"female"},
 {"word":"an oven rack","x":0.55,"y":0.50,"voice":"female"},
 {"word":"cookies","x":0.62,"y":0.79,"voice":"female"}],
"question":"What is she wearing on her head?",
"answer":["She","is","wearing","a","navy","headscarf."],
"answerVoice":"female",
"notes":"Woman and tray overlap where her hand grips the tray (2.0-10.0): split vertically at x~0.26, so her hand tip is in the tray box. 0-1.5 woman box stops above the tray (y<0.65). Tray rests on the counter until 10.0, then is lifted into the oven (box follows it)."}
json.dump(c,open('content/5178.json','w'),indent=1)
