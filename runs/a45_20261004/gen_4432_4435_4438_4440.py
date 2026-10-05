import json, os
H = os.path.dirname(os.path.abspath(__file__))
def keys(times, d):
    out = []
    for t in times:
        b = d.get(t)
        out.append({"t": t, "off": True} if b is None else {"t": t, "x": b[0], "y": b[1], "w": b[2], "h": b[3]})
    return out
def T(n): return [i * 0.5 for i in range(n)]
def write(c):
    json.dump(c, open(f'{H}/content/{c["mediaId"]}.json', 'w'), indent=1, ensure_ascii=False)

# ---------- 4432
t = T(19)
braids = {0.0: (.27, .2, .73, .8), 0.5: (.44, .18, .56, .82), 1.0: (.32, .22, .68, .78), 1.5: (.18, .19, .72, .81), 2.0: (0, .2, .54, .8)}
coffee = {2.0: (.55, .35, .45, .65), 2.5: (.52, .34, .48, .66), 3.0: (0, .45, .5, .55), 3.5: (.13, .51, .37, .42)}
sales = {3.5: (.31, .26, .5, .24), 4.0: (.31, .23, .33, .3), 4.5: (.31, .23, .32, .27), 5.0: (.42, .24, .2, .16), 5.5: (.36, .24, .24, .24),
         6.0: (.34, .22, .28, .3), 6.5: (.44, .37, .18, .24), 7.0: (.42, .38, .18, .21), 7.5: (.42, .38, .18, .22), 8.0: (.42, .38, .18, .23),
         8.5: (.42, .42, .18, .19), 9.0: (.42, .42, .18, .19)}
write({"mediaId": 4432, "level": "B", "keyWord": "ignore", "defaultVoice": "male",
 "taps": [
  {"phrase": "to beckon to passing shoppers", "target": "the salesman", "voice": "male", "keys": keys(t, sales)},
  {"phrase": "to carry a takeaway coffee", "target": "the woman in the trench coat", "voice": "female", "keys": keys(t, coffee)},
  {"phrase": "to wear long braids", "target": "the woman in the mustard coat", "voice": "female", "keys": keys(t, braids)}],
 "stillS": 2.5,
 "nouns": [{"word": "a sale poster", "x": .2, "y": .2, "voice": "male"}, {"word": "glasses", "x": .35, "y": .38, "voice": "male"},
           {"word": "a paper cup", "x": .62, "y": .67, "voice": "male"}, {"word": "a tote bag", "x": .85, "y": .9, "voice": "male"}],
 "question": "What is the salesman doing?",
 "answer": ["He", "is", "beckoning", "to", "the", "passing", "shoppers."], "answerVoice": "male",
 "notes": "Key word 'ignore' is what the shoppers (all of them) do, so no phrase uses it for one target. Mustard-coat woman has no action unique to her: state phrase (braids). Salesman at 6.5 s in the wide shot is small and next to a man in a light shirt: box position is my best reading. Trench-coat woman at 4.0 s is only a sliver at the left edge: off."})

# ---------- 4435
woman = {0.0: (0, .12, 1, .88), 0.5: (0, .12, 1, .88), 1.0: (0, .11, 1, .89), 1.5: (0, .06, 1, .94), 2.0: (0, 0, 1, 1), 2.5: (0, 0, 1, 1),
         3.0: (0, .02, .88, .98), 3.5: (0, .04, .87, .96), 4.0: (0, .18, .7, .82), 4.5: (0, .19, .57, .81), 5.0: (0, .23, .66, .77),
         5.5: (0, .26, .58, .74), 6.0: (0, .24, .5, .76), 6.5: (0, .21, .5, .79), 7.0: (0, .34, .74, .66), 7.5: (0, .41, .74, .59),
         8.0: (0, .49, .66, .51), 8.5: (0, .51, .62, .49), 9.0: (.02, .51, .8, .49)}
giant = {5.0: (.55, 0, .45, .18), 5.5: (.45, 0, .55, .22), 6.0: (.35, 0, .65, .23), 6.5: (.3, 0, .7, .2), 7.0: (.2, 0, .8, .33),
         7.5: (.1, 0, .9, .4), 8.0: (0, 0, 1, .48), 8.5: (0, 0, 1, .5), 9.0: (0, 0, 1, .5)}
wk = keys(t, woman)
write({"mediaId": 4435, "level": "B", "keyWord": "exhibition", "defaultVoice": "female",
 "taps": [
  {"phrase": "to examine a brain model", "target": "the woman", "voice": "female", "keys": wk},
  {"phrase": "to point at an exhibit", "target": "the woman", "voice": "female", "keys": wk},
  {"phrase": "to glow bright pink", "target": "the giant brain", "voice": "female", "keys": keys(t, giant)}],
 "stillS": 0.0,
 "nouns": [{"word": "ceiling lights", "x": .5, "y": .07, "voice": "female"}, {"word": "a hair clip", "x": .36, "y": .28, "voice": "female"},
           {"word": "a brain model", "x": .53, "y": .62, "voice": "female"}, {"word": "a denim jacket", "x": .5, "y": .92, "voice": "female"}],
 "question": "What is the woman doing?",
 "answer": ["She", "is", "examining", "a", "model", "at", "an", "exhibition."], "answerVoice": "female",
 "notes": "Only two usable targets (woman, giant glowing brain); the woman carries two phrases. From 6.5 s the giant brain hangs over her head: boxes split on a horizontal line at her hair top, so the brain's lowest part (stem, right) falls outside its box. 'exhibition' is abstract, not used as a noun slot; it is in the answer."})

