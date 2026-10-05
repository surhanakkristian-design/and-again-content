import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
T = [i * 0.5 for i in range(21)]
def keys(d):
    out = []
    for t in T:
        b = d.get(t)
        out.append({'t': t, 'off': True} if not b else {'t': t, 'x': b[0], 'y': b[1], 'w': b[2], 'h': b[3]})
    return out
def write(vid, level, kw, dv, taps, boxes, still, nouns, q, a, av, notes):
    c = {'mediaId': vid, 'level': level, 'keyWord': kw, 'defaultVoice': dv,
         'taps': [{'phrase': p, 'target': tg, 'voice': v, 'keys': keys(boxes[tg])} for p, tg, v in taps],
         'stillS': still, 'nouns': [{'word': w, 'x': x, 'y': y, 'voice': v} for w, x, y, v in nouns],
         'question': q, 'answer': a, 'answerVoice': av, 'notes': notes}
    json.dump(c, open(f'{HERE}/content/{vid}.json', 'w'), indent=1, ensure_ascii=False)

# ---------- 805
W = {0.0: [0, 0, .31, .27], 0.5: [.03, 0, .42, .35], 1.0: [.14, .42, .32, .55], 2.5: [.17, .38, .30, .40],
     3.0: [.07, .34, .40, .52], 3.5: [.08, .33, .42, .67], 4.0: [.07, .31, .42, .66], 4.5: [.14, .31, .35, .69],
     5.0: [.10, .26, .39, .74], 5.5: [0, .30, .40, .70], 6.0: [0, .35, .49, .65], 6.5: [0, .28, .48, .72],
     7.0: [0, .26, .40, .74], 7.5: [0, .26, .42, .74], 8.0: [0, .25, .52, .75], 8.5: [0, .27, .62, .73],
     9.0: [0, .25, .54, .75], 9.5: [0, .26, .60, .74], 10.0: [0, .27, .53, .73]}
M = {0.0: [.52, 0, .48, .45], 0.5: [.56, 0, .44, .62], 1.0: [.58, .38, .42, .62], 2.5: [.57, .38, .40, .43],
     3.0: [.52, .34, .34, .52], 3.5: [.55, .29, .45, .71], 4.0: [.49, .23, .44, .77], 4.5: [.49, .26, .40, .74],
     5.0: [.49, .24, .36, .76], 5.5: [.40, .23, .52, .77], 6.0: [.50, .34, .50, .66], 6.5: [.50, .25, .50, .75],
     7.0: [.48, .26, .52, .74], 7.5: [.50, .26, .50, .74], 8.0: [.53, .19, .47, .81], 8.5: [.62, .24, .38, .76],
     9.0: [.54, .22, .46, .78], 9.5: [.61, .23, .39, .77], 10.0: [.53, .25, .47, .75]}
TR = {1.0: [0, .38, .14, .36], 1.5: [0, .38, 1, .40], 2.0: [0, .30, 1, .42], 2.5: [0, .23, 1, .15],
      3.0: [0, .17, 1, .17], 3.5: [0, .02, 1, .27]}
write(805, 'A', 'traveling', 'male',
      [('to carry a backpack', 'the woman', 'female'), ('to wear shorts', 'the man', 'male'), ('to wait at the station', 'the train', 'male')],
      {'the woman': W, 'the man': M, 'the train': TR}, 10.0,
      [('mountains', .60, .20, 'male'), ('a backpack', .17, .47, 'male'), ('a map', .55, .72, 'male'), ('a watch', .86, .86, 'male')],
      'What are they holding?', ['They', 'are', 'holding', 'a', 'map.'], 'male',
      'Both people run, lift suitcases and look at the map, so their phrases are states (backpack / shorts). Train: its box is only the part above the two people at 2.5-3.5 s (they stand in front of it), a narrow strip at 1.0 s; off inside the train and at 0.0-0.5 s (only a sliver at the top edge). Woman/man boxes are split along the line between them when they sit close.')

# ---------- 806
WA = {0.5: [0, .34, .24, .22], 1.0: [0, .44, .63, .24], 1.5: [0, .43, .77, .52], 2.0: [0, .58, 1, .37], 2.5: [0, .58, .36, .36],
      3.0: [0, .42, .95, .58], 3.5: [0, .38, .80, .62], 4.0: [.03, .35, .97, .65], 4.5: [.07, .28, .93, .72],
      5.0: [.30, .33, .70, .54], 5.5: [.27, .36, .73, .64], 6.0: [.25, .48, .72, .52], 6.5: [.24, .22, .76, .78],
      7.0: [.20, .08, .60, .50], 7.5: [.12, .13, .52, .52], 8.0: [.22, .11, .52, .57], 8.5: [.31, .10, .52, .60],
      9.0: [.30, .09, .56, .68], 9.5: [.32, .20, .50, .57], 10.0: [.23, .11, .52, .60]}
