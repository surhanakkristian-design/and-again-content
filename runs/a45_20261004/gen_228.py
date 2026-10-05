import json, os
RUN = os.path.dirname(os.path.abspath(__file__))

def keys(times, d):
    out = []
    for t in times:
        b = d.get(t)
        if b is None:
            out.append({"t": t, "off": True})
        else:
            x0, y0, x1, y1 = b
            out.append({"t": t, "x": round(x0, 2), "y": round(y0, 2), "w": round(x1 - x0, 2), "h": round(y1 - y0, 2)})
    return out

def T(n):
    return [i * 0.5 for i in range(n)]

docs = {}

# ---------------- 228 ----------------
t = T(21)
woman = {0.5: (.60, .14, .82, .47), 1.0: (.25, .15, .79, .62), 1.5: (.18, .15, .84, .72), 2.0: (.20, .17, .88, .70),
         2.5: (.17, .14, .97, .70), 3.0: (.10, .25, .95, .80), 3.5: (0, .28, .18, .78), 4.0: (0, .24, .15, .72),
         4.5: (0, .21, .13, .72), 5.0: (0, .27, .10, .60), 8.5: (0, .42, .22, .90), 9.0: (0, .45, .31, .95),
         9.5: (0, .45, .31, .95), 10.0: (.02, .45, .31, .86)}
man = {0.0: (.55, 0, 1, .62), 0.5: (.82, 0, 1, .62), 1.0: (.80, .52, 1, .70), 3.5: (.68, .10, 1, .58),
       4.0: (.64, .08, 1, .55), 4.5: (.68, .04, 1, .53), 5.0: (.72, .14, 1, .62), 5.5: (.76, .17, 1, .62),
       6.0: (.62, .25, 1, .47), 6.5: (.50, .28, 1, .52), 7.0: (.46, .25, 1, .60), 7.5: (.59, .28, 1, .62),
       8.0: (.62, .30, 1, .64), 8.5: (.66, .33, 1, .78), 9.0: (.63, .40, 1, .92), 9.5: (.62, .41, 1, .92),
       10.0: (.62, .43, 1, .84)}
cat = {3.5: (.42, .35, .60, .49), 4.0: (.42, .33, .60, .47), 4.5: (.45, .31, .63, .45), 5.0: (.46, .30, .64, .44),
       5.5: (.48, .28, .66, .42), 6.0: (.44, .28, .62, .42),        7.5: (.40, .34, .58, .48), 8.0: (.42, .35, .60, .49), 8.5: (.43, .38, .61, .52), 9.0: (.44, .42, .62, .56),
       9.5: (.43, .43, .61, .57), 10.0: (.43, .44, .61, .58)}
docs[228] = {
    "mediaId": 228, "level": "A", "keyWord": "dinner", "defaultVoice": "female",
    "taps": [
        {"phrase": "to carry a hot pot", "target": "the woman with the pot", "voice": "female", "keys": keys(t, woman)},
        {"phrase": "to light a candle", "target": "the man", "voice": "male", "keys": keys(t, man)},
        {"phrase": "to sit on the wall", "target": "the cat", "voice": "female", "keys": keys(t, cat)},
    ],
    "stillS": 4.0,
    "nouns": [
        {"word": "a cat", "x": 0.52, "y": 0.39, "voice": "female"},
        {"word": "a pot", "x": 0.45, "y": 0.57, "voice": "female"},
        {"word": "a salad", "x": 0.55, "y": 0.70, "voice": "female"},
        {"word": "bread", "x": 0.68, "y": 0.87, "voice": "female"},
    ],
    "question": "What are the people doing?",
    "answer": ["They", "are", "having", "dinner", "together."],
    "answerVoice": "female",
    "notes": "Clip has cuts and four people. 'the woman with the pot' = the woman with the bun; after 3.5 s she sits at the left edge (off 5.5-8.0 where only the dark-haired woman is in frame). 'the man' = the man who lights the candle at 0-1 s; from 8.5 s two similar bearded men sit side by side on the right, the box there covers both (cannot tell them apart for a tap). Man box at 0.5 s misses his hand so it does not overlap the woman. Cat hidden behind the raised glass and arm at 6.5-7.0 s (off).",
}

# ---------------- 229 ----------------
t = T(19)
grad = {0.0: (.20, .28, 1, .95), 0.5: (0, .26, .82, .88), 1.0: (.22, .25, .88, .95), 1.5: (.46, .26, .86, .95),
        2.0: (.35, .22, .72, .95), 2.5: (.25, .22, .78, .95), 3.0: (.08, .24, .75, 1), 3.5: (.17, .24, .83, 1),
        4.0: (.15, .30, .72, 1), 4.5: (.17, .27, .90, 1), 5.0: (.12, .22, .85, 1), 5.5: (.34, .25, .88, 1),
        6.0: (0, .40, 1, 1), 6.5: (.10, .26, 1, 1), 7.0: (.12, .23, 1, 1), 7.5: (0, .21, 1, 1), 8.0: (.05, .21, 1, 1),
        8.5: (0, .24, 1, 1), 9.0: (0, .24, 1, 1)}
