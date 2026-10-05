import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
hen={0.0:(.13,.17,.75,.60),0.5:(.10,.16,.71,.56),1.0:(.14,.21,.73,.57),1.5:(.10,.20,.63,.53),2.0:(.17,.28,.65,.52),2.5:(0,.20,.97,.54),
3.0:(.05,.31,.49,.42),3.5:(0,.12,.83,.64),4.0:(0,.08,.84,.69),4.5:(0,.08,.80,.69),5.0:(.05,.10,.87,.64),5.5:(.06,.15,.79,.65),
6.0:(.07,.16,.78,.66),6.5:(.10,.13,.77,.66),7.0:(0,0,1,.60),8.5:(0,.77,.19,.23),9.0:(.38,.86,.38,.14),9.5:(.24,.70,.70,.30),10.0:(.38,.68,.57,.32)}
woman={8.5:(0,0,1,.77),9.0:(0,0,1,.86),9.5:(0,0,1,.70),10.0:(0,0,1,.68)}
c={"mediaId":160,"level":"B","keyWord":"nest","defaultVoice":"female",
"taps":[
 {"phrase":"to peck at the grain","target":"the hen","voice":"female","keys":keys(hen)},
 {"phrase":"to settle into the nest","target":"the hen","voice":"female","keys":keys(hen)},
 {"phrase":"to carry a wicker basket","target":"the woman","voice":"female","keys":keys(woman)}],
"stillS":7.0,
"nouns":[{"word":"a hen","x":.32,"y":.33,"voice":"female"},{"word":"an egg","x":.48,"y":.67,"voice":"female"},
 {"word":"a nest","x":.72,"y":.77,"voice":"female"},{"word":"a plank","x":.40,"y":.88,"voice":"female"}],
"question":"What is the hen doing?",
"answer":["The","hen","is","settling","into","the","nest."],
"answerVoice":"female",
"notes":"Two phrases share the hen: the egg and the basket were not used as tap targets because they sit inside the woman's outline (egg in her hand, basket on her arm) and an egg phrase ('to lie in the straw') would also fit the sitting hen. Hen pecks only 0.0-0.5, settles 4.0-6.5. In the last shot (8.5-10.0) the hen stands in front of the woman's skirt: the woman's box stops above the hen's box. Hen off at 7.5-8.0 (only egg and straw). Noun 'a nest' is placed on the straw ring right of the egg; 'a plank' = wooden front board of the coop."}
json.dump(c,open("content/160.json","w"),indent=1)
