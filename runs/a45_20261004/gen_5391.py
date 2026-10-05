import json
T=[i*0.5 for i in range(21)]
def K(lst):
    out=[]
    for t,v in zip(T,lst):
        if v is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=v; out.append({"t":t,"x":x,"y":y,"w":round(w,2),"h":round(h,2)})
    return out
N=None
board=[(0.45,0.55,0.27,0.14),(0.38,0.58,0.35,0.14),(0.29,0.60,0.27,0.14),(0.30,0.66,0.49,0.16),(0.17,0.40,0.22,0.34),(0.08,0.40,0.30,0.27)]+[N]*15
ball=[N]*6+[(0.53,0.36,0.21,0.15),(0.30,0.48,0.20,0.14),(0.33,0.47,0.19,0.14),(0.27,0.33,0.19,0.14),(0.47,0.03,0.20,0.14),(0.62,0.14,0.19,0.14),(0.65,0.27,0.18,0.14),(0.47,0.36,0.18,0.14)]+[N]*7
boy=[N]*14+[(0.40,0.55,0.40,0.45),(0.37,0.28,0.38,0.72),(0.30,0.25,0.42,0.72),(0.30,0.25,0.41,0.72),(0.30,0.26,0.40,0.72),(0.31,0.24,0.40,0.74),(0.30,0.28,0.40,0.70)]
c={"mediaId":5391,"level":"B","keyWord":"stare","defaultVoice":"male",
 "taps":[
  {"phrase":"to roll across the concrete","target":"the skateboard","voice":"male","keys":K(board)},
  {"phrase":"to hit the backboard","target":"the basketball","voice":"male","keys":K(ball)},
  {"phrase":"to hold the phone sideways","target":"the boy in the middle","voice":"male","keys":K(boy)}],
 "stillS":8.5,
 "nouns":[{"word":"a phone","x":0.50,"y":0.62,"voice":"male"},
          {"word":"a basketball hoop","x":0.50,"y":0.11,"voice":"male"},
          {"word":"a white T-shirt","x":0.77,"y":0.50,"voice":"male"},
          {"word":"the sky","x":0.18,"y":0.19,"voice":"male"}],
 "question":"What are the teenagers doing?",
 "answer":["They","are","staring","at","the","phone","screen."],
 "answerVoice":"male",
 "notes":"Three shots; skater, shooter and phone boy may be the same boy in a black hoodie, so the boy targets are avoided except 'the boy in the middle' (only in the bench shot, 7.0-10.0; a boy at the right edge at 6.0-6.5 is left off). Ball hits the backboard at 5.5 s and drops beside the pole (does not go in). 'to roll across the concrete': board rolling 0-1.5 s, carried 2.0-2.5 s. Group is mixed (boys and girls), so 'teenagers'."}
json.dump(c,open("content/5391.json","w"),indent=1)
