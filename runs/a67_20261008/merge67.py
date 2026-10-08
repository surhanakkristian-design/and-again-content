# A67: merges the reviewed content (content/final.json) and the verified row translations (tr/tr67_final2.json) into
# the app's lib/lab58.json: writeAt (exercise 3's picture without a prepared caption), ownRow (exercise 4's new row),
# fillDistractors (exercise 4's word box, Tips on), storyConnectors (exercise 5 page 2), tr.<lang>.ownRow.
import json, os
APP = os.path.expanduser('~/Projects/and-again-a67/lib/lab58.json')
HERE = os.path.dirname(os.path.abspath(__file__))
WRITE_AT = {8055: 1, 236: 0, 7071: 2, 8056: 0, 62: 2, 8039: 1, 900001: 0, 900002: 2}
final = json.load(open(f'{HERE}/content/final.json'))
tr = json.load(open(f'{HERE}/tr/tr67_final2.json'))
lab = json.load(open(APP))
n = 0
for c in lab:
    i = c['mediaId']
    if i not in WRITE_AT: continue
    f = final[str(i)]
    c['writeAt'] = WRITE_AT[i]
    c['ownRow'] = f['ownRow']['parts']
    c['fillDistractors'] = f['distractors']
    c['storyConnectors'] = f['connectors']
    for lang, text in tr[str(i)].items():
        c['tr'].setdefault(lang, {})['ownRow'] = text
    n += 1
json.dump(lab, open(APP, 'w'), ensure_ascii=False, indent=1)
print(n, 'items merged')
