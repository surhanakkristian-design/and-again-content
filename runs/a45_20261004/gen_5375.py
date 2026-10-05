from lib_5372_5373_5374_5375 import keys, write, times
T = times(5375)
w = {0.0:(0,.17,.68,1),0.5:(.08,.21,1,1),1.0:(.06,.16,.72,1),1.5:(0,.15,.96,1),2.0:(0,.16,.88,1),
 2.5:(0,.20,.76,1),3.0:(0,.24,1,1),3.5:(.02,.18,.82,1),4.0:(.06,.18,.75,1),4.5:(.26,.37,.80,1),
 5.0:(.04,.32,.70,1),5.5:(0,.32,.78,.92),6.0:(.14,.42,.80,.73),6.5:(.28,.42,.74,.62),7.0:(.27,.38,.58,.54),
 7.5:(.22,.34,.52,.50),8.0:(.30,.34,.56,.50),8.5:(.41,.40,.71,.60),9.0:(.41,.43,.82,.77),9.5:(.23,.19,.70,.96),10.0:(.06,.18,.76,1)}
kw = keys(T, w)
write(5375, {"mediaId":5375,"level":"B","keyWord":"swing","defaultVoice":"female",
 "taps":[{"phrase":"to swing a golf club","target":"the woman","voice":"female","keys":kw},
         {"phrase":"to grip a thick rope","target":"the woman","voice":"female","keys":kw},
         {"phrase":"to swing out over the lake","target":"the woman","voice":"female","keys":kw}],
 "stillS":6.0,
 "nouns":[{"word":"the sky","x":0.75,"y":0.08,"voice":"female"},{"word":"a rope","x":0.55,"y":0.20,"voice":"female"},
          {"word":"trees","x":0.82,"y":0.32,"voice":"female"},{"word":"a lake","x":0.68,"y":0.84,"voice":"female"}],
 "question":"What is she doing over the lake?","answer":["She","is","swinging","on","a","thick","rope."],"answerVoice":"female",
 "notes":"Only one person, so all three phrases target the woman (club and rope are held by her, boxes would overlap). The description misses a shot: 2.5-4.0 is a batting cage where she swings a baseball bat (bat visible at 2.5, top left), not the golf range; golf club only 0.0-2.0. Phrase 1 and 3 both use 'swing' (key word) in two different senses. Woman small and far at 7.0-8.0 (boxes padded)."})
