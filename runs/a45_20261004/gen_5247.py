import json, os
from gen_5244_lib import K, write
H = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(f'{H}/frames/5247/packet.json'))['times']
OW = {0.0:(.05,.12,.44,.6), 0.5:(.05,.12,.44,.6), 1.0:(.05,.14,.46,.58), 1.5:(.05,.15,.45,.57), 2.0:(.04,.14,.44,.6),
      2.5:(0,.16,.56,.64), 3.0:(0,.11,.53,.79), 3.5:(0,.1,.45,.78), 4.0:(0,.04,.38,.8), 4.5:(0,.04,.4,.78),
      5.0:(0,.04,.4,.74), 5.5:(0,.02,.44,.73), 6.0:(0,.04,.45,.7), 6.5:(.05,.16,.45,.56), 7.0:(.06,.19,.33,.52)}
MAN = {0.0:(.56,0,.44,.57), 0.5:(.57,0,.43,.57), 1.0:(.56,0,.44,.58), 1.5:(.53,0,.47,.59), 2.0:(.49,0,.51,.59),
       2.5:(.57,0,.43,.87), 3.0:(.54,0,.46,.86), 3.5:(.46,0,.54,.5), 4.0:(.39,0,.61,.44), 4.5:(.41,0,.59,.44),
       5.0:(.41,0,.59,.42), 5.5:(.45,0,.55,.44), 6.0:(.46,0,.54,.46), 6.5:(.5,.02,.47,.53), 7.0:(.48,.04,.47,.51)}
DOG = {0.0:(.72,.58,.28,.26), 0.5:(.69,.58,.31,.26), 1.0:(.69,.59,.31,.26), 1.5:(.72,.6,.28,.26), 2.0:(.72,.6,.28,.26),
       3.5:(.58,.51,.32,.19), 4.0:(.54,.45,.2,.24), 4.5:(.57,.45,.21,.24), 5.0:(.53,.43,.21,.24), 5.5:(.54,.45,.22,.24),
       6.0:(.52,.47,.22,.23), 6.5:(.74,.56,.24,.22), 7.0:(.73,.56,.24,.23)}
for t in T:
    if t > 7.0: OW[t] = OW[7.0]; MAN[t] = MAN[7.0]; DOG[t] = DOG[7.0]
d = {"mediaId": 5247, "level": "B", "keyWord": "footprints", "defaultVoice": "male",
 "taps": [
  {"phrase": "to wag her finger", "target": "the old woman", "voice": "female", "keys": K(OW, T)},
  {"phrase": "to mop the muddy floor", "target": "the young man", "voice": "male", "keys": K(MAN, T)},
  {"phrase": "to sit obediently by the wall", "target": "the dog", "voice": "male", "keys": K(DOG, T)}],
 "stillS": 8.0,
 "nouns": [{"word": "footprints", "x": .42, "y": .87, "voice": "male"},
           {"word": "a mop", "x": .48, "y": .70, "voice": "male"},
           {"word": "a helmet", "x": .70, "y": .27, "voice": "male"},
           {"word": "an apron", "x": .22, "y": .47, "voice": "male"}],
 "question": "What is the young man doing?",
 "answer": ["He", "is", "mopping", "the", "muddy", "footprints."],
 "answerVoice": "male",
 "notes": "Dog sits in front of the man's legs: man/dog split along y, so the man's boots are outside his box at most times; at 3.5-6.0 s the dog walks between his legs and the man's box covers only his upper body. Dog set off at 2.5-3.0 s (hidden behind the boots). defaultVoice male: the man is taken as the main person (evenId false anyway). The old woman (wagging her finger 0-2 s) mops nothing, so phrase 2 fits only the man."}
write(f'{H}/content/5247.json', d)
