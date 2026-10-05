# helper for media 4416, 4417, 4418, 4421: writes content/<id>.json
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
def keys(times, d):
    out = []
    for t in times:
        b = d.get(t)
        out.append({"t": t, "off": True} if b is None else {"t": t, "x": b[0], "y": b[1], "w": round(b[2], 2), "h": round(b[3], 2)})
    return out
def T(n): return [i * 0.5 for i in range(n)]
def write(c):
    json.dump(c, open(f'{HERE}/content/{c["mediaId"]}.json', 'w'), ensure_ascii=False, indent=1)

# ---------- 4416
t = T(19)
woman = {0.0: (0, 0, 1, .30), 0.5: (0, 0, .50, .30), 1.0: (0, 0, .42, .36), 1.5: (0, 0, .62, .44), 2.0: (0, 0, .95, .73),
         2.5: (0, .03, 1, .83), 3.0: (0, .22, 1, .78), 6.0: (0, .18, .85, .82), 6.5: (0, .18, .88, .82), 7.0: (0, .25, .85, .75),
         7.5: (.12, .24, .78, .76), 8.0: (.12, .10, .88, .90), 8.5: (.32, .08, .68, .92)}
printer = {0.0: (0, .30, 1, .70), 0.5: (0, .40, 1, .60), 1.0: (0, .48, 1, .52), 1.5: (0, .46, 1, .54), 2.0: (.10, .74, .90, .26),
           2.5: (.20, .86, .70, .14)}
pen = {0.5: (.50, .12, .42, .28), 1.0: (.42, .08, .58, .40), 1.5: (.62, .24, .38, .22)}
write({"mediaId": 4416, "level": "A", "keyWord": "ticket", "defaultVoice": "female",
 "taps": [
  {"phrase": "to read her ticket", "target": "the woman", "voice": "female", "keys": keys(t, woman)},
  {"phrase": "to print a ticket", "target": "the printer", "voice": "female", "keys": keys(t, printer)},
  {"phrase": "to draw a blue circle", "target": "the pen", "voice": "female", "keys": keys(t, pen)}],
 "stillS": 4.0,
 "nouns": [{"word": "a ticket", "x": .40, "y": .57, "voice": "female"}, {"word": "a hand", "x": .80, "y": .75, "voice": "female"},
           {"word": "a light", "x": .60, "y": .15, "voice": "female"}, {"word": "a screen", "x": .57, "y": .33, "voice": "female"}],
 "question": "What is the woman reading?",
 "answer": ["She", "is", "reading", "her", "ticket."], "answerVoice": "female",
 "notes": "Woman: at 0-1.5 s only her torso behind the printer is boxed (the pen hand belongs to a second person); at 3.5-5.5 and 9.0 only her hand is in the picture -> off. Pen box = the pen, not the whole hand. Printer at 2.5 s is only a strip at the bottom edge. Nouns at 4.0 s: 'a light' = the green lamp on top of the gate, 'a screen' sits on the screen with the red cross."})

# ---------- 4417
t = T(21)
woman = {0.0: (.48, .30, .52, .70), 0.5: (.36, .30, .64, .70), 1.0: (.20, .34, .74, .66), 1.5: (.18, .36, .72, .64),
         2.0: (.10, .24, .82, .76), 2.5: (.06, .23, .80, .77), 3.0: (.12, .28, .66, .72), 3.5: (.48, .28, .44, .50),
         4.0: (.32, .40, .48, .47), 4.5: (.33, .42, .42, .44), 5.0: (.33, .45, .36, .44), 5.5: (.36, .46, .32, .40),
         6.0: (.35, .41, .33, .31), 6.5: (.40, .38, .31, .31),
         7.0: (.36, .36, .26, .50), 7.5: (.37, .35, .28, .47), 8.0: (.38, .35, .24, .31), 8.5: (.40, .34, .23, .30),
         9.0: (.40, .31, .22, .42), 9.5: (.40, .37, .22, .34), 10.0: (.40, .36, .20, .19)}
tram = {0.0: (0, .02, .48, .72), 0.5: (0, .02, .36, .80), 1.0: (0, 0, 1, .34), 1.5: (0, 0, 1, .36), 2.0: (0, 0, 1, .24),
        2.5: (0, 0, 1, .23), 3.0: (0, 0, 1, .28), 3.5: (0, 0, .48, 1)}
