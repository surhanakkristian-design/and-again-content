from gen_5592_5593_5595_5596_lib import keys, write
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def b(x0,y0,x1,y1): return (x0,y0,x1-x0,y1-y0)
man=[b(.07,.16,.45,.80),b(.09,.16,.45,.82),b(.07,.15,.44,.85),b(.04,.14,.43,.85),
     b(0,.12,.40,.92),b(0,.10,.39,.98),b(0,.09,.38,1),b(0,.08,.38,1)]
wom=[b(.70,.26,.99,.86),b(.70,.27,.98,.87),b(.70,.27,1,.90),b(.70,.26,1,.91),
     b(.69,.26,1,.99),b(.71,.26,1,1),b(.74,.26,1,1),b(.76,.26,1,1)]
dog=[b(.47,.57,.69,.95),b(.45,.58,.69,.98),b(.44,.58,.69,1),b(.44,.60,.69,1),
     b(.40,.62,.68,1),b(.39,.67,.70,1),b(.40,.71,.70,1),b(.40,.76,.70,1)]
write(5595,{"mediaId":5595,"level":"A","keyWord":"awful","defaultVoice":"male",
 "taps":[{"phrase":"to sing into a microphone","target":"the man","voice":"male","keys":keys([(t,)+man[i] for i,t in enumerate(T)])},
         {"phrase":"to cover her ears","target":"the woman","voice":"female","keys":keys([(t,)+wom[i] for i,t in enumerate(T)])},
         {"phrase":"to sit on the floor","target":"the dog","voice":"male","keys":keys([(t,)+dog[i] for i,t in enumerate(T)])}],
 "stillS":0.2,
 "nouns":[{"word":"a microphone","x":0.40,"y":0.25,"voice":"male"},
          {"word":"a lamp","x":0.15,"y":0.40,"voice":"male"},
          {"word":"a sofa","x":0.12,"y":0.53,"voice":"male"},
          {"word":"a dog","x":0.58,"y":0.78,"voice":"male"}],
 "question":"What is the woman doing?",
 "answer":["She","is","covering","her","ears."],
 "answerVoice":"female",
 "notes":"Key word 'awful' is an adjective, not placed. Dog phrase kept A-level ('to sit on the floor') instead of 'to howl'; the dog sits on the rug in front of the stage, nobody else sits. Background guests (a couple with drinks) are not targets. The camera pushes in, so the dog and woman are cut by the frame edge in the last frames."})
