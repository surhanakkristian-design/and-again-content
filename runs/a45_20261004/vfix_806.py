import json
p='content/806.json'; c=json.load(open(p))
assert c['taps'][1]['phrase']=='to wear a brown apron'
c['taps'][1]['phrase']='to put down the tray'
for k in c['taps'][2]['keys']:
    if abs(k['t']-6.0)<0.01:
        k.clear(); k.update({"t":6.0,"x":0.6,"y":0.27,"w":0.25,"h":0.15})
c['notes']+=' Verifier: phrase 2 was "to wear a brown apron" (apron is not A-level) -> "to put down the tray" (7.0-7.5 s); old man box added at 6.0 s (his face is visible behind the bar).'
json.dump(c,open(p,'w'),ensure_ascii=False,indent=1)
