import json
T=[i*0.5 for i in range(21)]
def C(b): return [{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t in T]
d={"mediaId":4065,"level":"A","keyWord":"driver","defaultVoice":"male",
"taps":[
 {"phrase":"to sit in the driver's seat","target":"the white dog","voice":"male","keys":C((0.50,0.22,0.50,0.60))},
 {"phrase":"to show its tongue","target":"the brown dog","voice":"male","keys":C((0.0,0.34,0.27,0.38))},
 {"phrase":"to hide behind a seat","target":"the raccoon","voice":"male","keys":C((0.28,0.28,0.18,0.14))}],
"stillS":4.0,
"nouns":[{"word":"trees","x":0.75,"y":0.06,"voice":"male"},{"word":"a driver","x":0.72,"y":0.38,"voice":"male"},{"word":"a cat","x":0.46,"y":0.50,"voice":"male"},{"word":"a steering wheel","x":0.78,"y":0.62,"voice":"male"}],
"question":"Who is sitting in the driver's seat?",
"answer":["A","white","dog","is","sitting","in","the","driver's","seat."],
"answerVoice":"male",
"notes":"Static shot with a slight sway, so the boxes are constant. Brown dog's box stops at x 0.27 (its front paw reaches a little further right) so it does not touch the raccoon's box. The raccoon's head shows above/behind the red seat ('to hide behind a seat'); 'raccoon' itself is not an A-level word but is only the target name. 'a driver' pill is on the white dog (key word); no 'a dog' noun because there are two dogs."}
json.dump(d,open("content/4065.json","w"),indent=1)
