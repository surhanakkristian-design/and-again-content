import json
P='/Users/kristiansurhanak/Projects/and-again-content/runs/a57_20261006/tr/b002/de/en.json'
t=json.load(open(P))
def rep(k,field,old,new):
    o=t[k]
    if isinstance(o[field],list):
        n=0
        for i,x in enumerate(o[field]):
            if x==old: o[field][i]=new; n+=1
        assert n, (k,field,old)
    else:
        assert o[field]==old,(k,field,o[field]); o[field]=new
rep('5594','answer','The overwhelming dragon is perching on a rocky ridge.','The awe-inspiring dragon is perching on a rocky ridge.')
rep('7124','question','What is the young man walking down?','What is the young man descending?')
rep('7124','answer','He is walking down the long stone staircase.','He is descending the long stone staircase.')
rep('7124','recall','is walking down the long stone staircase','is descending the long stone staircase')
for f in ('phrases','recall'):
    rep('7016',f,'to walk alongside the cows laughing','to walk laughing alongside the cows')
    rep('7744',f,'to shoot suddenly out of the water','to suddenly shoot out of the water')
json.dump(t,open(P,'w'),ensure_ascii=False,indent=1)
