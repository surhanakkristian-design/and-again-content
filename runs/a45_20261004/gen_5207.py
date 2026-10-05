import json
T=[i*0.5 for i in range(21)]
def K(d):
    out=[]
    for t in T:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=b; x0=max(0,x0);y0=max(0,y0);x1=min(1,x1);y1=min(1,y1)
            out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
W={0.0:(.27,.49,.96,1),0.5:(.28,.54,1,1),1.0:(.25,.60,1,1),1.5:(.30,.67,1,1),2.0:(.50,.69,1,1),2.5:(.71,.72,1,1),
3.0:(.81,.86,1,1),7.5:(.88,.79,1,.95),8.0:(.71,.63,1,.78),8.5:(.56,.64,1,.88),9.0:(.46,.64,1,.99),9.5:(.24,.64,1,1),10.0:(.12,.64,1,1)}
C={2.0:(0,.19,.42,.93),2.5:(.19,.31,.70,.92),3.0:(.34,.44,.80,.93),3.5:(.46,.40,.92,.93),4.0:(.62,.42,1,.94),4.5:(.70,.42,1,.94),
5.0:(.72,.40,1,.55),5.5:(.78,.40,1,.80),6.0:(.76,.39,1,.82),6.5:(.70,.38,1,.85),7.0:(.62,.39,1,.88),7.5:(.52,.38,.88,.88),
8.0:(.25,.38,.71,.88),8.5:(.06,.39,.56,.84),9.0:(0,.41,.46,.89),9.5:(0,.50,.24,.88),10.0:(0,.64,.12,.88)}
B={3.5:(0,.08,.46,1),4.0:(0,.05,.62,1),4.5:(0,.23,.70,1),5.0:(0,.55,1,1),5.5:(.06,.47,.78,1),6.0:(.05,.53,.76,1),
6.5:(0,.64,.70,1),7.0:(0,.67,.62,1),7.5:(0,.71,.52,1),8.0:(0,.77,.25,1),8.5:(0,.84,.28,1)}
c={"mediaId":5207,"level":"B","keyWord":"sweat","defaultVoice":"male",
"taps":[{"phrase":"to sprawl on a wooden bench","target":"the woman","voice":"female","keys":K(W)},
{"phrase":"to gulp water from a bottle","target":"the man in the cap","voice":"male","keys":K(C)},
{"phrase":"to lean on trekking poles","target":"the bearded man","voice":"male","keys":K(B)}],
"stillS":10.0,
"nouns":[{"word":"peaks","x":.45,"y":.22,"voice":"male"},{"word":"a meadow","x":.70,"y":.55,"voice":"male"},
{"word":"a bench","x":.33,"y":.72,"voice":"male"},{"word":"a water bottle","x":.15,"y":.83,"voice":"male"}],
"question":"What is the bearded man holding?","answer":["He","is","holding","two","trekking","poles."],"answerVoice":"male",
"notes":"The packet description does not match the picture: there are THREE hikers - a woman in a red jacket sprawled on a bench (holding a water bottle), a shirtless young man in a cap with a blue backpack who sits on a rock and drinks (6.5-8.5), and a shirtless bearded man with two trekking poles who leans on them (3.5-5.5) and then lies in the grass. defaultVoice male (mixed group, evenId false). Several splits where they overlap: at 4.0-4.5 the bearded man's pole hand reaches into the cap man's box; at 2.5, 8.0, 8.5, 9.0 the woman's bottle hand / the cap man's boots are cut at the split; at 5.0 the cap man is only head/chest above the bearded man's arm. Woman off 3.5-7.0 (only a hand at the edge at 3.5), bearded man off from 9.0 (a sliver of hand). Key word sweat is not a placeable noun."}
json.dump(c,open('content/5207.json','w'),indent=1)
