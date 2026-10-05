import json
T=[i*0.5 for i in range(21)]
top={0.0:(.10,.14),0.5:(.08,.12),1.0:(0,.08),1.5:(0,.10),2.0:(0,.04),2.5:(0,.09),3.0:(0,.10),3.5:(0,.03),4.0:(0,.08),4.5:(0,.09),
     5.0:(0,.10),5.5:(.18,.14),6.0:(.20,.12),6.5:(.25,.24),7.0:(.08,.32),7.5:(.12,.46),8.0:(.20,.37),8.5:(.26,.29),9.0:(.28,.29),9.5:(.18,.26),10.0:(.14,.21)}
keys=[{"t":t,"x":top[t][0],"y":top[t][1],"w":round(1-top[t][0],2),"h":round(1-top[t][1],2)} for t in T]
c={"mediaId":5101,"level":"B","keyWord":"nausea","defaultVoice":"female",
 "taps":[
  {"phrase":"to grip the handrail","target":"the woman","voice":"female","keys":keys},
  {"phrase":"to feel seasick","target":"the woman","voice":"female","keys":keys},
  {"phrase":"to slump onto a bench","target":"the woman","voice":"female","keys":keys}],
 "stillS":8.0,
 "nouns":[{"word":"passengers","x":0.72,"y":0.30,"voice":"female"},{"word":"the sea","x":0.14,"y":0.35,"voice":"female"},
          {"word":"a bench","x":0.15,"y":0.58,"voice":"female"},{"word":"a plait","x":0.66,"y":0.60,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","clamping","her","hands","over","her","mouth."],
 "answerVoice":"female",
 "notes":"Only one real target: the blonde woman fills the frame; the passengers in the background are tiny and do nothing distinctive, so all three phrases use her. 'to grip the handrail' is shown 0-1.5 (hand on the rail), 'to slump onto a bench' 7.0-7.5 (she sits down). 'to feel seasick' is a state but the whole clip shows it (ferry, hands over mouth). Question could also be answered with 'She is covering her mouth.' - model answer uses 'clamping' for B level."}
json.dump(c,open('content/5101.json','w'),indent=1)
