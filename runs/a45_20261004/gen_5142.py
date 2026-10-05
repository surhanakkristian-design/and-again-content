import json
def keys(times, boxes):
    return [{"t": t, "off": True} if b is None else {"t": t, "x": round(b[0],2), "y": round(b[1],2), "w": round(b[2],2), "h": round(b[3],2)} for t, b in zip(times, boxes)]
T = [i*0.5 for i in range(25)]
N = None
man = [(.05,.26,.73,.74),(.03,.26,.76,.74),(.02,.27,.77,.73),(0,.27,.79,.73),(0,.36,.82,.64),(0,.33,.88,.67),(0,.33,.86,.67),
       (0,.26,.88,.74),(0,.27,.86,.73),(0,.26,.94,.74),(0,.40,.90,.60),(.08,.10,.37,.78),(0,0,.26,.50),
       N,N,N,N,(.80,.24,.20,.76),(.50,.44,.43,.56),(.30,.44,.42,.56),(.32,.40,.40,.60),(.32,.39,.40,.61),(.31,.40,.40,.60),(.31,.39,.40,.61),(.30,.39,.40,.61)]
girl = [N]*13 + [(0,.80,.36,.20),(0,.40,.40,.60),(0,.55,.70,.45),(.33,.27,.67,.73),(0,.66,.38,.34)] + [N]*7
crowd = [N]*17 + [(.45,.27,.34,.14),(.28,.35,.68,.09),(.08,.32,.88,.12),(.05,.24,.90,.16),(.05,.24,.90,.15),(.05,.24,.90,.16),(.05,.24,.90,.15),(.05,.24,.90,.15)]
km, kg, kc = keys(T, man), keys(T, girl), keys(T, crowd)
d = {"mediaId": 5142, "level": "B", "keyWord": "neighborhood", "defaultVoice": "male",
 "taps": [{"phrase": "to smooth down a flag", "target": "the old man", "voice": "male", "keys": km},
          {"phrase": "to dash across the lawn", "target": "the little girl", "voice": "female", "keys": kg},
          {"phrase": "to wave from their gardens", "target": "the neighbours", "voice": "male", "keys": kc}],
 "stillS": 10.0,
 "nouns": [{"word": "bunting", "x": 0.50, "y": 0.09, "voice": "male"}, {"word": "neighbours", "x": 0.68, "y": 0.33, "voice": "male"},
           {"word": "overalls", "x": 0.52, "y": 0.70, "voice": "male"}, {"word": "a picket fence", "x": 0.14, "y": 0.80, "voice": "male"}],
 "question": "What is the little girl doing?",
 "answer": ["She", "is", "dashing", "across", "the", "lawn."], "answerVoice": "female",
 "notes": "Old man (white moustache, overalls) boxed 0.0-6.0 and 8.5-12.0; 6.5-8.0 off (men on ladders in the background are too small to tell apart; another man in jeans hammers at 5.5 and is not boxed). At 6.0 only his overall-clad legs are visible top left. The neighbours box (waving crowd far down the street) is split from the old man's head along a horizontal line at 9.0-12.0, so it is thin at 9.0. The girl with painted cheeks runs 6.5-8.5. Key word 'neighborhood' is not a visible noun, used in no text."}
json.dump(d, open('content/5142.json','w'), indent=1, ensure_ascii=False)
