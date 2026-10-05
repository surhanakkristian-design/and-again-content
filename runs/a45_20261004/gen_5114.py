import json
def keys(times, boxes):
    return [{"t": t, "off": True} if b is None else {"t": t, "x": b[0], "y": b[1], "w": round(b[2], 2), "h": round(b[3], 2)} for t, b in zip(times, boxes)]
T = [i * 0.5 for i in range(25)]
N = None
old = [N,N,N,(.12,.30,.45,.45),(.15,.29,.42,.48),(.15,.29,.43,.50),(.15,.30,.42,.50),(.14,.30,.42,.52),(.10,.29,.40,.52),(.08,.28,.38,.55),(.07,.28,.34,.56),(.07,.28,.31,.56),(.10,.27,.30,.58),
       N,N,N,N,N, N,N,N,N,N,N,N]
grn = [(.46,.34,.54,.66),(.46,.34,.54,.66),(.46,.35,.54,.65),(.58,.34,.22,.30),(.58,.35,.23,.30),(.59,.35,.21,.32),(.58,.35,.22,.33),(.56,.36,.21,.30),(.50,.35,.25,.35),(.46,.35,.26,.34),(.41,.36,.28,.34),(.38,.35,.29,.34),(.40,.37,.30,.35),
       N,N,N,N,N, (.52,.38,.48,.62),(.52,.39,.48,.61),(.53,.41,.47,.59),(.49,.40,.51,.60),(.47,.41,.53,.59),(.47,.41,.53,.59),(.48,.42,.52,.58)]
fla = [N]*13 + [(0,.43,1,.14),(0,.41,1,.15),(0,.39,1,.17),(0,.34,1,.24),(0,.33,1,.26)] + [N]*7
ko, kg, kf = keys(T, old), keys(T, grn), keys(T, fla)
d = {"mediaId": 5114, "level": "B", "keyWord": "flamingo", "defaultVoice": "female",
 "taps": [{"phrase": "to peer through a telescope", "target": "the older man", "voice": "male", "keys": ko},
          {"phrase": "to jot down notes", "target": "the woman with green hair", "voice": "female", "keys": kg},
          {"phrase": "to take flight", "target": "the flamingos", "voice": "female", "keys": kf}],
 "stillS": 7.0,
 "nouns": [{"word": "the sky", "x": 0.50, "y": 0.20, "voice": "female"}, {"word": "flamingos", "x": 0.50, "y": 0.48, "voice": "female"},
           {"word": "a lake", "x": 0.50, "y": 0.68, "voice": "female"}, {"word": "reeds", "x": 0.50, "y": 0.91, "voice": "female"}],
 "question": "What are the flamingos doing?",
 "answer": ["They", "are", "taking", "flight", "over", "the", "lake."], "answerVoice": "female",
 "notes": "Four shots: 0-1.0 from behind (people at the window), 1.5-6.0 front view inside the hide, 6.5-8.5 the lake with the flock, 9.0-12.0 from behind again. The older man peers through the spotting scope (called 'telescope') only in the front shot; in the two back shots he stands behind the green-haired woman, mostly hidden, holding binoculars, so his box is off there (avoids overlap with her box). The green-haired woman writes in a notepad in the back shots; in the front shot she is boxed on her face/hair between him and the dark-haired man. Flamingos are boxed only in the lake shot (6.5 still standing, take-off 7.0-8.5); in the back shots they are a tiny distant band behind the people, off. Several people hold binoculars, so no binocular phrase."}
json.dump(d, open('content/5114.json', 'w'), indent=1, ensure_ascii=False)
