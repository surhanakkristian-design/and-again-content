import json
R=lambda t,x0,y0,x1,y1:{"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)}
O=lambda t:{"t":t,"off":True}
run=[R(0.0,.22,0,.77,.30),R(0.5,.18,0,.76,.36),R(1.0,.16,.18,.76,.68),R(1.5,.18,.20,.77,1),R(2.0,.02,.15,.72,1),
R(2.5,0,.18,.78,1),R(3.0,0,.06,1,1),R(3.5,.08,0,.81,1),R(4.0,0,0,.88,1),R(4.5,.02,0,.90,1),R(5.0,0,.02,.88,1),R(5.5,0,.03,.87,1),
R(6.0,0,.05,.88,1),R(6.5,0,.08,.87,1),R(7.0,.02,.15,.87,1),R(7.5,.02,.17,.86,1),R(8.0,0,.17,.87,1),R(8.5,0,.12,.84,1),
R(9.0,0,.17,.84,1),R(9.5,0,0,1,1),R(10.0,0,0,.81,1)]
old=[R(0.0,.78,.03,1,.30),R(0.5,.77,.08,1,.36),R(1.0,.77,.36,1,.68),R(1.5,.78,.38,1,.62),R(2.0,.73,.40,1,.64),R(2.5,.79,.35,1,1),
O(3.0),R(3.5,.82,.34,1,.56)]+[O(t/2) for t in range(8,17)]+[O(8.5),R(9.0,.85,.46,1,.72),O(9.5),R(10.0,.82,.46,1,1)]
d={"mediaId":473,"level":"A","keyWord":"medal","defaultVoice":"female",
"taps":[{"phrase":"to bite a gold medal","target":"the runner","voice":"female","keys":run},
{"phrase":"to put her arms up","target":"the runner","voice":"female","keys":run},
{"phrase":"to clap her hands","target":"the old woman","voice":"female","keys":old}],
"stillS":9.0,
"nouns":[{"word":"a medal","x":.50,"y":.60,"voice":"female"},{"word":"a tree","x":.74,"y":.11,"voice":"female"},
{"word":"flags","x":.20,"y":.50,"voice":"female"},{"word":"a watch","x":.81,"y":.80,"voice":"female"}],
"question":"What is the runner doing?","answer":["She","is","biting","a","gold","medal."],"answerVoice":"female",
"notes":"The old woman (grey hair, white shirt, behind on the right) is only clearly in the picture at 0-2.5 s, 3.5 s, 9.0 s and 10.0 s; she claps at 0-0.5, 2.5 and 10.0 s. In between only a sliver of her hair shows at the right edge (off). Flags hang on both sides; the pill sits on the left group."}
json.dump(d,open("content/473.json","w"),indent=1,ensure_ascii=False)
