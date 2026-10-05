from gen_5585_5587_5588_5589_lib import *
R = keys([(0,0.41,0.69,1.0),(0,0.41,0.73,1.0),(0,0.44,0.68,1.0),(0.15,0.43,0.79,1.0),
          (0.32,0.43,0.89,0.99),(0.42,0.43,0.94,0.92),(0.45,0.43,0.95,0.89),(0.47,0.43,0.95,0.88)])
Wm = keys([None,None,None,(0,0.46,0.15,0.82),(0,0.43,0.28,0.92),(0.15,0.42,0.39,0.92),(0.17,0.42,0.42,0.90),(0.20,0.42,0.46,0.90)])
D = keys([None,None,None,None,None,(0,0.66,0.15,0.86),(0.02,0.65,0.17,0.87),(0.04,0.66,0.20,0.87)])
write({
 "mediaId": 5587, "level": "B", "keyWord": "automation", "defaultVoice": "female",
 "taps": [
  {"phrase": "to pick ripe apples", "target": "the robot", "voice": "female", "keys": R},
  {"phrase": "to sip from a mug", "target": "the woman", "voice": "female", "keys": Wm},
  {"phrase": "to trot along the path", "target": "the dog", "voice": "female", "keys": D},
 ],
 "stillS": 3.2,
 "nouns": [
  {"word": "a barn", "x": 0.38, "y": 0.45, "voice": "female"},
  {"word": "a wooden crate", "x": 0.64, "y": 0.64, "voice": "female"},
  {"word": "a robot", "x": 0.70, "y": 0.77, "voice": "female"},
  {"word": "a border collie", "x": 0.14, "y": 0.77, "voice": "female"},
 ],
 "question": "What is the robot doing?",
 "answer": ["It", "is", "picking", "ripe", "apples."],
 "answerVoice": "female",
 "notes": "Woman only enters at 1.7 s (edge of frame); dog only from 2.7 s. Woman/dog boxes split at the dog's right edge, so the woman's jacket edge is cut at 2.7 s."
})
