import json
OFF='off'
def keys(times, d):
    out=[]
    for t in times:
        v=d.get(t,OFF)
        if v==OFF: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
T5=[i*0.5 for i in range(11)]
T10=[i*0.5 for i in range(21)]
def save(c): json.dump(c,open(f'content/{c["mediaId"]}.json','w'),indent=1,ensure_ascii=False)

# 507
girl={0.0:(0,0.10,0.62,0.70),0.5:(0,0.10,0.65,0.70),1.0:(0,0.10,0.66,0.72),1.5:(0,0.10,0.67,0.72),
 2.0:(0,0.10,0.68,0.70),2.5:(0,0.10,0.67,0.72),3.0:(0,0.10,0.69,0.75),3.5:(0,0.07,0.81,0.85),
 4.0:(0,0.04,0.86,0.96),4.5:(0,0.03,0.91,0.97),5.0:(0,0.02,0.97,0.98)}
fly={0.0:(0.63,0.45,0.25,0.17),0.5:(0.66,0.45,0.22,0.17),1.0:(0.67,0.45,0.22,0.17),1.5:(0.68,0.45,0.21,0.17),
 2.0:(0.69,0.45,0.20,0.17),2.5:(0.68,0.45,0.21,0.18),3.0:(0.70,0.40,0.27,0.20),3.5:(0.82,0.22,0.18,0.18)}
save({"mediaId":507,"level":"B","keyWord":"observe","defaultVoice":"female",
 "taps":[
  {"phrase":"to observe an insect closely","target":"the girl","voice":"female","keys":keys(T5,girl)},
  {"phrase":"to perch on a reed","target":"the dragonfly","voice":"female","keys":keys(T5,fly)},
  {"phrase":"to crouch beside a stream","target":"the girl","voice":"female","keys":keys(T5,girl)}],
 "stillS":1.0,
 "nouns":[{"word":"a magnifying glass","x":0.50,"y":0.46,"voice":"female"},
  {"word":"a dragonfly","x":0.76,"y":0.55,"voice":"female"},
  {"word":"a stream","x":0.60,"y":0.89,"voice":"female"},
  {"word":"a ponytail","x":0.20,"y":0.24,"voice":"female"}],
 "question":"What is the girl doing?",
 "answer":["She","is","observing","a","dragonfly","through","a","magnifying","glass."],
 "answerVoice":"female",
 "notes":"Dragonfly flies off at 3.0 and leaves the frame after 3.5 (off from 4.0). Girl and dragonfly boxes split at the lens edge; the wing is partly behind the lens. The plant is a cattail; 'reed' used as the more common word. Glass and dragonfly pills are close (0.09 in y)."})

# 508
woman={3.5:(0.70,0.24,0.30,0.76),4.0:(0.58,0.32,0.42,0.68),4.5:(0.55,0.34,0.45,0.66),5.0:(0.54,0.32,0.46,0.68),
 5.5:(0.53,0.30,0.47,0.70),6.0:(0.36,0.10,0.64,0.90),6.5:(0.66,0.69,0.34,0.29),7.0:(0.55,0.68,0.45,0.28),
 7.5:(0.73,0.47,0.27,0.21),8.0:(0.74,0.44,0.26,0.24),8.5:(0.70,0.44,0.30,0.22),9.0:(0.74,0.46,0.26,0.20),
 9.5:(0.78,0.46,0.22,0.20),10.0:(0.82,0.47,0.18,0.14)}
man={7.5:(0.82,0.33,0.18,0.14),8.0:(0.78,0.28,0.22,0.16),8.5:(0.70,0.30,0.30,0.14),9.0:(0.74,0.32,0.26,0.14),
 9.5:(0.78,0.32,0.22,0.14),10.0:(0.80,0.33,0.20,0.14)}
dol={6.5:(0.46,0.49,0.36,0.19),7.0:(0.26,0.44,0.46,0.22),7.5:(0.17,0.36,0.55,0.28),8.0:(0.28,0.42,0.44,0.17),
 8.5:(0.08,0.46,0.58,0.24),9.0:(0.05,0.46,0.60,0.22),9.5:(0.32,0.44,0.32,0.18),10.0:(0.31,0.43,0.33,0.18)}
save({"mediaId":508,"level":"A","keyWord":"ocean","defaultVoice":"female",
 "taps":[
  {"phrase":"to jump out of the water","target":"the dolphins","voice":"female","keys":keys(T10,dol)},
  {"phrase":"to wear a yellow jacket","target":"the woman","voice":"female","keys":keys(T10,woman)},
  {"phrase":"to wear a red jacket","target":"the man","voice":"male","keys":keys(T10,man)}],
 "stillS":7.5,
 "nouns":[{"word":"the sky","x":0.45,"y":0.14,"voice":"female"},
  {"word":"the ocean","x":0.30,"y":0.36,"voice":"female"},
  {"word":"dolphins","x":0.47,"y":0.50,"voice":"female"},
  {"word":"a boat","x":0.76,"y":0.86,"voice":"female"}],
 "question":"What are the dolphins doing?",
 "answer":["They","are","jumping","out","of","the","ocean."],
 "answerVoice":"female",
 "notes":"No people or dolphins before 3.5 (only sea and boat). Two state phrases (jackets) because both people point/lean and cheer; the man is only an arm and head at the right edge from 7.5. Woman at 6.5-7.0 is only her arm (hair at the edge left out to keep clear of the dolphins). At 8.0-10.0 man and woman overlap, boxes split between his red sleeve and her head. Dolphins at 6.0 are unclear under water: off."})

