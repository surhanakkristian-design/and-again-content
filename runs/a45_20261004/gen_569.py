# writer helper for media 569, 572, 573, 574 (writes content/<id>.json)
import json, os
RUN = os.path.dirname(os.path.abspath(__file__))

def keys(times, d):
    out = []
    for t in times:
        b = d.get(t)
        if b is None:
            out.append({"t": t, "off": True})
        else:
            out.append({"t": t, "x": b[0], "y": b[1], "w": b[2], "h": b[3]})
    return out

def times(n):
    return [i * 0.5 for i in range(n)]

def write(d):
    with open(os.path.join(RUN, "content", "%d.json" % d["mediaId"]), "w") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)

# ---------------------------------------------------------------- 569
T = times(23)
boss = {0.0: (.20, .23, .78, .36), 0.5: (.20, .23, .78, .36), 1.0: (0, .21, 1, .77), 1.5: (.04, .14, .96, .86),
        2.0: (0, .11, .84, .78), 3.5: (.37, .37, .63, .37), 4.0: (0, .35, .64, .65),
        5.5: (0, .10, 1, .74), 6.0: (0, .10, 1, .74), 6.5: (0, .10, 1, .74),
        7.0: (.37, .13, .63, .71), 7.5: (.14, 0, .86, .44), 8.0: (.56, .03, .44, .72), 8.5: (.66, .14, .34, .61),
        9.5: (.56, .25, .30, .58), 10.0: (.14, .22, .70, .63), 10.5: (.15, .20, .81, .65), 11.0: (.15, .20, .81, .65)}
man = {2.5: (.08, .34, .52, .24), 3.0: (.13, .25, .44, .31), 4.5: (.16, .28, .35, .34), 5.0: (.17, .25, .29, .37),
       9.0: (.04, .20, .46, .67), 9.5: (.44, .30, .11, .14)}
girl = {2.5: (.66, .35, .34, .23), 3.0: (.61, .30, .32, .26), 4.5: (.58, .36, .32, .26), 5.0: (.58, .35, .32, .27),
        9.0: (.51, .29, .44, .58), 9.5: (.27, .34, .16, .22)}
write({
    "mediaId": 569, "level": "B", "keyWord": "postmaster", "defaultVoice": "female",
    "taps": [
        {"phrase": "to unlock the front door", "target": "the grey-haired woman", "voice": "female", "keys": keys(T, boss)},
        {"phrase": "to have a bushy moustache", "target": "the man", "voice": "male", "keys": keys(T, man)},
        {"phrase": "to wear a ponytail", "target": "the young woman", "voice": "female", "keys": keys(T, girl)},
    ],
    "stillS": 10.5,
    "nouns": [
        {"word": "a postmaster", "x": .58, "y": .44, "voice": "female"},
        {"word": "keys", "x": .66, "y": .63, "voice": "female"},
        {"word": "parcels", "x": .25, "y": .59, "voice": "female"},
        {"word": "a trolley", "x": .25, "y": .72, "voice": "female"},
    ],
    "question": "What is the postmaster doing?",
    "answer": ["She", "is", "pushing", "a", "trolley", "full", "of", "parcels."],
    "answerVoice": "female",
    "notes": "The two clerks get states (moustache, ponytail): every action of one clerk is also done by the other or by the postmaster (both lounge, both jump up, man and postmaster both push the trolley). 3.5-4.0 and 7.0-8.5 show only the postmaster's hand/arm; boxed as her. 9.0: the man's front foot reaches into the young woman's box (split at x .50). 9.5: the clerks are tiny in the background next to the postmaster, boxes kept small so they do not overlap; her left arm is outside her box."
})

# ---------------------------------------------------------------- 572
T = times(21)
man = {0.0: (0, 0, .50, .78), 0.5: (0, 0, .46, .78), 1.0: (0, 0, .36, .88), 1.5: (0, 0, .31, .86), 2.0: (0, 0, .34, .80),
       2.5: (0, 0, .16, .62), 3.0: (0, 0, .18, .14), 3.5: (0, 0, .19, .23),
       6.5: (0, .10, .51, .60), 7.0: (0, 0, .56, .76), 7.5: (0, 0, .23, .56), 8.0: (0, 0, .31, .34), 8.5: (0, 0, .32, .35),
       9.0: (0, 0, .38, .69), 9.5: (0, 0, .37, .66), 10.0: (0, 0, .34, .26)}
