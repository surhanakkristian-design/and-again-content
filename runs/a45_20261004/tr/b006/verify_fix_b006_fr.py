import json, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fr.json')
t = json.load(open(p, encoding='utf-8'))
def fix(i, field, idx, before, after):
    if idx is None:
        assert t[i][field] == before, (i, t[i][field]); t[i][field] = after
    else:
        assert t[i][field][idx] == before, (i, t[i][field][idx]); t[i][field][idx] = after
fix('359', 'phrases', 1, 'manger quelques graines', 'manger des graines')
fix('397', 'phrases', 0, 'scruter à travers des jumelles', 'regarder à travers des jumelles')
fix('414', 'question', None, 'Que fait la femme devant ?', 'Que fait la femme de devant ?')
fix('423', 'phrases', 0, 'souffler un baiser', 'envoyer un baiser')
json.dump(t, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
