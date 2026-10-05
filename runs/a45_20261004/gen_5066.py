import sys; sys.path.insert(0,'.')
from gen_5065_5066_5068_5070_lib import write
man={0.0:(0,.14,.6,.86),0.5:(0,.15,.64,.85),1.0:(0,.18,.68,.82),1.5:(0,.17,.69,.83),2.0:(0,.22,.75,.78),2.5:(0,.22,.75,.78),
 3.0:(0,.1,.24,.82),3.5:(0,.15,.38,.5),4.0:(0,.08,.63,.92),4.5:(0,.12,.84,.88),5.0:(0,.15,.72,.85),5.5:(0,.17,.84,.83),
 6.0:(0,.24,.82,.76),6.5:(0,.26,.68,.74),7.0:(0,.2,.52,.8),7.5:(0,.22,.47,.78),8.0:(0,.24,.44,.74),8.5:(0,.19,.5,.81),
 9.0:(0,.25,.86,.75),9.5:(0,.11,.98,.89),10.0:(0,.11,.9,.89)}
fruit={0.0:(.61,.3,.37,.26),0.5:(.66,.32,.33,.28),1.0:(.7,.35,.3,.27),1.5:(.7,.35,.3,.26),2.0:(.76,.36,.24,.24),2.5:(.76,.36,.24,.24)}
olive={3.0:(.55,.28,.45,.35),3.5:(.53,.2,.47,.4),4.0:(.64,.24,.36,.33),4.5:(.85,.33,.15,.33),5.0:(.82,.38,.18,.34),
 6.0:(.82,.46,.18,.24),6.5:(.7,.41,.3,.21)}
write(5066,{"mediaId":5066,"level":"A","keyWord":"sample","defaultVoice":"male",
"taps":[
 {"phrase":"to eat an olive","target":"the young man","voice":"male","box":man},
 {"phrase":"to wear a blue apron","target":"the fruit seller","voice":"male","box":fruit},
 {"phrase":"to hold a big spoon","target":"the olive seller","voice":"male","box":olive}],
"stillS":2.0,
"nouns":[{"word":"the sky","x":0.5,"y":0.1,"voice":"male"},{"word":"a mosque","x":0.82,"y":0.32,"voice":"male"},
 {"word":"oranges","x":0.88,"y":0.75,"voice":"male"},{"word":"a bag","x":0.52,"y":0.9,"voice":"male"}],
"question":"What is the young man eating?",
"answer":["He","is","eating","a","green","olive."],
"answerVoice":"male",
"notes":"Selfie clip with cuts: fruit stand 0-2.5, olive stall 3.0-6.5, spice bazaar 7.0-10.0. Young man only a hand/hair sliver at 3.0-3.5. At 2.0-2.5 his orange hand reaches into the fruit seller's area: split at x 0.76. Olive seller (white clothes, ladle) is only an arm with the ladle at the right edge 4.5-6.0, off at 5.5; a second worker in a white cap stands in the background. Key word 'sample' is abstract, no noun pill."})
