import json
T=[i*0.5 for i in range(21)]
W={0.0:[.18,.04,.72,.50],0.5:[.18,.04,.72,.50],1.0:[.18,.04,.72,.50],1.5:[.18,.04,.72,.50],
2.0:[.16,.04,.80,.50],2.5:[.16,.04,.84,.49],3.0:[.18,.06,.59,.48],3.5:[.22,.06,.56,.48],
4.0:[.14,.05,.86,.48],4.5:[.16,.07,.76,.40],5.0:[.24,.09,.41,.56],5.5:[.28,.10,.37,.55],
6.0:[.28,.08,.37,.54],6.5:[.28,.11,.37,.51],7.0:[.30,.12,.31,.54],7.5:[.30,.12,.32,.54],
8.0:[.30,.15,.31,.47],8.5:[.30,.19,.32,.43],9.0:[.30,.19,.31,.43],9.5:[.30,.19,.31,.43],10.0:[.30,.19,.31,.43]}
P={0.0:[.68,.55,.32,.21],0.5:[.68,.55,.32,.21],1.0:[.68,.55,.32,.21],1.5:[.68,.55,.32,.21],
2.0:[.68,.55,.32,.21],2.5:[.64,.54,.36,.21],3.0:[.66,.55,.34,.21],3.5:[.66,.55,.34,.21],
4.0:[.64,.54,.36,.19],4.5:[.64,.48,.36,.26],5.0:[.66,.39,.34,.34],5.5:[.66,.35,.34,.38],
6.0:[.66,.30,.34,.42],6.5:[.66,.24,.34,.47],7.0:[.62,.17,.38,.54],7.5:[.63,.17,.37,.54],
8.0:[.62,.17,.38,.54],8.5:[.63,.17,.37,.54],9.0:[.62,.17,.38,.54],9.5:[.62,.17,.38,.54],10.0:[.62,.17,.38,.54]}
def keys(d): return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
c={"mediaId":4572,"level":"B","keyWord":"correct","defaultVoice":"female",
"taps":[
{"phrase":"to correct exam papers","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to adjust her red glasses","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to tower above her head","target":"the pile on the right","voice":"female","keys":keys(P)}],
"stillS":9.5,
"nouns":[{"word":"a clock","x":.50,"y":.19,"voice":"female"},{"word":"glasses","x":.50,"y":.31,"voice":"female"},
{"word":"a blouse","x":.48,"y":.48,"voice":"female"},{"word":"a coffee cup","x":.78,"y":.70,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","correcting","a","pile","of","exam","papers."],
"answerVoice":"female",
"notes":"Woman box is cut at the top of the right pile while her hands rest between the piles (0-4.5 s), so the two boxes never overlap. 'to tower above her head' fits only the right pile (the left one ends at about head height), true from about 7 s. She touches her glasses only around 4.5 s. Two red pens lie on the desk at the end, so no 'a pen' noun."}
json.dump(c,open("content/4572.json","w"),indent=1)
