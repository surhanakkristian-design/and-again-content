from mk_7214_7215_7216_7219 import write
W=[(.31,.31,.31,.54),(.30,.31,.34,.56),(.28,.30,.38,.60),(.19,.29,.51,.67),(.07,.28,.61,.72),(.02,.28,.64,.72),(0,.28,.64,.72),(0,.27,.71,.73)]
D=[(.62,.63,.24,.14),(.64,.64,.22,.14),(.66,.64,.24,.14),(.70,.67,.24,.15),(.68,.68,.32,.18),(.66,.70,.34,.18),(.64,.76,.36,.16),(.71,.79,.29,.18)]
write(7214,"B","heat wave","female",[
 ("to throw her arms wide","the woman","female",W),
 ("to stand barefoot on cobblestones","the woman","female",W),
 ("to roll onto its back","the dog","female",D)],
 0.2,[("a double-decker bus",.35,.20,"female"),("a pencil skirt",.47,.60,"female"),("a dog",.72,.70,"female"),("cobblestones",.30,.90,"female")],
 "What is the barefoot woman doing?","She is throwing her arms wide.","female",
 "Woman boxes cut at the dog's edge where her shoe hand reaches it (2.2-3.7). Dog rolls onto its back mainly at 2.2-2.7.")
