import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes): return [dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,boxes)]
woman=K([(0.17,0.37,0.32,0.63),(0.19,0.37,0.33,0.63),(0.18,0.36,0.32,0.64),(0.19,0.36,0.33,0.64),
         (0.15,0.35,0.32,0.65),(0.17,0.34,0.35,0.66),(0.15,0.35,0.35,0.65),(0.17,0.33,0.34,0.67)])
man=K([(0.50,0.21,0.45,0.40),(0.53,0.21,0.45,0.40),(0.51,0.21,0.47,0.40),(0.53,0.19,0.46,0.42),
       (0.48,0.17,0.52,0.45),(0.53,0.16,0.46,0.46),(0.51,0.14,0.49,0.48),(0.52,0.12,0.48,0.50)])
c=dict(mediaId=8013,level="A",keyWord="sweet",defaultVoice="female",
 taps=[dict(phrase="to take a selfie",target="the woman",voice="female",keys=woman),
       dict(phrase="to kiss her cheek",target="the man",voice="male",keys=man),
       dict(phrase="to hold up a jacket",target="the man",voice="male",keys=man)],
 stillS=2.2,
 nouns=[dict(word="the sky",x=0.65,y=0.06,voice="female"),
        dict(word="a tree",x=0.14,y=0.16,voice="female"),
        dict(word="a jacket",x=0.20,y=0.42,voice="female"),
        dict(word="grass",x=0.85,y=0.60,voice="female")],
 question="What is the man doing?",
 answer=["He","is","kissing","her","on","the","cheek."],answerVoice="male",
 notes="The couple overlap; boxes split vertically at the line between her cheek and his face, so her hair/skirt right of that line (lower right) lies in no box and the jacket's left drape lies in her box. Man kisses her until ~2.7 s, then smiles. Key word 'sweet' is not a noun.")
json.dump(c,open('content/8013.json','w'),indent=1)
