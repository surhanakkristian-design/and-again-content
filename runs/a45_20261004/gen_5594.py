import json
def K(times, boxes):
    out=[]
    for t,b in zip(times,boxes):
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2],2),"h":round(b[3],2)})
    return out
def W(d): json.dump(d,open(f"content/{d['mediaId']}.json","w"),indent=1,ensure_ascii=False)
T8=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
# 5594
dr=K(T8,[(0.10,0.12,0.90,0.60),(0.13,0.20,0.87,0.52),(0.17,0.26,0.83,0.48),(0.21,0.31,0.79,0.42),(0.20,0.33,0.80,0.39),(0.20,0.33,0.80,0.39),(0.20,0.33,0.80,0.39),(0.22,0.33,0.78,0.39)])
W({"mediaId":5594,"level":"B","keyWord":"awesome","defaultVoice":"female",
 "taps":[{"phrase":"to perch on a ridge","target":"the dragon","voice":"female","keys":dr},
         {"phrase":"to fold its leathery wings","target":"the dragon","voice":"female","keys":dr},
         {"phrase":"to lower its horned head","target":"the dragon","voice":"female","keys":dr}],
 "stillS":2.7,
 "nouns":[{"word":"peaks","x":0.50,"y":0.17,"voice":"female"},{"word":"clouds","x":0.20,"y":0.42,"voice":"female"},
          {"word":"a dragon","x":0.68,"y":0.52,"voice":"female"},{"word":"pine trees","x":0.25,"y":0.82,"voice":"female"}],
 "question":"What is the dragon doing?",
 "answer":["The","awesome","dragon","is","perching","on","a","ridge."],
 "answerVoice":"female",
 "notes":"Only one possible target (the dragon), so all three phrases share it. Key word 'awesome' is an adjective, used in the answer. Dragon box runs to the right edge (wing leaves the frame)."})
# 94
T=[i*0.5 for i in range(19)]
F=(0,0,1,1)
man=[(0.50,0.26,0.50,0.74),F,F,None,(0.46,0,0.54,1),(0.12,0,0.88,1),(0.12,0,0.88,1),F,F,F,F,(0.50,0.18,0.50,0.82),(0.54,0.20,0.46,0.75),None,None,(0.47,0.15,0.53,0.85),(0.48,0.13,0.52,0.87),(0.56,0.22,0.44,0.78),(0.55,0.25,0.45,0.75)]
wom=[(0,0.26,0.50,0.74),None,None,(0,0.15,0.88,0.85),(0,0.20,0.46,0.80),None,None,None,None,None,None,(0,0.15,0.48,0.85),(0,0.13,0.52,0.82),F,F,(0,0.13,0.47,0.87),(0,0.10,0.48,0.90),(0,0.24,0.48,0.76),(0,0.27,0.48,0.73)]
km=K(T,man); kw=K(T,wom)
W({"mediaId":94,"level":"B","keyWord":"blink","defaultVoice":"male",
 "taps":[{"phrase":"to shed a tear","target":"the man","voice":"male","keys":km},
         {"phrase":"to grit his teeth","target":"the man","voice":"male","keys":km},
         {"phrase":"to grin in triumph","target":"the woman","voice":"female","keys":kw}],
 "stillS":0.0,
 "nouns":[{"word":"sunglasses","x":0.64,"y":0.34,"voice":"male"},{"word":"a hoop earring","x":0.30,"y":0.49,"voice":"male"},
          {"word":"milkshakes","x":0.47,"y":0.64,"voice":"male"},{"word":"car keys","x":0.72,"y":0.76,"voice":"male"}],
 "question":"What is the man trying to avoid?",
 "answer":["He","is","trying","not","to","blink."],
 "answerVoice":"male",
 "notes":"Clip of many cuts with extreme close-ups: close-ups of the man's eye/face = the man (full frame), close-ups of the woman's eye (6.5, 7.0) = the woman. 1.5 and 2.0 show a hand waved in front of his eye; by skin tone it is the woman's, boxed as the woman (doubt). 'to grin in triumph': both laugh at 8.5/9.0, but only she grins in triumph at 5.5-8.0. The blink itself falls between frames; the answer says he is trying not to blink (staring contest)."})
