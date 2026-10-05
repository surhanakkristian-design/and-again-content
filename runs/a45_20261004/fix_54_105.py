import json
p='content/54.json'; c=json.load(open(p))
for tap in c['taps']:
    for i,k in enumerate(tap['keys']):
        if tap['target']=='the ATM' and k['t']==3.0: tap['keys'][i]={"t":3.0,"x":0.52,"y":0.18,"w":0.48,"h":0.74}
        if tap['target']=='the ATM' and k['t']==4.0: tap['keys'][i]={"t":4.0,"x":0.62,"y":0.18,"w":0.38,"h":0.7}
        if tap['target']=='the woman' and k['t']==4.0: tap['keys'][i]={"t":4.0,"x":0,"y":0.1,"w":0.62,"h":0.9}
c['notes']+=" Verifier: ATM box at 3.0 s raised to hold the hood; split at 4.0 s moved to x 0.62 so the fanned banknotes lie in the woman's box."
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
p='content/105.json'; c=json.load(open(p))
c['answer']=["She","is","aiming","an","arrow","at","the","target."]
c['notes']+=" Verifier: answer changed (old chips also allowed 'shooting a bow with an arrow')."
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
