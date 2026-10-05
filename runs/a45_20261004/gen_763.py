import json
O=None
def mk(K,i):
    out=[]
    for t in sorted(K):
        b=K[t][i]
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
# tablecloth, cat, sun
K={0.0:((.23,.47,.56,.22),O,(.38,.22,.24,.17)),
0.5:((.21,.42,.61,.17),O,(.38,.24,.24,.17)),
1.0:((.19,.55,.60,.22),O,(.38,.28,.24,.17)),
1.5:((.20,.08,.66,.30),O,(.38,.44,.24,.17)),
2.0:((.20,.08,.64,.24),O,(.38,.60,.24,.17)),
2.5:((.13,.15,.76,.29),O,(.39,.61,.24,.17)),
3.0:((.08,.23,.92,.30),O,(.39,.54,.24,.14)),
3.5:((.08,.48,.88,.42),O,(.40,.34,.24,.14)),
4.0:((0,.52,1,.40),O,(.39,.23,.24,.17)),
4.5:((0,.50,1,.40),O,(.39,.18,.24,.17)),
5.0:((0,.50,1,.48),O,(.39,.17,.24,.16)),
5.5:((0,.48,1,.48),O,(.39,.17,.24,.16)),
6.0:((0,.48,1,.37),O,(.39,.17,.24,.16)),
6.5:((0,.48,1,.41),O,(.40,.18,.24,.16)),
7.0:((0,.50,1,.48),O,(.39,.18,.24,.16)),
7.5:((0,.50,1,.48),O,(.40,.18,.24,.16)),
8.0:((0,.50,1,.40),O,(.39,.18,.24,.16)),
8.5:((0,.50,1,.40),O,(.40,.18,.24,.16)),
9.0:((0,.60,.69,.40),(.70,.52,.30,.37),(.39,.19,.24,.16)),
9.5:((0,.65,1,.33),(.42,.46,.36,.18),(.40,.19,.24,.16)),
10.0:((0,.69,1,.21),(.38,.49,.24,.19),(.39,.19,.24,.16))}
d={"mediaId":763,"level":"B","keyWord":"tablecloth","defaultVoice":"male",
"taps":[{"phrase":"to float through the air","target":"the tablecloth","voice":"male","keys":mk(K,0)},
{"phrase":"to wander across the table","target":"the cat","voice":"male","keys":mk(K,1)},
{"phrase":"to set over the sea","target":"the sun","voice":"male","keys":mk(K,2)}],
"stillS":8.5,
"nouns":[{"word":"a tablecloth","x":.50,"y":.74,"voice":"male"},{"word":"a vase","x":.51,"y":.57,"voice":"male"},
{"word":"the sea","x":.42,"y":.37,"voice":"male"},{"word":"the sun","x":.52,"y":.25,"voice":"male"}],
"question":"What are they doing?",
"answer":["They","are","spreading","a","tablecloth","over","the","table."],
"answerVoice":"male",
"notes":"The man and the woman do exactly the same throughout, so no phrase fits only one of them; targets are the tablecloth, the cat and the sun instead. The cat is a dark sliver at the right edge at 8.0-8.5 s (off there), jumps up at 9.0 s and walks on the table at 9.5-10.0 s: there the tablecloth box is cut (right part at 9.0 s, only the part below the cat at 9.5-10.0 s). Sun box = the disc only, not its reflection on the sea. 'to set over the sea' is a slow state-like action (sunset). defaultVoice male: mixed pair, odd id."}
json.dump(d,open("content/763.json","w"),indent=1,ensure_ascii=False)
