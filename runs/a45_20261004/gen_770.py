import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} if b else {"t":t,"off":True})
    return out
W={0.0:(.36,.35,.62,.52),0.5:(.42,.40,.45,.46),1.0:(.62,.5,.38,.44),1.5:(.82,.53,.18,.42),2.0:(.82,.52,.18,.36),2.5:(.6,.47,.4,.42),
 3.0:(.29,.47,.42,.5),3.5:(.32,.47,.3,.5),4.0:(0,.45,.5,.47),4.5:(.17,.44,.31,.45),5.0:(.27,.48,.44,.47),5.5:(.34,.49,.64,.43),
 6.0:(.2,.5,.8,.25),6.5:(.15,.54,.8,.2),7.0:(.14,.55,.76,.32),7.5:(.15,.52,.63,.34),8.0:(.27,.48,.45,.27),8.5:(.24,.49,.47,.27),
 9.0:(.22,.51,.47,.36),9.5:(.24,.5,.47,.37),10.0:(.24,.5,.46,.26)}
O={1.0:(.01,.42,.18,.15),1.5:(.16,.4,.18,.16),2.0:(.11,.4,.19,.15),3.0:(.10,.33,.19,.15),3.5:(.53,.33,.19,.14),4.0:(.63,.37,.19,.16),
 4.5:(.53,.37,.18,.15),5.0:(.46,.35,.18,.13),5.5:(.54,.36,.18,.13),6.0:(.70,.33,.17,.16),6.5:(.68,.34,.18,.17),7.0:(.66,.33,.19,.22),
 7.5:(.58,.32,.18,.2),8.0:(.5,.31,.19,.17),8.5:(.44,.32,.19,.17),9.0:(.37,.32,.18,.19),9.5:(.31,.32,.18,.18),10.0:(.23,.32,.2,.18)}
B={0.0:(.11,.42,.18,.14),0.5:(.18,.42,.18,.14),1.0:(.38,.43,.18,.14),1.5:(.57,.42,.18,.14),2.0:(.52,.4,.18,.14),2.5:(.29,.37,.18,.14),
 3.0:(.47,.33,.18,.14),3.5:(.82,.33,.18,.14),4.0:(.82,.37,.18,.14),4.5:(.71,.37,.18,.14),6.0:(.87,.33,.13,.15),6.5:(.87,.34,.13,.15),
 7.0:(.86,.35,.14,.15),7.5:(.79,.35,.18,.14),8.0:(.74,.33,.18,.15),8.5:(.71,.33,.18,.16),9.0:(.72,.34,.18,.15),9.5:(.75,.34,.18,.15),10.0:(.78,.34,.18,.16)}
c={"mediaId":770,"level":"A","keyWord":"tennis","defaultVoice":"female",
"taps":[{"phrase":"to fall on the ground","target":"the woman in white","voice":"female","keys":keys(W)},
{"phrase":"to wear an orange shirt","target":"the man in orange","voice":"male","keys":keys(O)},
{"phrase":"to wear black clothes","target":"the man in black","voice":"male","keys":keys(B)}],
"stillS":10.0,
"nouns":[{"word":"a ball","x":.43,"y":.60,"voice":"female"},{"word":"a racket","x":.33,"y":.70,"voice":"female"},
{"word":"trees","x":.5,"y":.15,"voice":"female"},{"word":"a net","x":.80,"y":.50,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","playing","tennis."],"answerVoice":"female",
"notes":"The opponent in orange is small and far away; I read him as a man (headband, shorts) - check. He and the man in black are small, boxes at minimum size; the man in black box is narrower than 0.18 at 6.0-7.0 s (picture edge / next to the opponent). Where the opponent stands behind the woman (5.0, 8.0-10.0 s) the boxes are split at a horizontal line, his legs fall outside his box. 'A racket' at 10.0 s is the woman's racket on the ground; the opponent also holds one, small, at (0.38, 0.47)."}
json.dump(c,open('content/770.json','w'),indent=1,ensure_ascii=False)
