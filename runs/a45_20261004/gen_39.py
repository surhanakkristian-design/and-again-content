import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
black={0.0:(0,0.28,0.20,0.67),0.5:(0,0.25,0.26,0.65),1.0:(0,0.24,0.27,0.73),1.5:(0,0.18,0.28,0.79),2.0:(0,0.12,0.27,0.83),2.5:(0,0.06,0.20,0.88),3.0:(0,0.22,0.18,0.16),
       9.0:(0,0.28,0.18,0.16),9.5:(0,0.30,0.18,0.62),10.0:(0,0.30,0.14,0.66)}
amb={0.0:(0.23,0.46,0.19,0.15),0.5:(0.26,0.46,0.19,0.14),1.0:(0.27,0.46,0.19,0.15),1.5:(0.28,0.47,0.20,0.19),2.0:(0.27,0.44,0.25,0.20),2.5:(0.24,0.42,0.37,0.23),
     3.0:(0.25,0.38,0.51,0.27),3.5:(0.26,0.34,0.74,0.34),4.0:(0.26,0.30,0.74,0.41),4.5:(0.25,0.30,0.75,0.43),5.0:(0.23,0.31,0.77,0.43),5.5:(0.23,0.31,0.77,0.43),
     6.0:(0.25,0.32,0.75,0.42),6.5:(0.57,0.33,0.43,0.43),7.0:(0.58,0.33,0.42,0.43),7.5:(0.61,0.33,0.39,0.43),8.0:(0.63,0.34,0.37,0.44),8.5:(0.65,0.36,0.35,0.42),
     9.0:(0.73,0.37,0.27,0.42),9.5:(0.77,0.36,0.23,0.44),10.0:(0.70,0.33,0.30,0.40)}
yel={6.5:(0.39,0.41,0.18,0.24),7.0:(0.39,0.39,0.19,0.28),7.5:(0.48,0.39,0.13,0.28),8.0:(0.45,0.41,0.18,0.32),8.5:(0.46,0.39,0.19,0.36),9.0:(0.47,0.39,0.26,0.41),
     9.5:(0.46,0.36,0.31,0.50),10.0:(0.33,0.31,0.37,0.62)}
c={"mediaId":39,"level":"A","keyWord":"ambulance","defaultVoice":"male",
 "taps":[{"phrase":"to watch the ambulance","target":"the man in black","voice":"male","keys":keys(black)},
         {"phrase":"to stop near the cafe","target":"the ambulance","voice":"male","keys":keys(amb)},
         {"phrase":"to carry a red bag","target":"the man in yellow","voice":"male","keys":keys(yel)}],
 "stillS":9.0,
 "nouns":[{"word":"the sky","x":0.50,"y":0.08,"voice":"male"},{"word":"houses","x":0.75,"y":0.30,"voice":"male"},
          {"word":"an ambulance","x":0.80,"y":0.52,"voice":"male"},{"word":"a bag","x":0.53,"y":0.64,"voice":"male"}],
 "question":"What is the man in black doing?",
 "answer":["He","is","watching","the","ambulance."],"answerVoice":"male",
 "notes":"Man in black is only in the picture 0-3 s and again as a sliver at the left edge 9-10 s. The paramedics stand in front of the ambulance from 6.5 s, so the ambulance box is cut to the part right of the man in yellow. At 6.5-7.0 s only one paramedic with the red bag is visible in the door (generated clip; could be read as the woman) - boxed as the bag carrier; from 8.0 s the man clearly carries the bag. At 7.5 s the man's box is narrow to leave out the woman."}
json.dump(c,open('content/39.json','w'),indent=1,ensure_ascii=False)
