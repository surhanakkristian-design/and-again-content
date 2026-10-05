# usage: python3 gen_7183_7184_7185_7186_lib.py <id>  (reads spec_<id>.json, boxes as [x1,y1,x2,y2] or null)
import json, sys
vid = sys.argv[1]
s = json.load(open(f'spec_{vid}.json'))
times = json.load(open(f'frames/{vid}/packet.json'))['times']
taps = []
for p in s['taps']:
    keys = []
    for t, b in zip(times, s['boxes'][p['target']]):
        if b is None: keys.append({'t': t, 'off': True})
        else:
            x1, y1, x2, y2 = b
            keys.append({'t': t, 'x': round(x1, 2), 'y': round(y1, 2), 'w': round(x2 - x1, 2), 'h': round(y2 - y1, 2)})
    taps.append({'phrase': p['phrase'], 'target': p['target'], 'voice': p['voice'], 'keys': keys})
out = {'mediaId': int(vid), 'level': s['level'], 'keyWord': s['keyWord'], 'defaultVoice': s['defaultVoice'], 'taps': taps,
       'stillS': s['stillS'], 'nouns': s['nouns'], 'question': s['question'], 'answer': s['answer'].split(' '),
       'answerVoice': s['answerVoice'], 'notes': s['notes']}
json.dump(out, open(f'content/{vid}.json', 'w'), indent=1, ensure_ascii=False)
