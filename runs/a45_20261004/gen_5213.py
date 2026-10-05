from gen_5212_5213_5214_5216_lib import build
boy = {0.0:(.08,.33,.47,.5),0.5:(.02,.25,.56,.72),1.0:(0,.21,.5,.45),1.5:(0,.21,.36,.45),2.0:(0,.23,.32,.32),2.5:(0,.22,.3,.33),
 3.0:(0,.21,.3,.34),3.5:(0,.2,.3,.34),4.0:(0,.19,.24,.33),4.5:(0,.35,.3,.32)}
wom = {5.0:(.12,.47,.42,.53),5.5:(.37,.43,.33,.43),6.0:(.43,.37,.43,.44),6.5:(.36,.39,.47,.33),7.0:(.42,.38,.52,.3),7.5:(.4,.36,.42,.3),
 8.0:(.53,.33,.43,.33),8.5:(.68,.31,.3,.2),9.0:(.53,.35,.45,.36),9.5:(.47,.33,.52,.4),10.0:(.68,.3,.32,.46)}
man = {6.0:(0,.38,.14,.17),6.5:(0,.37,.23,.2),7.0:(0,.34,.33,.66),7.5:(0,.33,.4,.67),8.0:(0,.28,.3,.72),8.5:(.14,.29,.46,.71),
 9.0:(0,.31,.52,.69),9.5:(0,.28,.47,.72),10.0:(0,.26,.66,.74)}
build(5213,'B','railway','female',[
 ('to hold up a cardboard sign','the boy','male',boy),
 ('to leap into someone\'s arms','the young woman in denim','female',wom),
 ('to wear a baseball cap','the man','male',man)],
 5.5,[('a glass roof',.5,.12,'female'),('a railway',.86,.57,'female'),('a bouquet',.13,.68,'female'),('a platform',.66,.88,'female')],
 'What is the boy doing?',['He','is','holding','a','sign','above','his','head.'],'male',
 'The packet description does not match well: the sign is not blank (a heart is drawn on its back), the arriving traveller in grey is not clearly a man with a rucksack. Avoided the traveller and the dark-haired woman with the bouquet (the bouquet is later held by others). Boy only 0-4.5 s (afterwards maybe the short-haired head in the hug, too unclear -> off). Young woman in denim from 5.0 (runs, jumps up at 6.0); man in cap from 6.0 (only his head at 6.0/6.5). defaultVoice female = the young woman in denim as main person;')
