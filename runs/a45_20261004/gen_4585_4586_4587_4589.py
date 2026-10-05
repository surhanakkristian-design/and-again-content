import json, sys
def keys(times, d):
    out=[]
    for t in times:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]
def tap(p,tg,v,k): return {"phrase":p,"target":tg,"voice":v,"keys":k}
def save(o):
    json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# ---------- 4585
t=T(25)
w={0.0:(0.30,0.18,0.42,0.71),0.5:(0.33,0.16,0.39,0.72),1.0:(0.30,0.15,0.45,0.85),1.5:(0.30,0.12,0.50,0.88),
2.0:(0.25,0.10,0.66,0.80),2.5:(0.22,0.08,0.75,0.82),3.0:(0.51,0.42,0.21,0.29),3.5:(0.46,0.41,0.24,0.32),
4.0:(0.46,0.39,0.24,0.37),4.5:(0.40,0.38,0.31,0.41),5.0:(0.46,0.49,0.24,0.47),5.5:(0.38,0.47,0.28,0.53),
6.0:(0.39,0.47,0.18,0.20),6.5:(0.42,0.48,0.18,0.20),7.0:(0.42,0.48,0.18,0.42),7.5:(0.38,0.48,0.18,0.20),
8.0:(0.35,0.47,0.21,0.35),8.5:(0.36,0.47,0.22,0.37),9.0:(0.35,0.48,0.26,0.50),9.5:(0.37,0.47,0.28,0.52),
10.0:(0.37,0.44,0.30,0.48),10.5:(0.38,0.43,0.33,0.54),11.0:(0.33,0.43,0.40,0.57),11.5:(0.27,0.29,0.54,0.68),
12.0:(0.35,0.37,0.56,0.63)}
c={4.5:(0.0,0.40,0.20,0.32),5.0:(0.20,0.41,0.26,0.41),5.5:(0.66,0.41,0.18,0.35)}
a={6.0:(0.0,0.0,0.90,0.47),6.5:(0.0,0.0,0.95,0.48),7.0:(0.0,0.0,0.95,0.48),7.5:(0.0,0.0,0.95,0.48),
8.0:(0.0,0.0,0.95,0.47),8.5:(0.0,0.0,0.97,0.47),9.0:(0.0,0.0,0.95,0.48),9.5:(0.0,0.0,0.97,0.47),
10.0:(0.02,0.0,0.94,0.44),10.5:(0.02,0.0,0.96,0.43),11.0:(0.0,0.0,0.97,0.43),11.5:(0.0,0.0,0.97,0.29),
12.0:(0.03,0.0,0.94,0.37)}
save({"mediaId":4585,"level":"B","keyWord":"crossing","defaultVoice":"female",
"taps":[tap("to clutch a long baguette","the woman","female",keys(t,w)),
        tap("to pedal past the café","the cyclist","female",keys(t,c)),
        tap("to tower over the crowd","the arch","female",keys(t,a))],
"stillS":4.0,
"nouns":[{"word":"a crossing","x":0.40,"y":0.80,"voice":"female"},
         {"word":"a traffic light","x":0.67,"y":0.30,"voice":"female"},
         {"word":"an awning","x":0.82,"y":0.41,"voice":"female"},
         {"word":"a street lamp","x":0.74,"y":0.11,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","clutching","a","baguette","on","the","crossing."],
"answerVoice":"female",
"notes":"Cyclist is visible only at 4.5-5.5 s (three frames). In the crowd shot the woman is partly hidden at 6.0-7.5 s; her box there is the minimum size on her beret/torso. Arch box is cut above the woman's box at 11.5/12.0."})

# ---------- 4586
t=T(21)
w={0.0:(0.38,0.33,0.24,0.34),0.5:(0.32,0.32,0.31,0.38),1.0:(0.36,0.32,0.28,0.53),1.5:(0.23,0.31,0.43,0.60),
2.0:(0.25,0.30,0.46,0.56),2.5:(0.33,0.25,0.41,0.75),3.0:(0.20,0.17,0.60,0.83),3.5:(0.42,0.36,0.18,0.33),
4.0:(0.42,0.36,0.18,0.22),4.5:(0.43,0.36,0.18,0.20),5.0:(0.42,0.36,0.18,0.20),5.5:(0.42,0.37,0.18,0.25),
6.0:(0.42,0.35,0.21,0.30),6.5:(0.40,0.35,0.26,0.35),7.0:(0.39,0.36,0.30,0.56),7.5:(0.37,0.36,0.26,0.35),
8.0:(0.30,0.36,0.38,0.52),8.5:(0.27,0.36,0.53,0.64),9.0:(0.32,0.27,0.60,0.73),9.5:(0.60,0.20,0.40,0.80),
10.0:(0.62,0.17,0.38,0.83)}
c={1.0:(0.76,0.37,0.24,0.33),1.5:(0.66,0.36,0.22,0.34),2.5:(0.15,0.33,0.18,0.25),3.0:(0.0,0.33,0.20,0.22)}
a={3.5:(0.22,0.10,0.56,0.26),4.0:(0.23,0.10,0.54,0.26),4.5:(0.23,0.10,0.54,0.26),5.0:(0.23,0.10,0.54,0.26),
5.5:(0.22,0.10,0.54,0.27),6.0:(0.20,0.09,0.55,0.26),6.5:(0.20,0.09,0.55,0.26),7.0:(0.18,0.09,0.55,0.27),
7.5:(0.26,0.14,0.49,0.22),8.0:(0.26,0.13,0.48,0.23),8.5:(0.26,0.13,0.48,0.23),9.0:(0.24,0.12,0.48,0.15),
9.5:(0.26,0.15,0.34,0.30),10.0:(0.26,0.15,0.36,0.27)}
save({"mediaId":4586,"level":"B","keyWord":"crosswalk","defaultVoice":"female",
"taps":[tap("to grin at the camera","the woman","female",keys(t,w)),
        tap("to pedal past the café","the cyclist","female",keys(t,c)),
        tap("to loom in the distance","the arch","female",keys(t,a))],
"stillS":8.5,
"nouns":[{"word":"a crosswalk","x":0.22,"y":0.80,"voice":"female"},
         {"word":"an arch","x":0.50,"y":0.22,"voice":"female"},
         {"word":"a baguette","x":0.67,"y":0.58,"voice":"female"},
         {"word":"a street lamp","x":0.80,"y":0.33,"voice":"female"}],
"question":"What is the woman carrying?",
"answer":["She","is","carrying","a","baguette","across","the","crosswalk."],
"answerVoice":"female",
"notes":"Cyclist: visible 1.0-1.5 s and 2.5-3.0 s, hidden behind the woman at 2.0 s. At 9.5/10.0 s the woman turns away close to the lens and overlaps the arch: her box starts at her head (x 0.60/0.62), so the baguette tip on the left is outside it. In the crowd shot (4.0-5.5 s) she is small and partly hidden."})

# ---------- 4587
t=T(19)
m={0.0:(0.0,0.27,0.95,0.73),0.5:(0.0,0.29,0.76,0.71),1.0:(0.0,0.30,0.67,0.70),1.5:(0.0,0.30,0.64,0.70),
2.0:(0.0,0.31,0.65,0.69),2.5:(0.0,0.31,0.67,0.69),3.0:(0.0,0.30,0.67,0.70),3.5:(0.0,0.31,0.61,0.69),
4.0:(0.0,0.29,0.74,0.71),4.5:(0.0,0.29,0.72,0.71),5.0:(0.0,0.30,0.77,0.70),5.5:(0.0,0.29,0.77,0.71),
6.0:(0.0,0.28,0.78,0.72),6.5:(0.0,0.30,0.80,0.70),7.0:(0.0,0.26,0.93,0.74),7.5:(0.0,0.30,0.88,0.70),
8.0:(0.0,0.24,0.85,0.76),8.5:(0.0,0.27,0.84,0.73),9.0:(0.0,0.27,0.82,0.73)}
s={0.5:(0.76,0.13,0.24,0.50),1.0:(0.67,0.20,0.26,0.44),1.5:(0.64,0.22,0.24,0.42),2.0:(0.65,0.21,0.24,0.44),
2.5:(0.67,0.20,0.26,0.45),3.0:(0.67,0.19,0.25,0.46),3.5:(0.61,0.17,0.27,0.45)}
mk=keys(t,m)
save({"mediaId":4587,"level":"A","keyWord":"cyclist","defaultVoice":"male",
"taps":[tap("to sit on a bike","the man","male",mk),
        tap("to look at the cars","the man","male",mk),
        tap("to stand in the grass","the sign","male",keys(t,s))],
"stillS":6.0,
"nouns":[{"word":"a cyclist","x":0.20,"y":0.60,"voice":"male"},
         {"word":"a car","x":0.72,"y":0.50,"voice":"male"},
         {"word":"a bike","x":0.62,"y":0.88,"voice":"male"},
         {"word":"the sky","x":0.45,"y":0.14,"voice":"male"}],
"question":"What is the cyclist looking at?",
"answer":["He","is","looking","at","the","cars."],
"answerVoice":"male",
"notes":"Only two targets: the man fills the frame diagonally, so a car or the far crowd as a target would have forced cutting his box in most frames; the cars change from shot to shot. 'to look at the cars' is true for shots 2 and 3 (4.0 s on); in shot 1 he looks at the sign. The sign phrase is a state (a sign has no action). Man's box is trimmed on the right in shot 1 where his hand meets the sign's box."})

# ---------- 4589
t=T(19)
w={0.0:(0.43,0.35,0.23,0.34),0.5:(0.43,0.33,0.24,0.39),1.0:(0.42,0.32,0.27,0.56),1.5:(0.39,0.30,0.29,0.61),
2.0:(0.41,0.30,0.30,0.55),2.5:(0.15,0.24,0.85,0.76),3.0:(0.16,0.25,0.74,0.75),3.5:(0.17,0.24,0.80,0.76),
4.0:(0.11,0.24,0.76,0.76),4.5:(0.19,0.23,0.74,0.77),5.0:(0.23,0.23,0.57,0.77),5.5:(0.37,0.37,0.28,0.41),
6.0:(0.41,0.45,0.20,0.24),6.5:(0.42,0.46,0.18,0.17),7.0:(0.41,0.46,0.18,0.14),7.5:(0.40,0.45,0.18,0.14),
8.0:(0.40,0.43,0.18,0.14),8.5:(0.40,0.42,0.18,0.14),9.0:(0.40,0.43,0.18,0.14)}
v={0.0:(0.07,0.35,0.35,0.24),0.5:(0.07,0.35,0.35,0.23),1.0:(0.10,0.35,0.32,0.24),1.5:(0.10,0.34,0.29,0.23),
2.0:(0.15,0.34,0.26,0.21)}
g={3.0:(0.74,0.0,0.20,0.14),3.5:(0.69,0.0,0.20,0.15),4.0:(0.66,0.0,0.20,0.17),4.5:(0.63,0.03,0.19,0.16),
5.0:(0.59,0.06,0.18,0.15)}
save({"mediaId":4589,"level":"B","keyWord":"pedestrian","defaultVoice":"female",
"taps":[tap("to stride towards the camera","the woman","female",keys(t,w)),
        tap("to idle at the red light","the black van","female",keys(t,v)),
        tap("to show a green figure","the walk signal","female",keys(t,g))],
"stillS":1.0,
"nouns":[{"word":"a pedestrian","x":0.58,"y":0.52,"voice":"female"},
         {"word":"a van","x":0.27,"y":0.43,"voice":"female"},
         {"word":"a manhole cover","x":0.20,"y":0.61,"voice":"female"},
         {"word":"a bicycle","x":0.85,"y":0.43,"voice":"female"}],
"question":"What is the woman in coral doing?",
"answer":["She","is","striding","over","the","pedestrian","crossing."],
"answerVoice":"female",
"notes":"Van: keys only 0.0-2.0 s; at 2.5-3.0 s it is mostly hidden behind the woman / another walker (its box would overlap hers), and in the aerial shot there are two black cars. Walk signal (green figure) is in the picture only 3.0-5.0 s. In the aerial crowd frames (7.0-9.0 s) the woman is tiny (coral dot in the centre), box = minimum size."})
