import json
T=[i*0.5 for i in range(9)]
S={0.0:.76,0.5:.75,1.0:.75,1.5:.76,2.0:.77,2.5:.77,3.0:.78,3.5:.78,4.0:.78}
BX={0.0:(.07,.90),0.5:(.07,.97),1.0:(.07,.90),1.5:(.05,.98),2.0:(.04,.91),2.5:(.02,.93),3.0:(.01,.93),3.5:(.01,.93),4.0:(.01,.93)}
g=[{"t":t,"x":0.0,"y":0.0,"w":.90,"h":S[t]} for t in T]
b=[{"t":t,"x":BX[t][0],"y":S[t],"w":round(BX[t][1]-BX[t][0],2),"h":round(1-S[t],2)} for t in T]
c={"mediaId":537,"level":"A","keyWord":"peel","defaultVoice":"female",
 "taps":[{"phrase":"to peel a red apple","target":"the girl","voice":"female","keys":g},
         {"phrase":"to use a small knife","target":"the girl","voice":"female","keys":g},
         {"phrase":"to stand on the floor","target":"the basket","voice":"female","keys":b}],
 "stillS":4.0,
 "nouns":[{"word":"an apple","x":.58,"y":.24,"voice":"female"},{"word":"a basket","x":.45,"y":.94,"voice":"female"},
          {"word":"a tree","x":.86,"y":.73,"voice":"female"},{"word":"clouds","x":.72,"y":.09,"voice":"female"}],
 "question":"What is the girl doing?",
 "answer":["She","is","peeling","a","red","apple."],"answerVoice":"female",
 "notes":"Only two real tap targets (girl, basket); the girl has two phrases. The girl is shown from the chin down and fills the left/upper picture; her skirt reaches down to the basket handle, so the boxes are split at the handle's top. Basket phrase is a state (no action fits it). At the still (4.0 s) the apple is already peeled (pale); 'a tree' is the one large apple tree bottom right, far trees are small."}
json.dump(c,open('content/537.json','w'),indent=1)
