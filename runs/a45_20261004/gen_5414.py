import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
T = [i*0.5 for i in range(19)]
def keys(boxes):
    out = []
    for t, b in zip(T, boxes):
        out.append({"t": t, "off": True} if b is None else {"t": t, "x": b[0], "y": b[1], "w": b[2], "h": b[3]})
    return out
boy = [(0,.05,.68,.95),(0,.05,.72,.95),(0,.08,.66,.92),(0,.1,1,.9),(0,.1,.98,.9),(0,.1,1,.9),(0,.22,1,.78),(0,.25,1,.75),
       (0,.05,.7,.95),(.1,.34,.88,.66),(.1,.31,.84,.69),(0,.21,1,.79),(0,.36,1,.64),(.02,.42,.97,.58),(.08,.5,.86,.5),
       (.12,.55,.8,.45),(.12,.54,.76,.46),(.12,.6,.74,.4),(.12,.61,.74,.39)]
cars = [(.68,.36,.32,.21),(.72,.37,.28,.2),(.66,.38,.34,.2),None,None,None,None,None,
        (.7,.12,.3,.3),(0,.08,1,.25),(0,.08,1,.22),(0,.06,1,.14),(0,.18,1,.16),(0,.18,1,.23),(0,.27,1,.22),
        (0,.28,1,.26),(0,.29,1,.24),(0,.3,1,.29),(0,.3,1,.3)]
kb = keys(boy)
c = {"mediaId": 5414, "level": "B", "keyWord": "rail", "defaultVoice": "male",
 "taps": [
  {"phrase": "to glance at his watch", "target": "the boy", "voice": "male", "keys": kb},
  {"phrase": "to grip the metal rail", "target": "the boy", "voice": "male", "keys": kb},
  {"phrase": "to fill every lane", "target": "the cars", "voice": "male", "keys": keys(cars)}],
 "stillS": 8.0,
 "nouns": [{"word": "the sky", "x": .5, "y": .08, "voice": "male"},
           {"word": "a streetlight", "x": .78, "y": .24, "voice": "male"},
           {"word": "cars", "x": .3, "y": .42, "voice": "male"},
           {"word": "a rail", "x": .13, "y": .73, "voice": "male"}],
 "question": "What is the boy holding?",
 "answer": ["He", "is", "gripping", "the", "metal", "rail."],
 "answerVoice": "male",
 "notes": "Cars box off 1.5-3.5 (inside the car, mostly hidden by the boy / scooters). 'the cars' box at 0-1.0 only covers the right part of the window to avoid the boy's box. Boy grips the rail from 6.5 s."}
json.dump(c, open(f"{HERE}/content/5414.json", "w"), indent=1)
