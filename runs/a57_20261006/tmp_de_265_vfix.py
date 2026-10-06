import json
p='content/de/265.json'; d=json.load(open(p))
d['taps'][2]['phrase']='ihm die Hand auf die Schulter legen'
r=d['recall'][2]; assert r['parts'][0]['text']=='ihm auf die'
r['parts'][0]['text']='ihm die Hand auf die'; r['parts'][2]['text']='legen'
d['recall'][0]['parts'][1]['accept']=['bekommen','kriegen','erhalten']
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
p='content/de/267.json'; d=json.load(open(p))
assert d['nouns'][3]['word']=='die Box'; d['nouns'][3]['word']='die Schale'
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
