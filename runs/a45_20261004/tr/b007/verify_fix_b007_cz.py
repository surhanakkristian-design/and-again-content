import json,os
H=os.path.dirname(os.path.abspath(__file__));p=H+'/cz.json';t=json.load(open(p))
def ph(i,k,a,b):
    assert t[i]['phrases'][k]==a,(i,t[i]['phrases'][k]);t[i]['phrases'][k]=b
ph('448',2,'dívat se přes sluneční brýle','dívat se přes okraj slunečních brýlí')
ph('525',2,'odfouknout listy','odfouknout listy papíru')
ph('548',0,'dívat se hledáčkem','dívat se do hledáčku')
assert t['521']['answer']=='Bolestí si drží nohu.';t['521']['answer']='V bolestech si drží nohu.'
json.dump(t,open(p,'w'),ensure_ascii=False,indent=1)
s=json.load(open(H+'/source.json'));print(sum(5+len(v['nouns']) for v in s.values()))
