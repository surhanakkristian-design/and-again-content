import json
def keys(times, boxes):
    return [{"t": t, "off": True} if b is None else {"t": t, "x": round(b[0],2), "y": round(b[1],2), "w": round(b[2],2), "h": round(b[3],2)} for t, b in zip(times, boxes)]
T = [i*0.5 for i in range(25)]
N = None
brd = [(0,.20,.50,.80),(0,.20,.53,.80),(0,.18,.57,.82),(0,.18,.50,.82),(0,.18,.52,.82),(.02,.18,.56,.82),(0,.18,.58,.82),(.02,.18,.56,.82),(0,.17,.60,.83),(0,.17,.60,.83),
       (.40,.29,.22,.67),(.40,.29,.23,.67),(.38,.28,.24,.65),(.33,.47,.14,.29),(.36,.47,.11,.27),(.36,.49,.11,.27),(.34,.49,.12,.29),(.34,.51,.12,.29),(.33,.54,.13,.32),(.32,.57,.13,.32),
       (.31,.63,.14,.36),(.31,.68,.14,.32),(.31,.81,.14,.19),(.31,.83,.14,.17),(.31,.88,.15,.12)]
gls = [(.50,.18,.50,.82),(.53,.18,.47,.82),(.57,.18,.43,.82),(.50,.17,.50,.83),(.52,.17,.48,.83),(.58,.25,.42,.75),(.58,.20,.42,.80),(.58,.20,.42,.80),(.60,.20,.40,.80),(.60,.20,.40,.80),
       (.62,.29,.20,.67),(.63,.29,.20,.67),(.62,.28,.24,.65),(.47,.47,.12,.29),(.47,.47,.12,.27),(.47,.49,.11,.27),(.46,.49,.11,.29),(.46,.51,.11,.29),(.46,.54,.11,.32),(.45,.57,.12,.32),
       (.45,.63,.11,.36),(.45,.68,.12,.32),(.45,.81,.10,.19),(.45,.83,.10,.17),(.46,.88,.11,.12)]
dov = [N]*12 + [(.24,.08,.25,.20),(.28,.35,.42,.12),(.18,.33,.60,.14),(.08,.28,.82,.19),(0,.18,1,.31),(0,.08,1,.43),(0,0,1,.54),(0,0,1,.57),
       (0,0,1,.52),(0,0,1,.52),(0,0,1,.68),(0,0,1,.65),(0,0,1,.55)]
kb, kg, kd = keys(T, brd), keys(T, gls), keys(T, dov)
d = {"mediaId": 5144, "level": "B", "keyWord": "dove", "defaultVoice": "male",
 "taps": [{"phrase": "to weep on his shoulder", "target": "the bearded man", "voice": "male", "keys": kb},
          {"phrase": "to wear a beige suit", "target": "the man with glasses", "voice": "male", "keys": kg},
          {"phrase": "to soar above the monument", "target": "the flying doves", "voice": "male", "keys": kd}],
 "stillS": 10.0,
 "nouns": [{"word": "doves", "x": 0.50, "y": 0.14, "voice": "male"}, {"word": "a monument", "x": 0.47, "y": 0.50, "voice": "male"},
           {"word": "schoolgirls", "x": 0.14, "y": 0.75, "voice": "male"}, {"word": "a wicker basket", "x": 0.75, "y": 0.93, "voice": "male"}],
 "question": "What are the white doves doing?",
 "answer": ["They", "are", "soaring", "above", "the", "monument."], "answerVoice": "male",
 "notes": "Bearded man in the dark suit cries during the hug (2.0-4.5, tears and wet eyes visible); the man with glasses wears the beige suit. The two men stand close together all clip long: their boxes are split on a vertical line between them, and from 6.5 they are small in the wide shot (boxes narrow, below the 0.18 minimum width because they touch). 'the flying doves' only counts birds in the air (one dove at 6.0, the flock from 6.5); doves still in the baskets are not boxed. The flock box is cut off horizontally above the men's heads at 6.5-10.5. 0.0-5.5 doves are only in baskets, so off."}
json.dump(d, open('content/5144.json','w'), indent=1, ensure_ascii=False)
