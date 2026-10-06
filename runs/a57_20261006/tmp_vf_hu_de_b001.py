import json,sys
R='/Users/kristiansurhanak/Projects/and-again-content/runs/a57_20261006/tr/b001/'
s=json.load(open(R+'source_de.json')); h=json.load(open(R+'de/hu.json'))
ids=list(s)
a,b=int(sys.argv[1]),int(sys.argv[2])
for i in ids[a:b]:
  S=s[i];H=h[i]
  print(f"## {i} | {S['about'][:110]}")
  for k,(p,q) in enumerate(zip(S['phrases'],H['phrases'])): print(f" p{k}: {p['text']} [{p['target']}] => {q}")
  for k,(p,q) in enumerate(zip(S['nouns'],H['nouns'])): print(f" n{k}: {p} => {q}")
  print(f" Q: {S['question']} => {H['question']}")
  print(f" A: {S['answer']} => {H['answer']}")
  for k,(p,q) in enumerate(zip(S['recall'],H['recall'])): print(f" r{k}: {p} => {q}")
print(len(ids))
