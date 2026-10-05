import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [({"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3])) for t in T]
def mk(i,c): json.dump(c,open('content/%d.json'%i,'w'),indent=1)
M={2.5:(0,0,.69,.58),3.0:(0,0,.67,.66),3.5:(0,0,.69,.60),4.0:(0,0,.67,.56)}
W={2.5:(.70,.03,.30,.50),3.0:(.68,.14,.32,.50),3.5:(.70,.03,.30,.52),4.0:(.68,0,.32,.52),
   4.5:(.58,0,.42,.43),5.0:(.58,0,.42,.46),5.5:(.62,0,.38,.41)}
C={4.5:(.15,.44,.50,.28),5.0:(.17,.48,.50,.41),5.5:(.16,.43,.57,.42),6.0:(.16,.36,.62,.36),6.5:(.29,.16,.66,.40),
   7.0:(.18,.36,.64,.50),7.5:(.16,.34,.71,.52),8.0:(.09,.36,.74,.41),8.5:(.16,.11,.70,.38),9.0:(.39,.43,.61,.55)}
mk(352,{"mediaId":352,"level":"A","keyWord":"grill","defaultVoice":"male",
 "taps":[{"phrase":"to hold out his hand","target":"the man","voice":"male","keys":keys(M)},
  {"phrase":"to hold a plate","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to have dark stripes","target":"the cheese","voice":"male","keys":keys(C)}],
 "stillS":10.0,
 "nouns":[{"word":"flowers","x":.30,"y":.12,"voice":"male"},{"word":"a table","x":.18,"y":.25,"voice":"male"},
  {"word":"a candle","x":.62,"y":.35,"voice":"male"},{"word":"a grill","x":.40,"y":.52,"voice":"male"}],
 "question":"Where is the cheese?","answer":["The","cheese","is","on","the","grill."],"answerVoice":"male",
 "notes":"Man and woman are only clearly shown 2.5-4.0 (woman's body with raised finger also 4.5-5.5). Later only a blurred arm (6.0-8.0) and an apron torso with tongs (8.5-9.0) are in the picture: set off. Cheese phrase is a state; stripes are visible from 6.5, the box follows the cheese from 4.5. 'a candle' pill sits on the candle inside the lantern. The cheese is on the grill 4.5-8.0, on a plate at 8.5-9.0."})
