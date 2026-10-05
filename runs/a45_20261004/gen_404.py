import json
T=[i*0.5 for i in range(25)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
B={t:(0,0.31,0.32,0.69) for t in T}
G={0.0:(0.33,0.26,0.43,0.37),0.5:(0.33,0.26,0.43,0.37),1.0:(0.33,0.26,0.43,0.37),1.5:(0.33,0.26,0.43,0.37),2.0:(0.33,0.26,0.43,0.37),
   2.5:(0.33,0.25,0.43,0.38),3.0:(0.33,0.21,0.42,0.42),3.5:(0.33,0.22,0.42,0.41),4.0:(0.33,0.20,0.42,0.43),4.5:(0.33,0.18,0.44,0.45),
   5.0:(0.33,0.19,0.46,0.44),5.5:(0.33,0.18,0.48,0.45),6.0:(0.33,0.18,0.44,0.45),6.5:(0.33,0.17,0.46,0.46),7.0:(0.33,0.23,0.47,0.40),
   7.5:(0.33,0.18,0.49,0.45),8.0:(0.33,0.18,0.47,0.45),8.5:(0.33,0.24,0.47,0.39),9.0:(0.33,0.26,0.49,0.37),9.5:(0.33,0.26,0.54,0.37),
   10.0:(0.33,0.26,0.57,0.37),10.5:(0.33,0.27,0.59,0.36),11.0:(0.33,0.31,0.59,0.32),11.5:(0.33,0.32,0.60,0.31),12.0:(0.33,0.32,0.62,0.31)}
c={"mediaId":404,"level":"A","keyWord":"classroom","defaultVoice":"male",
 "taps":[
  {"phrase":"to look at the camera","target":"the boy in front","voice":"male","keys":keys(B)},
  {"phrase":"to fight at the back","target":"the boys at the back","voice":"male","keys":keys(G)},
  {"phrase":"to laugh together","target":"the boys at the back","voice":"male","keys":keys(G)}],
 "stillS":0.0,
 "nouns":[{"word":"curtains","x":0.20,"y":0.10,"voice":"male"},{"word":"posters","x":0.60,"y":0.20,"voice":"male"},
          {"word":"a tablet","x":0.72,"y":0.77,"voice":"male"},{"word":"a desk","x":0.50,"y":0.88,"voice":"male"}],
 "question":"What are the boys behind him doing?",
 "answer":["They","are","fighting","in","the","classroom."],
 "answerVoice":"male",
 "notes":"Two targets only: the boy in front (does not move) and the group of three or four boys at the back, who are one tangle and cannot be boxed one by one - so two phrases share the group. 'to fight' = play fight (they wrestle and laugh). The boy in front overlaps the group in the picture (his head is beside them, his hands and desk reach under them), so his box is cut at x 0.32 and holds only his head and the left part of his body; the group box starts at 0.33 and at 5.5 misses the left edge of the boy in the cream sweater. The key word 'classroom' is the whole room, not one place, so it is in the answer and not a noun pill. 'a desk' pill is on the front desk (other desks stand behind), 'posters' on the papers left of the board."}
json.dump(c,open('content/404.json','w'),indent=1)
