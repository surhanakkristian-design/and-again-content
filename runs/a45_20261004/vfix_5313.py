import json
p='content/5313.json'; d=json.load(open(p))
d['taps'][1]['phrase']='to bite into a rice cake'
d['answer']=['She','is','eating','a','rice','cake','on','a','skewer.']
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
