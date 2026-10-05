import json
def K(times,f):
    o=[]
    for t in times:
        b=f.get(t)
        o.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return o
T=[i*0.5 for i in range(20)]
p={0.0:(0.0,0.19,0.68,0.62),0.5:(0.0,0.28,0.70,0.54),1.0:(0.0,0.26,0.72,0.56),1.5:(0.0,0.20,1.0,0.78),2.0:(0.0,0.08,1.0,0.78),
2.5:(0.0,0.05,1.0,0.82),3.0:(0.0,0.28,0.82,0.62),3.5:(0.08,0.30,0.82,0.62),4.0:(0.06,0.28,0.90,0.57),4.5:(0.0,0.22,0.82,0.56),
5.0:(0.0,0.15,0.82,0.58),7.0:(0.27,0.16,0.32,0.45),7.5:(0.31,0.13,0.43,0.50),8.0:(0.43,0.28,0.53,0.41),8.5:(0.0,0.07,0.76,0.58),
9.0:(0.0,0.17,0.50,0.54),9.5:(0.23,0.23,0.27,0.40)}
h={0.0:(0.0,0.0,0.82,0.19),0.5:(0.0,0.0,0.80,0.28),1.0:(0.0,0.0,0.82,0.26)}
pk=K(T,p)
d={"mediaId":4066,"level":"B","keyWord":"dirt","defaultVoice":"female",
"taps":[
 {"phrase":"to adjust a tiny helmet","target":"the hand","voice":"female","keys":K(T,h)},
 {"phrase":"to ride a dirt bike","target":"the parrot","voice":"female","keys":pk},
 {"phrase":"to soar over a mound","target":"the parrot","voice":"female","keys":pk}],
"stillS":2.0,
"nouns":[{"word":"a helmet","x":0.62,"y":0.13,"voice":"female"},{"word":"a parrot","x":0.33,"y":0.38,"voice":"female"},{"word":"a dirt bike","x":0.42,"y":0.60,"voice":"female"},{"word":"dirt","x":0.30,"y":0.88,"voice":"female"}],
"question":"What is the parrot doing?",
"answer":["It","is","riding","a","tiny","dirt","bike."],
"answerVoice":"female",
"notes":"Two targets only: the hand (0-1.0 s) and the parrot. The parrot's box includes the bike once it is riding (from 1.5 s). Hand and parrot boxes are split at the top of the helmet (fingertips reach a little lower beside the helmet). 5.5-6.5 s is a close-up of the rear wheel only: parrot off. The jump ('to soar over a mound') is at 7.0-7.5 s."}
json.dump(d,open("content/4066.json","w"),indent=1)
