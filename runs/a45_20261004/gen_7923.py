from gen_7922_7923_7924_7926_lib import keys, write
main = keys([(0.33,0.11,0.64,0.88),(0.33,0.10,0.66,0.89),(0.33,0.10,0.64,0.89),(0.33,0.10,0.65,0.89),
             (0.33,0.09,0.65,0.90),(0.33,0.09,0.65,0.90),(0.33,0.09,0.65,0.90),(0.33,0.09,0.65,0.90)])
tee = keys([(0.14,0.30,0.18,0.38),(0.15,0.30,0.18,0.38),(0.14,0.29,0.18,0.51),(0.13,0.29,0.18,0.45),
            (0.14,0.28,0.18,0.36),(0.14,0.27,0.18,0.43),(0.15,0.29,0.18,0.41),(0.14,0.27,0.18,0.44)])
write({"mediaId": 7923, "level": "B", "keyWord": "on the other hand", "defaultVoice": "male",
 "taps": [
  {"phrase": "to curl a heavy dumbbell", "target": "the man in the vest", "voice": "male", "keys": main},
  {"phrase": "to stare at a chocolate doughnut", "target": "the man in the vest", "voice": "male", "keys": main},
  {"phrase": "to wear a white T-shirt", "target": "the man in the white T-shirt", "voice": "male", "keys": tee}],
 "stillS": 2.7,
 "nouns": [{"word": "hanging lamps", "x": 0.25, "y": 0.18, "voice": "male"},
           {"word": "a vest", "x": 0.62, "y": 0.40, "voice": "male"},
           {"word": "a doughnut", "x": 0.73, "y": 0.59, "voice": "male"},
           {"word": "a dumbbell", "x": 0.22, "y": 0.72, "voice": "male"}],
 "question": "What is the man in front doing?",
 "answer": ["He", "is", "staring", "at", "a", "chocolate", "doughnut."],
 "answerVoice": "male",
 "notes": "background man in white T-shirt is blurred and partly behind the dumbbell; state phrase used because he does no clear action. Main man box starts at his shoulder (x .33) so it does not overlap the T-shirt man; the dumbbell plates left of that are outside the box."})
