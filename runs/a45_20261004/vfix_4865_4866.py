import json
p='content/4865.json'; c=json.load(open(p))
t=c['taps'][1]
t['phrase']='to give a thumbs-up'; t['target']='the photographer'; t['voice']='male'
t['keys']=json.loads(json.dumps(c['taps'][0]['keys']))
c['notes']=(c.get('notes') or '')+' | VERIFIER: cyclist phrase replaced (visible in one 0.5 s frame only, not tappable); phrase 2 = thumbs-up by the photographer at 9.5-10 s.'
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
p='content/4866.json'; c=json.load(open(p))
c['nouns']=[n for n in c['nouns'] if n['word']!='trees']
c['notes']=(c.get('notes') or '')+' | VERIFIER: removed "trees" (tiny distant clump on the horizon, not clearly identifiable).'
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
