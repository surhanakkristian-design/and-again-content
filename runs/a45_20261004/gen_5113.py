import json
def keys(times, boxes):
    return [{"t": t, "off": True} if b is None else {"t": t, "x": b[0], "y": b[1], "w": round(b[2], 2), "h": round(b[3], 2)} for t, b in zip(times, boxes)]
T = [i * 0.5 for i in range(21)]
wom = [(0,0,.44,.45),(0,0,.46,.47),(0,.02,.44,.50),(0,0,.43,.52),(0,0,.52,.48),(0,0,.46,.48),(0,.02,.46,.45),(.01,0,.54,.44),(.04,0,.57,.41),(.04,0,.57,.43),
       (.07,0,.53,.55),(.06,0,.53,.50),(.04,.05,.50,.44),(.04,.07,.52,.44),(.04,.10,.51,.44),(.01,.11,.50,.43),(0,.12,.56,.43),(.02,.12,.57,.44),(0,.14,.61,.47),(0,.14,.60,.52),(0,.14,.60,.52)]
man = [(.57,0,.43,.44),(.56,0,.44,.44),(.51,.03,.49,.42),(.53,.03,.47,.43),(.55,0,.45,.45),(.50,0,.50,.47),(.55,.03,.45,.44),(.59,0,.41,.46),(.63,0,.37,.45),(.72,0,.28,.46),
       (.77,.04,.23,.60),(.72,.05,.28,.62),(.62,.10,.38,.42),(.61,.12,.39,.44),(.62,.15,.38,.42),(.60,.17,.40,.40),(.59,.19,.41,.42),(.61,.19,.39,.42),(.62,.19,.38,.44),(.61,.19,.39,.45),(.61,.19,.39,.46)]
kw, km = keys(T, wom), keys(T, man)
d = {"mediaId": 5113, "level": "A", "keyWord": "advice", "defaultVoice": "female",
 "taps": [{"phrase": "to point at the poster", "target": "the woman", "voice": "female", "keys": kw},
          {"phrase": "to give a thumbs up", "target": "the young man", "voice": "male", "keys": km},
          {"phrase": "to touch his shoulder", "target": "the woman", "voice": "female", "keys": kw}],
 "stillS": 7.0,
 "nouns": [{"word": "a poster", "x": 0.50, "y": 0.15, "voice": "female"}, {"word": "tomatoes", "x": 0.24, "y": 0.63, "voice": "female"},
           {"word": "milk", "x": 0.87, "y": 0.62, "voice": "female"}, {"word": "a fish", "x": 0.45, "y": 0.76, "voice": "female"}],
 "question": "What is the woman pointing at?",
 "answer": ["She", "is", "pointing", "at", "the", "poster."], "answerVoice": "female",
 "notes": "Pointing at the food pyramid poster at 8.0-8.5; hand on his shoulder 9.0-10.0; thumbs up 9.5-10.0. Hands placing rice (2.5) and fish (3.5) come from the right edge and are not clearly attributable, so no 'put food on the table' phrase. The two people touch at 9.0-10.0 (her arm behind his back): boxes split vertically around x 0.61. 'advice' is abstract, in no text."}
json.dump(d, open('content/5113.json', 'w'), indent=1, ensure_ascii=False)
