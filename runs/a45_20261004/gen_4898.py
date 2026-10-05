import json
T=[i*0.5 for i in range(19)]
def k(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
def keys(d): return [k(t,d.get(t)) for t in T]
fl={0.0:(0.17,0.46,0.83,0.36),0.5:(0.17,0.58,0.83,0.33),1.0:(0.15,0.62,0.83,0.27),1.5:(0.18,0.61,0.73,0.28),2.0:(0.16,0.57,0.66,0.18),2.5:(0.0,0.56,0.52,0.18)}
man={3.0:(0.69,0.28,0.28,0.42),3.5:(0.69,0.35,0.18,0.46),4.0:(0.67,0.36,0.18,0.34)}
dome={6.0:(0.18,0.25,0.82,0.5),6.5:(0.0,0.0,1.0,0.22),7.0:(0.0,0.1,1.0,0.66),7.5:(0.0,0.22,1.0,0.52),8.0:(0.02,0.3,0.96,0.38),8.5:(0.04,0.32,0.95,0.37),9.0:(0.04,0.34,0.92,0.37)}
c={"mediaId":4898,"level":"B","keyWord":"panel","defaultVoice":"male",
 "taps":[
  {"phrase":"to bloom in a raised bed","target":"the flowers","voice":"male","keys":keys(fl)},
  {"phrase":"to wear beige work trousers","target":"the man in beige trousers","voice":"male","keys":keys(man)},
  {"phrase":"to tower over the forest","target":"the glass dome","voice":"male","keys":keys(dome)}],
 "stillS":2.0,
 "nouns":[{"word":"a glass panel","x":0.28,"y":0.33,"voice":"male"},
          {"word":"the sky","x":0.55,"y":0.07,"voice":"male"},
          {"word":"flowers","x":0.45,"y":0.63,"voice":"male"},
          {"word":"gravel","x":0.7,"y":0.88,"voice":"male"}],
 "question":"What are the gardeners doing?",
 "answer":["They","are","fitting","glass","panels","into","a","frame."],
 "answerVoice":"male",
 "notes":"Gardeners look alike (straw hats, grey T-shirts), so only one person target: the man in beige/khaki trousers + dark T-shirt, 3.0-4.0 s (at 4.0 he stands inside the glass box). The middle gardener at 0-2.0 s (behind the glass, olive clothes) may be the same man - kept off; verifier please check. Flowers only in the first bed (0-2.5 s; 2.5 blurred). Dome blurred through trees at 6.0, only its top edge at 6.5; 7.0/7.5 dome has an odd cut-out ring shape. Still 2.0: three gardeners visible, so no person noun."}
json.dump(c,open("content/4898.json","w"),indent=1)
