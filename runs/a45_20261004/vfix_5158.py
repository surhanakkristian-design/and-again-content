import json
p='content/5158.json'; c=json.load(open(p))
c['taps'][2]['phrase']='to stare in amazement'
c['answer']=['He','is','connecting','cables','to','his','computer.']
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
