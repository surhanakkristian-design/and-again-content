import json, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cz.json')
t = json.load(open(p, encoding='utf-8'))
def rep(i, field, idx, before, after):
    if idx is None:
        assert t[i][field] == before, (i, field, t[i][field]); t[i][field] = after
    else:
        assert t[i][field][idx] == before, (i, field, t[i][field][idx]); t[i][field][idx] = after
rep('6949', 'phrases', 2, 'pít z šálku', 'pít ze šálku')
rep('4210', 'phrases', 0, 'svírat dvě dřevěná dřívka', 'svírat dvě dřevěné tyčinky')
rep('6908', 'phrases', 1, 'toulat se kolem auta', 'loudat se kolem auta')
rep('6908', 'answer', None, 'Toulá se kolem kabrioletu.', 'Loudá se kolem kabrioletu.')
rep('20', 'phrases', 1, 'ležet dokořán otevřená', 'ležet doširoka rozevřená')
json.dump(t, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
