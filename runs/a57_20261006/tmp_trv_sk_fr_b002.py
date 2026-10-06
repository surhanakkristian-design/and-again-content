import json
p='tr/b002/fr/sk.json'; d=json.load(open(p))
fixes=[]
def rep(i,field,old,new,why):
    v=d[i][field]
    if isinstance(v,list):
        n=0
        for j,x in enumerate(v):
            if x==old: v[j]=new; n+=1
        assert n, (i,field,old)
    else:
        assert v==old,(i,field,v); d[i][field]=new
    fixes.append(f"- {i} {field}: {old} -> {new} ({why})")
rep('5149','phrases','svietiť jasnozeleno','svietiť jasnozelenou farbou','"jasnozeleno" is not natural Slovak')
rep('5149','recall','svietiť jasnozeleno','svietiť jasnozelenou farbou','same as phrase')
rep('4206','phrases','rozsvietiť sa jasnou zelenou','rozsvietiť sa jasnozelenou farbou','elliptical, noun missing')
rep('4206','recall','rozsvietiť sa jasnou zelenou','rozsvietiť sa jasnozelenou farbou','same as phrase')
rep('234','phrases','pustiť do vody kocku cukru','pustiť kocku cukru','"do vody" added, not in source')
rep('234','recall','pustiť do vody kocku cukru','pustiť kocku cukru','same as phrase')
rep('4156','phrases','vrhnúť sa za robotom, aby ho chytil','vrhnúť sa po robotovi','entry form must not carry a gendered finite clause')
rep('4156','recall','vrhnúť sa za robotom, aby ho chytil','vrhnúť sa po robotovi','same as phrase')
rep('7145','phrases','fúkať nozdrami','fŕkať nozdrami','horse snorting is "fŕkať"')
rep('7145','recall','fúkať nozdrami','fŕkať nozdrami','same as phrase')
rep('747','answer','Láme sa pod stresom z práce.','Zrúti sa pod stresom z práce.','"lámať sa pod stresom" is not idiomatic; craquer = break down')
rep('747','recall','láme sa pod stresom z práce','zrúti sa pod stresom z práce','same as answer')
rep('7563','phrases','riadiť motorku','jazdiť na motorke','"riadiť motorku" unnatural')
rep('7563','recall','riadiť motorku','jazdiť na motorke','same as phrase')
rep('5517','nouns','šperkovnica','puzdierko','écrin here is a small ring box, not a jewellery box')
rep('4918','phrases','ťažko niesť ťažké tašky','s námahou niesť ťažké tašky','repetition ťažko/ťažké')
rep('4918','recall','ťažko niesť ťažké tašky','s námahou niesť ťažké tašky','same as phrase')
rep('7369','phrases','oboplávať veľrybu na pádli','pádlovať okolo veľryby','"na pádli" wrong; en pagayant = paddling')
rep('7369','recall','oboplávať veľrybu na pádli','pádlovať okolo veľryby','same as phrase')
rep('7369','answer','Oboplávava veľkú veľrybu.','Pláva okolo veľkej veľryby.','"oboplávava" is not a standard form')
rep('7369','recall','oboplávava veľkú veľrybu','pláva okolo veľkej veľryby','same as answer')
rep('7119','phrases','preplňovať sa striebornými rybami','byť preplnený striebornými rybami','"preplňovať sa" unnatural')
rep('7119','recall','preplňovať sa striebornými rybami','byť preplnený striebornými rybami','same as phrase')
rep('4930','phrases','trblietať sa na strane','trblietať sa na stránke','page of a notebook = stránka')
rep('4930','recall','trblietať sa na strane','trblietať sa na stránke','same as phrase')
rep('7154','question','Ako sa podnikateľ prepravuje?','Ako sa podnikateľ presúva?','"prepravovať sa" unnatural for getting around')
rep('7154','answer','Prepravuje sa na jednokolke.','Presúva sa na jednokolke.','same as question')
rep('7154','recall','prepravuje sa na jednokolke','presúva sa na jednokolke','same as answer')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
open('tmp_trv_sk_fr_b002_fixes.txt','w').write("\n".join(fixes))
print(len(fixes))
