import json
def K(rows):
    out=[]
    for r in rows:
        if len(r)==1: out.append({"t":r[0],"off":True})
        else: out.append({"t":r[0],"x":r[1],"y":r[2],"w":r[3],"h":r[4]})
    return out
T=[i*0.5 for i in range(100)]
def write(mid,d):
    json.dump(d,open(f"content/{mid}.json","w"),indent=1,ensure_ascii=False)

# ---------- 4303
amb=K([(0.0,0.22,0.33,0.18,0.14),(0.5,0.22,0.33,0.20,0.15),(1.0,0.17,0.34,0.25,0.18),(1.5,0.07,0.33,0.38,0.23),
(2.0,0,0.32,0.47,0.31),(2.5,0,0.30,0.65,0.43),(3.0,0,0.39,1,0.61),(3.5,0,0.33,1,0.67),(4.0,0,0.36,1,0.64),
(4.5,0,0.40,1,0.60),(5.0,0,0.40,1,0.60),(5.5,0,0.42,1,0.58),(6.0,0,0.38,0.95,0.62),(6.5,0,0.53,1,0.47),
(7.0,0,0.57,1,0.43),(7.5,0,0.62,1,0.38),(8.0,0,0.59,1,0.41),(8.5,0,0.56,1,0.44),(9.0,0,0.55,1,0.45),
(9.5,0,0.55,1,0.45),(10.0,0,0.50,1,0.50)])
boy=K([(0.0,0,0.32,0.20,0.68),(0.5,0,0.32,0.21,0.68),(1.0,0,0.33,0.15,0.62)]+[(t,) for t in T[3:21]])
men=K([(t,) for t in T[:13]]+[(6.5,0,0.31,0.36,0.20),(7.0,0.15,0.31,0.38,0.25),(7.5,0.37,0.32,0.32,0.29),
(8.0,0.48,0.33,0.35,0.25),(8.5,0.47,0.32,0.36,0.23),(9.0,0.40,0.33,0.33,0.20),(9.5,0.37,0.33,0.27,0.18),(10.0,0.35,0.32,0.22,0.14)])
write(4303,{"mediaId":4303,"level":"A","keyWord":"medical","defaultVoice":"male",
"taps":[{"phrase":"to drive down the street","target":"the ambulance","voice":"male","keys":amb},
{"phrase":"to wear a backpack","target":"the boy","voice":"male","keys":boy},
{"phrase":"to cross the street","target":"the two men","voice":"male","keys":men}],
"stillS":8.0,
"nouns":[{"word":"an ambulance","x":0.38,"y":0.75,"voice":"male"},{"word":"men","x":0.66,"y":0.43,"voice":"male"},{"word":"a building","x":0.42,"y":0.12,"voice":"male"}],
"question":"What are the two men carrying?","answer":["They","are","carrying","red","bags."],"answerVoice":"male",
"notes":"Key word 'medical' is an adjective, not used as a noun. Ambulance box from 6.5 s covers only the bonnet (split from the two men seen above the windscreen). The two medics are one target (they overlap); off until they are out of the car at 6.5 s. The boy is only in the first three frames; 'to wear a backpack' is a state (no clear action only he does)."})
