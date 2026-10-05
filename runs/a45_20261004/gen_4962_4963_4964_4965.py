import json, sys
def K(times, boxes):
    out=[]
    for t in times:
        b=boxes.get(t)
        if b is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def write(vid, level, kw, dv, taps, still, nouns, q, a, av, notes):
    times=json.load(open(f'frames/{vid}/packet.json'))['times']
    c={"mediaId":vid,"level":level,"keyWord":kw,"defaultVoice":dv,
       "taps":[{"phrase":p,"target":tg,"voice":v,"keys":K(times,bx)} for p,tg,v,bx in taps],
       "stillS":still,"nouns":[{"word":w,"x":x,"y":y,"voice":v} for w,x,y,v in nouns],
       "question":q,"answer":a,"answerVoice":av,"notes":notes}
    json.dump(c,open(f'content/{vid}.json','w'),indent=1)
