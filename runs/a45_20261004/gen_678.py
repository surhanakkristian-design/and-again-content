import json
OFF=None
def keys(d):
    out=[]
    for t in sorted(d):
        b=d[t]
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2],2),"h":round(b[3],2)})
    return out
G={0.0:(0,0,.17,1),0.5:(0,.08,.23,.92),1.0:(0,.16,.45,.84),1.5:(0,.16,.47,.84),2.0:(0,.22,.43,.78),2.5:(0,.38,.52,.62),
3.0:(0,.52,.42,.48),3.5:(0,.46,.50,.54),4.0:(0,.33,.50,.67),4.5:(0,.25,.63,.75),5.0:(0,.22,.56,.78),5.5:(0,.18,.57,.82),
6.0:(0,.13,.57,.87),6.5:(0,.10,.52,.90),7.0:(0,.11,.46,.89),7.5:(0,.16,.50,.84),8.0:(0,.18,.38,.72),8.5:(0,.10,.33,.62),
9.0:(0,.18,.33,.65),9.5:(0,.18,.42,.70),10.0:(0,.22,.41,.58)}
P={0.0:(.18,.18,.82,.82),0.5:(.24,.30,.76,.70),1.0:(.60,.26,.40,.74),1.5:(.48,.26,.52,.74),2.0:(.44,.27,.56,.73),2.5:(.53,.45,.47,.55),
3.0:(.43,.60,.57,.40),3.5:OFF,4.0:(.52,.40,.48,.60),4.5:(.64,.31,.36,.69),5.0:(.57,.28,.43,.72),5.5:(.58,.23,.42,.77),
6.0:(.58,.16,.42,.52),6.5:(.53,.12,.47,.55),7.0:(.47,.16,.50,.51),7.5:(.51,.22,.43,.39),8.0:(.40,.23,.47,.38),8.5:(.52,.20,.22,.37),
9.0:(.34,.35,.15,.40),9.5:(.43,.26,.40,.46),10.0:(.42,.24,.47,.47)}
C={t/2:OFF for t in range(21)}
C.update({7.0:(.80,.68,.20,.18),7.5:(.76,.62,.24,.24),8.0:(.63,.62,.37,.18),8.5:(.50,.58,.37,.16),9.0:(.50,.61,.34,.28)})
c={"mediaId":678,"level":"B","keyWord":"silk","defaultVoice":"female",
"taps":[
{"phrase":"to press silk against her cheek","target":"the woman in the beige shirt","voice":"female","keys":keys(G)},
{"phrase":"to have shoulder-length hair","target":"the woman in the purple blouse","voice":"female","keys":keys(P)},
{"phrase":"to crouch on the counter","target":"the cat","voice":"female","keys":keys(C)}],
"stillS":8.0,
"nouns":[{"word":"a fan","x":.36,"y":.07,"voice":"female"},{"word":"silk","x":.36,"y":.62,"voice":"female"},
{"word":"a cat","x":.82,"y":.70,"voice":"female"},{"word":"a counter","x":.40,"y":.80,"voice":"female"}],
"question":"What is the woman in beige doing?",
"answer":["She","is","pressing","silk","against","her","cheek."],
"answerVoice":"female",
"notes":"The woman in beige (hair in a bun) presses the silk to her own cheek at 4.5-5.5 s; at 4.0 s her hand holds it at the other woman's cheek, so she is still the one who presses. State phrase for the woman in purple (a bob to the shoulders; the other wears a bun) because every action of hers (laughing, gasping, looking up, hands on the counter) is also done by the woman in beige. The women overlap with each other and with the silk: boxes are split at a vertical line between them, so an arm of one sometimes lies in the other's box (2.5 s, 6.0 s). Purple woman off at 3.5 s (hidden by the silk); at 8.5 s and 9.0 s only a strip of her is visible beside the silk, small box. The cat is in the picture only 7.0-9.0 s (7.0 s half out of frame); at 9.5 s it is under the silk."}
json.dump(c,open('content/678.json','w'),indent=1,ensure_ascii=False)
