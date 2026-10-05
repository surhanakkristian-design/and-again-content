import json
times=[i/2 for i in range(21)]
def wb(t):
    if t<=1.5: return 0.57
    if t<=2.0: return 0.62
    if t<=2.5: return 0.70
    if t<=3.5: return 0.74
    if t<=6.0: return 0.71
    if t<=6.5: return 0.70
    return 0.68
woman=[{"t":t,"x":0.0,"y":0.0,"w":wb(t),"h":1.0} for t in times]
def sk(t):
    x=wb(t)+0.01
    y=0.24 if t<=1.5 else 0.32
    h=0.20 if t<=1.5 else 0.16
    return {"t":t,"x":round(x,2),"y":y,"w":round(1-x,2),"h":h}
sky=[sk(t) for t in times]
c={"mediaId":4948,"level":"B","keyWord":"skyline","defaultVoice":"female",
"taps":[
{"phrase":"to apply powder with a brush","target":"the woman","voice":"female","keys":woman},
{"phrase":"to raise her eyebrows in surprise","target":"the woman","voice":"female","keys":woman},
{"phrase":"to stretch across the horizon","target":"the skyline","voice":"female","keys":sky}],
"stillS":8.0,
"nouns":[{"word":"a skyline","x":0.82,"y":0.40,"voice":"female"},
{"word":"a make-up brush","x":0.50,"y":0.58,"voice":"female"},
{"word":"a powder compact","x":0.86,"y":0.80,"voice":"female"},
{"word":"a robe","x":0.20,"y":0.72,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","applying","powder","to","her","face."],
"answerVoice":"female",
"notes":"One person only; the skyline is the second target (hazy city outline through the window, right half, y ~0.27-0.47). Woman box is cut at the skyline's left edge, so her compact hand (lower right) lies outside her box (no phrase is about the compact); skyline box stops above it. Woman boxes are wide (x 0 to ~0.7) because her brush hand moves to the right of her face."}
json.dump(c,open('content/4948.json','w'),indent=1)
