import json
def K(d, times):
    out=[]
    for t in times:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=b; out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(min(w,1-x),2),"h":round(min(h,1-y),2)})
    return out
T=[i*0.5 for i in range(19)]
woman={0.0:(0.2,0.45,0.7,0.55),0.5:(0.2,0.45,0.8,0.55),1.0:(0.18,0.46,0.8,0.54),1.5:(0.15,0.45,0.75,0.55),
 2.0:(0.08,0.43,0.88,0.57),2.5:(0.06,0.41,0.7,0.59),3.0:(0.05,0.40,0.65,0.6),3.5:(0.06,0.41,0.66,0.59),
 4.0:(0.05,0.41,0.6,0.59),4.5:(0.06,0.42,0.63,0.58),5.0:(0.08,0.44,0.72,0.56),5.5:(0.11,0.45,0.65,0.55),
 6.0:(0.16,0.43,0.84,0.57),6.5:(0.16,0.43,0.6,0.57),7.0:(0.15,0.43,0.57,0.57),7.5:(0.11,0.45,0.62,0.55),
 8.0:(0.13,0.47,0.63,0.53),8.5:(0.14,0.46,0.63,0.54),9.0:(0.15,0.48,0.61,0.52)}
lights={3.5:(0.76,0,0.24,0.32),4.0:(0.76,0,0.24,0.30),6.5:(0,0,1,0.38),7.0:(0,0,1,0.42),7.5:(0,0,1,0.44),
 8.0:(0,0,1,0.46),8.5:(0,0,1,0.45),9.0:(0,0,1,0.47)}
c={"mediaId":5351,"level":"B","keyWord":"streetlight","defaultVoice":"female",
 "taps":[
  {"phrase":"to stretch out her arm","target":"the woman","voice":"female","keys":K(woman,T)},
  {"phrase":"to gaze up in amazement","target":"the woman","voice":"female","keys":K(woman,T)},
  {"phrase":"to hang over the square","target":"the fairy lights","voice":"female","keys":K(lights,T)}],
 "stillS":1.0,
 "nouns":[{"word":"a streetlight","x":0.38,"y":0.20,"voice":"female"},
          {"word":"bare trees","x":0.75,"y":0.29,"voice":"female"},
          {"word":"a beret","x":0.50,"y":0.52,"voice":"female"},
          {"word":"the road","x":0.86,"y":0.61,"voice":"female"}],
 "question":"What is the woman looking at?",
 "answer":["She","is","gazing","up","at","the","fairy","lights."],
 "answerVoice":"female",
 "notes":"Only one person (selfie-style, she holds the camera). Fairy lights visible only top right at 3.5-4.0 and overhead from 6.5. Streetlight not used as a tap target because several lamps glow; it is a noun at 1.0, where one lamp dominates the picture. 'gazing up' is clearest 8.0-9.0."}
json.dump(c,open('content/5351.json','w'),indent=1)
