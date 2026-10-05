import json
def K(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
T10=[i*0.5 for i in range(21)]
T15=[i*0.5 for i in range(31)]
def dump(c): json.dump(c, open(f"content/{c['mediaId']}.json","w"), indent=1, ensure_ascii=False)

# ---------- 168
off_ = {2.5:(0.42,0.20,0.58,0.80),3.0:(0.45,0.18,0.55,0.82),3.5:(0.55,0.18,0.45,0.82),4.0:(0.68,0.18,0.32,0.82)}
bur = {0.0:(0.03,0.33,0.24,0.67),0.5:(0.02,0.33,0.26,0.67),1.0:(0.0,0.33,0.26,0.67),1.5:(0.0,0.33,0.25,0.67),2.0:(0.0,0.31,0.24,0.69),
 4.5:(0.0,0.05,1.0,0.95),5.0:(0.0,0.08,1.0,0.92),7.5:(0.72,0.15,0.28,0.85),8.0:(0.57,0.18,0.33,0.82),8.5:(0.60,0.0,0.22,0.22),
 9.0:(0.12,0.18,0.24,0.80),9.5:(0.13,0.20,0.24,0.76),10.0:(0.16,0.22,0.22,0.72)}
bald = {0.0:(0.27,0.30,0.19,0.70),0.5:(0.28,0.30,0.18,0.70),1.0:(0.26,0.30,0.20,0.70),1.5:(0.25,0.30,0.21,0.70),2.0:(0.24,0.28,0.22,0.72),
 4.0:(0.0,0.10,0.14,0.90),5.5:(0.0,0.08,1.0,0.92),6.0:(0.0,0.08,1.0,0.92),6.5:(0.0,0.08,1.0,0.92),7.0:(0.0,0.10,1.0,0.90),
 7.5:(0.24,0.13,0.48,0.87),8.0:(0.25,0.18,0.32,0.82),8.5:(0.38,0.0,0.22,0.97),
 9.0:(0.36,0.18,0.30,0.80),9.5:(0.37,0.20,0.28,0.76),10.0:(0.38,0.22,0.28,0.72)}
dump({"mediaId":168,"level":"B","keyWord":"citizenship","defaultVoice":"female",
 "taps":[
  {"phrase":"to present a rolled certificate","target":"the official","voice":"female","keys":K(T10,off_)},
  {"phrase":"to shed tears of joy","target":"the man in the burgundy suit","voice":"male","keys":K(T10,bur)},
  {"phrase":"to raise a scroll overhead","target":"the bald woman","voice":"female","keys":K(T10,bald)}],
 "stillS":10.0,
 "nouns":[{"word":"a scroll","x":0.40,"y":0.30,"voice":"female"},{"word":"a sash","x":0.84,"y":0.62,"voice":"female"},
          {"word":"a beard","x":0.65,"y":0.45,"voice":"female"},{"word":"a window","x":0.55,"y":0.10,"voice":"female"}],
 "question":"What is the official presenting?",
 "answer":["She","is","presenting","a","rolled","certificate."],"answerVoice":"female",
 "notes":"The official = grey-haired woman in the pale blue dress (2.5-4.0 s); a second grey-haired woman in a blue suit stands among the new citizens. Tears of the man are visible at 4.5-5.0 s only. The bald woman raises her scroll at 9.0-10.0 s while the others raise flags. At 4.0 s the bald woman is only a sliver at the left edge. At 8.0-8.5 s (hug) the boxes of the man and the bald woman are rough splits."})

# ---------- 169
wom = {0.0:(0,0,0.62,0.60),0.5:(0,0,0.70,0.73),1.0:(0,0,0.68,0.76),1.5:(0,0,0.68,0.82),2.0:(0,0,0.68,0.70),2.5:(0,0,0.74,0.70),
 3.0:(0,0,0.70,0.85),3.5:(0,0,0.74,0.86),4.0:(0,0,0.70,0.74),4.5:(0,0,0.72,0.76),5.0:(0,0,0.70,0.84),5.5:(0,0,0.72,0.84),
 6.0:(0,0,0.70,0.72),6.5:(0,0,0.73,0.72),7.0:(0,0,0.70,0.80),7.5:(0,0,0.72,0.80),8.0:(0,0,0.70,0.70),8.5:(0,0,0.72,0.70),
 9.0:(0,0,0.72,0.78),9.5:(0,0,0.73,0.77),10.0:(0,0,0.65,0.76)}
cat = {0.0:(0.63,0.45,0.20,0.14),0.5:(0.70,0.44,0.20,0.14),1.0:(0.68,0.40,0.18,0.14),1.5:(0.68,0.35,0.18,0.14),2.0:(0.68,0.34,0.20,0.14),
 2.5:(0.74,0.31,0.20,0.14),3.0:(0.70,0.32,0.20,0.14),3.5:(0.74,0.29,0.20,0.14),4.0:(0.70,0.28,0.20,0.14),4.5:(0.72,0.27,0.20,0.14),
 5.0:(0.70,0.27,0.20,0.14),5.5:(0.72,0.27,0.20,0.14),6.0:(0.70,0.27,0.20,0.14),6.5:(0.73,0.27,0.20,0.14),7.0:(0.70,0.27,0.20,0.14),
 7.5:(0.72,0.27,0.20,0.14),8.0:(0.70,0.28,0.20,0.14),8.5:(0.72,0.30,0.20,0.14),9.0:(0.72,0.36,0.20,0.14),9.5:(0.74,0.44,0.20,0.14),
 10.0:(0.66,0.50,0.20,0.14)}
man = {0.0:(0.79,0.03,0.21,0.42),0.5:(0.80,0.0,0.20,0.44),1.0:(0.86,0.0,0.14,0.52),1.5:(0.86,0.0,0.14,0.46),2.0:(0.82,0.0,0.18,0.34),
 2.5:(0.82,0.0,0.18,0.31),3.0:(0.82,0.0,0.18,0.32),3.5:(0.82,0.0,0.18,0.29),4.0:(0.82,0.0,0.18,0.28),4.5:(0.82,0.0,0.18,0.27),
 5.0:(0.82,0.0,0.18,0.27),5.5:(0.82,0.0,0.18,0.27),6.0:(0.82,0.0,0.18,0.27),6.5:(0.82,0.0,0.18,0.27),7.0:(0.82,0.0,0.18,0.27),
 7.5:(0.82,0.0,0.18,0.27),8.0:(0.82,0.0,0.18,0.28),8.5:(0.82,0.0,0.18,0.30),9.0:(0.80,0.0,0.20,0.36),9.5:(0.80,0.0,0.20,0.44),
 10.0:(0.73,0.0,0.27,0.50)}
dump({"mediaId":169,"level":"A","keyWord":"clay","defaultVoice":"female",
 "taps":[
  {"phrase":"to make a clay pot","target":"the woman","voice":"female","keys":K(T10,wom)},
  {"phrase":"to sit on the floor","target":"the cat on the floor","voice":"female","keys":K(T10,cat)},
  {"phrase":"to stand near the wheel","target":"the man","voice":"male","keys":K(T10,man)}],
 "stillS":0.0,
 "nouns":[{"word":"clay","x":0.42,"y":0.17,"voice":"female"},{"word":"a cat","x":0.76,"y":0.52,"voice":"female"},
          {"word":"a wheel","x":0.50,"y":0.70,"voice":"female"},{"word":"a window","x":0.72,"y":0.06,"voice":"female"}],
 "question":"What is the woman making?",
 "answer":["She","is","making","a","pot","from","clay."],"answerVoice":"female",
 "notes":"The woman is mostly arms and hands (face at 0.0, 9.5, 10.0 s). The man is a standing figure at the right edge, mostly an arm; his face shows only at 10.0 s. From about 2.0 s a second cat walks on a shelf at the top right (inside the man's box at some times); the target is the cat sitting on the floor. The woman's box is cut on the right where her hands come close to the cat. The object is a tall pot / vase (the transcript says bowl)."})

# ---------- 170
cl = {0.5:(0.38,0.19,0.38,0.68),1.0:(0.34,0.18,0.35,0.72),1.5:(0.27,0.09,0.48,0.83),2.0:(0.30,0.26,0.52,0.60),2.5:(0.03,0.65,0.74,0.35),
 3.0:(0.05,0.45,0.85,0.26),3.5:(0.16,0.10,0.70,0.69),4.0:(0.30,0.0,0.70,0.62),4.5:(0.50,0.11,0.50,0.52),5.0:(0.36,0.18,0.64,0.76),
 5.5:(0.18,0.10,0.62,0.90),6.0:(0.64,0.36,0.36,0.26),6.5:(0.42,0.0,0.58,0.48),7.0:(0.05,0.57,0.95,0.40),
 8.0:(0.34,0.12,0.66,0.77),8.5:(0.05,0.21,0.90,0.75),9.0:(0.35,0.30,0.31,0.64),9.5:(0.33,0.33,0.36,0.57),10.0:(0.33,0.33,0.36,0.46)}
sun = {6.0:(0.15,0.20,0.30,0.22),6.5:(0.12,0.0,0.30,0.26),7.0:(0.22,0.0,0.50,0.32),8.5:(0.66,0.03,0.28,0.18),9.0:(0.55,0.15,0.26,0.15),
 9.5:(0.57,0.17,0.26,0.16),10.0:(0.56,0.19,0.24,0.14)}
dump({"mediaId":170,"level":"A","keyWord":"cleaner","defaultVoice":"female",
 "taps":[
  {"phrase":"to make the bed","target":"the cleaner","voice":"female","keys":K(T10,cl)},
  {"phrase":"to clean the window","target":"the cleaner","voice":"female","keys":K(T10,cl)},
  {"phrase":"to shine in the sky","target":"the sun","voice":"female","keys":K(T10,sun)}],
 "stillS":10.0,
 "nouns":[{"word":"a cleaner","x":0.50,"y":0.52,"voice":"female"},{"word":"a bed","x":0.27,"y":0.66,"voice":"female"},
          {"word":"a door","x":0.14,"y":0.38,"voice":"female"},{"word":"the sun","x":0.67,"y":0.29,"voice":"female"}],
 "question":"Who is making the bed?",
 "answer":["The","cleaner","is","making","the","bed."],"answerVoice":"female",
 "notes":"Only one person in the clip, so two phrases share the cleaner; the third target is the sun (visible 6.0-7.0 s in the window she cleans and 8.5-10.0 s; at 6.0 s it is only a soft glare). At 2.0 s the cleaner is hidden behind the sheet she holds (gloves and dress visible); at 6.0-7.0 s only her gloved hand is in the picture; at 7.5 s only a shoe (off)."})

# ---------- 171
A = {0.0:(0.26,0.20,0.74,0.80),0.5:(0.0,0.19,0.42,0.81),1.0:(0.0,0.26,0.52,0.74),1.5:(0.0,0.23,0.48,0.77),2.0:(0.0,0.20,0.47,0.80),
 2.5:(0.0,0.18,0.52,0.82),3.0:(0.0,0.08,1.0,0.92),3.5:(0.0,0.06,1.0,0.94),4.0:(0.0,0.22,0.46,0.78),4.5:(0.0,0.20,0.36,0.80),5.0:(0.0,0.30,0.22,0.70)}
H = {0.5:(0.42,0.25,0.58,0.75),1.0:(0.52,0.33,0.48,0.67),1.5:(0.48,0.30,0.52,0.70),2.0:(0.47,0.28,0.53,0.72),2.5:(0.52,0.26,0.48,0.74),
 4.0:(0.50,0.31,0.50,0.69),4.5:(0.58,0.10,0.42,0.90),5.0:(0.68,0.64,0.32,0.36),5.5:(0.66,0.33,0.34,0.67),6.0:(0.62,0.30,0.38,0.70),
 6.5:(0.76,0.27,0.24,0.73),7.0:(0.63,0.25,0.37,0.75),7.5:(0.56,0.23,0.44,0.77),11.0:(0.03,0.15,0.97,0.71),11.5:(0.78,0.25,0.22,0.75),
 12.5:(0.48,0.26,0.52,0.74),13.0:(0.57,0.25,0.43,0.75),13.5:(0.72,0.08,0.28,0.92),14.0:(0.47,0.26,0.53,0.74),14.5:(0.47,0.28,0.53,0.72),
 15.0:(0.50,0.28,0.50,0.72)}
W = {5.5:(0.18,0.33,0.48,0.67),6.0:(0.08,0.31,0.54,0.69),6.5:(0.20,0.28,0.56,0.72),7.0:(0.02,0.26,0.61,0.74),7.5:(0.0,0.25,0.56,0.75),
 8.0:(0.0,0.08,1.0,0.92),8.5:(0.0,0.08,1.0,0.92),9.0:(0.0,0.08,1.0,0.92),9.5:(0.0,0.08,1.0,0.92),10.0:(0.0,0.08,1.0,0.92),10.5:(0.0,0.08,1.0,0.92),
 11.0:(0.0,0.86,0.40,0.14),11.5:(0.10,0.26,0.66,0.74),12.0:(0.54,0.26,0.46,0.74),12.5:(0.0,0.28,0.48,0.72),13.0:(0.02,0.28,0.55,0.72),
 13.5:(0.0,0.25,0.72,0.75),14.0:(0.0,0.24,0.47,0.76),14.5:(0.0,0.28,0.47,0.72),15.0:(0.0,0.28,0.50,0.72)}
dump({"mediaId":171,"level":"A","keyWord":"correct","defaultVoice":"male",
 "taps":[
  {"phrase":"to hold a microphone","target":"the man in the hoodie","voice":"male","keys":K(T15,H)},
  {"phrase":"to give the correct answer","target":"the man in the T-shirt","voice":"male","keys":K(T15,A)},
  {"phrase":"to cross her arms","target":"the woman","voice":"female","keys":K(T15,W)}],
 "stillS":13.0,
 "nouns":[{"word":"a woman","x":0.32,"y":0.42,"voice":"female"},{"word":"a man","x":0.76,"y":0.40,"voice":"male"},
          {"word":"a microphone","x":0.72,"y":0.62,"voice":"male"},{"word":"a bag","x":0.20,"y":0.93,"voice":"male"}],
 "question":"What is the woman doing?",
 "answer":["She","is","crossing","her","arms."],"answerVoice":"female",
 "notes":"'to give the correct answer' rests on the green 'Correct' caption over the man in the T-shirt at 3.0 s (no sound needed); the red 'Wrong' caption appears at 11.0 s (over the host) and 11.5 s (over the woman). The woman crosses her arms at 5.5-7.5 and 11.0-12.0 s, not at the end. Only the host's hand with the microphone is visible at 0.0, 3.0 and 8.0-10.5 s (off there). At 11.0 s the woman is only a corner of her jacket at the bottom left. At 15.0 s the host's hand with the microphone reaches into the woman's box. 'a man' and 'a microphone' are both on the host at 13.0 s (face vs. hand)."})
