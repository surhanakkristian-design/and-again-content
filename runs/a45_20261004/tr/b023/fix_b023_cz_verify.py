import json
p='cz.json'; d=json.load(open(p))
fixes=[('5618','phrases',0,'točit kamarádku dokola','točit kamarádkou dokola'),
('5628','nouns',0,'disko koule','diskokoule'),
('5681','nouns',0,'disko koule','diskokoule'),
('5681','phrases',2,'natáhnout paži rovně před sebe','natáhnout paži rovně'),
('5677','phrases',1,'ukázat podél dráhy','ukázat směrem po dráze'),
('5645','phrases',2,'valit se po podlaze','jet po podlaze'),
('5699','phrases',2,'odpočívat na břehu','ležet na břehu'),
('5711','phrases',0,'hladit slona po hlavě','hladit slůně po hlavě')]
for i,f,k,a,b in fixes:
    assert d[i][f][k]==a,(i,d[i][f][k]); d[i][f][k]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
