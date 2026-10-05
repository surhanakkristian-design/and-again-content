import json,sys
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def box(b):
    return [ {"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":round(v[2]-v[0],2),"h":round(v[3]-v[1],2)} for t,v in zip(T,b)]
def write(mid,level,kw,dv,taps,still,nouns,q,ans,av,notes):
    d={"mediaId":mid,"level":level,"keyWord":kw,"defaultVoice":dv,
       "taps":[{"phrase":p,"target":tg,"voice":v,"keys":box(b)} for p,tg,v,b in taps],
       "stillS":still,"nouns":[{"word":w,"x":x,"y":y,"voice":v} for w,x,y,v in nouns],
       "question":q,"answer":ans.split(" "),"answerVoice":av,"notes":notes}
    json.dump(d,open(f"content/{mid}.json","w"),indent=1,ensure_ascii=False)
