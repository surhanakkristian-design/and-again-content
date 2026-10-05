import json
p='tr/b030/cz.json'; d=json.load(open(p))
fixes=[('7896','phrases',2,'otevřít doširoka pusu','doširoka otevřít pusu'),
('7903','phrases',1,'unášet se po kalné vodě','nechat se unášet kalnou vodou'),
('7903','answer',None,'Klouže po tyrkysové vodě.','Pluje po tyrkysové vodě.'),
('7914','answer',None,'Polévá souseda od vedle vodou.','Polévá vodou souseda od vedle.'),
('7917','phrases',1,'vířit přes solnou pláň','vířit po solné pláni'),
('7964','phrases',2,'šklebit se do kamery','culit se do kamery'),
('7988','phrases',1,'rozpažit ruce','rozpažit')]
for k,f,i,a,b in fixes:
  cur=d[k][f][i] if i is not None else d[k][f]
  assert cur==a,(k,cur)
  if i is None: d[k][f]=b
  else: d[k][f][i]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
