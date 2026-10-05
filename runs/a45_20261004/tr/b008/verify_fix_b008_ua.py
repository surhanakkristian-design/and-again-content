import json, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ua.json')
t = json.load(open(p, encoding='utf-8'))
assert t['576']['phrases'][1] == 'складати долоні разом'; t['576']['phrases'][1] = 'складати долоні'
assert t['691']['answer'] == 'Він охороняє машину з палицею.'; t['691']['answer'] = 'Він із палицею охороняє машину.'
json.dump(t, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
