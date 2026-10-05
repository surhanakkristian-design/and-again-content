import json
p='content/533.json'; s=open(p).read()
assert s.count('"to stamp her passport"')==1
s=s.replace('"to stamp her passport"','"to check her passport"'); open(p,'w').write(s); json.loads(s)
p='content/535.json'; d=json.load(open(p))
n=[x for x in d['nouns'] if x['word']=='a plate'][0]; print(n); n['x']=0.13; n['y']=0.81
raw=open(p).read()
import re
new=re.sub(r'("word":\s*"a plate",\s*"x":\s*)0\.2(,\s*"y":\s*)0\.8\b', r'\g<1>0.13\g<2>0.81', raw)
assert new!=raw; json.loads(new); open(p,'w').write(new)
