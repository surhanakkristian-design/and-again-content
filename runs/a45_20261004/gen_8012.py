import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(b): return [dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t in T]
woman=K((0.0,0.23,0.45,0.43)); man=K((0.46,0.29,0.26,0.22)); dog=K((0.07,0.67,0.63,0.33))
c=dict(mediaId=8012,level="B",keyWord="suspicion",defaultVoice="female",
 taps=[dict(phrase="to peer under the table",target="the woman in yellow",voice="female",keys=woman),
       dict(phrase="to sip a cup of coffee",target="the seated man",voice="male",keys=man),
       dict(phrase="to sit on the cobblestones",target="the dog",voice="female",keys=dog)],
 stillS=0.2,
 nouns=[dict(word="an awning",x=0.75,y=0.08,voice="female"),
        dict(word="a tablecloth",x=0.68,y=0.58,voice="female"),
        dict(word="a bulldog",x=0.30,y=0.85,voice="female"),
        dict(word="cobblestones",x=0.80,y=0.93,voice="female")],
 question="What is the seated man doing?",
 answer=["He","is","sipping","a","cup","of","coffee."],answerVoice="male",
 notes="Camera is static, so boxes are constant. The woman's forearm reaches into the man's area at y~0.5; her box stops at x 0.45 to avoid overlap. She holds a round white plate/lid (packet says lid) - not used in texts. The man sips mainly in the first second, later holds the cup. 'seated man' separates him from the standing waiter. Key word 'suspicion' is abstract, not placed.")
json.dump(c,open('content/8012.json','w'),indent=1)