plane = {7.0: (.62, .34, .38, .32), 7.5: (.65, .34, .35, .32), 8.0: (.62, .34, .38, .32), 8.5: (.63, .34, .37, .32),
         9.0: (.62, .34, .38, .32), 9.5: (.62, .34, .38, .32), 10.0: (.62, .34, .38, .32)}
write({"mediaId": 4417, "level": "A", "keyWord": "travel", "defaultVoice": "female",
 "taps": [
  {"phrase": "to carry a red backpack", "target": "the woman", "voice": "female", "keys": keys(t, woman)},
  {"phrase": "to open its doors", "target": "the tram", "voice": "female", "keys": keys(t, tram)},
  {"phrase": "to wait at the airport", "target": "the plane", "voice": "female", "keys": keys(t, plane)}],
 "stillS": 4.5,
 "nouns": [{"word": "a boat", "x": .50, "y": .33, "voice": "female"}, {"word": "a backpack", "x": .51, "y": .60, "voice": "female"},
           {"word": "water", "x": .14, "y": .46, "voice": "female"}, {"word": "the sky", "x": .25, "y": .08, "voice": "female"}],
 "question": "What is the woman carrying?",
 "answer": ["She", "is", "carrying", "a", "red", "backpack."], "answerVoice": "female",
 "notes": "Key word 'travel' is not a visible noun. Tram and woman overlap in the picture in the whole first shot: the tram box is the part of the tram beside / above her (changes shape per frame). Plane: she climbs the stairs in front of it, so the plane box is only the nose part right of her; the left part of the fuselage is unboxed. 'to open its doors': doors are closed at 0.5 s and open at 1.0 s. The boat is not used as a tap target."})

# ---------- 4418
t = T(25)
woman = {0.0: (.12, .10, .50, .37), 0.5: (.10, .10, .52, .38), 1.0: (.10, .11, .50, .38), 1.5: (.10, .11, .52, .39),
         2.0: (0, .12, .56, .40), 2.5: (0, .11, .50, .42), 3.0: (0, .12, .42, .41), 3.5: (0, .08, .33, .46),
         4.0: (0, .08, .40, .32), 4.5: (0, .08, .42, .32), 5.0: (0, .10, .42, .38), 5.5: (0, .10, .42, .38),
         6.0: (0, .10, .36, .34), 6.5: (0, .12, .42, .47), 7.0: (0, .12, .44, .47), 7.5: (0, .10, .58, .48),
         8.0: (0, .10, .70, .47), 8.5: (0, .10, .84, .46), 9.0: (0, .12, .88, .47), 9.5: (0, .12, .90, .48),
         10.0: (0, .10, .88, .44), 10.5: (0, .15, .97, .46), 11.0: (0, .20, .90, .56), 11.5: (.03, .24, .95, .52),
         12.0: (0, .24, 1, .42)}
pan = {0.0: (.28, .47, .54, .25), 0.5: (.28, .48, .54, .25), 1.0: (.27, .49, .55, .25), 1.5: (.27, .50, .55, .25),
       2.0: (.24, .52, .52, .24), 2.5: (.13, .53, .53, .24), 3.0: (0, .53, .48, .24), 3.5: (0, .54, .34, .24),
       4.0: (0, .54, .24, .22), 4.5: (0, .56, .20, .16), 5.0: (0, .57, .19, .20), 5.5: (0, .58, .24, .19),
       6.0: (0, .59, .30, .22), 6.5: (0, .59, .42, .23), 7.0: (.15, .59, .44, .22), 7.5: (.40, .58, .42, .22),
       8.0: (.62, .57, .38, .24), 8.5: (.78, .57, .22, .26), 9.0: (.82, .60, .18, .24), 9.5: (.82, .61, .18, .24)}
pot = {0.0: (.82, .35, .18, .30), 0.5: (.82, .36, .18, .30), 1.0: (.82, .37, .18, .30), 1.5: (.82, .38, .18, .30),
       2.0: (.76, .37, .24, .32), 2.5: (.68, .36, .32, .38), 3.0: (.48, .38, .52, .50), 3.5: (.34, .38, .66, .52),
       4.0: (.24, .40, .76, .42), 4.5: (.20, .40, .76, .42), 5.0: (.19, .48, .75, .44), 5.5: (.24, .48, .72, .44),
       6.0: (.30, .44, .70, .38), 6.5: (.42, .44, .58, .40), 7.0: (.60, .44, .40, .36), 7.5: (.82, .46, .18, .26)}
