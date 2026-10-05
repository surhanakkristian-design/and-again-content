# A55: checks tr/<lang>/<native>.json against tr/source_<lang>.json (every id, counts, caption keys, no empty text).
#   python3 tr_check.py <lang> <native>
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
lang, nat = sys.argv[1], sys.argv[2]
src = json.load(open(f'{HERE}/tr/source_{lang}.json'))
try: t = json.load(open(f'{HERE}/tr/{lang}/{nat}.json'))
except Exception as x: sys.exit(f'{lang}/{nat}: not valid JSON: {x}')
e = []
if nat == lang: e.append('a learning language never gets a translation into itself')
for vid, s in src.items():
    x = t.get(vid)
    if not x: e.append(f'{vid}: missing'); continue
    if len(x.get('phrases', [])) != len(s['phrases']) or not all(x['phrases']): e.append(f'{vid}: phrases')
    if len(x.get('nouns', [])) != len(s['nouns']) or not all(x['nouns']): e.append(f'{vid}: nouns')
    if not x.get('question') or not x.get('answer'): e.append(f'{vid}: question / answer')
    if set((x.get('captions') or {}).keys()) != set(s['captions']) or not all((x.get('captions') or {}).values()): e.append(f'{vid}: captions (keys must be the source captions)')
    if len(x.get('recall', [])) != len(s['recall']) or not all(x['recall']): e.append(f'{vid}: recall')
extra = set(t) - set(src)
if extra: e.append(f'ids not in the source: {sorted(extra)}')
print(f'{lang}/{nat}: ' + ('ok, ' + str(len(src)) + ' ids' if not e else 'ERRORS: ' + '; '.join(e))); sys.exit(1 if e else 0)
