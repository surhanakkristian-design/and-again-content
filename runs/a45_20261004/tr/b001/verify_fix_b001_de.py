import json, os
H = os.path.dirname(os.path.abspath(__file__)); p = f'{H}/de.json'
d = json.load(open(p))
def fix(i, field, idx, before, after):
    if idx is None:
        assert d[i][field] == before, (i, d[i][field]); d[i][field] = after
    else:
        assert d[i][field][idx] == before, (i, d[i][field][idx]); d[i][field][idx] = after
fix('4658', 'answer', None, 'Sie fährt ein Auto am Meer.', 'Sie fährt am Meer Auto.')
fix('122', 'phrases', 1, 'einen Einkaufswagen halten', 'einen Einkaufstrolley halten')
fix('449', 'phrases', 1, 'sich beide Ohren halten', 'die Hände an beide Ohren halten')
json.dump(d, open(p, 'w'), ensure_ascii=False, indent=1)
print(sum(3 + len(v['nouns']) + 2 for v in d.values()))
