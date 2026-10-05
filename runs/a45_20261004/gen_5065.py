import sys; sys.path.insert(0,'.')
from gen_5065_5066_5068_5070_lib import write
man={0.0:(.2,.32,.8,.68),0.5:(.08,.33,.92,.67),1.0:(.13,.31,.87,.69),1.5:(.1,.29,.9,.71),
 3.5:(0,.29,.8,.71),4.0:(0,.29,.72,.71),4.5:(0,.3,.72,.7),5.0:(.29,.53,.53,.47),5.5:(.28,.52,.52,.48),
 6.0:(.32,.48,.41,.52),6.5:(.31,.47,.38,.53),7.0:(.32,.44,.33,.56),7.5:(.26,.42,.41,.58),8.0:(.22,.41,.46,.59),
 8.5:(.19,.4,.56,.6),9.0:(.16,.39,.71,.61)}
scale={2.5:(0,.36,.5,.64),3.0:(.08,.27,.53,.73)}
write(5065,{"mediaId":5065,"level":"B","keyWord":"aisle","defaultVoice":"male",
"taps":[
 {"phrase":"to sample a green olive","target":"the young man","voice":"male","box":dict(man)},
 {"phrase":"to stroll down the aisle","target":"the young man","voice":"male","box":dict(man)},
 {"phrase":"to dangle from metal chains","target":"the scale","voice":"male","box":scale}],
"stillS":7.0,
"nouns":[{"word":"a ceiling","x":0.5,"y":0.15,"voice":"male"},{"word":"an aisle","x":0.5,"y":0.41,"voice":"male"},
 {"word":"spices","x":0.15,"y":0.63,"voice":"male"},{"word":"a mesh bag","x":0.3,"y":0.75,"voice":"male"}],
"question":"Where is the young man walking?",
"answer":["He","is","strolling","down","a","long","aisle."],
"answerVoice":"male",
"notes":"Cuts: selfie at the fruit stall 0-1.5, fish stall 2.0-3.0 (young man off), olive barrel 3.5-4.5, spice bazaar 5.0-9.0. The scale (two pans on chains) only at 2.5-3.0. Two fishmongers appear (bald at 2.0, bearded at 2.5-3.0), so no phrase for them. Two taps share the young man."})
