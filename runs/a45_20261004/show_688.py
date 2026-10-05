import json,sys
for i in sys.argv[1:]:
    p=json.load(open(f'frames/{i}/packet.json'))
    print('=====',i,p['keyWord'],p['level'],'even',p['evenId'],'|',p['description'],'| TR:',p['transcript'],'| n times',len(p['times']),'sheets',p['sheets'])
    try: c=json.load(open(f'content/{i}.json'))
    except Exception as e: print('NO JSON',e); continue
    print('default',c['defaultVoice'],'stillS',c['stillS'])
    for t in c['taps']:
        print(' TAP',t['phrase'],'|',t['target'],'|',t['voice'])
        print('   ',' '.join(('%g:off'%k['t']) if k.get('off') else '%g:%.2f,%.2f,%.2f,%.2f'%(k['t'],k['x'],k['y'],k['w'],k['h']) for k in t['keys']))
    for n in c['nouns']: print(' NOUN',n)
    print(' Q',c['question'],'| A',c['answer'],c['answerVoice'])
    print(' notes',c.get('notes'))
