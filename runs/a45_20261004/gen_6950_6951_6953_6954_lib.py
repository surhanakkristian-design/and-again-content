import json, sys
def K(times, boxes):
    out=[]
    for t,b in zip(times,boxes):
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def write(mid, level, kw, dv, taps, stillS, nouns, q, ans, av, notes):
    times=json.load(open(f'frames/{mid}/packet.json'))['times']
    c={"mediaId":mid,"level":level,"keyWord":kw,"defaultVoice":dv,
       "taps":[{"phrase":p,"target":tg,"voice":v,"keys":K(times,bx)} for p,tg,v,bx in taps],
       "stillS":stillS,"nouns":[{"word":w,"x":x,"y":y,"voice":v} for w,x,y,v in nouns],
       "question":q,"answer":ans.split(" "),"answerVoice":av,"notes":notes}
    json.dump(c,open(f'content/{mid}.json','w'),indent=1)
