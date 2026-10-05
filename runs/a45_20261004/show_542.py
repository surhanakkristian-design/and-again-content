import json,sys
for i in sys.argv[1:]:
    p=json.load(open(f'frames/{i}/packet.json')); 
    print('==',i,{k:p[k] for k in p if k!='times'}, 'ntimes',len(p['times']))
    try: c=json.load(open(f'content/{i}.json'))
    except Exception as e: print('NO JSON',e); continue
    print({k:c[k] for k in c if k not in('taps','nouns')})
    for t in c['taps']:
        print(' ',t['phrase'],'|',t['target'],'|',t['voice'])
        print('   ',' '.join(('%g:off'%k['t']) if k.get('off') else '%g:%.2f,%.2f,%.2f,%.2f'%(k['t'],k['x'],k['y'],k['w'],k['h']) for k in t['keys']))
    for n in c['nouns']: print('  N',n)
