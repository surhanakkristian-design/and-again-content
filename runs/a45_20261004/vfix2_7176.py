import json
p='content/7176.json'; d=json.load(open(p))
d['taps'][1]['phrase']='to wear a collar'
d['question']='What is the young woman doing?'
d['answer']=['She','is','taking','off','her','hat.']
d['answerVoice']='female'
d['notes']+=' | Verifier 2: "sit next to the woman" also fits the man at the back (next to the knitting woman); goat phrase = collar; question moved to the young woman (two women visible).'
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
