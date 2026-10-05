import json
def keys(T,d):
    out=[]
    for t in T:
        if t in d:
            a=d[t]; out.append({"t":t,"x":a[0],"y":a[1],"w":round(a[2]-a[0],2),"h":round(a[3]-a[1],2)})
        else: out.append({"t":t,"off":True})
    return out
def dump(c): json.dump(c,open('content/%d.json'%c["mediaId"],'w'),indent=1)

# ---------- 837
T=[i*0.5 for i in range(13)]
D={0.0:(0,.2,.52,.8),0.5:(0,.2,.45,.8),1.0:(0,.18,.75,.85),1.5:(0,.42,.30,.75),
   4.5:(.08,.18,1,.68),5.0:(0,.22,.95,.78),5.5:(0,.22,.95,.78),6.0:(.05,.2,1,.76)}
X={2.0:(.56,.2,1,1),2.5:(.6,.18,1,1),3.0:(.6,.27,1,1),3.5:(.58,.27,1,1),4.0:(.57,.2,1,1)}
kd,kx=keys(T,D),keys(T,X)
dump({"mediaId":837,"level":"A","keyWord":"taxi","defaultVoice":"male",
"taps":[{"phrase":"to hold the wheel","target":"the driver","voice":"male","keys":kd},
{"phrase":"to turn his head","target":"the driver","voice":"male","keys":kd},
{"phrase":"to go down a small street","target":"the yellow taxi","voice":"male","keys":kx}],
"stillS":2.0,
"nouns":[{"word":"a taxi","x":.80,"y":.58,"voice":"male"},{"word":"a wall","x":.45,"y":.20,"voice":"male"},
{"word":"the road","x":.25,"y":.78,"voice":"male"},{"word":"a mirror","x":.70,"y":.38,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","driving","a","yellow","taxi."],"answerVoice":"male",
"notes":"Cuts: inside the cab 0-1.5 s and 4.5-6.0 s (driver from behind, the taxi itself is not a tappable outside object there, so the taxi box is off), outside 2.0-4.0 s (only the taxi, driver off). At 1.5 s the camera swings and only the driver's arm on the wheel is left at the left edge. A dark shape at the bottom right at 0.0-1.5 s is probably the passenger, not used. 'a mirror' = the side mirror of the taxi at 2.0 s, close above the 'a taxi' pill."})

# ---------- 838
T=[i*0.5 for i in range(19)]
M={0.0:(.25,.1,.70,.96),0.5:(.06,.13,.78,.96),1.0:(.18,.15,.80,1),1.5:(.28,.15,.72,1),2.0:(.17,.17,.70,.95),
   2.5:(.21,.18,.76,.94),3.0:(.30,.2,.72,1),3.5:(.35,.2,.75,1),4.0:(.42,.2,.75,.92),
   4.5:(.30,.25,1,1),5.0:(.30,.25,1,1),5.5:(.30,.25,1,1),6.0:(.28,.25,1,1),6.5:(.02,.25,1,1),7.0:(0,.25,1,1),
   7.5:(.05,.2,1,1),8.0:(0,.2,1,1),8.5:(0,.2,1,1),9.0:(0,.2,1,1)}
W={2.5:(0,.28,.20,.86),3.0:(0,.27,.29,.98),3.5:(.08,.27,.35,.98),4.0:(.22,.28,.42,.72)}
km,kw=keys(T,M),keys(T,W)
dump({"mediaId":838,"level":"A","keyWord":"pilot","defaultVoice":"male",
"taps":[{"phrase":"to touch his hair","target":"the man in the brown jacket","voice":"male","keys":km},
{"phrase":"to take a selfie","target":"the man in the brown jacket","voice":"male","keys":km},
{"phrase":"to smile at the man","target":"the woman in the blue hat","voice":"female","keys":kw}],
"stillS":5.5,
"nouns":[{"word":"a pilot","x":.72,"y":.75,"voice":"male"},{"word":"a plane","x":.25,"y":.40,"voice":"male"},
{"word":"the sky","x":.80,"y":.23,"voice":"male"},{"word":"the ground","x":.20,"y":.90,"voice":"male"}],
"question":"What is the man in sunglasses doing?","answer":["He","is","touching","his","hair."],"answerVoice":"male",
"notes":"Shot 1 (0-4.0 s) airport hall, shot 2 (4.5-9.0 s) selfie in front of a jet engine. The woman in uniform is in the picture 2.5-4.0 s only; at 3.5 and 4.0 s she stands partly behind the man, boxes split by a vertical line (3.5 s: x 0.35, 4.0 s: x 0.42), so the man's back boot (3.5 s) and his back leg (4.0 s) fall outside his box - weak spot. A uniformed man with stripes passes at 0.5-1.5 s, not used as a target (he overlaps the main man); because of him the question says 'the man in sunglasses', not 'the pilot'. 'a plane' is placed on the engine (only part of the plane in view); tiny far planes at the right edge about y 0.32. He touches his hair from 7.0 s."})

# ---------- 839
T=[i*0.5 for i in range(31)]
M={0.0:(.14,.3,.97,.97),0.5:(.15,.31,1,1),1.0:(.1,.04,1,1),1.5:(.1,.08,1,.97),2.0:(.22,.1,1,.68),2.5:(.32,.12,1,.7),
 3.0:(.39,.15,1,.82),3.5:(.57,.28,.95,.75),4.0:(.6,.28,.94,.6),4.5:(.62,.29,1,.68),5.0:(.42,.27,1,.97),5.5:(.82,.28,1,.63),
 6.0:(0,.24,.35,1),6.5:(.27,.42,1,.97),7.0:(.65,.55,1,1),7.5:(.35,.3,.63,.56),8.0:(.08,.3,.62,.6),8.5:(.52,.24,1,1),
 9.0:(.07,.27,.78,1),9.5:(.57,.29,1,.5),10.0:(.62,.12,1,.77),10.5:(.57,.07,1,1),11.0:(.67,.34,1,.8),11.5:(.09,.44,.95,.75),
 12.0:(.49,.41,1,.66),12.5:(.75,.52,1,.76),13.0:(.25,.29,.58,.55),13.5:(.19,.45,1,.75),14.0:(.57,.37,.93,.81),
 14.5:(.57,.37,.96,.83),15.0:(.6,.39,1,.95)}
km=keys(T,M)
dump({"mediaId":839,"level":"B","keyWord":"extend","defaultVoice":"male",
"taps":[{"phrase":"to extend a dining table","target":"the man","voice":"male","keys":km},
{"phrase":"to stretch out on a bench","target":"the man","voice":"male","keys":km},
{"phrase":"to spread his arms wide","target":"the man","voice":"male","keys":km}],
"stillS":14.5,
"nouns":[{"word":"a dining table","x":.35,"y":.56,"voice":"male"},{"word":"a bench","x":.68,"y":.76,"voice":"male"},
{"word":"a sweater","x":.78,"y":.54,"voice":"male"},{"word":"a ceiling","x":.50,"y":.12,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","extending","his","dining","table."],"answerVoice":"male",
"notes":"One target only: the man is the only actor and the table / bench always overlap him, so all three phrases are his. Many jump cuts. 5.5 s: only his arm and shoe at the right edge; 6.5 and 7.0 s: close-up of his hand under the table top (box on the hand and arm); 8.0 s: a cross-fade shows him twice, the box covers both figures; 12.5 s: only hands and a foot at the right edge. Arms spread at 9.5 s; lying on the bench 11.5-12.0 and 13.5 s. 'a sweater' pill sits on the man's chest at 14.5 s."})

# ---------- 840
M={0.0:(0,.35,.55,.92),0.5:(0,.33,.58,.92),1.0:(0,.34,.56,.93),1.5:(0,.29,.61,.94),2.0:(0,.12,.5,.9),2.5:(0,.02,.61,.91),
 3.0:(0,0,.7,1),4.0:(.1,.57,.78,1),4.5:(.22,.67,.98,1),5.0:(.22,.7,.85,1),5.5:(.12,.59,1,1),6.0:(.08,.59,.75,1),
 8.5:(0,.25,1,1),9.0:(0,.2,1,1),9.5:(0,.2,1,1),10.0:(0,.18,1,1),10.5:(0,.18,1,1),11.0:(0,.22,.93,1),
 13.0:(.12,.49,.63,.97),13.5:(.12,.49,.63,.97),14.0:(.12,.48,.62,.95),14.5:(0,.42,1,1),15.0:(0,.42,1,1)}
C={0.0:(.72,.57,1,.73),0.5:(.72,.57,1,.73),1.0:(.72,.57,1,.73),1.5:(.72,.57,1,.73),2.0:(.72,.57,1,.73),2.5:(.72,.57,1,.73),3.0:(.72,.57,1,.73)}
km,kc=keys(T,M),keys(T,C)
dump({"mediaId":840,"level":"B","keyWord":"hike","defaultVoice":"male",
"taps":[{"phrase":"to lace up his boots","target":"the man","voice":"male","keys":km},
{"phrase":"to perch on a ledge","target":"the man","voice":"male","keys":km},
{"phrase":"to be parked on gravel","target":"the car","voice":"male","keys":kc}],
"stillS":13.5,
"nouns":[{"word":"the sky","x":.50,"y":.12,"voice":"male"},{"word":"a valley","x":.50,"y":.42,"voice":"male"},
{"word":"a beanie","x":.33,"y":.57,"voice":"male"},{"word":"a backpack","x":.10,"y":.88,"voice":"male"}],
"question":"Where is the man hiking?","answer":["He","is","hiking","in","the","mountains."],"answerVoice":"male",
"notes":"Shots: boots by the chalet 0-3.0 s (3.5 s: lens covered, all off), POV on the forest trail 4.0-6.0 s (only his arm in the orange jacket is visible - the box is on the arm), landscape only 6.5-8.0 s and 11.5-12.5 s (off), selfie 8.5-11.0 s, sitting on the ledge 13.0-14.0 s, POV with the fruit box 14.5-15.0 s (legs, hands, boot). The car is only in the first shot. 'a backpack' sits at the left edge at 13.5 s (x 0-0.13), pill at x 0.10. The answer says 'in the mountains' (shown throughout), no place name."})
