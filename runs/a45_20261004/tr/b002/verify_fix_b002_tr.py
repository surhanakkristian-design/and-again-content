import json,os
p=os.path.join(os.path.dirname(os.path.abspath(__file__)),'tr.json')
t=json.load(open(p))
def sub(i,f,k,old,new):
    if k is None:
        assert t[i][f]==old,(i,f,t[i][f]); t[i][f]=new
    else:
        assert t[i][f][k]==old,(i,f,t[i][f][k]); t[i][f][k]=new
sub('94','nouns',2,"milkshake'ler","milkshakeler")
sub('6820','nouns',2,"fildişleri","fil dişleri")
sub('4408','answer',None,"Taze bir meyveli smoothie'nin tadına bakıyor.","Taze meyveli bir smoothie tadıyor.")
sub('347','phrases',1,"ellerini ağzına kapatıp nefesini tutmak","ellerini ağzına kapatıp nefesi kesilmek")
sub('5540','question',None,"Örgülü kadın ne yapıyor?","Saçı örgülü kadın ne yapıyor?")
open(p,'w').write('{\n'+',\n'.join(json.dumps(k,ensure_ascii=False)+': '+json.dumps(v,ensure_ascii=False) for k,v in t.items())+'\n}\n')
