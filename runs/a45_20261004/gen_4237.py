import json
def K(d,times):
    out=[]
    for t in times:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
times=[i*0.5 for i in range(24)]
B={0.0:(.12,.21,.39,.43),0.5:(.20,.19,.39,.43),1.0:(.24,.19,.34,.42),1.5:(.25,.20,.33,.38),2.0:(.24,.20,.44,.23),2.5:(.27,.17,.33,.45),
3.0:(.24,.15,.38,.47),3.5:(.25,.17,.38,.48),4.0:(.22,.18,.48,.51),4.5:(.27,.24,.44,.46),5.0:(.29,.32,.40,.42),5.5:(.30,.33,.40,.41),
6.0:(.30,.32,.38,.38),6.5:(.27,.32,.37,.35),7.0:(.22,.325,.37,.31),7.5:(.25,.34,.36,.30),8.0:(.27,.29,.21,.34),8.5:(.27,.30,.21,.36),
9.0:(.25,.30,.24,.40),9.5:(.28,.30,.23,.42),10.0:(.24,.35,.38,.38),10.5:(.22,.32,.40,.45),11.0:(.27,.28,.37,.49),11.5:(.25,.27,.38,.50)}
H={4.0:(.64,0,.24,.15),4.5:(.56,0,.26,.22),5.0:(.50,.06,.27,.24),5.5:(.47,.09,.30,.24),6.0:(.42,.07,.32,.25),6.5:(.40,.07,.33,.25),
7.0:(.40,.05,.33,.275),7.5:(.42,.05,.36,.29),8.0:(.48,.04,.34,.36),8.5:(.49,.04,.36,.37),9.0:(.49,.04,.40,.40),9.5:(.51,.04,.44,.38),
10.0:(.48,0,.52,.35),10.5:(.50,0,.50,.32),11.0:(.50,0,.50,.28),11.5:(.50,0,.50,.27)}
C={0.0:(.51,.35,.21,.16),0.5:(.59,.36,.21,.19),1.0:(.58,.39,.23,.20),1.5:(.58,.40,.25,.21),2.0:(.57,.43,.27,.20),2.5:(.60,.43,.32,.26),
3.0:(.62,.49,.35,.29),3.5:(.64,.61,.36,.37),4.0:(.70,.77,.30,.23)}
c={"mediaId":4237,"level":"B","keyWord":"barn","defaultVoice":"male",
"taps":[
{"phrase":"to offer a carrot","target":"the boy","voice":"male","keys":K(B,times)},
{"phrase":"to lean over the stall","target":"the horse","voice":"male","keys":K(H,times)},
{"phrase":"to be packed with carrots","target":"the crate","voice":"male","keys":K(C,times)}],
"stillS":6.0,
"nouns":[{"word":"a horse","x":.60,"y":.16,"voice":"male"},{"word":"a carrot","x":.60,"y":.36,"voice":"male"},
{"word":"jeans","x":.50,"y":.59,"voice":"male"}],
"question":"What is the boy doing?",
"answer":["He","is","feeding","a","horse","in","the","barn."],
"answerVoice":"male",
"notes":"The small figure has a toddler's body but a bearded face (generated clip); called 'the boy' as in the description. Key word 'barn' is the whole room, so it has no single place for a noun pill; it is used in the answer instead. Only 3 nouns: the carrot in the hand is small at 6.0 s. Boy / horse boxes are split where the muzzle meets his head (7.0-9.5 s); boy / crate boxes are split where he reaches into the crate (1.0-3.5 s, his carrot arm is cut at 2.5 s, his legs at 2.0 s)."}
json.dump(c,open("content/4237.json","w"),indent=1)
