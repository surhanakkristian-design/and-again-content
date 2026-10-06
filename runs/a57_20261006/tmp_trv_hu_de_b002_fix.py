import json
P='/Users/kristiansurhanak/Projects/and-again-content/runs/a57_20261006/tr/b002/de/hu.json'
h=json.load(open(P))
F=[("93","felfelé tartani a hüvelykujját","feltartani a hüvelykujját"),
("6","felfelé tartani a hüvelykujját","feltartani a hüvelykujját"),
("5712","leejteni egy kósza lapot","leejteni egy különálló lapot"),
("7844","Két generáció női együtt forgatják a palacsintákat.","Két nőgeneráció együtt forgatja a palacsintákat."),
("747","stresszbe kerülni a telefonnál","telefonálás közben stresszbe kerülni"),
("343","úszószemüveg","búvárszemüveg"),
("4125","rángatni egy kendőt","rángatni egy leplet"),
("376","habozni a sziklákon","habzani a sziklákon"),
("7","ballagási kalap","diplomaosztó kalap"),
("5540","biztosítani a mászót","segítséget nyújtani"),
("5540","szőnyeg","matrac"),
("6836","Felemel egy kanapét az erkélyére.","Felhúz egy kanapét az erkélyére."),
("6836","felemel egy kanapét az erkélyére","felhúz egy kanapét az erkélyére"),
("5379","méretet venni egy vendégről","mértéket venni egy vendégről")]
def sub(x,a,b,c):
  if isinstance(x,str): 
    if x==a: c[0]+=1; return b
    return x
  if isinstance(x,list): return [sub(y,a,b,c) for y in x]
  if isinstance(x,dict): return {k:sub(v,a,b,c) for k,v in x.items()}
  return x
for i,a,b in F:
  c=[0]; h[i]=sub(h[i],a,b,c); print(i,a,'->',b,c[0])
json.dump(h,open(P,'w'),ensure_ascii=False,indent=1)
