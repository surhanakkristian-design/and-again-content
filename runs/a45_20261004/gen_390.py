import json
OFF=None
def keys(times, boxes):
    assert len(times)==len(boxes), (len(times),len(boxes))
    out=[]
    for t,b in zip(times,boxes):
        if b is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":b[0],"y":b[1],"w":round(b[2],2),"h":round(b[3],2)})
    return out
t=[round(i*0.5,2) for i in range(21)]
# split x per frame, woman top, man top
sp=[0.25,0.27,0.25,0.36,0.38,0.33,0.30,0.30,0.33,0.33,0.31,0.30,0.29,0.30,0.37,0.48,0.45]
wt=[0.36,0.33,0.33,0.30,0.30,0.30,0.31,0.31,0.30,0.31,0.30,0.35,0.39,0.33,0.31,0.33,0.32]
mt=[0.25,0.12,0.13,0.13,0.14,0.13,0.15,0.16,0.15,0.13,0.13,0.13,0.11,0.10,0.13,0.16,0.18]
W=[(0,wt[i],sp[i],round(1-wt[i],2)) for i in range(17)]
M=[(sp[i],mt[i],round(1-sp[i],2),round(1-mt[i],2)) for i in range(17)]
W+=[(0,0.30,0.40,0.70),(0.02,0.29,0.34,0.71),(0.02,0.26,0.29,0.60),(0.03,0.27,0.25,0.50)]
M+=[(0.40,0.20,0.44,0.80),(0.36,0.18,0.37,0.82),(0.31,0.18,0.33,0.80),(0.28,0.21,0.27,0.57)]
D=[OFF]*17+[(0.84,0.40,0.16,0.22),(0.73,0.38,0.27,0.22),(0.66,0.38,0.34,0.23),(0.62,0.39,0.33,0.21)]
json.dump({"mediaId":390,"level":"A","keyWord":"hoodie","defaultVoice":"male",
 "taps":[
  {"phrase":"to pull up his hood","target":"the man","voice":"male","keys":keys(t,M)},
  {"phrase":"to wear a red hoodie","target":"the woman","voice":"female","keys":keys(t,W)},
  {"phrase":"to swim in the water","target":"the ducks","voice":"male","keys":keys(t,D)}],
 "stillS":10.0,
 "nouns":[{"word":"water","x":0.60,"y":0.14,"voice":"male"},{"word":"bikes","x":0.13,"y":0.24,"voice":"male"},
          {"word":"a hoodie","x":0.40,"y":0.37,"voice":"male"},{"word":"ducks","x":0.78,"y":0.50,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","pulling","up","his","hood."],"answerVoice":"male",
 "notes":"Woman's hoodie is maroon / dark red ('red' vs the man's blue). She stands at the left edge, partly cut; 0.0-1.0 the man's raised arm reaches into her box (split by a vertical line). Ducks only 8.5-10.0. Noun 'a hoodie' sits on the man's back; the woman's hoodie is not another noun. 7.5 s both seen from the side, bent forward."},
 open("content/390.json","w"),indent=1,ensure_ascii=False)