OM = {6.5: [.07, .04, .27, .17], 8.0: [0, .17, .22, .15], 8.5: [.08, .19, .22, .14], 9.0: [.04, .18, .24, .15],
      9.5: [.05, .19, .25, .15], 10.0: [0, .21, .23, .15]}
write(806, 'A', 'tray', 'female',
      [('to carry a full tray', 'the waitress', 'female'), ('to wear a brown apron', 'the waitress', 'female'), ('to stand behind the bar', 'the old man', 'male')],
      {'the waitress': WA, 'the old man': OM}, 8.0,
      [('a waitress', .50, .35, 'female'), ('a pot', .52, .63, 'female'), ('a tray', .50, .78, 'female'), ('a table', .50, .90, 'female')],
      'What is the waitress carrying?', ['She', 'is', 'carrying', 'a', 'full', 'tray.'], 'female',
      'Two targets only (waitress twice): the guests show just clapping hands on both sides, so no phrase fits one of them alone. Waitress: only her hand / arm is in the picture at 0.5-3.0 s; off at 0.0 s (fingertips at the edge). At 8.5 s her stretched left arm is outside her box because it crosses under the old man. Old man: small figure behind the coffee machine; off at 6.0 s (a blurred face behind the counter, not sure it is him) and 7.0 s (only a sliver at the top edge).')

# ---------- 808
WO = {0.0: [0, 0, .31, .58], 0.5: [0, 0, .47, .68], 1.0: [.19, .30, .30, .52], 1.5: [.27, .51, .23, .30], 2.0: [.30, .66, .20, .30],
      2.5: [.28, .78, .20, .22], 3.0: [.29, .90, .18, .10], 3.5: [0, .43, .55, .57], 4.0: [0, .25, .52, .75], 4.5: [0, .26, .60, .74],
      5.0: [0, .31, .55, .69], 5.5: [0, .33, .52, .67], 6.0: [0, .38, .52, .62], 6.5: [0, .44, .52, .56], 7.0: [0, .51, .42, .49],
      7.5: [.05, .60, .33, .40], 8.0: [0, .70, .37, .30], 8.5: [.05, .74, .33, .26], 9.0: [.02, .75, .38, .25], 9.5: [.05, .75, .32, .25],
      10.0: [.06, .74, .34, .26]}
MA = {0.0: [.68, 0, .32, .58], 0.5: [.57, 0, .43, .66], 1.0: [.53, .30, .28, .53], 1.5: [.50, .51, .23, .30], 2.0: [.50, .66, .20, .30],
      2.5: [.48, .78, .20, .22], 3.0: [.47, .90, .18, .10], 3.5: [.57, .35, .43, .65], 4.0: [.70, .18, .30, .65], 4.5: [.80, .18, .20, .60],
      5.0: [.80, .25, .20, .73], 5.5: [.75, .31, .25, .67], 6.0: [.72, .38, .28, .46], 6.5: [.69, .40, .31, .60], 7.0: [.71, .48, .29, .52],
      7.5: [.68, .58, .32, .42], 8.0: [.64, .70, .36, .30], 8.5: [.62, .74, .36, .26], 9.0: [.58, .75, .37, .25], 9.5: [.63, .75, .35, .25],
      10.0: [.57, .74, .38, .26]}
TE = {0.0: [.32, 0, .35, .27], 0.5: [.47, 0, .10, .35], 1.0: [0, 0, 1, .30], 1.5: [0, 0, 1, .51], 2.0: [0, 0, 1, .66], 2.5: [0, 0, 1, .78],
      3.0: [0, .08, 1, .82], 3.5: [0, 0, 1, .34], 4.0: [.53, 0, .17, 1], 4.5: [.61, 0, .18, 1], 5.0: [.56, 0, .23, 1], 5.5: [0, 0, 1, .31],
      6.0: [0, 0, 1, .38], 6.5: [0, 0, 1, .40], 7.0: [0, 0, 1, .48], 7.5: [0, 0, 1, .58], 8.0: [0, 0, 1, .70], 8.5: [0, 0, 1, .74],
      9.0: [0, 0, 1, .75], 9.5: [0, 0, 1, .75], 10.0: [0, 0, 1, .74]}
