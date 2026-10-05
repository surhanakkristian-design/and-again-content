import json
p='tr/b022/de.json'; d=json.load(open(p))
def rep(i,field,idx,old,new):
    if idx is None:
        assert d[i][field]==old,(i,field); d[i][field]=new
    else:
        assert d[i][field][idx]==old,(i,field,idx); d[i][field][idx]=new
rep('5511','question',None,'Was macht die Frau in Flieder?','Was macht die Frau in Lila?')
rep('5539','phrases',2,'die Wendemarke markieren','den Wendepunkt markieren')
rep('5562','phrases',1,'die Hände in die Luft werfen','die Hände hochreißen')
rep('5562','question',None,'Was macht die Frau in Creme?','Was macht die Frau in Cremeweiß?')
rep('5570','nouns',3,'ein Creolen-Ohrring','eine Creole')
rep('5573','phrases',0,'die Straße hinunterzeigen','die Straße hinunter zeigen')
rep('5597','phrases',0,'zum Schweigen auffordern','ein Zeichen zum Schweigen geben')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
