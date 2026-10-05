import sys; sys.path.insert(0, '/Users/kristiansurhanak/Projects/and-again-content/runs/a45_20261004')
from gen_5318_5320_5321_5322_lib import K, write
woman = K([
 (0.0, .29, .33, .38, .67), (0.5, .20, .33, .49, .67), (1.0, .11, .33, .58, .67), (1.5, .10, .33, .60, .67),
 (2.0, .42, .42, .19, .18), (2.5, .42, .42, .19, .18), (3.0, .41, .44, .19, .20), (3.5, .41, .44, .19, .20),
 (4.0, .41, .42, .19, .18), (4.5, .42, .42, .19, .18),
 (5.0, .37, .28, .31, .47), (5.5, .37, .28, .32, .47), (6.0, .35, .28, .32, .47), (6.5, .36, .28, .32, .48),
 (7.0, .29, .31, .37, .48), (7.5, .34, .23, .32, .55), (8.0, .33, .23, .32, .56), (8.5, .33, .25, .33, .54), (9.0, .33, .28, .33, .53)])
youngman = K([(0.0, .70, .62, .30, .38), (0.5, .71, .60, .29, .40), (1.0, .72, .61, .28, .39), (1.5, .72, .59, .28, .41)] +
 [(t,) for t in [2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0]])
write({
 "mediaId": 5318, "level": "A", "keyWord": "speak", "defaultVoice": "female",
 "taps": [
  {"phrase": "to speak into a microphone", "target": "the woman", "voice": "female", "keys": woman},
  {"phrase": "to touch his chin", "target": "the young man", "voice": "male", "keys": youngman},
  {"phrase": "to raise her fist", "target": "the woman", "voice": "female", "keys": woman},
 ],
 "stillS": 5.5,
 "nouns": [
  {"word": "the sky", "x": 0.50, "y": 0.12, "voice": "female"},
  {"word": "buildings", "x": 0.15, "y": 0.33, "voice": "female"},
  {"word": "a woman", "x": 0.53, "y": 0.47, "voice": "female"},
  {"word": "people", "x": 0.17, "y": 0.62, "voice": "female"},
 ],
 "question": "What is the woman doing?",
 "answer": ["She", "is", "speaking", "into", "a", "microphone."],
 "answerVoice": "female",
 "notes": "Young man only visible 0-1.5 s (close shot) touching his chin with his hand. Wide shots 2-4.5 s: woman small at centre. Many people in the crowd film with phones, so no filming phrase."
})
