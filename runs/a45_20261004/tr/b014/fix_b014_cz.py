import json
p='/Users/kristiansurhanak/Projects/and-again-content/runs/a45_20261004/tr/b014/cz.json'
d=json.load(open(p))
def f(i,field,idx,old,new):
    if idx is None:
        assert d[i][field]==old,(i,field); d[i][field]=new
    else:
        assert d[i][field][idx]==old,(i,field,idx); d[i][field][idx]=new
f('4459','nouns',2,'marshmallow','marshmallowy')
f('4535','phrases',2,'tleskat rukama','tleskat')
f('4540','nouns',0,'helma','přilba')
f('4542','phrases',0,'držet tablet','zvednout tablet')
f('4557','answer',None,'Schoulí se muži na klíně.','Choulí se muži na klíně.')
f('4570','phrases',2,'nosit bílý kabát','nosit bílý kabátek')
f('4583','nouns',1,'tílko','vesta')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
