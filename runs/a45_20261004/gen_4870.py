import json
T=[round(i*0.5,1) for i in range(21)]
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
full=(0.0,0.0,1.0,1.0)
man=keys({0.0:full,0.5:full,1.0:full,1.5:full,2.0:full,2.5:full,
 3.0:(0.0,0.19,0.84,0.81),3.5:(0.0,0.19,0.86,0.81),4.0:(0.0,0.18,0.84,0.70),4.5:(0.0,0.18,0.86,0.70),
 5.0:(0.45,0.32,0.55,0.68),5.5:(0.45,0.32,0.55,0.68),6.0:(0.45,0.32,0.55,0.68),
 8.0:(0.18,0.29,0.78,0.65),8.5:(0.0,0.31,0.80,0.57),9.0:(0.03,0.36,0.67,0.56),9.5:(0.23,0.35,0.55,0.59),10.0:(0.23,0.34,0.54,0.58)})
barber=keys({5.0:(0.0,0.08,0.45,0.92),5.5:(0.0,0.07,0.45,0.93),6.0:(0.0,0.10,0.45,0.90)})
c=dict(mediaId=4870,level="B",keyWord="foam",defaultVoice="male",taps=[
 dict(phrase="to use an electric trimmer",target="the shirtless man",voice="male",keys=man),
 dict(phrase="to lean over the customer",target="the barber",voice="male",keys=barber),
 dict(phrase="to give two thumbs up",target="the shirtless man",voice="male",keys=man)],
 stillS=1.0,
 nouns=[dict(word="an ear",x=0.14,y=0.25,voice="male"),dict(word="stubble",x=0.45,y=0.42,voice="male"),
        dict(word="foam",x=0.22,y=0.62,voice="male"),dict(word="a straight razor",x=0.45,y=0.88,voice="male")],
 question="What is the barber doing?",answer=["He","is","leaning","over","the","customer."],answerVoice="male",
 notes="Main man used for two phrases (trimmer 3-4.5 s, thumbs up 9.5-10 s); barber the only other clear actor. Forearm shot 6.5-7.5 s OFF (whose arm unclear). At 5-6 s barber and customer split at x=0.45; the barber's hands with the razor reach into the customer's box. Final shot: applauding men behind him are inside his box area but not targets. Target named 'the shirtless man' (shirtless in every shot except the barbershop, where he wears a blue top under a cape and is still boxed as the customer).")
json.dump(c,open('content/4870.json','w'),indent=1)
