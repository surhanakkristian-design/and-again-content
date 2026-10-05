import json, os
H = os.path.dirname(os.path.abspath(__file__)); p = f'{H}/hu.json'
t = json.load(open(p)); s = json.load(open(f'{H}/source.json'))
def fix(i, field, before, after, k=None):
    x = t[i]
    if k is None:
        assert x[field] == before, (i, x[field]); x[field] = after
    else:
        assert x[field][k] == before, (i, x[field][k]); x[field][k] = after
fix('374', 'phrases', 'az út mentén kocogni', 'az úton kocogni', 0)
fix('374', 'answer', 'Az út mentén kocog.', 'Az úton kocog.')
fix('380', 'answer', 'Egy metró forgókapuján halad át.', 'A metró forgókapuján halad át.')
fix('381', 'answer', 'A megijedt férfi egy szőlőszemet tart.', 'Az ijedt férfi egy szőlőszemet tart.')
fix('411', 'answer', 'Féltékenynek tűnik a másik táncosra.', 'Irigynek tűnik a másik táncosra.')
json.dump(t, open(p, 'w'), ensure_ascii=False, indent=1)
print(sum(3 + len(v['nouns']) + 2 for v in s.values()))
