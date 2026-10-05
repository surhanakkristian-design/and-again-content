import json
p='de.json'; d=json.load(open(p))
def ph(i,k,old,new):
    assert d[i]['phrases'][k]==old,(i,d[i]['phrases'][k]); d[i]['phrases'][k]=new
ph('7777',1,'einen Donut greifen','einen Donut nehmen')
ph('7819',2,'über ihre Schulter blicken','über die Schulter blicken')
ph('7824',0,'tief geduckt auf ihrem Board fahren','tief auf ihrem Board kauern')
assert d['7831']['question']=='Was macht die Frau in Creme?'; d['7831']['question']='Was macht die Frau in Cremeweiß?'
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
