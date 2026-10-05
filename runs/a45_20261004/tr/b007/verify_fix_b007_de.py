import json, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'de.json')
t = json.load(open(p, encoding='utf-8'))
def fix(i, field, idx, before, after):
    x = t[i]
    if idx is None:
        assert x[field] == before, (i, field, x[field]); x[field] = after
    else:
        assert x[field][idx] == before, (i, field, x[field][idx]); x[field][idx] = after
fix('505', 'phrases', 0, 'eine Nuss öffnen', 'eine Nuss knacken')
fix('505', 'answer', None, 'Er öffnet eine Nuss.', 'Er knackt eine Nuss.')
fix('520', 'phrases', 0, 'ein Kanu paddeln', 'in einem Kanu paddeln')
fix('520', 'answer', None, 'Sie paddelt ein Kanu an den Klippen vorbei.', 'Sie paddelt in einem Kanu an den Klippen vorbei.')
fix('530', 'phrases', 0, 'einen roten Flügel öffnen', 'einen roten Flügel ausbreiten')
fix('545', 'answer', None, 'Sie jonglieren bei einer Straßenvorstellung mit Keulen.', 'Sie jonglieren bei einer Straßenvorführung mit Keulen.')
json.dump(t, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
