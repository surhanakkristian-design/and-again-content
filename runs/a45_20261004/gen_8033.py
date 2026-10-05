import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else dict(t=t,off=True) for t,r in zip(T,rows)]
man=K([(0,0.17,0.21,0.29)]*4+[(0,0.15,0.21,0.28)]*4)
woman=K([(0.21,0.22,0.32,0.72)]*4+[(0.21,0.19,0.33,0.75)]*4)
dog=K([(0.54,0.56,0.46,0.40),(0.54,0.57,0.45,0.39),(0.54,0.59,0.46,0.39),(0.54,0.59,0.46,0.39),
       (0.54,0.59,0.46,0.39),(0.54,0.59,0.46,0.39),(0.54,0.59,0.45,0.40),(0.54,0.59,0.46,0.40)])
c=dict(mediaId=8033,level="A",keyWord="unfortunately",defaultVoice="female",
 taps=[dict(phrase="to kneel on the ground",target="the woman",voice="female",keys=woman),
       dict(phrase="to eat the ice cream",target="the dog",voice="female",keys=dog),
       dict(phrase="to smile at the woman",target="the man",voice="male",keys=man)],
 stillS=2.7,
 nouns=[dict(word="the sky",x=0.72,y=0.10,voice="female"),
        dict(word="an ice cream",x=0.55,y=0.44,voice="female"),
        dict(word="a bench",x=0.85,y=0.54,voice="female"),
        dict(word="a dog",x=0.75,y=0.76,voice="female")],
 question="What is the woman looking at?",
 answer=["She","is","looking","at","her","ice","cream."],
 answerVoice="female",
 notes="Key word 'unfortunately' is an adverb, not used as a noun; kept out of the answer (free adverb position). The dog catches the falling scoop at 0.2 s and licks its lips after. Man/woman boxes split at x 0.21 (her ponytail/shoulder vs his arm in the window), so her knee/foot at the far left is outside her box; her box ends at x 0.53-0.54 to stay clear of the dog, cutting the hand with the cone.")
json.dump(c,open('content/8033.json','w'),indent=1)
