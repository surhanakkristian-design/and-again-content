import json,sys
R='/Users/kristiansurhanak/Projects/and-again-content/runs/a57_20261006/tr/b002/'
s=json.load(open(R+'source_de.json')); h=json.load(open(R+'de/hu.json'))
ids=list(s)
a,b=int(sys.argv[1]),int(sys.argv[2])
for i in ids[a:b]:
  S=s[i];H=h[i]
  print(f"=== {i} | {S['about'][:150]}")
  for p,q in zip(S['phrases'],H['phrases']): print(f" P {p['text']} || {q}")
  print(" N", S['nouns'],"||",H['nouns'])
  print(" Q",S['question'],"||",H['question'])
  print(" A",S['answer'],"||",H['answer'])
  for p,q in zip(S['recall'],H['recall']): print(f" R {p} || {q}")
print(len(ids))
