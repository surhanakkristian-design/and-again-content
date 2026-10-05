import json
B={0.0:(0.10,0.07,0.85,0.70),0.5:(0.11,0.08,0.86,0.68),1.0:(0.10,0.07,0.87,0.71),1.5:(0.10,0.09,0.90,0.67),
2.0:(0.07,0.06,0.92,0.69),2.5:(0.05,0.10,0.95,0.65),3.0:(0.03,0.20,0.97,0.60),3.5:(0.03,0.13,0.97,0.62),
4.0:(0.02,0.16,0.98,0.60),4.5:(0,0.13,1,0.60),5.0:(0,0.16,1,0.60),5.5:(0,0.19,1,0.55),6.0:(0,0.18,1,0.55),
6.5:(0.25,0.21,0.52,0.66),7.0:(0.18,0.28,0.70,0.66),7.5:(0.17,0.0,0.80,0.71),8.0:(0.20,0.06,0.62,0.64),
8.5:(0.32,0.16,0.52,0.56),9.0:(0.32,0.15,0.50,0.56)}
keys=[dict(t=t,x=v[0],y=v[1],w=v[2],h=v[3]) for t,v in B.items()]
taps=[dict(phrase=p,target="the woman",voice="female",keys=keys) for p in ["to hold two apples","to wear a colourful headscarf","to raise her arms"]]
c=dict(mediaId=4862,level="A",keyWord="choose",defaultVoice="female",taps=taps,stillS=0.0,
nouns=[dict(word="a headscarf",x=0.53,y=0.15,voice="female"),dict(word="tomatoes",x=0.90,y=0.47,voice="female"),
dict(word="a bag",x=0.88,y=0.68,voice="female"),dict(word="a table",x=0.30,y=0.86,voice="female")],
question="What is the woman doing?",answer=["She","is","choosing","between","two","apples."],answerVoice="female",
notes="Only one clear target (background crowd is blurred), so all three taps are the woman. Apples/melons/sacks/pumpkins always come in pairs, so none is used as a single-noun slot or tap target. 'to hold two apples' 0-1.5 s, 'to raise her arms' 7.5-8.0 s. 'a table' = the wooden stall top under the balance.")
json.dump(c,open('content/4862.json','w'),indent=1)
