import json, sys
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def keys(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=b; out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
def write(mid,level,kw,dv,taps,still,nouns,q,ans,av,notes):
    c={"mediaId":mid,"level":level,"keyWord":kw,"defaultVoice":dv,
       "taps":[{"phrase":p,"target":tg,"voice":v,"keys":keys(b)} for p,tg,v,b in taps],
       "stillS":still,"nouns":[{"word":w,"x":x,"y":y,"voice":v} for w,x,y,v in nouns],
       "question":q,"answer":ans.split(),"answerVoice":av,"notes":notes}
    json.dump(c,open(f"content/{mid}.json","w"),indent=1,ensure_ascii=False)
