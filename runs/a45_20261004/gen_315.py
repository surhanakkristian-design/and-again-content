import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
M={1.5:(0,.38,.26,.30),2.0:(0,.52,.70,.48),2.5:(0,.40,.72,.48),3.0:(0,.34,.52,.54),3.5:(0,.36,.50,.42),
4.0:(0,.22,.42,.55),4.5:(0,.22,.30,.54),5.0:(0,.27,.26,.60),5.5:(0,.29,.24,.57),6.0:(0,.29,.28,.42),6.5:(0,.29,.40,.44),
9.5:(.44,.33,.40,.47),10.0:(.32,.30,.50,.60)}
W={0.0:(0,0,.78,.24),0.5:(0,0,1,.62),1.0:(0,.12,1,.88),1.5:(.26,.24,.74,.74),2.0:(.14,.22,.86,.30),2.5:(.33,.18,.67,.22),
3.0:(.52,.21,.48,.44),3.5:(.50,.25,.45,.34),4.0:(.43,.28,.57,.31),4.5:(.47,.30,.53,.31),5.0:(.54,.34,.46,.40),
5.5:(.58,.35,.42,.38),6.0:(.56,.32,.44,.30),6.5:(.40,.35,.52,.27),7.0:(0,.40,.19,.47),7.5:(0,.58,.17,.39),
9.0:(0,.40,.47,.22),9.5:(.17,.27,.27,.22),10.0:(.10,.31,.22,.19)}
G={7.0:(.19,.55,.18,.16),7.5:(.40,.63,.18,.15),8.0:(.47,.56,.18,.15),8.5:(.50,.47,.25,.15)}
c={"mediaId":315,"level":"B","keyWord":"free kick","defaultVoice":"male",
"taps":[
{"phrase":"to take a free kick","target":"the player in red","voice":"male","keys":keys(M)},
{"phrase":"to form a defensive wall","target":"the defenders in black","voice":"male","keys":keys(W)},
{"phrase":"to dive for the ball","target":"the goalkeeper","voice":"male","keys":keys(G)}],
"stillS":6.0,
"nouns":[{"word":"a football","x":.72,"y":.67,"voice":"male"},{"word":"defenders","x":.78,"y":.47,"voice":"male"},
{"word":"a hill","x":.33,"y":.38,"voice":"male"},{"word":"the pitch","x":.30,"y":.85,"voice":"male"}],
"question":"What is the player in red doing?",
"answer":["He","is","taking","a","free","kick."],
"answerVoice":"male",
"notes":"The taker's shirt is dark red (maroon). Target 2 is a group (the four defenders in black forming the wall), one box around all of them. 2.0-3.5 s the taker bends in front of the wall and the two overlap: split by a horizontal line at 2.0/2.5 s (wall = upper bodies) and by a vertical line at 3.0/3.5 s (wall = the men right of the taker's head; the ball is outside the taker's box there). 9.5/10.0 s: defenders behind the kneeling taker, split vertically. The leg and arm at 0.0-1.5 s belong to a referee (not a target). Goalkeeper visible only 7.0-8.5 s, he dives at 8.5 s."}
json.dump(c,open("content/315.json","w"),indent=1,ensure_ascii=False)
