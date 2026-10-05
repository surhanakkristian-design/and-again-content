import json
T=[i*0.5 for i in range(25)]
def mk(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
boy={3.5:(0.73,0.34,0.27,0.40),4.0:(0.44,0.37,0.31,0.38),4.5:(0.33,0.46,0.37,0.27),5.0:(0.38,0.52,0.44,0.19)}
flag={5.5:(0,0.24,0.36,0.76),6.0:(0,0.25,0.24,0.62),6.5:(0,0.26,0.28,0.54),7.0:(0,0.28,0.3,0.72),7.5:(0,0.24,0.36,0.76),
 8.0:(0,0.24,0.48,0.74),8.5:(0.03,0.26,0.9,0.74),9.0:(0,0.2,0.78,0.8),9.5:(0,0.17,0.88,0.83),10.0:(0,0.05,1,0.9)}
grp={10.5:(0,0.2,1,0.69),11.0:(0,0.23,1,0.67),11.5:(0,0.25,1,0.68),12.0:(0,0.29,1,0.61)}
c={"mediaId":5477,"level":"B","keyWord":"fort","defaultVoice":"male",
 "taps":[{"phrase":"to tumble into the snow","target":"the boy in blue","voice":"male","keys":mk(boy)},
  {"phrase":"to clutch a red flag","target":"the child with the flag","voice":"male","keys":mk(flag)},
  {"phrase":"to collapse in a heap","target":"the group","voice":"male","keys":mk(grp)}],
 "stillS":0.0,
 "nouns":[{"word":"trees","x":0.25,"y":0.36,"voice":"male"},{"word":"a flag","x":0.67,"y":0.39,"voice":"male"},
  {"word":"a fort","x":0.45,"y":0.47,"voice":"male"},{"word":"snow","x":0.5,"y":0.58,"voice":"male"}],
 "question":"What is the boy in blue doing?",
 "answer":["He","is","tumbling","into","the","snow."],"answerVoice":"male",
 "notes":"The boy in blue (teen/young man) visible 3.5-5.0 only; the blue figure at 3.0 is too small to tell. Flag carrier's gender unclear -> default voice. 'the group' = the laughing heap at 10.5-12.0 (people look like teens/young adults, not small children). Fort at stillS 0.0 is the distant snow fort with blue figures; 'snow' = the open snowfield in front of the fort; trees = the bare trees behind the fort (left)."}
json.dump(c,open('content/5477.json','w'),indent=1)
