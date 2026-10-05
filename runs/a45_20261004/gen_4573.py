import json
T=[i*0.5 for i in range(19)]
Wm={0.0:[.45,0,.55,.42],0.5:[.24,0,.76,.54],1.0:[.20,0,.78,.61],1.5:[.18,0,.80,.62],2.0:[.16,0,.72,.73],
4.5:[.70,.19,.30,.56],5.0:[.70,.17,.30,.54],5.5:[.71,.17,.29,.54],6.0:[.70,.17,.30,.47],6.5:[.71,.17,.29,.47],
7.0:[.67,.20,.33,.46],7.5:[.65,.20,.35,.46],8.0:[.63,.17,.37,.45],8.5:[.63,.17,.37,.36],9.0:[.66,.16,.34,.42]}
M={0.0:[0,.58,.42,.24],0.5:[0,.57,.45,.17],1.0:[0,.65,.40,.17],
2.5:[0,.07,.58,.66],3.0:[0,.11,.44,.55],3.5:[0,.12,.40,.38],4.0:[0,.13,.38,.24],
4.5:[0,.19,.30,.60],5.0:[0,.16,.32,.52],5.5:[0,.15,.32,.47],6.0:[0,.15,.32,.45],6.5:[0,.15,.32,.45],
7.0:[0,.16,.38,.48],7.5:[0,.16,.35,.46],8.0:[0,.14,.34,.46],8.5:[0,.14,.32,.40],9.0:[0,.13,.36,.42]}
V={4.5:[.40,.07,.29,.31],5.0:[.33,.06,.29,.36],5.5:[.34,.05,.30,.34],6.0:[.37,.05,.31,.31],6.5:[.40,.05,.30,.31],
7.0:[.39,.05,.27,.33],7.5:[.36,.05,.28,.32],8.0:[.35,.05,.27,.29],8.5:[.33,.04,.29,.32],9.0:[.37,.04,.28,.33]}
def keys(d): return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
c={"mediaId":4573,"level":"B","keyWord":"secret","defaultVoice":"male",
"taps":[
{"phrase":"to slide a folded napkin","target":"the elderly woman","voice":"female","keys":keys(Wm)},
{"phrase":"to open a leather briefcase","target":"the man with the gold watch","voice":"male","keys":keys(M)},
{"phrase":"to play the violin","target":"the violinist","voice":"male","keys":keys(V)}],
"stillS":9.0,
"nouns":[{"word":"a violin","x":.52,"y":.13,"voice":"male"},{"word":"a tablecloth","x":.48,"y":.48,"voice":"male"},
{"word":"banknotes","x":.50,"y":.64,"voice":"male"},{"word":"a wheelbarrow","x":.32,"y":.79,"voice":"male"}],
"question":"What are the man and woman doing?",
"answer":["They","are","shaking","hands","over","a","wheelbarrow."],
"answerVoice":"male",
"notes":"Cuts at 2.5 s and 4.5 s. At 0-1 s only the man's hand with the gold watch is in the picture (boxed). Violinist appears only from 4.5 s. During the handshake (7-9 s) the outstretched arms cross under the violinist, so the man's and woman's boxes hold body and head, not the joined hands. The napkin slide is short (0-0.5 s). Briefcase looks dark brown. Other diners and a waiter in the background are not targets."}
json.dump(c,open("content/4573.json","w"),indent=1)
