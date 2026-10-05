import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows):
    return [{"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]} for t,r in zip(T,rows)]
woman=K([(0.14,0.40,0.56,0.50),(0.13,0.40,0.60,0.50),(0.13,0.40,0.62,0.50),(0.13,0.40,0.62,0.50),
         (0.11,0.40,0.65,0.53),(0.11,0.40,0.67,0.53),(0.10,0.40,0.73,0.56),(0.09,0.40,0.74,0.56)])
man=K([(0.31,0.13,0.32,0.25)]*8)
d={"mediaId":6986,"level":"A","keyWord":"cooler","defaultVoice":"female",
 "taps":[
  {"phrase":"to read a book","target":"the woman on the floor","voice":"female","keys":woman},
  {"phrase":"to hold a water bottle","target":"the woman on the floor","voice":"female","keys":woman},
  {"phrase":"to wave a fan","target":"the man with the fan","voice":"male","keys":man}],
 "stillS":1.7,
 "nouns":[{"word":"a cooler","x":0.66,"y":0.60,"voice":"female"},
          {"word":"a book","x":0.50,"y":0.76,"voice":"female"},
          {"word":"bottles","x":0.12,"y":0.62,"voice":"female"},
          {"word":"a fan","x":0.40,"y":0.24,"voice":"female"}],
 "question":"What is the sitting woman doing?",
 "answer":["She","is","reading","a","book."],
 "answerVoice":"female",
 "notes":"The man in the green T-shirt holds the paper fan (checked on a zoomed frame); the other man at the counter only rests his head on his hand. 'a cooler' sits on the misty glass-door cooler behind the woman; the bottle-filled cooler on the left is labelled 'bottles'. The two laughing women at the back and the arm on the right edge are not used."}
json.dump(d,open('content/6986.json','w'),indent=1)
