import json,os
P=os.path.expanduser('~/Projects/and-again-content/runs/a57_20261006/tr/b002/de/cz.json')
t=json.load(open(P))
fixes={('5149','svítit jasně zeleně'):'svítit světle zeleně',
 ('4206','rozsvítit se jasně zeleně'):'rozsvítit se světle zeleně',
 ('5458','zpěnit a zbarvit se do oranžova'):'zpěnit se a zbarvit do oranžova',
 ('7369','vyfouknout vodotrysk'):'vychrlit sloupec vody',
 ('5379','naznačit na látku křídou'):'označit látku křídou'}
n=0
for (k,old),new in fixes.items():
    for f in ('phrases','recall'):
        for i,x in enumerate(t[k][f]):
            if x==old: t[k][f][i]=new; n+=1
print(n)
json.dump(t,open(P,'w'),ensure_ascii=False,indent=1)