old = {1.0: (0, .28, .22, .92), 1.5: (.03, .30, .46, .95), 2.0: (.72, .32, .98, .85), 2.5: (.82, .40, 1, .95)}
dip = {5.5: (.02, .57, .34, .76), 6.0: (.12, .26, .68, .40), 6.5: (.36, .11, .88, .26), 7.0: (.40, .08, .92, .23),
       7.5: (.26, .06, .82, .21), 8.0: (.33, .07, .85, .21), 8.5: (.30, .10, .84, .24), 9.0: (.25, .10, .80, .24)}
docs[229] = {
    "mediaId": 229, "level": "B", "keyWord": "diploma", "defaultVoice": "male",
    "taps": [
        {"phrase": "to stride across the stage", "target": "the graduate", "voice": "male", "keys": keys(t, grad)},
        {"phrase": "to congratulate the graduate", "target": "the older man", "voice": "male", "keys": keys(t, old)},
        {"phrase": "to be tied with a ribbon", "target": "the diploma", "voice": "male", "keys": keys(t, dip)},
    ],
    "stillS": 8.0,
    "nouns": [
        {"word": "a diploma", "x": 0.58, "y": 0.14, "voice": "male"},
        {"word": "a graduation cap", "x": 0.57, "y": 0.31, "voice": "male"},
        {"word": "a gown", "x": 0.22, "y": 0.52, "voice": "male"},
        {"word": "a sash", "x": 0.55, "y": 0.76, "voice": "male"},
    ],
    "question": "What is the graduate doing?",
    "answer": ["He", "is", "lifting", "his", "diploma", "above", "his", "head."],
    "answerVoice": "male",
    "notes": "The diploma is held by the graduate, so the two boxes are split along a horizontal line under the scroll (6.0 s: the scroll is in front of his cap, graduate box starts below it; 5.5 s: scroll is left of his body). 'the older man' = the official in the black gown and hat who shakes his hand at 1.0-1.5 s (at 2.5 s only his gown at the right edge). 'a sash' = the gold stole; 'a gown' pill sits on the sleeve.",
}

# ---------------- 231 ----------------
t = T(19)
wom = {0.0: (.17, .25, .95, .60), 0.5: (.22, .25, .97, .61), 1.0: (.20, .24, 1, .62), 1.5: (0, .08, 1, .63),
       2.0: (.55, .20, 1, .62), 2.5: (.55, .20, 1, .62), 3.0: (.53, .24, 1, .62), 3.5: (.53, .24, 1, .62),
       4.0: (.44, .28, 1, .63), 4.5: (.48, .23, 1, .66), 5.0: (.46, .24, 1, .66), 5.5: (.46, .24, 1, .67),
       6.0: (.42, .23, 1, .67), 6.5: (.20, .23, 1, .67), 7.0: (.18, .26, 1, .66), 7.5: (.16, .26, 1, .66),
       8.0: (.17, .26, .95, .69), 8.5: (.17, .30, .93, .67), 9.0: (.19, .31, .93, .66)}
man = {2.0: (0, .08, .55, .62), 2.5: (0, .06, .55, .62), 3.0: (0, .10, .53, .62), 3.5: (0, .10, .53, .62),
       4.0: (0, .08, .44, .55), 4.5: (0, .03, .48, .50), 5.0: (0, .02, .46, .58), 5.5: (0, .02, .46, .60),
       6.0: (0, 0, .42, .55), 6.5: (0, .47, .20, .67)}
can = {0.0: (.41, .60, .59, .81), 0.5: (.41, .61, .59, .82), 1.0: (.41, .62, .59, .84), 1.5: (.41, .63, .59, .86),
       2.0: (.42, .62, .60, .82), 2.5: (.42, .62, .60, .82), 3.0: (.42, .62, .60, .82), 3.5: (.42, .62, .60, .82),
       4.0: (.42, .63, .60, .84), 4.5: (.42, .66, .60, .89), 5.0: (.42, .66, .60, .91), 5.5: (.42, .67, .60, .92),
       6.0: (.43, .67, .61, .91), 6.5: (.44, .67, .62, .91), 7.0: (.43, .66, .61, .89), 7.5: (.43, .66, .61, .87),
       8.0: (.43, .69, .61, .85), 8.5: (.44, .67, .62, .82), 9.0: (.42, .66, .60, .80)}
