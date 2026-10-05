import json
def keys(times, d):
    return [{"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if d.get(t) else {"t":t,"off":True} for t in times]
times=[i*0.5 for i in range(21)]
W={0.0:(0,0,.33,.90),0.5:(0,.03,.60,.85),1.0:(0,.20,.50,.80),1.5:(0,.20,.20,.80),2.0:(0,.08,.38,.92),2.5:(0,.08,.22,.60),
3.5:(0,.13,.48,.83),4.0:(0,.13,.42,.77),4.5:(0,.61,.72,.36),5.0:(0,.53,.27,.47),5.5:(0,.60,.18,.40)}
M={1.0:(.50,.08,.50,.92),1.5:(.20,.10,.38,.90),2.0:(.40,.05,.60,.95),2.5:(.64,.07,.36,.93),3.0:(.48,.10,.52,.90),
4.0:(.42,.22,.48,.66),4.5:(.55,.10,.45,.51),5.0:(.33,.10,.67,.90),5.5:(.50,.12,.32,.88),6.0:(.70,.13,.30,.87),6.5:(.60,.15,.40,.85),
7.0:(.57,.17,.43,.83),7.5:(.55,.18,.45,.82),8.0:(0,.12,1,.88),8.5:(0,.12,1,.88),9.0:(0,.13,1,.87),9.5:(0,.13,1,.87),10.0:(0,.08,1,.92)}
R={1.5:(.58,.13,.36,.84),2.5:(.33,.15,.31,.78),3.0:(.12,.17,.36,.83),5.5:(.82,.06,.18,.20),6.0:(.26,.10,.44,.84),6.5:(.13,.10,.47,.89),
7.0:(0,.13,.54,.87),7.5:(0,.13,.50,.87)}
c={"mediaId":4754,"level":"B","keyWord":"referee","defaultVoice":"female",
"taps":[
{"phrase":"to show a yellow card","target":"the referee","voice":"female","keys":keys(times,R)},
{"phrase":"to tumble onto the pitch","target":"the player in white","voice":"male","keys":keys(times,W)},
{"phrase":"to protest with open palms","target":"the stocky player in maroon","voice":"male","keys":keys(times,M)}],
"stillS":7.0,
"nouns":[{"word":"a yellow card","x":.42,"y":.20,"voice":"female"},{"word":"a referee","x":.24,"y":.47,"voice":"female"},
{"word":"a jersey","x":.80,"y":.42,"voice":"female"},{"word":"grass","x":.52,"y":.80,"voice":"female"}],
"question":"What is the referee showing the player?",
"answer":["She","is","showing","him","a","yellow","card."],
"answerVoice":"female",
"notes":"Many cuts. defaultVoice female: mixed group, evenId true. 'The player in white' = the fair-haired one in the foreground (a second white player stands far back at 0.5, not boxed); other maroon players in the background (0.0, 0.5, 3.5, 4.0, 5.0-6.0) are not the target and not boxed. Referee marked off at 2.0 (almost fully hidden behind the maroon player) and before 1.5; at 5.5 only her raised arm with the card shows behind him, so she has a small box top right and his box is narrowed to x<0.82. White player off at 6.0/6.5 (only a leg / hair at the edge). Overlaps split on straight lines: 1.0 and 4.0 (players tangled, vertical split), 4.5 (horizontal split at y 0.61, the maroon player's lower legs fall in the white player's box)."}
json.dump(c,open("content/4754.json","w"),indent=1,ensure_ascii=False)
