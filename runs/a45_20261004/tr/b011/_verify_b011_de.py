import json,os
p=os.path.dirname(os.path.abspath(__file__))+'/de.json'
d=json.load(open(p))
n=sum(3+len(v['nouns'])+2 for v in d.values())
assert d['4161']['phrases'][0]=='sich langsam vorwärts bewegen'; d['4161']['phrases'][0]='sich langsam vorwärtsbewegen'
assert d['4093']['phrases'][1]=='vor der Dunkelheit leuchten'; d['4093']['phrases'][1]='in der Dunkelheit leuchten'
assert d['4093']['answer']=='Der runde Mond leuchtet vor der Dunkelheit.'; d['4093']['answer']='Der runde Mond leuchtet in der Dunkelheit.'
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print(n)
