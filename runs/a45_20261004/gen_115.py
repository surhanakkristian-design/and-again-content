import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
    return out
W={0.0:(.27,.32,.63,.90),0.5:(.17,.24,.62,.74),1.0:(0,.15,.50,.87),1.5:(0,.14,.60,.82),2.0:(0,.12,.68,.74),2.5:(.08,.12,1,.73),
   3.0:(.08,.22,1,.86),6.5:(0,.13,.24,.82),7.0:(0,.26,.24,.90),7.5:(0,.28,.30,.90),8.0:(0,.28,.28,.90),8.5:(0,.28,.29,.90),
   9.0:(0,.28,.26,.90),9.5:(0,.26,.22,.90),10.0:(0,.48,.52,.88)}
M={0.5:(.66,.26,1,.70),1.0:(.50,.14,.83,.76),1.5:(.60,.07,1,.76),2.0:(.68,.34,1,.70),6.5:(.68,.11,1,.72),7.0:(.58,.28,1,.84),
   7.5:(.55,.30,1,.86),8.0:(.55,.28,1,.82),8.5:(.58,.26,1,.82),9.0:(.50,.26,1,.88),9.5:(.52,.28,1,.90),10.0:(.52,.45,1,.90)}
R={6.0:(.20,.09,.40,.24),6.5:(.24,.23,.44,.38),7.0:(.24,.33,.44,.47),7.5:(.30,.35,.48,.49),8.0:(.28,.35,.46,.49),8.5:(.29,.35,.47,.49),
   9.0:(.26,.34,.46,.48),9.5:(.22,.35,.42,.49),10.0:(.21,.34,.41,.48)}
c={"mediaId":115,"level":"A","keyWord":"breakfast","defaultVoice":"male",
 "taps":[{"phrase":"to break an egg","target":"the woman","voice":"female","keys":keys(W)},
         {"phrase":"to eat toast with egg","target":"the man","voice":"male","keys":keys(M)},
         {"phrase":"to stand on the fence","target":"the rooster","voice":"male","keys":keys(R)}],
 "stillS":8.0,
 "nouns":[{"word":"a tree","x":.50,"y":.20,"voice":"male"},{"word":"a fence","x":.48,"y":.52,"voice":"male"},
          {"word":"toast","x":.38,"y":.77,"voice":"male"},{"word":"milk","x":.86,"y":.83,"voice":"male"}],
 "question":"What are they doing?","answer":["They","are","eating","breakfast","in","the","garden."],"answerVoice":"male",
 "notes":"defaultVoice male: a couple (mixed), evenId false. Woman breaks the egg at 1.0-2.0 s; man eats the egg toast at 6.5-8.0 s. Rooster is small (on the fence, 6.0-10.0 s). In the kitchen shots (1.0-2.0 s) man stands behind the woman: boxes split along a vertical line. At 9.0-10.0 s the woman's arm with the glass crosses the rooster: her box is cut (9.0/9.5 head+body only, 10.0 arm+body only, head sliver left out). Close-ups 3.5-5.5 s show only food/hands: all off. Key word breakfast is not placed as a noun (it would cover toast/milk); it is in the answer. Several toasts on the table at 8.0 s - pill sits on the front one."}
json.dump(c,open("content/115.json","w"),indent=1)
