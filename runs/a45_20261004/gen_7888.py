from lib_7884_7887_7888_7889 import build
M = [(.37,.21,.63,.26),(.37,.21,.63,.24),(.36,.22,.64,.25),(.36,.21,.64,.26),(.35,.21,.65,.26),(.34,.19,.66,.28),(.34,.18,.66,.34),(.34,.17,.66,.35)]
T = [(.03,.49,.52,.15),(.44,.45,.26,.13),None,None,None,None,None,None]
HD = [(.42,.65,.58,.35),(.42,.59,.58,.41),(.46,.48,.54,.52),(.46,.48,.54,.52),(.45,.48,.55,.52),(.44,.48,.56,.52),(.37,.66,.63,.34),(.37,.66,.63,.34)]
build(7888,'B','layout','male',[
 ('to lean across the table','the man','male',M),
 ('to cross a stone viaduct','the red train','male',T),
 ('to place a miniature fir tree','the hands in lilac sleeves','male',HD)],
 3.2,[('a skylight',.75,.06,'male'),('a tunnel',.33,.42,'male'),('a fir tree',.50,.57,'male'),('a viaduct',.20,.68,'male')],
 'What is the man leaning across?',['He','is','leaning','across','a','model','railway','layout.'],'male',
 'Hands belong to an unseen person (only lilac sleeves), so target = the hands, voice = default male. Man box kept to head/torso/arm (his legs lie behind the hands area). Train off from 1.2 (only a tiny red speck may show near the station). Man places a tiny piece; the fir tree is only in the hands.')
