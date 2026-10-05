import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
T = [i*0.5 for i in range(21)]
def keys(boxes):
    return [{"t": t, "off": True} if b is None else {"t": t, "x": b[0], "y": b[1], "w": b[2], "h": b[3]} for t, b in zip(T, boxes)]
woman = [(.30,.30,.38,.52),(.26,.29,.38,.56),(.28,.25,.41,.69),(.26,.23,.48,.7),(.17,.26,.63,.74),(.14,.36,.82,.64),(.08,.37,.92,.63),
         (0,.29,.49,.71),(0,.31,.5,.69),(0,.3,.45,.7),(0,.3,.42,.7),(0,.3,.44,.7),
         (.26,.29,.23,.71),(.07,.32,.34,.68),(0,.40,.76,.6),(.07,.41,.67,.59),(.17,.41,.57,.47),(.14,.43,.6,.46),(.14,.42,.55,.57),(.3,.41,.38,.58),(.28,.42,.39,.57)]
tram = [None]*12 + [(.52,.3,.2,.17),(.41,.28,.27,.18),(.29,.26,.32,.14),(.2,.27,.42,.14),(.15,.27,.55,.14),(.12,.27,.75,.15),(.1,.22,.9,.19),(.68,.18,.32,.72),(.67,.17,.33,.65)]
kw = keys(woman)
c = {"mediaId": 5418, "level": "B", "keyWord": "interior", "defaultVoice": "female",
 "taps": [
  {"phrase": "to grip a brass pole", "target": "the woman", "voice": "female", "keys": kw},
  {"phrase": "to lean out of the carriage", "target": "the woman", "voice": "female", "keys": kw},
  {"phrase": "to pull into the station", "target": "the modern tram", "voice": "female", "keys": keys(tram)}],
 "stillS": 2.0,
 "nouns": [{"word": "a ceiling light", "x": .38, "y": .06, "voice": "female"},
           {"word": "a brass pole", "x": .76, "y": .25, "voice": "female"},
           {"word": "a canvas bag", "x": .58, "y": .56, "voice": "female"},
           {"word": "a wooden bench", "x": .6, "y": .72, "voice": "female"}],
 "question": "What is the woman holding?",
 "answer": ["She", "is", "gripping", "a", "brass", "pole."],
 "answerVoice": "female",
 "notes": "Modern tram only 6.0-10.0 s; at 7.0-9.0 s it is behind the woman, so its box is the strip above her head (roof + pantograph) and her box starts at her hair line; at 6.5 s her box is cut at x 0.41 (bag partly outside) to stay clear of the tram. A second parked tram stands on the right at 6.0-8.5 s (not the target, it does not move). Key word 'interior' is not used as a noun slot (no single place)."}
json.dump(c, open(f"{HERE}/content/5418.json", "w"), indent=1)
