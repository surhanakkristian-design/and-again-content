import json, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ua.json')
t = json.load(open(p, encoding='utf-8'))
def sw(i, f, k, a, b):
    if k is None:
        assert t[i][f] == a, (i, f, t[i][f]); t[i][f] = b
    else:
        assert t[i][f][k] == a, (i, f, t[i][f][k]); t[i][f][k] = b
sw('163', 'phrases', 1, 'впускати свою їжу', 'упускати свою їжу')
sw('247', 'phrases', 0, 'впускати червоне яблуко', 'упускати червоне яблуко')
sw('247', 'answer', None, 'Він впускає червоне яблуко.', 'Він упускає червоне яблуко.')
sw('10', 'phrases', 1, 'сяяти яскраво-зеленим', 'сяяти яскраво-зеленим світлом')
sw('694', 'nouns', 0, 'куртка', 'кітель')
sw('100', 'phrases', 0, "зав'язувати свій черевик", 'зашнуровувати свій черевик')
sw('121', 'phrases', 0, 'спалити млинець', 'спалювати млинець')
json.dump(t, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
