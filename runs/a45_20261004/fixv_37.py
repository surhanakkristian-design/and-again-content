import json
p='content/37.json'; c=json.load(open(p))
c['answer']=["They","are","advancing","towards","the","summit."]
json.dump(c,open(p,'w'),ensure_ascii=False,indent=1)
