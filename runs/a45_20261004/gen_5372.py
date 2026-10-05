from lib_5372_5373_5374_5375 import keys, write, times
T = times(5372)
# boxes as x1,y1,x2,y2
man = {0.0:(.25,0,.67,.37),0.5:(.24,0,.58,.40),1.0:(.18,0,.57,.39),1.5:(.28,0,.77,.40),2.0:(.20,0,.62,.38),
 2.5:(.0,0,.62,.38),3.0:(.0,0,.57,.39),3.5:(.10,0,.45,.43),4.0:(.02,0,.57,.40),4.5:(.0,0,.45,.44),
 5.0:(.0,0,.55,.40),5.5:(.08,0,.60,.57),6.0:(.14,0,.52,.63),6.5:(.18,0,.68,.56),7.0:(.0,.04,.62,.57),
 7.5:(.03,.0,.62,.54),8.0:(.03,0,.50,.56),8.5:(.08,0,1.0,.50),9.0:(.08,.18,.95,.57),9.5:(.18,.15,1.0,.56),
 10.0:(.10,.08,.84,.57),10.5:(.13,.09,.77,.56),11.0:(.06,.05,.74,.58),11.5:(.17,.07,.67,.60),12.0:(.20,.09,.64,.64)}
pile = {0.0:(.30,.37,1,.60),0.5:(.30,.40,1,.63),1.0:(.40,.39,1,.68),1.5:(.48,.40,1,.70),2.0:(.35,.38,1,.68),
 2.5:(.25,.38,1,.58),3.0:(.20,.39,1,.60),3.5:(.45,.30,1,.62),4.0:(.25,.40,1,.64),4.5:(.46,.44,1,.70),
 5.0:(.25,.40,1,.73),5.5:(.60,.42,1,.82),6.0:(.52,.50,1,.88),6.5:(.20,.56,1,.76),7.0:(.18,.57,1,.76),
 7.5:(.25,.54,1,.73),8.0:(.50,.44,1,.70),8.5:(.28,.50,1,.73),9.0:(.18,.57,1,.84),9.5:(.18,.56,1,.84),
 10.0:(.18,.57,1,.80),10.5:(.18,.56,1,.80),11.0:(.18,.58,1,.86),11.5:(.22,.60,1,.86),12.0:(.28,.64,1,.88)}
km, kp = keys(T, man), keys(T, pile)
write(5372, {"mediaId":5372,"level":"A","keyWord":"broom","defaultVoice":"male",
 "taps":[{"phrase":"to sweep the leaves","target":"the man","voice":"male","keys":km},
         {"phrase":"to bend forward","target":"the man","voice":"male","keys":km},
         {"phrase":"to lie in a big pile","target":"the leaves","voice":"male","keys":kp}],
 "stillS":12.0,
 "nouns":[{"word":"palm trees","x":0.70,"y":0.18,"voice":"male"},{"word":"a car","x":0.16,"y":0.42,"voice":"male"},
          {"word":"a broom","x":0.52,"y":0.61,"voice":"male"},{"word":"leaves","x":0.64,"y":0.73,"voice":"male"}],
 "question":"What is the man doing?","answer":["He","is","sweeping","the","leaves."],"answerVoice":"male",
 "notes":"Single shot, one young man sweeping a terrace. Passers-by in the background (t 4.5+), so phrases avoid walking. Man box includes the broom head; leaf-pile box split from the man at his feet line (pile edge near his feet excluded). Two phrases share the man; third target is the leaf pile (a state)."})
