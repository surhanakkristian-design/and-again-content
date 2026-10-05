import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
    return out
ph={0.0:(.09,.29,.98,.73),0.5:(.09,.29,.81,.73),1.0:(.17,.32,.89,.73),1.5:(.21,.34,.99,.67),2.0:(.20,.40,.85,.68)}
mg={2.5:(.33,0,.96,.50),3.0:(.30,0,1.0,.50),3.5:(.34,0,1.0,.50),4.0:(.33,0,1.0,.48)}
br={4.5:(.27,0,.74,.56),5.0:(.26,0,.72,.56),5.5:(.27,0,.74,.56),6.0:(.26,0,.74,.53),6.5:(.26,0,.74,.53)}
c={"mediaId":4907,"level":"B","keyWord":"speaker","defaultVoice":"male",
 "taps":[{"phrase":"to vibrate on wooden boards","target":"the phone","voice":"male","keys":keys(ph)},
  {"phrase":"to pound a muscular arm","target":"the massage gun","voice":"male","keys":keys(mg)},
  {"phrase":"to punch into the gravel","target":"the hydraulic breaker","voice":"male","keys":keys(br)}],
 "stillS":8.0,
 "nouns":[{"word":"a young man","x":.20,"y":.28,"voice":"male"},{"word":"a speaker","x":.60,"y":.42,"voice":"male"},
  {"word":"a glass of water","x":.20,"y":.68,"voice":"male"},{"word":"a table","x":.30,"y":.88,"voice":"male"}],
 "question":"What is the massage gun doing?","answer":["It","is","pounding","a","muscular","arm."],"answerVoice":"male",
 "notes":"Phone 'vibrate' shows as the phone shifting on the boards between frames. Massage gun box includes the hand holding it. Speaker shot (7.0-9.0) used for the nouns only; a woman left of the young man also gasps, so no phrase on him."}
json.dump(c,open('content/4907.json','w'),indent=1)
