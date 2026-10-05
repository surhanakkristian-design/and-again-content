import json
T=[i*0.5 for i in range(25)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
W={0.0:(0.02,0.33,0.62,0.67),0.5:(0.03,0.36,0.66,0.64),1.0:(0.04,0.39,0.66,0.61),1.5:(0.12,0.41,0.69,0.59),
2.0:(0.12,0.42,0.70,0.58),2.5:(0.14,0.41,0.66,0.59),3.0:(0.19,0.38,0.63,0.62),3.5:(0.25,0.64,0.70,0.36),
4.0:(0.0,0.66,1.0,0.34),4.5:(0.07,0.69,0.93,0.31),5.0:(0.18,0.74,0.82,0.26),5.5:(0.0,0.74,1.0,0.26),
6.0:(0.0,0.74,1.0,0.26),6.5:(0.0,0.75,1.0,0.25),7.0:(0.0,0.76,1.0,0.24),7.5:(0.0,0.75,1.0,0.25)}
tops={8.0:0.29,8.5:0.26,9.0:0.25,9.5:0.21,10.0:0.17,10.5:0.14,11.0:0.12,11.5:0.09,12.0:0.07}
F={t:(0.40,round(v-0.03,2),0.20,0.26) for t,v in tops.items()}
C={t:(0.0,0.66 if t<9 else 0.68,1.0,0.34 if t<9 else 0.32) for t in tops}
d={"mediaId":4731,"level":"A","keyWord":"nation","defaultVoice":"female",
"taps":[
 {"phrase":"to pull a rope","target":"the women in grey","voice":"female","keys":keys(W)},
 {"phrase":"to fly in the middle","target":"the big flag","voice":"female","keys":keys(F)},
 {"phrase":"to watch the big flag","target":"the crowd","voice":"female","keys":keys(C)}],
"stillS":10.0,
"nouns":[{"word":"the sky","x":0.75,"y":0.08,"voice":"female"},{"word":"a building","x":0.72,"y":0.33,"voice":"female"},
 {"word":"flags","x":0.30,"y":0.50,"voice":"female"},{"word":"people","x":0.50,"y":0.85,"voice":"female"}],
"question":"What are the women in grey doing?",
"answer":["They","are","pulling","the","ropes."],
"answerVoice":"female",
"notes":"Three shots: 0-3.0 s one woman in a grey suit pulling the rope of a flagpole; 3.5-7.5 s a row of women in the same suits all doing the same; 8.0-12.0 s wide shot of the crowd, the row of small flags and one big flag rising in the middle. Because many women pull ropes, target 1 is the group 'the women in grey': the single woman in shot 1, the strip with the whole row of women in shot 2 (the box also holds flagpole bases and two tiny men in the background at 3.5-4.5 s). 'the big flag' and 'the crowd' exist only in shot 3; the seated audience behind the woman in shot 1 is not boxed (no big flag there). Key word 'nation' is abstract, not placed; 'flags' = the row of small flags, the pill sits on its left half. 'ropes' in the answer is the plural of the phrase's 'a rope'."}
json.dump(d,open("content/4731.json","w"),ensure_ascii=False,indent=1)
