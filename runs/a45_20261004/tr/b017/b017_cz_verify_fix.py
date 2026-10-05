import json
p='tr/b017/cz.json'; d=json.load(open(p))
fixes=[('4869','phrases',0,'kreslit na tablet','kreslit na tabletu'),
('4869','question',None,'Na co žena kreslí?','Na čem žena kreslí?'),
('4869','answer',None,'Kreslí na tablet.','Kreslí na tabletu.'),
('4877','phrases',1,'opřít se v sedadle dozadu','opřít se dozadu v sedadle'),
('4904','phrases',1,'kymácet se proti obloze','kymácet se na pozadí oblohy'),
('4932','answer',None,'Kličkuje s taxíkem provozem.','Kličkuje taxíkem provozem.'),
('4946','phrases',1,'krčit se na podlaze','dřepět na podlaze')]
for k,f,i,a,b in fixes:
  if i is None: assert d[k][f]==a,(k,f); d[k][f]=b
  else: assert d[k][f][i]==a,(k,f); d[k][f][i]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
