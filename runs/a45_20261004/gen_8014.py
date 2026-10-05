import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes): return [dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) if b else dict(t=t,off=True) for t,b in zip(T,boxes)]
man=K([(0.15,0.39,0.32,0.55),(0.12,0.37,0.35,0.60),(0.13,0.36,0.36,0.64),(0.11,0.35,0.42,0.65),
       (0.11,0.34,0.44,0.66),(0.08,0.32,0.51,0.68),(0.06,0.30,0.52,0.70),(0.02,0.30,0.57,0.70)])
woman=K([(0.48,0.43,0.20,0.49),(0.48,0.43,0.22,0.51),(0.50,0.43,0.24,0.53),(0.54,0.42,0.25,0.58),
         (0.56,0.41,0.24,0.59),(0.60,0.40,0.21,0.60),(0.62,0.41,0.37,0.59),(0.62,0.45,0.37,0.55)])
dog=K([(0.69,0.72,0.30,0.18),(0.71,0.73,0.29,0.19),(0.75,0.75,0.25,0.18),(0.80,0.78,0.20,0.17),
       (0.81,0.84,0.19,0.14),(0.82,0.86,0.18,0.14),None,None])
c=dict(mediaId=8014,level="B",keyWord="take after",defaultVoice="male",
 taps=[dict(phrase="to pose by the portrait",target="the young man",voice="male",keys=man),
       dict(phrase="to giggle behind her hand",target="the woman",voice="female",keys=woman),
       dict(phrase="to lie by the fireplace",target="the dog",voice="male",keys=dog)],
 stillS=0.2,
 nouns=[dict(word="a chandelier",x=0.75,y=0.06,voice="male"),
        dict(word="a portrait",x=0.27,y=0.30,voice="male"),
        dict(word="a fireplace",x=0.85,y=0.64,voice="male"),
        dict(word="a wolfhound",x=0.82,y=0.79,voice="male")],
 question="What is the woman doing?",
 answer=["She","is","giggling","behind","her","hand."],answerVoice="female",
 notes="Camera pushes in: the dog leaves the bottom-right corner (only a sliver at 2.2-2.7 s, off from 3.2 s). Woman's box is cut at her legs' right edge to keep clear of the dog box, so the tip of her braids is outside at 0.2-2.7 s. Her pointing finger reaches the man's shoulder at 1.2-1.7 s; split along his shoulder line. 'a wolfhound' is specific (could be 'a dog' if too rare). Man laughs openly at 3.2+ but never behind his hand.")
json.dump(c,open('content/8014.json','w'),indent=1)
