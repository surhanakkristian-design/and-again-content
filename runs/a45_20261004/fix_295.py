import json
p='content/295.json'; c=json.load(open(p))
c['taps'][0]['phrase']='to mix the thick paste'
c['answer']=["The","hand","is","mixing","the","thick","paste."]
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
