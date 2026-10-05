import json,sys
vid=sys.argv[1]; edits=json.loads(sys.argv[2])
p=f'content/{vid}.json'; c=json.load(open(p))
for e in edits:
    # e: {"tap":i,"t":t,"key":{...}} sets key for tap i and all taps sharing its target
    tgt=c['taps'][e['tap']]['target']
    for tap in c['taps']:
        if tap['target']!=tgt: continue
        for k in tap['keys']:
            if abs(k['t']-e['t'])<0.01:
                k.clear(); k.update({'t':e['t'],**e['key']})
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