# 7981
L=[(0.02,0.32,0.35,0.45),(0.02,0.33,0.35,0.44),(0.02,0.33,0.36,0.50),(0,0.32,0.37,0.55),(0,0.29,0.30,0.50),(0,0.28,0.27,0.50),(0,0.29,0.30,0.60),(0,0.31,0.41,0.60)]
M=[(0.37,0.30,0.25,0.48),(0.37,0.30,0.26,0.48),(0.38,0.31,0.27,0.52),(0.38,0.29,0.30,0.50),(0.31,0.27,0.38,0.53),(0.28,0.26,0.45,0.55),(0.31,0.25,0.42,0.65),(0.42,0.23,0.29,0.50)]
J=[(0.62,0.35,0.38,0.45),(0.63,0.35,0.37,0.45),(0.65,0.38,0.35,0.48),(0.69,0.37,0.31,0.50),(0.70,0.33,0.30,0.50),(0.74,0.33,0.26,0.50),(0.74,0.33,0.26,0.65),(0.72,0.32,0.28,0.65)]
W({"mediaId":7981,"level":"B","keyWord":"sharing","defaultVoice":"male",
 "taps":[{"phrase":"to bite into a strawberry","target":"the woman with locs","voice":"female","keys":K(T8,L)},
         {"phrase":"to wear rolled-up sleeves","target":"the man","voice":"male","keys":K(T8,M)},
         {"phrase":"to offer a strawberry","target":"the woman in the jacket","voice":"female","keys":K(T8,J)}],
 "stillS":0.2,
 "nouns":[{"word":"an awning","x":0.45,"y":0.19,"voice":"male"},{"word":"a sundae","x":0.46,"y":0.69,"voice":"male"},
          {"word":"a jug","x":0.78,"y":0.84,"voice":"male"}],
 "question":"What are the three friends doing?",
 "answer":["They","are","sharing","a","sundae."],
 "answerVoice":"male",
 "notes":"All three eat from the sundae, so eating phrases fit nobody alone. The strawberry is offered (3.2) and bitten (3.7) only at the end. The man's phrase is a state (rolled-up sleeves) because no action is his alone. The three stand shoulder to shoulder: boxes are split along the lines between them and cut some arms. Background people are not targets."})
# 7145
cow=[(0.10,0.40,0.53,0.50),(0.10,0.41,0.54,0.50),(0.10,0.42,0.56,0.53),(0.10,0.44,0.58,0.33),(0.10,0.43,0.60,0.35),(0.10,0.43,0.63,0.35),(0.08,0.45,0.67,0.33),(0.08,0.45,0.67,0.33)]
mn=[(0.63,0.32,0.33,0.57),(0.64,0.32,0.34,0.58),(0.66,0.32,0.31,0.64),(0.68,0.32,0.30,0.62),(0.70,0.32,0.28,0.60),(0.73,0.32,0.27,0.55),(0.75,0.34,0.25,0.62),(0.80,0.33,0.20,0.63)]
cat=[None,None,None,(0.50,0.77,0.18,0.14),(0.52,0.78,0.18,0.14),(0.53,0.79,0.19,0.14),(0.48,0.79,0.25,0.16),(0.48,0.78,0.26,0.17)]
W({"mediaId":7145,"level":"B","keyWord":"front door","defaultVoice":"male",
 "taps":[{"phrase":"to retreat behind the door","target":"the man","voice":"male","keys":K(T8,mn)},
         {"phrase":"to snort at the man","target":"the big cow","voice":"male","keys":K(T8,cow)},
         {"phrase":"to stroll past milk bottles","target":"the cat","voice":"male","keys":K(T8,cat)}],
 "stillS":0.2,
 "nouns":[{"word":"a front door","x":0.82,"y":0.30,"voice":"male"},{"word":"a bathrobe","x":0.72,"y":0.62,"voice":"male"},
          {"word":"milk bottles","x":0.55,"y":0.75,"voice":"male"},{"word":"cobblestones","x":0.22,"y":0.93,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","retreating","behind","his","front","door."],
 "answerVoice":"male",
 "notes":"The cow box stops above the cat from 1.7 s on (the cow's lower legs are left out so the boxes do not overlap). The cat only peeks out at 1.7 s. 'the big cow' = the one at the door; the herd behind is not boxed. Cow and man overlap at the muzzle; split along x."})
