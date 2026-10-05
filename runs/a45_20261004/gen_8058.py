from gen_8053_8054_8057_8058_lib import K, write
T = [i*0.5 for i in range(10)]
man = K(T, [(.08,.38,.62,.68)]*10)
shelf = K(T, [(.10,.25,.52,.38)]*10)
plant = K(T, [(.62,.28,.93,.68)]*10)
write(8058, {"mediaId": 8058, "level": "A", "keyWord": "guitar", "defaultVoice": "male",
 "taps": [
  {"phrase": "to play the guitar", "target": "the man", "voice": "male", "keys": man},
  {"phrase": "to hang on the wall", "target": "the shelf", "voice": "male", "keys": shelf},
  {"phrase": "to grow in a blue pot", "target": "the plant", "voice": "male", "keys": plant}],
 "stillS": 0.0,
 "nouns": [{"word": "books", "x": 0.30, "y": 0.33, "voice": "male"},
           {"word": "a man", "x": 0.34, "y": 0.44, "voice": "male"},
           {"word": "a guitar", "x": 0.40, "y": 0.535, "voice": "male"},
           {"word": "a plant", "x": 0.78, "y": 0.40, "voice": "male"}],
 "question": "What is the man doing?",
 "answer": ["He", "is", "playing", "the", "guitar."],
 "answerVoice": "male",
 "notes": "Static illustration with small loops (hand strumming, music notes); boxes are the same in every frame. Man box ends at x .62 so his lower legs/feet (to x .77) lie in the plant box; the shelf box ends where his hair starts (y .38). Shelf and plant phrases are states (no other action fits a thing here). The instrument is small (ukulele-like) but the packet calls it a guitar."})
