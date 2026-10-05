import json
def ed(i,f):
    p='content/%d.json'%i; d=json.load(open(p)); f(d); json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
def a(d):
    for n in d['nouns']:
        if n['word']=='a bun': n['word']='a ponytail'
ed(412,a)
def b(d): d['answer']=["He","is","drinking","a","glass","of","juice."]
ed(413,b)
def c(d): d['question']="What is the woman in front doing?"
ed(414,c)
