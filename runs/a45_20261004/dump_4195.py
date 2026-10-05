import json,sys
for i in sys.argv[1:]:
    p=json.load(open(f'frames/{i}/packet.json'))
    print('==',i,p['keyWord'],p['level'],'even',p['evenId'],'sheets',p['sheets']);print(p['description']);print('TR:',p['transcript'])
    try:c=json.load(open(f'content/{i}.json'))
    except Exception as e:
        print('NOJSON',e);continue
    print('default',c['defaultVoice'])
    for t in c['taps']:
        print(' TAP',t['phrase'],'|',t['target'],t['voice'])
        for k in t['keys']:
            print('   ',k['t'],'off' if k.get('off') else (k['x'],k['y'],k['w'],k['h']))
    print(' still',c['stillS']);
    for n in c['nouns']:print(' N',n)
    print(' Q',c['question'],c['answer'],c['answerVoice']);print(' notes',c.get('notes'))
