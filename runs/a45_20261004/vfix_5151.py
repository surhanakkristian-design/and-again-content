import json
p='content/5151.json'; c=json.load(open(p))
c['answer']='He is hanging a new picture.'.split(' ')
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
