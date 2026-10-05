import json
OFF=None
coach={0.0:(0.18,0.10,0.80,0.72),0.5:(0.13,0.09,0.77,0.74),1.0:(0.25,0.13,0.67,0.79),1.5:(0.63,0.15,0.37,0.67),
2.0:(0.73,0.15,0.27,0.55),2.5:(0.72,0.17,0.28,0.53),3.0:(0.65,0.13,0.35,0.67),3.5:(0.48,0.17,0.52,0.63),
4.0:(0.28,0.16,0.50,0.15),4.5:OFF,5.0:OFF,5.5:(0.27,0.27,0.56,0.73),6.0:(0.69,0.18,0.31,0.60),6.5:(0.66,0.18,0.34,0.57),
7.0:(0.66,0.20,0.32,0.66),7.5:(0.63,0.20,0.35,0.66),8.0:(0.63,0.20,0.36,0.55)}
man={0.0:OFF,0.5:OFF,1.0:OFF,1.5:(0.0,0.52,0.46,0.22),2.0:(0.0,0.46,0.44,0.27),2.5:(0.0,0.46,0.43,0.27),
3.0:(0.0,0.51,0.45,0.32),3.5:(0.0,0.50,0.45,0.33),4.0:(0.10,0.31,0.50,0.44),4.5:(0.55,0.25,0.40,0.52),
5.0:(0.54,0.31,0.38,0.52),5.5:OFF,6.0:(0.02,0.25,0.28,0.55),6.5:(0.07,0.25,0.26,0.51),7.0:(0.05,0.25,0.26,0.62),
7.5:(0.03,0.23,0.25,0.64),8.0:(0.02,0.23,0.24,0.53)}
def keys(d): return [({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]}) for t,v in sorted(d.items())]
c={"mediaId":184,"level":"B","keyWord":"command","defaultVoice":"female",
"taps":[{"phrase":"to blow a whistle","target":"the coach","voice":"female","keys":keys(coach)},
{"phrase":"to raise a clenched fist","target":"the coach","voice":"female","keys":keys(coach)},
{"phrase":"to sprint ahead of everyone","target":"the tall man","voice":"male","keys":keys(man)}],
"stillS":8.0,
"nouns":[{"word":"a fist","x":0.68,"y":0.25,"voice":"female"},{"word":"a whistle","x":0.80,"y":0.43,"voice":"female"},
{"word":"a beard","x":0.38,"y":0.37,"voice":"female"},{"word":"reflections","x":0.45,"y":0.79,"voice":"female"}],
"question":"What is the coach doing?",
"answer":["She","is","commanding","the","others","to","sprint."],"answerVoice":"female",
"notes":"Coach = the woman with braids and the whistle (targets named 'the coach'; nothing in the picture says coach except whistle/role). Tall man = black-haired man without beard; not visible 0.0-1.0; at 4.0 coach and runners overlap, boxes split at y 0.31 (coach box = head + arm only). 5.5 = close-up of the coach's fist. He is clearly in front at 4.5 and 5.0."}

T=sorted(coach)
def fix(idx,t,v):
    for i in idx:
        k=c['taps'][i]['keys'][T.index(t)]; k['x'],k['y'],k['w'],k['h']=v
fix([0,1],1.0,(0.25,0.13,0.67,0.69)); fix([0,1],1.5,(0.63,0.15,0.37,0.56))
fix([0,1],3.0,(0.65,0.12,0.35,0.60)); fix([2],3.0,(0.0,0.50,0.45,0.24))
fix([0,1],3.5,(0.48,0.17,0.52,0.54)); fix([2],3.5,(0.0,0.48,0.45,0.25))
fix([2],5.0,(0.54,0.31,0.38,0.41))
fix([0,1],7.0,(0.66,0.20,0.32,0.53)); fix([2],7.0,(0.05,0.25,0.26,0.50))
fix([0,1],7.5,(0.63,0.20,0.35,0.54)); fix([2],7.5,(0.03,0.23,0.25,0.52))
json.dump(c,open('content/184.json','w'),indent=1)
