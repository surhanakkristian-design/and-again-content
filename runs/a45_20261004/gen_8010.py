import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def keys(d): return [ (dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if d.get(t) else dict(t=t,off=True)) for t in T]
wom=keys({0.2:(0.0,0.34,0.46,0.66),0.7:(0.0,0.33,0.45,0.67),1.2:(0.0,0.33,0.45,0.67),1.7:(0.0,0.33,0.44,0.67),2.2:(0.0,0.33,0.43,0.67),2.7:(0.0,0.33,0.43,0.67),3.2:(0.0,0.33,0.44,0.67),3.7:(0.0,0.33,0.46,0.67)})
mar=keys({0.2:(0.47,0.33,0.49,0.37),0.7:(0.46,0.33,0.51,0.37),1.2:(0.46,0.33,0.51,0.38),1.7:(0.45,0.32,0.52,0.40),2.2:(0.44,0.30,0.50,0.40),2.7:(0.44,0.30,0.50,0.42),3.2:(0.45,0.30,0.50,0.43),3.7:(0.47,0.30,0.50,0.44)})
tea=keys({0.2:(0.48,0.18,0.36,0.15),0.7:(0.48,0.17,0.39,0.16),1.2:(0.48,0.17,0.39,0.16),1.7:(0.48,0.16,0.39,0.16),2.2:(0.48,0.14,0.40,0.16),2.7:(0.48,0.14,0.42,0.16),3.2:(0.50,0.13,0.48,0.17),3.7:(0.52,0.12,0.48,0.18)})
c=dict(mediaId=8010,level="B",keyWord="surgical",defaultVoice="male",taps=[
 dict(phrase="to stitch a banana",target="the man in maroon",voice="male",keys=mar),
 dict(phrase="to clap her gloved hands",target="the woman",voice="female",keys=wom),
 dict(phrase="to adjust the operating lamp",target="the man in teal",voice="male",keys=tea)],
 stillS=2.2,
 nouns=[dict(word="an operating lamp",x=0.78,y=0.10,voice="male"),dict(word="a banana",x=0.84,y=0.69,voice="male"),
        dict(word="a tissue box",x=0.66,y=0.88,voice="male"),dict(word="a tray",x=0.25,y=0.83,voice="male")],
 question="What is the man in maroon doing?",answer=["He","is","stitching","a","banana."],answerVoice="male",
 notes="Woman/maroon man split vertically around x 0.45 (her clapping gloves cross in front of his arm). Teal man box = head, shoulders and raised arms above the maroon man's cap. Key word 'surgical' is an adjective, not placed.")
json.dump(c,open('content/8010.json','w'),indent=1)
