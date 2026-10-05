from gen_7986_7987_7988_7989_lib import *
lil=keys([(.05,.36,.42,.40),(.01,.36,.46,.40),(.00,.37,.46,.39),(.00,.37,.44,.39),(.00,.35,.46,.38),(.00,.33,.43,.44),None,(.00,.27,.50,.51)])
dog=keys([(.57,.59,.36,.21),(.57,.59,.37,.21),(.57,.59,.37,.21),(.57,.61,.40,.20),(.72,.63,.26,.17),(.62,.62,.37,.21),(.55,.61,.43,.23),(.51,.60,.47,.24)])
cor=keys([(.59,.33,.18,.25),(.58,.31,.18,.27),(.49,.29,.21,.29),(.46,.27,.30,.33),None,(.44,.13,.48,.48),None,None])
write(7986,{"mediaId":7986,"level":"B","keyWord":"slower","defaultVoice":"female",
"taps":[
 {"phrase":"to tug hard on the lead","target":"the woman in lilac","voice":"female","keys":lil},
 {"phrase":"to refuse to budge","target":"the bulldog","voice":"female","keys":dog},
 {"phrase":"to leap over the lead","target":"the woman in coral","voice":"female","keys":cor}],
"stillS":0.7,
"nouns":[{"word":"a bulldog","x":0.78,"y":0.70,"voice":"female"},
 {"word":"a lead","x":0.53,"y":0.58,"voice":"female"},
 {"word":"a stone bridge","x":0.14,"y":0.36,"voice":"female"},
 {"word":"a lamp post","x":0.62,"y":0.27,"voice":"female"}],
"question":"What is the woman in lilac doing?",
"answer":["She","is","tugging","hard","on","the","lead."],
"answerVoice":"female",
"notes":"Coral woman at 0.2 is a small far runner; she is hidden at 2.2 (behind the man in the navy vest) and gone at 3.2/3.7 -> off. Lilac woman hidden behind the white-shirt runner at 3.2 -> off. 'leap over the lead' = the coral woman jumps over the stretched lead at 2.7."})
