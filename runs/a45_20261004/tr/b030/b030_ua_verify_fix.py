import json
p='tr/b030/ua.json'
d=json.load(open(p))
assert d['7891']['answer']=='Там лежить маленький шматочок риби.'
d['7891']['answer']='На ній лежить маленький шматочок риби.'
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
