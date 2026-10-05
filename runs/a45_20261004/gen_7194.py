import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
main={0.2:(0.28,0.31,0.57,0.45),0.7:(0.30,0.31,0.58,0.45),1.2:(0.30,0.31,0.58,0.45),1.7:(0.30,0.31,0.58,0.45),
      2.2:(0.30,0.31,0.59,0.45),2.7:(0.30,0.31,0.60,0.45),3.2:(0.30,0.31,0.59,0.45),3.7:(0.30,0.31,0.60,0.45)}
def k(d): return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
lad={t:(0.00,0.25,0.22,0.34) for t in T}
c=dict(mediaId=7194,level="B",keyWord="graphics",defaultVoice="female",
 taps=[dict(phrase="to hold a moth print",target="the woman in front",voice="female",keys=k(main)),
       dict(phrase="to smooth the page flat",target="the woman in front",voice="female",keys=k(main)),
       dict(phrase="to stand on a stepladder",target="the woman on the ladder",voice="female",keys=k(lad))],
 stillS=2.2,
 nouns=[dict(word="graphics",x=0.80,y=0.13,voice="female"),dict(word="a window",x=0.37,y=0.18,voice="female"),
        dict(word="a stepladder",x=0.15,y=0.47,voice="female"),dict(word="brushes",x=0.86,y=0.84,voice="female")],
 question="What is the woman in front doing?",
 answer=["She","is","pinning","a","print","to","the","wall."],answerVoice="female",
 notes="Three women; the seated woman at the left edge is only partly visible and not used. Several moth prints exist, so no 'a moth' noun; 'graphics' placed on the wall of pinned prints. Ladder woman's feet are hidden behind the ladder top.")
json.dump(c,open("content/7194.json","w"),indent=1)
