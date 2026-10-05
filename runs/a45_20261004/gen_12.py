# writer helper for media 12, 14, 15, 16
import json
def K(times, d):
    out = []
    for t in times:
        b = d.get(t)
        if b is None: out.append({"t": t, "off": True})
        else:
            x, y, x2, y2 = b
            out.append({"t": t, "x": round(x, 2), "y": round(y, 2), "w": round(x2 - x, 2), "h": round(y2 - y, 2)})
    return out
def T(n): return [i * 0.5 for i in range(n)]
def save(c): json.dump(c, open(f'content/{c["mediaId"]}.json', 'w'), indent=1, ensure_ascii=False)

# ---------- 12
t = T(13)
man = {0.5: (.08, .41, .33, .73), 1.0: (.29, .41, .57, .72), 1.5: (.47, .41, .61, .74), 2.0: (.50, .41, .71, .72),
       2.5: (.57, .40, .73, .72), 3.0: (.57, .39, .75, .74), 3.5: (.56, .39, .74, .74), 4.0: (.56, .39, .74, .72),
       4.5: (.51, .39, .69, .72), 5.0: (.48, .40, .66, .75), 5.5: (.51, .40, .69, .75), 6.0: (.54, .39, .72, .70)}
wom = {1.0: (.64, .41, .94, .72), 1.5: (.31, .41, .47, .74), 2.0: (.26, .41, .50, .72),
       2.5: (.37, .40, .57, .72), 3.0: (.39, .39, .57, .74), 3.5: (.38, .39, .56, .74), 4.0: (.38, .39, .56, .72),
       4.5: (.33, .39, .51, .72), 5.0: (.30, .40, .48, .75), 5.5: (.33, .40, .51, .75), 6.0: (.36, .39, .54, .70)}
sunc = {0.0: (.24, .29), 0.5: (.24, .33), 1.0: (.24, .33), 1.5: (.27, .34), 2.0: (.44, .33), 2.5: (.54, .32), 3.0: (.54, .31),
        3.5: (.50, .32), 4.0: (.47, .31), 4.5: (.44, .31), 5.0: (.44, .30), 5.5: (.47, .30), 6.0: (.49, .30)}
sun = {k: (x - .11, y - .09, x + .11, y + .07) for k, (x, y) in sunc.items()}
save({"mediaId": 12, "level": "A", "keyWord": "to hug", "defaultVoice": "female",
 "taps": [
  {"phrase": "to have short hair", "target": "the man", "voice": "male", "keys": K(t, man)},
  {"phrase": "to have long hair", "target": "the woman", "voice": "female", "keys": K(t, wom)},
  {"phrase": "to shine in the sky", "target": "the sun", "voice": "female", "keys": K(t, sun)}],
 "stillS": 1.0,
 "nouns": [{"word": "the sun", "x": .24, "y": .33, "voice": "female"}, {"word": "a man", "x": .40, "y": .52, "voice": "male"},
           {"word": "a woman", "x": .78, "y": .60, "voice": "female"}, {"word": "grass", "x": .50, "y": .86, "voice": "female"}],
 "question": "What are the man and woman doing?",
 "answer": ["They", "are", "hugging", "in", "the", "grass."], "answerVoice": "female",
 "notes": "Both people run and hug, so the two person phrases are states (hair length); from 1.5 s on the two overlap, boxes are split at the line between them. Man and woman are off at 0.0 (only a hand at the edge)."})

# ---------- 14
t = T(27)
hands = {0.0: (.04, .54, 1, 1), 0.5: (0, .55, 1, 1), 1.0: (0, .64, .95, 1), 1.5: (0, .64, 1, 1), 2.0: (0, .50, 1, 1),
         5.5: (.61, .15, 1, 1), 6.0: (.57, .16, 1, 1), 6.5: (0, .66, 1, 1), 7.0: (0, .67, 1, 1), 7.5: (0, .67, 1, 1),
         11.5: (.80, .47, 1, 1), 12.0: (.82, .47, 1, 1), 12.5: (.82, .47, 1, 1), 13.0: (.82, .48, 1, 1)}
flower = {2.5: (.36, .39, .82, .67), 3.0: (.38, .42, .82, .71), 3.5: (.38, .42, .82, .71), 4.0: (.38, .42, .82, .68),
          4.5: (.38, .42, .82, .68), 5.0: (.38, .42, .82, .70), 5.5: (.40, .44, .60, .63), 6.0: (.39, .46, .57, .64),
          6.5: (.42, .45, .78, .65), 7.0: (.42, .46, .77, .66), 7.5: (.42, .46, .80, .66),
          8.0: (.34, .44, .63, .68), 8.5: (.34, .44, .66, .68), 9.0: (.34, .43, .55, .68), 9.5: (.34, .44, .64, .68),
          10.0: (.34, .44, .68, .68), 10.5: (.34, .44, .72, .68), 11.0: (.34, .44, .61, .67),
          11.5: (.60, .62, .79, .76), 12.0: (.62, .63, .81, .77), 12.5: (.62, .63, .81, .77), 13.0: (.61, .63, .81, .77)}
