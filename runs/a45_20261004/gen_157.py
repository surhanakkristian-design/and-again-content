import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
W={0.0:(.22,0,.65,1),0.5:(.22,0,.75,1),1.0:(.26,.06,.52,.94),1.5:(.29,.10,.53,.90),2.0:(.36,.15,.52,.85),2.5:(.34,.17,.62,.83),
3.0:(.39,.16,.61,.84),3.5:(.41,.18,.59,.82),4.0:(.43,.13,.57,.87),4.5:(.48,.14,.52,.86),5.0:(.53,.20,.47,.80),5.5:(.54,.20,.46,.80),
6.0:(.55,.21,.45,.79),6.5:(.51,.20,.49,.80),7.0:(.50,.21,.50,.79),7.5:(.48,.20,.52,.80),8.0:(.48,.23,.52,.77),8.5:(.45,.23,.55,.77),
9.0:(.52,.23,.48,.77),9.5:(.54,.23,.46,.77),10.0:(.55,.23,.45,.77)}
M={0.0:(0,0,.10,1),0.5:(0,0,.09,1),1.0:(0,.02,.10,.98),1.5:(0,.08,.13,.92),2.0:(0,.03,.20,.97),2.5:(0,.03,.20,.97),
3.0:(0,0,.20,1),3.5:(0,0,.22,1),4.0:(0,0,.20,1),4.5:(0,0,.27,1),5.0:(0,.04,.32,.96),5.5:(0,.07,.33,.93),
6.0:(0,.05,.32,.95),6.5:(0,.03,.29,.97),7.0:(0,.05,.29,.95),7.5:(0,.05,.27,.95),8.0:(0,.05,.28,.95),8.5:(0,.05,.28,.95),
9.0:(0,.05,.31,.95),9.5:(0,.05,.32,.95),10.0:(0,.05,.31,.95)}
B={0.0:(.10,.20,.12,.15),0.5:(.09,.22,.13,.15),1.0:(.11,.24,.15,.15),1.5:(.14,.28,.15,.15),2.0:(.21,.30,.15,.14),2.5:(.20,.31,.14,.15),
3.0:(.21,.34,.18,.15),3.5:(.23,.35,.18,.15),4.0:(.24,.34,.19,.14),4.5:(.28,.34,.20,.14),5.0:(.33,.35,.19,.14),5.5:(.34,.35,.19,.14),
6.0:(.33,.36,.20,.14),6.5:(.30,.36,.20,.14),7.0:(.30,.38,.19,.14),7.5:(.28,.38,.19,.14),8.0:(.29,.38,.18,.14),8.5:(.29,.38,.16,.14),
9.0:(.32,.38,.19,.14),9.5:(.33,.38,.20,.14),10.0:(.32,.37,.22,.14)}
c={"mediaId":157,"level":"A","keyWord":"chewing gum","defaultVoice":"female",
"taps":[
 {"phrase":"to open the chewing gum","target":"the woman","voice":"female","keys":keys(W)},
 {"phrase":"to look at the woman","target":"the man","voice":"male","keys":keys(M)},
 {"phrase":"to stand behind the people","target":"the bird","voice":"female","keys":keys(B)}],
"stillS":0.0,
"nouns":[{"word":"chewing gum","x":.52,"y":.64,"voice":"female"},{"word":"a drink","x":.90,"y":.57,"voice":"female"},
 {"word":"a bird","x":.15,"y":.27,"voice":"female"},{"word":"the sea","x":.80,"y":.33,"voice":"female"}],
"question":"What is the woman opening?",
"answer":["She","is","opening","the","chewing gum."],
"answerVoice":"female",
"notes":"The three targets stand very close: the bird (a seagull on the rail) sits between the man's and the woman's heads, so its box is narrower than 0.18 at 0.0-2.5 and the woman's box starts right of the bird (her left sleeve/hand is outside her box in several frames). Man is only a sliver at the left edge 0.0-1.5. 'to look at the woman': the man watches her most of the clip. 'chewing gum.' kept as one chip. At stillS 0.0 the 'chewing gum' pill is on the wrapped stick in her hands."}
json.dump(c,open("content/157.json","w"),indent=1)
