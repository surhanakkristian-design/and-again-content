import json
p='hu.json'; d=json.load(open(p))
F=[('7767','phrases',1,'átautózni a hídon','áthajtani a hídon'),
('7772','nouns',0,'vízimentő-torony','vízimentőtorony'),
('7788','phrases',0,'két félre hasadni','kettéhasadni'),
('7789','phrases',1,'jeges vízben didergni','jeges vízben dideregni'),
('7796','nouns',0,'fém redőny','fémredőny'),
('7797','phrases',2,'végül ülve kikötni','végül a fenekén kötni ki'),
('7802','phrases',2,'csupa sár lenni','csupa sárosnak lenni'),
('7818','phrases',1,'a levegőbe rúgni a lábát','a levegőbe lendíteni a lábát'),
('7820','phrases',0,'égősort feszíteni egy ágon','égősort aggatni egy ágra'),
('7840','question',None,'Mit csinál a barna ruhás férfi?','Mit csinál a barna kabátos férfi?'),
('7860','phrases',1,'egy nehéz kalapácsot felemelni','felemelni egy nehéz kalapácsot'),
('7865','phrases',0,'egy kis fát tartani','némi fát tartani'),
('7889','nouns',0,'sárkány','papírsárkány')]
for i,f,n,a,b in F:
    if n is None: assert d[i][f]==a,(i,f); d[i][f]=b
    else: assert d[i][f][n]==a,(i,f,n); d[i][f][n]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
print(len(F))
