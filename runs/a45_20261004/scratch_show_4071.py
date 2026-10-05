import json,sys
for i in sys.argv[1:]:
    try: c=json.load(open(f'content/{i}.json'))
    except Exception as e: print(i,'NOJSON',e); continue
    p=json.load(open(f'frames/{i}/packet.json'))
    print('==',i,p['keyWord'],p['level'],'even',p['evenId'],'sheets',p['sheets']);print(p['description']);print('TR',p['transcript'])
    print('default',c['defaultVoice'],'still',c['stillS'])
    for t in c['taps']:
        print(' ',t['phrase'],'|',t['target'],t['voice'])
        print('   ',' '.join(('%.1f:off'%k['t']) if k.get('off') else '%.1f:%.2f,%.2f,%.2f,%.2f'%(k['t'],k['x'],k['y'],k['w'],k['h']) for k in t['keys']))
    for n in c['nouns']: print('  N',n)
    print(c['question'],c['answer'],c['answerVoice']);print('notes',c.get('notes'))
