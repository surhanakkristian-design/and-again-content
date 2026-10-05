import json
T=[i*0.5 for i in range(24)]
man={0.0:(0,.11,1,.89),0.5:(0,.06,1,.94),1.0:(0,.11,1,.89),1.5:(0,.2,1,.8),2.0:(0,.2,.97,.8),2.5:(0,.25,1,.72),3.0:(0,.27,1,.72),
3.5:(0,.27,.83,.71),4.0:(.18,.30,.70,.53),4.5:(.22,.30,.50,.54),5.0:(.1,.34,.85,.66),9.5:(.23,.36,.66,.58),10.0:(.2,.32,.7,.63),
10.5:(.2,.33,.68,.63),11.0:(.08,.29,.73,.71),11.5:(.08,.25,.76,.75)}
ro={0.0:(.03,0,.94,.11),0.5:(.08,0,.84,.06),1.0:(.03,0,.94,.11),1.5:(.03,0,.9,.2),2.0:(.03,0,.9,.2),2.5:(.05,0,.92,.25),3.0:(.08,0,.88,.27),
3.5:(.1,0,.85,.27),4.0:(.15,0,.85,.30),4.5:(.15,0,.85,.30),5.0:(.2,0,.8,.34),5.5:(.2,.03,.8,.97),6.0:(.15,.03,.85,.97),6.5:(.15,.03,.85,.97),
7.0:(.15,.03,.85,.97),7.5:(.15,.03,.85,.97),8.0:(.30,.08,.44,.80),8.5:(.30,.08,.44,.80),9.0:(.30,.08,.44,.80),9.5:(.2,0,.75,.36),
10.0:(.15,0,.8,.32),10.5:(.2,0,.75,.33),11.0:(.2,0,.75,.29),11.5:(.2,0,.78,.25)}
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
v="male"
o={"mediaId":4191,"level":"A","keyWord":"tower","defaultVoice":v,
"taps":[{"phrase":"to jump up and down","target":"the man","voice":v,"keys":keys(man)},
{"phrase":"to tower over the man","target":"the rocket","voice":v,"keys":keys(ro)},
{"phrase":"to raise both arms","target":"the man","voice":v,"keys":keys(man)}],
"stillS":8.5,
"nouns":[{"word":"the sky","x":.5,"y":.07,"voice":v},{"word":"a rocket","x":.52,"y":.32,"voice":v},
{"word":"the sun","x":.68,"y":.58,"voice":v},{"word":"a building","x":.27,"y":.77,"voice":v}],
"question":"What is the man doing?","answer":["He","is","jumping","in","front","of","a","rocket."],"answerVoice":v,
"notes":"The man stands in front of the rocket in every shot he is in, so the two overlap: the rocket box is the band ABOVE the man's head/hands (split along that line), which is very thin at 0.0-1.0 (0.06-0.11 high) because his hair almost reaches the top edge. 5.5-9.0 are rocket-only shots (man off). Key word 'tower' is a verb, used in the rocket phrase. Still 8.5 is the silhouette shot: the building is a dark silhouette at the lower left; the two palm trees are not used as nouns (two apart)."}
json.dump(o,open("content/4191.json","w"),indent=1)