write({"mediaId": 4418, "level": "B", "keyWord": "burst", "defaultVoice": "female",
 "taps": [
  {"phrase": "to lift a heavy lid", "target": "the woman", "voice": "female", "keys": keys(t, woman)},
  {"phrase": "to have a long handle", "target": "the saucepan", "voice": "female", "keys": keys(t, pan)},
  {"phrase": "to bubble by the window", "target": "the open pot", "voice": "female", "keys": keys(t, pot)}],
 "stillS": 12.0,
 "nouns": [{"word": "steam", "x": .50, "y": .12, "voice": "female"}, {"word": "a lid", "x": .20, "y": .47, "voice": "female"},
           {"word": "an apron", "x": .58, "y": .56, "voice": "female"}, {"word": "a pot", "x": .55, "y": .82, "voice": "female"}],
 "question": "What happens when she lifts the lid?",
 "answer": ["A", "cloud", "of", "steam", "bursts", "out."], "answerVoice": "female",
 "notes": "Three pots: the small saucepan with the long black handle, the open boiling pot beside the window, the huge lidded pot (not a tap target). 'to have a long handle' is a state: no action fits only the saucepan. Saucepan off from 10.0 s (only a sliver of a pot at the right edge, not surely the saucepan); open pot off from 8.0 s. The woman's boxes are cut at the top edge of the pots in front of her; from 8.0 s her box includes the lid she holds. Question in the present simple (a sequence, not something going on). Still 12.0 s is hazy with steam but all four things are clear."})

# ---------- 4421
t = T(19)
girl = {0.0: (0, .08, 1, .92), 0.5: (0, .10, 1, .90), 1.0: (0, .13, 1, .87), 1.5: (0, .15, 1, .85),
        2.0: (.29, .08, .71, .76), 2.5: (.32, .10, .68, .64), 3.0: (.32, .13, .68, .74), 3.5: (.30, .17, .70, .70),
        4.0: (.28, .18, .68, .58), 4.5: (.28, .18, .66, .58), 5.0: (.28, .22, .66, .65), 5.5: (.28, .22, .66, .64),
        6.0: (.28, .20, .66, .56), 6.5: (.05, .45, .90, .55), 7.0: (.20, .68, .60, .32), 7.5: (.18, .72, .64, .28),
        8.0: (.26, .72, .56, .28), 8.5: (.26, .68, .56, .32), 9.0: (.26, .70, .56, .30)}
skel = {2.0: (0, 0, .29, .65), 2.5: (0, 0, .32, .62), 3.0: (0, 0, .32, .68), 3.5: (0, 0, .30, .68), 4.0: (0, 0, .28, .65),
        4.5: (0, 0, .28, .65), 5.0: (0, 0, .28, .68), 5.5: (0, 0, .28, .66), 6.0: (0, 0, .28, .62)}
dino = {6.5: (.30, 0, .48, .44), 7.0: (.36, 0, .46, .66), 7.5: (.40, 0, .42, .72), 8.0: (.40, 0, .40, .72),
        8.5: (.40, 0, .42, .68), 9.0: (.40, 0, .40, .70)}
write({"mediaId": 4421, "level": "A", "keyWord": "bone", "defaultVoice": "female",
 "taps": [
  {"phrase": "to hold a long bone", "target": "the girl", "voice": "female", "keys": keys(t, girl)},
  {"phrase": "to hang in the classroom", "target": "the skeleton", "voice": "female", "keys": keys(t, skel)},
  {"phrase": "to stand on big legs", "target": "the dinosaur", "voice": "female", "keys": keys(t, dino)}],
 "stillS": 2.0,
 "nouns": [{"word": "a bone", "x": .42, "y": .77, "voice": "female"}, {"word": "glasses", "x": .68, "y": .28, "voice": "female"},
           {"word": "a sweater", "x": .62, "y": .48, "voice": "female"}],
 "question": "What is the girl holding?",
 "answer": ["She", "is", "holding", "a", "long", "bone."], "answerVoice": "female",
 "notes": "'the girl' = the girl in the mustard sweater (other pupils sit far in the background). Classroom skeleton and girl overlap in the picture: the skeleton box is the left strip (spine, pole, left half of the pelvis, hanging hand); the right half of the pelvis and the arm bones in front of the girl fall in her box. Dinosaur: its legs stand behind her raised arm from 7.5 s; the split is a horizontal line above her head, so the dinosaur box holds the legs (and her raised hand) and the girl's box her head and body. 'to stand on big legs' is the weakest phrase (people in the hall stand too, but not on big legs). Several bones lie on the tray: the 'a bone' pill is on the one she lifts."})
