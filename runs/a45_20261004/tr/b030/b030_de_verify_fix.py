import json
p='tr/b030/de.json'; d=json.load(open(p))
fixes=[('7896','phrases',0,'in seine Hand niesen','in die Hand niesen'),
('7896','answer',None,'Er niest in seine Hand.','Er niest in die Hand.'),
('7960','question',None,'Was macht die lockige Frau?','Was macht die Frau mit den Locken?'),
('7961','answer',None,'Er schnüffelt am Gesicht der lockigen Frau.','Er schnüffelt am Gesicht der Frau mit den Locken.'),
('7969','phrases',1,'eine Aktentasche über den Kopf halten','eine Aktentasche über dem Kopf halten'),
('7969','answer',None,'Er hält seine Aktentasche über den Kopf.','Er hält seine Aktentasche über dem Kopf.'),
('7995','answer',None,'Sie fährt ein Motorrad auf dem Hinterrad.','Sie fährt mit dem Motorrad auf dem Hinterrad.'),
('8007','question',None,'Was macht der schlammige Spieler?','Was macht der schlammverschmierte Spieler?'),
('8014','phrases',1,'hinter ihrer Hand kichern','hinter vorgehaltener Hand kichern'),
('8014','answer',None,'Sie kichert hinter ihrer Hand.','Sie kichert hinter vorgehaltener Hand.')]
for i,f,ix,a,b in fixes:
    if ix is None: assert d[i][f]==a,(i,f); d[i][f]=b
    else: assert d[i][f][ix]==a,(i,f); d[i][f][ix]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
