import json
ID=5333
times=json.load(open(f'frames/{ID}/packet.json'))['times']
B={0.0:(0,.20,.99,.93),0.5:(0,.21,.99,1),1.0:(0,.20,.99,1),1.5:(0,.18,.99,1),2.0:(0,.16,.99,.94),2.5:(0,.07,.88,.98),
 3.0:(0,.33,.88,1),3.5:(0,.20,.93,.98),4.0:(0,.15,.81,.99),4.5:(0,.11,.81,1),5.0:(0,.07,.73,1),5.5:(0,.15,.99,1),
 6.0:(0,.15,.99,1),6.5:(0,.14,.99,1),7.0:(0,.15,.99,1),7.5:(0,.07,.99,1),8.0:(0,.17,.69,1),8.5:(0,.19,.67,1),
 9.0:(0,.22,.71,1),9.5:(0,.24,.74,1),10.0:(0,.26,.71,1),10.5:(0,.27,.71,1),11.0:(0,.29,.71,1),11.5:(0,.31,.69,1),12.0:(0,.31,.73,1)}
keys=[{"t":t,"x":B[t][0],"y":B[t][1],"w":round(B[t][2]-B[t][0],2),"h":round(B[t][3]-B[t][1],2)} for t in times]
tap=lambda p:{"phrase":p,"target":"the young man","voice":"male","keys":keys}
c={"mediaId":ID,"level":"B","keyWord":"staircase","defaultVoice":"male",
 "taps":[tap("to climb a staircase"),tap("to grip the handrail"),tap("to stare up in amazement")],
 "stillS":12.0,
 "nouns":[{"word":"balconies","x":0.45,"y":0.24,"voice":"male"},
          {"word":"a banister","x":0.86,"y":0.37,"voice":"male"},
          {"word":"a staircase","x":0.16,"y":0.47,"voice":"male"},
          {"word":"a backpack","x":0.30,"y":0.70,"voice":"male"}],
 "question":"What is the young man doing?",
 "answer":["He","is","climbing","a","staircase."],
 "answerVoice":"male",
 "notes":"Only one target (selfie clip), so all three phrases use the young man; his box covers most of the frame. He grips the handrail in the concrete, spiral and wooden staircases (0-7.5), not in the marble one. Still 12.0: 'a staircase' sits on the left white marble steps of the grand staircase (the red carpet in the middle is part of it); 'a backpack' pill on the dark strap/bag on his shoulder; 'a banister' on the right balustrade."}
json.dump(c,open(f'content/{ID}.json','w'),indent=1)
