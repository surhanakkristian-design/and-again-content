import json
T=[i*0.5 for i in range(19)]
def keys(lst):
    out=[]
    for t,b in zip(T,lst):
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
W=[(0,.40,.24,.60),(0,.38,.38,.62),(0,.62,.66,.38),(0,.62,.70,.38),(0,.70,.62,.30),(0,.40,.50,.60),
   (0,.24,.34,.76),(0,.24,.43,.76),(.08,.17,.76,.60),(.13,.24,.74,.58),(0,.30,.36,.70),(0,.30,.50,.70),
   (0,.32,.52,.68),(0,.33,.52,.67),(0,.34,.49,.66),(0,.34,.52,.66),(0,.36,.48,.64),(0,.36,.50,.64),(0,.34,.42,.66)]
P=[(.24,.49,.20,.15),(.38,.47,.18,.14),(.34,.40,.32,.22),(.41,.40,.27,.22),(.26,.50,.34,.20),(.50,.44,.22,.18),
   (.55,.50,.24,.24),(.58,.49,.24,.23),None,None,(.36,.33,.62,.58),(.50,.30,.45,.55),
   (.52,.32,.44,.52),(.52,.32,.44,.53),(.49,.34,.47,.52),(.52,.34,.44,.52),(.48,.36,.46,.50),(.50,.36,.44,.50),(.46,.35,.48,.53)]
c={"mediaId":5048,"level":"B","keyWord":"shut","defaultVoice":"female",
 "taps":[
  {"phrase":"to fiddle with the key","target":"the old woman","voice":"female","keys":keys(W)},
  {"phrase":"to hold a ripe watermelon","target":"the old woman","voice":"female","keys":keys(W)},
  {"phrase":"to dangle from the handles","target":"the padlock","voice":"female","keys":keys(P)}],
 "stillS":6.0,
 "nouns":[{"word":"a headscarf","x":0.22,"y":0.40,"voice":"female"},
          {"word":"a hinge","x":0.58,"y":0.22,"voice":"female"},
          {"word":"a padlock","x":0.72,"y":0.70,"voice":"female"},
          {"word":"a bunch of keys","x":0.22,"y":0.80,"voice":"female"}],
 "question":"What is the old woman doing?",
 "answer":["She","is","fiddling","with","a","huge","padlock."],
 "answerVoice":"female",
 "notes":"Two padlocks: a small black one (0.0-3.5) and a giant wooden one (5.0-9.0), both 'the padlock'; 4.0-4.5 is the watermelon shot (padlock off). Her hands grip the padlock in many frames, so woman/padlock boxes are split side by side and her hands/arms fall partly into the padlock box (1.0-2.5, 5.0, 7.5-8.5). Doors are ajar at 0.0, so 'shut' is not used in the answer; doors not used as a target (would overlap everything)."}
json.dump(c,open('content/5048.json','w'),indent=1)