docs[231] = {
    "mediaId": 231, "level": "B", "keyWord": "disappoint", "defaultVoice": "female",
    "taps": [
        {"phrase": "to burst into tears", "target": "the woman", "voice": "female", "keys": keys(t, wom)},
        {"phrase": "to pat her shoulder", "target": "the man", "voice": "male", "keys": keys(t, man)},
        {"phrase": "to flicker on the table", "target": "the candle", "voice": "female", "keys": keys(t, can)},
    ],
    "stillS": 1.0,
    "nouns": [
        {"word": "fairy lights", "x": 0.50, "y": 0.05, "voice": "female"},
        {"word": "a candle", "x": 0.50, "y": 0.66, "voice": "female"},
        {"word": "spaghetti", "x": 0.26, "y": 0.76, "voice": "female"},
        {"word": "a present", "x": 0.72, "y": 0.75, "voice": "female"},
    ],
    "question": "What is the woman doing?",
    "answer": ["She", "is", "bursting", "into", "tears", "at", "the", "table."],
    "answerVoice": "female",
    "notes": "The candle stands in front of the woman, so her box ends at the top of the flame (head and upper body only) and the candle box lies below it. The candle is out from 8.0 s (it flickers 0-7.5 s). The man rests his hand on her shoulder at 5.0-6.5 s ('to pat her shoulder'); at 6.5 s only his arm is left in frame. Key word 'disappoint' is a verb whose sense needs the story, so it is not used in a phrase or the answer. Nouns on the still sit in one band: candle pill is on the flame/upper candle, spaghetti and present pills about 0.10 lower.",
}

# ---------------- 232 ----------------
t = T(21)
man = {0.0: (.15, .20, 1, .80), 0.5: (.10, .18, 1, .80), 1.0: (.03, .17, 1, .76), 1.5: (.08, .14, 1, .63),
       2.0: (0, .13, 1, .53), 2.5: (0, .15, 1, .53), 3.0: (0, .14, 1, .47), 3.5: (0, .14, 1, .44),
       4.0: (0, .13, 1, .41), 4.5: (0, .14, 1, .45), 5.0: (0, .14, 1, .47), 5.5: (0, .14, 1, .48),
       6.0: (.15, .17, 1, .49), 6.5: (.18, .14, 1, .47), 7.0: (.20, .14, 1, .49), 7.5: (.28, .13, 1, .59),
       8.0: (.26, .13, 1, .60), 8.5: (.26, .13, 1, .60), 9.0: (.25, .13, 1, .60), 9.5: (.28, .12, 1, .60),
       10.0: (.27, .12, 1, .60)}
tray = {1.0: (.68, .76, 1, .96), 1.5: (.48, .63, 1, .80), 2.0: (.30, .53, .92, .67), 2.5: (.30, .53, .88, .65),
        3.0: (.28, .47, .87, .60), 3.5: (.28, .44, .87, .59), 4.0: (.28, .41, .87, .55), 4.5: (.30, .45, .87, .59),
        5.0: (.28, .47, .85, .61), 5.5: (.28, .48, .87, .62), 6.0: (.30, .49, .85, .63), 6.5: (.28, .47, .85, .61),
        7.0: (.23, .49, .80, .63), 7.5: (.25, .59, .82, .73), 8.0: (.22, .60, .80, .74), 8.5: (.23, .60, .82, .74),
        9.0: (.21, .60, .80, .74), 9.5: (.21, .60, .80, .74), 10.0: (.22, .60, .81, .74)}
mk = keys(t, man)
docs[232] = {
    "mediaId": 232, "level": "B", "keyWord": "disappointed", "defaultVoice": "male",
    "taps": [
        {"phrase": "to rub his hands eagerly", "target": "the man in the raincoat", "voice": "male", "keys": mk},
        {"phrase": "to look deeply disappointed", "target": "the man in the raincoat", "voice": "male", "keys": mk},
        {"phrase": "to contain a tiny portion", "target": "the man's tray", "voice": "male", "keys": keys(t, tray)},
    ],
    "stillS": 8.5,
    "nouns": [
        {"word": "a beanie", "x": 0.52, "y": 0.19, "voice": "male"},
        {"word": "a beard", "x": 0.52, "y": 0.34, "voice": "male"},
        {"word": "a raincoat", "x": 0.50, "y": 0.50, "voice": "male"},
        {"word": "a tray", "x": 0.50, "y": 0.66, "voice": "male"},
    ],
    "question": "How does the man in front look?",
    "answer": ["He", "looks", "disappointed", "with", "his", "empty", "tray."],
    "answerVoice": "male",
    "notes": "One main person only, so two phrases share him. The tray is held in front of his body, so his box is the part above the tray (head and chest) and the tray box lies below it. Tray holds the tiny bite only at 1.5-5.5 s and is empty afterwards (still boxed, same tray). A stack of other trays stands on the counter at 0-5.5 s, hence the target name 'the man's tray'. From 6.0 s a blurred man with glasses stands at the left; the main man's box starts right of him. Question uses present simple because it asks about a state.",
}

for i, d in docs.items():
    with open(os.path.join(RUN, "content", f"{i}.json"), "w") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
print("ok")
