import json
p='tr/b025/tr.json'; d=json.load(open(p))
def s(i,f,idx,old,new):
    if idx is None: assert d[i][f]==old,(i,f); d[i][f]=new
    else: assert d[i][f][idx]==old,(i,f,idx); d[i][f][idx]=new
s('6973','phrases',0,'yüzünü ciddi tutmak','ciddiyetini korumak')
s('6973','answer',None,'Komedyen yüzünü ciddi tutuyor.','Komedyen ciddiyetini koruyor.')
s('6978','phrases',2,'suçlarcasına parmağıyla göstermek','suçlarcasına parmağıyla işaret etmek')
s('7030','phrases',2,'gökyüzünde süzülerek dalış yapmak','gökyüzünde süzülerek alçalmak')
s('6957','nouns',3,'beslenme kutusu','yemek kutusu')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
