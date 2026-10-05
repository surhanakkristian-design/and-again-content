import json,sys
vid=int(sys.argv[1]); spec=json.load(open(f'spec_{vid}.json'))
times=spec['times']
taps=[]
for p in spec['taps']:
    boxes=spec['boxes'][p['target']]
    keys=[]
    for t,b in zip(times,boxes):
        if b is None: keys.append({'t':t,'off':True})
        else:
            x,y,x2,y2=b; keys.append({'t':t,'x':round(x,2),'y':round(y,2),'w':round(x2-x,2),'h':round(y2-y,2)})
    taps.append({'phrase':p['phrase'],'target':p['target'],'voice':p['voice'],'keys':keys})
out={k:spec[k] for k in ['mediaId','level','keyWord','defaultVoice']}
out['taps']=taps
for k in ['stillS','nouns','question','answer','answerVoice','notes']: out[k]=spec[k]
json.dump(out,open(f'content/{vid}.json','w'),indent=1,ensure_ascii=False)
