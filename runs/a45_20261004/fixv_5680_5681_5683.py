import json
def ld(i): return json.load(open(f'content/{i}.json'))
def sv(i,d): json.dump(d,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
d=ld(5680)
d['taps'][1]['phrase']='to kneel at the tea table'
d['taps'][2]['phrase']='to waddle across the table'
sv(5680,d)
d=ld(5681)
d['taps'][0]['target']='the woman with a ponytail'
d['taps'][2]['phrase']='to extend her arm straight out'
d['question']='What is the curly-haired woman doing?'
d['answer']=['She','is','gasping','in','surprise.']
sv(5681,d)
d=ld(5683)
d['taps'][0]['phrase']='to prop up her chin'
d['taps'][2]['phrase']='to run out of sand'
k=d['taps'][1]['keys'][-1]; k['x']=0.63; k['w']=0.37
sv(5683,d)
