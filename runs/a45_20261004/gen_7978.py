from gen_7977_7978_7979_7980_lib import *
turtle = keys([(0,.34,.36,.28),(0,.33,.37,.20),(0,.27,.37,.25),(0,.33,.37,.21),(0,.32,.36,.33),(0,.32,.36,.26),(0,.26,.34,.26),(0,.25,.36,.25)])
woman = keys([(.37,.35,.45,.55),(.38,.35,.44,.56),(.39,.35,.43,.58),(.38,.34,.47,.61),(.37,.34,.48,.63),(.36,.34,.52,.66),(.34,.34,.55,.66),(.36,.34,.60,.66)])
write(7978, {"mediaId": 7978, "level": "B", "keyWord": "separate", "defaultVoice": "female",
 "taps": [
  {"phrase": "to glide past the glass", "target": "the sea turtle", "voice": "female", "keys": turtle},
  {"phrase": "to paddle with its flippers", "target": "the sea turtle", "voice": "female", "keys": turtle},
  {"phrase": "to wear a cropped blue jumper", "target": "the woman", "voice": "female", "keys": woman}],
 "stillS": 2.2,
 "nouns": [{"word": "a sea turtle", "x": .17, "y": .40, "voice": "female"}, {"word": "a pillar", "x": .86, "y": .34, "voice": "female"},
           {"word": "a fern", "x": .88, "y": .50, "voice": "female"}, {"word": "a handrail", "x": .32, "y": .74, "voice": "female"}],
 "question": "What is the sea turtle doing?",
 "answer": ["It", "is", "gliding", "past", "the", "glass."],
 "answerVoice": "female",
 "notes": "The man stands right behind the woman and overlaps her almost completely, so he is not a target; both touch the glass and laugh, so the woman gets a clothing state (cropped blue jumper) that only she has. Her box therefore also covers the man. Her hand on the glass touches the turtle's head at 2.7-3.7: boxes split at the glass line. Key word 'separate' (verb) is not a noun. defaultVoice female: mixed couple, evenId true."})
