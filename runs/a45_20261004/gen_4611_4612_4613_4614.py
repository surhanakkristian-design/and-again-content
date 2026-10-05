import json, os
RUN = os.path.dirname(os.path.abspath(__file__))

def keys(times, d):
    out = []
    for t in times:
        b = d.get(t)
        if b is None:
            out.append({"t": t, "off": True})
        else:
            x, y, w, h = b
            w = min(w, round(1 - x, 2)); h = min(h, round(1 - y, 2))
            out.append({"t": t, "x": x, "y": y, "w": round(w, 2), "h": round(h, 2)})
    return out

def T(n):
    return [i * 0.5 for i in range(n)]

def save(c):
    with open(os.path.join(RUN, "content", "%d.json" % c["mediaId"]), "w") as f:
        json.dump(c, f, indent=1, ensure_ascii=False)

# ---------------- 4611
t = T(19)
girl = {0.0: (0, 0, .88, .47), 0.5: (0, 0, .86, .47), 1.0: (0, 0, .88, .41), 1.5: (0, .02, .59, .75),
        2.0: (0, .03, .57, .75), 2.5: (0, .15, .70, .68), 3.0: (0, .16, .66, .75), 3.5: (0, .15, .52, .80),
        4.0: (.08, .13, .44, .75), 4.5: (.08, .12, .44, .75), 5.0: (.63, .36, .30, .40), 5.5: (.40, .36, .55, .38),
        6.0: (.15, .33, .58, .36), 6.5: (.12, .35, .42, .31), 7.0: (.16, .52, .20, .35), 7.5: (.13, .52, .21, .35),
        8.0: (.08, .51, .18, .24), 8.5: (.04, .51, .20, .24), 9.0: (.02, .52, .20, .24)}
woman = {0.5: (.86, 0, .14, .47), 1.0: (.45, .41, .55, .22), 1.5: (.59, 0, .41, .75), 2.0: (.57, 0, .43, .77),
         2.5: (.70, 0, .30, .97), 3.0: (.66, .02, .34, .98), 3.5: (.52, .15, .48, .85), 4.0: (.52, .18, .48, .80),
         4.5: (.52, .17, .48, .80), 7.0: (0, .44, .16, .43), 7.5: (0, .44, .13, .44), 8.0: (0, .44, .08, .31)}
gk, wk = keys(t, girl), keys(t, woman)
save({
 "mediaId": 4611, "level": "A", "keyWord": "daughter", "defaultVoice": "female",
 "taps": [
  {"phrase": "to show a drawing", "target": "the girl", "voice": "female", "keys": gk},
  {"phrase": "to dance with two men", "target": "the girl", "voice": "female", "keys": gk},
  {"phrase": "to hug her daughter", "target": "the woman", "voice": "female", "keys": wk},
 ],
 "stillS": 2.5,
 "nouns": [
  {"word": "a daughter", "x": 0.30, "y": 0.24, "voice": "female"},
  {"word": "a mother", "x": 0.84, "y": 0.50, "voice": "female"},
  {"word": "a drawing", "x": 0.42, "y": 0.56, "voice": "female"},
  {"word": "a bowl", "x": 0.28, "y": 0.92, "voice": "female"},
 ],
 "question": "What is the daughter showing her mother?",
 "answer": ["She", "is", "showing", "her", "mother", "a", "drawing."],
 "answerVoice": "female",
 "notes": "Clip has cuts. 0.0-1.0 shows only hands/torsos (girl = cream cable-knit sweater, woman = brown sleeve/hand with ring; woman off at 0.0, only a chin sliver). 5.0-6.5 girl dances with two men, woman not in shot. Park shot 7.0-9.0: boxes follow the foreground girl with the ponytail and the woman holding her hand at the left edge, assumed to be the same daughter and mother (woman off from 8.5, only an arm left). 'to hug her daughter': the girl hugs too, but 'her daughter' fits only the mother."
})

# ---------------- 4612
t = T(25)
seller = {0.0: (.44, .15, .56, .85), 0.5: (.41, .14, .59, .86), 1.0: (.42, .18, .58, .82), 1.5: (.42, .20, .58, .80),
          2.0: (.47, .19, .53, .81), 2.5: (.55, .20, .45, .68), 3.0: (.60, .46, .40, .46), 3.5: (.60, .02, .40, .95),
          4.0: (.42, 0, .58, .70), 4.5: (.50, 0, .50, .80), 5.0: (.58, 0, .42, .82), 5.5: (.54, 0, .46, .80),
          6.0: (.58, .02, .42, .95), 6.5: (.56, .18, .44, .55), 7.0: (.60, .30, .40, .55), 7.5: (.49, .28, .51, .50),
          8.0: (.45, .22, .55, .42), 8.5: (.80, .22, .20, .62), 9.0: (.80, .30, .20, .65), 9.5: (.70, .20, .30, .80),
          10.0: (.33, .18, .67, .82), 10.5: (.32, .16, .68, .84), 11.0: (.28, .17, .72, .83), 11.5: (.36, .17, .64, .83),
          12.0: (.50, .15, .50, .85)}
