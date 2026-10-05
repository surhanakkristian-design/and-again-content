import json
T=[i*0.5 for i in range(19)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
wt={0.0:(0.22,0.13,0.66,0.87),0.5:(0.22,0.13,0.68,0.87),1.0:(0.0,0.05,1.0,0.95),1.5:(0.0,0.08,0.26,0.92),2.0:(0.0,0.08,0.2,0.92),
 2.5:(0.08,0.12,0.92,0.88),3.0:(0.0,0.1,1.0,0.9),3.5:(0.0,0.1,0.8,0.9),4.0:(0.18,0.15,0.65,0.85),4.5:(0.22,0.17,0.62,0.83),
 5.0:(0.38,0.2,0.48,0.8),5.5:(0.48,0.18,0.5,0.82),6.0:(0.36,0.17,0.62,0.55),6.5:(0.05,0.18,0.95,0.47),7.0:(0.08,0.17,0.92,0.5),
 7.5:(0.05,0.16,0.95,0.5),8.0:(0.14,0.15,0.6,0.5),8.5:(0.55,0.13,0.3,0.15)}
wd={1.5:(0.62,0.27,0.38,0.73),2.0:(0.6,0.26,0.4,0.74),8.0:(0.75,0.1,0.25,0.9),8.5:(0.62,0.29,0.38,0.71),9.0:(0.68,0.3,0.32,0.7)}
c={"mediaId":4923,"level":"A","keyWord":"seat","defaultVoice":"female",
 "taps":[{"phrase":"to carry the menus","target":"the waitress","voice":"female","keys":K(wt)},
  {"phrase":"to read a big book","target":"the waitress","voice":"female","keys":K(wt)},
  {"phrase":"to wear a white dress","target":"the woman in the dress","voice":"female","keys":K(wd)}],
 "stillS":7.0,
 "nouns":[{"word":"a waitress","x":0.55,"y":0.42,"voice":"female"},{"word":"a window","x":0.14,"y":0.28,"voice":"female"},
  {"word":"a candle","x":0.47,"y":0.7,"voice":"female"},{"word":"a table","x":0.55,"y":0.85,"voice":"female"}],
 "question":"What is the waitress carrying?",
 "answer":["She","is","carrying","the","menus."],"answerVoice":"female",
 "notes":"Waitress = blonde in white shirt and black apron. 'to read a big book' = 0.0-0.5 at the stand, she looks down into a large open book with her hand on the page (reservation book). Menus carried 2.5-5.5, laid on the chairs 6.0-7.5. At 1.5-2.0 the waitress is only a blurred back/hair at the left edge (box kept to the hair strip so it does not cover the couple). At 8.5 only her face behind the couple (small box). Man in black shirt not used (no action only he does; dark-clothed guests in the background). Key word 'seat' is a verb, so not a noun slot."}
json.dump(c,open('content/4923.json','w'),indent=1)
