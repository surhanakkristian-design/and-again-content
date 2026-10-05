import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=b; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
    return out
bp=K([(0.02,0.39,0.63,0.61),(0.20,0.40,0.52,0.60),(0.27,0.44,0.43,0.56),(0.33,0.45,0.38,0.55),
      (0.35,0.41,0.33,0.57),(0.33,0.40,0.36,0.52),(0.35,0.41,0.33,0.51),(0.33,0.41,0.32,0.52)])
vendor=K([(0.79,0.47,0.21,0.23),(0.78,0.47,0.22,0.23),(0.76,0.47,0.24,0.26),(0.73,0.48,0.27,0.24),
          (0.69,0.48,0.31,0.23),(0.70,0.48,0.30,0.24),(0.69,0.49,0.31,0.24),(0.72,0.49,0.28,0.26)])
sc=K([None,(0.0,0.46,0.19,0.36),(0.0,0.47,0.21,0.33),(0.0,0.47,0.21,0.37),
      (0.0,0.47,0.18,0.34),(0.0,0.50,0.18,0.30),(0.0,0.49,0.18,0.31),(0.0,0.49,0.18,0.32)])
d={"mediaId":7815,"level":"A","keyWord":"east","defaultVoice":"male",
 "taps":[{"phrase":"to carry a big backpack","target":"the man with the backpack","voice":"male","keys":bp},
         {"phrase":"to sell food","target":"the man in the red apron","voice":"male","keys":vendor},
         {"phrase":"to sit on a scooter","target":"the woman in the helmet","voice":"female","keys":sc}],
 "stillS":2.2,
 "nouns":[{"word":"the sun","x":0.50,"y":0.28,"voice":"male"},
          {"word":"a backpack","x":0.50,"y":0.58,"voice":"male"},
          {"word":"a scooter","x":0.10,"y":0.68,"voice":"male"},
          {"word":"oranges","x":0.86,"y":0.76,"voice":"male"}],
 "question":"Where is the backpacker walking?",
 "answer":["He","is","walking","towards","the","sun."],"answerVoice":"male",
 "notes":"Friend in black jacket (points at 1.2-1.7) is hidden behind the backpacker while pointing, so not used. Scooter rider at the left edge (white helmet, looks female) is half cut by the frame edge; hidden at 0.2. A blurred second helmet appears far behind at ~x .19 at 3.7 - check 'to sit on a scooter' stays unique. 'the sun' = bright low sun glow at the end of the lane."}
json.dump(d,open("content/7815.json","w"),indent=1)
