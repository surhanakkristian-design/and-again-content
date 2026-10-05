import json
W={0.0:(.00,.43,.64,.38),0.5:(.00,.43,.64,.38),1.0:(.00,.43,.62,.38),1.5:(.00,.43,.64,.38),2.0:(.00,.43,.64,.38),2.5:(.00,.43,.64,.38),
3.0:(.00,.42,.64,.39),3.5:(.00,.42,.64,.39),4.0:(.00,.41,.62,.38),4.5:(.00,.40,.64,.38),5.0:(.00,.40,.64,.39),5.5:(.00,.42,.64,.38),
6.0:(.00,.42,.64,.38),6.5:(.00,.43,.64,.38),7.0:(.00,.43,.64,.38),7.5:(.00,.43,.64,.38),8.0:(.00,.41,.66,.38),8.5:(.00,.40,.75,.40),
9.0:(.00,.37,.75,.44),9.5:(.00,.39,.80,.59),10.0:(.00,.26,.55,.74)}
ts=[i*0.5 for i in range(21)]
C={t:(.00,.00,1.0,.11) for t in ts}; C[9.5]=(.00,.00,1.0,.16); C[10.0]=(.00,.08,1.0,.17)
f=lambda D:[dict(t=t,x=D[t][0],y=D[t][1],w=D[t][2],h=D[t][3]) for t in ts]
wk,ck=f(W),f(C)
d={"mediaId":5268,"level":"B","keyWord":"rifle","defaultVoice":"female",
"taps":[{"phrase":"to aim at the targets","target":"the woman","voice":"female","keys":wk},
{"phrase":"to watch from behind barriers","target":"the crowd","voice":"female","keys":ck},
{"phrase":"to break into a grin","target":"the woman","voice":"female","keys":wk}],
"stillS":2.0,
"nouns":[{"word":"spectators","x":.50,"y":.05,"voice":"female"},{"word":"targets","x":.50,"y":.31,"voice":"female"},
{"word":"a headband","x":.32,"y":.52,"voice":"female"},{"word":"a rifle","x":.58,"y":.60,"voice":"female"}],
"question":"What is the athlete aiming at?",
"answer":["She","is","aiming","her","rifle","at","the","targets."],
"answerVoice":"female",
"notes":"Crowd is a thin strip at the top (y 0-.10) until 9.5. Grin at 8.0-10.0. 'spectators' pill sits at the top edge on the crowd strip."}
json.dump(d,open('content/5268.json','w'),indent=1)
