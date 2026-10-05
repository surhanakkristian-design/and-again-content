import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
woman={0.0:(0,.54,.46,.46),0.5:(0,.58,.52,.42),1.0:(0,.58,.52,.42),1.5:(0,.68,.40,.32),2.0:(0,.64,.18,.20),
3.5:(0,.22,.62,.56),4.0:(0,.24,.70,.50),4.5:(0,0,.52,1),5.0:(0,.03,.47,.97),5.5:(0,.10,.42,.90),6.0:(0,.16,.36,.60),
6.5:(0,.18,.40,.56),7.0:(0,.29,.40,.55),9.0:(0,.10,.55,.90),9.5:(0,.14,.54,.86),10.0:(0,.21,.56,.79)}
man={0.5:(.53,.41,.47,.24),1.0:(.53,.12,.47,.74),1.5:(.54,.04,.46,.70),2.0:(.44,0,.56,.60),2.5:(.46,0,.54,.38),3.0:(.48,0,.52,.36),
3.5:(.72,.18,.28,.42),4.0:(.80,.22,.20,.28),5.0:(.50,.21,.50,.42),5.5:(.46,.18,.54,.44),6.0:(.58,.20,.42,.32),6.5:(.58,.21,.42,.33),
7.0:(.62,.26,.38,.42),7.5:(.52,.02,.48,.62),8.0:(.50,.05,.50,.60),8.5:(.52,.08,.48,.40),9.0:(.57,.18,.43,.44),9.5:(.58,.21,.42,.42),10.0:(.60,.22,.40,.34)}
c={"mediaId":283,"level":"B","keyWord":"fabric","defaultVoice":"female",
"taps":[
 {"phrase":"to unroll the patterned cloth","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to cut with large scissors","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to hug the folded fabric","target":"the woman","voice":"female","keys":keys(woman)}],
"stillS":10.0,
"nouns":[{"word":"an earring","x":.20,"y":.42,"voice":"female"},{"word":"fabric","x":.33,"y":.68,"voice":"female"},
 {"word":"a table","x":.70,"y":.59,"voice":"female"},{"word":"a tape measure","x":.80,"y":.80,"voice":"female"}],
"question":"What is the man doing?",
"answer":["He","is","cutting","the","fabric","with","scissors."],
"answerVoice":"male",
"notes":"Only two people (a hen is visible for a moment at 9.5, too small). The man has two phrases. Woman's box at 0.0-2.0 and 3.5-4.0 is only her hand (the clip is filmed from her side); verifier may prefer 'off' there. At 9.0 her right hand with the fabric reaches a little beyond her box (kept clear of the man). 'fabric' pill is on her folded piece; the shelves are also full of fabric but no other slot lies on cloth. The white band over the table edge is the tape measure he measured with (clear at 7.0-8.5); two more white straps hang from the roof."}
json.dump(c,open('content/283.json','w'),indent=1)
