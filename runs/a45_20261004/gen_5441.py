import json
T=[i*0.5 for i in range(19)]
def K(d):
    return [({"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3])) for t in T]
cm={0.0:(.03,.23,.50,.74),0.5:(.43,.13,.56,.64),1.0:(.38,.11,.62,.80),1.5:(.03,.10,.46,.68),2.0:(.58,.10,.42,.67),
2.5:(.12,.17,.36,.31),3.0:(.10,.23,.39,.26),3.5:(.08,.22,.42,.26),4.0:(.36,.25,.64,.38),4.5:(.47,.27,.53,.36),
5.0:(.50,.27,.50,.37),5.5:(.50,.33,.50,.30),6.0:(.55,.44,.45,.18),6.5:(.58,.46,.42,.17),7.0:(.43,.46,.53,.18),
7.5:(.45,.46,.53,.17),8.0:(.68,.38,.24,.19),8.5:(.72,.28,.21,.26),9.0:(.74,.33,.22,.24)}
girl={2.5:(.48,.47,.42,.53),3.0:(.49,.48,.40,.52),3.5:(.50,.49,.42,.51),4.0:(0,.24,.36,.64),4.5:(0,.25,.47,.63),
5.0:(0,.25,.50,.66),5.5:(0,.26,.50,.65),6.0:(0,.26,.55,.60),6.5:(0,.25,.58,.62),7.0:(0,.19,.30,.64),7.5:(0,.28,.30,.56)}
bm={2.5:(.49,.13,.48,.34),3.0:(.50,.12,.48,.36),3.5:(.50,.12,.48,.36),8.0:(.24,.12,.44,.86)}
c={"mediaId":5441,"level":"A","keyWord":"uncle","defaultVoice":"male",
"taps":[{"phrase":"to push a wheelbarrow","target":"the man in the colourful shirt","voice":"male","keys":K(cm)},
{"phrase":"to push his arm down","target":"the girl in pink","voice":"female","keys":K(girl)},
{"phrase":"to cook meat on the grill","target":"the man in the blue T-shirt","voice":"male","keys":K(bm)}],
"stillS":4.0,
"nouns":[{"word":"a girl","x":0.12,"y":0.48,"voice":"female"},{"word":"a man","x":0.74,"y":0.48,"voice":"male"},
{"word":"marshmallows","x":0.42,"y":0.72,"voice":"male"},{"word":"trees","x":0.60,"y":0.12,"voice":"male"}],
"question":"Who is sitting in the wheelbarrow?","answer":["A","boy","is","sitting","in","the","wheelbarrow."],"answerVoice":"male",
"notes":"Key word 'uncle' is not placed as a noun (a relationship cannot be seen). Overlaps at 2.5-3.5 s (colourful-shirt man behind the girls, blue T-shirt man behind the girl in pink) are split horizontally at the girls' heads. Arm-wrestling shots 4-7.5 s split vertically at the clasped hands. 8.0 s: the big man carrying a girl in the foreground is taken to be the blue T-shirt man (blue T-shirt, grey shorts); 8.5/9.0 s off for him and the girl in pink because the small background figures cannot be told apart. The colourful-shirt man is the small figure on the right 8.0-9.0 s (8.5/9.0 with a child on his shoulders). 'to cook meat on the grill' rests on 2.5-3.5 s only (meat on the grill visible at the right)."}
json.dump(c,open('content/5441.json','w'),indent=1)
