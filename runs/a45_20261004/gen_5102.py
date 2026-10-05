import json
T=[i*0.5 for i in range(25)]
def mk(d):
    ks=[]
    for t in T:
        b=d.get(t)
        if b: ks.append({"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
        else: ks.append({"t":t,"off":True})
    return ks
W={0.0:(.26,.22,.72,.93),0.5:(.27,.21,.70,.92),1.0:(.20,.17,.83,.89),1.5:(.34,.15,1,1),2.0:(.19,.17,1,1),2.5:(.19,.12,1,1),
   3.0:(.18,.14,1,1),3.5:(.14,.26,1,1),4.0:(.30,.25,.98,1),4.5:(.41,.27,.73,1),5.0:(.38,.31,.71,.96),5.5:(.39,.27,.81,.86),
   6.0:(.21,.28,.79,.85),6.5:(.18,.29,.71,.89),7.0:(.25,.27,.69,1),7.5:(.14,.29,.79,1),8.0:(.31,.25,.79,.99),8.5:(.31,.26,.67,.89),
   9.0:(.29,.26,.66,.99),9.5:(.29,.29,.66,.94),10.0:(.32,.32,.79,1),10.5:(.35,.35,.89,.97),11.0:(.25,.36,1,1),11.5:(.19,.39,1,1),12.0:(0,.31,1,1)}
S={4.5:(.31,.29,.41,.54),5.0:(.10,.31,.38,.75)}
c={"mediaId":5102,"level":"B","keyWord":"alley","defaultVoice":"female",
 "taps":[
  {"phrase":"to squeeze past a man","target":"the woman","voice":"female","keys":mk(W)},
  {"phrase":"to punch the air","target":"the woman","voice":"female","keys":mk(W)},
  {"phrase":"to wear dark sunglasses","target":"the man in sunglasses","voice":"male","keys":mk(S)}],
 "stillS":5.0,
 "nouns":[{"word":"a lantern","x":0.42,"y":0.12,"voice":"female"},{"word":"an awning","x":0.70,"y":0.22,"voice":"female"},
          {"word":"a backpack","x":0.53,"y":0.58,"voice":"female"},{"word":"an alley","x":0.55,"y":0.82,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","squeezing","past","a","man","in","the","alley."],
 "answerVoice":"female",
 "notes":"The man in sunglasses is visible only 4.5-5.0 (at 4.0 he is mostly hidden behind her head -> off); at 4.5 his box is narrow (0.10 wide) because she walks right next to him, split at x 0.40. 'to punch the air' = her fist pump at 11.5-12.0. 'an alley' pill sits on the paving of the narrow lane at the still. Other people (man in maroon ahead 0.5-2.5, man in red 9.0-10.5) walk too, so no walking phrase. The model answer is true at 4.5-5.0 only; the question could also be answered with 'She is checking a map on her phone.'"}
json.dump(c,open('content/5102.json','w'),indent=1)
