import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [({"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3])) for t in T]
M={0.0:(.50,0,.50,1),0.5:(.02,.29,.98,.71),1.0:(.02,.19,.98,.81),1.5:(.05,.09,.95,.91),2.0:(.34,.44,.66,.56),
   2.5:(.48,.25,.52,.33),3.0:(.32,.20,.68,.80),3.5:(.34,.24,.66,.76),4.0:(.37,.33,.63,.67),4.5:(.37,.31,.63,.69),
   5.0:(.38,.17,.62,.83),5.5:(.41,.19,.59,.81),6.0:(0,.18,1,.61),6.5:(.16,.17,.84,.62),7.0:(.14,.21,.86,.58),
   7.5:(.16,.19,.84,.60),8.0:(.12,.17,.88,.62),8.5:(.16,.18,.84,.61),9.0:(.14,.24,.86,.55),9.5:(.16,.24,.84,.55),10.0:(.14,.22,.86,.57)}
J={0.0:(.18,.33,.31,.27),2.5:(.27,.59,.33,.29),3.0:(0,.25,.31,.36),3.5:(.05,.28,.28,.34),4.0:(0,.28,.33,.25),
   4.5:(0,.28,.33,.25),5.0:(0,.29,.33,.36),5.5:(0,.29,.32,.36)}
P={t:(.14,.80,.57,.19) for t in T if t>=6.0}
c={"mediaId":355,"level":"B","keyWord":"guilt","defaultVoice":"male",
 "taps":[{"phrase":"to bury his face","target":"the man","voice":"male","keys":keys(M)},
  {"phrase":"to have a long crack","target":"the cracked jug","voice":"male","keys":keys(J)},
  {"phrase":"to hold rice and stew","target":"the plate","voice":"male","keys":keys(P)}],
 "stillS":8.0,
 "nouns":[{"word":"a picture frame","x":.21,"y":.20,"voice":"male"},{"word":"pottery","x":.16,"y":.36,"voice":"male"},
  {"word":"a couch","x":.14,"y":.56,"voice":"male"},{"word":"a plate","x":.42,"y":.90,"voice":"male"}],
 "question":"How is the man showing his guilt?","answer":["He","is","burying","his","face","in","his","hands."],"answerVoice":"male",
 "notes":"Jug: boxed at 0.0 (still whole, on the shelf) and 2.5-5.5 (crack visible); 0.5-2.0 it is out of the picture. In the table shot (6.0+) a similar jug stands far in the background behind his shoulder with no crack visible: left off. At 2.5 he holds the jug in front of his body, so the man's box is his head and chest only. In the table shot the man's box ends above the plate. Plate phrase is a state (the plate does nothing). A second white plate is only a sliver in the bottom-left corner."}
json.dump(c,open('content/355.json','w'),indent=1)
