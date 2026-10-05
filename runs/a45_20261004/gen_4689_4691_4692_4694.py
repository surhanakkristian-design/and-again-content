import json
def keys(T,d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
def T(n): return [i*0.5 for i in range(n)]
def save(c): json.dump(c,open("content/%d.json"%c["mediaId"],"w"),indent=1)

# 4689
t=T(21)
man={0.0:(0,0.03,0.60,0.57),0.5:(0,0.03,0.60,0.56),1.0:(0,0.03,0.62,0.54),1.5:(0,0.06,0.63,0.48),2.0:(0,0.07,0.63,0.41),
2.5:(0,0,0.37,0.52),3.0:(0,0.07,0.30,0.70),3.5:(0,0.21,0.28,0.67),4.0:(0,0.28,0.25,0.60),4.5:(0,0.30,0.25,0.58),
5.0:(0,0.30,0.24,0.62),5.5:(0,0.28,0.25,0.64),6.0:(0,0.24,0.27,0.55),6.5:(0,0.19,0.29,0.52),7.0:(0,0.16,0.31,0.57),
7.5:(0,0.08,0.40,0.38),8.0:(0,0.02,0.45,0.46),8.5:(0,0,0.46,0.48),9.0:(0,0,0.48,0.50),9.5:(0,0.03,0.50,0.45),10.0:(0,0.04,0.52,0.42)}
whale={0.0:(0.25,0.61,0.65,0.39),0.5:(0.25,0.60,0.70,0.40),1.0:(0.28,0.57,0.72,0.43),1.5:(0.30,0.54,0.70,0.46),2.0:(0.30,0.48,0.70,0.52),
2.5:(0.37,0.19,0.63,0.73),3.0:(0.30,0.04,0.70,0.96),3.5:(0.28,0,0.72,1),4.0:(0.26,0,0.74,1),4.5:(0.26,0,0.74,1),5.0:(0.25,0,0.75,1),
5.5:(0.26,0,0.74,1),6.0:(0.28,0.06,0.72,0.94),6.5:(0.30,0.16,0.70,0.80),7.0:(0.31,0.29,0.69,0.68),7.5:(0.27,0.46,0.63,0.42),8.0:(0.30,0.50,0.68,0.28)}
save({"mediaId":4689,"level":"A","keyWord":"boat","defaultVoice":"male",
"taps":[
 {"phrase":"to point at the water","target":"the man","voice":"male","keys":keys(t,man)},
 {"phrase":"to wear a yellow coat","target":"the man","voice":"male","keys":keys(t,man)},
 {"phrase":"to come out of the water","target":"the whale","voice":"male","keys":keys(t,whale)}],
"stillS":7.0,
"nouns":[{"word":"a whale","x":0.62,"y":0.62,"voice":"male"},{"word":"mountains","x":0.66,"y":0.24,"voice":"male"},
 {"word":"a boat","x":0.13,"y":0.82,"voice":"male"},{"word":"a man","x":0.15,"y":0.42,"voice":"male"}],
"question":"What is next to the boat?",
"answer":["A","whale","is","next","to","the","boat."],
"answerVoice":"male",
"notes":"Only two targets (man, whale); the life ring overlaps the man's arm, so not used. 'to point at the water' is true only at 0.0-0.5 s (he points down at the dark shape). 'to wear a yellow coat' is a state, chosen because his other actions are short. Whale box at 0.0-1.0 s is the dark shape under water; off from 8.5 s (only foam). At 2.5 and 7.5 s man and whale are close: boxes split, the man's box loses a little of his face (2.5) / lower arm (7.5). 'a boat' pill sits on the wooden rail, the only part of the boat in the picture."})

# 4691
t=T(19)
man={0.0:(0.32,0.11,0.48,0.89),0.5:(0.16,0.07,0.72,0.93),1.0:(0.15,0,0.85,1),1.5:(0,0,1,1),2.0:(0.46,0.32,0.46,0.38),
2.5:(0,0.26,0.72,0.74),3.0:(0.15,0.23,0.48,0.77),3.5:(0.12,0.23,0.60,0.77),4.0:(0.04,0.31,0.72,0.69),4.5:(0,0.26,0.84,0.74),
5.0:(0,0.18,0.88,0.82),5.5:(0,0.11,0.76,0.89),6.0:(0,0.06,0.79,0.94),6.5:(0,0.18,0.87,0.70),7.0:(0,0.22,0.60,0.76),
7.5:(0.03,0.22,0.80,0.76),8.0:(0.02,0.21,0.90,0.68),8.5:(0,0.20,0.93,0.70),9.0:(0,0.21,0.92,0.76)}
save({"mediaId":4691,"level":"B","keyWord":"colleague","defaultVoice":"male",
"taps":[
 {"phrase":"to tap a touchscreen","target":"the young man","voice":"male","keys":keys(t,man)},
 {"phrase":"to settle down at his desk","target":"the young man","voice":"male","keys":keys(t,man)},
 {"phrase":"to clench his fists","target":"the young man","voice":"male","keys":keys(t,man)}],
"stillS":2.5,
"nouns":[{"word":"a colleague","x":0.87,"y":0.50,"voice":"male"},{"word":"a backpack","x":0.10,"y":0.56,"voice":"male"},
 {"word":"an office chair","x":0.60,"y":0.68,"voice":"male"}],
"question":"Who is the young man greeting?",
"answer":["He","is","greeting","a","colleague."],
"answerVoice":"male",
"notes":"One target for all three phrases: the bearded colleague is in the picture only at 2.5 s (and as an arm / blur at 3.0, 7.0, 7.5), and everything he clearly does (holding out a hand, holding files) the young man does too. 'to tap a touchscreen' = 0.0 s only; 'to clench his fists' = 6.0 s (small fist pump); 'to settle down at his desk' = 4.0-4.5 s. The stack of folders at 6.5-7.5 s is not in the description and unclear who hands it to whom, so not used. 'a colleague' pill is on the bearded man; no other noun names a person."})

# 4692
man={0.0:(0.55,0.45,0.45,0.30),0.5:(0.48,0.45,0.52,0.30),1.0:(0.28,0.42,0.72,0.58),1.5:(0.22,0.21,0.78,0.79),2.0:(0.45,0.24,0.55,0.76),
2.5:(0,0.07,0.84,0.93),3.0:(0,0.18,0.92,0.82),3.5:(0,0.18,0.76,0.82),4.0:(0,0.09,0.72,0.91),4.5:(0,0.20,0.93,0.80),
5.0:(0,0.16,1,0.84),5.5:(0,0.21,0.84,0.79),6.0:(0.16,0.14,0.56,0.60),6.5:(0.21,0.09,0.48,0.56),7.0:(0.24,0.05,0.44,0.86),
7.5:(0.16,0.14,0.50,0.72),8.0:(0.24,0.14,0.45,0.64),8.5:(0.29,0.10,0.40,0.67),9.0:(0.29,0.18,0.40,0.70)}
save({"mediaId":4692,"level":"A","keyWord":"product","defaultVoice":"male",
"taps":[
 {"phrase":"to carry a big box","target":"the man","voice":"male","keys":keys(t,man)},
 {"phrase":"to put cans on a shelf","target":"the man","voice":"male","keys":keys(t,man)},
 {"phrase":"to step on a box","target":"the man","voice":"male","keys":keys(t,man)}],
"stillS":2.0,
"nouns":[{"word":"a box","x":0.50,"y":0.56,"voice":"male"},{"word":"cans","x":0.30,"y":0.77,"voice":"male"},
 {"word":"a door","x":0.48,"y":0.29,"voice":"male"},{"word":"a man","x":0.83,"y":0.40,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","putting","cans","on","a","shelf."],
"answerVoice":"male",
"notes":"The clip differs from the description: 0.0-0.5 s only his hand with a card at a reader, 1.5-2.0 he lifts a box of cans over a trolley, 2.5-5.5 he puts cans on a shelf, 6.0-7.5 he drops an empty box and steps on it to flatten it, 8.0-9.0 he claps his hands clean and stands. Only one person, so one target; at 0.0-1.0 s the box covers just his arm. At 4.0-4.5 s a second hand (the camera person's) comes in from the left inside his box. Key word 'product' not used as a noun (the things are clearly cans); at 2.0 s the cans are in the trolley."})

# 4694
woman={0.0:(0,0.12,0.56,0.62),0.5:(0,0.09,0.56,0.64),1.0:(0,0.10,0.64,0.86),1.5:(0,0,0.62,0.86),2.0:(0,0,0.44,0.53),2.5:(0,0,0.30,0.45),
3.0:(0,0,0.30,0.38),3.5:(0.10,0.23,0.42,0.77),4.0:(0,0.18,0.54,0.82),4.5:(0,0.20,0.50,0.80),5.0:(0,0.20,0.50,0.80),5.5:(0,0.20,0.50,0.80),
6.0:(0,0.18,0.48,0.82),6.5:(0,0.16,0.45,0.84),7.0:(0.29,0.25,0.33,0.37),7.5:(0.18,0.25,0.56,0.36),8.0:(0.14,0.25,0.62,0.35),
8.5:(0.18,0.25,0.54,0.35),9.0:(0.30,0.25,0.33,0.47)}
man={0.0:(0.56,0.18,0.44,0.82),0.5:(0.56,0.15,0.44,0.85),1.0:(0.66,0.15,0.34,0.85),1.5:(0.65,0,0.35,1),2.0:(0.28,0.53,0.72,0.47),
2.5:(0.30,0.38,0.70,0.62),3.0:(0.30,0.38,0.70,0.62),3.5:(0.52,0.21,0.46,0.79),4.0:(0.55,0.17,0.45,0.83),4.5:(0.52,0.19,0.48,0.81),
5.0:(0.57,0.21,0.43,0.79),5.5:(0.60,0.17,0.40,0.83),6.0:(0.65,0.17,0.35,0.83),6.5:(0.68,0.12,0.32,0.88),7.0:(0.77,0.34,0.23,0.66),
7.5:(0.78,0.36,0.22,0.64),8.0:(0.77,0.33,0.23,0.64),8.5:(0.72,0.34,0.28,0.63),9.0:(0.72,0.34,0.28,0.66)}
save({"mediaId":4694,"level":"B","keyWord":"contract","defaultVoice":"female",
"taps":[
 {"phrase":"to sign a contract","target":"the young man","voice":"male","keys":keys(t,man)},
 {"phrase":"to pat his shoulder","target":"the woman in the suit","voice":"female","keys":keys(t,woman)},
 {"phrase":"to spread her arms wide","target":"the woman in the suit","voice":"female","keys":keys(t,woman)}],
"stillS":1.5,
"nouns":[{"word":"a contract","x":0.52,"y":0.80,"voice":"female"},{"word":"a coffee machine","x":0.62,"y":0.36,"voice":"female"},
 {"word":"a laptop","x":0.58,"y":0.55,"voice":"female"},{"word":"a blazer","x":0.17,"y":0.42,"voice":"female"}],
"question":"What is the young man signing?",
"answer":["He","is","signing","a","contract."],
"answerVoice":"male",
"notes":"Order in the clip: handshake (0.0-0.5), she lays the contract down and points (1.0-1.5), he signs (2.0-3.0, only his hands and the top of his head in the picture; her hand is top left), they walk into the office with her hand on his shoulder (3.5-4.5), she holds the clipboard (5.0-6.5), she presents the desk with the Welcome box, arms spread (7.5-8.5), staff clap. 'to pat his shoulder': her hand rests on his shoulder at 3.5-4.5 s. The man also claps at 8.5-9.0 like the staff, so no clapping phrase. At 7.0-9.0 s the man's box touches a seated woman colleague behind him. 'a blazer' is on the woman's jacket (the man's suit is hardly in the picture at 1.5 s)."})
