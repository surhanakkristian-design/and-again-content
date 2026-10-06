import json
P='/Users/kristiansurhanak/Projects/and-again-content/runs/a57_20261006/tr/b001/de/hu.json'
h=json.load(open(P))
fixes=[("7053","eltörölgetni egy tányért","megtörölni egy tányért"),
("785","megérkezni a pályaudvarra","megérkezni az állomásra"),
("5560","megköszönni neki","köszönetet mondani neki"),
("868","egyre nagyobbá válni","egyre nagyobbra nőni")]
for i,a,b in fixes:
  n=0
  for f in ("phrases","recall"):
    for k,v in enumerate(h[i][f]):
      if v==a: h[i][f][k]=b; n+=1
  print(i,n)
json.dump(h,open(P,'w'),ensure_ascii=False,indent=1)
