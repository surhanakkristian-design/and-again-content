import json
T=[i*0.5 for i in range(10)]
def keys(d):
    return [{"t":t,"x":d[t][0],"y":d[t][1],"w":round(d[t][2]-d[t][0],2),"h":round(d[t][3]-d[t][1],2)} for t in T]
W={0.0:(.42,.16,.90,1),0.5:(.42,.16,.94,1),1.0:(.39,.18,.92,1),1.5:(.39,.17,.94,1),2.0:(.40,.15,.95,1),2.5:(.41,.14,.97,1),3.0:(.39,.15,.95,1),3.5:(.40,.14,1,1),4.0:(.41,.13,1,1),4.5:(.42,.13,1,1)}
A={t:(0,.30,round(W[t][0]-.01,2),.63) for t in T}
A[4.0]=(0,.32,.40,.67);A[4.5]=(0,.32,.41,.67)
kw,ka=keys(W),keys(A)
c={"mediaId":831,"level":"B","keyWord":"speech","defaultVoice":"female",
"taps":[{"phrase":"to deliver a speech","target":"the woman","voice":"female","keys":kw},
{"phrase":"to gesture with one hand","target":"the woman","voice":"female","keys":kw},
{"phrase":"to listen to the speaker","target":"the audience","voice":"female","keys":ka}],
"stillS":4.5,
"nouns":[{"word":"the audience","x":.20,"y":.40,"voice":"female"},{"word":"a microphone","x":.25,"y":.53,"voice":"female"},
{"word":"a lectern","x":.25,"y":.74,"voice":"female"},{"word":"a blazer","x":.72,"y":.56,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","delivering","a","speech","to","the","audience."],"answerVoice":"female",
"notes":"Two targets: the speaker and the (blurred) seated audience. The audience box covers only the crowd left of the woman above the lectern (a few people right of her at the frame edge are inside her box). Her hand resting on the lectern reaches left out of her box. The microphone stem crosses the audience area, so the 'a microphone' pill sits on the stem over the crowd, 0.13 below 'the audience'. 'a lectern' = the wooden stand (the description calls it a podium). She gestures 0-3.5 s and folds her hands at 4.0-4.5 s."}
json.dump(c,open('content/831.json','w'),indent=1)
