import json
VID=5369
T=[i*0.5 for i in range(19)]
Y={0.0:0.02,0.5:0.04,1.0:0.03,1.5:0.02,2.0:0.13,2.5:0.09,3.0:0.12,3.5:0.14,4.0:0.11,4.5:0.09,5.0:0.12,5.5:0.03,6.0:0.09,6.5:0.02,7.0:0.12,7.5:0.12,8.0:0.16,8.5:0.07,9.0:0.08}
keys=[{"t":t,"x":0.0,"y":Y[t],"w":1.0,"h":round(1-Y[t],2)} for t in T]
c={"mediaId":VID,"level":"B","keyWord":"tough","defaultVoice":"male",
 "taps":[
  {"phrase":"to talk straight into the camera","target":"the boxer","voice":"male","keys":keys},
  {"phrase":"to catch his breath","target":"the boxer","voice":"male","keys":keys},
  {"phrase":"to wipe off the sweat","target":"the boxer","voice":"male","keys":keys}],
 "stillS":7.5,
 "nouns":[{"word":"a ceiling fan","x":0.76,"y":0.24,"voice":"male"},
          {"word":"a punchbag","x":0.74,"y":0.43,"voice":"male"},
          {"word":"a towel","x":0.3,"y":0.85,"voice":"male"},
          {"word":"a hand wrap","x":0.84,"y":0.87,"voice":"male"}],
 "question":"What is he doing with the towel?",
 "answer":["He","is","drying","his","hair","with","the","towel."],
 "answerVoice":"male",
 "notes":"One person fills the frame the whole clip; the other fighters are tiny, blurred and behind him, so all three phrases are about the boxer (box = whole width below his hair). 'to catch his breath' rests on the open mouth / hard breathing (description); 'to wipe off the sweat' = the towel at 8.0-9.0. Still 7.5: ceiling fan and black punchbag are blurred background but recognisable; towel bottom left, red hand wrap bottom right."}
json.dump(c,open(f'content/{VID}.json','w'),indent=1)
