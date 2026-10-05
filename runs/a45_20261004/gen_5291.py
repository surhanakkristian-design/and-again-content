from lib_5290_5291_5292_5293 import write
W = {0.0:(0,.10,1,.90),0.5:(0,.12,1,.88),1.0:(0,.15,1,.85),1.5:(0,.18,1,.82),2.0:(0,.22,1,.78),2.5:(0,.26,1,.74),
     3.0:(0,.33,.84,.67),3.5:(0,.34,.72,.66),4.0:(0,.38,.60,.62),4.5:(0,.41,.42,.59),5.0:(0,.55,.24,.45)}
H = {3.0:(.82,.15,.18,.18),3.5:(.72,.19,.28,.24),4.0:(.60,.23,.40,.25),4.5:(.43,.26,.45,.23),
     5.0:(.24,.29,.33,.23),5.5:(.08,.30,.40,.22),6.0:(0,.33,.22,.19)}
write(5291, {"mediaId":5291,"level":"A","keyWord":"businessman","defaultVoice":"female",
 "taps":[{"phrase":"to sleep with her mouth open","target":"the blonde woman","voice":"female","boxes":W},
         {"phrase":"to wear a grey hoodie","target":"the blonde woman","voice":"female","boxes":W},
         {"phrase":"to sleep with his hood up","target":"the man in the hood","voice":"male","boxes":H}],
 "stillS":8.0,
 "nouns":[{"word":"lights","x":.42,"y":.06,"voice":"female"},
          {"word":"a neck pillow","x":.80,"y":.46,"voice":"female"},
          {"word":"seats","x":.13,"y":.54,"voice":"female"},
          {"word":"a businessman","x":.75,"y":.68,"voice":"male"}],
 "question":"What is the blonde woman doing?",
 "answer":["She","is","sleeping","with","her","mouth","open."],
 "answerVoice":"female",
 "notes":"Everybody sleeps, so the phrases use what is unique: open mouth + grey hoodie (blonde woman, 0.0-5.0) and hood up (man in the black hoodie, 3.0-6.0). The neck-pillow man was not used because several men behind also wear neck pillows from 7.5. Still 8.0: 'a businessman' = the grey-haired man in the suit in front; 'seats' = the left row; 'a neck pillow' on the blue pillow of the man behind him; 'lights' = the ceiling lights."})
