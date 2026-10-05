import json
T=[i*0.5 for i in range(31)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
hand={0.0:(0,0.39,0.80,0.40),0.5:(0,0.42,0.84,0.40),1.0:(0,0.47,0.66,0.50),1.5:(0,0.22,0.40,0.75),2.0:(0,0.24,0.40,0.38),2.5:(0,0.24,0.45,0.38),
      3.0:(0,0.06,0.24,0.32),3.5:(0,0.04,0.24,0.33),4.0:(0,0,0.25,0.37),4.5:(0,0,0.26,0.37),5.0:(0,0,0.29,0.42),5.5:(0,0,0.33,0.42),6.0:(0,0,0.33,0.38),
      6.5:(0,0,0.32,0.38),7.0:(0,0,0.32,0.42),7.5:(0,0,0.33,0.43),8.0:(0,0,0.33,0.40),8.5:(0,0,0.55,0.13)}
ball={0.0:(0.40,0.21,0.27,0.18),0.5:(0.46,0.25,0.25,0.17),1.0:(0.37,0.27,0.33,0.20),1.5:(0.40,0.27,0.33,0.20),2.0:(0.40,0.29,0.35,0.24),2.5:(0.45,0.29,0.36,0.24),
      3.0:(0.24,0.17,0.27,0.23),3.5:(0.24,0.17,0.28,0.23),4.0:(0.25,0.14,0.32,0.26),4.5:(0.26,0.12,0.32,0.28),5.0:(0.29,0.16,0.33,0.28),5.5:(0.33,0.13,0.37,0.30),
      6.0:(0.33,0.10,0.35,0.31),6.5:(0.32,0.10,0.38,0.31),7.0:(0.32,0.13,0.36,0.31),7.5:(0.33,0.14,0.39,0.31),8.0:(0.33,0.15,0.37,0.30),8.5:(0.28,0.13,0.48,0.36),
      9.0:(0.27,0.13,0.50,0.36),9.5:(0.27,0.13,0.50,0.36),10.0:(0.25,0.13,0.50,0.38),10.5:(0.25,0.13,0.50,0.38),11.0:(0.24,0.14,0.50,0.37),11.5:(0.24,0.14,0.50,0.37),
      12.0:(0.22,0.14,0.50,0.37),12.5:(0.24,0.14,0.50,0.37),13.0:(0.21,0.15,0.50,0.37),13.5:(0.22,0.15,0.52,0.37),14.0:(0.22,0.14,0.50,0.37),14.5:(0.22,0.14,0.52,0.37),15.0:(0.23,0.15,0.51,0.37)}
c={"mediaId":43,"level":"A","keyWord":"to spin","defaultVoice":"male",
 "taps":[{"phrase":"to pull a string","target":"the hand","voice":"male","keys":keys(hand)},
         {"phrase":"to spin very fast","target":"the golden ball","voice":"male","keys":keys(ball)},
         {"phrase":"to hold a golden ball","target":"the hand","voice":"male","keys":keys(hand)}],
 "stillS":10.0,
 "nouns":[{"word":"a printer","x":0.16,"y":0.12,"voice":"male"},{"word":"a ball","x":0.50,"y":0.34,"voice":"male"},{"word":"a desk","x":0.50,"y":0.85,"voice":"male"}],
 "question":"What is the golden ball doing?",
 "answer":["It","is","spinning","very","fast."],"answerVoice":"male",
 "notes":"Only two targets: the man's hand(s) and the golden ball (= the gyroscope: ball, axle and ring; 'gyroscope' is not A level). Two hands are in the picture 0-1.5 s, boxed as one target. The hand holds the ball until 8.0 s, so the hand box is only the part of the hand beside or below the ball (fingers around the ring are left to the ball box). Hand gone from 9.0 s. The stand is not used as a target (no A-level phrase that fits only it). Only 3 nouns: pens and paper roll are not in the still, 'stand' / 'ring' left out as too hard or too close to the ball."}
json.dump(c,open('content/43.json','w'),indent=1,ensure_ascii=False)
