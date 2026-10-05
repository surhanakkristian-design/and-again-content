import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
W={0.0:(.26,.15,.43,.47),0.5:(.26,.21,.38,.5),1.0:(.18,.24,.48,.75),1.5:(.1,.14,.9,.86),2.0:(.15,.17,.72,.83),
   2.5:(.24,.22,.76,.78),3.0:(.17,.22,.66,.78),3.5:(.14,.27,.8,.73),4.0:(.02,.35,.78,.65),4.5:(.5,.37,.47,.63),
   5.0:(.23,.26,.77,.74),5.5:(.31,.12,.69,.88),6.0:(.26,.15,.72,.85),6.5:(.38,.33,.62,.67),7.0:(.38,.34,.62,.66),
   7.5:(.4,.34,.6,.66),8.0:(.39,.33,.61,.67),8.5:(.39,.33,.61,.67),9.0:(.39,.34,.61,.66)}
M={0.0:(.72,.56,.28,.3),0.5:(.65,.52,.35,.38),1.0:(.67,0.0,.33,1.0),5.0:(0.0,.5,.22,.5),5.5:(0.0,.37,.3,.63),6.0:(0.0,.33,.25,.67)}
c={"mediaId":5138,"level":"A","keyWord":"train","defaultVoice":"female",
 "taps":[
  {"phrase":"to sit by the window","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to wear an orange hat","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to help with the suitcase","target":"the man in uniform","voice":"male","keys":keys(M)}],
 "stillS":0.5,
 "nouns":[{"word":"a train","x":.22,"y":.12,"voice":"female"},{"word":"a hat","x":.46,"y":.28,"voice":"female"},
          {"word":"a ticket","x":.47,"y":.39,"voice":"female"},{"word":"a suitcase","x":.39,"y":.55,"voice":"female"}],
 "question":"Where is the woman sitting?","answer":["She","is","sitting","by","the","window."],"answerVoice":"female",
 "notes":"Woman gets on the train (0-1.0), corridor (1.5-4.0), lifts the suitcase to the rack (4.5-6.0), sits by the window (6.5-9.0). Man in uniform: only legs/hand at 0.0-0.5, head+arm at 1.0, foreground left at 5.0-6.0, off elsewhere; his box and the woman's are split where his arm reaches across her (1.0, 6.0). A bearded traveller at 4.0/5.0 is not a target. 'to sit by the window' is only true from 6.5. Still 0.5: train in the background behind the platform, ticket in her mouth."}
json.dump(c,open('content/5138.json','w'),indent=1)
