import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
W={0.2:(0.0,0.29,0.8,0.71),0.7:(0.0,0.3,0.81,0.7),1.2:(0.0,0.34,0.82,0.66),1.7:(0.0,0.35,0.82,0.65),
2.2:(0.0,0.34,0.81,0.66),2.7:(0.0,0.34,0.81,0.66),3.2:(0.0,0.37,0.8,0.63),3.7:(0.0,0.37,0.8,0.63)}
P={0.2:(0.0,0.0,0.55,0.28),0.7:(0.0,0.0,0.6,0.29),1.2:(0.0,0.0,0.58,0.33),1.7:(0.0,0.0,0.57,0.34),
2.2:(0.0,0.0,0.57,0.33),2.7:(0.0,0.0,0.57,0.33),3.2:(0.0,0.0,0.56,0.36),3.7:(0.0,0.0,0.56,0.36)}
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
c={"mediaId":5509,"level":"B","keyWord":"abnormal","defaultVoice":"female",
"taps":[{"phrase":"to stare in disbelief","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to gaze up at the sky","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to drop a clump of snow","target":"the palm tree","voice":"female","keys":keys(P)}],
"stillS":3.7,
"nouns":[{"word":"a palm tree","x":0.25,"y":0.15,"voice":"female"},
{"word":"a sun umbrella","x":0.76,"y":0.45,"voice":"female"},
{"word":"a sun lounger","x":0.12,"y":0.6,"voice":"female"},
{"word":"a straw hat","x":0.86,"y":0.7,"voice":"female"}],
"question":"What is falling on the beach?",
"answer":["Snow","is","falling","on","the","tropical","beach."],
"answerVoice":"female",
"notes":"Only one person, two phrases share her. 'the palm tree' = the big snowy palm behind her (other palms at the far left edge); its trunk runs behind her hair, so its box stops at her head (crown only). The clump of snow falls from it at about 1.7-2.2 s. She looks up 2.7-3.2 s, stares at the camera at the start and end. Key word 'abnormal' is an adjective, not placed."}
json.dump(c,open('content/5509.json','w'),indent=1)