brush = {8.0: (.63, .52, 1, .72), 8.5: (.66, .52, 1, .72), 9.0: (.55, .52, 1, .74), 9.5: (.64, .52, 1, .72),
         10.0: (.68, .48, 1, .68), 10.5: (.72, .54, 1, .72), 11.0: (.61, .53, 1, .74)}
save({"mediaId": 14, "level": "A", "keyWord": "page", "defaultVoice": "female",
 "taps": [
  {"phrase": "to open a notebook", "target": "the hands", "voice": "female", "keys": K(t, hands)},
  {"phrase": "to be bright yellow", "target": "the flower", "voice": "female", "keys": K(t, flower)},
  {"phrase": "to brush the green leaves", "target": "the brush", "voice": "female", "keys": K(t, brush)}],
 "stillS": 10.5,
 "nouns": [{"word": "a page", "x": .35, "y": .20, "voice": "female"}, {"word": "a flower", "x": .50, "y": .54, "voice": "female"},
           {"word": "a brush", "x": .86, "y": .63, "voice": "female"}, {"word": "a table", "x": .60, "y": .88, "voice": "female"}],
 "question": "What is on the page?",
 "answer": ["There", "is", "a", "yellow", "flower", "on", "the", "page."], "answerVoice": "female",
 "notes": "Hands, flower and brush overlap in the picture (fingers on the flower 5.5-7.5 s, brush tip on the leaves 8-11 s): boxes are split, so the hands box covers only one hand in some frames and the flower box is cut at the brush. Tweezers (2.5-5.0 s) are no target. The flower phrase is a state."})

# ---------- 15
t = T(17)
man = {0.0: (0, .09, .59, 1), 0.5: (0, .28, .53, 1), 1.0: (0, .28, .54, 1),
       4.0: (0, .08, 1, .80), 4.5: (0, .08, .71, 1), 5.0: (0, .08, .70, .44), 5.5: (0, .08, 1, 1), 6.0: (0, .08, 1, 1),
       6.5: (0, .25, .55, 1), 7.0: (0, .27, .55, 1), 7.5: (0, .29, .55, 1), 8.0: (0, .16, .44, 1)}
wom = {0.0: (.60, .22, 1, 1), 0.5: (.53, .20, 1, 1), 1.0: (.56, .22, 1, 1), 1.5: (0, .60, 1, 1), 2.0: (0, .62, 1, 1),
       2.5: (.12, 0, 1, .80), 3.0: (.13, .05, 1, .91), 3.5: (0, 0, 1, .68),
       6.5: (.60, .22, 1, 1), 7.0: (.62, .22, 1, 1), 7.5: (.62, .22, 1, 1), 8.0: (.44, .16, .76, .66)}
pill = {1.5: (.44, .45, .62, .59), 2.0: (.44, .47, .62, .61), 4.0: (.76, .81, .96, .96), 4.5: (.72, .35, .90, .49),
        5.0: (.37, .45, .55, .59)}
save({"mediaId": 15, "level": "A", "keyWord": "pill", "defaultVoice": "male",
 "taps": [
  {"phrase": "to drink some water", "target": "the man", "voice": "male", "keys": K(t, man)},
  {"phrase": "to pour some water", "target": "the woman", "voice": "female", "keys": K(t, wom)},
  {"phrase": "to lie in a hand", "target": "the pill", "voice": "male", "keys": K(t, pill)}],
 "stillS": 1.5,
 "nouns": [{"word": "a pill", "x": .53, "y": .52, "voice": "male"}, {"word": "a hand", "x": .35, "y": .67, "voice": "male"},
           {"word": "a tree", "x": .72, "y": .22, "voice": "male"}],
 "question": "What is the man doing?",
 "answer": ["He", "is", "taking", "a", "pill", "with", "water."], "answerVoice": "male",
 "notes": "Close-ups 1.5-3.5 s show only the woman's hands (teal sleeves): her box is on the hand / arms there. The pill lies inside the hand (1.5, 2.0, 4.0) and on the man's tongue (5.0): the person box is split away from the small pill box, so at 5.0 the man's box is only the top of his head. The still is the close-up at 1.5 s so that the key word is a noun; the tree behind is blurred."})

