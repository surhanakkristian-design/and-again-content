import json
T=[i*0.5 for i in range(19)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
wo={0.0:(0.05,0.15,0.68,0.85),0.5:(0.0,0.14,0.78,0.86),1.0:(0.0,0.13,0.88,0.87),1.5:(0.02,0.05,0.92,0.95),2.0:(0,0,1,1),2.5:(0,0,1,1),
 3.0:(0.0,0.14,0.5,0.8),3.5:(0.0,0.14,0.5,0.8),4.0:(0.0,0.14,0.51,0.76),4.5:(0.02,0.12,0.79,0.88),5.0:(0.0,0.13,0.72,0.87),
 5.5:(0.0,0.13,0.72,0.87),6.0:(0.05,0.1,0.67,0.9),7.0:(0.0,0.3,0.53,0.7),7.5:(0.0,0.2,0.43,0.75),8.0:(0.0,0.21,0.42,0.7),
 8.5:(0.0,0.23,0.48,0.68),9.0:(0.0,0.27,0.38,0.7)}
ma={3.0:(0.51,0.1,0.49,0.85),3.5:(0.51,0.1,0.49,0.85),4.0:(0.52,0.11,0.48,0.75),4.5:(0.82,0.6,0.18,0.25),5.0:(0.73,0.58,0.27,0.22),
 5.5:(0.73,0.58,0.27,0.22),6.0:(0.73,0.55,0.27,0.2),7.0:(0.54,0.3,0.46,0.65),7.5:(0.52,0.1,0.48,0.88),8.0:(0.6,0.14,0.4,0.78),
 8.5:(0.6,0.16,0.4,0.75),9.0:(0.48,0.2,0.47,0.73)}
c={"mediaId":4924,"level":"A","keyWord":"familiar","defaultVoice":"female",
 "taps":[{"phrase":"to look at her phone","target":"the woman","voice":"female","keys":K(wo)},
  {"phrase":"to wear a denim jacket","target":"the man","voice":"male","keys":K(ma)},
  {"phrase":"to wear a big sweater","target":"the woman","voice":"female","keys":K(wo)}],
 "stillS":8.0,
 "nouns":[{"word":"a woman","x":0.2,"y":0.5,"voice":"female"},{"word":"a man","x":0.82,"y":0.42,"voice":"male"},
  {"word":"the street","x":0.5,"y":0.62,"voice":"female"},{"word":"a plant","x":0.87,"y":0.8,"voice":"female"}],
 "question":"What is the woman looking at?",
 "answer":["She","is","looking","at","her","phone."],"answerVoice":"female",
 "notes":"Only two people; they do everything together (point, shake hands, hold coffee), so the man gets a state (denim jacket) and the woman a second state (big beige sweater). Man not visible 0.0-2.5 (only a blurred blue strip at the right edge at 1.0-1.5, left off). 4.5-6.0 the man is only his denim arm in the handshake (small box at the right). 6.5 = close-up of two hands with cups, owners unclear -> both off. 7.0 = cups close-up: sweater sleeve hand left (woman), denim sleeve hand right (man). Key word 'familiar' is an adjective, no noun slot."}
json.dump(c,open('content/4924.json','w'),indent=1)
