import json
T=[i/2 for i in range(21)]
M={0.0:(0,.37,.52,.47),0.5:(0,.34,.50,.48),1.0:(0,.22,.42,.60),1.5:(.05,.18,.28,.63),2.0:(.03,.19,.32,.63),2.5:(0,.23,.44,.59),
3.0:(0,.33,.50,.50),3.5:(0,.35,.50,.47),4.0:(0,.35,.51,.47),4.5:(0,.35,.51,.47),5.0:(0,.34,.50,.47),5.5:(0,.38,.40,.43),
6.0:(.04,.34,.40,.46),6.5:(0,.37,.50,.43),7.0:(0,.44,.52,.37),7.5:(0,.49,.53,.33),8.0:(0,.49,.50,.32),8.5:(0,.47,.50,.33),
9.0:(0,.44,.51,.36),9.5:(0,.41,.52,.37),10.0:(0,.37,.50,.38)}
W={0.0:(.53,.38,.47,.24),0.5:(.60,.33,.40,.29),1.0:(.68,.30,.32,.32),1.5:(.69,.30,.31,.32),2.0:(.69,.30,.31,.32),2.5:(.66,.30,.34,.32),
3.0:(.57,.34,.43,.30),3.5:(.53,.36,.47,.42),4.0:(.53,.37,.47,.43),4.5:(.53,.36,.47,.44),5.0:(.53,.37,.47,.44),5.5:(.55,.37,.45,.42),
6.0:(.62,.40,.38,.38),6.5:(.56,.38,.44,.42),7.0:(.52,.44,.48,.37),7.5:(.53,.49,.47,.33),8.0:(.50,.48,.50,.33),8.5:(.50,.46,.50,.34),
9.0:(.51,.43,.49,.37),9.5:(.52,.40,.48,.39),10.0:(.50,.35,.50,.40)}
F={0.0:(.58,.62,.42,.38),0.5:(.60,.62,.40,.38),1.0:(.58,.62,.42,.38),1.5:(.60,.62,.40,.38),2.0:(.60,.62,.40,.38),2.5:(.62,.62,.38,.38),
3.0:(.66,.64,.34,.36),3.5:(.70,.80,.30,.20)}
def keys(d): return [({"t":t,"off":True} if t not in d else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3])) for t in T]
c={"mediaId":4427,"level":"B","keyWord":"ceremony","defaultVoice":"male",
"taps":[{"phrase":"to kneel before the woman","target":"the tall man","voice":"male","keys":keys(M)},
{"phrase":"to bow to the tall man","target":"the woman in the kimono","voice":"female","keys":keys(W)},
{"phrase":"to film the ceremony","target":"the person with the phone","voice":"male","keys":keys(F)}],
"stillS":2.0,
"nouns":[{"word":"a lantern","x":.50,"y":.08,"voice":"male"},{"word":"a scroll","x":.55,"y":.33,"voice":"male"},
{"word":"a kimono","x":.78,"y":.57,"voice":"male"},{"word":"a suit","x":.20,"y":.47,"voice":"male"}],
"question":"What are the man and woman doing?","answer":["They","are","bowing","to","each","other."],"answerVoice":"male",
"notes":"defaultVoice male: two main people (man + woman), evenId false. Third target = the arm / hand holding up a phone in the bottom right corner, visible as filming only 0.0-3.5 s (off afterwards: only a sleeve edge, no phone). That arm overlaps the woman's legs in the picture: 0.0-3.0 s the boxes are split by a horizontal line at y .62-.64 (woman = head and upper body above, filming arm below; her lower legs fall in the arm's box); at 3.5 s the arm box is only the sleeve below y .80. From 7.0 s the two heads touch: split on the vertical line between them. The guests along the walls also kneel and wear suits, but only the tall man kneels before the woman; 'a suit' pill sits clearly on the tall man. The white sheet on the floor (certificate with calligraphy) left out of the nouns: what it is needs guessing."}
json.dump(c,open('content/4427.json','w'),indent=1)
