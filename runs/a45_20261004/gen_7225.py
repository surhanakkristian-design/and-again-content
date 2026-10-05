from gen_7225_7226_7228_7229_lib import *
drv=keys([(0.0,0.35,0.50,0.62)]*4+[(0.0,0.32,0.50,0.65)]*4)
ph=keys([(0.51,0.54,0.21,0.24)]*8)
co=keys([(0.76,0.36,0.24,0.48),(0.76,0.35,0.24,0.48),(0.77,0.34,0.23,0.50),(0.76,0.34,0.24,0.50),
         (0.75,0.51,0.25,0.42),(0.80,0.64,0.20,0.33),(0.74,0.66,0.26,0.32),(0.74,0.66,0.26,0.32)])
write(7225,dict(level="B",keyWord="holder",defaultVoice="female",
 taps=[dict(phrase="to grip the steering wheel",target="the driver",voice="female",keys=drv),
       dict(phrase="to stay clamped in its holder",target="the phone",voice="female",keys=ph),
       dict(phrase="to raise a gloved hand",target="the co-driver",voice="female",keys=co)],
 stillS=2.2,
 nouns=[dict(word="a windscreen",x=0.50,y=0.12,voice="female"),
        dict(word="sand dunes",x=0.55,y=0.40,voice="female"),
        dict(word="a helmet",x=0.12,y=0.40,voice="female"),
        dict(word="a holder",x=0.62,y=0.77,voice="female")],
 question="Where is the phone?",
 answer=["The","phone","is","clamped","in","a","holder."],
 answerVoice="female",
 notes="co-driver only partly visible (arm); hand down from 2.2 s. Holder pill on the spring mount below the phone."))
