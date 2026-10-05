import json
def K(rows):
    return [{"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)} for t,x0,y0,x1,y1 in rows]
M=K([(0.2,0.01,0.13,0.46,0.60),(0.7,0.02,0.12,0.46,0.60),(1.2,0.0,0.11,0.46,0.60),(1.7,0.0,0.09,0.46,0.60),(2.2,0.0,0.05,0.46,0.61),(2.7,0.0,0.0,0.46,0.66),(3.2,0.0,0.0,0.44,0.68),(3.7,0.0,0.0,0.44,0.64)])
W=K([(0.2,0.47,0.18,0.92,0.60),(0.7,0.47,0.17,0.93,0.60),(1.2,0.47,0.16,0.93,0.60),(1.7,0.47,0.14,0.97,0.60),(2.2,0.47,0.11,0.97,0.61),(2.7,0.47,0.08,1.0,0.66),(3.2,0.45,0.08,0.98,0.68),(3.7,0.45,0.13,1.0,0.64)])
P=K([(0.2,0.33,0.60,0.59,0.97),(0.7,0.31,0.60,0.61,0.97),(1.2,0.31,0.60,0.60,0.98),(1.7,0.30,0.60,0.61,0.98),(2.2,0.29,0.61,0.60,0.99),(2.7,0.31,0.67,0.63,1.0),(3.2,0.33,0.69,0.65,1.0),(3.7,0.28,0.65,0.67,1.0)])
d={"mediaId":5537,"level":"A","keyWord":"agree with","defaultVoice":"male",
"taps":[
 {"phrase":"to wear a white shirt","target":"the man","voice":"male","keys":M},
 {"phrase":"to wear a green jacket","target":"the woman","voice":"female","keys":W},
 {"phrase":"to stand on two legs","target":"the puppy at the fence","voice":"male","keys":P}],
"stillS":0.2,
"nouns":[{"word":"flags","x":0.60,"y":0.10,"voice":"male"},
 {"word":"a fence","x":0.82,"y":0.67,"voice":"male"},
 {"word":"puppies","x":0.45,"y":0.80,"voice":"male"},
 {"word":"straw","x":0.80,"y":0.93,"voice":"male"}],
"question":"What are the two people doing?",
"answer":["They","are","pointing","at","the","same","puppy."],
"answerVoice":"male",
"notes":"Man and woman do the same actions (point, laugh), so their phrases are states (shirt/jacket). Puppy 'stands on two legs' clearly 0.2-2.2; from 2.7 it is lower in the pile, still looking up. A second puppy at right also climbs on others at 0.2-0.7 (not upright). Person boxes stop at the top of the puppy box (legs behind the fence cut). defaultVoice male: mixed pair, evenId false."}
json.dump(d,open("content/5537.json","w"),indent=1)
