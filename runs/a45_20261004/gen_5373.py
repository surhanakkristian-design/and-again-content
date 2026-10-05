from lib_5372_5373_5374_5375 import keys, write, times
T = times(5373)
woman = {0.0:(.37,.24,.95,.95),0.5:(.27,.17,1,.85),1.0:(.40,.19,1,.50),1.5:(.33,.16,.92,.45),2.0:(.33,.14,.80,.36),
 4.0:(.54,.26,.87,.59),4.5:(.60,.27,.93,.55),5.0:(.58,.32,.92,.52),5.5:(.56,.36,.92,.52),6.0:(.58,.38,.88,.52),
 6.5:(.39,.57,.59,.93),7.0:(.40,.58,.62,.98),7.5:(.40,.55,.62,.97),8.0:(.43,.55,.64,.96),8.5:(0,.30,1,1),9.0:(.05,.54,.92,1)}
dough = {0.0:(0,.71,.22,.89),0.5:(0,.74,.18,.90),1.0:(0,.80,.18,.98),2.5:(0,.38,1,.82),3.0:(0,.36,1,.83),3.5:(0,.36,1,.84),
 6.5:(.04,.72,.32,.86),7.0:(.04,.75,.32,.88),7.5:(.06,.77,.33,.88),8.0:(.08,.77,.34,.89)}
castle = {6.5:(.02,.45,.98,.57),7.0:(.04,.44,.85,.58),7.5:(.06,.22,.94,.55),8.0:(.03,.13,1,.55),8.5:(0,0,1,.30),9.0:(0,0,1,.54)}
write(5373, {"mediaId":5373,"level":"B","keyWord":"expand","defaultVoice":"female",
 "taps":[{"phrase":"to gasp in amazement","target":"the woman in dungarees","voice":"female","keys":keys(T,woman)},
         {"phrase":"to rise over the rim","target":"the dough","voice":"female","keys":keys(T,dough)},
         {"phrase":"to inflate into a castle","target":"the bouncy castle","voice":"female","keys":keys(T,castle)}],
 "stillS":8.0,
 "nouns":[{"word":"the sky","x":0.50,"y":0.07,"voice":"female"},{"word":"a bouncy castle","x":0.50,"y":0.38,"voice":"female"},
          {"word":"dough","x":0.20,"y":0.84,"voice":"female"},{"word":"a picnic table","x":0.66,"y":0.87,"voice":"female"}],
 "question":"What is the dough doing?","answer":["It","is","rising","over","the","rim","of","the","bowl."],"answerVoice":"female",
 "notes":"Four shots: beach ball (0-2.0), dough close-up (2.5-3.5, woman off; only anonymous legs), pool (4.0-6.0, woman small behind it), bouncy castle (6.5-9.0). Woman in dungarees seen from behind in the group shots 6.5-8.0; there her box starts at head level and the castle box stops at head height (split; at 6.5/7.0 her head top is cut a little). Dough off 1.5-2.0 (hidden by the ball) and in the pool shots. Beach ball not used as a target."})
