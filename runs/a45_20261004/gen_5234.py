import json
T=[i*0.5 for i in range(21)]
# crowd/formation boundary b, flags/crowd boundary f (None = no flags)
B={4.0:0.10,4.5:0.11,5.0:0.17,5.5:0.20,6.0:0.20,6.5:0.23,7.0:0.29,7.5:0.32,8.0:0.35,8.5:0.39,9.0:0.43,9.5:0.48,10.0:0.49}
F={8.5:0.08,9.0:0.15,9.5:0.22,10.0:0.27}
def keys(f):
    out=[]
    for t in T:
        b=f(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":round(b[1],2),"w":b[2],"h":round(b[3],2)})
    return out
def form(t):
    b=B.get(t,0.0); return (0.0,b,1.0,1.0-b)
def crowd(t):
    if t not in B: return None
    top=F.get(t,0.0); return (0.0,top,1.0,B[t]-top)
def flags(t):
    if t not in F: return None
    top=0.0 if t<10 else 0.08
    return (0.0,top,1.0,F[t]-top)
c={"mediaId":5234,"level":"B","keyWord":"rank","defaultVoice":"female",
 "taps":[
  {"phrase":"to salute with white gloves","target":"the women in uniform","voice":"female","keys":keys(form)},
  {"phrase":"to watch from the stands","target":"the spectators","voice":"female","keys":keys(crowd)},
  {"phrase":"to flutter in the breeze","target":"the flags","voice":"female","keys":keys(flags)}],
 "stillS":10.0,
 "nouns":[{"word":"flags","x":0.6,"y":0.17,"voice":"female"},
          {"word":"spectators","x":0.5,"y":0.37,"voice":"female"},
          {"word":"ranks","x":0.5,"y":0.6,"voice":"female"}],
 "question":"What are the women in uniform doing?",
 "answer":["They","are","saluting","in","neat","ranks."],
 "answerVoice":"female",
 "notes":"Every woman in the formation salutes, so the formation is one group target (band below the crowd); a few women in the left column keep their arms down. Crowd band at the top from 4.0 (thin at 4.0-4.5), flags only from 8.5 (only a sliver at the top at 8.5, box 0-0.08 shares the boundary with the crowd). Bands split along horizontal lines; the boundary is approximate where caps meet the crowd."}
json.dump(c,open('content/5234.json','w'),indent=1)
