import json
def K(d, times):
    out=[]
    for t in times:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=v; out.append({"t":t,"x":x,"y":y,"w":round(min(w,1-x),2),"h":round(min(h,1-y),2)})
    return out
times=[i*0.5 for i in range(19)]
young={0.0:(0,0,1,0.46),0.5:(0,0,1,0.52),1.0:(0,0,1,0.56),1.5:(0.01,0.04,0.94,0.56),2.0:(0.04,0.10,0.78,0.53),
 2.5:(0.08,0.12,0.74,0.52),3.0:(0.05,0.13,0.77,0.52),3.5:(0.12,0.13,0.70,0.54),4.0:(0.06,0.13,0.76,0.50),
 4.5:(0.06,0.06,0.94,0.58),5.0:(0.12,0.11,0.88,0.55),5.5:(0.39,0.24,0.26,0.20),6.0:(0.41,0.24,0.26,0.18),
 6.5:(0.40,0.24,0.29,0.19),7.0:(0.24,0.22,0.46,0.23),7.5:(0.17,0.15,0.59,0.36),8.0:(0.22,0,0.60,0.46),
 8.5:(0,0,1,0.34),9.0:(0,0,1,0.32)}
beard={2.0:(0.82,0.11,0.18,0.40),2.5:(0.82,0.13,0.18,0.38),3.0:(0.82,0.13,0.18,0.38),3.5:(0.82,0.13,0.18,0.37),
 4.0:(0.82,0.14,0.18,0.32),5.5:(0.65,0.19,0.18,0.26),6.0:(0.67,0.18,0.18,0.24),6.5:(0.69,0.18,0.18,0.25),
 7.0:(0.70,0.17,0.19,0.32),7.5:(0.76,0.09,0.20,0.38),8.0:(0.82,0,0.18,0.30)}
c={"mediaId":5279,"level":"B","keyWord":"scroll","defaultVoice":"male","taps":[
 {"phrase":"to sign a giant scroll","target":"the young man","voice":"male","keys":K(young,times)},
 {"phrase":"to work through the paperwork","target":"the young man","voice":"male","keys":K(young,times)},
 {"phrase":"to hold a green folder","target":"the bearded man","voice":"male","keys":K(beard,times)}],
 "stillS":6.0,
 "nouns":[{"word":"a chandelier","x":0.50,"y":0.06,"voice":"male"},
  {"word":"a French flag","x":0.38,"y":0.27,"voice":"male"},
  {"word":"a scroll","x":0.50,"y":0.60,"voice":"male"},
  {"word":"a wooden table","x":0.50,"y":0.89,"voice":"male"}],
 "question":"What is the young man signing?",
 "answer":["He","is","signing","a","giant","scroll."],
 "answerVoice":"male",
 "notes":"Young man = the signer in glasses (0.0-0.5 only his hands/torso in close-up, it is him). Bearded man with the green folder stands at the right edge 2.0-4.0 (partly cut by the frame; box split at x 0.82 from the signer, signer's right elbow cut there), OFF at 4.5-5.0 (sliver/out) and 8.5-9.0; fully visible 5.5-8.0. The two aides both unroll the scroll, so neither got a phrase. 'paperwork' = stack at 3.0-5.0. Still 6.0: French flag pill on the tricolour (EU flag right next to it)."}
json.dump(c,open('content/5279.json','w'),indent=1)
