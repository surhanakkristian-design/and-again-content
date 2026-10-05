import json
T=[i*0.5 for i in range(25)]
W=[(.26,.16,.64,.84),(.26,.14,.64,.86),(.26,.17,.62,.83),(.3,.2,.6,.8),
   (0,.28,.48,.72),(0,.27,.52,.73),(0,.2,.55,.8),(0,.15,.6,.85),(0,.12,.62,.88),(0,.07,.62,.93),(0,.04,.66,.96),(0,0,.66,1),
   (0,.05,.43,.95),(0,.1,.68,.9),(.04,.19,.58,.81),(.08,.16,.56,.84),(.04,.15,.58,.85),(.08,.16,.56,.84),(.04,.22,.6,.78),
   (.05,.27,.62,.73),(.07,.3,.55,.7),(.02,.33,.5,.67),(0,.33,.44,.67),(0,.35,.4,.65),(0,.3,.4,.7)]
M=[None,None,None,None,
   (.49,.18,.51,.82),(.53,.16,.47,.84),(.56,.22,.44,.78),(.6,.2,.4,.8),(.63,.18,.37,.82),(.63,.23,.37,.77),(.67,.3,.33,.7),(.67,.37,.33,.63),
   (.44,.48,.56,.52),(.69,.52,.31,.48),(.66,.6,.34,.4),(.68,.6,.32,.4),(.68,.6,.32,.4),(.68,.6,.32,.4),(.68,.6,.32,.4),
   (.68,.58,.32,.42),(.63,.56,.37,.44),(.53,.48,.47,.52),(.45,.4,.55,.6),(.52,.33,.48,.67),(.5,.27,.5,.73)]
def K(B): return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,B)]
wk,mk=K(W),K(M)
c={"mediaId":5020,"level":"A","keyWord":"replace","defaultVoice":"female",
 "taps":[{"phrase":"to climb a ladder","target":"the woman","voice":"female","keys":wk},
         {"phrase":"to replace a light bulb","target":"the woman","voice":"female","keys":wk},
         {"phrase":"to give a thumbs-up","target":"the man","voice":"male","keys":mk}],
 "stillS":10.0,
 "nouns":[{"word":"a light bulb","x":.55,"y":.17,"voice":"female"},{"word":"a woman","x":.33,"y":.53,"voice":"female"},
          {"word":"a ladder","x":.45,"y":.87,"voice":"female"},{"word":"a man","x":.87,"y":.78,"voice":"male"}],
 "question":"What is the woman doing?",
 "answer":["She","is","replacing","a","light","bulb."],"answerVoice":"female",
 "notes":"Main person is the woman (defaultVoice female). Man is out of frame 0-1.5 s. Woman and man stand close behind/around the ladder 2.0-6.5 s and 10.5-11.0 s: boxes split along a vertical line (at 6.0 s her box is cut to her body/legs x<0.43 because his head is just right of her hand on the ladder top). The man's thumbs-up happens at 11.5-12.0 s; 'to hold the ladder' was avoided because the woman holds it too."}
json.dump(c,open('content/5020.json','w'),indent=1)
