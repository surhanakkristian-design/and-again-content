import json, sys, os
def build(txt, code):
    here = os.path.dirname(os.path.abspath(__file__))
    src = json.load(open(f'{here}/source.json'))
    out = {}; cur = None
    for line in txt.strip().splitlines():
        line = line.strip()
        if not line: continue
        tag, _, val = line.partition(' ')
        if tag.isdigit():
            cur = out.setdefault(tag, {}); continue
        val = val.strip()
        if tag == 'P': cur['phrases'] = [v.strip() for v in val.split(' ; ')]
        elif tag == 'N': cur['nouns'] = [v.strip() for v in val.split(' ; ')]
        elif tag == 'Q': cur['question'] = val
        elif tag == 'A': cur['answer'] = val
    res = {k: {f: out[k][f] for f in ('phrases', 'nouns', 'question', 'answer')} for k in src}
    json.dump(res, open(f'{here}/{code}.json', 'w'), ensure_ascii=False, indent=1)
