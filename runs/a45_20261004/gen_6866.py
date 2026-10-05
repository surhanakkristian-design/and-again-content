import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=round(r[2]-r[0],2),h=round(r[3]-r[1],2)) if r else {"t":t,"off":True} for t,r in zip(T,rows)]
cow=K([(0.20,0.48,0.80,0.85),(0.21,0.50,0.82,0.87),(0.21,0.49,1.0,0.89),(0.22,0.48,1.0,0.91),(0.21,0.49,1.0,0.93),(0.23,0.49,1.0,0.97),(0.19,0.50,1.0,1.0),(0.26,0.50,1.0,1.0)])
calf=K([(0.80,0.52,1.0,0.72),(0.82,0.52,1.0,0.70),None,None,None,None,None,None])
bird=K([None,(0.66,0.36,0.88,0.50),(0.66,0.35,0.88,0.49),(0.67,0.34,0.98,0.48),(0.69,0.34,0.95,0.49),(0.71,0.35,1.0,0.49),(0.74,0.36,1.0,0.50),(0.77,0.36,1.0,0.50)])
c=dict(mediaId=6866,level="A",keyWord="beef",defaultVoice="female",
 taps=[dict(phrase="to walk out of the water",target="the big cow",voice="female",keys=cow),
       dict(phrase="to follow the big cow",target="the small cow",voice="female",keys=calf),
       dict(phrase="to fly over the water",target="the bird on the right",voice="female",keys=bird)],
 stillS=2.2,
 nouns=[dict(word="the sky",x=0.50,y=0.07,voice="female"),dict(word="trees",x=0.78,y=0.20,voice="female"),
        dict(word="a river",x=0.15,y=0.62,voice="female"),dict(word="stones",x=0.30,y=0.92,voice="female")],
 question="What is the big cow doing?",answer=["It","is","walking","out","of","the","water."],answerVoice="female",
 notes="Key word 'beef' (meat) is not visible, so not among the nouns; 'a cow' left out because there are dozens of cows. The small cow (calf) is only visible at 0.2-0.7 on the right, then hidden behind the big cow's head (off). The bird on the right is the egret flying with spread wings; at 0.2 it is a small dark shape landing (off). Another egret spreads its wings on a cow's back in the middle at 2.7-3.7, but it stands, it does not fly over the water. Big cow box top cut 0.01-0.02 above the hump where the bird box sits.")
json.dump(c,open('content/6866.json','w'),indent=1)
