import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":round(w,2),"h":round(h,2)})
        else: out.append({"t":t,"off":True})
    return out
M={0.0:(0,0,.88,.57),0.5:(0,0,.88,.57),1.0:(0,0,.82,.59),1.5:(0,0,.82,.59),2.0:(0,0,.78,.61),2.5:(0,0,.82,.63),
3.0:(0,0,.78,.67),3.5:(0,0,.78,.70),4.0:(0,0,.76,.71),4.5:(0,0,.76,.73),5.0:(0,0,.68,.77),5.5:(0,.08,.74,.92),
6.0:(0,.10,.58,.68),6.5:(0,.17,.62,.61),7.0:(0,.19,.58,.59),7.5:(0,.24,.58,.55),8.0:(0,.28,.66,.50),8.5:(0,.17,.66,.61),
9.0:(0,.27,.50,.73),9.5:(0,.31,.50,.69),10.0:(0,.32,.47,.68)}
C={0.0:(.50,.57,.50,.43),0.5:(.50,.57,.50,.43),1.0:(.47,.59,.53,.41),1.5:(.50,.59,.50,.41),2.0:(.50,.61,.50,.39),2.5:(.50,.63,.50,.37),
3.0:(.48,.67,.52,.33),3.5:(.50,.70,.50,.30),4.0:(.50,.71,.50,.29),4.5:(.50,.73,.50,.27),5.0:(.47,.77,.53,.23),5.5:(.74,.76,.26,.24),
6.0:(.50,.78,.50,.22),6.5:(.52,.78,.48,.22),7.0:(.50,.78,.50,.22),7.5:(.50,.79,.50,.21),8.0:(.50,.78,.50,.22),8.5:(.50,.78,.50,.22),
9.0:(.50,.79,.50,.21),9.5:(.50,.79,.50,.21),10.0:(.48,.78,.52,.22)}
c={"mediaId":490,"level":"A","keyWord":"musician","defaultVoice":"male",
"taps":[
{"phrase":"to play the guitar","target":"the musician","voice":"male","keys":keys(M)},
{"phrase":"to sing a song","target":"the musician","voice":"male","keys":keys(M)},
{"phrase":"to have coins inside","target":"the guitar case","voice":"male","keys":keys(C)}],
"stillS":7.0,
"nouns":[{"word":"a musician","x":.20,"y":.50,"voice":"male"},{"word":"a guitar","x":.38,"y":.75,"voice":"male"},
{"word":"a baby","x":.48,"y":.26,"voice":"male"},{"word":"coins","x":.80,"y":.94,"voice":"male"}],
"question":"What is the musician doing?",
"answer":["He","is","playing","the","guitar."],
"answerVoice":"male",
"notes":"Only two tap targets: the people in the crowd (man holding a baby, two girls filming) sit in the empty corner of the musician's bounding box, so a box for them would overlap his; filming is done by two people anyway. Musician and case are split horizontally at the case's top edge: the bottom of the guitar body / his boots below that line (left of the case) are in no box, and at 5.5 s the split is vertical. At 0-3.5 s only his hands, jacket and guitar are visible; singing is visible from about 5.0 s (mouth open, head back at 8.0-8.5 s). 'to have coins inside' is a state. Clapping in the crowd is hardly visible, not used."}
json.dump(c,open("content/490.json","w"),indent=1,ensure_ascii=False)
