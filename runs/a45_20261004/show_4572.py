import json,sys,os
for i in (4572,4573,4575,4576):
    p=json.load(open(f'frames/{i}/packet.json'))
    print('==',i,p['keyWord'],p['level'],'even',p['evenId'],'dur',p['duration'],'sheets',p['sheets'])
    print(p['description']); print('TR',p['transcript'])
    if not os.path.exists(f'content/{i}.json'): print('SKIP',open(f'content/{i}.skip').read()); continue
    c=json.load(open(f'content/{i}.json'))
    print('default',c['defaultVoice'])
    for t in c['taps']:
        print(' ',t['phrase'],'|',t['target'],'|',t['voice'])
        print('   ',' '.join(f"{k['t']}:off" if k.get('off') else f"{k['t']}:{k['x']},{k['y']},{k['w']},{k['h']}" for k in t['keys']))
    print('still',c['stillS'],c['nouns'])
    print(c['question'],c['answer'],c['answerVoice'])
    print('notes',c.get('notes'))
