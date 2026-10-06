import json,sys
R='/Users/kristiansurhanak/Projects/and-again-content/runs/a57_20261006/tr/b002/'
s=json.load(open(R+'source_fr.json'));h=json.load(open(R+'fr/hu.json'))
ids=list(s)
a,b=int(sys.argv[1]),int(sys.argv[2])
for i in ids[a:b]:
  S=s[i];H=h[i]
  print(f"=== {i} | {S['about'][:150]}")
  for k,p in enumerate(S['phrases']): print(f" P{k} {p['text']} [{p['target']}] => {H['phrases'][k]}")
  print(" N", list(zip(S['nouns'],H['nouns'])))
  print(" Q", S['question'],'=>',H['question'])
  print(" A", S['answer'],'=>',H['answer'])
  for k,r in enumerate(S['recall']): print(f" R{k} {r} => {H['recall'][k]}")
