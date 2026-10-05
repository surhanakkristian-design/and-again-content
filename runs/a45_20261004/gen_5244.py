import json, os
from gen_5244_lib import K, write
H = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(f'{H}/frames/5244/packet.json'))['times']
DB = {0.0:(0,.2,.24,.8), 0.5:(0,.2,.41,.8), 1.0:(0,.2,.5,.8), 2.5:(0,.14,.44,.86), 3.0:(0,.1,.48,.9),
      3.5:(0,.11,.62,.89), 4.0:(0,.12,.54,.88), 4.5:(0,.12,.55,.88), 5.0:(.48,.14,.52,.7), 5.5:(.66,.1,.34,.6),
      6.0:(.77,.25,.23,.5), 6.5:(.74,.34,.26,.37), 7.0:(.67,.41,.22,.25), 7.5:(.66,.46,.24,.2)}
BB = {0.0:(.25,.13,.75,.87), 0.5:(.42,.13,.58,.87), 1.0:(.51,.14,.49,.86), 1.5:(.47,.17,.53,.83), 2.0:(.33,.17,.45,.8),
      2.5:(.45,.15,.55,.85), 3.0:(.49,.15,.51,.85), 3.5:(.63,.16,.37,.84), 4.0:(.55,.17,.45,.83), 4.5:(.56,.16,.44,.84),
      5.0:(0,.21,.47,.63), 5.5:(0,.28,.42,.44), 6.0:(0,.29,.33,.47), 6.5:(.05,.36,.27,.37), 7.0:(.16,.43,.2,.28), 7.5:(.26,.46,.18,.22)}
BALL = {6.0:(.58,.38,.18,.14), 6.5:(.44,.41,.18,.14), 7.0:(.46,.48,.18,.14), 7.5:(.47,.52,.18,.14), 8.0:(.55,.48,.18,.14)}
d = {"mediaId": 5244, "level": "A", "keyWord": "classmate", "defaultVoice": "male",
 "taps": [
  {"phrase": "to hold a sandwich", "target": "the dark-haired boy", "voice": "male", "keys": K(DB, T)},
  {"phrase": "to hold up a red apple", "target": "the blond boy", "voice": "male", "keys": K(BB, T)},
  {"phrase": "to roll across the grass", "target": "the ball", "voice": "male", "keys": K(BALL, T)}],
 "stillS": 4.5,
 "nouns": [{"word": "a classmate", "x": .78, "y": .22, "voice": "male"},
           {"word": "an apple", "x": .67, "y": .40, "voice": "male"},
           {"word": "a sandwich", "x": .58, "y": .56, "voice": "male"},
           {"word": "a bench", "x": .62, "y": .87, "voice": "male"}],
 "question": "What is the blond boy holding?",
 "answer": ["He", "is", "holding", "a", "red", "apple."],
 "answerVoice": "male",
 "notes": "Boys tracked through the field shots by position/hair; from 8.0 s they are too small to tell apart, set off. At 7.0-7.5 the right runner is assumed to be the dark-haired boy. 'a classmate' sits on the blond boy (either boy is a classmate). Ball only visible 6.0-8.0 s; split from the kicker at 7.5."}
write(f'{H}/content/5244.json', d)
