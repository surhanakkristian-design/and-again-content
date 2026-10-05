import json
p='content/5326.json'; c=json.load(open(p))
c['answer']=['She','is','putting','on','a','bandage.']
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
