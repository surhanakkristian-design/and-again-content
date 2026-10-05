import json, sys
def K(times, spec):
    out=[]
    for t in times:
        v=spec.get(t)
        if v is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=v; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
    return out
def write(mid, level, kw, dv, taps, still, nouns, q, ans, av, notes):
    times=json.load(open(f'frames/{mid}/packet.json'))['times']
    c={"mediaId":mid,"level":level,"keyWord":kw,"defaultVoice":dv,
       "taps":[{"phrase":p,"target":tg,"voice":v,"keys":K(times,sp)} for p,tg,v,sp in taps],
       "stillS":still,"nouns":[{"word":w,"x":x,"y":y,"voice":v} for w,x,y,v in nouns],
       "question":q,"answer":ans.split(),"answerVoice":av,"notes":notes}
    json.dump(c,open(f'content/{mid}.json','w'),indent=1,ensure_ascii=False)
