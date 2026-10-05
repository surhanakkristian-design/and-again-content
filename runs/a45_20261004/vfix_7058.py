import json
p='content/7058.json'; d=json.load(open(p))
for tap in d['taps']:
    for k in tap['keys']:
        if k.get('off'): continue
        early = k['t'] < 2.0
        if tap['target']=='the doe':
            top = 0.36 if early else 0.34
            bot = round(k['y']+k['h'],2)
            k['y']=top; k['h']=round(bot-top,2)
        elif tap['target']=='the cyclist':
            if early: k['y'],k['h']=0.22,0.14
            else: k['y'],k['h']=0.20,0.14
d['notes']+=" VERIFIER: doe box top raised to 0.36 / 0.34 (head was cut at 0.40), cyclist box shortened to head + phone (ends where the doe box starts); doe ear tips still cut slightly."
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
