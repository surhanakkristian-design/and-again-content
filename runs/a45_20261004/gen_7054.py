import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(lst):
    return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,lst)]
iron=K([(0.25,0.21,0.64,0.66),(0.28,0.21,0.62,0.67),(0.26,0.22,0.65,0.68),(0.22,0.22,0.47,0.73),
        (0.22,0.20,0.46,0.70),(0.17,0.19,0.50,0.76),(0.02,0.16,0.66,0.82),(0.0,0.15,0.66,0.84)])
ring=K([(0.0,0.33,0.25,0.17),(0.0,0.34,0.27,0.17),(0.0,0.34,0.25,0.17),(0.0,0.34,0.21,0.17),
        (0.0,0.33,0.22,0.17),(0.0,0.33,0.17,0.17),None,None])
gasp=K([None,None,None,(0.70,0.37,0.20,0.14),(0.69,0.35,0.23,0.16),(0.68,0.34,0.22,0.16),
        (0.69,0.29,0.26,0.24),(0.67,0.25,0.31,0.35)])
c={"mediaId":7054,"level":"B","keyWord":"do the ironing","defaultVoice":"male",
 "taps":[{"phrase":"to press a white shirt","target":"the man at the board","voice":"male","keys":iron},
         {"phrase":"to burst out laughing","target":"the woman on the ring","voice":"female","keys":ring},
         {"phrase":"to gasp in shock","target":"the man in the water","voice":"male","keys":gasp}],
 "stillS":2.2,
 "nouns":[{"word":"a beach umbrella","x":0.80,"y":0.05,"voice":"male"},{"word":"shirts","x":0.84,"y":0.16,"voice":"male"},
          {"word":"an iron","x":0.47,"y":0.61,"voice":"male"},{"word":"shallow water","x":0.75,"y":0.85,"voice":"male"}],
 "question":"What is happening in the sea?",
 "answer":["A","man","is","pressing","a","shirt","in","the","sea."],"answerVoice":"male",
 "notes":"Ironing man's box excludes his right hand on the shirt from 1.7 s so it does not overlap the gasping swimmer's box; at 0.2-1.2 it excludes his hand left of the iron (woman on ring). Swimmer only clearly visible from 1.7 s. Woman on ring leaves the frame after 2.7 s."}
json.dump(c,open('content/7054.json','w'),indent=1)
