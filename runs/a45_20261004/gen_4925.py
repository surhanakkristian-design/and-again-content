import json
T=[i*0.5 for i in range(19)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
nu={0.0:(0.42,0.33,0.47,0.5),0.5:(0.15,0.22,0.85,0.78),1.0:(0.42,0.3,0.46,0.7),1.5:(0.36,0.32,0.38,0.68),2.0:(0.3,0.31,0.34,0.69),
 2.5:(0.46,0.22,0.51,0.48),3.0:(0.45,0.23,0.48,0.55),3.5:(0.25,0.03,0.75,0.97),4.0:(0.47,0.26,0.53,0.5),4.5:(0.35,0.12,0.62,0.68),
 5.0:(0.35,0.02,0.57,0.8),5.5:(0.35,0.0,0.65,0.4),6.0:(0.0,0.0,1.0,0.5),6.5:(0.0,0.0,1.0,0.55),7.0:(0.0,0.0,1.0,0.38),
 7.5:(0.48,0.24,0.5,0.5),8.0:(0.44,0.25,0.54,0.46),8.5:(0.45,0.26,0.53,0.46),9.0:(0.43,0.22,0.57,0.55)}
pa={2.5:(0.0,0.29,0.45,0.71),3.0:(0.0,0.3,0.44,0.7),4.0:(0.0,0.33,0.46,0.67),4.5:(0.0,0.35,0.34,0.65),5.0:(0.0,0.37,0.34,0.63),
 5.5:(0.25,0.41,0.75,0.4),6.0:(0.28,0.51,0.72,0.39),6.5:(0.35,0.56,0.65,0.44),7.0:(0.2,0.39,0.8,0.61),7.5:(0.0,0.27,0.47,0.73),
 8.0:(0.0,0.28,0.43,0.72),8.5:(0.0,0.26,0.44,0.74),9.0:(0.0,0.05,0.42,0.95)}
c={"mediaId":4925,"level":"B","keyWord":"care","defaultVoice":"female",
 "taps":[{"phrase":"to push a supply trolley","target":"the nurse","voice":"female","keys":K(nu)},
  {"phrase":"to bandage his wrist","target":"the nurse","voice":"female","keys":K(nu)},
  {"phrase":"to lie in a hospital bed","target":"the patient","voice":"male","keys":K(pa)}],
 "stillS":8.0,
 "nouns":[{"word":"a juice carton","x":0.5,"y":0.46,"voice":"female"},{"word":"scrubs","x":0.75,"y":0.6,"voice":"female"},
  {"word":"a hospital gown","x":0.25,"y":0.72,"voice":"female"},{"word":"a bandage","x":0.82,"y":0.78,"voice":"female"}],
 "question":"What is the nurse pushing?",
 "answer":["She","is","pushing","a","supply","trolley","down","the","corridor."],"answerVoice":"female",
 "notes":"Nurse = woman in teal scrubs; the two colleagues in light blue (1.0, waving) are not targets. Trolley pushed 0.0-2.0 (at 1.0-2.0 seen from behind). Patient off 0.0-2.0 and at 3.5 (thermometer close-up). Bedside shots 2.5-5.0 and 7.5-9.0: the nurse stands right of the patient, but his arms stretch under her; the patient box is kept to his head/upper body on the left so the boxes do not overlap (his hands at the right are left out). Close-ups 5.5-7.0: nurse box = her hands/torso at the top, patient box = his bandaged wrist and hand below (her lower hand with the roll sits inside his box at 5.5). 'care' is a verb, no noun slot."}
json.dump(c,open('content/4925.json','w'),indent=1)
