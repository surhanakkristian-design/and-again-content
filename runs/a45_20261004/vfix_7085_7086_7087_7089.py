import json
def ld(i): return json.load(open(f'content/{i}.json'))
def sv(i,c): json.dump(c,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
def key(c,ti,t): return [k for k in c['taps'][ti]['keys'] if abs(k['t']-t)<.01][0]
c=ld(7085); k=key(c,0,0.7); k['x']=0.33; k['w']=0.38; key(c,1,0.7)['w']=0.32; sv(7085,c)
c=ld(7086); c['taps'][0]['phrase']='to lower curd into the vat'
c['question']='What is dripping from the curd?'; c['answer']=['Whey','is','dripping','from','the','curd.']; sv(7086,c)
c=ld(7087); key(c,0,1.2)['w']=0.33; sv(7087,c)
c=ld(7089); c['taps'][1]['phrase']='to tower over the woman'; sv(7089,c)
