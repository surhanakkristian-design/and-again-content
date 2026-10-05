import json
T=[i*0.5 for i in range(25)]
Wo=[(0,0,.33,.72),(0,0,.30,.74),(0,0,.29,.70),(0,0,.29,.70),(0,0,.27,.55),(0,0,.28,.55),(0,0,.42,.75),(0,0,.37,.76),
(0,0,.31,.50),(0,0,.27,.50),(0,.02,.40,.48),(0,.02,.38,.52),(0,.08,.46,.44),(0,.15,.42,.40),(.01,.21,.44,.33),(.06,.26,.39,.30),
(.13,.31,.32,.28),(.18,.32,.29,.29),(.21,.38,.26,.25),(.23,.41,.24,.26),(.26,.43,.23,.26),(.28,.44,.20,.25),(.29,.45,.19,.25),(.28,.47,.19,.24),(.27,.46,.20,.24)]
Ma=[(.38,0,.62,.58),(.33,0,.67,.74),(.31,0,.69,.75),(.30,0,.70,.78),(.30,0,.70,.76),(.32,0,.68,.55),(.43,0,.57,.62),(.38,0,.62,.55),
(.34,0,.66,.62),(.30,0,.70,.60),(.41,.06,.54,.46),(.40,.01,.55,.50),(.46,.09,.35,.38),(.42,.15,.34,.35),(.45,.21,.30,.32),(.45,.26,.28,.30),
(.46,.31,.26,.28),(.47,.35,.27,.27),(.47,.36,.25,.27),(.47,.39,.24,.27),(.49,.42,.21,.27),(.48,.43,.21,.25),(.48,.44,.20,.26),(.47,.46,.21,.25),(.47,.45,.21,.25)]
k=lambda L:[dict(t=t,x=a,y=b,w=c,h=d) for t,(a,b,c,d) in zip(T,L)]
c={"mediaId":5153,"level":"A","keyWord":"bed","defaultVoice":"male",
"taps":[{"phrase":"to have long dark hair","target":"the woman","voice":"female","keys":k(Wo)},
 {"phrase":"to wear blue shorts","target":"the man","voice":"male","keys":k(Ma)},
 {"phrase":"to wear a white shirt","target":"the woman","voice":"female","keys":k(Wo)}],
"stillS":9.5,
"nouns":[{"word":"the sky","x":0.50,"y":0.15,"voice":"male"},{"word":"trees","x":0.84,"y":0.38,"voice":"male"},
 {"word":"a man","x":0.58,"y":0.50,"voice":"male"},{"word":"a bed","x":0.56,"y":0.75,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","putting","small","plants","in","the","bed."],"answerVoice":"male",
"notes":"All three phrases are states: both people plant seedlings (the woman too at 3.0-3.5 and 5.0-5.5) and both hold a trowel at the end, so no planting/trowel action fits only one of them. Woman's shirt is off-white linen. Close-up 0-5.5: the woman is only partly in frame at the left; at 3.0/3.5 her reaching hand comes close to the man and the boxes are split at x 0.42/0.37 (her hand at 3.5 is partly in the man's area). 'a bed' at 9.5 sits on the middle raised bed, but two more beds are visible left and right; defaultVoice male (evenId false, mixed couple)."}
json.dump(c,open('content/5153.json','w'),indent=1)
