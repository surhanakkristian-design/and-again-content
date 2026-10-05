import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
boy={0.0:(.14,.12,.78,.68),0.5:(.08,.09,.90,.72),1.0:(.07,.09,.86,.82),1.5:(.09,.09,.89,.82),2.0:(.11,.20,.80,.58),2.5:(.11,.28,.82,.50),3.0:(.11,.28,.82,.60),3.5:(.10,.29,.83,.59),4.0:(.10,.29,.83,.49),4.5:(.10,.29,.83,.49),5.0:(.10,.27,.83,.61),5.5:(.10,.29,.83,.59),6.0:(0,0,1,1),6.5:(0,0,1,1),7.0:(.34,.47,.32,.42),7.5:(.34,.47,.32,.42),8.0:(.32,.47,.34,.31),8.5:(.32,.47,.34,.31),9.0:(.34,.47,.32,.42),9.5:(.34,.47,.32,.42),10.0:(.35,.47,.31,.31)}
k=keys(boy)
c={"mediaId":453,"level":"A","keyWord":"lonely","defaultVoice":"male",
"taps":[
 {"phrase":"to eat green peas","target":"the boy","voice":"male","keys":k},
 {"phrase":"to hold a fork","target":"the boy","voice":"male","keys":k},
 {"phrase":"to sit alone","target":"the boy","voice":"male","keys":k}],
"stillS":4.0,
"nouns":[{"word":"a boy","x":.50,"y":.57,"voice":"male"},{"word":"peas","x":.64,"y":.735,"voice":"male"},{"word":"a phone","x":.18,"y":.77,"voice":"male"},{"word":"windows","x":.82,"y":.40,"voice":"male"}],
"question":"What is the boy eating?",
"answer":["He","is","eating","green","peas","alone."],
"answerVoice":"male",
"notes":"Only one person in the clip, so all three phrases share the boy. Key word 'lonely' is an adjective; 'alone' is used in a phrase and the answer instead. In the wide shot (7.0-10.0) he is small. 'windows' is the group of windows on the right."}
json.dump(c,open("content/453.json","w"),indent=1)