young = {0.0: (0, 0, .20, .42), 0.5: (0, .02, .32, .42), 1.0: (0, .05, .40, .50), 1.5: (0, .08, .38, .85),
         2.0: (0, .08, .43, .85), 2.5: (0, .13, .47, .87), 3.0: (0, .04, .52, .96), 3.5: (0, 0, .35, 1.0),
         4.0: (0, .06, .18, .22), 4.5: (0, .66, .20, .28), 5.0: (0, .73, .24, .27), 5.5: (0, .22, .20, .20),
         6.0: (0, 0, .25, 1.0), 6.5: (0, .02, .42, .98), 7.0: (0, .08, .42, .92), 7.5: (0, .07, .48, .93),
         8.0: (0, .08, .43, .87), 8.5: (0, .08, .28, .58), 9.0: (0, .42, .22, .18),
         10.0: (0, .22, .18, .45), 10.5: (0, .20, .24, .47), 11.0: (0, .23, .27, .47), 11.5: (.08, .25, .25, .42),
         12.0: (.14, .24, .20, .28)}
sk, yk = keys(t, seller), keys(t, young)
save({
 "mediaId": 4612, "level": "A", "keyWord": "sell", "defaultVoice": "male",
 "taps": [
  {"phrase": "to sell peaches", "target": "the seller", "voice": "male", "keys": sk},
  {"phrase": "to fill a box", "target": "the seller", "voice": "male", "keys": sk},
  {"phrase": "to pay for the fruit", "target": "the young man", "voice": "male", "keys": yk},
 ],
 "stillS": 12.0,
 "nouns": [
  {"word": "peaches", "x": 0.24, "y": 0.62, "voice": "male"},
  {"word": "a box", "x": 0.50, "y": 0.86, "voice": "male"},
  {"word": "a man", "x": 0.85, "y": 0.56, "voice": "male"},
 ],
 "question": "What is the older man selling?",
 "answer": ["He", "is", "selling", "a", "box", "of", "peaches."],
 "answerVoice": "male",
 "notes": "Seller = older man with the moustache and waistcoat; young man = customer on the left. 4.0-5.5 is a close shot from above: the customer is only a hand with banknotes or his white trainers (small boxes there), the seller is arms/hands filling the box. 9.5 customer off (only a fingertip and the box edge). From 10.0 the customer walks away at the left with his back to the camera (olive T-shirt, cross strap) - boxed as the same man. 'a man' pill at 12.0 sits on the seller; a small blurred passer-by is in the background."
})

# ---------------- 4613
t = T(25)
man = {0.0: (0, .11, .45, .50), 0.5: (0, .10, .50, .52), 1.0: (0, .10, .30, .57), 1.5: (0, .05, .57, .67),
       2.0: (0, .04, .62, .60), 2.5: (0, .03, .54, .62), 3.0: (0, .08, .47, .74), 3.5: (0, .10, .38, .62),
       4.0: (0, .02, .52, .60), 4.5: (0, 0, .49, .64), 5.0: (0, 0, .47, .82), 5.5: (0, 0, .55, .78),
       6.0: (0, 0, .47, .74), 6.5: (0, 0, .36, .72), 7.0: (0, 0, .49, .87), 7.5: (0, 0, .47, .77),
       8.0: (0, 0, .47, .62), 8.5: (0, 0, .44, .62), 9.0: (0, 0, .44, .64), 9.5: (0, 0, .70, .67),
       10.0: (0, 0, .80, .67), 10.5: (0, 0, .82, .69), 11.0: (0, 0, .77, .74), 11.5: (0, 0, .82, .74),
       12.0: (0, 0, .82, .67)}
mk = keys(t, man)
save({
 "mediaId": 4613, "level": "A", "keyWord": "earth", "defaultVoice": "male",
 "taps": [
  {"phrase": "to hold a black bucket", "target": "the man", "voice": "male", "keys": mk},
  {"phrase": "to dig the earth", "target": "the man", "voice": "male", "keys": mk},
  {"phrase": "to work in a garden", "target": "the man", "voice": "male", "keys": mk},
 ],
 "stillS": 0.0,
 "nouns": [
  {"word": "the sky", "x": 0.60, "y": 0.08, "voice": "male"},
  {"word": "a bucket", "x": 0.50, "y": 0.32, "voice": "male"},
  {"word": "a man", "x": 0.17, "y": 0.47, "voice": "male"},
  {"word": "earth", "x": 0.55, "y": 0.66, "voice": "male"},
 ],
 "question": "What is the man doing?",
 "answer": ["He", "is", "digging", "the", "earth", "in", "a", "garden."],
 "answerVoice": "male",
 "notes": "Only one possible target (the man), used for all three phrases. The box follows him with the spade and his gloved hands; the bucket (0.0-1.0) is not inside the box except where he grips it. The heap is compost; called 'earth' as the key word and the description do."
})

