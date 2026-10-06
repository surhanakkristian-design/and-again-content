import json
def ld(i): return json.load(open(f'content/de/{i}.json'))
def sv(i,d): json.dump(d,open(f'content/de/{i}.json','w'),ensure_ascii=False,indent=2)
d=ld(7811); d['nouns'][2]['word']='der Tennisschläger'; sv(7811,d)
d=ld(526); d['recall'][1]['parts'][1]['accept']=['umklammern','festhalten','halten']; sv(526,d)
d=ld(517)
d['taps'][2]['phrase']='hinter das Cabrio zurückfallen'
d['recall'][2]['parts'][0]['text']='hinter das'
d['question']='Was macht das rote Cabrio?'
d['taps'][0]['target']=d['taps'][1]['target']='das rote Cabrio'
sv(517,d)