woman = {2.0: (.82, .58, .18, .25), 2.5: (.81, .42, .19, .26), 3.0: (.60, 0, .40, .60), 3.5: (.24, 0, .76, .76),
         4.0: (.20, 0, .80, .67), 4.5: (.39, 0, .61, .69), 5.0: (.40, 0, .60, .62), 5.5: (.33, 0, .67, .67),
         6.0: (.38, 0, .62, .77), 6.5: (.65, 0, .35, .78), 7.0: (.76, 0, .24, .79), 7.5: (.44, .03, .56, .65),
         8.0: (.51, .03, .49, .85), 8.5: (.52, .01, .48, .69), 9.0: (.57, .03, .43, .75), 9.5: (.46, .10, .54, .63),
         10.0: (.48, 0, .52, .78)}
bird = {0.0: (.51, .06, .18, .14), 0.5: (.51, .06, .18, .14), 1.0: (.51, .08, .18, .14), 1.5: (.50, .08, .18, .14),
        2.5: (.43, 0, .18, .14),
        7.5: (.25, 0, .18, .14), 8.0: (.32, .01, .18, .14), 8.5: (.33, .01, .18, .14), 9.0: (.39, .04, .18, .14)}
write({
    "mediaId": 572, "level": "A", "keyWord": "potato", "defaultVoice": "female",
    "taps": [
        {"phrase": "to dig in the garden", "target": "the man", "voice": "male", "keys": keys(T, man)},
        {"phrase": "to wear a blue scarf", "target": "the woman", "voice": "female", "keys": keys(T, woman)},
        {"phrase": "to sit on a fence", "target": "the bird", "voice": "female", "keys": keys(T, bird)},
    ],
    "stillS": 8.0,
    "nouns": [
        {"word": "a bird", "x": .40, "y": .08, "voice": "female"},
        {"word": "a woman", "x": .84, "y": .30, "voice": "female"},
        {"word": "potatoes", "x": .46, "y": .60, "voice": "female"},
        {"word": "a bucket", "x": .42, "y": .72, "voice": "female"},
    ],
    "question": "What is the woman doing?",
    "answer": ["She", "is", "putting", "potatoes", "in", "a", "bucket."],
    "answerVoice": "female",
    "notes": "Woman gets a state (blue scarf on her head): both pick up, hold and put potatoes in the bucket. defaultVoice female (man and woman equal, evenId true). Key word as bare plural 'potatoes' (several in the bucket). The bird is small, on a fence post; near it the man's / woman's boxes are cut back (7.5-9.0), so some fingertips lie outside; at 2.5 only its lower half shows at the top edge."
})

# ---------------------------------------------------------------- 573
man = {0.0: (0, 0, 1, .43), 0.5: (0, 0, 1, .43), 1.0: (0, 0, 1, .44), 1.5: (0, 0, 1, .44), 2.0: (.03, 0, .97, .54),
       2.5: (.06, 0, .94, .53), 3.0: (.10, 0, .90, .56), 3.5: (.17, 0, .83, .56), 4.0: (.24, 0, .76, .60),
       4.5: (.28, 0, .72, .74), 5.0: (.28, 0, .72, .78), 5.5: (.29, 0, .71, .76), 6.0: (.30, 0, .70, .80),
       6.5: (.31, 0, .69, .80), 7.0: (.30, 0, .70, .86), 7.5: (.36, 0, .64, .90), 8.0: (.38, .21, .62, .65),
       8.5: (.46, .09, .54, .70), 9.0: (.65, 0, .35, .68), 9.5: (.59, .03, .41, .74), 10.0: (.61, .09, .39, .73)}
woman = {4.0: (0, .09, .18, .33), 4.5: (0, .08, .25, .44), 5.0: (0, .08, .27, .44), 5.5: (0, .09, .27, .42),
         6.0: (0, .12, .27, .48), 6.5: (0, .19, .30, .44), 7.0: (0, .25, .27, .45), 7.5: (0, .28, .35, .42),
         8.0: (0, .28, .37, .50), 8.5: (0, .18, .44, .56), 9.0: (0, 0, .34, .70), 9.5: (0, .07, .32, .61),
         10.0: (0, .11, .35, .52)}
