import json,sys
def K(d, times):
    out=[]
    for t in times:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=v; out.append({"t":t,"x":x,"y":y,"w":round(min(w,1-x),2),"h":round(min(h,1-y),2)})
    return out
times=[i*0.5 for i in range(21)]
red={0.0:(0,0.38,0.33,0.32),0.5:(0.24,0.33,0.70,0.67),1.0:(0.52,0.31,0.43,0.50),1.5:(0.62,0.33,0.26,0.22),
 2.0:(0.28,0.27,0.32,0.43),2.5:(0.20,0.27,0.33,0.55),3.0:(0,0.32,0.20,0.53),
 4.5:(0.12,0.38,0.39,0.27),5.0:(0.08,0.35,0.41,0.28),5.5:(0,0.20,0.49,0.41),6.0:(0,0.18,0.49,0.43),6.5:(0,0.18,0.49,0.43),
 7.0:(0,0.16,0.48,0.46),7.5:(0,0.16,0.50,0.47),8.0:(0,0.16,0.49,0.47),8.5:(0,0.17,0.48,0.48),9.0:(0,0.18,0.50,0.48),
 9.5:(0,0.20,0.50,0.48),10.0:(0,0.20,0.48,0.48)}
yel={1.0:(0.30,0.30,0.22,0.38),1.5:(0.27,0.31,0.30,0.28),2.0:(0.68,0.30,0.22,0.30),2.5:(0.60,0.50,0.28,0.22),
 3.0:(0.76,0.46,0.24,0.34),3.5:(0.66,0.55,0.34,0.25),
 4.5:(0.52,0.38,0.32,0.25),5.0:(0.50,0.35,0.36,0.28),5.5:(0.50,0.20,0.50,0.41),6.0:(0.49,0.18,0.51,0.43),6.5:(0.49,0.18,0.51,0.43),
 7.0:(0.48,0.16,0.52,0.46),7.5:(0.50,0.16,0.50,0.47),8.0:(0.49,0.16,0.51,0.47),8.5:(0.48,0.17,0.52,0.48),9.0:(0.50,0.18,0.50,0.48),
 9.5:(0.50,0.20,0.50,0.48),10.0:(0.48,0.20,0.52,0.48)}
plate={5.5:(0.21,0.61,0.59,0.19),6.0:(0.19,0.61,0.63,0.22),6.5:(0.17,0.61,0.67,0.23),7.0:(0.16,0.62,0.69,0.24),
 7.5:(0.16,0.63,0.70,0.24),8.0:(0.15,0.63,0.71,0.26),8.5:(0.16,0.65,0.70,0.26),9.0:(0.15,0.66,0.72,0.27),
 9.5:(0.15,0.68,0.72,0.26),10.0:(0.14,0.68,0.74,0.27)}
c={"mediaId":5276,"level":"B","keyWord":"sibling","defaultVoice":"female","taps":[
 {"phrase":"to lift the blanket overhead","target":"the girl in red","voice":"female","keys":K(red,times)},
 {"phrase":"to wear a mustard-yellow T-shirt","target":"the girl in yellow","voice":"female","keys":K(yel,times)},
 {"phrase":"to rest on the granite counter","target":"the paper plate","voice":"female","keys":K(plate,times)}],
 "stillS":6.0,
 "nouns":[{"word":"siblings","x":0.50,"y":0.45,"voice":"female"},
  {"word":"a chocolate-chip cookie","x":0.52,"y":0.715,"voice":"female"},
  {"word":"a paper plate","x":0.50,"y":0.795,"voice":"female"},
  {"word":"a granite counter","x":0.50,"y":0.90,"voice":"female"}],
 "question":"What are the siblings sharing?",
 "answer":["The","siblings","are","sharing","a","chocolate-chip","cookie."],
 "answerVoice":"female",
 "notes":"Two sisters (red / yellow T-shirt) do almost everything together, so the yellow girl only gets a state (her T-shirt colour). Red girl alone lifts the blanket above her head at 2.0-2.5. Both girls off at 4.0 (only socks under the chairs) and red off at 3.5; yellow off at 0.0/0.5 (hidden behind red). Paper plate only in the counter shot 5.5-10.0; girls' boxes end where the plate box starts (hands reach onto the plate at 7.5). 'siblings' pill sits between the two touching heads at 6.0. 'sharing': at 7.5 they break the single cookie and each eats a half."}
json.dump(c,open('content/5276.json','w'),indent=1)
