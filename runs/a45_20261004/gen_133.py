import json
def keys(d, n):
    out=[]
    for i in range(n):
        t=i*0.5
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def save(o):
    json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 133
camel={0.0:(0,0.12,0.78,0.63),0.5:(0.02,0.08,0.86,0.62),1.0:(0,0.07,1,0.83),1.5:(0,0.07,1,0.89),2.0:(0,0.08,1,0.92),
2.5:(0,0.1,1,0.9),3.0:(0,0.13,1,0.87),3.5:(0,0.13,1,0.87),4.0:(0,0.13,1,0.87),4.5:(0,0.09,1,0.91),5.0:(0,0.07,1,0.93),
5.5:(0,0.16,1,0.84),6.0:(0,0,1,1),6.5:(0,0.08,1,0.92),7.0:(0,0.14,1,0.86),7.5:(0,0.14,1,0.86),8.0:(0,0.14,0.93,0.86),
8.5:(0,0.17,0.98,0.83),9.0:(0,0.19,0.9,0.81),9.5:(0,0.19,0.93,0.81),10.0:(0,0.19,0.92,0.81)}
k=keys(camel,21)
save({"mediaId":133,"level":"A","keyWord":"camel","defaultVoice":"male",
"taps":[{"phrase":"to walk across the sand","target":"the camel","voice":"male","keys":k},
{"phrase":"to lie down on the sand","target":"the camel","voice":"male","keys":k},
{"phrase":"to look into the camera","target":"the camel","voice":"male","keys":k}],
"stillS":10.0,
"nouns":[{"word":"a camel","x":0.45,"y":0.62,"voice":"male"},{"word":"the sun","x":0.17,"y":0.22,"voice":"male"},
{"word":"sand","x":0.82,"y":0.55,"voice":"male"},{"word":"the sky","x":0.62,"y":0.08,"voice":"male"}],
"question":"What is the camel doing?",
"answer":["The","camel","is","lying","on","the","sand."],"answerVoice":"male",
"notes":"Only one possible target (the camel) for all three phrases. From 2.0 to 6.0 s the camel fills the frame and the head is out of frame. The answer describes the second half of the clip (first half: walking)."})

# 134
woman={0.0:(0,0.08,0.47,0.72),0.5:(0,0.08,0.32,0.74),1.0:(0,0.27,0.47,0.71),1.5:(0,0.08,0.50,0.42),2.0:(0,0.3,0.41,0.58),
2.5:(0,0.37,0.48,0.52),3.0:(0,0.5,0.45,0.4),3.5:(0,0,0.53,0.78),4.0:(0,0.15,0.55,0.27),4.5:(0,0.38,0.38,0.42),5.0:(0,0.49,0.24,0.38),
8.5:(0.27,0.52,0.22,0.31),9.0:(0.27,0.52,0.23,0.41),9.5:(0.27,0.53,0.22,0.42),10.0:(0.27,0.54,0.23,0.33)}
man={0.0:(0.66,0,0.34,0.48),0.5:(0.62,0,0.38,0.47),1.0:(0.40,0,0.60,0.27),1.5:(0.65,0.2,0.35,0.45),2.0:(0.63,0.32,0.37,0.3),
2.5:(0.72,0.37,0.28,0.33),3.0:(0.45,0.45,0.55,0.37),3.5:(0.56,0.13,0.44,0.55),4.0:(0.56,0.05,0.44,0.38),4.5:(0.80,0.33,0.20,0.32),
5.0:(0.80,0.45,0.20,0.37),5.5:(0.67,0.27,0.33,0.47),6.0:(0.75,0.27,0.25,0.28),6.5:(0.55,0.35,0.45,0.43),7.0:(0.36,0.28,0.64,0.70),
7.5:(0,0.50,1,0.48),8.0:(0,0.5,1,0.4),8.5:(0.49,0.52,0.25,0.31),9.0:(0.50,0.52,0.24,0.41),9.5:(0.49,0.53,0.27,0.43),10.0:(0.50,0.54,0.27,0.33)}
lamp={7.0:(0.57,0,0.18,0.14),7.5:(0.58,0,0.18,0.14),8.0:(0.58,0,0.18,0.14),8.5:(0.41,0.38,0.18,0.14),9.0:(0.41,0.38,0.18,0.14),
9.5:(0.41,0.39,0.18,0.14),10.0:(0.41,0.40,0.18,0.14)}
save({"mediaId":134,"level":"A","keyWord":"camping","defaultVoice":"female",
"taps":[{"phrase":"to use a hammer","target":"the woman","voice":"female","keys":keys(woman,21)},
{"phrase":"to lie in the tent","target":"the man","voice":"male","keys":keys(man,21)},
{"phrase":"to hang in the tent","target":"the lamp","voice":"female","keys":keys(lamp,21)}],
"stillS":9.0,
"nouns":[{"word":"a tent","x":0.5,"y":0.46,"voice":"female"},{"word":"trees","x":0.5,"y":0.15,"voice":"female"},
{"word":"grass","x":0.5,"y":0.9,"voice":"female"}],
"question":"What are the two people doing?",
"answer":["They","are","camping","in","the","forest."],"answerVoice":"female",
"notes":"Many cuts. The woman uses the hammer only around 3.0-3.5 s (close-up: her hand from the left holds the hammer, the man's hands on the right hold the pole). At 4.0 s only hands are visible: left hand = woman, right hands = man. The lamp is large at 7.0-8.0 s and very small inside the tent at 8.5-10.0 s (box just above the two heads). Only 3 nouns: there are two bags and two cups, so they were left out."})

