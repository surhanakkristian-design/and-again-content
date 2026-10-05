import json
T=[i*0.5 for i in range(19)]
def keys(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
D={0.0:(.61,0.0,.39,.72),0.5:(.61,0.0,.39,.7),1.0:(.61,0.0,.39,.75),1.5:(0.0,.15,.3,.85),2.0:(0.0,.13,.29,.87),2.5:(0.0,.15,.29,.85),
   3.0:(0.0,.18,.22,.82),3.5:(0.0,.15,.25,.85),4.0:(.8,.38,.2,.16),4.5:(.79,.38,.21,.2),5.0:(.8,.47,.2,.16),5.5:(.82,.6,.18,.14),
   6.0:(.6,0.0,.4,1.0),6.5:(.6,.08,.4,.92),7.0:(.81,.15,.19,.85),8.0:(.82,.08,.18,.92),8.5:(.68,.62,.32,.38),9.0:(.53,.52,.47,.48)}
M={0.0:(0.0,.2,.6,.8),0.5:(0.0,.2,.6,.8),1.0:(0.0,.2,.6,.8),1.5:(.31,.12,.66,.88),2.0:(.3,.1,.7,.9),2.5:(.3,.1,.7,.9),
   3.0:(.23,.15,.77,.85),3.5:(.26,.18,.74,.82),4.0:(0.0,.12,.79,.88),4.5:(0.0,.08,.78,.92),5.0:(0.0,.08,.79,.92),5.5:(.08,.2,.73,.8),
   6.0:(.14,.26,.45,.74),6.5:(.14,.26,.45,.74),7.0:(0.0,.18,.8,.82),7.5:(.1,.18,.9,.82),8.0:(.02,.18,.79,.82),8.5:(0.0,.17,.67,.83),9.0:(0.0,.03,.52,.97)}
c={"mediaId":5141,"level":"A","keyWord":"doctor","defaultVoice":"male",
 "taps":[
  {"phrase":"to open his mouth","target":"the young man","voice":"male","keys":keys(M)},
  {"phrase":"to show his muscles","target":"the young man","voice":"male","keys":keys(M)},
  {"phrase":"to give a small card","target":"the doctor","voice":"male","keys":keys(D)}],
 "stillS":6.0,
 "nouns":[{"word":"a poster","x":.16,"y":.32,"voice":"male"},{"word":"a cupboard","x":.82,"y":.42,"voice":"male"},
          {"word":"a doctor","x":.78,"y":.8,"voice":"male"},{"word":"a bed","x":.15,"y":.86,"voice":"male"}],
 "question":"What is the young man opening?","answer":["He","is","opening","his","mouth."],"answerVoice":"male",
 "notes":"Two men, doctor and young patient; boxes split where the doctor's hands touch the patient (0.0-1.0 split at x .6, cuts the patient's right shoulder; 4.0-5.5 only the doctor's sleeve/hand at the right edge, patient box stops at ~.8 and cuts his outstretched arm). Doctor off at 7.5 (only a sliver at the edge). 'to open his mouth' true 0.0-2.5, 'to show his muscles' (flexing) 7.0-8.0, 'to give a small card' 6.5-9.0. Still 6.0: 'a bed' = the examination couch."}
json.dump(c,open('content/5141.json','w'),indent=1)
