import json
d=json.load(open('content/207.json'))
W={4.0:0.64,6.5:0.53,7.0:0.56,7.5:0.50,8.0:0.56,8.5:0.50,9.0:0.50}
M={5.5:(0.73,),6.5:(0.58,),7.0:(0.58,),7.5:(0.53,),8.0:(0.57,),8.5:(0.62,),9.0:(0.53,),9.5:(0.57,),10.0:(0.60,)}
for k in d['taps'][0]['keys']:
    if k['t'] in W: k['w']=W[k['t']]
for tap in d['taps'][1:]:
    for k in tap['keys']:
        if k['t'] in M:
            k['x']=M[k['t']][0]; k['w']=round(1-k['x'],2)
        if k['t']==4.5: k['y']=0.2; k['h']=0.42
assert d['taps'][1]['keys']==d['taps'][2]['keys']
d['notes']+=" With the cat no longer a target, the woman's and the man's boxes were widened to hold their hands and cups (4.0-10)."
json.dump(d,open('content/207.json','w'),ensure_ascii=False,indent=1)
