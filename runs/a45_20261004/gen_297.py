# writes content/297.json, 298.json, 299.json, 300.json
import json, os
H = os.path.dirname(os.path.abspath(__file__))
def keys(times, d):
    out = []
    for t in times:
        b = d.get(t)
        out.append({"t": t, "off": True} if b is None else {"t": t, "x": b[0], "y": b[1], "w": round(b[2], 2), "h": round(b[3], 2)})
    return out
def T(n): return [i * 0.5 for i in range(n)]
def save(c):
    json.dump(c, open(f"{H}/content/{c['mediaId']}.json", "w"), indent=1, ensure_ascii=False)

# ---------------- 297
t = T(21)
man = {0.0: (.60, .15, .40, .85), 1.5: (.45, .63, .55, .37), 2.0: (.52, .58, .48, .37), 2.5: (.68, .58, .32, .40),
       3.0: (.55, .59, .45, .38), 3.5: (.68, .58, .32, .40), 4.0: (.75, .52, .25, .48),
       6.0: (.71, .0, .29, .48), 6.5: (.77, .0, .23, .44), 7.0: (.50, .0, .50, .55),
       8.0: (.78, .49, .22, .18), 8.5: (.72, .12, .28, .68), 9.0: (.64, .25, .36, .70)}
wom = {1.5: (.82, .46, .18, .16), 2.5: (.80, .38, .20, .15), 3.0: (.80, .40, .20, .15),
       4.5: (.80, .17, .20, .43), 5.0: (.60, .13, .40, .50), 5.5: (.62, .0, .38, .64),
       6.0: (.45, .08, .26, .40), 6.5: (.43, .06, .33, .38), 7.5: (.68, .0, .32, .62),
       8.0: (.55, .0, .45, .49), 8.5: (.42, .19, .30, .43), 9.0: (.34, .34, .30, .38)}
fish = {4.5: (.10, .50, .35, .18), 5.0: (.08, .46, .46, .22), 5.5: (.28, .52, .30, .18),
        6.0: (.0, .50, .88, .14), 6.5: (.0, .46, 1.0, .20), 7.0: (.33, .56, .45, .18), 7.5: (.28, .54, .40, .24)}
save({"mediaId": 297, "level": "A", "keyWord": "fishing", "defaultVoice": "male",
 "taps": [
  {"phrase": "to hold a fishing rod", "target": "the man", "voice": "male", "keys": keys(t, man)},
  {"phrase": "to hold a net", "target": "the woman", "voice": "female", "keys": keys(t, wom)},
  {"phrase": "to swim in the lake", "target": "the fish", "voice": "male", "keys": keys(t, fish)}],
 "stillS": 6.5,
 "nouns": [{"word": "a fish", "x": .40, "y": .55, "voice": "male"}, {"word": "a net", "x": .45, "y": .78, "voice": "male"},
           {"word": "a cap", "x": .84, "y": .07, "voice": "male"}, {"word": "trees", "x": .22, "y": .12, "voice": "male"}],
 "question": "What are the man and woman doing?",
 "answer": ["They", "are", "fishing", "in", "the", "lake."], "answerVoice": "male",
 "notes": "Many cuts; the first shots show only hands, legs and the rod. Man: boxes on his visible part (hands/legs) in 1.5-4.0. Woman 1.5-3.0 = only her knee/net edge and her pointing hand in the teal sleeve (small boxes). 7.0: only a sliver of the woman's teal arm behind the man -> off. 8.0: man = only his fist at the right edge. 'to hold a net': she holds it 4.5-5.5; in 8.0-9.0 the net hangs at the left with no clear holder. Fish boxed 4.5-7.5 (splash, in the net, in the hands, in the water); 8.0 only a splash -> off. Key word 'fishing' is not a placeable noun, it is in the answer. A heron on a boat (9.5-10.0) is not used. defaultVoice male: mixed couple, odd id."})

# ---------------- 298
t = T(21)
bl = {0.0: (.26, .38, .28, .47), 2.0: (.25, .26, .32, .58), 2.5: (.15, .25, .39, .59), 3.0: (.17, .27, .37, .58),
      3.5: (.17, .27, .37, .58), 4.0: (.26, .42, .28, .41), 4.5: (.18, .25, .40, .59), 5.0: (.16, .25, .38, .60),
      5.5: (.18, .25, .38, .60), 6.0: (.15, .25, .40, .59), 6.5: (.32, .58, .25, .26), 8.0: (.20, .25, .37, .59),
      8.5: (.13, .25, .42, .59), 9.0: (.10, .27, .44, .58), 9.5: (.10, .27, .44, .58), 10.0: (.08, .27, .48, .57)}
