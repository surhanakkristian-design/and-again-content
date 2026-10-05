import json
T=[i*0.5 for i in range(19)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":round(v[2]-v[0],2),"h":round(v[3]-v[1],2)})
    return out
cream={0.0:(0,.21,1,1),0.5:(.10,.19,1,1),1.0:(0,.26,.98,1),1.5:(.15,.22,1,1),2.0:(0,0,1,1),
 4.0:(0,.22,1,1),4.5:(.25,.24,1,1),5.0:(.40,.25,.78,1),5.5:(.25,.28,.56,1),6.0:(.19,.30,.38,.83),
 6.5:(0,.27,.27,.76),7.0:(0,.28,.24,.78),7.5:(0,.26,.30,.74),8.0:(0,.28,.29,.76),8.5:(0,.27,.30,.75),9.0:(.02,.29,.28,.74)}
pin={2.5:(.40,.27,.66,.43),3.0:(.45,.23,.75,.42),3.5:(.41,.25,.73,.44)}
gar={2.5:(.50,.44,.76,.68),3.0:(.33,.43,.66,.95),3.5:(.25,.45,.56,.98)}
c={"mediaId":4409,"level":"B","keyWord":"blind","defaultVoice":"female",
 "taps":[
  {"phrase":"to stumble through the doorway","target":"the woman in the cream top","voice":"female","keys":K(cream)},
  {"phrase":"to dangle from a rope","target":"the piñata","voice":"female","keys":K(pin)},
  {"phrase":"to grip a wooden stick","target":"the woman in the garden","voice":"female","keys":K(gar)}],
 "stillS":0.0,
 "nouns":[{"word":"a blindfold","x":.58,"y":.31,"voice":"female"},{"word":"balloons","x":.85,"y":.08,"voice":"female"},
          {"word":"streamers","x":.24,"y":.08,"voice":"female"},{"word":"jeans","x":.60,"y":.80,"voice":"female"}],
 "question":"What are the friends wearing?",
 "answer":["They","are","wearing","rainbow","blindfolds","over","their","eyes."],
 "answerVoice":"female",
 "notes":"Three shots: doorway (0-1.5 s), close-up (2.0 s), garden (2.5-3.5 s), living room (4-9 s). The woman in the cream top is tracked through the living room: 2.0 s close-up assumed to be her (whole frame); at 6.0 s she is mostly hidden behind the woman in the brown jacket (small box on her visible part); from 6.5 s she is the woman at the far left. 'to stumble': she lurches forward through the patio door with her arms out - verifier may prefer 'to step'. The garden woman wears a pink top like a woman indoors, so she is named by place. The key word 'blind' is only reflected by 'blindfold(s)'."}
json.dump(c,open('content/4409.json','w'),indent=1,ensure_ascii=False)
