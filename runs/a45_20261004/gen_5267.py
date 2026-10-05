import json
W={0.0:(.00,.56,.90,.36),0.5:(.00,.57,.92,.35),1.0:(.00,.58,.93,.35),1.5:(.00,.57,.93,.35),2.0:(.00,.56,.93,.36),
2.5:(.00,.22,1.0,.62),3.0:(.00,.22,1.0,.60),3.5:(.00,.22,1.0,.60),4.0:(.00,.21,1.0,.61),4.5:(.00,.21,1.0,.61),5.0:(.00,.20,1.0,.62),
5.5:(.00,.20,1.0,.62),6.0:(.00,.22,1.0,.60),7.5:(.00,.14,1.0,.67),8.0:(.00,.11,1.0,.72),8.5:(.00,.00,.84,.92),9.0:(.00,.00,.98,1.0)}
ts=[i*0.5 for i in range(19)]
k=[dict(t=t,x=W[t][0],y=W[t][1],w=W[t][2],h=W[t][3]) if t in W else dict(t=t,off=True) for t in ts]
d={"mediaId":5267,"level":"A","keyWord":"gun","defaultVoice":"female",
"taps":[{"phrase":p,"target":"the woman","voice":"female","keys":k} for p in ["to lie on a mat","to shoot at the targets","to raise her fists"]],
"stillS":2.0,
"nouns":[{"word":"targets","x":.55,"y":.25,"voice":"female"},{"word":"snow","x":.45,"y":.45,"voice":"female"},
{"word":"a hat","x":.40,"y":.61,"voice":"female"},{"word":"a gun","x":.76,"y":.70,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","shooting","at","the","targets."],
"answerVoice":"female",
"notes":"Only one clear target; background officials are blurry and several hold bells, so all taps on the athlete. 6.5-7.0 show only the targets (off). 'to raise her fists' at 8.5-9.0."}
json.dump(d,open('content/5267.json','w'),indent=1)
