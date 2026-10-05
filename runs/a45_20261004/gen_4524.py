import json
def keys(d, times):
    return [dict(t=t, x=d[t][0], y=d[t][1], w=d[t][2], h=d[t][3]) if d.get(t) else dict(t=t, off=True) for t in times]
times=[i*0.5 for i in range(25)]
W={0.0:(0,0,1,.50),0.5:(0,0,1,.50),1.0:(0,0,1,.50),1.5:(0,0,1,.50),2.0:(0,0,1,.58),2.5:(0,0,1,.57),3.0:(0,0,1,.52),3.5:(0,0,1,.62),
4.0:(.05,0,.88,.64),4.5:(.10,0,.78,.66),5.0:(.13,.09,.72,.61),5.5:(.13,.12,.72,.59),6.0:(.15,.14,.67,.54),6.5:(.16,.16,.66,.52),
7.0:(.17,.17,.63,.50),7.5:(.18,.17,.64,.50),8.0:(.28,.17,.54,.31),8.5:(.42,.15,.31,.14),9.0:(.20,.26,.60,.30),9.5:(.20,.15,.60,.41),
10.0:(.20,.13,.62,.41),10.5:(.20,.11,.62,.44),11.0:(.10,.06,.76,.50),11.5:(.08,.06,.87,.51),12.0:(.10,.03,.78,.54)}
S={8.0:(.03,.48,.94,.52),8.5:(0,.29,1,.71),9.0:(.02,.56,.96,.44),9.5:(0,.56,1,.44),10.0:(0,.54,1,.46),10.5:(0,.55,1,.45),11.0:(0,.56,1,.44),11.5:(0,.57,1,.43),12.0:(0,.57,1,.43)}
L={5.0:(.31,0,.38,.09),5.5:(.30,0,.40,.11),6.0:(.31,0,.38,.13),6.5:(.31,0,.39,.15),7.0:(.31,0,.38,.14),7.5:(.31,0,.38,.14),8.0:(.32,0,.38,.13),8.5:(.32,0,.38,.13),9.5:(.33,0,.36,.13),10.0:(.32,0,.36,.12),10.5:(.32,0,.36,.10)}
c={"mediaId":4524,"level":"B","keyWord":"fold","defaultVoice":"female",
"taps":[
 {"phrase":"to arrange dumplings in rows","target":"the older woman","voice":"female","keys":keys(W,times)},
 {"phrase":"to release clouds of steam","target":"the bamboo steamer","voice":"female","keys":keys(S,times)},
 {"phrase":"to glow above the family","target":"the paper lantern","voice":"female","keys":keys(L,times)}],
"stillS":7.0,
"nouns":[{"word":"a lantern","x":.50,"y":.07,"voice":"female"},{"word":"a cardigan","x":.33,"y":.50,"voice":"female"},
 {"word":"dumplings","x":.50,"y":.77,"voice":"female"},{"word":"a handle","x":.50,"y":.87,"voice":"female"}],
"question":"What is the older woman doing?",
"answer":["She","is","folding","dumplings","and","arranging","them","in","rows."],
"answerVoice":"female",
"notes":"Lantern is only a sliver at 4.5 and 11.0 and hidden by steam at 9.0: off there. At 5.0-5.5 the lantern box is thinner than 0.14 so it does not overlap the woman's hair. At 8.5 the woman is mostly hidden behind the lifted lid; small box on her hair. The lid is lifted by an arm in a red sleeve (looks like the older woman's, not the man's), so no phrase about lifting the lid. Children also hold dumplings, so 'fold' is used only in the answer, not as a tap phrase."}
json.dump(c,open('content/4524.json','w'),indent=1,ensure_ascii=False)
