import json, os
from gen_5244_lib import K, write
H = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(f'{H}/frames/5246/packet.json'))['times']
W = {0.0:(.1,.08,.84,.66), 0.5:(.1,.08,.86,.68), 1.0:(.1,.09,.85,.66), 1.5:(.1,.09,.85,.66),
     2.0:(0,.02,1,.8), 2.5:(0,.02,1,.8), 3.0:(0,.06,1,.8), 3.5:(0,.04,1,.76), 4.0:(0,.03,1,.82),
     4.5:(0,.09,.97,.72), 5.0:(.02,.1,.95,.8), 5.5:(0,.04,1,.96), 6.0:(0,.03,1,.95), 6.5:(.22,.19,.78,.79),
     7.0:(.2,.22,.8,.78), 7.5:(.56,.16,.44,.84), 8.0:(.53,.16,.47,.84), 8.5:(.51,.16,.49,.84), 9.0:(.55,.17,.45,.83)}
M = {7.5:(.3,.27,.25,.27), 8.0:(.33,.26,.19,.2), 8.5:(.31,.3,.19,.26), 9.0:(.3,.3,.24,.28)}
d = {"mediaId": 5246, "level": "B", "keyWord": "flask", "defaultVoice": "female",
 "taps": [
  {"phrase": "to swirl a glass flask", "target": "the woman", "voice": "female", "keys": K(W, T)},
  {"phrase": "to jot down notes", "target": "the woman", "voice": "female", "keys": K(W, T)},
  {"phrase": "to wear a dark blue shirt", "target": "the man in the blue shirt", "voice": "male", "keys": K(M, T)}],
 "stillS": 6.5,
 "nouns": [{"word": "a flask", "x": .33, "y": .62, "voice": "female"},
           {"word": "a microscope", "x": .17, "y": .47, "voice": "female"},
           {"word": "safety goggles", "x": .5, "y": .33, "voice": "female"},
           {"word": "a lab coat", "x": .82, "y": .62, "voice": "female"}],
 "question": "What is the woman peering through?",
 "answer": ["She", "is", "peering", "through", "a", "microscope."],
 "answerVoice": "female",
 "notes": "Phrase 3 is a state: the colleague only sits and smiles (no action unique to him); visible 7.5-9.0 s only, hidden behind the microscope before. At 7.5-9.0 the woman's box is cut at the man's side, so her hand with the pink flask lies partly outside it. Swirling is at 2.0-2.5 s, notes at 4.0-5.0 s."}
write(f'{H}/content/5246.json', d)
