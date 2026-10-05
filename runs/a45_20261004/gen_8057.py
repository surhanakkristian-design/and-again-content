from gen_8053_8054_8057_8058_lib import K, write
T = [i*0.5 for i in range(40)]
woman = K(T, [(.42,.29,.90,.80)]*40)
cat = K(T, [(.09,.39,.42,.72)]*40)
write(8057, {"mediaId": 8057, "level": "A", "keyWord": "cat", "defaultVoice": "female",
 "taps": [
  {"phrase": "to hold a hot drink", "target": "the woman", "voice": "female", "keys": woman},
  {"phrase": "to carry a yellow cat", "target": "the woman", "voice": "female", "keys": woman},
  {"phrase": "to move its long tail", "target": "the cat", "voice": "female", "keys": cat}],
 "stillS": 0.0,
 "nouns": [{"word": "a scarf", "x": 0.74, "y": 0.40, "voice": "female"},
           {"word": "a cup", "x": 0.57, "y": 0.57, "voice": "female"},
           {"word": "a cat", "x": 0.27, "y": 0.48, "voice": "female"},
           {"word": "a coat", "x": 0.70, "y": 0.72, "voice": "female"}],
 "question": "What is the woman doing?",
 "answer": ["She", "is", "holding", "a", "yellow", "cat."],
 "answerVoice": "female",
 "notes": "Static illustration that loops two nearly identical poses for 19.8 s; boxes are the same in every frame. Only two targets exist (woman, cat), so the woman has two phrases. The cat lies on her coat: the boxes split at x .42, so the woman's box cuts the left edge of her face/hair a little and her left arm holding the cat is inside the cat box. Tail movement is small (tip shifts between poses)."})
