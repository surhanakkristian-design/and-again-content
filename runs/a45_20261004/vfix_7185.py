import json
p='content/7185.json'; d=json.load(open(p))
d['taps'][0]['phrase']='to leap through the detector'
d['taps'][2]['phrase']='to grab her ankle boots'
d['question']='What is the woman in socks doing?'
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
