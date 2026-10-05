import json
def keys(times, boxes):
    return [{"t": t, "off": True} if b is None else {"t": t, "x": round(b[0],2), "y": round(b[1],2), "w": round(b[2],2), "h": round(b[3],2)} for t, b in zip(times, boxes)]
T = [i*0.5 for i in range(19)]
N = None
man = [(.31,.19,.38,.58),(.31,.19,.37,.53),(.32,.22,.36,.70),(.25,.16,.47,.82),(.32,.20,.58,.64),(.33,.21,.34,.60),(.34,.22,.39,.56),(.32,.25,.37,.52),
       (.33,.25,.35,.51),(.33,.21,.35,.56),(.33,.24,.35,.53),(.33,.21,.35,.58),(.30,.19,.37,.60),(.34,.18,.40,.66),(.33,.18,.40,.67),(.34,.18,.40,.66),
       (.34,.17,.40,.66),(.33,.18,.40,.63),(.26,.25,.40,.58)]
tram = [N]*13 + [(.15,.31,.19,.14),(0,.32,.33,.14),(0,.32,.34,.14),(0,.31,.34,.13),(0,.32,.33,.12),(0,.32,.26,.11)]
km, kt = keys(T, man), keys(T, tram)
d = {"mediaId": 5145, "level": "A", "keyWord": "tram", "defaultVoice": "male",
 "taps": [{"phrase": "to press a button", "target": "the young man", "voice": "male", "keys": km},
          {"phrase": "to look at his watch", "target": "the young man", "voice": "male", "keys": km},
          {"phrase": "to have blue doors", "target": "the tram", "voice": "male", "keys": kt}],
 "stillS": 7.0,
 "nouns": [{"word": "a building", "x": 0.22, "y": 0.25, "voice": "male"}, {"word": "a tram", "x": 0.15, "y": 0.39, "voice": "male"},
           {"word": "a jacket", "x": 0.55, "y": 0.47, "voice": "male"}, {"word": "jeans", "x": 0.50, "y": 0.62, "voice": "male"}],
 "question": "What is the young man doing?",
 "answer": ["He", "is", "looking", "at", "his", "watch."], "answerVoice": "male",
 "notes": "He presses the button on the traffic-light pole at 2.0 only; he looks at his watch 6.5-8.5. Whether the tram moves is hard to see (camera moves too), so its phrase is the state 'to have blue doors' (blue doors clearly visible at 7.0-8.0). The tram runs behind the man: its box is only the part left of him (the right part behind him is not boxed), thin at 9.0. Other pedestrians and cyclists are not boxed."}
json.dump(d, open('content/5145.json','w'), indent=1, ensure_ascii=False)
