import json
def T(n): return [round(i*0.5,1) for i in range(n)]
def keys(n, d):
    out=[]
    for t in T(n):
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def tap(p,tg,v,k): return {"phrase":p,"target":tg,"voice":v,"keys":k}
def save(o): json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 4655
m={0.0:(0.02,0,0.88,1),0.5:(0.02,0,0.93,1),1.0:(0,0.03,1,0.97),1.5:(0,0.03,1,0.97),2.0:(0,0.05,1,0.95),
2.5:(0.05,0.02,0.95,0.98),3.0:(0.03,0.03,0.97,0.97),3.5:(0.10,0,0.90,1),4.0:(0,0,1,1),4.5:(0,0,1,1),
5.0:(0,0.02,1,0.98),5.5:(0.02,0,0.98,1),6.0:(0,0,1,1),6.5:(0,0,1,1),7.0:(0,0,1,1),7.5:(0,0,1,1),
8.0:(0.15,0,0.80,1),8.5:(0.05,0,0.90,0.78),9.0:(0.10,0,0.90,1),9.5:(0.02,0.08,0.85,0.92),10.0:(0,0.06,0.85,0.94)}
k=keys(21,m)
save({"mediaId":4655,"level":"A","keyWord":"dress","defaultVoice":"male",
"taps":[tap("to take off a T-shirt","the man","male",k),tap("to put on a shirt","the man","male",k),tap("to wear a dark suit","the man","male",k)],
"stillS":10.0,
"nouns":[{"word":"hair","x":0.37,"y":0.15,"voice":"male"},{"word":"a tie","x":0.42,"y":0.46,"voice":"male"},
{"word":"a jacket","x":0.25,"y":0.66,"voice":"male"},{"word":"pictures","x":0.72,"y":0.35,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","putting","on","a","dark","suit."],"answerVoice":"male",
"notes":"Only one real target (the man getting dressed); a second man lies in bed, small and blurred, in the background at 0.0-0.5 s and 4.0-4.5 s and does none of the phrases. Close-ups (4.0-9.0 s) show only parts of the man (legs, chest); boxes cover the visible part. Last two frames are his mirror image. Key word 'dress' is a verb, so no key-word noun."})

# 4656
w={0.0:(0,0.17,0.60,0.83),0.5:(0,0.17,0.60,0.83),1.0:(0,0.17,0.62,0.83),1.5:(0,0.16,0.60,0.84),2.0:(0,0.14,0.50,0.86),2.5:(0,0.18,0.50,0.82),
6.0:(0,0.33,0.22,0.67),6.5:(0,0.28,0.42,0.72),7.0:(0,0.33,0.42,0.67),7.5:(0,0.36,0.62,0.64),8.0:(0,0.36,0.56,0.64),8.5:(0,0.30,0.80,0.70),
9.0:(0.05,0.32,0.65,0.68),9.5:(0.10,0.33,0.68,0.67),10.0:(0.05,0.34,0.47,0.66),10.5:(0,0.35,0.45,0.60),11.0:(0,0.48,0.42,0.50),11.5:(0,0.47,0.42,0.50),12.0:(0,0.36,0.45,0.55)}
h={3.0:(0,0.37,0.40,0.63),3.5:(0,0.36,0.32,0.62),4.0:(0,0.45,0.20,0.35),4.5:(0,0.30,0.25,0.47),5.0:(0,0.38,0.18,0.30),5.5:(0,0.40,0.18,0.28)}
kw=keys(25,w); kh=keys(25,h)
save({"mediaId":4656,"level":"B","keyWord":"mount","defaultVoice":"female",
"taps":[tap("to drill into the brickwork","the woman","female",kw),tap("to drive in a screw","the hammer","female",kh),tap("to mount a wooden shelf","the woman","female",kw)],
"stillS":12.0,
"nouns":[{"word":"a brick wall","x":0.62,"y":0.20,"voice":"female"},{"word":"a shelf","x":0.62,"y":0.385,"voice":"female"},
{"word":"books","x":0.76,"y":0.52,"voice":"female"},{"word":"a tool belt","x":0.20,"y":0.64,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","mounting","wooden","shelves","on","a","brick","wall."],"answerVoice":"female",
"notes":"Hammer shot 3.0-5.5 s: the woman herself is off (only her hand); the hammer box includes the hand on the handle. At 4.0-5.5 s the hammer is mostly out of frame at the left edge (handle/hand only) - verifier may prefer 'off' there. Woman box at 0-1.5 s includes the drill she holds. Two shelves at the still: 'a shelf' sits on the upper one, 'books' on the stack on the lower one."})

# 4657
full=(0,0,1,1)
d={t:full for t in T(21)}
d.update({0.0:(0,0.03,1,0.97),0.5:(0,0.03,1,0.97),1.0:(0,0.02,1,0.98),1.5:(0,0.03,1,0.97),9.0:(0,0.10,1,0.90),9.5:(0.05,0.08,0.95,0.92),10.0:(0,0.18,1,0.82)})
k=keys(21,d)
save({"mediaId":4657,"level":"A","keyWord":"to drink","defaultVoice":"female",
"taps":[tap("to drink through a straw","the woman","female",k),tap("to hold a green coconut","the woman","female",k),tap("to open a water bottle","the woman","female",k)],
"stillS":2.5,
"nouns":[{"word":"hair","x":0.75,"y":0.12,"voice":"female"},{"word":"people","x":0.22,"y":0.33,"voice":"female"},
{"word":"a straw","x":0.58,"y":0.45,"voice":"female"},{"word":"a coconut","x":0.50,"y":0.70,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","drinking","through","a","straw."],"answerVoice":"female",
"notes":"Only one target: the woman fills the frame in every shot, so boxes are near full frame; background passers-by are blurred. 'people' = the blurred group in the street on the left at 2.5 s (weakest noun). The straw pill is narrow-target: placed on the straw between mouth and coconut. At 2.5 s another person's hand passes her the coconut from the bottom left."})

# 4659
s={0.0:(0,0.18,0.88,0.82),0.5:(0,0.18,0.90,0.82),1.0:(0,0.22,0.88,0.78),1.5:(0,0.20,0.90,0.80)}
v={2.0:(0.04,0.33,0.48,0.32),2.5:(0.05,0.33,0.48,0.32),3.0:(0.03,0.33,0.48,0.32),3.5:(0.04,0.33,0.48,0.32),4.0:(0.02,0.33,0.50,0.32),4.5:(0.05,0.33,0.48,0.32),5.0:(0.05,0.33,0.45,0.35),5.5:(0.08,0.33,0.46,0.35)}
c={8.5:(0,0.29,0.92,0.50),9.0:(0,0.28,0.92,0.52),9.5:(0,0.28,0.95,0.52),10.0:(0,0.25,1,0.57)}
save({"mediaId":4659,"level":"A","keyWord":"car","defaultVoice":"male",
"taps":[tap("to drive through the city","the man in the suit","male",keys(21,s)),tap("to drive a white van","the woman in the van","female",keys(21,v)),tap("to drive through a forest","the man in the checked shirt","male",keys(21,c))],
"stillS":8.0,
"nouns":[{"word":"the sky","x":0.45,"y":0.10,"voice":"male"},{"word":"the sea","x":0.22,"y":0.33,"voice":"male"},
{"word":"a woman","x":0.33,"y":0.64,"voice":"female"},{"word":"a car","x":0.68,"y":0.90,"voice":"male"}],
"question":"Who is driving the white van?",
"answer":["A","woman","is","driving","the","white","van."],"answerVoice":"female",
"notes":"Four shots: suit man in city traffic 0-1.5 s, woman in white van 2.0-5.5 s, couple in a parked blue convertible 6.0-8.0 s (no tap target), man in checked shirt on a forest road 8.5-10 s. All three phrases use 'to drive' but with a detail only one driver matches. Mixed group, odd id -> defaultVoice male. 'a car' pill is on the blue door of the convertible at the bottom of the still (the car fills the lower half); 'a woman' on the passenger with long hair, the man next to her is cut off at the left edge. Question is 6 words; answer subject 'A woman' -> female voice."})
