import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
d=load(7239)
d['taps'][1]['phrase']='to wear a waterproof jacket'
d['question']='What is the man doing?'
save(7239,d)
d=load(5712)
d['taps'][1]['phrase']='to drop a loose sheet'
d['taps'][2]['phrase']='to rest on a stand'
new={1.2:(0.44,0.56),1.7:(0.43,0.57),3.2:(0.44,0.43),3.7:(0.42,0.43)}
for k in d['taps'][2]['keys']:
    if k['t'] in new: k['y'],k['h']=new[k['t']]
save(5712,d)
d=load(378)
d['taps'][0]['phrase']='to perch on a railing'
d['taps'][2]['phrase']='to cast long golden rays'
save(378,d)
