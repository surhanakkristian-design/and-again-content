import json,sys
for i in sys.argv[1:]:
    try: c=json.load(open(f'content/{i}.json'))
    except Exception as e: print(i,'NOJSON',e); continue
    p=json.load(open(f'frames/{i}/packet.json'))
    print('==',i,p['level'],p['keyWord'],'even',p['evenId'],'sheets',p['sheets']); print(p['description']); print('TR',p['transcript'])
    print('default',c['defaultVoice'])
    for t in c['taps']:
        print(' TAP',t['phrase'],'|',t['target'],t['voice'])
        print('   ',' '.join('%g:off'%k['t'] if k.get('off') else '%g:%.2f,%.2f,%.2f,%.2f'%(k['t'],k['x'],k['y'],k['w'],k['h']) for k in t['keys']))
    print(' still',c['stillS'],c['nouns']); print(' Q',c['question'],c['answer'],c['answerVoice']); print(' notes',c.get('notes'))
