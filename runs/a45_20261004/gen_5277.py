import json
def K(d, times):
    out=[]
    for t in times:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=v; out.append({"t":t,"x":x,"y":y,"w":round(min(w,1-x),2),"h":round(min(h,1-y),2)})
    return out
times=[i*0.5 for i in range(19)]
boy={0.5:(0.03,0.14,0.58,0.47),1.0:(0,0.28,0.18,0.40),1.5:(0,0.20,0.37,0.50),2.0:(0,0.24,0.47,0.63),
 3.0:(0,0.05,0.55,0.95),3.5:(0,0.13,0.51,0.47),4.0:(0,0.10,0.49,0.52),4.5:(0,0.12,0.50,0.52),
 5.0:(0,0.12,0.49,0.53),5.5:(0,0.12,0.49,0.53),6.0:(0,0.12,0.49,0.50)}
girl={0.0:(0.18,0.19,0.68,0.81),0.5:(0.62,0.20,0.38,0.80),1.0:(0.56,0.24,0.44,0.76),1.5:(0.62,0.17,0.38,0.53),
 2.0:(0.55,0.30,0.45,0.47),3.0:(0.55,0.05,0.45,0.95),3.5:(0.51,0.20,0.49,0.40),4.0:(0.49,0.18,0.51,0.44),
 4.5:(0.50,0.18,0.50,0.46),5.0:(0.49,0.20,0.51,0.45),5.5:(0.49,0.20,0.51,0.45),6.0:(0.49,0.19,0.51,0.43)}
kids={6.5:(0,0.36,1.0,0.28),7.0:(0,0.36,0.95,0.26),7.5:(0,0.26,1.0,0.38),8.0:(0,0.27,1.0,0.43),
 8.5:(0,0.29,1.0,0.53),9.0:(0,0.27,1.0,0.73)}
c={"mediaId":5277,"level":"A","keyWord":"agree","defaultVoice":"male","taps":[
 {"phrase":"to wear blue jeans","target":"the boy","voice":"male","keys":K(boy,times)},
 {"phrase":"to wear a grey dress","target":"the girl","voice":"female","keys":K(girl,times)},
 {"phrase":"to lie on the grass","target":"the children in the garden","voice":"male","keys":K(kids,times)}],
 "stillS":3.5,
 "nouns":[{"word":"a boy","x":0.24,"y":0.30,"voice":"male"},
  {"word":"a girl","x":0.77,"y":0.33,"voice":"female"},
  {"word":"a cookie","x":0.51,"y":0.70,"voice":"male"},
  {"word":"a plate","x":0.50,"y":0.79,"voice":"male"}],
 "question":"Where are the children lying?",
 "answer":["The","children","are","lying","on","the","grass."],
 "answerVoice":"male",
 "notes":"Boy and girl do every action together (run, hold the sheet, high-five, pull the cookie), so they get clothing states. Indoor part is black-and-white; 'blue jeans' is only readable as denim (in colour in the garden). Garden 6.5-9.0: a different crowd of children; the boy/girl cannot be identified there, so both are OFF and one 'children' box covers the whole group (at 6.5/7.0 the running kids, 7.5+ the laughing pile). Weak spot: some garden kids also wear jeans/dresses, but they belong to the children box. Boy OFF at 0.0 (hidden behind the girl), both OFF at 2.5 (only the sheet). Key word 'agree' is a verb, not placed as a noun."}
json.dump(c,open('content/5277.json','w'),indent=1)
