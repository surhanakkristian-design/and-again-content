import json
T=[i/2 for i in range(21)]
W={0.0:(.12,.28,.76,.72),0.5:(.17,.28,.70,.72),1.0:(.15,.30,.65,.70),1.5:(.15,.30,.65,.70),2.0:(.05,.30,.57,.70),2.5:(0,.32,.41,.68),
3.0:(0,.36,.36,.64),3.5:(0,.37,.34,.63),4.0:(0,.37,.33,.63),4.5:(0,.47,.36,.53),5.0:(0,.42,.34,.58),5.5:(0,.42,.32,.58),
6.0:(.03,.43,.30,.55),6.5:(.07,.43,.29,.55),7.0:(0,.34,.40,.66),7.5:(0,.34,.40,.66),8.0:(0,.36,.39,.60),8.5:(0,.36,.39,.60),
9.0:(0,.45,.37,.55),9.5:(.05,.46,.31,.54),10.0:(0,.50,.36,.47)}
M={2.0:(.62,.22,.38,.78),2.5:(.41,.19,.59,.81),3.0:(.36,.21,.64,.79),3.5:(.34,.23,.66,.77),4.0:(.33,.22,.67,.78),4.5:(.36,.26,.52,.74),
5.0:(.34,.35,.42,.65),5.5:(.32,.36,.37,.64),6.0:(.33,.36,.35,.62),6.5:(.36,.36,.34,.60),7.0:(.40,.38,.27,.62),7.5:(.40,.39,.27,.59),
8.0:(.39,.39,.27,.56),8.5:(.39,.39,.27,.56),9.0:(.37,.40,.30,.60),9.5:(.36,.40,.32,.60),10.0:(.36,.40,.31,.54)}
H={4.5:(.88,.33,.12,.67),5.0:(.76,.37,.24,.63),5.5:(.69,.36,.31,.64),6.0:(.68,.36,.32,.64),6.5:(.70,.36,.30,.62),7.0:(.67,.37,.33,.63),
7.5:(.67,.38,.33,.62),8.0:(.66,.38,.34,.60),8.5:(.66,.38,.34,.60),9.0:(.67,.40,.33,.60),9.5:(.68,.45,.32,.55),10.0:(.67,.41,.33,.56)}
def keys(d): return [({"t":t,"off":True} if t not in d else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3])) for t in T]
c={"mediaId":5272,"level":"B","keyWord":"hiker","defaultVoice":"female",
"taps":[{"phrase":"to point at her companion","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to have a bushy beard","target":"the bearded man","voice":"male","keys":keys(M)},
{"phrase":"to wear a wide-brimmed hat","target":"the man in the hat","voice":"male","keys":keys(H)}],
"stillS":6.0,
"nouns":[{"word":"a hiker","x":.20,"y":.62,"voice":"female"},{"word":"a beard","x":.48,"y":.46,"voice":"female"},
{"word":"a canyon","x":.50,"y":.33,"voice":"female"},{"word":"a railing","x":.86,"y":.79,"voice":"female"}],
"question":"What are the hikers doing?","answer":["The","hikers","are","cheering","above","the","canyon."],"answerVoice":"female",
"notes":"All three shout / raise their arms, so the two men's phrases are states that fit only one person (beard, hat); the woman's phrase is her pointing at 3.0-4.0 s. Boxes are split on vertical lines between the people; the woman's raised right hand (7.0-8.5 s) and her outstretched hand at 9.0 s cross into the bearded man's column and are cut. 4.5 s: the man in the hat is only a narrow strip at the right edge. 'a hiker' pill sits on the woman; the other two hikers carry no person noun (a beard is on the bearded man's face). 'a railing' pill is on the rail at the right edge, close to the hat man's leg."}
json.dump(c,open('content/5272.json','w'),indent=1)
