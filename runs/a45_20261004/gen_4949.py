import json
times=[i/2 for i in range(25)]
B=lambda x,y,w,h:dict(x=x,y=y,w=w,h=h)
man={0.0:B(0.38,0.40,0.26,0.34),0.5:B(0.31,0.39,0.28,0.36),1.0:B(0.31,0.40,0.22,0.48),1.5:B(0.33,0.40,0.21,0.34),
2.0:B(0.37,0.38,0.26,0.34),2.5:B(0.40,0.41,0.27,0.35),3.0:B(0.46,0.43,0.23,0.40),3.5:B(0.41,0.41,0.26,0.47),
4.0:B(0.26,0.43,0.24,0.38),4.5:B(0.28,0.43,0.22,0.38),5.0:B(0.25,0.46,0.25,0.40),5.5:B(0.28,0.46,0.20,0.40),
6.0:B(0.28,0.49,0.22,0.35),6.5:B(0.28,0.49,0.22,0.35),7.0:B(0.27,0.46,0.23,0.40),
7.5:B(0.33,0.42,0.20,0.27),8.0:B(0.30,0.40,0.22,0.26),8.5:B(0.27,0.39,0.25,0.26),9.0:B(0.31,0.42,0.24,0.34),9.5:B(0.31,0.43,0.22,0.30),
10.0:B(0.31,0.47,0.21,0.22),10.5:B(0.31,0.47,0.20,0.24),11.0:B(0.28,0.47,0.23,0.25),11.5:B(0.25,0.47,0.27,0.27),12.0:B(0.25,0.47,0.25,0.25)}
woman={1.0:B(0.53,0.44,0.10,0.22),1.5:B(0.54,0.44,0.08,0.28),3.0:B(0.33,0.43,0.13,0.34),3.5:B(0.27,0.42,0.14,0.32),
4.0:B(0.50,0.38,0.17,0.30),4.5:B(0.50,0.40,0.17,0.25),5.0:B(0.50,0.42,0.15,0.24),5.5:B(0.48,0.41,0.18,0.22),
6.0:B(0.50,0.41,0.15,0.23),6.5:B(0.50,0.43,0.16,0.19),7.0:B(0.50,0.45,0.12,0.17),
7.5:B(0.53,0.47,0.21,0.22),8.0:B(0.52,0.44,0.24,0.26),8.5:B(0.52,0.44,0.27,0.28),9.0:B(0.55,0.46,0.25,0.42),9.5:B(0.53,0.47,0.26,0.38),
10.0:B(0.52,0.47,0.21,0.28),10.5:B(0.51,0.47,0.21,0.25),11.0:B(0.51,0.47,0.25,0.25),11.5:B(0.52,0.47,0.28,0.26),12.0:B(0.50,0.47,0.24,0.27)}
mtn={4.0:B(0.0,0.34,0.25,0.14),4.5:B(0.0,0.35,0.27,0.14),5.0:B(0.0,0.37,0.24,0.14),5.5:B(0.0,0.37,0.27,0.14),
6.0:B(0.0,0.36,0.27,0.14),6.5:B(0.0,0.36,0.27,0.14),7.0:B(0.0,0.37,0.26,0.14),
7.5:B(0.0,0.33,0.32,0.22),8.0:B(0.0,0.34,0.29,0.14),8.5:B(0.0,0.32,0.26,0.14),9.0:B(0.0,0.30,0.30,0.32),9.5:B(0.0,0.25,0.30,0.30),
10.0:B(0.0,0.24,1.0,0.22),10.5:B(0.0,0.24,1.0,0.22),11.0:B(0.0,0.24,1.0,0.22),11.5:B(0.0,0.24,1.0,0.22),12.0:B(0.0,0.22,1.0,0.24)}
def keys(d): return [dict(t=t,**d[t]) if t in d else {"t":t,"off":True} for t in times]
c={"mediaId":4949,"level":"B","keyWord":"scenery","defaultVoice":"male",
"taps":[
{"phrase":"to carry a blue rucksack","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to walk behind the man","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to tower over the valley","target":"the snowy mountains","voice":"male","keys":keys(mtn)}],
"stillS":12.0,
"nouns":[{"word":"the sky","x":0.50,"y":0.10,"voice":"male"},
{"word":"snowy peaks","x":0.62,"y":0.30,"voice":"male"},
{"word":"a glacier","x":0.15,"y":0.69,"voice":"male"},
{"word":"rocks","x":0.55,"y":0.88,"voice":"male"}],
"question":"What are the hikers doing?",
"answer":["They","are","climbing","a","rocky","slope."],
"answerVoice":"male",
"notes":"Forest shots 0-3.5: the man (blue rucksack) walks in front, seen from behind; the woman is tiny behind him at 1.0-1.5 (boxes narrower than 0.18 to avoid overlap) and off at 0-0.5, 2.0-2.5. 4.0-7.0 the woman is right behind the man, boxes split at x ~0.5 (man's outstretched arm partly in her box). Mountains: hazy far range on the left only 4.0-9.5 (small boxes), the big snowy wall only from 10.0 (box above the hikers' heads). At 10-12 the hikers stand on the top raising poles, so the answer 'climbing' fits the clip's main part. Key word 'scenery' is not a placeable noun, so it is not among the nouns. defaultVoice male: mixed pair, evenId false."}
json.dump(c,open('content/4949.json','w'),indent=1)
