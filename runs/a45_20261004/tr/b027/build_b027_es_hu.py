import json, sys, importlib.util, os
code = sys.argv[1]; here = os.path.dirname(os.path.abspath(__file__))
src = json.load(open(f'{here}/source.json')); D = {}
for p in ('p1', 'p2'):
    spec = importlib.util.spec_from_file_location('m', f'{here}/{code}_b027_{p}.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); D.update(m.D)
out = {}
for i in src:
    ph, nn, q, a = D[i]
    out[i] = {"phrases": ph, "nouns": nn, "question": q, "answer": a}
json.dump(out, open(f'{here}/{code}.json', 'w'), ensure_ascii=False, indent=1)