fr = {}
for x in t: fr[x] = (.63, .50, .37, .24)
for x in (3.0, 3.5, 7.0, 7.5): fr[x] = (.58, .50, .42, .24)
for x in (6.0,): fr[x] = (.60, .50, .40, .24)
for x in (6.5, 8.0): fr[x] = (.59, .50, .41, .24)
fr[8.5] = (.65, .45, .35, .29); fr[9.0] = (.65, .39, .35, .35); fr[9.5] = (.65, .39, .35, .35); fr[10.0] = (.65, .40, .35, .34)
dog = {x: (.74, .36, .26, .14) for x in t if x <= 8.0}
dog[8.5] = (.74, .31, .26, .14)
save({"mediaId": 298, "level": "B", "keyWord": "fitting room", "defaultVoice": "female",
 "taps": [
  {"phrase": "to try on several outfits", "target": "the blonde woman", "voice": "female", "keys": keys(t, bl)},
  {"phrase": "to give a thumbs up", "target": "the dark-haired woman", "voice": "female", "keys": keys(t, fr)},
  {"phrase": "to rest on the counter", "target": "the dog", "voice": "female", "keys": keys(t, dog)}],
 "stillS": 3.5,
 "nouns": [{"word": "a curtain", "x": .15, "y": .40, "voice": "female"}, {"word": "a jumpsuit", "x": .36, "y": .62, "voice": "female"},
           {"word": "sandals", "x": .38, "y": .79, "voice": "female"}, {"word": "a dog", "x": .85, "y": .44, "voice": "female"}],
 "question": "What is the blonde woman doing?",
 "answer": ["She", "is", "trying", "on", "outfits", "in", "a", "fitting", "room."], "answerVoice": "female",
 "notes": "Fixed camera. Blonde woman is hidden behind the closed curtain at 0.5-1.5 and 7.0-7.5 (off); 0.0, 4.0, 6.5: only her legs. The dark-haired woman also gives a thumbs down at 3.0-3.5; thumbs up at 5.5 and 8.0-9.5. Dog: 9.0-10.0 the friend sits up in front of it and it is mostly hidden behind her head and hands -> off there, so the boxes do not overlap. Key word 'fitting room' is not placed as a noun (it is the whole booth, would collide with the curtain); it is in the answer."})

# ---------------- 299
t = T(29)
w = {0.0: (.10, .40, .42, .13), 0.5: (.10, .40, .27, .20), 1.0: (.10, .40, .39, .24), 1.5: (.10, .40, .23, .22),
     2.0: (.08, .40, .18, .16), 2.5: (.08, .40, .20, .16), 3.0: (.08, .40, .18, .15), 3.5: (.10, .40, .30, .20),
     4.0: (.10, .40, .35, .22), 4.5: (.08, .40, .21, .18), 5.0: (.10, .48, .60, .18), 5.5: (.10, .48, .60, .18),
     6.0: (.10, .48, .60, .18), 6.5: (.10, .48, .60, .18), 7.0: (.05, .48, .68, .20), 7.5: (.05, .42, .35, .28),
     8.0: (.03, .43, .38, .31), 8.5: (.03, .47, .62, .26), 9.0: (.03, .47, .60, .28), 9.5: (.04, .43, .33, .30),
     10.0: (.07, .39, .44, .33), 10.5: (.15, .35, .40, .33), 11.0: (.20, .34, .28, .40), 11.5: (.24, .35, .25, .41)}
for x in (12.0, 12.5, 13.0, 13.5, 14.0): w[x] = (.25, .36, .24, .40)
d = {0.0: (.22, .53, .50, .20), 0.5: (.37, .48, .38, .24), 1.0: (.49, .43, .24, .29), 1.5: (.33, .40, .38, .20),
     2.0: (.26, .38, .36, .21), 2.5: (.28, .38, .26, .27), 3.0: (.26, .42, .44, .26), 3.5: (.40, .44, .31, .24),
     4.0: (.45, .41, .33, .20), 4.5: (.29, .38, .38, .19), 5.0: (.23, .37, .37, .11), 5.5: (.20, .36, .40, .12),
     6.0: (.20, .36, .40, .12), 6.5: (.20, .36, .40, .12), 7.0: (.25, .34, .35, .14), 7.5: (.40, .34, .20, .20),
     8.0: (.41, .37, .24, .23), 8.5: (.20, .34, .40, .13), 9.0: (.28, .33, .20, .14), 9.5: (.37, .39, .23, .23),
     10.0: (.51, .40, .22, .22), 10.5: (.55, .41, .23, .20), 11.0: (.48, .40, .44, .21), 11.5: (.49, .40, .45, .24)}
