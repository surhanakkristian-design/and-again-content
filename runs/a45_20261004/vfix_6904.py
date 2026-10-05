import json
p='content/6904.json'; c=json.load(open(p))
c['answer']=["She","is","holding","a","herb","pie","under","his","nose."]
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
