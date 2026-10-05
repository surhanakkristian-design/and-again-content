import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else dict(t=t,off=True) for t,r in zip(T,rows)]
maroon=K([(0,0.38,0.27,0.19),(0,0.36,0.27,0.20),(0,0.36,0.34,0.20),(0,0.36,0.39,0.19),
          (0,0.43,0.29,0.14),(0,0.44,0.30,0.14),(0,0.44,0.27,0.14),(0,0.44,0.29,0.14)])
beanie=K([(0.27,0.40,0.38,0.34),(0.27,0.40,0.38,0.34),(0.34,0.38,0.31,0.36),(0.39,0.38,0.27,0.36),
          (0.29,0.37,0.36,0.37),(0.30,0.37,0.32,0.37),(0.27,0.36,0.33,0.38),(0.29,0.35,0.31,0.39)])
lilac=K([(0.66,0.43,0.34,0.30),(0.66,0.42,0.34,0.31),(0.66,0.42,0.34,0.31),(0.67,0.41,0.33,0.32),
         (0.66,0.41,0.34,0.32),(0.62,0.40,0.38,0.33),(0.60,0.42,0.40,0.32),(0.60,0.41,0.40,0.33)])
c=dict(mediaId=8035,level="B",keyWord="viral",defaultVoice="female",
 taps=[dict(phrase="to blow her nose",target="the woman in the beanie",voice="female",keys=beanie),
       dict(phrase="to squirt hand sanitiser",target="the woman in lilac",voice="female",keys=lilac),
       dict(phrase="to lie across the bench",target="the woman in maroon",voice="female",keys=maroon)],
 stillS=3.7,
 nouns=[dict(word="a beanie",x=0.46,y=0.45,voice="female"),
        dict(word="a scarf",x=0.46,y=0.67,voice="female"),
        dict(word="tissues",x=0.25,y=0.76,voice="female"),
        dict(word="a notebook",x=0.88,y=0.76,voice="female")],
 question="What is the woman with tissues doing?",
 answer=["She","is","blowing","her","nose","into","a","tissue."],
 answerVoice="female",
 notes="Key word 'viral' is an adjective, not placed. The woman in the beanie coughs/sneezes at 0.2-1.2 (face blurred at 0.2) and blows her nose from 1.7 on. The woman in maroon leans away at 0.2-1.7 and lies across the bench only from 2.2 (mostly hidden behind the woman in the beanie then, small box). The woman in lilac holds the sanitiser bottle from the start and squirts it into her hand from 2.7. Boxes split vertically between the three women: the beanie woman's left hair/shoulder is cut at 1.2-1.7 where the maroon woman's head is next to her; the lilac woman's fingertips are cut at 3.2-3.7. The man pulling his jumper over his nose is not used; he sits behind the woman in lilac, so her box also covers part of him (not a target).")
json.dump(c,open('content/8035.json','w'),indent=1)
