from gen_7891_7892_7893_7894_lib import *
wom=keys([(.30,.35,.53,.97),(.29,.34,.53,.98),(.28,.34,.53,.99),(.29,.33,.53,1),(.29,.32,.54,.99),(.29,.32,.54,.99),(.27,.31,.54,.99),(.27,.31,.54,1)])
man=keys([(.53,.32,.67,.95),(.53,.31,.67,.96),(.53,.30,.645,1),(.53,.29,.655,1),(.54,.29,.66,1),(.54,.29,.66,1),(.54,.28,.665,1),(.54,.27,.67,1)])
cat=keys([(.67,.77,.86,.91),(.67,.76,.86,.91),(.645,.73,.88,.93),(.655,.69,.88,.91),(.66,.71,.89,.91),(.66,.71,.88,.91),(.665,.71,.92,.91),(.67,.71,.93,.93)])
write({"mediaId":7893,"level":"B","keyWord":"live together","defaultVoice":"male",
"taps":[{"phrase":"to take a mirror selfie","target":"the woman","voice":"female","keys":wom},
{"phrase":"to hug her from behind","target":"the man","voice":"male","keys":man},
{"phrase":"to wander across the floor","target":"the cat","voice":"male","keys":cat}],
"stillS":2.2,
"nouns":[{"word":"a pendant lamp","x":0.19,"y":0.21,"voice":"male"},{"word":"cardboard boxes","x":0.23,"y":0.66,"voice":"male"},
{"word":"a bicycle","x":0.71,"y":0.68,"voice":"male"},{"word":"a cat","x":0.76,"y":0.85,"voice":"male"}],
"question":"What is the couple doing?","answer":["They","are","taking","a","mirror","selfie","together."],"answerVoice":"male",
"notes":"Man stands right behind the woman: boxes split vertically at x~0.53-0.54, so his head is only partly inside his box (left half of his face lies in the woman's box) and her right elbow is cut. Man and cat boxes split at x~0.65-0.67 where his feet are next to the cat. defaultVoice male: mixed couple, evenId false."})
