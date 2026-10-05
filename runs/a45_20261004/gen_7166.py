from gen_7162_7163_7164_7166_lib import write
K=[(0.00,0.11,0.97,0.64),(0.15,0.13,0.78,0.65),(0.18,0.09,0.56,0.74),(0.19,0.11,0.60,0.78),(0.20,0.13,0.56,0.79),(0.19,0.15,0.62,0.84),(0.17,0.17,0.59,0.83),(0.17,0.17,0.60,0.83)]
T="the climber"
write(7166, {"mediaId":7166,"level":"B","keyWord":"get","defaultVoice":"female",
 "taps":[{"phrase":"to step onto the summit","target":T,"voice":"female","keys":K},
         {"phrase":"to balance on the ridge","target":T,"voice":"female","keys":list(K)},
         {"phrase":"to push up her goggles","target":T,"voice":"female","keys":list(K)}],
 "stillS":2.2,
 "nouns":[{"word":"goggles","x":0.47,"y":0.18,"voice":"female"},{"word":"clouds","x":0.13,"y":0.38,"voice":"female"},
          {"word":"an ice axe","x":0.36,"y":0.64,"voice":"female"},{"word":"a rope","x":0.80,"y":0.92,"voice":"female"}],
 "question":"Where is the climber standing?",
 "answer":["She","is","standing","on","the","snowy","summit."],"answerVoice":"female",
 "notes":"Only one person, so all three phrases share the climber (shadow/rope overlap her box or are not doers). 'get' is a verb, not placed. She balances with arms out in the first second, pushes the goggles up at 2.7-3.7 s. Pill 'clouds' sits on the sea of clouds left of her arm."})
