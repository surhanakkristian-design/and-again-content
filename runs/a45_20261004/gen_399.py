import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
M={0.0:(0,0.10,0.45,0.85),0.5:(0,0.05,0.45,0.90),1.0:(0,0.08,0.50,0.92),1.5:(0,0.50,0.68,0.50),
   2.0:(0,0.12,0.19,0.88),2.5:(0,0.20,0.61,0.80),3.0:(0,0.27,0.64,0.73),3.5:(0,0.22,0.66,0.78),
   4.0:(0,0.15,0.60,0.85),4.5:(0,0.10,0.71,0.90),5.0:(0,0.10,0.43,0.90),5.5:(0,0.06,0.56,0.94),
   6.0:(0,0.03,0.49,0.97),6.5:(0,0.03,0.55,0.97),7.0:(0,0.06,0.60,0.94),7.5:(0,0.08,0.59,0.92),
   8.0:(0,0.08,0.50,0.92),8.5:(0,0.08,0.49,0.92),9.0:(0,0.08,0.46,0.92),9.5:(0,0.10,0.45,0.90),10.0:(0,0.10,0.44,0.90)}
W={2.0:(0.20,0.44,0.24,0.22),2.5:(0.62,0.50,0.38,0.50),3.0:(0.65,0.56,0.35,0.44),3.5:(0.67,0.48,0.33,0.52),
   4.0:(0.61,0.46,0.39,0.54),4.5:(0.72,0.42,0.28,0.45),5.0:(0.72,0.43,0.28,0.57),5.5:(0.80,0.30,0.20,0.70),
   6.0:(0.82,0.24,0.18,0.18),6.5:(0.82,0.22,0.18,0.16),7.0:(0.82,0.24,0.18,0.16),7.5:(0.82,0.26,0.18,0.36),
   8.0:(0.78,0.24,0.22,0.40),8.5:(0.72,0.18,0.28,0.60),9.0:(0.68,0.17,0.32,0.70),9.5:(0.65,0.16,0.35,0.70),10.0:(0.64,0.15,0.36,0.75)}
B={5.0:(0.44,0.28,0.20,0.14),5.5:(0.57,0.22,0.18,0.14),6.0:(0.50,0.15,0.24,0.19),6.5:(0.56,0.14,0.24,0.20),
   7.0:(0.61,0.15,0.20,0.19),7.5:(0.60,0.16,0.21,0.19),8.0:(0.51,0.14,0.24,0.20),8.5:(0.50,0.13,0.20,0.20),
   9.0:(0.47,0.14,0.20,0.20),9.5:(0.46,0.13,0.18,0.20),10.0:(0.45,0.13,0.18,0.20)}
c={"mediaId":399,"level":"A","keyWord":"ice cream","defaultVoice":"male",
 "taps":[
  {"phrase":"to lick the ice cream","target":"the man","voice":"male","keys":keys(M)},
  {"phrase":"to wear a big hat","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to stand on the wall","target":"the bird","voice":"male","keys":keys(B)}],
 "stillS":10.0,
 "nouns":[{"word":"the sky","x":0.50,"y":0.07,"voice":"male"},{"word":"a bird","x":0.52,"y":0.23,"voice":"male"},
          {"word":"a hat","x":0.82,"y":0.31,"voice":"male"},{"word":"ice cream","x":0.50,"y":0.45,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","licking","his","ice cream."],
 "answerVoice":"male",
 "notes":"The man = the customer with the beard (the seller in the apron at 0.0-1.0 is not a target; at 1.5 only the man's hand is in the picture). 'to wear a big hat' is a state: the woman's only own actions (pointing 3.5-4.5, holding a cone - the man holds one too) are short or shared. From 5.0 the bird stands right beside the man's head, so the man's box is cut at the bird and misses part of his hand/shoulder on the right. 6.0-7.5 only the brim of the woman's hat is in the picture. Two ice creams at 10.0: the pill is on the man's big one. 'ice cream.' is one chip."}
json.dump(c,open('content/399.json','w'),indent=1)
