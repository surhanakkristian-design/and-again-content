import sys; sys.path.insert(0, '/Users/kristiansurhanak/Projects/and-again-content/runs/a45_20261004')
from gen_5318_5320_5321_5322_lib import K, write
sk = K([
 (0.0, .28, 0, .50, .92), (0.5, 0, .30, 1.0, .70), (1.0, 0, .20, 1.0, .80), (1.5, .05, .07, .76, .90),
 (2.0, .28, .21, .70, .79), (2.5, 0, .24, .91, .72), (3.0, .13, .32, .87, .56), (3.5, .26, .36, .50, .50),
 (4.0, .26, .35, .51, .51), (4.5, .30, .37, .52, .50), (5.0, .24, .34, .69, .52), (5.5, .22, .27, .72, .62),
 (6.0, .23, .03, .59, .89), (6.5, .20, .03, .73, .88), (7.0, 0, .04, .91, .93), (7.5, 0, .04, .92, .93), (8.0, 0, .06, .91, .92)])
write({
 "mediaId": 5321, "level": "A", "keyWord": "skate", "defaultVoice": "male",
 "taps": [
  {"phrase": "to spin on the ice", "target": "the skater", "voice": "male", "keys": sk},
  {"phrase": "to stretch out his arms", "target": "the skater", "voice": "male", "keys": sk},
  {"phrase": "to lift one leg", "target": "the skater", "voice": "male", "keys": sk},
 ],
 "stillS": 8.0,
 "nouns": [
  {"word": "a blue line", "x": 0.86, "y": 0.30, "voice": "male"},
  {"word": "a skater", "x": 0.50, "y": 0.45, "voice": "male"},
  {"word": "ice", "x": 0.85, "y": 0.56, "voice": "male"},
 ],
 "question": "What is the skater doing?",
 "answer": ["He", "is", "spinning", "on", "the", "ice."],
 "answerVoice": "male",
 "notes": "Only one person in the clip, so all three phrases use the skater. Arms stretched out wide at 0.5-1.0 s; free leg lifted 1.5-3.0 s and 5.0 s; fast spin 2.0-6.5 s. The line on the ice is blue-purple."
})
