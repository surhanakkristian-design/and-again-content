import json
T=[i*0.5 for i in range(21)]
M=[(.05,.15,.68,.60),(.29,.05,.48,.71),(.24,.02,.58,.82),(.28,.19,.49,.60),(.24,.27,.52,.47),(.26,.22,.48,.46),(.23,.22,.56,.46),(.23,.23,.56,.45),(.21,.23,.57,.46),(.24,.26,.56,.44),(.12,.15,.67,.56),(.16,.04,.66,.70),(.11,.11,.78,.60),(.18,.26,.48,.42),(.23,.34,.41,.28),(.33,.35,.36,.24),(.45,.34,.36,.23),(.44,.32,.30,.27),(.31,.28,.32,.33),(.26,.28,.34,.34),(.22,.29,.34,.35)]
F=[(.73,.38,.27,.28),(.77,.33,.23,.30),(.82,.31,.18,.37),(.77,.28,.23,.38),(.76,.24,.24,.28),(.74,.22,.26,.30),(.79,.23,.21,.36),(.79,.24,.21,.36),(.78,.24,.22,.28),(.80,.24,.20,.26),(.79,.30,.21,.34),(.82,.47,.18,.20),None,None,None,None,None,(.74,.36,.26,.30),(.63,.36,.37,.31),(.60,.37,.36,.31),(.56,.39,.36,.30)]
def keys(L): return [({"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} if b else {"t":t,"off":True}) for t,b in zip(T,L)]
c={"mediaId":707,"level":"A","keyWord":"snowboard","defaultVoice":"male",
"taps":[{"phrase":"to put on a snowboard","target":"the man in blue","voice":"male","keys":keys(M)},
{"phrase":"to ride down the hill","target":"the man in blue","voice":"male","keys":keys(M)},
{"phrase":"to wear a dark jacket","target":"the person in grey","voice":"male","keys":keys(F)}],
"stillS":0.5,
"nouns":[{"word":"a snowboard","x":.50,"y":.77,"voice":"male"},{"word":"a helmet","x":.63,"y":.15,"voice":"male"},{"word":"snow","x":.35,"y":.93,"voice":"male"},{"word":"the sky","x":.25,"y":.06,"voice":"male"}],
"question":"What is the man in blue doing?","answer":["He","is","riding","a","snowboard","down","the","hill."],"answerVoice":"male",
"notes":"The rider's face looks male (1.0 s), so 'the man in blue'; the sitting friend's gender is not clear, so 'the person in grey' with the default voice and a state phrase (both people sit on the snow, so sitting would fit both; the friend's own action, covering the face at 9.0-10.0 s, needs his/her). The friend is at the right edge and partly cut off in 0.0-5.5 s, out of frame 6.0-8.0 s. Boxes are split where the two are close (1.0, 3.0-4.5, 9.0-10.0 s); at 0.0 s the held orange board reaches over the friend, the rider's box stops at x 0.73. The friend also has a (dark) snowboard on the feet, hardly visible; the 'a snowboard' pill is on the orange one."}
json.dump(c,open('content/707.json','w'),indent=1)
