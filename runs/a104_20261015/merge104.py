# A104: unique story names - writes the renamed Ex5 stories (content/<id>.json story5 example + guided) and their
# re-recorded audio (audio/voices104_<id>.json: audio, per-token times, duration) into lib/lab58.json.
import json, os
APP = os.path.expanduser('~/Projects/and-again/lib/lab58.json'); HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(APP))
for it in d:
    vid = str(it['mediaId'])
    if not os.path.exists(f'{HERE}/audio/voices104_{vid}.json') or it.get('lesson') != 'word': continue
    c = json.load(open(f'{HERE}/content/{vid}.json'))['story5']; v = json.load(open(f'{HERE}/audio/voices104_{vid}.json'))
    toks = sum(len(p.split()) if isinstance(p, str) else 1 for p in c['guided'])
    assert len(v['guided']['times']) == toks, (vid, len(v['guided']['times']), toks)
    s = it['story5']
    s['example'] = c['example']; s['guided'] = c['guided']
    s['audio'] = v['guided']['audio']; s['times'] = v['guided']['times']; s['duration'] = v['guided']['duration']
    print(vid, s['audio'].split('/')[-1], s['duration'], 's |', s['example'][:60])
json.dump(d, open(APP, 'w'), ensure_ascii=False, indent=1)
