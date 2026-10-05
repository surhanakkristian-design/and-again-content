import json
p='content/5331.json'; d=json.load(open(p))
d['taps'][2]['phrase']='to catch the dripping juice'
for n in d['nouns']:
    if n['word']=='watermelon': n.update(word='a fist',x=0.42,y=0.27)
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
