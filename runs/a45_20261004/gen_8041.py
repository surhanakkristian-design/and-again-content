from gen_8038_8041_8042_8043_lib import *
T = [0.2, 0.7, 1.2, 1.7, 2.2, 2.7, 3.2, 3.7]
def card(t):
    return (0.20, 0.23, 0.65, 0.96) if t < 2.5 else (0.20, 0.23, 0.78, 0.96)
def green(t):
    if t < 2.5: return (0.66, 0.23, 1.0, 0.58)
    return (0.80, 0.21, 1.0, 0.52)
ck = keys(T, card); gk = keys(T, green)
write(8041, {
 "mediaId": 8041, "level": "B", "keyWord": "weighing", "defaultVoice": "female",
 "taps": [
  {"phrase": "to weigh up two puppies", "target": "the woman in yellow", "voice": "female", "keys": ck},
  {"phrase": "to pull a doubtful face", "target": "the woman in yellow", "voice": "female", "keys": ck},
  {"phrase": "to empty a bucket", "target": "the woman in green", "voice": "female", "keys": gk},
 ],
 "stillS": 0.7,
 "nouns": [
  {"word": "blossom", "x": 0.20, "y": 0.12, "voice": "female"},
  {"word": "a kennel", "x": 0.12, "y": 0.52, "voice": "female"},
  {"word": "a bucket", "x": 0.90, "y": 0.42, "voice": "female"},
  {"word": "a tennis ball", "x": 0.18, "y": 0.88, "voice": "female"},
 ],
 "question": "What is the woman in yellow doing?",
 "answer": ["She", "is", "weighing", "up", "two", "puppies."],
 "answerVoice": "female",
 "notes": "Two women; the kneeling one in the yellow cardigan holds a golden puppy and a black puppy and frowns/hesitates (0.2-2.7 s), then smiles at 3.7 s. The woman in green pours water from a bucket into the paddling pool (clearest 0.2 and 2.2 s). Boxes split at x 0.65/0.66 until 2.2 s, at 0.78/0.80 later when the green woman stands behind the raised black puppy. 'weigh up' used both literally (a puppy in each hand) and as 'consider'. Puppies are not targets (both are held and dangle, no phrase fits only one).",
})
