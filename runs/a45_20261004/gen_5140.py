import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
O={0.0:(.5,.08,.5,.42),0.5:(.5,.02,.5,.52),1.0:(.42,0.0,.58,.6),1.5:(.33,0.0,.67,.6),2.0:(.25,0.0,.75,.56),2.5:(.28,0.0,.72,.56),
   3.0:(.18,0.0,.82,.55),3.5:(.19,0.0,.81,.57),4.0:(.2,0.0,.8,.6),4.5:(.3,0.0,.7,.6),5.0:(.22,0.0,.78,.6),5.5:(.45,0.0,.55,.62),
   6.0:(.44,0.0,.56,.52),6.5:(.48,.02,.52,.44),7.0:(.5,.08,.45,.28),7.5:(.5,.15,.36,.16)}
W={0.0:(0.0,.63,.45,.35),0.5:(0.0,.58,.55,.4),1.0:(0.0,.76,.18,.14),5.5:(0.0,.65,.2,.3),
   6.0:(0.0,.53,.68,.47),6.5:(0.0,.46,.68,.54),7.0:(0.0,.37,.92,.63),7.5:(0.0,.32,.96,.68),8.0:(0.0,0.0,1.0,1.0),
   8.5:(0.0,0.0,1.0,1.0),9.0:(.08,.1,.86,.9),9.5:(.08,.17,.9,.83),10.0:(.1,.22,.9,.78)}
c={"mediaId":5140,"level":"B","keyWord":"allow","defaultVoice":"male",
 "taps":[
  {"phrase":"to stamp a passport","target":"the officer","voice":"male","keys":keys(O)},
  {"phrase":"to wear a peaked cap","target":"the officer","voice":"male","keys":keys(O)},
  {"phrase":"to show off her passport","target":"the woman in the beanie","voice":"female","keys":keys(W)}],
 "stillS":3.0,
 "nouns":[{"word":"a peaked cap","x":.68,"y":.08,"voice":"male"},{"word":"a queue","x":.3,"y":.22,"voice":"male"},
          {"word":"a rubber stamp","x":.26,"y":.49,"voice":"male"},{"word":"a passport","x":.52,"y":.58,"voice":"male"}],
 "question":"What is the officer doing?","answer":["He","is","stamping","the","traveller's","passport."],"answerVoice":"male",
 "notes":"defaultVoice male = the officer is the main person for most of the clip (woman appears in full only from 8.0). Woman in the beanie: 0.0-1.5, 5.5-7.5 only her hand (ring, olive sleeve, POV filming) - assumed to be her hand; 1.0 only a fingertip at the bottom-left edge (weak, minimum box), 1.5 off. Officer and woman boxes split at 6.0-7.5 where she holds the passport in front of him (officer box = only the part above the passport). A blonde woman with glasses stands in the queue, hence 'the woman in the beanie'. Key word 'allow' is a verb, not a noun. Still 3.0: queue of travellers top left."}
json.dump(c,open('content/5140.json','w'),indent=1)
