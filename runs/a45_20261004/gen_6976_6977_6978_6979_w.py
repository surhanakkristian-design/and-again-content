import json, sys
def K(times, boxes):
    out=[]
    for t,b in zip(times, boxes):
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def write(vid, spec):
    times=json.load(open(f'frames/{vid}/packet.json'))['times']
    taps=[]
    for ph,tg,vo,boxes in spec['taps']:
        assert len(boxes)==len(times)
        taps.append({"phrase":ph,"target":tg,"voice":vo,"keys":K(times,boxes)})
    c={"mediaId":vid,"level":spec['level'],"keyWord":spec['keyWord'],"defaultVoice":spec['dv'],"taps":taps,
       "stillS":spec['still'],"nouns":[{"word":w,"x":x,"y":y,"voice":v} for w,x,y,v in spec['nouns']],
       "question":spec['q'],"answer":spec['a'].split(' '),"answerVoice":spec['av'],"notes":spec.get('notes','')}
    json.dump(c,open(f'content/{vid}.json','w'),indent=1)
if __name__=='__main__':
    vid=int(sys.argv[1]); import importlib.util
    spec=json.load(open(f'scratch/spec_{vid}.json')); write(vid,spec)
