import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else {"t":t,"off":True} for t,r in zip(T,rows)]
bra=K([(.31,.17,.31,.43),(.38,.16,.36,.37),(.46,.14,.54,.21),(.45,.16,.48,.22),(.40,.15,.28,.44),(.17,.13,.42,.43),(.29,.15,.30,.46),(.39,.15,.24,.46)])
peg=K([(.38,.73,.18,.14),(.43,.83,.18,.14),(.42,.86,.18,.14),(.43,.86,.18,.14),(.43,.85,.18,.14),(.42,.85,.18,.14),(.41,.86,.18,.14),(.41,.86,.18,.14)])
cat=K([(.78,.55,.20,.14),(.79,.55,.20,.14),(.78,.56,.20,.14),(.79,.56,.20,.14),(.79,.56,.20,.14),(.80,.56,.20,.14),(.80,.56,.20,.14),(.80,.56,.20,.14)])
d={"mediaId":6888,"level":"A","keyWord":"bra","defaultVoice":"female",
"taps":[{"phrase":"to fly over the line","target":"the bra","voice":"female","keys":bra},
{"phrase":"to fall into the water","target":"the peg","voice":"female","keys":peg},
{"phrase":"to lie by the window","target":"the cat","voice":"female","keys":cat}],
"stillS":2.2,
"nouns":[{"word":"a towel","x":.17,"y":.43,"voice":"female"},{"word":"a bra","x":.53,"y":.33,"voice":"female"},
{"word":"a bike","x":.18,"y":.72,"voice":"female"},{"word":"a cat","x":.88,"y":.62,"voice":"female"}],
"question":"What is hanging on the line?","answer":["A","pink","bra","is","hanging","on","the","line."],"answerVoice":"female",
"notes":"No people; evenId true -> female voices. Bra flips up over the line at 1.2-1.7. Peg is in the air at 0.2 and lies in the puddle from 0.7 (small, min-size box). Cat lies on the windowsill, small. Question: other washing also hangs on the line, but the model answer names the key word."}
json.dump(d,open("content/6888.json","w"),indent=1)
