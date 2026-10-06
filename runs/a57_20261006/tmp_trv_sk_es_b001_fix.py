import json
P='/Users/kristiansurhanak/Projects/and-again-content/runs/a57_20261006/tr/b001/es/sk.json'
t=json.load(open(P))
def rep(i,old,new):
    n=0
    for k,v in t[i].items():
        if isinstance(v,str) and v==old: t[i][k]=new;n+=1
        elif isinstance(v,list):
            for j,x in enumerate(v):
                if x==old: v[j]=new;n+=1
    assert n,(i,old); print(i,n,old,'->',new)
rep('5468','odfotiť sa selfie','urobiť si selfie')
rep('5468','Fotí sa s mužom selfie.','Robí si s mužom selfie.')
rep('5468','Fotí sa s mužom selfie','Robí si s mužom selfie')
rep('721','dieťa','chlapec')
rep('365','Má na sebe obrovské biele slúchadlá.','Má na sebe veľmi veľké biele slúchadlá.')
rep('365','Má na sebe obrovské biele slúchadlá','Má na sebe veľmi veľké biele slúchadlá')
rep('5282','Spieva pieseň so svojou gitarou.','Spieva pieseň s gitarou.')
rep('5282','Spieva pieseň so svojou gitarou','Spieva pieseň s gitarou')
rep('5108','Mávajú z jedného domu v dedine.','Mávajú z domu v dedine.')
rep('5108','Mávajú z jedného domu v dedine','Mávajú z domu v dedine')
json.dump(t,open(P,'w'),ensure_ascii=False,indent=1)
