import json
T=[i*0.5 for i in range(21)]
C=[(.50,.77),(.51,.77),(.49,.765),(.50,.77),(.47,.775),(.49,.775),(.46,.785),(.50,.775),(.49,.76),(.50,.755),(.50,.76),(.50,.745),(.49,.75),(.50,.75),(.48,.765),(.50,.765),(.49,.76),(.50,.77),(.50,.78),(.52,.79),(.53,.79)]
TOP=[0,.01,0,.04,.02,.03,.02,.04,.04,.06,.06,.03,.02,.04,0,.04,0,0,0,.03,.01]
r=lambda v: round(v,2)
wk=[];sk=[]
for t,(cx,cy),top in zip(T,C,TOP):
    st=r(cy-.06)
    sk.append({"t":t,"x":r(cx-.11),"y":st,"w":.22,"h":.14})
    wk.append({"t":t,"x":0,"y":top,"w":1,"h":r(st-.01-top)})
d={"mediaId":4479,"level":"A","keyWord":"hard","defaultVoice":"female",
"taps":[
{"phrase":"to touch her head","target":"the woman","voice":"female","keys":wk},
{"phrase":"to show blue numbers","target":"the screen","voice":"female","keys":sk},
{"phrase":"to point at the screen","target":"the woman","voice":"female","keys":wk}],
"stillS":4.5,
"nouns":[{"word":"a woman","x":.50,"y":.28,"voice":"female"},{"word":"a screen","x":.50,"y":.76,"voice":"female"},{"word":"a bike","x":.50,"y":.92,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","working","hard","on","her","bike."],
"answerVoice":"female",
"notes":"One shot. The riders behind her also ride bikes, so no phrase about riding; the woman's two phrases are things only she does (hand on her head at 8.5-9.0 s, finger on the screen at 10.0 s, also 2.0-2.5 s). Second target = the small blue screen on the handlebars. Split: the woman's box ends just above the screen, so her hands on the grips and her legs below the handlebars fall outside it; the box is full width for her arms and takes in the small riders behind her (they are no targets). Key word 'hard' is an adjective; the answer uses it as an adverb ('working hard'), please check that this is acceptable. Only 3 nouns: the towel lies too close to the screen for two pills, hands come in pairs. 'a bike' pill sits on the bike's frame under the handlebars; the screen is part of the bike too."}
json.dump(d,open("content/4479.json","w"),indent=1,ensure_ascii=False)
