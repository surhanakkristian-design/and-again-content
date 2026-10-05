import json
T=[i*0.5 for i in range(21)]
tops=[0.11,0.12,0.13,0.10,0.10,0.09,0.10,0.10,0.14,0.14,0.17,0.14,0.13,0.14,0.17,0.17,0.14,0.14,0.15,0.17,0.17]
k=[dict(t=t,x=0.0,y=y,w=1.0,h=round(1.0-y,2)) for t,y in zip(T,tops)]
d=dict(mediaId=2,level="B",keyWord="certificate",defaultVoice="female",
 taps=[dict(phrase="to display a framed certificate",target="the woman",voice="female",keys=k),
       dict(phrase="to clutch several framed certificates",target="the woman",voice="female",keys=k),
       dict(phrase="to beam with pride",target="the woman",voice="female",keys=k)],
 stillS=6.0,
 nouns=[dict(word="curly hair",x=0.55,y=0.17,voice="female"),
        dict(word="a certificate",x=0.46,y=0.60,voice="female"),
        dict(word="a top",x=0.50,y=0.94,voice="female")],
 question="What is the woman doing?",
 answer=["She","is","displaying","her","framed","certificates","with","pride."],answerVoice="female",
 notes="Only one target (the woman, with the certificates she holds), so all three phrases use her with the same keys; her box is the full width because her arms and the frames reach both edges. She displays single certificates at 0-1.5 s and 5-6.5 s and clutches an armful at 2-4.5 s and 7-10 s. The text on the certificates is AI gibberish.")
json.dump(d,open("content/2.json","w"),indent=1)
