import json
def ld(i): return json.load(open(f'content/{i}.json'))
def sv(i,d): json.dump(d,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
d=ld(7131)
d['taps'][1]['phrase']='to hold up a big cake'
d['question']='What is the man on the balcony doing?'
d['answer']=['He','is','standing','in','a','pool.']
sv(7131,d)
d=ld(7132)
for k in d['taps'][2]['keys']:
    if k['t']==3.2:
        k.clear(); k.update({'t':3.2,'x':0.0,'y':0.51,'w':0.16,'h':0.49})
sv(7132,d)
d=ld(7134)
d['nouns'][0]={'word':'the sky','x':0.75,'y':0.12,'voice':'male'}
sv(7134,d)
