import json
def keys(d, times):
    out=[]
    for t in times:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=b
            out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
def write(vid, c, tk):
    times=json.load(open(f'frames/{vid}/packet.json'))['times']
    for tp in c['taps']: tp['keys']=keys(tk[tp.pop('k')], times)
    json.dump(c, open(f'content/{vid}.json','w'), indent=1, ensure_ascii=False)
if __name__=='__main__':
    T=[i*0.5 for i in range(25)]
    W={};F={};P={}
    # t: woman top, split y, woman x0, x split to people, people (x1,y0,y1), fire (x0,x1,y1)
    rows={
    0.0:(0.03,0.48,0.17,0.70,(0.90,0.13,0.32),(0.13,0.87,0.78)),
    0.5:(0.03,0.48,0.17,0.70,(0.90,0.13,0.32),(0.13,0.87,0.78)),
    1.0:(0.03,0.48,0.14,0.70,(0.90,0.14,0.33),(0.13,0.87,0.78)),
    1.5:(0.03,0.48,0.17,0.70,(0.90,0.14,0.33),(0.13,0.87,0.78)),
    2.0:(0.03,0.48,0.18,0.71,(0.91,0.14,0.33),(0.13,0.87,0.78)),
    2.5:(0.03,0.46,0.18,0.71,(0.91,0.14,0.33),(0.13,0.87,0.78)),
    3.0:(0.04,0.47,0.18,0.71,(0.92,0.15,0.34),(0.13,0.87,0.78)),
    3.5:(0.04,0.44,0.18,0.71,(0.92,0.15,0.34),(0.13,0.87,0.78)),
    4.0:(0.03,0.44,0.12,0.71,(0.92,0.15,0.34),(0.13,0.87,0.78)),
    4.5:(0.04,0.42,0.18,0.71,(0.92,0.16,0.35),(0.13,0.87,0.78)),
    5.0:(0.04,0.44,0.18,0.71,(0.92,0.16,0.35),(0.13,0.87,0.78)),
    5.5:(0.03,0.42,0.13,0.72,(0.94,0.17,0.36),(0.13,0.87,0.80)),
    6.0:(0.02,0.42,0.17,0.72,(0.92,0.17,0.36),(0.12,0.90,0.80)),
    6.5:(0.05,0.42,0.20,0.73,(0.95,0.17,0.37),(0.12,0.92,0.82)),
    7.0:(0.10,0.45,0.17,0.73,(0.94,0.18,0.39),(0.12,0.92,0.84)),
    7.5:(0.11,0.45,0.18,0.74,(0.95,0.19,0.39),(0.12,0.92,0.84)),
    8.0:(0.11,0.44,0.20,0.74,(0.95,0.19,0.39),(0.12,0.92,0.84)),
    8.5:(0.12,0.44,0.20,0.74,(0.96,0.19,0.39),(0.12,0.92,0.84)),
    9.0:(0.12,0.45,0.18,0.73,(0.93,0.20,0.40),(0.12,0.92,0.84)),
    9.5:(0.12,0.44,0.18,0.73,(0.93,0.20,0.40),(0.12,0.92,0.84)),
    10.0:(0.11,0.44,0.17,0.72,(0.90,0.20,0.40),(0.12,0.92,0.84)),
    10.5:(0.11,0.44,0.18,0.72,(0.90,0.20,0.40),(0.12,0.92,0.84)),
    11.0:(0.12,0.46,0.18,0.70,(0.88,0.20,0.40),(0.12,0.92,0.84)),
    11.5:(0.08,0.45,0.15,0.73,(0.94,0.18,0.39),(0.10,0.95,0.86)),
    12.0:(0.02,0.47,0.08,0.78,(0.99,0.12,0.36),(0.06,0.95,0.95)),
    }
    for t,(top,sp,wx0,xs,p,f) in rows.items():
        W[t]=(wx0,top,xs,sp); P[t]=(xs+0.01,p[1],p[0],p[2]+0.02); F[t]=(f[0],sp+0.01,f[1],f[2])
    c={"mediaId":4457,"level":"B","keyWord":"crouch","defaultVoice":"female",
     "taps":[
      {"phrase":"to crouch by a campfire","target":"the woman","voice":"female","k":"W"},
      {"phrase":"to blaze in a stone ring","target":"the fire","voice":"female","k":"F"},
      {"phrase":"to stand near the shore","target":"the two people","voice":"female","k":"P"}],
     "stillS":2.0,
     "nouns":[{"word":"the sky","x":0.30,"y":0.06,"voice":"female"},
              {"word":"the sea","x":0.16,"y":0.27,"voice":"female"},
              {"word":"a campfire","x":0.50,"y":0.60,"voice":"female"},
              {"word":"stones","x":0.52,"y":0.84,"voice":"female"}],
     "question":"What is the woman doing?",
     "answer":["She","is","crouching","by","a","campfire."],
     "answerVoice":"female",
     "notes":"Woman and fire overlap in the picture: boxes split along a horizontal line at about knee/hand level, so flame tips that rise in front of her body (from 5.5 s) fall in the woman's box and her hands feeding the fire (0-5 s) fall in the fire's box. Woman's box is cut at the right where the two background people stand (her right elbow slightly cut 0-4 s). The two people are small dark figures; gender not clear, default voice used."}
    write(4457,c,{"W":W,"F":F,"P":P})
