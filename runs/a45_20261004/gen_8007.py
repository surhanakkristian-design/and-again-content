import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def keys(d): return [ (dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if d.get(t) else dict(t=t,off=True)) for t in T]
sub=keys({0.2:(0.0,0.27,0.52,0.73),0.7:(0.08,0.29,0.54,0.71),1.2:(0.28,0.33,0.70,0.67),1.7:(0.78,0.41,0.22,0.59)})
mud=keys({0.2:(0.53,0.22,0.47,0.78),0.7:(0.63,0.25,0.37,0.75),1.7:(0.51,0.30,0.26,0.62),2.2:(0.45,0.31,0.42,0.66),2.7:(0.45,0.33,0.39,0.63),3.2:(0.47,0.32,0.34,0.62),3.7:(0.46,0.32,0.33,0.58)})
c=dict(mediaId=8007,level="B",keyWord="substitute",defaultVoice="male",taps=[
 dict(phrase="to jog onto the pitch",target="the substitute",voice="male",keys=sub),
 dict(phrase="to trudge off the pitch",target="the muddy player",voice="male",keys=mud),
 dict(phrase="to wear a mud-stained kit",target="the muddy player",voice="male",keys=mud)],
 stillS=1.2,
 nouns=[dict(word="a substitute",x=0.62,y=0.68,voice="male"),dict(word="a training bib",x=0.12,y=0.57,voice="male"),
        dict(word="trees",x=0.15,y=0.30,voice="male"),dict(word="the sky",x=0.65,y=0.12,voice="male")],
 question="What is the muddy player doing?",answer=["He","is","trudging","off","the","pitch."],answerVoice="male",
 notes="Muddy player OFF at 1.2 (almost fully hidden behind the substitute). Substitute leaves frame after 1.7. Two phrases share the muddy player.")
json.dump(c,open('content/8007.json','w'),indent=1)
