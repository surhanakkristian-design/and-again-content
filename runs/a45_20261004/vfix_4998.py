import json
p='content/4998.json'; d=json.load(open(p))
for t in d['taps']:
  if t['target'] in ('the gates','the lanterns'): t['voice']=d['defaultVoice']
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
print([(t['target'],t['voice']) for t in d['taps']])
