from gen_8053_8054_8057_8058_lib import K, write
T = [0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
woman = K(T, [(.47,.25,.90,1),(.45,.25,.95,1),(.45,.26,1,1),(.43,.23,1,1),(.10,.30,.82,1),(.10,.31,.82,1),(.08,.20,.82,1),(.38,.21,.98,1)])
man = K(T, [(.20,.22,.47,.58),(.12,.21,.45,.58),(.10,.21,.45,.60),(.12,.23,.43,.58),(.30,.215,.56,.30),(.30,.22,.60,.31),None,(0,.21,.38,.58)])
lant = K(T, [(.24,.08,.42,.22),(.22,.07,.40,.21),(.21,.07,.39,.21),(.25,.09,.43,.23),(.31,.075,.49,.215),(.32,.08,.50,.22),(.29,.06,.47,.20),(.22,.07,.40,.21)])
write(8053, {"mediaId": 8053, "level": "B", "keyWord": "patriot", "defaultVoice": "female",
 "taps": [
  {"phrase": "to press a sandbag into place", "target": "the woman", "voice": "female", "keys": woman},
  {"phrase": "to pass a sandbag along", "target": "the grey-haired man", "voice": "male", "keys": man},
  {"phrase": "to glow on a post", "target": "the lantern", "voice": "female", "keys": lant}],
 "stillS": 0.2,
 "nouns": [{"word": "a lantern", "x": 0.33, "y": 0.17, "voice": "female"},
           {"word": "a willow", "x": 0.80, "y": 0.17, "voice": "female"},
           {"word": "floodwater", "x": 0.86, "y": 0.45, "voice": "female"},
           {"word": "a sandbag", "x": 0.74, "y": 0.62, "voice": "female"}],
 "question": "What is the woman doing?",
 "answer": ["She", "is", "pressing", "a", "sandbag", "into", "place."],
 "answerVoice": "female",
 "notes": "Key word 'patriot' is not a placeable concrete noun, so not among the nouns. Man is heavily occluded behind the woman at 2.2-2.7 (thin box above her head, her beanie top cut a little) and off at 3.2 (only a sliver of his jacket). Woman box at 0.2-1.7 starts at her head (x .43-.47) so it does not overlap the man; her left knee/jacket edge is outside. 'to pass a sandbag along' = he holds the next bag in the chain (0.2-1.7)."})