# 135
m={}
for t,y in [(0.0,0.08),(0.5,0.08),(1.0,0.09),(1.5,0.0),(6.5,0.05),(7.0,0.07),(7.5,0.08),(8.0,0.07),(8.5,0.07),(9.0,0.09),(9.5,0.15),
(10.0,0.13),(10.5,0.1),(11.0,0.1),(11.5,0.1),(12.0,0.09),(12.5,0.09),(13.0,0.08),(13.5,0.08),(14.0,0.1),(14.5,0.03),(15.0,0.04)]:
    m[t]=(0,y,1,round(1-y,2))
for t,h in [(2.0,0.82),(2.5,0.84),(3.0,0.86),(3.5,0.86),(4.0,0.86)]: m[t]=(0,0,1,h)
ph={2.0:(0.52,0.82,0.48,0.18),2.5:(0.52,0.84,0.48,0.16),3.0:(0.54,0.86,0.46,0.14),3.5:(0.56,0.86,0.44,0.14),4.0:(0.56,0.86,0.30,0.14),
4.5:(0,0,1,1),5.0:(0,0,1,1),5.5:(0,0,1,1),6.0:(0,0,1,1)}
mk=keys(m,31)
save({"mediaId":135,"level":"B","keyWord":"cancel","defaultVoice":"male",
"taps":[{"phrase":"to clench his fist","target":"the man","voice":"male","keys":mk},
{"phrase":"to grin with delight","target":"the man","voice":"male","keys":mk},
{"phrase":"to display a text message","target":"the smartphone","voice":"male","keys":keys(ph,31)}],
"stillS":3.0,
"nouns":[{"word":"curly hair","x":0.45,"y":0.12,"voice":"male"},{"word":"a sweater","x":0.4,"y":0.6,"voice":"male"},
{"word":"a smartphone","x":0.72,"y":0.95,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","grinning","and","clenching","his","fist."],"answerVoice":"male",
"notes":"4.5-6.0 s: close-up of the smartphone, it fills the frame; only the man's fingertips are at the edges, so the man is 'off' there. 2.0-4.0 s the smartphone lies in his lap at the bottom right (small box, man's box ends above it). At 1.5 s and 6.5-7.5 s only a dark edge of the phone is visible: phone 'off'. The key word (verb 'cancel') is only readable in the message on the screen, so it is not in the answer. Only 3 nouns."})

# 136
candle={0.0:(0.38,0.15,0.28,0.68),0.5:(0.36,0.1,0.28,0.73),1.0:(0.40,0.15,0.24,0.77),1.5:(0.40,0.15,0.24,0.77),2.0:(0.39,0.17,0.24,0.66),
2.5:(0.40,0.2,0.24,0.63),3.0:(0.40,0.27,0.22,0.63),3.5:(0.40,0.32,0.21,0.57),4.0:(0.44,0.37,0.18,0.40),4.5:(0.45,0.4,0.18,0.4),
5.0:(0.46,0.46,0.18,0.43),5.5:(0.46,0.46,0.18,0.43),6.0:(0.46,0.45,0.18,0.39),6.5:(0.46,0.45,0.18,0.39),7.0:(0.46,0.47,0.18,0.47),
7.5:(0.47,0.53,0.18,0.41),8.0:(0.43,0.56,0.18,0.30),8.5:(0.44,0.60,0.18,0.27),9.0:(0.43,0.61,0.18,0.33),9.5:(0.43,0.60,0.18,0.34),
10.0:(0.43,0.60,0.18,0.26)}
wom={2.5:(0,0,0.22,0.5),3.0:(0,0,0.29,0.62),3.5:(0,0,0.39,0.63),4.0:(0,0.02,0.44,0.6),4.5:(0,0.08,0.45,0.56),5.0:(0,0.12,0.46,0.56),
5.5:(0,0.12,0.46,0.56),6.0:(0,0.12,0.46,0.55),6.5:(0,0.12,0.46,0.55),7.0:(0,0.12,0.45,0.62),7.5:(0,0.14,0.47,0.62),
8.0:(0,0.15,0.42,0.6),8.5:(0,0.15,0.40,0.6),9.0:(0,0.13,0.37,0.67),9.5:(0,0.1,0.32,0.72),10.0:(0,0.15,0.18,0.56)}
cat={8.5:(0.40,0.46,0.20,0.14),9.0:(0.37,0.47,0.31,0.14),9.5:(0.34,0.46,0.38,0.14),10.0:(0.33,0.46,0.40,0.14)}
save({"mediaId":136,"level":"A","keyWord":"candle","defaultVoice":"female",
"taps":[{"phrase":"to burn on the table","target":"the candle","voice":"female","keys":keys(candle,21)},
{"phrase":"to have long hair","target":"the woman","voice":"female","keys":keys(wom,21)},
{"phrase":"to lie on a bench","target":"the cat","voice":"female","keys":keys(cat,21)}],
"stillS":9.5,
"nouns":[{"word":"a candle","x":0.52,"y":0.72,"voice":"female"},{"word":"a cat","x":0.5,"y":0.55,"voice":"female"},
{"word":"smoke","x":0.56,"y":0.15,"voice":"female"},{"word":"a woman","x":0.16,"y":0.33,"voice":"female"}],
"question":"What is burning on the table?",
"answer":["A","candle","is","burning","on","the","table."],"answerVoice":"female",
"notes":"The woman and the man do the same actions (lean in, blow), so the woman's phrase is a state (long plaited hair; the man's is short). The woman is 'off' until 2.0 s (only a blurred shoulder). The cat is clearly visible only from 8.5 s, small, on the bench behind the candle; its box sits directly above the candle's box. The candle burns until about 7.0 s, then it is blown out."})