# ---------- 4438
t = T(25)
w = {0.0: (.04, .13, .9, .87), 0.5: (.25, .18, .72, .82), 1.0: (.03, .22, .95, .78), 1.5: (.17, .2, .65, .8),
     4.5: (.19, .34, .69, .66), 5.0: (.25, .37, .7, .63), 5.5: (.27, .4, .73, .6), 6.0: (.25, .41, .72, .59), 6.5: (.3, .45, .7, .55),
     7.0: (.33, .54, .65, .46), 7.5: (.33, .66, .65, .34), 8.0: (.38, .76, .62, .24), 8.5: (.47, .86, .5, .14), 9.0: (.45, .86, .5, .14),
     9.5: (.17, .38, .8, .62), 10.0: (.12, .4, .6, .6), 10.5: (.14, .44, .5, .56), 11.0: (.22, .44, .66, .56), 11.5: (.22, .47, .76, .53),
     12.0: (.2, .47, .55, .53)}
st = {5.0: (.6, 0, .4, .14), 5.5: (.5, 0, .5, .39), 6.0: (.22, 0, .78, .4), 6.5: (.08, 0, .9, .44), 7.0: (0, 0, .95, .53),
      7.5: (0, 0, .93, .65), 8.0: (.02, .07, .9, .64), 8.5: (.04, .11, .86, .63), 9.0: (.04, .13, .86, .71)}
wk = keys(t, w)
write({"mediaId": 4438, "level": "B", "keyWord": "parade", "defaultVoice": "female",
 "taps": [
  {"phrase": "to juggle a football", "target": "the woman", "voice": "female", "keys": wk},
  {"phrase": "to run ahead of dancers", "target": "the woman", "voice": "female", "keys": wk},
  {"phrase": "to tower over the crowd", "target": "the statue", "voice": "female", "keys": keys(t, st)}],
 "stillS": 12.0,
 "nouns": [{"word": "confetti", "x": .4, "y": .1, "voice": "female"}, {"word": "tower blocks", "x": .8, "y": .25, "voice": "female"},
           {"word": "a feather headdress", "x": .8, "y": .5, "voice": "female"}],
 "question": "What is she doing at the parade?",
 "answer": ["She", "is", "running", "ahead", "of", "the", "dancers."], "answerVoice": "female",
 "notes": "'the woman' = the red-haired woman (the dancers are several, never a tap target). The football overlaps her body, so it is not a separate target. From 5.5 s the statue stands behind her head: split on a horizontal line at her hair top, the plinth falls outside the statue box in 5.5-7.0 s. Running is taken from the description (stills show her moving ahead of the dancers). Several headdresses in the still: the pill sits on the right-hand one, no other noun names another. 'parade' is not a placeable thing; it is in the question."})

# ---------- 4440
t = T(19)
fw = {0.0: (0, .02, .7, .67), 0.5: (0, .11, .67, .6), 1.0: (0, .01, .74, .68), 1.5: (0, .05, .55, .65), 2.0: (0, .06, .7, .65),
      2.5: (0, .05, .72, .65), 3.0: (0, .05, .74, .62), 3.5: (0, .08, .75, .6), 4.0: (0, .03, .67, .64), 4.5: (0, .02, .68, .95),
      5.0: (0, .1, .65, .9), 5.5: (.06, .15, .51, .82), 6.0: (0, .13, .54, .78), 6.5: (0, .14, .55, .78), 7.0: (0, .14, .5, .86),
      7.5: (0, .12, .59, .44), 8.0: (0, .12, .56, .44), 8.5: (0, .12, .54, .88), 9.0: (0, .08, .57, .92)}
bo = {0.0: (.23, .7, .77, .2), 0.5: (.25, .72, .75, .2), 1.0: (.25, .7, .75, .17), 1.5: (.3, .71, .7, .17), 2.0: (.35, .72, .65, .17),
      2.5: (.3, .71, .7, .16), 3.0: (.26, .68, .74, .16), 3.5: (.25, .69, .75, .15), 4.0: (.21, .68, .79, .18)}
sl = {5.5: (.58, .26, .42, .74), 6.0: (.55, .25, .45, .75), 6.5: (.56, .24, .44, .76), 7.0: (.51, .38, .49, .62), 7.5: (.5, .57, .5, .43),
      8.0: (.48, .57, .5, .43), 8.5: (.55, .58, .45, .42), 9.0: (.58, .6, .42, .4)}
write({"mediaId": 4440, "level": "B", "keyWord": "strike", "defaultVoice": "female",
 "taps": [
  {"phrase": "to strike a wooden board", "target": "the woman in front", "voice": "female", "keys": keys(t, fw)},
  {"phrase": "to snap in half", "target": "the wooden boards", "voice": "female", "keys": keys(t, bo)},
  {"phrase": "to crumble at the top", "target": "the stack of slabs", "voice": "female", "keys": keys(t, sl)}],
 "stillS": 6.0,
 "nouns": [{"word": "trees", "x": .6, "y": .08, "voice": "female"},            {"word": "a black belt", "x": .2, "y": .49, "voice": "female"}, {"word": "concrete slabs", "x": .76, "y": .58, "voice": "female"}],
 "question": "What is the woman in front doing?",
 "answer": ["She", "is", "striking", "a", "stack", "of", "concrete", "slabs."], "answerVoice": "female",
 "notes": "The boards lie in front of her legs (0-4.0 s): boxes split on a horizontal line at the board top, her lower legs fall outside her box there. At 7.5 and 8.0 s the same split against the slab stack. Blue tile block (4.5-5.0 s) is no target. Background students also wear black belts, but small; the belt pill is on the main woman."})
