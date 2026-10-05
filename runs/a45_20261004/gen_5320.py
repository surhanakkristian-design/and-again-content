import sys; sys.path.insert(0, '/Users/kristiansurhanak/Projects/and-again-content/runs/a45_20261004')
from gen_5318_5320_5321_5322_lib import K, write
woman = K([
 (0.0, 0, .28, .60, .72), (0.5, 0, .29, .67, .71), (1.0, 0, .30, .66, .70), (1.5, 0, .28, .62, .72),
 (2.0, 0, .28, .44, .72), (2.5, 0, .31, .32, .69),
 (3.0, 0, .61, .42, .39), (3.5, 0, .43, .47, .57), (4.0, 0, .48, .43, .52), (4.5, 0, .53, .45, .47),
 (5.0, 0, .68, .48, .32), (5.5, 0, .69, .50, .31), (6.0, 0, .69, .50, .31), (6.5, 0, .70, .35, .30),
 (7.0, 0, .74, .18, .26), (7.5, 0, .74, .18, .26), (8.0, 0, .70, .18, .26), (8.5, 0, .70, .18, .30), (9.0, 0, .70, .16, .30)])
man = K([
 (0.0, .62, .11, .38, .89), (0.5, .69, .12, .31, .88), (1.0, .67, .13, .33, .87), (1.5, .64, .12, .36, .88),
 (2.0, .55, .12, .45, .88), (2.5, .47, .11, .53, .89),
 (3.0, .38, .14, .54, .46), (3.5, .48, .15, .37, .85), (4.0, .44, .13, .40, .87), (4.5, .46, .11, .40, .89),
 (5.0, .30, .10, .58, .57), (5.5, .30, .10, .70, .58), (6.0, .29, .03, .71, .65), (6.5, .36, 0, .56, 1.0),
 (7.0, .20, 0, .52, 1.0), (7.5, .22, 0, .58, 1.0), (8.0, .19, .26, .81, .74), (8.5, .20, .24, .76, .76), (9.0, .17, .23, .60, .77)])
write({
 "mediaId": 5320, "level": "B", "keyWord": "demonstrate", "defaultVoice": "female",
 "taps": [
  {"phrase": "to twist a spine model", "target": "the woman", "voice": "female", "keys": woman},
  {"phrase": "to press his lower back", "target": "the woman", "voice": "female", "keys": woman},
  {"phrase": "to stretch both arms overhead", "target": "the young man", "voice": "male", "keys": man},
 ],
 "stillS": 2.0,
 "nouns": [
  {"word": "blinds", "x": 0.40, "y": 0.38, "voice": "female"},
  {"word": "a T-shirt", "x": 0.80, "y": 0.56, "voice": "female"},
  {"word": "a spine model", "x": 0.24, "y": 0.68, "voice": "female"},
  {"word": "a treatment table", "x": 0.50, "y": 0.78, "voice": "female"},
 ],
 "question": "What is the woman showing the man?",
 "answer": ["She", "is", "showing", "him", "a", "spine", "model."],
 "answerVoice": "female",
 "notes": "From 3.0 s the woman is mostly only her arm/hand + the spine model at the left edge; her hand touches his back, so boxes split there (horizontal split at 3.0 and 5.0-6.0 s, vertical split elsewhere). 7.0-9.0 s only the spine model and her fingers are visible at the left edge (small woman box). At 3.5-4.5 s she presses his mid/upper back, at 5.0-6.0 s his lower back."
})
