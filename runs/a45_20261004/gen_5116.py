import json
def keys(times, boxes):
    return [{"t": t, "off": True} if b is None else {"t": t, "x": b[0], "y": b[1], "w": round(b[2], 2), "h": round(b[3], 2)} for t, b in zip(times, boxes)]
T = [i * 0.5 for i in range(25)]
N = None
man = [N,N,N,N,(0,.10,.56,.90),(0,.19,1.0,.81),(.18,.25,.82,.75),(.12,.25,.85,.75),(.30,.32,.60,.68),(.32,.31,.68,.69),(.10,.33,.86,.67),(.13,.38,.84,.62),
       (.19,.36,.59,.64),(.22,.36,.47,.64),(.26,.35,.52,.65),(.36,.35,.32,.65),(.29,.36,.42,.64),(.19,.37,.66,.63),(.11,.38,.78,.60),(.34,.39,.32,.58),
       (.34,.38,.30,.44),(.33,.38,.33,.40),(.35,.38,.31,.39),(.35,.38,.31,.39),(.35,.39,.31,.39)]
km = keys(T, man)
d = {"mediaId": 5116, "level": "A", "keyWord": "to open", "defaultVoice": "male",
 "taps": [{"phrase": "to open the curtains", "target": "the young man", "voice": "male", "keys": km},
          {"phrase": "to open the balcony doors", "target": "the young man", "voice": "male", "keys": km},
          {"phrase": "to walk onto the balcony", "target": "the young man", "voice": "male", "keys": km}],
 "stillS": 12.0,
 "nouns": [{"word": "the sky", "x": 0.50, "y": 0.28, "voice": "male"}, {"word": "a curtain", "x": 0.10, "y": 0.62, "voice": "male"},
           {"word": "a balcony", "x": 0.50, "y": 0.70, "voice": "male"}, {"word": "the floor", "x": 0.50, "y": 0.90, "voice": "male"}],
 "question": "What is the young man opening?",
 "answer": ["He", "is", "opening", "the", "balcony", "doors."], "answerVoice": "male",
 "notes": "0.0-1.5 is a separate kitchen shot where only a bare arm opens a small window; it cannot be told whose arm it is, so the man's box is off there. Only one person in the clip, so all three phrases are on the young man (curtains 4.0-5.5, windows 6.0-7.0, balcony doors 8.0-9.0, steps out 10.0-12.0). The 'balcony' pill sits on the railing next to his legs. The question has one model answer; 'the curtains' / 'the windows' would also be true at other moments."}
json.dump(d, open('content/5116.json', 'w'), indent=1, ensure_ascii=False)
