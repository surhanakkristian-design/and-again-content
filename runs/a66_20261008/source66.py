# A66: content/source.json (the 8 shown items as now in lib/lab58.json, after the quad-bike change) and
# verify/blind/blind.json (each story's 3 parts in a fixed shuffled order, labelled a/b/c; key kept in content/blind_key.json).
import json, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
SHOWN = [8055, 236, 7071, 8056, 62, 8039, 900001, 900002]
lab = {c['mediaId']: c for c in json.load(open(os.path.expanduser('~/Projects/and-again-a66/lib/lab58.json')))}
def row(r): return ' '.join(('[' + p['text'] + ']') if p.get('gap') else p['text'] for p in r)
src = {}
for i in SHOWN:
    c = lab[i]
    src[i] = {'level': c['level'], 'pos': c['pos'], 'keyWord': c['mindMap'].get('centre'),
              'ex1_tap_phrases': [t['phrase'] for t in c['taps']], 'ex2_nouns': [n['word'] for n in c['nouns']],
              'ex3_captions': c['captions'], 'ex3_scenes': c.get('scenes'),
              'ex4_map': [{'caption': n.get('caption'), 'chip': n.get('partner')} for n in c['mindMap']['nodes']],
              'ex4_rows': [row(r) for r in c['rows']], 'ex5_story': c['story'], 'ex5_bModels': c.get('storyModels')}
json.dump(src, open(f'{HERE}/content/source.json', 'w'), ensure_ascii=False, indent=1)
rng = random.Random(66); blind = {}; key = {}
perms = ['acb', 'bac', 'bca', 'cab', 'cba']
for i in SHOWN:
    p = perms[rng.randrange(5)]  # never the writer's order abc
    # shown letter L at position k holds part index ord(p[k])-97 ... shown a = original part p[0]
    shown = {L: lab[i]['story'][ord(p[k]) - 97] for k, L in enumerate('abc')}
    blind[i] = {'level': lab[i]['level'], 'keyWord': lab[i]['mindMap'].get('centre'), 'parts': shown}
    # the right order expressed in shown letters
    inv = {p[k]: L for k, L in enumerate('abc')}
    key[i] = ''.join(inv[o] for o in 'abc')
os.makedirs(f'{HERE}/verify/blind', exist_ok=True)
json.dump(blind, open(f'{HERE}/verify/blind/blind.json', 'w'), ensure_ascii=False, indent=1)
json.dump(key, open(f'{HERE}/content/blind_key.json', 'w'), indent=1)
print(key)
