import json, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'es.json')
t = json.load(open(p, encoding='utf-8'))
fixes = [('4103', 0, 'asomarse por un lado de una pantalla', 'asomarse por un lado de una mampara'),
         ('4104', 1, 'ponerse con la cara roja', 'ponerse colorado'),
         ('4144', 0, 'asomarse de una caja', 'asomarse desde una caja'),
         ('4165', 1, 'salir de una curva', 'aparecer tras una curva')]
for i, k, a, b in fixes:
    assert t[i]['phrases'][k] == a, (i, t[i]['phrases'][k]); t[i]['phrases'][k] = b
json.dump(t, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