write(808, 'A', 'tree', 'female',
      [('to wear a blue jacket', 'the woman', 'female'), ('to wear a red T-shirt', 'the man', 'male'), ('to grow in a field', 'the tree', 'female')],
      {'the woman': WO, 'the man': MA, 'the tree': TE}, 1.0,
      [('a tree', .50, .15, 'female'), ('a woman', .27, .43, 'female'), ('a man', .70, .52, 'male'), ('grass', .50, .88, 'female')],
      'Where are they walking?', ['They', 'are', 'walking', 'to', 'a', 'big', 'tree.'], 'female',
      'Woman and man do the same things all the time (walk, touch the bark, look up), so their phrases are states (clothes). The tree fills the picture behind the people: its box is the part above them, or the strip of bark between their hands at 4.0-5.0 s. At 3.5-5.0 s only hands are visible: hands with a denim sleeve = woman, bare arms on the right = man.')

# ---------- 809
YW = {0.0: [0, .28, .57, .72], 0.5: [0, .28, .43, .72], 1.0: [0, .29, .40, .71], 1.5: [0, .29, .40, .71], 2.0: [0, .30, .42, .70],
      2.5: [0, .30, .33, .70], 3.0: [0, .30, .38, .70], 3.5: [0, .33, .31, .67], 4.0: [0, .32, .64, .68], 4.5: [0, .31, .69, .69],
      5.0: [0, .38, .62, .62], 5.5: [0, .38, .41, .62], 6.0: [0, .31, .66, .69], 6.5: [0, .29, .47, .71], 7.0: [0, .30, .27, .70],
      7.5: [0, .30, .25, .70], 8.0: [0, .28, .28, .72], 8.5: [0, .26, .25, .74], 9.0: [0, .28, .27, .72], 9.5: [0, .31, .29, .69],
      10.0: [0, .26, .36, .74]}
YM = {0.0: [.66, .25, .34, .75], 0.5: [.66, .25, .34, .75], 1.0: [.66, .25, .34, .75], 1.5: [.68, .25, .32, .75], 2.0: [.63, .26, .37, .74],
      2.5: [.68, .28, .32, .72], 3.0: [.65, .26, .35, .38], 3.5: [.56, .33, .44, .67], 4.0: [.64, .31, .36, .69], 4.5: [.69, .28, .31, .72],
      5.0: [.63, .28, .37, .72], 5.5: [.66, .28, .34, .72], 6.0: [.66, .25, .34, .75], 6.5: [.48, .25, .52, .75], 7.0: [.28, .28, .72, .72],
      7.5: [.26, .22, .74, .78], 8.0: [.31, .23, .69, .77], 8.5: [.50, .20, .50, .80], 9.0: [.48, .23, .52, .77], 9.5: [.57, .20, .43, .80],
      10.0: [.57, .22, .43, .78]}
DG = {3.0: [.45, .64, .34, .36], 3.5: [.31, .71, .18, .24], 5.5: [.41, .58, .18, .14], 8.5: [.25, .62, .18, .16],
      9.0: [.27, .70, .20, .20], 9.5: [.29, .69, .27, .20], 10.0: [.36, .77, .21, .20]}
write(809, 'B', 'trend', 'male',
      [('to giggle behind her hand', 'the young woman', 'female'), ('to try on a hat', 'the young man', 'male'), ('to trot along the street', 'the dog', 'male')],
      {'the young woman': YW, 'the young man': YM, 'the dog': DG}, 9.5,
      [('an awning', .30, .19, 'male'), ('a passer-by', .38, .50, 'male'), ('a stall', .66, .63, 'male'), ('a corgi', .42, .83, 'male')],
      'What is the young man trying on?', ['He', 'is', 'trying', 'on', 'a', 'yellow', 'bucket', 'hat.'], 'male',
      'The woman giggles behind her hand only at 9.0-9.5 s; the man tries the hat on from 7.0 s. Dog: visible at 3.0-3.5, 5.5 (tiny, in the background) and 8.5-10.0 s; where it walks in front of / behind the two friends their boxes are cut back (man at 3.0 s = head and chest only; woman at 5.5 and 8.5-10.0 s without her stretched hand). No noun "a bucket hat": several hats are in the still picture (man, passer-by, dog, stall). "an awning" is upper B2.')
