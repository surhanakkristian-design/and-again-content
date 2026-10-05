import json,sys
for i in sys.argv[1:]:
    p=json.load(open(f'frames/{i}/packet.json')); 
    print('=====',i,p['keyWord'],p['level'],'even',p['evenId'],'dur',p['duration'],'sheets',p['sheets']); print(p['description']); print('TR:',p['transcript'])
    try: c=json.load(open(f'content/{i}.json'))
    except Exception as e: print('NO JSON',e); continue
    print('default',c['defaultVoice'])
    for t in c['taps']:
        print(' ',t['phrase'],'|',t['target'],'|',t['voice'])
        print('   '+' '.join((f"{k['t']}:off" if k.get('off') else f"{k['t']}:{k['x']},{k['y']},{k['w']},{k['h']}") for k in t['keys']))
    print('still',c['stillS'],c['nouns']); print(c['question'],c['answer'],c['answerVoice']); print('notes',c.get('notes'))
