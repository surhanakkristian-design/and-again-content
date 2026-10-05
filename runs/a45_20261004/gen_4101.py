import json
T=[i*0.5 for i in range(30)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
man={1.0:(.28,.33,.44,.10),1.5:(.24,.36,.48,.08),2.0:(.24,.38,.18,.20),3.5:(.33,.36,.28,.12),4.0:(.23,.36,.50,.13)}
for t in T:
    if 4.5<=t<=10.0: man[t]=(.23,.36,.50,.26)
man[10.5]=(.36,.36,.24,.26)
bird={0.0:(.40,.37,.35,.29),0.5:(.41,.37,.35,.29),1.0:(.40,.43,.34,.25),1.5:(.42,.44,.32,.23),2.0:(.42,.39,.32,.28),2.5:(.41,.39,.34,.28),
3.0:(.40,.44,.34,.22),3.5:(.44,.49,.30,.16),11.0:(.39,.45,.35,.18),11.5:(.24,.24,.52,.38),12.0:(.02,.19,.94,.42),12.5:(0,.18,1,.44),
13.0:(0,.20,1,.43),13.5:(0,.20,1,.43),14.0:(0,.21,1,.41),14.5:(0,.21,1,.41)}
ppl={t:((0,.68,1,.32) if t<13 else (0,.63,1,.37)) for t in T}
c={"mediaId":4101,"level":"A","keyWord":"show","defaultVoice":"male",
"taps":[{"phrase":"to open his arms","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to show its big tail","target":"the bird","voice":"male","keys":keys(bird)},
{"phrase":"to watch the show","target":"the people","voice":"male","keys":keys(ppl)}],
"stillS":12.5,
"nouns":[{"word":"light","x":.50,"y":.08,"voice":"male"},{"word":"a bird","x":.50,"y":.50,"voice":"male"},
{"word":"a phone","x":.17,"y":.76,"voice":"male"},{"word":"people","x":.58,"y":.89,"voice":"male"}],
"question":"What is the bird showing?",
"answer":["The","bird","is","showing","its","big","tail."],"answerVoice":"male",
"notes":"The bird is a peacock ('bird' used for level A). The man (performer in white, taken as male) stands behind the bird at the start: off at 0-0.5 and 2.5-3.0 (hidden by bird/cloth), slim boxes above the bird's head at 1.0-2.0, off from 11.0 (hidden behind the tail). From 4.5 to 10.5 his box also takes the top of the cloth cone that hangs from him. The bird is hidden under the cloth 4.0-10.5 (off). People = the dark audience at the bottom; their box starts higher from 13.0 (raised hands) and stops at the tail. Phones: slot is on the left phone; a second smaller phone is at the right (x .70). The open tail shows flag colours - not mentioned. 'light' = the spotlight beam."}
json.dump(c,open('content/4101.json','w'),indent=1)