for x in (12.0, 12.5, 13.0, 13.5, 14.0): d[x] = (.49, .39, .45, .24)
save({"mediaId": 299, "level": "A", "keyWord": "wake up", "defaultVoice": "female",
 "taps": [
  {"phrase": "to sleep in bed", "target": "the woman", "voice": "female", "keys": keys(t, w)},
  {"phrase": "to walk on the bed", "target": "the dog", "voice": "female", "keys": keys(t, d)},
  {"phrase": "to cover her face", "target": "the woman", "voice": "female", "keys": keys(t, w)}],
 "stillS": 12.5,
 "nouns": [{"word": "a pillow", "x": .16, "y": .48, "voice": "female"}, {"word": "a dog", "x": .72, "y": .48, "voice": "female"},
           {"word": "a blanket", "x": .42, "y": .76, "voice": "female"}, {"word": "a door", "x": .72, "y": .18, "voice": "female"}],
 "question": "What is the dog doing?",
 "answer": ["The", "dog", "is", "waking", "her", "up."], "answerVoice": "female",
 "notes": "Dark night-camera clip, only two targets (woman, dog), so two phrases share the woman. The dog walks over and stands on the lying woman in most frames: the two boxes are split along the line between them, so the woman's box often holds only head + upper body and her legs fall outside (0.5-4.5, 7.5-14.0), or (5.0-7.0, 8.5-9.0) the dog's box is the strip above her and the top of her head is cut. 'her' in the answer has no antecedent in the question (chosen so that the chips have one order: 'waking her up'). 'a woman' is not a noun slot: at 12.5 she sits between the pillow and the dog."})

# ---------------- 300
t = T(15)
g = {0.0: (.0, .33, 1.0, .21), 0.5: (.05, .33, .95, .19), 1.0: (.52, .44, .48, .56), 1.5: (.46, .38, .54, .62),
     2.0: (.45, .43, .55, .57), 4.0: (.45, .18, .55, .82), 4.5: (.10, .46, .90, .54), 5.0: (.40, .57, .60, .43),
     5.5: (.34, .67, .54, .33), 6.0: (.30, .67, .53, .33), 6.5: (.27, .67, .56, .33), 7.0: (.25, .68, .56, .32)}
f = {0.0: (.12, .54, .65, .46), 0.5: (.22, .52, .48, .48), 1.0: (.22, .27, .30, .38), 1.5: (.22, .25, .24, .38),
     2.0: (.22, .23, .23, .32), 2.5: (.27, .14, .22, .26), 3.0: (.32, .19, .36, .34), 3.5: (.27, .12, .73, .43),
     5.5: (.27, .0, .73, .28), 6.0: (.25, .02, .73, .32), 6.5: (.25, .02, .73, .32), 7.0: (.25, .04, .71, .32)}
save({"mediaId": 300, "level": "A", "keyWord": "flag", "defaultVoice": "female",
 "taps": [
  {"phrase": "to pull the rope", "target": "the girl", "voice": "female", "keys": keys(t, g)},
  {"phrase": "to wave in the wind", "target": "the flag", "voice": "female", "keys": keys(t, f)},
  {"phrase": "to look up at the flag", "target": "the girl", "voice": "female", "keys": keys(t, g)}],
 "stillS": 6.0,
 "nouns": [{"word": "a flag", "x": .60, "y": .18, "voice": "female"}, {"word": "the sky", "x": .60, "y": .40, "voice": "female"},
           {"word": "mountains", "x": .74, "y": .58, "voice": "female"}, {"word": "a girl", "x": .56, "y": .90, "voice": "female"}],
 "question": "What is the girl looking at?",
 "answer": ["She", "is", "looking", "at", "the", "flag."], "answerVoice": "female",
 "notes": "Only two targets (girl, flag); two phrases share the girl. 0.0-0.5 close-up: only her mittens and sleeves with the folded flag hanging under them - girl box = the mitten band, flag box = the folded cloth below (her jacket behind the cloth falls into the flag box). 4.0-5.0 close-ups of her mittens tying the rope / her face: girl on, flag off. 2.5-3.5 flag alone. 'the sky' pill sits in the blue between flag and mountains."})
