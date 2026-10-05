import json,sys
def keys(times, boxes):
    out=[]
    for t in times:
        b=boxes.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(min(b[2],1-b[0]),2),"h":round(min(b[3],1-b[1]),2)})
    return out
def build(vid, spec):
    info=json.load(open(f'frames/{vid}/packet.json')); times=info['times']
    taps=[]
    for ph,tg,v,bx in spec['taps']:
        taps.append({"phrase":ph,"target":tg,"voice":v,"keys":keys(times,spec['boxes'][bx])})
    c={"mediaId":vid,"level":info['level'],"keyWord":spec['keyWord'],"defaultVoice":spec['dv'],"taps":taps,
       "stillS":spec['still'],"nouns":[{"word":w,"x":x,"y":y,"voice":v} for w,x,y,v in spec['nouns']],
       "question":spec['q'],"answer":spec['a'].split(),"answerVoice":spec['av'],"notes":spec['notes']}
    json.dump(c,open(f'content/{vid}.json','w'),indent=1,ensure_ascii=False)
if __name__=='__main__':
    man={0.0:(0.0,0.14,1.0,0.86),0.5:(0.03,0.21,0.97,0.79),1.0:(0.14,0.16,0.84,0.84),1.5:(0.22,0.22,0.76,0.78),
     2.0:(0.18,0.30,0.64,0.70),2.5:(0.0,0.35,0.92,0.65),3.0:(0.18,0.39,0.82,0.61),
     9.0:(0.42,0.47,0.58,0.53),9.5:(0.38,0.48,0.62,0.52),10.0:(0.48,0.50,0.40,0.50),10.5:(0.41,0.53,0.59,0.47),
     11.0:(0.45,0.54,0.55,0.46),11.5:(0.46,0.54,0.54,0.46),12.0:(0.51,0.54,0.49,0.46)}
    build(5217,{"keyWord":"vest","dv":"male","boxes":{"man":man},
     "taps":[("to touch the roof","the man","male","man"),("to wear a yellow vest","the man","male","man"),("to smile at the camera","the man","male","man")],
     "still":2.0,"nouns":[("the sky",0.5,0.15,"male"),("a tower",0.71,0.44,"male"),("a vest",0.5,0.72,"male"),("a roof",0.15,0.9,"male")],
     "q":"What is the man wearing?","a":"He is wearing a yellow vest.","av":"male",
     "notes":"Only one person, so all three taps use the man. He is off from 3.5 to 8.5 while the camera pans over the town (only a hand sliver at the right edge at 3.5 and 8.5). 'to touch the roof' is true at 0.0-1.0 (hand on the tiles). Still 2.0: tower = the small bell tower right of his head; vest pill on his chest."})
