import json
T=[i/2 for i in range(21)]
M={1.0:(0,0,1,.16),1.5:(0,0,1,.27),2.0:(0,0,1,.36),2.5:(0,0,1,.38),3.0:(0,0,1,.34),3.5:(0,0,1,.34),4.0:(0,0,1,.31),4.5:(0,0,1,.29),
5.0:(0,0,1,.29),5.5:(0,0,1,.29),6.0:(0,0,1,.27),6.5:(.52,0,.48,.45),7.0:(.52,0,.48,.42),7.5:(.52,0,.48,.42),8.0:(.56,0,.44,.42),
8.5:(0,0,.60,.80),9.0:(0,.07,.85,.51),9.5:(0,.02,.59,.80),10.0:(0,.02,.61,.75)}
B={0.0:(.03,.03,.94,.97),0.5:(.03,.03,.94,.97),1.0:(.12,.16,.78,.84),1.5:(.18,.27,.67,.73),2.0:(.22,.36,.58,.64),2.5:(.27,.38,.53,.62),
3.0:(.25,.34,.50,.66),3.5:(.34,.34,.50,.66),4.0:(.30,.31,.48,.66),4.5:(.30,.29,.52,.68),5.0:(.27,.29,.50,.71),5.5:(.30,.29,.50,.71),
6.0:(.30,.27,.50,.72),6.5:(0,0,.52,.42),7.0:(0,0,.52,.40),7.5:(0,0,.52,.40),8.0:(0,0,.56,.40),
8.5:(.60,.47,.40,.53),9.0:(.57,.59,.43,.41),9.5:(.59,.49,.41,.51),10.0:(.61,.47,.39,.53)}
def keys(d): return [({"t":t,"off":True} if t not in d else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3])) for t in T]
c={"mediaId":4408,"level":"B","keyWord":"taste","defaultVoice":"male",
"taps":[{"phrase":"to gulp down a smoothie","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to give a thumbs up","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to blend fruit and spinach","target":"the blender","voice":"male","keys":keys(B)}],
"stillS":10.0,
"nouns":[{"word":"a blender","x":.82,"y":.90,"voice":"male"},{"word":"spinach","x":.50,"y":.81,"voice":"male"},
{"word":"a smoothie","x":.32,"y":.56,"voice":"male"},{"word":"a moustache","x":.47,"y":.24,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","tasting","a","fresh","fruit","smoothie."],"answerVoice":"male",
"notes":"Two targets only (the glass sits in front of the man's face/body when it matters). The blender stands in front of the man for most of the clip: the man's box is the strip above the blender (head, hands), the blender's box below; his arms/torso beside the blender are in neither. 0.0-0.5 s: only the jug with his vest behind it, man set off. 6.5-8.0 s (pouring close-up): the blender box is the tilted jug at the top left, the man is the right part. 8.5, 9.5, 10.0 s: vertical split, his right shoulder / thumb is cut. Key word 'taste' is a noun in the packet; the answer uses the verb 'tasting'. 'a smoothie' pill is on the glass, 'a blender' on the black base (the jug also holds smoothie). 'a moustache' = the smoothie moustache."}
json.dump(c,open('content/4408.json','w'),indent=1)
