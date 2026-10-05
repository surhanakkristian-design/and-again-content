import json
p='content/400.json'
d=json.load(open(p))
d['nouns']=[n for n in d['nouns'] if n['word']!='a puck']
d['notes']+=" VERIFIER: removed the noun 'a puck' (pill lay inside the goal, where 'a goal' is right too; tiny thing; not an A-level everyday word). Three nouns remain."
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
