import json
p='content/6905.json'; c=json.load(open(p))
cru={0.2:(0.21,0.36,0.20,0.18),0.7:(0.21,0.37,0.20,0.18),1.2:(0.20,0.39,0.20,0.19),1.7:(0.21,0.41,0.21,0.18),
     2.2:(0.20,0.46,0.20,0.19),2.7:(0.17,0.54,0.20,0.19),3.2:(0.13,0.60,0.18,0.18),3.7:(0.07,0.65,0.18,0.18)}
c['taps'][2]={"phrase":"to glow red-hot","target":"the crucible","voice":c['defaultVoice'],
  "keys":[{"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]} for t,v in cru.items()]}
man={2.7:(0.40,0.41,0.32,0.53),3.2:(0.32,0.45,0.31,0.55),3.7:(0.26,0.48,0.29,0.52)}
for k in c['taps'][0]['keys']:
    t=round(k['t'],2)
    if t in man: k['x'],k['y'],k['w'],k['h']=man[t]
c['nouns']=[n for n in c['nouns'] if n['word']!='a bell']+[{"word":"smoke","x":0.38,"y":0.22,"voice":c['defaultVoice']}]
c['notes']+=" | VERIFIER: third phrase changed from the blurred horse leg (box also held the sand mould, which also 'rises out of the sand') to the crucible; man's box raised at 2.7-3.7 s to hold his head; 'a bell' replaced by 'smoke' (bells are bronze too)."
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
