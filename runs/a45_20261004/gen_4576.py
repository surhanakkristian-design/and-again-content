import json
T=[i*0.5 for i in range(19)]
W={0.0:[0,.07,1.0,.70],0.5:[0,.07,1.0,.72],1.0:[0,.07,1.0,.71],1.5:[0,.08,1.0,.72],2.0:[0,.07,1.0,.72],2.5:[0,.07,1.0,.72],3.0:[0,.08,1.0,.72],
3.5:[.31,.17,.43,.24],4.0:[.34,.16,.41,.23],4.5:[.38,.16,.38,.20],5.0:[.38,.16,.36,.19],5.5:[.40,.19,.24,.14],6.0:[.40,.19,.24,.14],
6.5:[.40,.20,.22,.14],7.0:[.42,.21,.20,.14],7.5:[.42,.20,.20,.14],8.0:[.40,.14,.22,.18],8.5:[.39,.14,.22,.18],9.0:[.40,.15,.20,.18]}
def keys(d): return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
c={"mediaId":4576,"level":"A","keyWord":"count","defaultVoice":"female",
"taps":[
{"phrase":"to count the papers","target":"the woman in green","voice":"female","keys":keys(W)},
{"phrase":"to hold a blue pen","target":"the woman in green","voice":"female","keys":keys(W)},
{"phrase":"to raise her hands","target":"the woman in green","voice":"female","keys":keys(W)}],
"stillS":0.0,
"nouns":[{"word":"a chair","x":.72,"y":.33,"voice":"female"},{"word":"hair","x":.27,"y":.44,"voice":"female"},
{"word":"a pen","x":.47,"y":.61,"voice":"female"},{"word":"paper","x":.68,"y":.78,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","counting","the","papers."],
"answerVoice":"female",
"notes":"Only one clear target (the woman in green at the head of the table), so all three phrases use her; everyone else is a crowd doing the same counting, so 'to count the papers' is not unique to her in the wide shot (3.5 s on) - she is the only one shown close and the one the camera stays on. She is small from 5.5 s (minimum-size box). Both arms go up only at 8-9 s. A second (white) chair stands at the right edge at 0 s; the pill is on the nearer pink one. 'paper' is on the pile, the tally sheet is also paper."}
json.dump(c,open("content/4576.json","w"),indent=1)
