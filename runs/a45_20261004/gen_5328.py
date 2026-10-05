import json
T=[0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0]
B=[(0,0.38,1,0.62),(0,0.38,1,0.62),(0,0.08,1,0.92),(0,0.08,1,0.92),(0.10,0,0.90,1),(0.34,0.06,0.66,0.94),
(0.40,0.24,0.60,0.76),(0.45,0.24,0.55,0.76),(0.45,0.14,0.55,0.86),(0.44,0.14,0.56,0.86),(0.50,0.14,0.50,0.86),(0.42,0.16,0.58,0.84),
(0.35,0.24,0.65,0.76),(0.38,0.24,0.62,0.76),(0.38,0.27,0.62,0.73),(0.44,0.28,0.56,0.72),(0.44,0.27,0.56,0.73),(0.56,0.26,0.44,0.74),
(0.60,0.28,0.40,0.72),(0.54,0.28,0.46,0.72),(0.53,0.29,0.47,0.71)]
keys=[dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,B)]
d=dict(mediaId=5328,level="A",keyWord="a blouse",defaultVoice="female",
taps=[dict(phrase=p,target="the woman",voice="female",keys=keys) for p in ["to spray perfume on her wrist","to smell her wrist","to spray the clothes"]],
stillS=4.0,
nouns=[dict(word="a blouse",x=0.20,y=0.40,voice="female"),dict(word="a window",x=0.40,y=0.10,voice="female"),dict(word="a woman",x=0.86,y=0.62,voice="female")],
question="What is the woman doing?",answer=["She","is","spraying","the","clothes."],answerVoice="female",
notes="Only one person, so all three phrases target the woman. Description says she sniffs the blouse; frames show her spraying perfume on her wrist and smelling the wrist (t 0-1.5), then misting the blouse and rail with a white spray bottle.")
json.dump(d,open("content/5328.json","w"),indent=1)
