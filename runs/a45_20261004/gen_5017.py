import json
T=[i*0.5 for i in range(25)]
B=[(.45,0,.55,.54),(.48,0,.52,.48),(0,0,1,.66),(.48,0,.52,.64),(.55,0,.45,.54),(0,0,1,.42),
   (.02,0,.98,.84),(.02,0,.98,.84),(0,0,1,.82),(0,0,1,.82),(.02,0,.98,.82),(0,0,1,.82),(0,0,1,.78),
   (0,0,1,.76),(0,0,1,.78),(0,0,1,.78),(0,0,1,.64),(0,0,1,.64),(0,.02,.98,.92),(.04,.03,.92,.84),
   (.08,.02,.88,.76),(.06,.02,.92,.76),(.06,.02,.9,.76),(.06,.02,.9,.76),(.05,.01,.9,.76)]
keys=[dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,B)]
c={"mediaId":5017,"level":"A","keyWord":"cut","defaultVoice":"male",
 "taps":[{"phrase":p,"target":"the man","voice":"male","keys":keys} for p in ["to cut a red onion","to smile at the camera","to wear an apron"]],
 "stillS":12.0,
 "nouns":[{"word":"a man","x":.46,"y":.32,"voice":"male"},{"word":"a tea towel","x":.66,"y":.71,"voice":"male"},
          {"word":"vegetables","x":.55,"y":.81,"voice":"male"},{"word":"a knife","x":.10,"y":.90,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","cutting","vegetables","with","a","knife."],"answerVoice":"male",
 "notes":"Only one person: all three taps target the man (close-ups 0-2.5 s show only his hands). Key word 'cut' is an adjective (cut vegetables), not used as a noun pill. Knife pill sits at the left edge (knife x .00-.11)."}
json.dump(c,open('content/5017.json','w'),indent=1)
