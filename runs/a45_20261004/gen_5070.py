import sys; sys.path.insert(0,'.')
from gen_5065_5066_5068_5070_lib import write
w={0.0:(.17,.05,.73,.95),0.5:(.22,.3,.63,.7),1.0:(.22,.3,.62,.7),1.5:(.22,.3,.62,.7),2.0:(.21,.28,.62,.72),2.5:(.24,.11,.65,.89),
 3.0:(.26,.25,.63,.75),3.5:(.29,.36,.56,.64),4.0:(.29,.27,.56,.73),4.5:(.29,.28,.58,.72),5.0:(.26,.28,.62,.72),5.5:(.25,.28,.63,.72),
 6.0:(.25,.27,.63,.73),6.5:(0,.15,1,.85),7.0:(.05,.27,.9,.73),7.5:(.14,.34,.71,.24),8.0:(.15,.38,.64,.3),8.5:(.14,.38,.71,.31),
 9.0:(.15,.39,.62,.3),9.5:(.14,.37,.66,.32),10.0:(.14,.35,.69,.36),10.5:(.14,.35,.71,.37),11.0:(.14,.35,.71,.39),
 11.5:(.14,.35,.72,.4),12.0:(.14,.34,.73,.41)}
write(5070,{"mediaId":5070,"level":"B","keyWord":"mattress","defaultVoice":"female",
"taps":[
 {"phrase":"to perch on the edge","target":"the woman","voice":"female","box":dict(w)},
 {"phrase":"to pull a pained face","target":"the woman","voice":"female","box":dict(w)},
 {"phrase":"to sprawl across the mattress","target":"the woman","voice":"female","box":dict(w)}],
"stillS":10.0,
"nouns":[{"word":"windows","x":0.7,"y":0.07,"voice":"female"},{"word":"a headboard","x":0.82,"y":0.22,"voice":"female"},
 {"word":"a woman","x":0.52,"y":0.45,"voice":"female"},{"word":"a mattress","x":0.8,"y":0.63,"voice":"female"}],
"question":"Where is the woman lying?",
"answer":["She","is","lying","across","a","huge","mattress."],
"answerVoice":"female",
"notes":"Only one person, so all three taps use the woman (no other clear single target; many identical beds and pillows). Pained face = 1.5-2.0; perched on the edge = 0.5-2.0 and 4.0-6.0; sprawled with arms and legs spread = 8.0-12.0. At 6.5 her arms reach both picture edges, box is the full width."})
