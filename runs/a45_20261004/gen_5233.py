import json
T=[i*0.5 for i in range(19)]
def keys(f):
    out=[]
    for t in T:
        b=f(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def officer(t):
    if t<4.5: return None
    x={4.5:0.56,5.0:0.56}.get(t,0.54 if t<=6.0 else 0.53)
    return (x,0.47,0.19,0.20)
def crowd(t):
    if t<4.5: return None
    return (0.0,0.69,1.0,0.31)
def flags(t):
    if t<2.0: return None
    if t<=4.0: return (0.0,0.06,1.0,0.17)
    return (0.0,0.31,1.0,0.14)
c={"mediaId":5233,"level":"B","keyWord":"military","defaultVoice":"female",
 "taps":[
  {"phrase":"to stand before the troops","target":"the officer in front","voice":"female","keys":keys(officer)},
  {"phrase":"to watch from behind barriers","target":"the spectators","voice":"female","keys":keys(crowd)},
  {"phrase":"to flutter in the breeze","target":"the flags","voice":"female","keys":keys(flags)}],
 "stillS":6.0,
 "nouns":[{"word":"the sky","x":0.5,"y":0.15,"voice":"female"},
          {"word":"troops","x":0.3,"y":0.44,"voice":"female"},
          {"word":"an officer","x":0.64,"y":0.57,"voice":"female"},
          {"word":"spectators","x":0.3,"y":0.86,"voice":"female"}],
 "question":"What are the spectators doing?",
 "answer":["They","are","watching","the","military","parade."],
 "answerVoice":"female",
 "notes":"Close-up 0.0-1.5 of a saluting young woman: everyone salutes, so no unique phrase there; all three targets off in the close-up. Flags: big band 2.0-4.0, thin distant line at y~0.37 in the wide shot 4.5-9.0. Officer gender not readable (small figure) -> default voice; defaultVoice female = the young woman in the close-up. Spectator box starts at y 0.69 to avoid the officer box, so the top of the left heads (0.58-0.69) is cut."}
json.dump(c,open('content/5233.json','w'),indent=1)
