import json, os
from gen_5244_lib import K, write
H = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(f'{H}/frames/5248/packet.json'))['times']
W = {0.0:(0,.2,1,.8), 0.5:(0,.17,1,.83), 1.0:(0,.21,1,.79), 1.5:(.1,.28,.32,.47), 2.0:(.12,.25,.42,.6),
     2.5:(.25,.26,.52,.62), 3.0:(.23,.22,.57,.72), 3.5:(0,.17,1,.83), 4.0:(0,.15,1,.85), 4.5:(0,.15,1,.85),
     5.0:(.22,.08,.62,.92), 5.5:(.33,.19,.46,.76), 6.0:(.42,.26,.34,.52)}
R = {1.5:(.43,.33,.57,.42), 2.0:(.55,.32,.45,.47), 2.5:(0,.33,.24,.35), 3.0:(0,.32,.22,.5)}
d = {"mediaId": 5248, "level": "A", "keyWord": "rent", "defaultVoice": "female",
 "taps": [
  {"phrase": "to look at her phone", "target": "the woman in the orange jacket", "voice": "female", "keys": K(W, T)},
  {"phrase": "to ride next to the sea", "target": "the woman in the orange jacket", "voice": "female", "keys": K(W, T)},
  {"phrase": "to stand in a long row", "target": "the parked scooters", "voice": "female", "keys": K(R, T)}],
 "stillS": 2.0,
 "nouns": [{"word": "the sky", "x": .5, "y": .12, "voice": "female"},
           {"word": "the sea", "x": .82, "y": .34, "voice": "female"},
           {"word": "a jacket", "x": .24, "y": .52, "voice": "female"},
           {"word": "scooters", "x": .8, "y": .52, "voice": "female"}],
 "question": "What is the woman looking at?",
 "answer": ["She", "is", "looking", "at", "her", "phone."],
 "answerVoice": "female",
 "notes": "Key word 'rent' is not a visible noun. The palm-promenade shot (6.5-9.0 s) shows a different curly-haired woman in a red jacket riding; the main woman is set off there, and phrase 2 says 'next to the sea' because the sea is visible only in her shots. Phrase 3 is a state (the parked rank, 1.5-3.0 s); where the woman stands in front of the rank only the part beside her is boxed. At 3.5-4.5 s she is only hands/sleeves + phone in close-up."}
write(f'{H}/content/5248.json', d)
