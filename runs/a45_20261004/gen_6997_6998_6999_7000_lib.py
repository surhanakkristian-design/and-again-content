import json, sys
def build(mid, level, kw, dv, taps, still, nouns, q, ans, av, notes):
    T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
    out=[]
    for ph,tg,v,boxes in taps:
        keys=[]
        for t,b in zip(T,boxes):
            if b is None: keys.append({"t":t,"off":True})
            else:
                x,y,w,h=b; keys.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(w,2),"h":round(h,2)})
        out.append({"phrase":ph,"target":tg,"voice":v,"keys":keys})
    c={"mediaId":mid,"level":level,"keyWord":kw,"defaultVoice":dv,"taps":out,"stillS":still,
       "nouns":[{"word":w,"x":x,"y":y,"voice":vv} for w,x,y,vv in nouns],
       "question":q,"answer":ans.split(),"answerVoice":av,"notes":notes}
    json.dump(c,open(f'content/{mid}.json','w'),indent=1,ensure_ascii=False)