# 509
W=(0,0,0.62,0.36)
woman={0.0:W,0.5:(0,0,0.62,0.34),1.0:W,1.5:W,2.0:(0,0,0.60,0.33),2.5:(0,0,0.60,0.32),3.0:(0,0,0.60,0.32),
 3.5:(0,0,0.60,0.30),4.0:(0,0,0.56,0.32),4.5:(0,0,0.60,0.52),5.0:(0,0,0.50,0.36),5.5:(0,0,0.38,0.66),
 6.0:(0,0,0.31,0.63),6.5:(0,0,0.28,0.56),7.0:(0,0,0.11,0.42),7.5:(0,0.05,0.24,0.65),8.0:(0,0,0.22,0.65),
 8.5:(0,0,0.13,0.72),9.0:(0,0.08,0.28,0.72),9.5:(0,0.13,0.29,0.65),10.0:(0,0.18,0.42,0.54)}
man={5.5:(0.39,0,0.61,0.63),6.0:(0.32,0,0.68,0.60),6.5:(0.30,0,0.70,0.74),7.0:(0.11,0,0.89,0.72),
 7.5:(0.25,0,0.75,0.92),8.0:(0.23,0,0.77,0.88),8.5:(0.14,0,0.86,0.90),9.0:(0.29,0,0.71,0.88),
 9.5:(0.38,0.10,0.62,0.75),10.0:(0.44,0.17,0.56,0.67)}
save({"mediaId":509,"level":"A","keyWord":"oil","defaultVoice":"male",
 "taps":[
  {"phrase":"to pour the oil","target":"the woman","voice":"female","keys":keys(T10,woman)},
  {"phrase":"to dip bread in oil","target":"the man","voice":"male","keys":keys(T10,man)},
  {"phrase":"to eat a piece of bread","target":"the man","voice":"male","keys":keys(T10,man)}],
 "stillS":8.5,
 "nouns":[{"word":"bread","x":0.55,"y":0.66,"voice":"male"},
  {"word":"oil","x":0.42,"y":0.88,"voice":"male"},
  {"word":"tomatoes","x":0.12,"y":0.74,"voice":"male"},
  {"word":"a window","x":0.35,"y":0.20,"voice":"male"}],
 "question":"What is the man eating?",
 "answer":["He","is","eating","bread","with","oil."],
 "answerVoice":"male",
 "notes":"0.0-5.0: only the woman's white shirt and her hand (bottle, tomato) are in the picture, no face; her box covers shirt + hand. The pouring hand at 0-2.5 is taken as hers (she pours with a white sleeve at 5.5-6.0). From 7.0 she is a narrow strip at the left edge; at 7.0 her box is only 0.11 wide. Bread and tomatoes pills are close in y (0.08) but 0.43 apart in x."})

# 511
man={0.0:(0,0,1,0.65),0.5:(0,0,1,0.68),1.0:(0,0,1,0.68),1.5:(0,0,1,0.70),2.0:(0,0,1,0.68),2.5:(0,0,1,0.62),
 3.0:(0,0,1,0.80),3.5:(0,0,0.97,0.86),4.0:(0,0.02,0.88,0.85),4.5:(0,0.08,0.83,0.80),5.0:(0,0.12,0.67,0.75),
 5.5:(0,0.12,0.52,0.75),6.0:(0,0.12,0.76,0.72),6.5:(0,0.10,0.85,0.72),7.0:(0,0.10,0.86,0.80),
 7.5:(0,0.10,1,0.80),8.0:(0,0.08,1,0.80),8.5:(0,0.08,0.85,0.80),9.0:(0,0.08,0.78,0.80),
 9.5:(0,0.10,0.72,0.75),10.0:(0,0.12,0.67,0.56)}
woman={4.0:(0.89,0.36,0.11,0.30),4.5:(0.84,0.26,0.16,0.48),5.0:(0.68,0.26,0.32,0.58),5.5:(0.57,0.26,0.43,0.60),
 6.0:(0.77,0.28,0.23,0.44),6.5:(0.86,0.28,0.14,0.46),7.0:(0.87,0.30,0.13,0.56),8.5:(0.86,0.38,0.14,0.34),
 9.0:(0.79,0.23,0.21,0.54),9.5:(0.73,0.23,0.27,0.55),10.0:(0.68,0.23,0.32,0.42)}
save({"mediaId":511,"level":"A","keyWord":"onion","defaultVoice":"male",
 "taps":[
  {"phrase":"to cut an onion","target":"the man","voice":"male","keys":keys(T10,man)},
  {"phrase":"to put on goggles","target":"the man","voice":"male","keys":keys(T10,man)},
  {"phrase":"to clap her hands","target":"the woman","voice":"female","keys":keys(T10,woman)}],
 "stillS":10.0,
 "nouns":[{"word":"an onion","x":0.45,"y":0.67,"voice":"male"},
  {"word":"goggles","x":0.38,"y":0.27,"voice":"male"},
  {"word":"a window","x":0.30,"y":0.11,"voice":"male"},
  {"word":"a woman","x":0.80,"y":0.42,"voice":"female"}],
 "question":"What is the man cutting?",
 "answer":["He","is","cutting","an","onion."],
 "answerVoice":"male",
 "notes":"Both cry, so no crying phrase. The woman holds her hands together and claps only at 9.0-10.0; earlier she cries with a hand at her mouth. She is a thin strip at the right edge at 3.5, 7.5 and 8.0 (off there) and narrow at 4.0-4.5, 6.5-7.0, 8.5. At 6.0-7.0 the man's hands with the goggles are in front of her; boxes split by x. 'goggles' may be above A level but is the visible object of the clip."})