write({
    "mediaId": 573, "level": "A", "keyWord": "pouring", "defaultVoice": "male",
    "taps": [
        {"phrase": "to pour orange juice", "target": "the man", "voice": "male", "keys": keys(T, man)},
        {"phrase": "to hold a big bottle", "target": "the man", "voice": "male", "keys": keys(T, man)},
        {"phrase": "to pick up a glass", "target": "the woman", "voice": "female", "keys": keys(T, woman)},
    ],
    "stillS": 10.0,
    "nouns": [
        {"word": "a man", "x": .80, "y": .33, "voice": "male"},
        {"word": "a woman", "x": .17, "y": .33, "voice": "female"},
        {"word": "a bottle", "x": .65, "y": .62, "voice": "male"},
        {"word": "glasses", "x": .48, "y": .80, "voice": "male"},
    ],
    "question": "What is the man doing?",
    "answer": ["He", "is", "pouring", "orange", "juice", "into", "glasses."],
    "answerVoice": "male",
    "notes": "Only two possible targets (a cat in the background is too faint), so the man has two phrases. The woman picks up a glass only at the end (9.5-10.0). 7.5-8.0: the woman's elbow reaches under the man's raised bottle; boxes split at x about .36."
})

# ---------------------------------------------------------------- 574
bun = {2.5: (0, .25, .18, .60), 3.0: (0, 0, .26, 1), 3.5: (0, 0, .40, 1), 4.0: (0, 0, .56, 1), 4.5: (0, 0, .68, 1),
       5.0: (0, .02, .83, .98), 5.5: (0, .09, 1, .91), 6.0: (.37, .15, .60, .85), 6.5: (.55, .15, .45, .85),
       7.0: (.65, .17, .35, .83), 7.5: (.72, .17, .28, .83), 8.0: (.68, .20, .32, .80), 8.5: (.64, .12, .36, .88),
       9.0: (.64, .09, .36, .91), 9.5: (.55, .06, .45, .94), 10.0: (.51, .06, .49, .94)}
short = {6.0: (0, 0, .36, 1), 6.5: (0, 0, .52, 1), 7.0: (0, .03, .63, .97), 7.5: (0, .03, .70, .97), 8.0: (0, 0, .66, 1),
         8.5: (0, 0, .62, 1), 9.0: (0, 0, .62, 1), 9.5: (0, 0, .53, 1), 10.0: (0, 0, .48, 1)}
write({
    "mediaId": 574, "level": "A", "keyWord": "powder", "defaultVoice": "female",
    "taps": [
        {"phrase": "to open her mouth wide", "target": "the woman with the bun", "voice": "female", "keys": keys(T, bun)},
        {"phrase": "to touch her chest", "target": "the woman with the bun", "voice": "female", "keys": keys(T, bun)},
        {"phrase": "to have short black hair", "target": "the woman with short hair", "voice": "female", "keys": keys(T, short)},
    ],
    "stillS": 2.0,
    "nouns": [
        {"word": "a tree", "x": .62, "y": .12, "voice": "female"},
        {"word": "a brush", "x": .45, "y": .58, "voice": "female"},
        {"word": "a jar", "x": .60, "y": .74, "voice": "female"},
        {"word": "powder", "x": .50, "y": .90, "voice": "female"},
    ],
    "question": "What is in the jar?",
    "answer": ["There", "is", "powder", "in", "the", "jar."],
    "answerVoice": "female",
    "notes": "The clip does not show clearly whose hand holds the brush (0.5-4.0 a hand from the camera side; 6.0-8.5 a hand in a cream sleeve), so no phrase is about brushing and the question is about the jar. The short-haired woman only sits still, so she gets a state. 0.0-2.0 show only jar, brush and a hand: both women off. 2.5-3.5: the woman with the bun is only a blurred figure at the left edge. 6.0-8.5: the brush hand lies in front of both women; boxes split between the two faces. 'a jar' sits on the upper glass part, 'powder' on the powder inside."
})
print("ok")
