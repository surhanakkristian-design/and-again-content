import json
p='content/4696.json'; c=json.load(open(p))
wom={7.0:(0.36,0.23,0.57,0.40),7.5:(0.40,0.23,0.54,0.42),9.0:(0.41,0.25,0.53,0.51),9.5:(0.40,0.08,0.54,0.72),11.0:(0.37,0.13,0.58,0.76),11.5:(0.35,0.13,0.62,0.78)}
crowd={7.0:(0,0.64,0.82,0.36),7.5:(0,0.66,0.80,0.34),9.0:(0,0.77,0.82,0.23),9.5:(0,0.81,0.80,0.19)}
for i in (0,1):
    for k in c['taps'][i]['keys']:
        if k['t'] in wom: k['x'],k['y'],k['w'],k['h']=wom[k['t']]
for k in c['taps'][2]['keys']:
    if k['t'] in crowd: k['x'],k['y'],k['w'],k['h']=crowd[k['t']]
for n in c['nouns']:
    if n['word']=='an elbow': n.update(word='spectators',x=0.45,y=0.70)
c['question']='What are the spectators doing?'
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
