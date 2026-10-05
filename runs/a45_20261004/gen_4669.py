import json
T=[i*0.5 for i in range(25)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def tap(p,tg,v,d): return {"phrase":p,"target":tg,"voice":v,"keys":keys(d)}
def nn(l,v): return [{"word":w,"x":x,"y":y,"voice":vv or v} for (w,x,y,*r) in l for vv in [r[0] if r else None]]
def write(i,o):
    json.dump(o,open(f"content/{i}.json","w"),indent=1,ensure_ascii=False)

# 4669
W={0.0:(0.30,0.03,0.60,0.44),0.5:(0.35,0.24,0.53,0.28),1.0:None,1.5:None,2.0:(0,0.70,0.32,0.30),2.5:(0,0.60,0.36,0.38),
3.0:(0,0.66,0.40,0.34),3.5:(0,0.25,0.23,0.75),4.0:(0,0.25,0.45,0.75),4.5:(0,0.27,0.48,0.73),5.0:(0,0.27,0.60,0.73),5.5:(0,0.27,0.55,0.73),
6.0:(0,0.25,0.45,0.75),6.5:(0,0.24,0.58,0.76),7.0:(0,0.23,0.48,0.77),7.5:(0,0.20,0.45,0.80),8.0:(0,0.22,0.32,0.78),8.5:(0,0.23,0.47,0.77),
9.0:(0,0.18,0.45,0.82),9.5:(0,0.20,0.30,0.80),10.0:(0,0.18,0.27,0.82),10.5:(0,0.18,0.50,0.82),11.0:(0,0.23,0.38,0.77),11.5:(0,0.25,0.44,0.75),12.0:(0,0.27,0.27,0.73)}
S={0.0:(0,0.47,0.78,0.53),0.5:(0,0.52,0.80,0.48),1.0:(0,0.36,0.76,0.64),1.5:(0,0.30,0.76,0.70),2.0:(0.05,0.30,0.95,0.40),2.5:(0.10,0.12,0.74,0.48),
3.0:(0.12,0.42,0.70,0.24),3.5:(0.23,0.34,0.72,0.56),4.0:(0.45,0.32,0.50,0.45),4.5:(0.48,0.33,0.52,0.42),5.0:(0.60,0.36,0.36,0.58),5.5:(0.55,0.36,0.40,0.58),
6.0:(0.45,0.36,0.48,0.53),6.5:(0.58,0.37,0.36,0.58),7.0:(0.48,0.36,0.46,0.64),7.5:(0.45,0.45,0.55,0.55),8.0:(0.32,0.55,0.63,0.42),8.5:(0.47,0.44,0.50,0.56),
9.0:(0.45,0.46,0.45,0.54),9.5:(0.30,0.48,0.34,0.50),10.0:(0.27,0.40,0.37,0.46),10.5:(0.50,0.44,0.48,0.54),11.0:(0.38,0.76,0.32,0.24),11.5:(0.44,0.66,0.22,0.32),12.0:(0.27,0.66,0.25,0.32)}
write(4669,{"mediaId":4669,"level":"B","keyWord":"laundry","defaultVoice":"female",
"taps":[tap("to peg up a shirt","the woman","female",W),tap("to clutch the clean laundry","the woman","female",W),tap("to flutter in the breeze","the white shirt","female",S)],
"stillS":4.0,"nouns":nn([("a clothes peg",0.82,0.35),("laundry",0.62,0.55),("an apron",0.18,0.70),("tiles",0.65,0.88)],"female"),
"question":"What is the woman doing?","answer":["She","is","pegging","laundry","on","the","line."],"answerVoice":"female",
"notes":"Two targets that touch all the time (she handles the shirt): the boxes are split along a straight line between woman and shirt, so in several frames a part of her arm lies in the shirt box and at 2.0-3.0 s / 9.5-10.0 s only a part of her is in her own box. Woman is off at 1.0 and 1.5 s (only a sliver of hand). 'The white shirt' = the garment she pegs, takes down and holds; it flutters clearly 1.0-3.5 s. Pegging: 0-0.5 and 6-8 s; clutching the bundle 11-12 s. 'laundry' pill sits on the hanging white washing; the peg is small."})

# 4670
W={0.0:(0.10,0.26,0.80,0.74),0.5:(0.25,0.08,0.63,0.92),1.0:(0.22,0.27,0.70,0.73),1.5:(0.07,0.32,0.64,0.68),2.0:(0.12,0.29,0.76,0.71),2.5:(0.28,0.27,0.72,0.73),
6.0:(0.15,0.34,0.72,0.66),6.5:(0.14,0.35,0.76,0.65),7.0:(0.12,0.35,0.74,0.65),7.5:(0.24,0.34,0.74,0.66),8.0:(0.27,0.32,0.59,0.68),8.5:(0.24,0.30,0.69,0.70),
9.0:(0.22,0.27,0.73,0.73),9.5:(0.33,0.28,0.67,0.72),10.0:(0.30,0.33,0.65,0.67),10.5:(0.25,0.30,0.75,0.70),11.0:(0.20,0.30,0.73,0.70),11.5:(0.10,0.29,0.83,0.71),12.0:(0.15,0.29,0.78,0.71)}
write(4670,{"mediaId":4670,"level":"A","keyWord":"roof","defaultVoice":"female",
"taps":[tap("to hang up a shirt","the woman","female",W),tap("to touch a white sheet","the woman","female",W),tap("to walk on the roof","the woman","female",W)],
"stillS":5.5,"nouns":nn([("the sky",0.50,0.15),("a church",0.60,0.39),("a roof",0.62,0.57),("clothes",0.20,0.74)],"female"),
"question":"What is the woman doing?","answer":["She","is","hanging","clothes","on","the","roof."],"answerVoice":"female",
"notes":"Only one acting target (the woman), so all three phrases use her; she is off 3.0-5.5 s (city view). Her box includes the shirt she holds up. Hang up a shirt: 0-2.5 s; touch a white sheet: 6-7.5 s; walk: 6-7.5 s. The still at 5.5 s has no person; 'a roof' = the big red tiled roof in the middle (other roofs are visible further away)."})

# 4671
M={0.0:(0.36,0.16,0.64,0.36),0.5:(0.38,0.11,0.62,0.32),1.0:(0.64,0.08,0.36,0.92),1.5:(0.68,0.11,0.32,0.89),2.0:(0.70,0.13,0.30,0.87),2.5:(0,0.08,0.40,0.92),
3.0:(0,0.23,0.58,0.77),3.5:(0,0,0.42,1.0),4.0:(0,0,0.88,1.0),4.5:(0,0,0.54,1.0),8.0:(0,0.02,0.70,0.98),8.5:(0,0.01,0.40,0.99),9.0:(0,0.03,0.62,0.97),
9.5:(0,0.08,0.68,0.92),10.0:(0,0.03,0.45,0.97),10.5:(0,0.01,0.30,0.99),11.0:(0,0.03,0.45,0.25),11.5:(0,0.05,0.52,0.23),12.0:(0,0.05,0.52,0.24)}
B={0.0:(0.22,0.52,0.46,0.22),0.5:(0.20,0.43,0.48,0.30),1.0:(0.10,0.28,0.54,0.60),1.5:(0.16,0.25,0.52,0.63),2.0:(0.13,0.25,0.57,0.50),2.5:(0.40,0.26,0.57,0.54),
3.0:(0.58,0.55,0.20,0.26),3.5:(0.54,0.44,0.27,0.40),4.0:None,4.5:(0.54,0.47,0.20,0.25),5.0:(0,0.27,0.92,0.63),5.5:(0,0.18,0.66,0.72),6.0:(0,0.10,0.88,0.72),
6.5:(0,0.10,1.0,0.68),7.0:(0,0.24,0.90,0.66),7.5:(0,0.12,1.0,0.76),8.0:(0.70,0.48,0.18,0.24),8.5:(0.62,0.48,0.23,0.25),9.0:(0.64,0.62,0.21,0.24),
9.5:(0.68,0.47,0.18,0.37),10.0:(0.45,0.36,0.40,0.38),10.5:(0.30,0.30,0.63,0.52),11.0:(0.15,0.28,0.53,0.72),11.5:(0.24,0.28,0.58,0.72),12.0:(0.30,0.29,0.56,0.71)}
write(4671,{"mediaId":4671,"level":"A","keyWord":"machine","defaultVoice":"male",
"taps":[tap("to close the door","the man","male",M),tap("to hug a big blanket","the man","male",M),tap("to turn in the machine","the blanket","male",B)],
"stillS":12.0,"nouns":nn([("towels",0.62,0.15),("a man",0.16,0.62,"male"),("a machine",0.84,0.36),("a blanket",0.50,0.82)],"male"),
"question":"What is the man doing?","answer":["He","is","taking","a","blanket","out","of","the","machine."],"answerVoice":"male",
"notes":"Man and blanket touch in most frames: boxes are split along a straight line. At 0-0.5 s and 11-12 s the man's box is his head and shoulders only (the blanket covers his chest); at 1-2 s it is the right strip with his face. Blanket is off at 4.0 s (almost hidden behind his hands and the door); man is off 5.0-7.5 s (close-up of the drum). Close the door: 4.0-4.5 s; hug: 11-12 s; the blanket turns 5-7.5 s. The answer describes 9.5-10.5 s; earlier he also puts the blanket in. Two machines stand on each other at 12.0 s: the pill is on the upper one."})

# 4674
M={0.0:(0.15,0.16,0.47,0.52),0.5:(0.12,0.16,0.50,0.52),1.0:(0.02,0.16,0.55,0.56),1.5:(0,0.16,0.57,0.56),2.0:(0.02,0.16,0.52,0.46),2.5:(0.08,0.18,0.50,0.46),
3.0:(0.07,0.25,0.53,0.48),3.5:(0.05,0.28,0.60,0.52),4.0:(0.03,0.30,0.62,0.50),4.5:(0,0.34,0.58,0.52),5.0:(0,0.35,0.55,0.60),5.5:(0,0.37,0.48,0.58),
6.0:(0,0.37,0.53,0.53),6.5:(0,0.37,0.65,0.52),7.0:(0,0.38,0.58,0.56),7.5:(0.05,0.36,0.48,0.52),8.0:(0.05,0.33,0.48,0.44),8.5:(0.08,0.36,0.47,0.37),
9.0:(0.07,0.30,0.50,0.40),9.5:(0.07,0.26,0.50,0.50),10.0:(0.03,0.20,0.57,0.38),10.5:(0.08,0.20,0.62,0.45),11.0:(0.08,0.20,0.72,0.70),11.5:(0.08,0.18,0.76,0.72),12.0:(0.08,0.15,0.74,0.70)}
write(4674,{"mediaId":4674,"level":"A","keyWord":"shelf","defaultVoice":"male",
"taps":[tap("to clean a gold clock","the man","male",M),tap("to reach a high shelf","the man","male",M),tap("to wave his hand","the man","male",M)],
"stillS":4.0,"nouns":nn([("a window",0.17,0.22),("a shelf",0.75,0.32),("a man",0.22,0.55,"male"),("an armchair",0.35,0.85)],"male"),
"question":"What is the man doing?","answer":["He","is","cleaning","the","shelves."],"answerVoice":"male",
"notes":"Only one acting target (the man), all three phrases use him. Clean a gold clock: 0-2 s; reach a high shelf: 3.5-6.5 s; wave his hand (waving the dust away): 10.5-11.5 s. 'a shelf' pill sits on the edge of a shelf board full of books at 4.0 s; many shelves and clocks are visible, so 'books' and 'a clock' were left out."})
