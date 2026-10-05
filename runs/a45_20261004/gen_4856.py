import json,sys
def keys(times, boxes):
    out=[]
    for t,b in zip(times,boxes):
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=b; out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(w,2),"h":round(h,2)})
    return out
def build(spec):
    pk=json.load(open(f"frames/{spec['mediaId']}/packet.json"))
    times=pk["times"]
    taps=[]
    for p in spec["taps"]:
        taps.append({"phrase":p[0],"target":p[1],"voice":p[2],"keys":keys(times,spec["boxes"][p[1]])})
    d={"mediaId":spec["mediaId"],"level":pk["level"],"keyWord":pk["keyWord"],"defaultVoice":spec["defaultVoice"],
       "taps":taps,"stillS":spec["stillS"],"nouns":[{"word":n[0],"x":n[1],"y":n[2],"voice":n[3]} for n in spec["nouns"]],
       "question":spec["question"],"answer":spec["answer"].split(" "),"answerVoice":spec["answerVoice"],"notes":spec["notes"]}
    json.dump(d,open(f"content/{spec['mediaId']}.json","w"),indent=1)
if __name__=="__main__":
    build(json.load(open(sys.argv[1])))
