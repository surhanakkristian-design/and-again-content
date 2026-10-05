import json
T=[i*0.5 for i in range(19)]
L=[(.57,.06,.43,.34),(.27,.03,.66,.97),(.3,.02,.7,.98),(.26,.04,.72,.96),(.02,.22,.88,.58),
   (.06,.03,.9,.78),(.09,.03,.83,.77),(.09,.03,.86,.77),(.07,.05,.82,.75),
   (.1,.03,.86,.62),(.14,0,.82,.62),(.08,0,.8,.48),None,None,
   (0,0,1,1),(0,0,1,1),(0,0,1,1),(0,0,1,1),(0,0,1,1)]
M=[None,None,None,None,None,
   (0,.15,.05,.22),(0,.17,.08,.32),(0,.2,.07,.25),(0,.19,.06,.2),
   (0,.66,.38,.34),(0,.64,.5,.36),(0,.5,.5,.5),(0,.18,.82,.82),(0,0,.9,1),
   None,None,None,None,None]
def K(B): return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,B)]
lk,mk=K(L),K(M)
tl="the lady in the straw hat"
c={"mediaId":5021,"level":"A","keyWord":"lady","defaultVoice":"female",
 "taps":[{"phrase":"to pour some tea","target":tl,"voice":"female","keys":lk},
         {"phrase":"to smile at the camera","target":tl,"voice":"female","keys":lk},
         {"phrase":"to wipe his hands","target":"the man in the jacket","voice":"male","keys":mk}],
 "stillS":2.0,
 "nouns":[{"word":"a hat","x":.55,"y":.31,"voice":"female"},{"word":"a lady","x":.5,"y":.55,"voice":"female"},
          {"word":"a teapot","x":.22,"y":.81,"voice":"female"},{"word":"cakes","x":.7,"y":.78,"voice":"female"}],
 "question":"What is the lady doing?",
 "answer":["She","is","pouring","tea","into","a","cup."],"answerVoice":"female",
 "notes":"Other women at 0.0 s (flower hat, blurred blonde) so the target is 'the lady in the straw hat'. The man in the jacket is only partly visible: a sliver of dark hair at the left edge 2.5-4.0 s (assumed to be him; tiny boxes), his sleeve/hand 4.5-5.5 s (box covers the arm only, his head at the edge is left out to avoid the lady's arm), and 6.0-6.5 s close-up of him wiping his hands on a napkin (lady off). The hands holding cups at 8.5-9.0 s are not boxed (owners unclear). The clip is short (9 s) and ends with the lady smiling into the camera."}
json.dump(c,open('content/5021.json','w'),indent=1)
