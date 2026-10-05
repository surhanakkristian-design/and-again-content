import sys; sys.path.insert(0, '/Users/kristiansurhanak/Projects/and-again-content/runs/a45_20261004')
from gen_5318_5320_5321_5322_lib import K, write
tops = {0.0:.02,0.5:.02,1.0:.04,1.5:.08,2.0:.01,2.5:0,3.0:.01,3.5:.01,4.0:0,4.5:0,5.0:.05,5.5:.03,6.0:.02,6.5:0,7.0:.01,7.5:0,
        8.0:.07,8.5:.09,9.0:.13,9.5:.10,10.0:.14}
man = K([(t, 0, y, 1.0, .74 - y) for t, y in tops.items()])
write({
 "mediaId": 5322, "level": "B", "keyWord": "spit", "defaultVoice": "male",
 "taps": [
  {"phrase": "to taste the green soup", "target": "the man", "voice": "male", "keys": man},
  {"phrase": "to stick out his tongue", "target": "the man", "voice": "male", "keys": man},
  {"phrase": "to spit out a mouthful", "target": "the man", "voice": "male", "keys": man},
 ],
 "stillS": 4.0,
 "nouns": [
  {"word": "a bowl of soup", "x": 0.55, "y": 0.78, "voice": "male"},
  {"word": "a mug", "x": 0.14, "y": 0.76, "voice": "male"},
  {"word": "sauce", "x": 0.24, "y": 0.89, "voice": "male"},
  {"word": "a kitchen counter", "x": 0.72, "y": 0.93, "voice": "male"},
 ],
 "question": "What is the man doing?",
 "answer": ["He", "is", "spitting", "liquid", "over", "the", "counter."],
 "answerVoice": "male",
 "notes": "Only one person, so all three phrases use the man (box = head and upper body down to the counter edge, full width because his arms reach the frame edges). He spits at 7.5-8.0 s right after drinking from the white mug, so the answer says 'liquid', not 'soup' (the description says soup). Tongue out at 1.0-1.5 s and 8.5-10 s."
})
