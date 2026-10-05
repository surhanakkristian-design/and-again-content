import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
W={0.0:(0,0,1,0.92),0.5:(0,0,1,0.95),1.0:(0,0,1,0.95),1.5:(0,0,1,1),2.0:(0,0,1,0.92),2.5:(0,0,0.95,0.60),
   3.0:(0,0,0.82,0.67),3.5:(0.26,0,0.60,0.37),4.0:(0.29,0,0.62,0.28),4.5:(0.24,0,0.50,0.35),5.0:(0.29,0,0.69,0.57),5.5:(0.29,0.05,0.50,0.47),
   6.0:(0.07,0.10,0.65,0.45),6.5:(0.18,0.14,0.61,0.44),7.0:(0.16,0.17,0.60,0.44),7.5:(0.24,0.17,0.38,0.48),8.0:(0.11,0.20,0.75,0.42),8.5:(0.19,0.17,0.65,0.48),
   9.0:(0.29,0.14,0.55,0.69),9.5:(0.32,0.11,0.54,0.82),10.0:(0.30,0.04,0.54,0.84)}
F={8.5:(0.0,0.34,0.18,0.18),9.0:(0.10,0.31,0.18,0.24),9.5:(0.13,0.30,0.18,0.37),10.0:(0.10,0.27,0.19,0.21)}
c={"mediaId":401,"level":"A","keyWord":"ice skates","defaultVoice":"female",
 "taps":[
  {"phrase":"to tie her ice skates","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to hold her arms out","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to wear a green jacket","target":"the person in green","voice":"female","keys":keys(F)}],
 "stillS":10.0,
 "nouns":[{"word":"a hat","x":0.50,"y":0.13,"voice":"female"},{"word":"trees","x":0.82,"y":0.22,"voice":"female"},
          {"word":"a scarf","x":0.47,"y":0.36,"voice":"female"},{"word":"ice skates","x":0.50,"y":0.78,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","skating","on","the","ice."],
 "answerVoice":"female",
 "notes":"Two targets: the woman (0.0-4.5 only her hands, legs and skates are in the picture) and the person in the green jacket who appears behind her only from 8.5 s (small; gender not clear, so default voice; 'to wear a green jacket' is a state). The tiny far figures at 3.5-6.0 are not a target. From 9.0 the woman's left arm passes in front of the person in green: her box is cut at that arm."}
json.dump(c,open('content/401.json','w'),indent=1)