# ---------- 16
t = T(31)
W = {0.0: (.20, .30, .62, .56), 0.5: (.12, .24, .68, .63), 1.0: (.09, .24, .71, .62), 1.5: (.09, .23, .73, .62),
     2.0: (.07, .21, .69, .60), 2.5: (.09, .22, .69, .61), 3.0: (.12, .22, .65, .61), 3.5: (.12, .21, .65, .61),
     4.0: (.12, .22, .64, .60), 4.5: (.13, .22, .64, .61), 5.0: (.13, .23, .65, .61), 5.5: (.13, .22, .65, .61),
     6.0: (0, .30, .43, .62), 6.5: (0, .31, .60, .63), 7.0: (0, .31, .60, .64), 7.5: (0, .31, .60, .64),
     8.0: (0, .30, .57, .62), 8.5: (0, .30, .35, .62), 9.0: (0, .30, .34, .63), 9.5: (0, .30, .39, .63),
     10.0: (0, .28, .44, .61), 10.5: (0, .28, .44, .61), 11.0: (.07, .16, .78, .73), 11.5: (.05, .15, .80, .75),
     12.0: (.02, .09, .81, .74), 12.5: (.02, .11, .82, .77), 13.0: (.04, .11, .82, .77), 13.5: (.05, .09, .82, .75),
     14.0: (.07, .09, .82, .74), 14.5: (.02, .10, .82, .75), 15.0: (.02, .11, .82, .76)}
S = {0.0: (.62, .09, 1, .56), 0.5: (.68, 0, 1, .60), 1.0: (.71, 0, 1, .60), 1.5: (.73, 0, 1, .60), 2.0: (.69, 0, 1, .60),
     2.5: (.69, 0, 1, .60), 3.0: (.65, 0, 1, .61), 3.5: (.65, 0, 1, .61), 4.0: (.64, 0, 1, .60), 4.5: (.64, 0, 1, .60),
     5.0: (.65, 0, 1, .61), 5.5: (.65, 0, 1, .61), 6.0: (.43, .05, 1, .62), 6.5: (.60, .08, 1, .63), 7.0: (.60, .07, 1, .64),
     7.5: (.60, .07, 1, .64), 8.0: (.57, .05, 1, .62), 8.5: (.35, .05, 1, .62), 9.0: (.34, .07, 1, .63), 9.5: (.39, .06, 1, .63),
     10.0: (.44, .03, 1, .61), 10.5: (.44, .03, 1, .61), 11.0: (.78, 0, 1, .70), 11.5: (.80, 0, 1, .75), 12.0: (.81, 0, 1, .72),
     12.5: (.82, 0, 1, .75), 13.0: (.82, 0, 1, .72), 13.5: (.82, 0, 1, .72), 14.0: (.82, 0, 1, .72), 14.5: (.82, 0, 1, .72),
     15.0: (.82, 0, 1, .70)}
Ctop = {0.0: .56, 0.5: .63, 1.0: .62, 1.5: .62, 2.0: .60, 2.5: .61, 3.0: .61, 3.5: .61, 4.0: .60, 4.5: .61, 5.0: .61, 5.5: .61,
        6.0: .62, 6.5: .63, 7.0: .64, 7.5: .64, 8.0: .62, 8.5: .62, 9.0: .63, 9.5: .63, 10.0: .61, 10.5: .61}
C = {k: (0, v, 1, 1) for k, v in Ctop.items()}
C.update({11.0: (0, .73, .36, 1), 11.5: (0, .75, .30, 1), 12.0: (0, .74, .32, 1), 12.5: (0, .77, .33, 1), 13.0: (0, .77, .32, 1),
          13.5: (0, .75, .36, 1), 14.0: (0, .74, .36, 1), 14.5: (0, .75, .36, 1), 15.0: (0, .76, .33, 1)})
save({"mediaId": 16, "level": "B", "keyWord": "presentation", "defaultVoice": "female",
 "taps": [
  {"phrase": "to deliver a presentation", "target": "the student in red", "voice": "female", "keys": K(t, W)},
  {"phrase": "to display the slides", "target": "the screen", "voice": "female", "keys": K(t, S)},
  {"phrase": "to sit in the audience", "target": "the classmates", "voice": "female", "keys": K(t, C)}],
 "stillS": 0.0,
 "nouns": [{"word": "a presentation", "x": .72, "y": .30, "voice": "female"}, {"word": "a sweater", "x": .42, "y": .50, "voice": "female"},
           {"word": "a whiteboard", "x": .20, "y": .32, "voice": "female"}, {"word": "an audience", "x": .64, "y": .66, "voice": "female"}],
 "question": "What is the student in red doing?",
 "answer": ["She", "is", "delivering", "a", "presentation", "to", "her", "classmates."], "answerVoice": "female",
 "notes": "The student stands in front of the screen and behind the classmates' heads: her box is cut at the top of the heads (legs left out) and the screen box starts at her right edge. From 11 s on only one classmate's head is left in the bottom-left corner. 'a presentation' labels the slides on the screen; the bullet points only appear from 6 s."})
