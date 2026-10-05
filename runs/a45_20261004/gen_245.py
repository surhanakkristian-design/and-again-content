import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
woman={0.0:(0,.17,1,.83),0.5:(0,.10,1,.90),1.0:(0,.25,1,.75),1.5:(0,.20,1,.80),2.0:(0,.20,1,.80),2.5:(0,.15,1,.85),3.0:(0,.23,.90,.77),
5.5:(0,.29,.44,.71),6.0:(0,.33,.45,.45),6.5:(0,.16,.47,.50),7.0:(0,.19,.50,.58),7.5:(0,.26,.49,.54),8.0:(0,.28,.48,.50),
8.5:(0,.36,.50,.42),9.0:(0,.41,.51,.38),9.5:(0,.42,.53,.37),10.0:(0,.42,.48,.36)}
man={3.5:(.26,.12,.74,.88),4.0:(.07,.12,.93,.88),4.5:(.07,.10,.93,.90),5.0:(.28,.13,.72,.87),5.5:(.45,.20,.55,.80),6.0:(.46,.14,.54,.86),
6.5:(.48,0,.52,.74),7.0:(.52,.08,.48,.92),7.5:(.51,.12,.49,.88),8.0:(.56,.25,.44,.75),8.5:(.51,.31,.49,.69),9.0:(.52,.37,.48,.63),
9.5:(.54,.39,.46,.61),10.0:(.54,.38,.46,.62)}
animal={7.0:(.27,.77,.22,.16),7.5:(.27,.80,.22,.16),8.0:(.32,.79,.22,.15),8.5:(.32,.79,.18,.15),9.0:(.33,.80,.18,.14),9.5:(.36,.80,.18,.14),
10.0:(.36,.78,.18,.14)}
c={"mediaId":245,"level":"A","keyWord":"drinking","defaultVoice":"male",
"taps":[{"phrase":"to wash her hands","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to fill the bottle","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to sit on the rocks","target":"the small animal","voice":"male","keys":keys(animal)}],
"stillS":10.0,
"nouns":[{"word":"the sky","x":.50,"y":.08,"voice":"male"},{"word":"mountains","x":.50,"y":.25,"voice":"male"},
{"word":"a woman","x":.25,"y":.60,"voice":"female"},{"word":"a man","x":.76,"y":.55,"voice":"male"}],
"question":"What are the two people doing?","answer":["They","are","drinking","water","from","their","bottles."],"answerVoice":"male",
"notes":"Both people drink, so the tap phrases use what only one does: the woman holds her hands under the tap (5.5-6.5 s), the man holds the bottle under the tap (6.0-6.5 s). Third target is the marmot behind the railing (7.0-10.0 s), small; named 'the small animal' for level A. In the wide shots the woman's box stops above the marmot, so her lower legs are outside. At 3.0 s only the man's hands are in the picture (man off, woman's box covers them). defaultVoice male: mixed pair, odd id."}
json.dump(c,open("content/245.json","w"),indent=1)
