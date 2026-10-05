from gen_5585_5587_5588_5589_lib import *
Wm = keys([(0.12,0.29,0.58,0.69),(0.17,0.55,0.57,0.80),(0.16,0.52,0.60,0.79),(0.14,0.52,0.59,0.78),
           (0.16,0.52,0.60,0.77),(0.16,0.52,0.58,0.76),(0.17,0.52,0.57,0.75),(0.17,0.53,0.56,0.76)])
D = keys([(0.58,0.60,0.90,0.72),(0.57,0.60,0.90,0.71),(0.60,0.58,0.88,0.70),(0.59,0.57,0.85,0.71),
          (0.60,0.57,0.86,0.70),(0.58,0.56,0.83,0.69),(0.57,0.57,0.82,0.69),(0.56,0.57,0.79,0.69)])
write({
 "mediaId": 5588, "level": "B", "keyWord": "available", "defaultVoice": "female",
 "taps": [
  {"phrase": "to leap through the air", "target": "the woman in white", "voice": "female", "keys": Wm},
  {"phrase": "to fling her straw hat", "target": "the woman in white", "voice": "female", "keys": Wm},
  {"phrase": "to doze on a sun lounger", "target": "the dog", "voice": "female", "keys": D},
 ],
 "stillS": 2.2,
 "nouns": [
  {"word": "the sky", "x": 0.50, "y": 0.15, "voice": "female"},
  {"word": "the sea", "x": 0.15, "y": 0.47, "voice": "female"},
  {"word": "a golden retriever", "x": 0.72, "y": 0.62, "voice": "female"},
  {"word": "a book", "x": 0.66, "y": 0.75, "voice": "female"},
 ],
 "question": "What is the dog doing?",
 "answer": ["It", "is", "dozing", "on", "a", "sun", "lounger."],
 "answerVoice": "female",
 "notes": "Question asks about the dog because it dozes through the whole clip; the woman's leap lasts only to 0.7 s. The woman in white also lies on a lounger later, but she is not dozing (eyes open/laughing), so 'to doze' fits only the dog. Several straw hats, baskets and umbrellas in frame, so nouns avoid them; 'a book' is A-level but the only unique small object."
})
