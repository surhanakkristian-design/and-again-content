import json
times=[i*0.5 for i in range(31)]
def box(b): return dict(x=round(b[0],2),y=round(b[1],2),w=round(b[2]-b[0],2),h=round(b[3]-b[1],2))
pup={0.5:(.71,.32,1,.66),1.0:(.66,.32,.97,.78),1.5:(.66,.33,.90,.78),2.0:(.44,.31,.85,.55),2.5:(.32,.24,.85,.55),
3.0:(.40,.29,.94,.55),3.5:(.36,.22,.92,.55),4.0:(.36,.28,.97,.55),
11.5:(.05,.20,1,.95),12.0:(.17,.17,1,.76),12.5:(.19,.17,1,.74),13.0:(.27,.18,1,.74),13.5:(.27,.17,1,.74),14.0:(.30,.17,1,.72),14.5:(.30,.17,1,.72),15.0:(.27,.18,1,.74)}
for t in times:
    if 4.5<=t<=11.0: pup[t]=(.38,.23,1,.55)
sau={}
for t in times:
    if t<=1.5: sau[t]=(.40,.53,.64,.87)
    elif t<=11.0: sau[t]=(.36,.55,.60,.85)
def keys(d): return [dict(t=t,**box(d[t])) if t in d else dict(t=t,off=True) for t in times]
c=dict(mediaId=4103,level="B",keyWord="patience",defaultVoice="male",
 taps=[dict(phrase="to peer around a screen",target="the puppy",voice="male",keys=keys(pup)),
       dict(phrase="to stick out of cardboard",target="the sausage",voice="male",keys=keys(sau)),
       dict(phrase="to snatch the sausage",target="the puppy",voice="male",keys=keys(pup))],
 stillS=5.0,
 nouns=[dict(word="a puppy",x=.72,y=.40,voice="male"),dict(word="a sausage",x=.47,y=.72,voice="male"),
        dict(word="a rug",x=.70,y=.93,voice="male"),dict(word="a door",x=.27,y=.14,voice="male")],
 question="What is the puppy doing?",
 answer=["It","is","peering","at","the","sausage","with","patience."],answerVoice="male",
 notes="Puppy and sausage overlap in the picture from 2.0 s: split horizontally at y=0.55 (puppy box above, loses the paws; sausage box below). Sausage off from 11.5 s (in the puppy's mouth). Key word patience is abstract, so only in the answer. 'a door' is an A-level noun but the clearest fourth thing.")
json.dump(c,open("content/4103.json","w"),indent=1,ensure_ascii=False)
