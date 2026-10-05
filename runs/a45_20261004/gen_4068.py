import json
# t: (woman x0, woman top, split y, shark x0, shark bottom)
D={0.0:(0.40,0.34,0.47,0.04,0.70),0.5:(0.40,0.34,0.47,0.05,0.69),1.0:(0.41,0.40,0.50,0.07,0.71),1.5:(0.43,0.39,0.50,0.09,0.72),
2.0:(0.44,0.40,0.50,0.11,0.72),2.5:(0.45,0.41,0.50,0.11,0.74),3.0:(0.45,0.41,0.50,0.10,0.74),3.5:(0.45,0.40,0.50,0.09,0.75),
4.0:(0.44,0.40,0.49,0.08,0.72),4.5:(0.44,0.39,0.49,0.08,0.72),5.0:(0.45,0.40,0.49,0.09,0.74),5.5:(0.45,0.40,0.49,0.09,0.74),
6.0:(0.46,0.38,0.48,0.08,0.72),6.5:(0.47,0.37,0.48,0.06,0.74),7.0:(0.48,0.38,0.49,0.03,0.75),7.5:(0.47,0.37,0.49,0.02,0.75),
8.0:(0.48,0.36,0.47,0.01,0.72),8.5:(0.48,0.35,0.48,0.05,0.72),9.0:(0.49,0.35,0.50,0.04,0.77),9.5:(0.48,0.34,0.50,0.04,0.77),
10.0:(0.36,0.33,0.47,0.04,0.76),10.5:(0.34,0.33,0.47,0.04,0.84),11.0:(0.34,0.34,0.48,0.06,0.99),11.5:(0.34,0.34,0.48,0.03,0.77),
12.0:(0.35,0.32,0.46,0.02,0.71),12.5:(0.36,0.32,0.46,0.04,0.72),13.0:(0.38,0.33,0.47,0.07,0.93)}
r=lambda v:round(v,2)
wk=[{"t":t,"x":a,"y":b,"w":r(1-a),"h":r(s-b)} for t,(a,b,s,c,e) in D.items()]
sk=[{"t":t,"x":c,"y":s,"w":r(1-c),"h":r(e-s)} for t,(a,b,s,c,e) in D.items()]
d={"mediaId":4068,"level":"B","keyWord":"stroke","defaultVoice":"female",
"taps":[
 {"phrase":"to stroke a tiger shark","target":"the woman","voice":"female","keys":wk},
 {"phrase":"to cast a dark shadow","target":"the shark","voice":"female","keys":sk},
 {"phrase":"to glide beside a shark","target":"the woman","voice":"female","keys":wk}],
"stillS":10.0,
"nouns":[{"word":"a diver","x":0.74,"y":0.43,"voice":"female"},{"word":"a shark","x":0.30,"y":0.55,"voice":"female"},{"word":"a shadow","x":0.42,"y":0.67,"voice":"female"},{"word":"the seabed","x":0.50,"y":0.87,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","stroking","a","tiger","shark."],
"answerVoice":"female",
"notes":"Woman swims right above the shark and the two overlap in the picture: boxes are split by a horizontal line (woman above, shark below), so the shark's dorsal fin tip falls into the woman's box and her trailing legs/fins dip into the shark's box in some frames. Her hand clearly rests on the shark from about 6 s on; before that she swims close beside it. 'to cast a dark shadow': only the shark's shadow is visible on the sand."}
json.dump(d,open("content/4068.json","w"),indent=1)
