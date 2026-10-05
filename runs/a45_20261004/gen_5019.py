import json
T=[i*0.5 for i in range(25)]
W=[(.16,0,.84,.6),(.13,0,.87,.74),(.2,.05,.78,.52),(.35,0,.65,.5),(.3,0,.7,.6),(.2,0,.8,.46),(.2,0,.8,.66),
   (.15,0,.85,.56),(.2,0,.8,.52),(.25,0,.75,.52),(.25,0,.75,.56),(.3,0,.7,.56),(.3,0,.7,.46),
   (0,0,1,.64),(0,0,1,.72),(0,0,1,.72),(0,0,1,.74),(0,0,1,.74),
   (.18,.02,.78,.7),(.2,0,.76,.72),(.17,0,.81,.72),(.18,0,.82,.7),(.15,.03,.82,.82),(.22,.05,.76,.78),(.11,.13,.87,.67)]
M=[(0,.17,.16,.3),(0,.16,.12,.3),(0,.14,.15,.3),(0,.12,.2,.3),(0,.05,.2,.28),(0,0,.18,.3),(0,0,.14,.22),
   None,None,None,None,None,None,None,None,None,None,None,
   (0,.17,.16,.3),(0,.19,.19,.3),(0,.19,.16,.3),(0,.2,.17,.28),(0,.23,.14,.3),(0,.22,.2,.3),(0,.24,.11,.3)]
def K(B): return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,B)]
wk,mk=K(W),K(M)
c={"mediaId":5019,"level":"A","keyWord":"beef","defaultVoice":"female",
 "taps":[{"phrase":"to cook beef on a grill","target":"the waitress","voice":"female","keys":wk},
         {"phrase":"to hold a lettuce leaf","target":"the waitress","voice":"female","keys":wk},
         {"phrase":"to wear glasses","target":"the man with glasses","voice":"male","keys":mk}],
 "stillS":2.0,
 "nouns":[{"word":"a man","x":.10,"y":.18,"voice":"male"},{"word":"lettuce","x":.12,"y":.48,"voice":"female"},
          {"word":"beef","x":.48,"y":.66,"voice":"female"},{"word":"a grill","x":.55,"y":.80,"voice":"female"}],
 "question":"What is the waitress doing?",
 "answer":["She","is","cooking","beef","on","a","grill."],"answerVoice":"female",
 "notes":"Two women (waitress + a female guest), so the question and targets name her the waitress. The man's box is small (guest at the far left, w < 0.18) because the waitress's hands come close; at 11.0 and 12.0 her hands/lettuce overlap him in the picture and the boxes are split at x 0.14/0.11. 'to wear glasses' is a state (no action fits only the man)."}
json.dump(c,open('content/5019.json','w'),indent=1)
