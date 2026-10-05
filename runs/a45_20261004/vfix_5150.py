import json
p='content/5150.json'; c=json.load(open(p))
for k in c['taps'][0]['keys']:
    if k['t']==1.5: k.update(x=0.12,w=0.88)
c['question']='What is the pharmacist doing?'
c['answer']='The pharmacist is reading his prescription.'.split(' ')
c['answerVoice']='female'
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
