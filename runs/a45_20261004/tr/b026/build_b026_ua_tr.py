import json, sys, importlib.util
code = sys.argv[1]
D = {}
for p in ('p1', 'p2'):
    spec = importlib.util.spec_from_file_location('m', f'gen_b026_{code}_{p}.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); D.update(m.D)
src = json.load(open('source.json'))
out = {}
for i in src:
    ph, no, q, a = D[i]
    out[i] = {"phrases": ph, "nouns": no, "question": q, "answer": a}
json.dump(out, open(f'{code}.json', 'w'), ensure_ascii=False, indent=1)