# ---------------- 4614
t = T(25)
man = {0.0: (0, .08, .46, .92), 0.5: (0, .08, .44, .92), 1.0: (0, .09, .42, .91), 1.5: (0, .09, .42, .91),
       2.0: (0, .10, .37, .80), 2.5: (0, .10, .37, .80), 3.0: (.03, .11, .47, .80), 3.5: (.03, .11, .47, .80),
       4.0: (.13, .07, .87, .93), 4.5: (.02, .08, .98, .92), 5.0: (0, .09, .40, .85), 5.5: (0, .10, .47, .82),
       6.0: (0, .09, .33, .91), 6.5: (0, .13, .32, .85), 7.0: (0, .18, .37, .82), 7.5: (0, .20, .42, .80),
       8.0: (0, .25, .44, .70), 8.5: (.10, .34, .36, .63), 9.0: (.18, .34, .34, .66), 9.5: (.20, .34, .32, .64),
       10.0: (.23, .34, .29, .57), 10.5: (.28, .35, .24, .53), 11.0: (.31, .36, .20, .60), 11.5: (.33, .36, .19, .58),
       12.0: (.33, .36, .19, .46)}
woman = {0.0: (.46, .53, .54, .47), 0.5: (.44, .50, .56, .50), 1.0: (.42, .50, .55, .50), 1.5: (.42, .50, .50, .50),
         2.0: (.37, .38, .63, .62), 2.5: (.37, .38, .63, .62), 3.0: (.50, .44, .50, .56), 3.5: (.50, .48, .50, .52),
         5.0: (.50, .40, .50, .60), 5.5: (.50, .38, .50, .62), 6.0: (.35, .42, .63, .58), 6.5: (.47, .40, .53, .60),
         7.0: (.48, .41, .50, .59), 7.5: (.50, .38, .45, .62), 8.0: (.50, .39, .42, .61), 8.5: (.47, .38, .41, .62),
         9.0: (.52, .38, .30, .62), 9.5: (.52, .38, .30, .60), 10.0: (.52, .38, .26, .55), 10.5: (.52, .40, .24, .48),
         11.0: (.51, .41, .23, .56), 11.5: (.52, .41, .21, .54), 12.0: (.52, .40, .20, .42)}
stream = {7.5: (.03, 0, .92, .19), 8.0: (0, 0, 1.0, .24), 8.5: (0, 0, 1.0, .32), 9.0: (0, 0, 1.0, .33),
          9.5: (0, 0, 1.0, .33), 10.0: (0, 0, 1.0, .33), 10.5: (0, 0, 1.0, .34), 11.0: (0, 0, 1.0, .35),
          11.5: (0, 0, 1.0, .35), 12.0: (0, 0, 1.0, .35)}
save({
 "mediaId": 4614, "level": "B", "keyWord": "hang", "defaultVoice": "female",
 "taps": [
  {"phrase": "to stand on a stepladder", "target": "the man", "voice": "male", "keys": keys(t, man)},
  {"phrase": "to inflate an orange balloon", "target": "the woman", "voice": "female", "keys": keys(t, woman)},
  {"phrase": "to hang from the ceiling", "target": "the streamers", "voice": "female", "keys": keys(t, stream)},
 ],
 "stillS": 10.0,
 "nouns": [
  {"word": "streamers", "x": 0.50, "y": 0.10, "voice": "female"},
  {"word": "a denim jacket", "x": 0.64, "y": 0.56, "voice": "female"},
  {"word": "a stepladder", "x": 0.17, "y": 0.66, "voice": "female"},
  {"word": "balloons", "x": 0.80, "y": 0.80, "voice": "female"},
 ],
 "question": "What is hanging from the ceiling?",
 "answer": ["Paper", "streamers", "are", "hanging", "from", "the", "ceiling."],
 "answerVoice": "female",
 "notes": "Many cuts. 0.0-3.5 man and woman are close: the split runs along the woman's raised hand, so the man's box holds his head, torso and legs but cuts his outstretched arms/hands at the wall (0.0-2.5). 4.0-4.5 man alone. Streamers exist only from 7.5 (off before); their box is the ceiling band above the couple's heads; garlands and light strings on the wall also 'hang', but only the streamers hang from the ceiling. Balloons lie all over the floor at 10.0: the pill sits on the group at the lower right."
})
