import json
T=[i*0.5 for i in range(25)]
W=[(0,.20,.49,.78),(0,.25,.55,.73),(0,.26,.44,.74),(0,.26,.44,.74),(0,.26,.42,.72),(0,.13,.52,.87),(0,.12,.50,.88),(0,.13,.49,.87),(0,.13,.47,.87),(0,.13,.47,.87),(0,.14,.46,.86),(0,.13,.46,.87),(0,.14,.47,.86),
(0,.47,.58,.53),(0,.40,.44,.60),(.05,.48,.45,.52),(0,.54,.52,.46),(0,.53,.57,.47),(0,.55,.67,.45),(0,.56,.72,.44),
(0,.15,.27,.85),(0,.22,.37,.78),(0,.25,.42,.75),(0,.26,.46,.74),(0,.24,.47,.76)]
C=[(.50,.09,.45,.77),(.56,.08,.42,.77),(.45,.08,.50,.89),(.45,.08,.52,.88),(.43,.06,.53,.78),(.53,0,.47,.95),(.51,0,.49,.97),(.50,0,.50,.97),(.48,0,.52,.92),(.48,0,.52,.92),(.47,0,.53,.97),(.47,0,.53,.97),(.48,0,.52,.97),
(.10,0,.90,.46),(.45,0,.55,1),(.10,0,.90,.47),(.08,0,.92,.53),(.05,0,.95,.52),(.05,0,.95,.54),(.15,0,.85,.55),
(.28,0,.72,.95),(.38,.02,.62,.95),(.43,.03,.57,.92),(.47,.03,.53,.92),(.48,0,.52,.90)]
def k(t,b): return {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
wk=[k(t,b) for t,b in zip(T,W)]
d={"mediaId":4478,"level":"A","keyWord":"date","defaultVoice":"female",
"taps":[
{"phrase":"to draw a red circle","target":"the woman","voice":"female","keys":wk},
{"phrase":"to hang on the wall","target":"the calendar","voice":"female","keys":[k(t,b) for t,b in zip(T,C)]},
{"phrase":"to point at a date","target":"the woman","voice":"female","keys":wk}],
"stillS":12.0,
"nouns":[{"word":"a window","x":.14,"y":.12,"voice":"female"},{"word":"a calendar","x":.72,"y":.28,"voice":"female"},{"word":"a woman","x":.24,"y":.45,"voice":"female"}],
"question":"What is the woman pointing at?",
"answer":["She","is","pointing","at","a","date","on","the","calendar."],
"answerVoice":"female",
"notes":"Only two targets (woman, calendar) and they overlap all the time: her arms and hands are in front of the calendar. Split: a vertical line at the left edge of the calendar in the wide shots, so her hand on the calendar falls into the calendar's box; in the close-ups 6.5-9.5 s only her hand and sleeve are in the picture, the woman's box is that hand (lower left) and the calendar's box the strip above it (at 7.0 the part right of the hand). 'to hang on the wall' is a state: the calendar does nothing else. Key word 'date' is in a phrase and the answer, not a noun pill, because its place is on the calendar and 'a calendar' would fit there too. Only 3 nouns: the pen is tiny and lies on the calendar, the sweater is on the woman. At 0-1 s she first turns a page of the calendar."}
json.dump(d,open("content/4478.json","w"),indent=1,ensure_ascii=False)
