import json, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hu.json')
t = json.load(open(p, encoding='utf-8'))
def sw(i, f, k, old, new):
    if k is None:
        assert t[i][f] == old, (i, f, t[i][f]); t[i][f] = new
    else:
        assert t[i][f][k] == old, (i, f, t[i][f][k]); t[i][f][k] = new
sw('572', 'answer', None, 'Krumplikat tesz egy vödörbe.', 'Krumplit tesz egy vödörbe.')
sw('591', 'answer', None, 'Ütéseket visz be a bokszzsákra.', 'Ütéseket mér a bokszzsákra.')
sw('594', 'nouns', 3, 'szőnyeg', 'matrac')
sw('606', 'answer', None, 'Palacsintákat esznek.', 'Palacsintát esznek.')
json.dump(t, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
