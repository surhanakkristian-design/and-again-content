import json
p='content/4353.json'; c=json.load(open(p))
new={11.0:(0,.49),11.5:(0,.50),12.0:(0,.51)}
for tap in c['taps'][:2]:
    for k in tap['keys']:
        if k['t'] in new: k['y'],k['h']=new[k['t']]
c['taps'][2]['phrase']='to have chocolate on top'
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
p='content/4363.json'; c=json.load(open(p))
c['taps'][2]['phrase']='to be hugged tightly'
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
