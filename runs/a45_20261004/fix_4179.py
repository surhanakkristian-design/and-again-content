import json
p='content/4179.json'; c=json.load(open(p))
c['answer']=["She","is","blowing out","her","birthday","candles."]
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
