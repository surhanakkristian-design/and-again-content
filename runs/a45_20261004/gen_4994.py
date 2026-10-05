import json
T=[0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0,10.5,11.0,11.5,12.0]
B=[(.04,.09,.93,.66),(.02,.08,.97,.67),(.02,.07,.96,.68),(.08,.07,.92,.68),(.02,.08,.97,.67),(.02,.08,.97,.67),(.02,.09,.95,.66),
(.08,.06,.92,.70),(0,.02,1,.62),(0,.03,1,.63),(0,.05,1,.63),(0,.05,1,.62),(0,.04,1,.58),(0,.02,1,.60),(0,.02,1,.62),(0,.02,1,.62),(.08,.02,.92,.62),(.10,.02,.90,.62),
(.28,.18,.42,.41),(.26,.12,.48,.46),(.22,.23,.54,.35),(.25,.25,.63,.38),(.29,.18,.42,.42),(.25,.18,.54,.42),(.24,.18,.55,.40)]
keys=[dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,B)]
taps=[dict(phrase=p,target="the woman",voice="female",keys=keys) for p in ["to make fresh pasta","to use a wooden spoon","to carry a big plate"]]
c=dict(mediaId=4994,level="A",keyWord="wooden",defaultVoice="female",taps=taps,stillS=12.0,
nouns=[dict(word="a woman",x=.52,y=.30,voice="female"),dict(word="garlic",x=.86,y=.21,voice="female"),dict(word="pasta",x=.50,y=.58,voice="female"),dict(word="a table",x=.50,y=.88,voice="female")],
question="What is the woman carrying?",answer="She is carrying a big plate of pasta.".split(),answerVoice="female",
notes="Only one clear target (the grandmother); the family is spread on both sides of her, so all 3 phrases use the woman. Key word 'wooden' is in phrase 2 (wooden spoon, 3.5-8.5 s); the wooden table is the noun 'a table'.")
json.dump(c,open('content/4994.json','w'),indent=1)
