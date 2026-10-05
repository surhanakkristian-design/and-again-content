import json
p='content/6911.json'; d=json.load(open(p))
for n in d['nouns']:
    if n['word']=='a double-decker': n['word']='a bus'
json.dump(d,open(p,'w'),indent=1)
