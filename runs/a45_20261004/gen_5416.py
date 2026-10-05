import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
T = [i*0.5 for i in range(19)]
def keys(boxes):
    return [{"t": t, "off": True} if b is None else {"t": t, "x": b[0], "y": b[1], "w": b[2], "h": b[3]} for t, b in zip(T, boxes)]
woman = [(0,.19,.31,.81),(0,.19,.28,.81),(0,.2,.3,.8),(0,.2,.29,.8),(0,.22,.31,.78),(0,.23,.33,.77),
         (0,.2,.27,.8),(0,.27,.36,.73),(0,.29,.4,.71),(0,.28,.42,.72),(0,.27,.34,.73),(0,.27,.34,.73),
         (0,.29,.45,.71),(0,.31,.5,.69),(0,.33,.46,.67),(0,.34,.56,.66),(0,.31,.38,.69),None,None]
loco = [(.31,.38,.18,.15),(.28,.37,.24,.15),(.3,.36,.3,.18),(.29,.34,.42,.23),(.31,.29,.64,.37),(.33,.18,.67,.6)] + [None]*13
blue = [None]*6 + [(.27,.28,.73,.23),(.37,.27,.63,.24),(.4,.29,.6,.24),(.42,.3,.58,.26),(.34,.35,.66,.22),(.34,.35,.66,.22)] + [None]*7
c = {"mediaId": 5416, "level": "B", "keyWord": "locomotive", "defaultVoice": "female",
 "taps": [
  {"phrase": "to stare in amazement", "target": "the woman", "voice": "female", "keys": keys(woman)},
  {"phrase": "to be painted bright orange", "target": "the orange locomotive", "voice": "female", "keys": keys(loco)},
  {"phrase": "to speed past the platform", "target": "the blue train", "voice": "female", "keys": keys(blue)}],
 "stillS": 2.0,
 "nouns": [{"word": "the sky", "x": .6, "y": .12, "voice": "female"},
           {"word": "a locomotive", "x": .65, "y": .42, "voice": "female"},
           {"word": "a scarf", "x": .15, "y": .62, "voice": "female"},
           {"word": "a suitcase", "x": .52, "y": .9, "voice": "female"}],
 "question": "What is the woman staring at?",
 "answer": ["She", "is", "staring", "at", "the", "orange", "locomotive."],
 "answerVoice": "female",
 "notes": "Woman box at 0-2.5 s is cut at her face line so it does not overlap the locomotive (her suitcase/hand at x 0.4-0.55 lie outside it). Orange locomotive only 0-2.5 s, blue train only 3.0-5.5 s; the white high-speed train at 6.5-9.0 s is not a target. 'to speed past' fits the blue train (orange one rolls in slowly)."}
json.dump(c, open(f"{HERE}/content/5416.json", "w"), indent=1)
