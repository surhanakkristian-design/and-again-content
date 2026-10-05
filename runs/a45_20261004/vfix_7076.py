import json
p='content/7076.json'; d=json.load(open(p))
tap=d['taps'][2]
tap['phrase']='to double over with laughter'
tap['target']='the man in the white T-shirt'
tap['voice']='male'
tap['keys']=[{"t":k["t"],"x":0.78,"y":0.36,"w":0.21,"h":0.21} for k in d['taps'][0]['keys']]
d['notes']+=" VERIFIER: phrase 3 changed - the man in the hat points at the other man, not at the woman; now the laughing man in the white T-shirt."
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
