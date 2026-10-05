import json
p='de.json'; d=json.load(open(p))
def rep(k,field,i,old,new):
    if i is None:
        assert d[k][field]==old,(k,field,d[k][field]); d[k][field]=new
    else:
        assert d[k][field][i]==old,(k,field,d[k][field][i]); d[k][field][i]=new
rep('4887','nouns',0,'Klippen','Felswände')
rep('4900','phrases',1,'Einkäufe aufs Gras verschütten','Einkäufe auf dem Gras verstreuen')
rep('4929','phrases',0,'zum Unterricht rennen','zur Vorlesung rennen')
rep('4929','answer',None,'Er rennt zum Unterricht.','Er rennt zur Vorlesung.')
rep('4946','phrases',2,'den Pferdeschwanz schwingen','den Pferdeschwanz schwingen lassen')
rep('4950','answer',None,'Er legt die Hände auf die Hüften.','Er stützt die Hände in die Hüften.')
rep('4952','phrases',1,'an dem Mann hochspringen','am Mann hochspringen')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
