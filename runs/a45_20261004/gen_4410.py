import json
T=[i*0.5 for i in range(19)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":round(v[2]-v[0],2),"h":round(v[3]-v[1],2)})
    return out
F=(0,0,1,1)
man={0.0:F,0.5:F,1.0:F,1.5:(0,0,.46,1),2.0:(0,0,.46,1),2.5:(0,0,.46,1),4.5:(0,0,.50,.85),
 5.5:(0,.08,.42,1),6.0:(0,.08,.42,1),6.5:(0,.06,.42,1),7.0:(0,.06,.34,1),7.5:(0,.09,.20,.75),8.5:F,9.0:F}
wom={1.5:(.50,0,1,.86),2.0:(.50,0,1,.86),2.5:(.50,0,1,.86),5.0:(.58,.08,1,1)}
bag={1.5:(.80,.87,1,1),2.0:(.80,.87,1,1),2.5:(.80,.87,1,1),5.5:(.70,.85,1,1),6.0:(.70,.74,1,.95),6.5:(.70,.75,1,.96),
 7.0:(.68,.76,1,.97),7.5:(.66,.77,1,.97),8.0:(.62,.79,1,.97)}
c={"mediaId":4410,"level":"A","keyWord":"contest","defaultVoice":"male",
 "taps":[
  {"phrase":"to look at the camera","target":"the man in front","voice":"male","keys":K(man)},
  {"phrase":"to cover her face","target":"the woman with the ring","voice":"female","keys":K(wom)},
  {"phrase":"to lie on the sofa","target":"the big bag of chips","voice":"male","keys":K(bag)}],
 "stillS":8.0,
 "nouns":[{"word":"a plant","x":.50,"y":.23,"voice":"male"},{"word":"pillows","x":.62,"y":.42,"voice":"male"},
          {"word":"socks","x":.54,"y":.93,"voice":"male"}],
 "question":"What are the friends doing?",
 "answer":["They","are","looking","into","each","other's","eyes."],
 "answerVoice":"male",
 "notes":"Many cuts and many faces; identities across shots are my reading. 'The man in front' = the man with brown wavy hair and a light-blue shirt whose eye fills the frame at 0-1 s and 8.5-9 s (only he looks at the camera); I also boxed him at 1.5-2.5 s (left face), 4.5 s (left face), 5.5-7 s (big face on the left) and 7.5 s (far left, laughing) - 7.5 s is the least certain. 'The woman with the ring' covers her face at 5.0 s; the fair woman at 1.5-2.5 s is taken to be her (ring hand visible at the bottom); the blonde woman in the background of 5.5-8 s is NOT boxed (not sure she is the same). The bag: yellow bag on the brown sofa arm (5.5-8 s) and the yellow corner at 1.5-2.5 s; the blue-topped bag at 3-4 s is not boxed; 'sofa' is my reading of the brown cushion. The pair at 3-4 s has no target. Key word 'contest' is not in the texts: 'a staring contest' seemed above level A - verifier may prefer the answer 'They are having a staring contest.' Only 3 nouns; 'pillows' pill lies close to the small bags on the table."}
json.dump(c,open('content/4410.json','w'),indent=1,ensure_ascii=False)
