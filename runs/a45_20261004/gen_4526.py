import json
def keys(d, times):
    return [dict(t=t, x=d[t][0], y=d[t][1], w=d[t][2], h=d[t][3]) if d.get(t) else dict(t=t, off=True) for t in times]
times=[i*0.5 for i in range(19)]
O={0.0:(.12,.08,.88,.92),0.5:(.12,.07,.88,.93),1.0:(.11,.07,.89,.93),1.5:(.12,.07,.88,.93),2.0:(.11,.05,.89,.95),2.5:(.11,.04,.89,.96),
3.0:(0,.06,.92,.94),3.5:(.02,.07,.93,.93),4.0:(.02,.08,.90,.92),4.5:(.02,.07,.92,.93),5.0:(.02,.08,.90,.92),5.5:(.02,.08,.93,.92),
6.0:(0,0,1,.72),6.5:(.11,.12,.89,.88),7.0:(.12,.16,.80,.84),7.5:(.17,.17,.82,.83),8.0:(.07,.13,.90,.87),8.5:(.11,.09,.89,.91)}
k=keys(O,times)
c={"mediaId":4526,"level":"B","keyWord":"election","defaultVoice":"female",
"taps":[
 {"phrase":"to vote in an election","target":"the older woman","voice":"female","keys":k},
 {"phrase":"to grip a yellow pencil","target":"the older woman","voice":"female","keys":k},
 {"phrase":"to leave the voting booth","target":"the older woman","voice":"female","keys":k}],
"stillS":0.5,
"nouns":[{"word":"glasses","x":.60,"y":.30,"voice":"female"},{"word":"a scarf","x":.62,"y":.48,"voice":"female"},
 {"word":"a pencil","x":.30,"y":.66,"voice":"female"},{"word":"a ballot paper","x":.58,"y":.88,"voice":"female"}],
"question":"What is the older woman doing?",
"answer":["She","is","ticking","a","box","on","her","ballot","paper."],
"answerVoice":"female",
"notes":"All three phrases use the older woman on purpose: she fills the frame and the people in the queue are only visible as slivers around her (eyes above her hair, jacket strips beside her), so a second target's box could not be drawn without overlapping hers. At 6.0 only her hands and the ballot are in the picture (box on the hands). At 9.0 she has left the picture (off). 'to vote in an election' relies on the setting (booth, ballot), the others only wait."}
json.dump(c,open('content/4526.json','w'),indent=1,ensure_ascii=False)
