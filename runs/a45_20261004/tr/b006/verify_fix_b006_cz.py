import json, os
H = os.path.dirname(os.path.abspath(__file__)); p = f'{H}/cz.json'; t = json.load(open(p))
F = [('308','phrases',2,'dívat se na ně nahoru','dívat se k nim nahoru'),
     ('310','question',None,'Kde jdou?','Kudy jdou?'),
     ('311','phrases',0,'držet vidličku nahoře','držet zdviženou vidličku'),
     ('312','answer',None,'Píská na píšťalku faul.','Píská na píšťalku kvůli faulu.'),
     ('352','phrases',1,'držet nahoře jeden prst','držet jeden zdvižený prst'),
     ('355','answer',None,'Boří obličej do dlaní.','Zabořuje obličej do dlaní.'),
     ('372','phrases',2,'točit se vzduchem','točit se ve vzduchu'),
     ('389','nouns',2,'chleba','chléb'),
     ('418','phrases',0,'vypáčit kroužek','rozevřít kroužek')]
for i, f, k, a, b in F:
    if k is None: assert t[i][f] == a, (i, t[i][f]); t[i][f] = b
    else: assert t[i][f][k] == a, (i, t[i][f][k]); t[i][f][k] = b
json.dump(t, open(p, 'w'), ensure_ascii=False, indent=1)
print(sum(len(v['phrases']) + len(v['nouns']) + 2 for v in t.values()))
